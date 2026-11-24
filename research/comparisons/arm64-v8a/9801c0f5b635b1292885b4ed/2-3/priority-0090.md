# v16.0.1 → v16.0.2 · 最優先の変更候補 (90)

[一覧の目次](README.md)

<a id="compare-114dad94b5830ebeb4aa95d85d30584e"></a>

### [`00c38914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md) → [`00c389b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c389b0.md) FUN_00c389b0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38a10",
      "incomplete_value": true,
      "site": "00c38a14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38974",
      "incomplete_value": true,
      "site": "00c38978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
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
      "definition_site": "00c38a00",
      "incomplete_value": true,
      "site": "00c38a14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38964",
      "incomplete_value": true,
      "site": "00c38978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c389fc",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a00",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a00",
      "PARAM",
      [
        "storage",
        "00c969e8",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c389fc",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a00",
      "READ",
      [
        "storage",
        "00c9bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00c38a00",
      "PARAM",
      [
        "storage",
        "00c96ab8",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md#insn-00c38978) · [`00c38940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md#insn-00c38940) · [`00c38960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38914.md#insn-00c38960)
- 新版 `00c38a14`（命令位置の公開資料なし） · `00c389dc`（命令位置の公開資料なし） · `00c389fc`（命令位置の公開資料なし）

~~~diff
- 00c38978 ["INT_ADD", "register:40f0:8", ["const:c38978:8", "const:4:8"]]
- 00c38978 ["CALL", null, ["callee:00c586e0:8"]]
+ 00c38a14 ["INT_ADD", "register:40f0:8", ["const:c38a14:8", "const:4:8"]]
+ 00c38a14 ["CALL", null, ["callee:00c586e0:8"]]
- 00c38978 bytes 267f0094
+ 00c38a14 bytes 337f0094
- 00c38940 ["INT_ADD", "register:40f0:8", ["const:c38940:8", "const:4:8"]]
- 00c38940 ["CALL", null, ["callee:00c5b920:8"]]
+ 00c389dc ["INT_ADD", "register:40f0:8", ["const:c389dc:8", "const:4:8"]]
+ 00c389dc ["CALL", null, ["callee:00c5b920:8"]]
- 00c38940 bytes c48b0094
+ 00c389dc bytes d18b0094
- 00c38960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
- 00c38960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c389fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00c389fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c38960 bytes 083d47f9
+ 00c389fc bytes 08a547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28ab724ddf11eac64dbd734fe9086a2e"></a>

### [`00c389c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md) → [`00c38a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38a5c.md) FUN_00c38a5c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c38c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38c7c.md) [`00c38d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38d70.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c38d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38d18.md) [`00c38e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38e0c.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 89.14% / 新版 89.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 11件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c38a88",
      "incomplete_value": true,
      "site": "00c38a8c",
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
    "old": {
      "definition_site": "00c389ec",
      "incomplete_value": true,
      "site": "00c389f0",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c38b9c",
      "incomplete_value": true,
      "site": "00c38ba0",
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
    "old": {
      "definition_site": "00c38b00",
      "incomplete_value": true,
      "site": "00c38b04",
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
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38aec",
      "incomplete_value": true,
      "site": "00c38af8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38a50",
      "incomplete_value": true,
      "site": "00c38a5c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:e78:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c38a84",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38aec",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38aec",
      "PARAM",
      [
        "storage",
        "00c969b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38a84",
      "READ",
      [
        "storage",
        "00c9bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00c38aec",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c38aec",
      "PARAM",
      [
        "storage",
        "00c96a88",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md#insn-00c38a5c) · [`00c38a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md#insn-00c38a8c) · [`00c38a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c389c0.md#insn-00c38a94)
- 新版 `00c38af8`（命令位置の公開資料なし） · `00c38b28`（命令位置の公開資料なし） · `00c38b30`（命令位置の公開資料なし）

~~~diff
- 00c38a5c ["INT_ADD", "register:40f0:8", ["const:c38a5c:8", "const:4:8"]]
- 00c38a5c ["CALL", null, ["callee:00c586e0:8"]]
+ 00c38af8 ["INT_ADD", "register:40f0:8", ["const:c38af8:8", "const:4:8"]]
+ 00c38af8 ["CALL", null, ["callee:00c586e0:8"]]
- 00c38a5c bytes ed7e0094
+ 00c38af8 bytes fa7e0094
- 00c38a8c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e98:8"]]
- 00c38a8c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38b28 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:f68:8"]]
+ 00c38b28 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00c38a8c bytes 424c47f9
+ 00c38b28 bytes 42b447f9
- 00c38a94 ["INT_ADD", "register:40f0:8", ["const:c38a94:8", "const:4:8"]]
- 00c38a94 ["CALL", null, ["callee:00c586e0:8"]]
+ 00c38b30 ["INT_ADD", "register:40f0:8", ["const:c38b30:8", "const:4:8"]]
+ 00c38b30 ["CALL", null, ["callee:00c586e0:8"]]
- 00c38a94 bytes df7e0094
+ 00c38b30 bytes ec7e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9671aae7b4d0c61f9da69e53570699b"></a>

### [`00c38e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md) → [`00c38eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38eac.md) FUN_00c38eac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.81% / 新版 86.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c38ed0",
      "incomplete_value": true,
      "site": "00c38ed4",
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
                "register:40a8:8"
              ],
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
    "old": {
      "definition_site": "00c38e34",
      "incomplete_value": true,
      "site": "00c38e38",
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
                "register:40a8:8"
              ],
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38f1c",
      "incomplete_value": true,
      "site": "00c38f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38e80",
      "incomplete_value": true,
      "site": "00c38e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
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
      "definition_site": "00c38f28",
      "incomplete_value": true,
      "site": "00c38f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38e8c",
      "incomplete_value": true,
      "site": "00c38e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c38ecc",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38f1c",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38f1c",
      "PARAM",
      [
        "storage",
        "00c969b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38ecc",
      "READ",
      [
        "storage",
        "00c9bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00c38f1c",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c38f1c",
      "PARAM",
      [
        "storage",
        "00c96a88",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md#insn-00c38e5c) · [`00c38e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md#insn-00c38e90) · [`00c38ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c38e10.md#insn-00c38ec0)
- 新版 `00c38ef8`（命令位置の公開資料なし） · `00c38f2c`（命令位置の公開資料なし） · `00c38f5c`（命令位置の公開資料なし）

~~~diff
- 00c38e5c ["INT_ADD", "register:40f0:8", ["const:c38e5c:8", "const:4:8"]]
- 00c38e5c ["CALL", null, ["callee:00c5b920:8"]]
+ 00c38ef8 ["INT_ADD", "register:40f0:8", ["const:c38ef8:8", "const:4:8"]]
+ 00c38ef8 ["CALL", null, ["callee:00c5b920:8"]]
- 00c38e5c bytes 7d8a0094
+ 00c38ef8 bytes 8a8a0094
- 00c38e90 ["INT_ADD", "register:40f0:8", ["const:c38e90:8", "const:4:8"]]
- 00c38e90 ["CALL", null, ["callee:00c586e0:8"]]
+ 00c38f2c ["INT_ADD", "register:40f0:8", ["const:c38f2c:8", "const:4:8"]]
+ 00c38f2c ["CALL", null, ["callee:00c586e0:8"]]
- 00c38e90 bytes e07d0094
+ 00c38f2c bytes ed7d0094
- 00c38ec0 ["INT_ADD", "register:40f0:8", ["const:c38ec0:8", "const:4:8"]]
- 00c38ec0 ["CALL", null, ["callee:00c586e0:8"]]
+ 00c38f5c ["INT_ADD", "register:40f0:8", ["const:c38f5c:8", "const:4:8"]]
+ 00c38f5c ["CALL", null, ["callee:00c586e0:8"]]
- 00c38ec0 bytes d47d0094
+ 00c38f5c bytes e17d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb7410dd910c2e1ff45c48747a2b75c4"></a>

### [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) → [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) __cxa_demangle

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5edf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5edf0.md) · 呼出先 10件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5eec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eec0.md) · 呼出先 10件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c39e64",
      "incomplete_value": false,
      "site": "00c39e64",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39dc8",
      "incomplete_value": false,
      "site": "00c39dc8",
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
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39fbc",
      "incomplete_value": false,
      "site": "00c39fc8",
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
            "const:dff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39f20",
      "incomplete_value": false,
      "site": "00c39f2c",
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
            "const:e53:8"
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
      "definition_site": "00c3a0a4",
      "incomplete_value": false,
      "site": "00c3a0bc",
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
    "old": {
      "definition_site": "00c3a008",
      "incomplete_value": false,
      "site": "00c3a020",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c39e64",
      "DATA",
      [
        "storage",
        "00c997e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c39fbc",
      "PARAM",
      [
        "storage",
        "002b9e53",
        null,
        "string"
      ]
    ],
    [
      "00c3a0a4",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c39e64",
      "DATA",
      [
        "storage",
        "00c998b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c39fbc",
      "PARAM",
      [
        "storage",
        "002b9dff",
        null,
        "string"
      ]
    ],
    [
      "00c3a0a4",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c39f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md#insn-00c39f2c) · [`00c3a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md#insn-00c3a020) · [`00c39adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md#insn-00c39adc)
- 新版 `00c39fc8`（命令位置の公開資料なし） · `00c3a0bc`（命令位置の公開資料なし） · `00c39b78`（命令位置の公開資料なし）

~~~diff
- 00c39f2c ["INT_ADD", "register:40f0:8", ["const:c39f2c:8", "const:4:8"]]
- 00c39f2c ["CALL", null, ["callee:00c3acb4:8"]]
+ 00c39fc8 ["INT_ADD", "register:40f0:8", ["const:c39fc8:8", "const:4:8"]]
+ 00c39fc8 ["CALL", null, ["callee:00c3acb4:8"]]
- 00c39f2c bytes 3b030094
+ 00c39fc8 bytes 3b030094
- 00c3a020 ["INT_ADD", "register:40f0:8", ["const:c3a020:8", "const:4:8"]]
- 00c3a020 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c3a0bc ["INT_ADD", "register:40f0:8", ["const:c3a0bc:8", "const:4:8"]]
+ 00c3a0bc ["CALL", null, ["callee:00c380a8:8"]]
- 00c3a020 bytes fbf7ff97
+ 00c3a0bc bytes fbf7ff97
- 00c39adc ["INT_ADD", "register:40f0:8", ["const:c39adc:8", "const:4:8"]]
- 00c39adc ["CALL", null, ["callee:00c580b0:8"]]
+ 00c39b78 ["INT_ADD", "register:40f0:8", ["const:c39b78:8", "const:4:8"]]
+ 00c39b78 ["CALL", null, ["callee:00c580b0:8"]]
- 00c39adc bytes 41790094
+ 00c39b78 bytes 4e790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b87248956e89048682da8299d78672c"></a>

### [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) → [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) FUN_00c3a214

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 31件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c3ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md)
- 新版 呼出元 5件 [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 31件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c3acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3a43c",
      "incomplete_value": false,
      "site": "00c3a43c",
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
    "old": {
      "definition_site": "00c3a3a0",
      "incomplete_value": false,
      "site": "00c3a3a0",
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
            "const:550:8"
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
      "definition_site": "00c3a880",
      "incomplete_value": false,
      "site": "00c3a880",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a7e4",
      "incomplete_value": false,
      "site": "00c3a7e4",
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
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3aa84",
      "incomplete_value": false,
      "site": "00c3aa90",
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
            "const:5f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a9e8",
      "incomplete_value": false,
      "site": "00c3a9f4",
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
            "const:1f:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3a43c",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a6e0",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a704",
      "DATA",
      [
        "storage",
        "002b090e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3a43c",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a6e0",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3a704",
      "DATA",
      [
        "storage",
        "002b08b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3a9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md#insn-00c3a9f4) · [`00c3ab3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md#insn-00c3ab3c) · [`00c3a1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md#insn-00c3a1a8)
- 新版 `00c3aa90`（命令位置の公開資料なし） · `00c3abd8`（命令位置の公開資料なし） · `00c3a244`（命令位置の公開資料なし）

~~~diff
- 00c3a9f4 ["INT_ADD", "register:40f0:8", ["const:c3a9f4:8", "const:4:8"]]
- 00c3a9f4 ["CALL", null, ["callee:00c3acb4:8"]]
+ 00c3aa90 ["INT_ADD", "register:40f0:8", ["const:c3aa90:8", "const:4:8"]]
+ 00c3aa90 ["CALL", null, ["callee:00c3acb4:8"]]
- 00c3a9f4 bytes 89000094
+ 00c3aa90 bytes 89000094
- 00c3ab3c ["INT_ADD", "register:40f0:8", ["const:c3ab3c:8", "const:4:8"]]
- 00c3ab3c ["CALL", null, ["callee:00c380a8:8"]]
+ 00c3abd8 ["INT_ADD", "register:40f0:8", ["const:c3abd8:8", "const:4:8"]]
+ 00c3abd8 ["CALL", null, ["callee:00c380a8:8"]]
- 00c3ab3c bytes 34f5ff97
+ 00c3abd8 bytes 34f5ff97
- 00c3a1a8 ["INT_ADD", "register:40f0:8", ["const:c3a1a8:8", "const:4:8"]]
- 00c3a1a8 ["CALL", null, ["callee:00c3c100:8"]]
+ 00c3a244 ["INT_ADD", "register:40f0:8", ["const:c3a244:8", "const:4:8"]]
+ 00c3a244 ["CALL", null, ["callee:00c3c100:8"]]
- 00c3a1a8 bytes af070094
+ 00c3a244 bytes af070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06b95c1c0d03121ae7ca0bf575a8ce1c"></a>

### [`00c3ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md) → [`00c3acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md) FUN_00c3acb4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ad24",
      "incomplete_value": false,
      "site": "00c3ad24",
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
    "old": {
      "definition_site": "00c3ac88",
      "incomplete_value": false,
      "site": "00c3ac88",
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
            "const:550:8"
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
      "00c3ad24",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3ad24",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md#insn-00c3ac50) · [`00c3ac78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md#insn-00c3ac78) · [`00c3ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ac18.md#insn-00c3ac80)
- 新版 `00c3acec`（命令位置の公開資料なし） · `00c3ad14`（命令位置の公開資料なし） · `00c3ad1c`（命令位置の公開資料なし）

~~~diff
- 00c3ac50 ["INT_ADD", "register:40f0:8", ["const:c3ac50:8", "const:4:8"]]
- 00c3ac50 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3acec ["INT_ADD", "register:40f0:8", ["const:c3acec:8", "const:4:8"]]
+ 00c3acec ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3ac50 bytes f47c0094
+ 00c3acec bytes 017d0094
- 00c3ac78 ["INT_ADD", "register:40f0:8", ["const:c3ac78:8", "const:4:8"]]
- 00c3ac78 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c3ad14 ["INT_ADD", "register:40f0:8", ["const:c3ad14:8", "const:4:8"]]
+ 00c3ad14 ["CALL", null, ["callee:00c580b0:8"]]
- 00c3ac78 bytes da740094
+ 00c3ad14 bytes e7740094
- 00c3ac80 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3ac80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ac80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ac80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ad1c ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3ad1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ad1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ad1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ac80 bytes 08411591
+ 00c3ad1c bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-211f6ba64d3f35217ee792c55bed08f2"></a>

### [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) → [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) FUN_00c3ad68

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`00c39a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c39/00c39a80.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 38件 [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md) [`00c3e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md)
- 新版 呼出元 15件 [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 38件 [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md) [`00c3e278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 21件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3af4c",
      "incomplete_value": false,
      "site": "00c3af4c",
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
    "old": {
      "definition_site": "00c3aeb0",
      "incomplete_value": false,
      "site": "00c3aeb0",
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
            "const:640:8"
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
      "definition_site": "00c3afbc",
      "incomplete_value": false,
      "site": "00c3afbc",
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
    "old": {
      "definition_site": "00c3af20",
      "incomplete_value": false,
      "site": "00c3af20",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3b02c",
      "incomplete_value": false,
      "site": "00c3b02c",
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
    "old": {
      "definition_site": "00c3af90",
      "incomplete_value": false,
      "site": "00c3af90",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3adb4",
      "DATA",
      [
        "storage",
        "003129e0",
        "switchD_00c3ad20::switchdataD_003129e0",
        "ushort"
      ]
    ],
    [
      "00c3aecc",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3af4c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3adb4",
      "DATA",
      [
        "storage",
        "00312a20",
        "switchD_00c3adbc::switchdataD_00312a20",
        "ushort"
      ]
    ],
    [
      "00c3aecc",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3af4c",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3b050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md#insn-00c3b050) · [`00c3b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md#insn-00c3b8d4) · [`00c3bc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md#insn-00c3bc4c)
- 新版 `00c3b0ec`（命令位置の公開資料なし） · `00c3b970`（命令位置の公開資料なし） · `00c3bce8`（命令位置の公開資料なし）

~~~diff
- 00c3b050 ["INT_ADD", "register:40f0:8", ["const:c3b050:8", "const:4:8"]]
- 00c3b050 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3b0ec ["INT_ADD", "register:40f0:8", ["const:c3b0ec:8", "const:4:8"]]
+ 00c3b0ec ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3b050 bytes f47b0094
+ 00c3b0ec bytes 017c0094
- 00c3b8d4 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3b8d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3b8d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3b8d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3b970 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3b970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3b970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3b970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3b8d4 bytes 08011991
+ 00c3b970 bytes 08411c91
- 00c3bc4c ["INT_ADD", "register:40f0:8", ["const:c3bc4c:8", "const:4:8"]]
- 00c3bc4c ["CALL", null, ["callee:00c3cd04:8"]]
+ 00c3bce8 ["INT_ADD", "register:40f0:8", ["const:c3bce8:8", "const:4:8"]]
+ 00c3bce8 ["CALL", null, ["callee:00c3cd04:8"]]
- 00c3bc4c bytes 07040094
+ 00c3bce8 bytes 07040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56052fa08105371e10b61609805cfda5"></a>

### [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) → [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) FUN_00c3c2a8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c429c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md) · 呼出先 19件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c3c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c064.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d030.md)
- 新版 呼出元 7件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c42a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md) · 呼出先 19件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c3c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3d0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3c6a4",
      "incomplete_value": false,
      "site": "00c3c6a4",
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
    "old": {
      "definition_site": "00c3c608",
      "incomplete_value": false,
      "site": "00c3c608",
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
            "const:640:8"
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
      "definition_site": "00c3c6c8",
      "incomplete_value": false,
      "site": "00c3c6c8",
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
    "old": {
      "definition_site": "00c3c62c",
      "incomplete_value": false,
      "site": "00c3c62c",
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
            "const:d84:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3c990",
      "incomplete_value": false,
      "site": "00c3c990",
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
    "old": {
      "definition_site": "00c3c8f4",
      "incomplete_value": false,
      "site": "00c3c8f4",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3c408",
      "PARAM",
      [
        "storage",
        "002b18fa",
        null,
        "string"
      ]
    ],
    [
      "00c3c588",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3c6a4",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3c408",
      "PARAM",
      [
        "storage",
        "002b189e",
        null,
        "string"
      ]
    ],
    [
      "00c3c588",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3c6a4",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md#insn-00c3c374) · [`00c3c858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md#insn-00c3c858) · [`00c3c29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md#insn-00c3c29c)
- 新版 `00c3c410`（命令位置の公開資料なし） · `00c3c8f4`（命令位置の公開資料なし） · `00c3c338`（命令位置の公開資料なし）

~~~diff
- 00c3c374 ["INT_ADD", "register:40f0:8", ["const:c3c374:8", "const:4:8"]]
- 00c3c374 ["CALL", null, ["callee:00c4d18c:8"]]
+ 00c3c410 ["INT_ADD", "register:40f0:8", ["const:c3c410:8", "const:4:8"]]
+ 00c3c410 ["CALL", null, ["callee:00c4d18c:8"]]
- 00c3c374 bytes 5f430094
+ 00c3c410 bytes 5f430094
- 00c3c858 ["INT_ADD", "register:40f0:8", ["const:c3c858:8", "const:4:8"]]
- 00c3c858 ["CALL", null, ["callee:00c3e660:8"]]
+ 00c3c8f4 ["INT_ADD", "register:40f0:8", ["const:c3c8f4:8", "const:4:8"]]
+ 00c3c8f4 ["CALL", null, ["callee:00c3e660:8"]]
- 00c3c858 bytes 5b070094
+ 00c3c8f4 bytes 5b070094
- 00c3c29c ["INT_ADD", "register:40f0:8", ["const:c3c29c:8", "const:4:8"]]
- 00c3c29c ["CALL", null, ["callee:00c3e4f0:8"]]
+ 00c3c338 ["INT_ADD", "register:40f0:8", ["const:c3c338:8", "const:4:8"]]
+ 00c3c338 ["CALL", null, ["callee:00c3e4f0:8"]]
- 00c3c29c bytes 6e080094
+ 00c3c338 bytes 6e080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e479cad09bb13c653e7d32cf69a085b1"></a>

### [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) → [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) FUN_00c3c9dc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 13件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md)
- 新版 呼出元 4件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 13件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3cc54",
      "incomplete_value": false,
      "site": "00c3cc58",
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
            "const:232:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cbb8",
      "incomplete_value": false,
      "site": "00c3cbbc",
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
            "const:28e:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3cc0c",
      "DATA",
      [
        "storage",
        "00c995b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cc0c",
      "DATA",
      [
        "storage",
        "00c99620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cc54",
      "PARAM",
      [
        "storage",
        "002a528e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3cc0c",
      "DATA",
      [
        "storage",
        "00c99680",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cc0c",
      "DATA",
      [
        "storage",
        "00c996f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cc54",
      "PARAM",
      [
        "storage",
        "002a5232",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md#insn-00c3cbbc) · [`00c3c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md#insn-00c3c9b0) · [`00c3c9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md#insn-00c3c9d8)
- 新版 `00c3cc58`（命令位置の公開資料なし） · `00c3ca4c`（命令位置の公開資料なし） · `00c3ca74`（命令位置の公開資料なし）

~~~diff
- 00c3cbbc ["INT_ADD", "register:40f0:8", ["const:c3cbbc:8", "const:4:8"]]
- 00c3cbbc ["CALL", null, ["callee:00c580a0:8"]]
+ 00c3cc58 ["INT_ADD", "register:40f0:8", ["const:c3cc58:8", "const:4:8"]]
+ 00c3cc58 ["CALL", null, ["callee:00c580a0:8"]]
- 00c3cbbc bytes 056d0094
+ 00c3cc58 bytes 126d0094
- 00c3c9b0 ["INT_ADD", "register:40f0:8", ["const:c3c9b0:8", "const:4:8"]]
- 00c3c9b0 ["CALL", null, ["callee:00c3a214:8"]]
+ 00c3ca4c ["INT_ADD", "register:40f0:8", ["const:c3ca4c:8", "const:4:8"]]
+ 00c3ca4c ["CALL", null, ["callee:00c3a214:8"]]
- 00c3c9b0 bytes f2f5ff97
+ 00c3ca4c bytes f2f5ff97
- 00c3c9d8 ["INT_ADD", "register:40f0:8", ["const:c3c9d8:8", "const:4:8"]]
- 00c3c9d8 ["CALL", null, ["callee:00c3fe18:8"]]
+ 00c3ca74 ["INT_ADD", "register:40f0:8", ["const:c3ca74:8", "const:4:8"]]
+ 00c3ca74 ["CALL", null, ["callee:00c3fe18:8"]]
- 00c3c9d8 bytes e90c0094
+ 00c3ca74 bytes e90c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca3dab5e7540935dfe761ac33973005"></a>

### [`00c3cd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md) → [`00c3cddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cddc.md) FUN_00c3cddc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ce40",
      "incomplete_value": false,
      "site": "00c3ce40",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cda4",
      "incomplete_value": false,
      "site": "00c3cda4",
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
      "00c3ce40",
      "DATA",
      [
        "storage",
        "00c99690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3ce40",
      "DATA",
      [
        "storage",
        "00c99760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md#insn-00c3cd74) · [`00c3cd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md#insn-00c3cd98) · [`00c3cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md#insn-00c3cddc)
- 新版 `00c3ce10`（命令位置の公開資料なし） · `00c3ce34`（命令位置の公開資料なし） · `00c3ce78`（命令位置の公開資料なし）

~~~diff
- 00c3cd74 ["INT_ADD", "register:40f0:8", ["const:c3cd74:8", "const:4:8"]]
- 00c3cd74 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3ce10 ["INT_ADD", "register:40f0:8", ["const:c3ce10:8", "const:4:8"]]
+ 00c3ce10 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3cd74 bytes ab740094
+ 00c3ce10 bytes b8740094
- 00c3cd98 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00c3cd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ce34 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00c3ce34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ce34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ce34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cd98 bytes 08411a91
+ 00c3ce34 bytes 08811d91
- 00c3cddc ["INT_ADD", "register:40f0:8", ["const:c3cddc:8", "const:4:8"]]
- 00c3cddc ["CALL", null, ["callee:00c580f0:8"]]
+ 00c3ce78 ["INT_ADD", "register:40f0:8", ["const:c3ce78:8", "const:4:8"]]
+ 00c3ce78 ["CALL", null, ["callee:00c580f0:8"]]
- 00c3cddc bytes 916c0094
+ 00c3ce78 bytes 9e6c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95ccfdedcab62063e7438ef1e6ff9fa"></a>

### [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) → [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) FUN_00c3ce7c

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 10件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3cf98",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
    "old": {
      "definition_site": "00c3cefc",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:ee2:8"
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
      "definition_site": "00c3cfa0",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
    "old": {
      "definition_site": "00c3cf04",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:896:8"
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
      "definition_site": "00c3cfa8",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
    "old": {
      "definition_site": "00c3cf0c",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3cf98",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c3cfa0",
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      "00c3cfa8",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3cf98",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c3cfa0",
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      "00c3cfa8",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md#insn-00c3cf14) · [`00c3cf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md#insn-00c3cf34) · [`00c3ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md#insn-00c3ce4c)
- 新版 `00c3cfb0`（命令位置の公開資料なし） · `00c3cfd0`（命令位置の公開資料なし） · `00c3cee8`（命令位置の公開資料なし）

~~~diff
- 00c3cf14 ["INT_ADD", "register:40f0:8", ["const:c3cf14:8", "const:4:8"]]
- 00c3cf14 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c3cfb0 ["INT_ADD", "register:40f0:8", ["const:c3cfb0:8", "const:4:8"]]
+ 00c3cfb0 ["CALL", null, ["callee:00c380a8:8"]]
- 00c3cf14 bytes 3eecff97
+ 00c3cfb0 bytes 3eecff97
- 00c3cf34 ["INT_ADD", "register:40f0:8", ["const:c3cf34:8", "const:4:8"]]
- 00c3cf34 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c3cfd0 ["INT_ADD", "register:40f0:8", ["const:c3cfd0:8", "const:4:8"]]
+ 00c3cfd0 ["CALL", null, ["callee:00c380a8:8"]]
- 00c3cf34 bytes 36ecff97
+ 00c3cfd0 bytes 36ecff97
- 00c3ce4c ["INT_ADD", "register:40f0:8", ["const:c3ce4c:8", "const:4:8"]]
- 00c3ce4c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3cee8 ["INT_ADD", "register:40f0:8", ["const:c3cee8:8", "const:4:8"]]
+ 00c3cee8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3ce4c bytes 75740094
+ 00c3cee8 bytes 82740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-063442c24140fa334e2f9894025cfd39"></a>

### [`00c3cf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md) → [`00c3cfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md) FUN_00c3cfd8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d060",
      "incomplete_value": false,
      "site": "00c3d060",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cfc4",
      "incomplete_value": false,
      "site": "00c3cfc4",
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
      "00c3d060",
      "DATA",
      [
        "storage",
        "00c99770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3d060",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md#insn-00c3cf94) · [`00c3cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md#insn-00c3cfb8) · [`00c3d02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md#insn-00c3d02c)
- 新版 `00c3d030`（命令位置の公開資料なし） · `00c3d054`（命令位置の公開資料なし） · `00c3d0c8`（命令位置の公開資料なし）

~~~diff
- 00c3cf94 ["INT_ADD", "register:40f0:8", ["const:c3cf94:8", "const:4:8"]]
- 00c3cf94 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d030 ["INT_ADD", "register:40f0:8", ["const:c3d030:8", "const:4:8"]]
+ 00c3d030 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3cf94 bytes 23740094
+ 00c3d030 bytes 30740094
- 00c3cfb8 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00c3cfb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cfb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3cfb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d054 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00c3d054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3cfb8 bytes 08c11d91
+ 00c3d054 bytes 08012191
- 00c3d02c ["INT_ADD", "register:40f0:8", ["const:c3d02c:8", "const:4:8"]]
- 00c3d02c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c3d0c8 ["INT_ADD", "register:40f0:8", ["const:c3d0c8:8", "const:4:8"]]
+ 00c3d0c8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c3d02c bytes fd6b0094
+ 00c3d0c8 bytes 0a6c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99712768a647bc428e66a0490bddfd5c"></a>

### [`00c3d210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md) → [`00c3d2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d2ac.md) FUN_00c3d2ac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d310",
      "incomplete_value": false,
      "site": "00c3d310",
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
    "old": {
      "definition_site": "00c3d274",
      "incomplete_value": false,
      "site": "00c3d274",
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
            "const:550:8"
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
      "definition_site": "00c3d334",
      "incomplete_value": false,
      "site": "00c3d334",
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
            "const:e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d298",
      "incomplete_value": false,
      "site": "00c3d298",
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
            "const:13d:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d310",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d334",
      "DATA",
      [
        "storage",
        "002bb13d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d310",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d334",
      "DATA",
      [
        "storage",
        "002bb0e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md#insn-00c3d244) · [`00c3d268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md#insn-00c3d268) · [`00c3d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md#insn-00c3d290)
- 新版 `00c3d2e0`（命令位置の公開資料なし） · `00c3d304`（命令位置の公開資料なし） · `00c3d32c`（命令位置の公開資料なし）

~~~diff
- 00c3d244 ["INT_ADD", "register:40f0:8", ["const:c3d244:8", "const:4:8"]]
- 00c3d244 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d2e0 ["INT_ADD", "register:40f0:8", ["const:c3d2e0:8", "const:4:8"]]
+ 00c3d2e0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d244 bytes 77730094
+ 00c3d2e0 bytes 84730094
- 00c3d268 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d304 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d268 bytes 08411591
+ 00c3d304 bytes 08811891
- 00c3d290 ["COPY", "tmp:0:8", ["const:13d:8"]]
- 00c3d290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d32c ["COPY", "tmp:0:8", ["const:e9:8"]]
+ 00c3d32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d290 bytes 08f50491
+ 00c3d32c bytes 08a50391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f54bc7ba2c52989b1fbd8b11778743"></a>

### [`00c3d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md) → [`00c3d35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md) FUN_00c3d35c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d324",
      "incomplete_value": false,
      "site": "00c3d324",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d348",
      "incomplete_value": false,
      "site": "00c3d348",
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
            "const:8d1:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d3c0",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d3e4",
      "DATA",
      [
        "storage",
        "002b18d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d3c0",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d3e4",
      "DATA",
      [
        "storage",
        "002b1875",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md#insn-00c3d2f4) · [`00c3d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md#insn-00c3d318) · [`00c3d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md#insn-00c3d340)
- 新版 `00c3d390`（命令位置の公開資料なし） · `00c3d3b4`（命令位置の公開資料なし） · `00c3d3dc`（命令位置の公開資料なし）

~~~diff
- 00c3d2f4 ["INT_ADD", "register:40f0:8", ["const:c3d2f4:8", "const:4:8"]]
- 00c3d2f4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d390 ["INT_ADD", "register:40f0:8", ["const:c3d390:8", "const:4:8"]]
+ 00c3d390 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d2f4 bytes 4b730094
+ 00c3d390 bytes 58730094
- 00c3d318 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3b4 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d3b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d318 bytes 08411591
+ 00c3d3b4 bytes 08811891
- 00c3d340 ["COPY", "tmp:0:8", ["const:8d1:8"]]
- 00c3d340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3dc ["COPY", "tmp:0:8", ["const:875:8"]]
+ 00c3d3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d340 bytes 08452391
+ 00c3d3dc bytes 08d52191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-165d3c959032f7360fff1ca58b8fcc42"></a>

### [`00c3d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md) → [`00c3d40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md) FUN_00c3d40c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d3d4",
      "incomplete_value": false,
      "site": "00c3d3d4",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d3f8",
      "incomplete_value": false,
      "site": "00c3d3f8",
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
            "const:e6b:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d470",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d494",
      "DATA",
      [
        "storage",
        "0029fe6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d470",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d494",
      "DATA",
      [
        "storage",
        "0029fe1e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md#insn-00c3d3a4) · [`00c3d3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md#insn-00c3d3c8) · [`00c3d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md#insn-00c3d3f0)
- 新版 `00c3d440`（命令位置の公開資料なし） · `00c3d464`（命令位置の公開資料なし） · `00c3d48c`（命令位置の公開資料なし）

~~~diff
- 00c3d3a4 ["INT_ADD", "register:40f0:8", ["const:c3d3a4:8", "const:4:8"]]
- 00c3d3a4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d440 ["INT_ADD", "register:40f0:8", ["const:c3d440:8", "const:4:8"]]
+ 00c3d440 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d3a4 bytes 1f730094
+ 00c3d440 bytes 2c730094
- 00c3d3c8 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d464 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d3c8 bytes 08411591
+ 00c3d464 bytes 08811891
- 00c3d3f0 ["COPY", "tmp:0:8", ["const:e6b:8"]]
- 00c3d3f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d3f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d3f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d48c ["COPY", "tmp:0:8", ["const:e1e:8"]]
+ 00c3d48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d3f0 bytes 08ad3991
+ 00c3d48c bytes 08793891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9132d90ac5304b9de5f7ac749ff7e57c"></a>

### [`00c3d420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md) → [`00c3d4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md) FUN_00c3d4bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d484",
      "incomplete_value": false,
      "site": "00c3d484",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d4a8",
      "incomplete_value": false,
      "site": "00c3d4a8",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d520",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d544",
      "DATA",
      [
        "storage",
        "002b2888",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d520",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d544",
      "DATA",
      [
        "storage",
        "002b28b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md#insn-00c3d454) · [`00c3d478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md#insn-00c3d478) · [`00c3d4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md#insn-00c3d4a0)
- 新版 `00c3d4f0`（命令位置の公開資料なし） · `00c3d514`（命令位置の公開資料なし） · `00c3d53c`（命令位置の公開資料なし）

~~~diff
- 00c3d454 ["INT_ADD", "register:40f0:8", ["const:c3d454:8", "const:4:8"]]
- 00c3d454 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d4f0 ["INT_ADD", "register:40f0:8", ["const:c3d4f0:8", "const:4:8"]]
+ 00c3d4f0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d454 bytes f3720094
+ 00c3d4f0 bytes 00730094
- 00c3d478 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d514 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d478 bytes 08411591
+ 00c3d514 bytes 08811891
- 00c3d4a0 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00c3d4a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d4a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d4a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d53c ["COPY", "tmp:0:8", ["const:8b9:8"]]
+ 00c3d53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d4a0 bytes 08212291
+ 00c3d53c bytes 08e52291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f0bd27fb44c031d8b2992ee72e808d8"></a>

### [`00c3d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md) → [`00c3d56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md) FUN_00c3d56c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d534",
      "incomplete_value": false,
      "site": "00c3d534",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d558",
      "incomplete_value": false,
      "site": "00c3d558",
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
            "const:9ac:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d5d0",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d5f4",
      "DATA",
      [
        "storage",
        "002a99ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d5d0",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d5f4",
      "DATA",
      [
        "storage",
        "002a99db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md#insn-00c3d504) · [`00c3d528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md#insn-00c3d528) · [`00c3d550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md#insn-00c3d550)
- 新版 `00c3d5a0`（命令位置の公開資料なし） · `00c3d5c4`（命令位置の公開資料なし） · `00c3d5ec`（命令位置の公開資料なし）

~~~diff
- 00c3d504 ["INT_ADD", "register:40f0:8", ["const:c3d504:8", "const:4:8"]]
- 00c3d504 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d5a0 ["INT_ADD", "register:40f0:8", ["const:c3d5a0:8", "const:4:8"]]
+ 00c3d5a0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d504 bytes c7720094
+ 00c3d5a0 bytes d4720094
- 00c3d528 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d5c4 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d528 bytes 08411591
+ 00c3d5c4 bytes 08811891
- 00c3d550 ["COPY", "tmp:0:8", ["const:9ac:8"]]
- 00c3d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d5ec ["COPY", "tmp:0:8", ["const:9db:8"]]
+ 00c3d5ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d5ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d5ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d550 bytes 08b12691
+ 00c3d5ec bytes 086d2791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b1279eb573ba089e095c827bfa384e5"></a>

### [`00c3d730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md) → [`00c3d7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md) FUN_00c3d7cc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d794",
      "incomplete_value": false,
      "site": "00c3d794",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d7b8",
      "incomplete_value": false,
      "site": "00c3d7b8",
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
            "const:e75:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d830",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d854",
      "DATA",
      [
        "storage",
        "002b9e75",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d830",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d854",
      "DATA",
      [
        "storage",
        "002b9e21",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md#insn-00c3d764) · [`00c3d788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md#insn-00c3d788) · [`00c3d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md#insn-00c3d7b0)
- 新版 `00c3d800`（命令位置の公開資料なし） · `00c3d824`（命令位置の公開資料なし） · `00c3d84c`（命令位置の公開資料なし）

~~~diff
- 00c3d764 ["INT_ADD", "register:40f0:8", ["const:c3d764:8", "const:4:8"]]
- 00c3d764 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d800 ["INT_ADD", "register:40f0:8", ["const:c3d800:8", "const:4:8"]]
+ 00c3d800 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d764 bytes 2f720094
+ 00c3d800 bytes 3c720094
- 00c3d788 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d824 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d788 bytes 08411591
+ 00c3d824 bytes 08811891
- 00c3d7b0 ["COPY", "tmp:0:8", ["const:e75:8"]]
- 00c3d7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d84c ["COPY", "tmp:0:8", ["const:e21:8"]]
+ 00c3d84c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d84c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d84c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d7b0 bytes 08d53991
+ 00c3d84c bytes 08853891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed96fb9cc73a7eb9b0450aa97236f46a"></a>

### [`00c3d7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md) → [`00c3d87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md) FUN_00c3d87c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d848",
      "incomplete_value": false,
      "site": "00c3d848",
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
            "const:5d0:8"
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
      "00c3d8e4",
      "DATA",
      [
        "storage",
        "00c975d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3d8e4",
      "DATA",
      [
        "storage",
        "00c976a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md#insn-00c3d818) · [`00c3d83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md#insn-00c3d83c) · [`00c3d884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md#insn-00c3d884)
- 新版 `00c3d8b4`（命令位置の公開資料なし） · `00c3d8d8`（命令位置の公開資料なし） · `00c3d920`（命令位置の公開資料なし）

~~~diff
- 00c3d818 ["INT_ADD", "register:40f0:8", ["const:c3d818:8", "const:4:8"]]
- 00c3d818 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d8b4 ["INT_ADD", "register:40f0:8", ["const:c3d8b4:8", "const:4:8"]]
+ 00c3d8b4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d818 bytes 02720094
+ 00c3d8b4 bytes 0f720094
- 00c3d83c ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00c3d83c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d83c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d83c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d8d8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00c3d8d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d8d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d8d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d83c bytes 08411791
+ 00c3d8d8 bytes 08811a91
- 00c3d884 ["INT_ADD", "register:40f0:8", ["const:c3d884:8", "const:4:8"]]
- 00c3d884 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c3d920 ["INT_ADD", "register:40f0:8", ["const:c3d920:8", "const:4:8"]]
+ 00c3d920 ["CALL", null, ["callee:00c580f0:8"]]
- 00c3d884 bytes e7690094
+ 00c3d920 bytes f4690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bbd7f7acd7d1a48dc9dc42675b6da15"></a>

### [`00c3d888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md) → [`00c3d924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md) FUN_00c3d924

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d8ec",
      "incomplete_value": false,
      "site": "00c3d8ec",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d910",
      "incomplete_value": false,
      "site": "00c3d910",
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
            "const:8e5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d988",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d9ac",
      "DATA",
      [
        "storage",
        "002b08e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d988",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d9ac",
      "DATA",
      [
        "storage",
        "002b0889",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md#insn-00c3d8bc) · [`00c3d8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md#insn-00c3d8e0) · [`00c3d908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md#insn-00c3d908)
- 新版 `00c3d958`（命令位置の公開資料なし） · `00c3d97c`（命令位置の公開資料なし） · `00c3d9a4`（命令位置の公開資料なし）

~~~diff
- 00c3d8bc ["INT_ADD", "register:40f0:8", ["const:c3d8bc:8", "const:4:8"]]
- 00c3d8bc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3d958 ["INT_ADD", "register:40f0:8", ["const:c3d958:8", "const:4:8"]]
+ 00c3d958 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d8bc bytes d9710094
+ 00c3d958 bytes e6710094
- 00c3d8e0 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d97c ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3d97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d8e0 bytes 08411591
+ 00c3d97c bytes 08811891
- 00c3d908 ["COPY", "tmp:0:8", ["const:8e5:8"]]
- 00c3d908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d9a4 ["COPY", "tmp:0:8", ["const:889:8"]]
+ 00c3d9a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d9a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d9a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d908 bytes 08952391
+ 00c3d9a4 bytes 08252291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e991c29057200f06853a72d30f90f3f"></a>

### [`00c3d938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md) → [`00c3d9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md) FUN_00c3d9d4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3d99c",
      "incomplete_value": false,
      "site": "00c3d99c",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3d9c0",
      "incomplete_value": false,
      "site": "00c3d9c0",
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
            "const:e14:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3da38",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3da5c",
      "DATA",
      [
        "storage",
        "002c0e14",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3da38",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3da5c",
      "DATA",
      [
        "storage",
        "002c0e54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md#insn-00c3d96c) · [`00c3d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md#insn-00c3d990) · [`00c3d9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md#insn-00c3d9b8)
- 新版 `00c3da08`（命令位置の公開資料なし） · `00c3da2c`（命令位置の公開資料なし） · `00c3da54`（命令位置の公開資料なし）

~~~diff
- 00c3d96c ["INT_ADD", "register:40f0:8", ["const:c3d96c:8", "const:4:8"]]
- 00c3d96c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3da08 ["INT_ADD", "register:40f0:8", ["const:c3da08:8", "const:4:8"]]
+ 00c3da08 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3d96c bytes ad710094
+ 00c3da08 bytes ba710094
- 00c3d990 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3d990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3da2c ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3da2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3da2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3da2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d990 bytes 08411591
+ 00c3da2c bytes 08811891
- 00c3d9b8 ["COPY", "tmp:0:8", ["const:e14:8"]]
- 00c3d9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3da54 ["COPY", "tmp:0:8", ["const:e54:8"]]
+ 00c3da54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3da54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3da54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d9b8 bytes 08513891
+ 00c3da54 bytes 08513991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0539b49561e394b1f060dabad75af1"></a>

### [`00c3d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md) → [`00c3da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md) FUN_00c3da84

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3da4c",
      "incomplete_value": false,
      "site": "00c3da4c",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3da70",
      "incomplete_value": false,
      "site": "00c3da70",
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
            "const:99b:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3dae8",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3db0c",
      "DATA",
      [
        "storage",
        "002a899b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3dae8",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3db0c",
      "DATA",
      [
        "storage",
        "002a893f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3da1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md#insn-00c3da1c) · [`00c3da40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md#insn-00c3da40) · [`00c3da60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md#insn-00c3da60)
- 新版 `00c3dab8`（命令位置の公開資料なし） · `00c3dadc`（命令位置の公開資料なし） · `00c3dafc`（命令位置の公開資料なし）

~~~diff
- 00c3da1c ["INT_ADD", "register:40f0:8", ["const:c3da1c:8", "const:4:8"]]
- 00c3da1c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3dab8 ["INT_ADD", "register:40f0:8", ["const:c3dab8:8", "const:4:8"]]
+ 00c3dab8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3da1c bytes 81710094
+ 00c3dab8 bytes 8e710094
- 00c3da40 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3da40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3da40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3da40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3dadc ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3dadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3dadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3dadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3da40 bytes 08411591
+ 00c3dadc bytes 08811891
- 00c3da60 ["COPY", "tmp:0:8", ["const:99b:8"]]
- 00c3da60 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00c3da60 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00c3da60 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00c3dafc ["COPY", "tmp:0:8", ["const:93f:8"]]
+ 00c3dafc ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00c3dafc ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00c3dafc ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00c3da60 bytes 6b6d2691
+ 00c3dafc bytes 6bfd2491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c80cd37e33746f73b372beb8793feda8"></a>

### [`00c3da94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md) → [`00c3db30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md) FUN_00c3db30

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3daf8",
      "incomplete_value": false,
      "site": "00c3daf8",
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
            "const:550:8"
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
    "old": {
      "definition_site": "00c3db1c",
      "incomplete_value": false,
      "site": "00c3db1c",
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
            "const:fa6:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3db94",
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dbb8",
      "DATA",
      [
        "storage",
        "002c1fa6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3db94",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dbb8",
      "DATA",
      [
        "storage",
        "002c1fe6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3dac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md#insn-00c3dac8) · [`00c3daec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md#insn-00c3daec) · [`00c3db14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md#insn-00c3db14)
- 新版 `00c3db64`（命令位置の公開資料なし） · `00c3db88`（命令位置の公開資料なし） · `00c3dbb0`（命令位置の公開資料なし）

~~~diff
- 00c3dac8 ["INT_ADD", "register:40f0:8", ["const:c3dac8:8", "const:4:8"]]
- 00c3dac8 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3db64 ["INT_ADD", "register:40f0:8", ["const:c3db64:8", "const:4:8"]]
+ 00c3db64 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3dac8 bytes 56710094
+ 00c3db64 bytes 63710094
- 00c3daec ["COPY", "tmp:0:8", ["const:550:8"]]
- 00c3daec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3daec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3daec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3db88 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3db88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3db88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3db88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3daec bytes 08411591
+ 00c3db88 bytes 08811891
- 00c3db14 ["COPY", "tmp:0:8", ["const:fa6:8"]]
- 00c3db14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3db14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3db14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3dbb0 ["COPY", "tmp:0:8", ["const:fe6:8"]]
+ 00c3dbb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3dbb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3dbb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3db14 bytes 08993e91
+ 00c3dbb0 bytes 08993f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6e2e34e7ed2c6f913b73d2f15e80ee"></a>

### [`00c3de30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md) → [`00c3decc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md) FUN_00c3decc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3de98",
      "incomplete_value": true,
      "site": "00c3dea4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:15c:8"
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
    "old": {
      "definition_site": "00c3de9c",
      "incomplete_value": true,
      "site": "00c3dea8",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3df34",
      "READ",
      [
        "storage",
        "002bb15c",
        null,
        "string"
      ]
    ],
    [
      "00c3df38",
      "READ",
      [
        "storage",
        "002bb16c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3df34",
      "READ",
      [
        "storage",
        "002bb108",
        null,
        "string"
      ]
    ],
    [
      "00c3df38",
      "READ",
      [
        "storage",
        "002bb118",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md#insn-00c3de78) · [`00c3de90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md#insn-00c3de90) · [`00c3dec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md#insn-00c3dec8)
- 新版 `00c3df14`（命令位置の公開資料なし） · `00c3df2c`（命令位置の公開資料なし） · `00c3df64`（命令位置の公開資料なし）

~~~diff
- 00c3de78 ["INT_ADD", "register:40f0:8", ["const:c3de78:8", "const:4:8"]]
- 00c3de78 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3df14 ["INT_ADD", "register:40f0:8", ["const:c3df14:8", "const:4:8"]]
+ 00c3df14 ["CALL", null, ["callee:00c5a170:8"]]
- 00c3de78 bytes 8a700094
+ 00c3df14 bytes 97700094
- 00c3de90 ["COPY", "tmp:0:8", ["const:15c:8"]]
- 00c3de90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c3de90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c3de90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c3df2c ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00c3df2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3df2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3df2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c3de90 bytes 4a710591
+ 00c3df2c bytes 4a210491
- 00c3dec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3dec8 ["INT_ADD", "register:40f0:8", ["const:c3dec8:8", "const:4:8"]]
- 00c3dec8 ["CALLIND", null, ["register:0:8"]]
+ 00c3df64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3df64 ["INT_ADD", "register:40f0:8", ["const:c3df64:8", "const:4:8"]]
+ 00c3df64 ["CALLIND", null, ["register:0:8"]]
- 00c3dec8 bytes 00013fd6
+ 00c3df64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9fafa15f4648adc49aee8661187ec0d"></a>

### [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) → [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) FUN_00c3e04c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3db44.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 7件 [`00c3dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3e0d0",
      "incomplete_value": false,
      "site": "00c3e0d0",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3e16c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e178",
      "DATA",
      [
        "storage",
        "002af764",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e16c",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e178",
      "DATA",
      [
        "storage",
        "002af708",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md#insn-00c3e0a0) · [`00c3e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md#insn-00c3e0c4) · [`00c3e128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md#insn-00c3e128)
- 新版 `00c3e13c`（命令位置の公開資料なし） · `00c3e160`（命令位置の公開資料なし） · `00c3e1c4`（命令位置の公開資料なし）

~~~diff
- 00c3e0a0 ["INT_ADD", "register:40f0:8", ["const:c3e0a0:8", "const:4:8"]]
- 00c3e0a0 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3e13c ["INT_ADD", "register:40f0:8", ["const:c3e13c:8", "const:4:8"]]
+ 00c3e13c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3e0a0 bytes e06f0094
+ 00c3e13c bytes ed6f0094
- 00c3e0c4 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3e0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e160 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3e160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3e0c4 bytes 08011991
+ 00c3e160 bytes 08411c91
- 00c3e128 ["INT_ADD", "register:40f0:8", ["const:c3e128:8", "const:4:8"]]
- 00c3e128 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3e1c4 ["INT_ADD", "register:40f0:8", ["const:c3e1c4:8", "const:4:8"]]
+ 00c3e1c4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3e128 bytes be6f0094
+ 00c3e1c4 bytes cb6f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c47ae0746b28aa151346e918844a7d5"></a>

### [`00c3e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md) → [`00c3e278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md) FUN_00c3e278

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3e240",
      "incomplete_value": false,
      "site": "00c3e240",
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
            "const:640:8"
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
      "00c3e2dc",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e2dc",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md#insn-00c3e210) · [`00c3e234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md#insn-00c3e234) · [`00c3e278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md#insn-00c3e278)
- 新版 `00c3e2ac`（命令位置の公開資料なし） · `00c3e2d0`（命令位置の公開資料なし） · `00c3e314`（命令位置の公開資料なし）

~~~diff
- 00c3e210 ["INT_ADD", "register:40f0:8", ["const:c3e210:8", "const:4:8"]]
- 00c3e210 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3e2ac ["INT_ADD", "register:40f0:8", ["const:c3e2ac:8", "const:4:8"]]
+ 00c3e2ac ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3e210 bytes 846f0094
+ 00c3e2ac bytes 916f0094
- 00c3e234 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3e234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e2d0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3e2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3e234 bytes 08011991
+ 00c3e2d0 bytes 08411c91
- 00c3e278 ["INT_ADD", "register:40f0:8", ["const:c3e278:8", "const:4:8"]]
- 00c3e278 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c3e314 ["INT_ADD", "register:40f0:8", ["const:c3e314:8", "const:4:8"]]
+ 00c3e314 ["CALL", null, ["callee:00c580f0:8"]]
- 00c3e278 bytes 6a670094
+ 00c3e314 bytes 77670094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f86af9c79b27099ce03600747d05431"></a>

### [`00c3e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) → [`00c3e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) FUN_00c3e4f0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 4件 [`00c3f034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 4件 [`00c3f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3e558",
      "incomplete_value": false,
      "site": "00c3e564",
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
            "const:d84:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3e5d8",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e600",
      "DATA",
      [
        "storage",
        "002b8d84",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3e5d8",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e600",
      "DATA",
      [
        "storage",
        "002b8d30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md#insn-00c3e4ac) · [`00c3e4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md#insn-00c3e4fc) · [`00c3e530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md#insn-00c3e530)
- 新版 `00c3e548`（命令位置の公開資料なし） · `00c3e598`（命令位置の公開資料なし） · `00c3e5cc`（命令位置の公開資料なし）

~~~diff
- 00c3e4ac ["INT_ADD", "register:40f0:8", ["const:c3e4ac:8", "const:4:8"]]
- 00c3e4ac ["CALL", null, ["callee:00c3f0d0:8"]]
+ 00c3e548 ["INT_ADD", "register:40f0:8", ["const:c3e548:8", "const:4:8"]]
+ 00c3e548 ["CALL", null, ["callee:00c3f0d0:8"]]
- 00c3e4ac bytes e2020094
+ 00c3e548 bytes e2020094
- 00c3e4fc ["INT_ADD", "register:40f0:8", ["const:c3e4fc:8", "const:4:8"]]
- 00c3e4fc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3e598 ["INT_ADD", "register:40f0:8", ["const:c3e598:8", "const:4:8"]]
+ 00c3e598 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3e4fc bytes c96e0094
+ 00c3e598 bytes d66e0094
- 00c3e530 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3e530 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c3e530 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c3e530 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c3e5cc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3e5cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3e5cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3e5cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c3e530 bytes 29011991
+ 00c3e5cc bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef74456e386fad2c5974b8ccf5e6fe0"></a>

### [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) → [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) FUN_00c3e660

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) · 呼出先 8件 [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 5件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 8件 [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3ea44",
      "incomplete_value": false,
      "site": "00c3ea44",
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
            "const:4d0:8"
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
      "00c3e874",
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3eae0",
      "DATA",
      [
        "storage",
        "00c994d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e874",
      "DATA",
      [
        "storage",
        "00c99530",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3eae0",
      "DATA",
      [
        "storage",
        "00c995a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md#insn-00c3e638) · [`00c3e644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md#insn-00c3e644) · [`00c3e64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md#insn-00c3e64c)
- 新版 `00c3e6d4`（命令位置の公開資料なし） · `00c3e6e0`（命令位置の公開資料なし） · `00c3e6e8`（命令位置の公開資料なし）

~~~diff
- 00c3e638 ["INT_ADD", "register:40f0:8", ["const:c3e638:8", "const:4:8"]]
- 00c3e638 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c3e6d4 ["INT_ADD", "register:40f0:8", ["const:c3e6d4:8", "const:4:8"]]
+ 00c3e6d4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c3e638 bytes 9a6e0094
+ 00c3e6d4 bytes a76e0094
- 00c3e644 ["INT_ADD", "register:40f0:8", ["const:c3e644:8", "const:4:8"]]
- 00c3e644 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c3e6e0 ["INT_ADD", "register:40f0:8", ["const:c3e6e0:8", "const:4:8"]]
+ 00c3e6e0 ["CALL", null, ["callee:00c5b210:8"]]
- 00c3e644 bytes bf720094
+ 00c3e6e0 bytes cc720094
- 00c3e64c ["INT_ADD", "register:40f0:8", ["const:c3e64c:8", "const:4:8"]]
- 00c3e64c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3e6e8 ["INT_ADD", "register:40f0:8", ["const:c3e6e8:8", "const:4:8"]]
+ 00c3e6e8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3e64c bytes 756e0094
+ 00c3e6e8 bytes 826e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fedb7041f3ba6c0abd3db0feef89cf64"></a>

### [`00c3ea94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md) → [`00c3eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) FUN_00c3eb30

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3eafc",
      "incomplete_value": false,
      "site": "00c3eafc",
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
            "const:540:8"
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
      "00c3eb98",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3eb98",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3eacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md#insn-00c3eacc) · [`00c3eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md#insn-00c3eaf0) · [`00c3eb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md#insn-00c3eb38)
- 新版 `00c3eb68`（命令位置の公開資料なし） · `00c3eb8c`（命令位置の公開資料なし） · `00c3ebd4`（命令位置の公開資料なし）

~~~diff
- 00c3eacc ["INT_ADD", "register:40f0:8", ["const:c3eacc:8", "const:4:8"]]
- 00c3eacc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3eb68 ["INT_ADD", "register:40f0:8", ["const:c3eb68:8", "const:4:8"]]
+ 00c3eb68 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3eacc bytes 556d0094
+ 00c3eb68 bytes 626d0094
- 00c3eaf0 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00c3eaf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3eaf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3eaf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3eb8c ["COPY", "tmp:0:8", ["const:610:8"]]
+ 00c3eb8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3eb8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3eb8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3eaf0 bytes 08011591
+ 00c3eb8c bytes 08411891
- 00c3eb38 ["INT_ADD", "register:40f0:8", ["const:c3eb38:8", "const:4:8"]]
- 00c3eb38 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c3ebd4 ["INT_ADD", "register:40f0:8", ["const:c3ebd4:8", "const:4:8"]]
+ 00c3ebd4 ["CALL", null, ["callee:00c580f0:8"]]
- 00c3eb38 bytes 3a650094
+ 00c3ebd4 bytes 47650094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7377a53908fbfca0f37101c07dc54613"></a>

### [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) → [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) FUN_00c3ebd8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 7件 [`00c3f970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md) [`00c3fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 4件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 7件 [`00c3fa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md) [`00c3fae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3eda8",
      "incomplete_value": false,
      "site": "00c3eda8",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3ed2c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ee44",
      "DATA",
      [
        "storage",
        "00c97720",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ef24",
      "PARAM",
      [
        "storage",
        "002a1d99",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3ed2c",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ee44",
      "DATA",
      [
        "storage",
        "00c977f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ef24",
      "PARAM",
      [
        "storage",
        "002a1d4c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md#insn-00c3ec60) · [`00c3ec84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md#insn-00c3ec84) · [`00c3ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md#insn-00c3ed70)
- 新版 `00c3ecfc`（命令位置の公開資料なし） · `00c3ed20`（命令位置の公開資料なし） · `00c3ee0c`（命令位置の公開資料なし）

~~~diff
- 00c3ec60 ["INT_ADD", "register:40f0:8", ["const:c3ec60:8", "const:4:8"]]
- 00c3ec60 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3ecfc ["INT_ADD", "register:40f0:8", ["const:c3ecfc:8", "const:4:8"]]
+ 00c3ecfc ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3ec60 bytes f06c0094
+ 00c3ecfc bytes fd6c0094
- 00c3ec84 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3ec84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ec84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ec84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ed20 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3ed20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ed20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ed20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ec84 bytes 08011991
+ 00c3ed20 bytes 08411c91
- 00c3ed70 ["INT_ADD", "register:40f0:8", ["const:c3ed70:8", "const:4:8"]]
- 00c3ed70 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3ee0c ["INT_ADD", "register:40f0:8", ["const:c3ee0c:8", "const:4:8"]]
+ 00c3ee0c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3ed70 bytes ac6c0094
+ 00c3ee0c bytes b96c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eaf7d71a639808b8b492aead15ff21d"></a>

### [`00c3ef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) → [`00c3ef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) FUN_00c3ef9c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 3件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 3件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 3件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3efdc",
      "incomplete_value": false,
      "site": "00c3efdc",
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
            "const:40:8"
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
    "old": {
      "definition_site": "00c3effc",
      "incomplete_value": false,
      "site": "00c3effc",
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
            "const:58c:8"
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
      "00c3f078",
      "DATA",
      [
        "storage",
        "00c98040",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f098",
      "DATA",
      [
        "storage",
        "002ae58c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3f078",
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f098",
      "DATA",
      [
        "storage",
        "002ae530",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md#insn-00c3ef60) · [`00c3efa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md#insn-00c3efa8) · [`00c3efd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md#insn-00c3efd0)
- 新版 `00c3effc`（命令位置の公開資料なし） · `00c3f044`（命令位置の公開資料なし） · `00c3f06c`（命令位置の公開資料なし）

~~~diff
- 00c3ef60 ["INT_ADD", "register:40f0:8", ["const:c3ef60:8", "const:4:8"]]
- 00c3ef60 ["CALL", null, ["callee:00c3fe18:8"]]
+ 00c3effc ["INT_ADD", "register:40f0:8", ["const:c3effc:8", "const:4:8"]]
+ 00c3effc ["CALL", null, ["callee:00c3fe18:8"]]
- 00c3ef60 bytes 87030094
+ 00c3effc bytes 87030094
- 00c3efa8 ["INT_ADD", "register:40f0:8", ["const:c3efa8:8", "const:4:8"]]
- 00c3efa8 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3f044 ["INT_ADD", "register:40f0:8", ["const:c3f044:8", "const:4:8"]]
+ 00c3f044 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3efa8 bytes 1e6c0094
+ 00c3f044 bytes 2b6c0094
- 00c3efd0 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00c3efd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c3efd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c3efd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c3f06c ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00c3f06c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3f06c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3f06c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c3efd0 bytes 4a010191
+ 00c3f06c bytes 4a410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af0bd51da85c64e145960bb62908e62"></a>

### [`00c3f034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) → [`00c3f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) FUN_00c3f0d0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 6件 [`00c4c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c228.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)
- 新版 呼出元 3件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 6件 [`00c4c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c2c4.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3f258",
      "incomplete_value": false,
      "site": "00c3f25c",
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
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3f2f8",
      "DATA",
      [
        "storage",
        "00c99070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f2f8",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md#insn-00c3f200) · [`00c3f258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md#insn-00c3f258) · [`00c3f260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md#insn-00c3f260)
- 新版 `00c3f29c`（命令位置の公開資料なし） · `00c3f2f4`（命令位置の公開資料なし） · `00c3f2fc`（命令位置の公開資料なし）

~~~diff
- 00c3f200 ["INT_ADD", "register:40f0:8", ["const:c3f200:8", "const:4:8"]]
- 00c3f200 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3f29c ["INT_ADD", "register:40f0:8", ["const:c3f29c:8", "const:4:8"]]
+ 00c3f29c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3f200 bytes 886b0094
+ 00c3f29c bytes 956b0094
- 00c3f258 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00c3f258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f2f4 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00c3f2f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f2f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f2f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3f258 bytes 08c10191
+ 00c3f2f4 bytes 08010591
- 00c3f260 ["INT_ADD", "register:40f0:8", ["const:c3f260:8", "const:4:8"]]
- 00c3f260 ["CALL", null, ["callee:00c4c2c4:8"]]
+ 00c3f2fc ["INT_ADD", "register:40f0:8", ["const:c3f2fc:8", "const:4:8"]]
+ 00c3f2fc ["CALL", null, ["callee:00c4c2c4:8"]]
- 00c3f260 bytes f2330094
+ 00c3f2fc bytes f2330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0948ae17f299c289a9398d55cb44060d"></a>

### [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) → [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) FUN_00c3f3ac

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) · 呼出先 13件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3db44.md) [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md)
- 新版 呼出元 2件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) · 呼出先 13件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3f558",
      "incomplete_value": false,
      "site": "00c3f558",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3f7c0",
      "incomplete_value": false,
      "site": "00c3f7c0",
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
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3f538",
      "DATA",
      [
        "storage",
        "00c990f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f5f4",
      "DATA",
      [
        "storage",
        "00c992a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f6e4",
      "DATA",
      [
        "storage",
        "00c99380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f538",
      "DATA",
      [
        "storage",
        "00c991c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f5f4",
      "DATA",
      [
        "storage",
        "00c99370",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f6e4",
      "DATA",
      [
        "storage",
        "00c99450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md#insn-00c3f344) · [`00c3f3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md#insn-00c3f3c8) · [`00c3f3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md#insn-00c3f3e8)
- 新版 `00c3f3e0`（命令位置の公開資料なし） · `00c3f464`（命令位置の公開資料なし） · `00c3f484`（命令位置の公開資料なし）

~~~diff
- 00c3f344 ["INT_ADD", "register:40f0:8", ["const:c3f344:8", "const:4:8"]]
- 00c3f344 ["CALL", null, ["callee:00c3dbe0:8"]]
+ 00c3f3e0 ["INT_ADD", "register:40f0:8", ["const:c3f3e0:8", "const:4:8"]]
+ 00c3f3e0 ["CALL", null, ["callee:00c3dbe0:8"]]
- 00c3f344 bytes 00faff97
+ 00c3f3e0 bytes 00faff97
- 00c3f3c8 ["INT_ADD", "register:40f0:8", ["const:c3f3c8:8", "const:4:8"]]
- 00c3f3c8 ["CALL", null, ["callee:00c3e04c:8"]]
+ 00c3f464 ["INT_ADD", "register:40f0:8", ["const:c3f464:8", "const:4:8"]]
+ 00c3f464 ["CALL", null, ["callee:00c3e04c:8"]]
- 00c3f3c8 bytes fafaff97
+ 00c3f464 bytes fafaff97
- 00c3f3e8 ["INT_ADD", "register:40f0:8", ["const:c3f3e8:8", "const:4:8"]]
- 00c3f3e8 ["CALL", null, ["callee:00c465bc:8"]]
+ 00c3f484 ["INT_ADD", "register:40f0:8", ["const:c3f484:8", "const:4:8"]]
+ 00c3f484 ["CALL", null, ["callee:00c465bc:8"]]
- 00c3f3e8 bytes 4e1c0094
+ 00c3f484 bytes 4e1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57d9d5fc4b424fb7b8a038123115a3d6"></a>

### [`00c3f8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md) → [`00c3f96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md) FUN_00c3f96c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3f934",
      "incomplete_value": false,
      "site": "00c3f934",
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
            "const:640:8"
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
      "00c3f9d0",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f9d0",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md#insn-00c3f904) · [`00c3f928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md#insn-00c3f928) · [`00c3f96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md#insn-00c3f96c)
- 新版 `00c3f9a0`（命令位置の公開資料なし） · `00c3f9c4`（命令位置の公開資料なし） · `00c3fa08`（命令位置の公開資料なし）

~~~diff
- 00c3f904 ["INT_ADD", "register:40f0:8", ["const:c3f904:8", "const:4:8"]]
- 00c3f904 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3f9a0 ["INT_ADD", "register:40f0:8", ["const:c3f9a0:8", "const:4:8"]]
+ 00c3f9a0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3f904 bytes c7690094
+ 00c3f9a0 bytes d4690094
- 00c3f928 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3f928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f9c4 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3f9c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f9c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f9c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3f928 bytes 08011991
+ 00c3f9c4 bytes 08411c91
- 00c3f96c ["INT_ADD", "register:40f0:8", ["const:c3f96c:8", "const:4:8"]]
- 00c3f96c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c3fa08 ["INT_ADD", "register:40f0:8", ["const:c3fa08:8", "const:4:8"]]
+ 00c3fa08 ["CALL", null, ["callee:00c580f0:8"]]
- 00c3f96c bytes ad610094
+ 00c3fa08 bytes ba610094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab5e4b1d70e33db505d46a391368f9a1"></a>

### [`00c3fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md) → [`00c3fae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) FUN_00c3fae4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c3fab4",
      "incomplete_value": false,
      "site": "00c3fab4",
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
            "const:640:8"
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
      "00c3fb50",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3fb50",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3fa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md#insn-00c3fa7c) · [`00c3faa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md#insn-00c3faa4) · [`00c3faac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md#insn-00c3faac)
- 新版 `00c3fb18`（命令位置の公開資料なし） · `00c3fb40`（命令位置の公開資料なし） · `00c3fb48`（命令位置の公開資料なし）

~~~diff
- 00c3fa7c ["INT_ADD", "register:40f0:8", ["const:c3fa7c:8", "const:4:8"]]
- 00c3fa7c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c3fb18 ["INT_ADD", "register:40f0:8", ["const:c3fb18:8", "const:4:8"]]
+ 00c3fb18 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c3fa7c bytes 69690094
+ 00c3fb18 bytes 76690094
- 00c3faa4 ["INT_ADD", "register:40f0:8", ["const:c3faa4:8", "const:4:8"]]
- 00c3faa4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c3fb40 ["INT_ADD", "register:40f0:8", ["const:c3fb40:8", "const:4:8"]]
+ 00c3fb40 ["CALL", null, ["callee:00c580b0:8"]]
- 00c3faa4 bytes 4f610094
+ 00c3fb40 bytes 5c610094
- 00c3faac ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c3faac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c3faac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c3faac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c3fb48 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3fb48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3fb48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c3fb48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c3faac bytes 29011991
+ 00c3fb48 bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dde3ecc844d858a051dfcec8e94e01a"></a>

### [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) → [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) FUN_00c3fe18

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 14件 [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3ef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) · 呼出先 42件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md)
- 新版 呼出元 14件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3ef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) · 呼出先 42件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c40510",
      "incomplete_value": false,
      "site": "00c40510",
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
            "const:e10:8"
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
    "old": {
      "definition_site": "00c40950",
      "incomplete_value": false,
      "site": "00c40950",
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
            "const:40:8"
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
    "old": {
      "definition_site": "00c40ffc",
      "incomplete_value": false,
      "site": "00c40ffc",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "ordinal": 164,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3feec",
      "READ",
      [
        "storage",
        "00c97960",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3fefc",
      "READ",
      [
        "storage",
        "00c97961",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3ff28",
      "READ",
      [
        "storage",
        "00c97970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3feec",
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3fefc",
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3ff28",
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c40234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md#insn-00c40234) · [`00c40294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md#insn-00c40294) · [`00c40474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md#insn-00c40474)
- 新版 `00c402d0`（命令位置の公開資料なし） · `00c40330`（命令位置の公開資料なし） · `00c40510`（命令位置の公開資料なし）

~~~diff
- 00c40234 ["INT_ADD", "register:40f0:8", ["const:c40234:8", "const:4:8"]]
- 00c40234 ["CALL", null, ["callee:00c3a1b4:8"]]
+ 00c402d0 ["INT_ADD", "register:40f0:8", ["const:c402d0:8", "const:4:8"]]
+ 00c402d0 ["CALL", null, ["callee:00c3a1b4:8"]]
- 00c40234 bytes b9e7ff97
+ 00c402d0 bytes b9e7ff97
- 00c40294 ["INT_ADD", "register:40f0:8", ["const:c40294:8", "const:4:8"]]
- 00c40294 ["CALL", null, ["callee:00c3a1b4:8"]]
+ 00c40330 ["INT_ADD", "register:40f0:8", ["const:c40330:8", "const:4:8"]]
+ 00c40330 ["CALL", null, ["callee:00c3a1b4:8"]]
- 00c40294 bytes a1e7ff97
+ 00c40330 bytes a1e7ff97
- 00c40474 ["INT_ADD", "register:40f0:8", ["const:c40474:8", "const:4:8"]]
- 00c40474 ["CALL", null, ["local:b0:8"]]
+ 00c40510 ["INT_ADD", "register:40f0:8", ["const:c40510:8", "const:4:8"]]
+ 00c40510 ["CALL", null, ["local:b0:8"]]
- 00c40474 bytes 42feff97
+ 00c40510 bytes 42feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61df89a1ae133b0da1356ecb2eac4704"></a>

### [`00c4110c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md) → [`00c411a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md) FUN_00c411a8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4117c",
      "incomplete_value": false,
      "site": "00c4117c",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c41218",
      "DATA",
      [
        "storage",
        "00c97c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c41218",
      "DATA",
      [
        "storage",
        "00c97d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4114c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md#insn-00c4114c) · [`00c41170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md#insn-00c41170) · [`00c411c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md#insn-00c411c8)
- 新版 `00c411e8`（命令位置の公開資料なし） · `00c4120c`（命令位置の公開資料なし） · `00c41264`（命令位置の公開資料なし）

~~~diff
- 00c4114c ["INT_ADD", "register:40f0:8", ["const:c4114c:8", "const:4:8"]]
- 00c4114c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c411e8 ["INT_ADD", "register:40f0:8", ["const:c411e8:8", "const:4:8"]]
+ 00c411e8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4114c bytes b5630094
+ 00c411e8 bytes c2630094
- 00c41170 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00c41170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4120c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00c4120c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4120c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4120c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41170 bytes 08413191
+ 00c4120c bytes 08813491
- 00c411c8 ["INT_ADD", "register:40f0:8", ["const:c411c8:8", "const:4:8"]]
- 00c411c8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c41264 ["INT_ADD", "register:40f0:8", ["const:c41264:8", "const:4:8"]]
+ 00c41264 ["CALL", null, ["callee:00c580f0:8"]]
- 00c411c8 bytes 965b0094
+ 00c41264 bytes a35b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ccc2adb70c2bc45461fdfd1f34afce4"></a>

### [`00c411cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md) → [`00c41268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md) FUN_00c41268

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4123c",
      "incomplete_value": false,
      "site": "00c4123c",
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
            "const:cc0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c412d8",
      "DATA",
      [
        "storage",
        "00c97cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c412d8",
      "DATA",
      [
        "storage",
        "00c97d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md#insn-00c4120c) · [`00c41230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md#insn-00c41230) · [`00c41284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md#insn-00c41284)
- 新版 `00c412a8`（命令位置の公開資料なし） · `00c412cc`（命令位置の公開資料なし） · `00c41320`（命令位置の公開資料なし）

~~~diff
- 00c4120c ["INT_ADD", "register:40f0:8", ["const:c4120c:8", "const:4:8"]]
- 00c4120c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c412a8 ["INT_ADD", "register:40f0:8", ["const:c412a8:8", "const:4:8"]]
+ 00c412a8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4120c bytes 85630094
+ 00c412a8 bytes 92630094
- 00c41230 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00c41230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c412cc ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00c412cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c412cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c412cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41230 bytes 08013391
+ 00c412cc bytes 08413691
- 00c41284 ["INT_ADD", "register:40f0:8", ["const:c41284:8", "const:4:8"]]
- 00c41284 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c41320 ["INT_ADD", "register:40f0:8", ["const:c41320:8", "const:4:8"]]
+ 00c41320 ["CALL", null, ["callee:00c580f0:8"]]
- 00c41284 bytes 675b0094
+ 00c41320 bytes 745b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3bfe2e4220add2496ef86cd9431acbf"></a>

### [`00c41288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md) → [`00c41324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md) FUN_00c41324

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c412fc",
      "incomplete_value": false,
      "site": "00c412fc",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c41398",
      "DATA",
      [
        "storage",
        "00c97d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c41398",
      "DATA",
      [
        "storage",
        "00c97e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c412cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md#insn-00c412cc) · [`00c412f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md#insn-00c412f0) · [`00c41350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md#insn-00c41350)
- 新版 `00c41368`（命令位置の公開資料なし） · `00c4138c`（命令位置の公開資料なし） · `00c413ec`（命令位置の公開資料なし）

~~~diff
- 00c412cc ["INT_ADD", "register:40f0:8", ["const:c412cc:8", "const:4:8"]]
- 00c412cc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c41368 ["INT_ADD", "register:40f0:8", ["const:c41368:8", "const:4:8"]]
+ 00c41368 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c412cc bytes 55630094
+ 00c41368 bytes 62630094
- 00c412f0 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00c412f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c412f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c412f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4138c ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00c4138c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4138c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4138c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c412f0 bytes 08c13491
+ 00c4138c bytes 08013891
- 00c41350 ["INT_ADD", "register:40f0:8", ["const:c41350:8", "const:4:8"]]
- 00c41350 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c413ec ["INT_ADD", "register:40f0:8", ["const:c413ec:8", "const:4:8"]]
+ 00c413ec ["CALL", null, ["callee:00c580f0:8"]]
- 00c41350 bytes 345b0094
+ 00c413ec bytes 415b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66d35b26f6c9abda9235d87b0b920869"></a>

### [`00c41354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md) → [`00c413f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md) FUN_00c413f0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c413d4",
      "incomplete_value": false,
      "site": "00c413d4",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c41470",
      "DATA",
      [
        "storage",
        "00c97da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c41470",
      "DATA",
      [
        "storage",
        "00c97e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c413a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md#insn-00c413a4) · [`00c413c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md#insn-00c413c8) · [`00c4143c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md#insn-00c4143c)
- 新版 `00c41440`（命令位置の公開資料なし） · `00c41464`（命令位置の公開資料なし） · `00c414d8`（命令位置の公開資料なし）

~~~diff
- 00c413a4 ["INT_ADD", "register:40f0:8", ["const:c413a4:8", "const:4:8"]]
- 00c413a4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c41440 ["INT_ADD", "register:40f0:8", ["const:c41440:8", "const:4:8"]]
+ 00c41440 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c413a4 bytes 1f630094
+ 00c41440 bytes 2c630094
- 00c413c8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00c413c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c413c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c413c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41464 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00c41464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c413c8 bytes 08813691
+ 00c41464 bytes 08c13991
- 00c4143c ["INT_ADD", "register:40f0:8", ["const:c4143c:8", "const:4:8"]]
- 00c4143c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c414d8 ["INT_ADD", "register:40f0:8", ["const:c414d8:8", "const:4:8"]]
+ 00c414d8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4143c bytes f95a0094
+ 00c414d8 bytes 065b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68bf664b71dd39e3fd8f812a06e9ec20"></a>

### [`00c41440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md) → [`00c414dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md) FUN_00c414dc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c414b0",
      "incomplete_value": false,
      "site": "00c414b0",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4154c",
      "DATA",
      [
        "storage",
        "00c97e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4154c",
      "DATA",
      [
        "storage",
        "00c97f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md#insn-00c41480) · [`00c414a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md#insn-00c414a4) · [`00c414fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md#insn-00c414fc)
- 新版 `00c4151c`（命令位置の公開資料なし） · `00c41540`（命令位置の公開資料なし） · `00c41598`（命令位置の公開資料なし）

~~~diff
- 00c41480 ["INT_ADD", "register:40f0:8", ["const:c41480:8", "const:4:8"]]
- 00c41480 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4151c ["INT_ADD", "register:40f0:8", ["const:c4151c:8", "const:4:8"]]
+ 00c4151c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c41480 bytes e8620094
+ 00c4151c bytes f5620094
- 00c414a4 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00c414a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c414a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c414a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41540 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00c41540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c414a4 bytes 08013a91
+ 00c41540 bytes 08413d91
- 00c414fc ["INT_ADD", "register:40f0:8", ["const:c414fc:8", "const:4:8"]]
- 00c414fc ["CALL", null, ["callee:00c580f0:8"]]
+ 00c41598 ["INT_ADD", "register:40f0:8", ["const:c41598:8", "const:4:8"]]
+ 00c41598 ["CALL", null, ["callee:00c580f0:8"]]
- 00c414fc bytes c95a0094
+ 00c41598 bytes d65a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0961287131cffc66a255a096ce0236fb"></a>

### [`00c41500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md) → [`00c4159c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md) FUN_00c4159c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c41570",
      "incomplete_value": false,
      "site": "00c41570",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4160c",
      "DATA",
      [
        "storage",
        "00c97ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4160c",
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md#insn-00c41540) · [`00c41564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md#insn-00c41564) · [`00c415bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md#insn-00c415bc)
- 新版 `00c415dc`（命令位置の公開資料なし） · `00c41600`（命令位置の公開資料なし） · `00c41658`（命令位置の公開資料なし）

~~~diff
- 00c41540 ["INT_ADD", "register:40f0:8", ["const:c41540:8", "const:4:8"]]
- 00c41540 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c415dc ["INT_ADD", "register:40f0:8", ["const:c415dc:8", "const:4:8"]]
+ 00c415dc ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c41540 bytes b8620094
+ 00c415dc bytes c5620094
- 00c41564 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00c41564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c41600 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 00c41600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c41600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41564 bytes 08c13b91
+ 00c41600 bytes 08013f91
- 00c415bc ["INT_ADD", "register:40f0:8", ["const:c415bc:8", "const:4:8"]]
- 00c415bc ["CALL", null, ["callee:00c580f0:8"]]
+ 00c41658 ["INT_ADD", "register:40f0:8", ["const:c41658:8", "const:4:8"]]
+ 00c41658 ["CALL", null, ["callee:00c580f0:8"]]
- 00c415bc bytes 995a0094
+ 00c41658 bytes a65a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-439f3dbe205060cdb1343fe0b35722a8"></a>

### [`00c415c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md) → [`00c4165c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md) FUN_00c4165c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c41634",
      "incomplete_value": false,
      "site": "00c41634",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c416d0",
      "DATA",
      [
        "storage",
        "00c97f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c416d0",
      "DATA",
      [
        "storage",
        "00c98030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md#insn-00c41604) · [`00c41624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md#insn-00c41624) · [`00c41628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md#insn-00c41628)
- 新版 `00c416a0`（命令位置の公開資料なし） · `00c416c0`（命令位置の公開資料なし） · `00c416c4`（命令位置の公開資料なし）

~~~diff
- 00c41604 ["INT_ADD", "register:40f0:8", ["const:c41604:8", "const:4:8"]]
- 00c41604 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c416a0 ["INT_ADD", "register:40f0:8", ["const:c416a0:8", "const:4:8"]]
+ 00c416a0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c41604 bytes 87620094
+ 00c416a0 bytes 94620094
- 00c41624 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c416c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c41624 bytes a80200d0
+ 00c416c0 bytes a80200f0
- 00c41628 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 00c41628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c416c4 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 00c416c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c416c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c416c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41628 bytes 08813d91
+ 00c416c4 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b33cbf80cc206b2f2577695edd3c69"></a>

### [`00c41688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md) → [`00c41724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md) FUN_00c41724

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c416fc",
      "incomplete_value": false,
      "site": "00c416fc",
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
            "const:fd0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c41798",
      "DATA",
      [
        "storage",
        "00c97fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c41798",
      "DATA",
      [
        "storage",
        "00c980a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c416cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md#insn-00c416cc) · [`00c416ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md#insn-00c416ec) · [`00c416f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md#insn-00c416f0)
- 新版 `00c41768`（命令位置の公開資料なし） · `00c41788`（命令位置の公開資料なし） · `00c4178c`（命令位置の公開資料なし）

~~~diff
- 00c416cc ["INT_ADD", "register:40f0:8", ["const:c416cc:8", "const:4:8"]]
- 00c416cc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c41768 ["INT_ADD", "register:40f0:8", ["const:c41768:8", "const:4:8"]]
+ 00c41768 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c416cc bytes 55620094
+ 00c41768 bytes 62620094
- 00c416ec ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c41788 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c416ec bytes a80200d0
+ 00c41788 bytes a80200f0
- 00c416f0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00c416f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c416f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c416f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4178c ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00c4178c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4178c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4178c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c416f0 bytes 08413f91
+ 00c4178c bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84234df2f88de8ae79dbf32aae20f08d"></a>

### [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) → [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) FUN_00c417ec

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 12件 [`00c3a118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) [`00c3a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c46238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md) [`00c4632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md)
- 新版 呼出元 2件 [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 12件 [`00c3a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c462d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) [`00c463c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c41a94",
      "incomplete_value": false,
      "site": "00c41a94",
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
            "const:190:8"
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
    "old": {
      "definition_site": "00c41db0",
      "incomplete_value": false,
      "site": "00c41db0",
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
            "const:270:8"
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
    "old": {
      "definition_site": "00c4202c",
      "incomplete_value": false,
      "site": "00c4202c",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4184c",
      "DATA",
      [
        "storage",
        "00312adc",
        "switchD_00c417b8::switchdataD_00312adc",
        "ushort"
      ]
    ],
    [
      "00c41984",
      "PARAM",
      [
        "storage",
        "002ad1ed",
        null,
        "string"
      ]
    ],
    [
      "00c4199c",
      "PARAM",
      [
        "storage",
        "002ac4c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4184c",
      "DATA",
      [
        "storage",
        "00312b1c",
        "switchD_00c41854::switchdataD_00312b1c",
        "ushort"
      ]
    ],
    [
      "00c41984",
      "PARAM",
      [
        "storage",
        "002ad191",
        null,
        "string"
      ]
    ],
    [
      "00c4199c",
      "PARAM",
      [
        "storage",
        "002ac46c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md#insn-00c41c9c) · [`00c417a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md#insn-00c417a4) · [`00c417ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md#insn-00c417ac)
- 新版 `00c41d38`（命令位置の公開資料なし） · `00c41840`（命令位置の公開資料なし）

~~~diff
- 00c41c9c ["INT_ADD", "register:40f0:8", ["const:c41c9c:8", "const:4:8"]]
- 00c41c9c ["CALL", null, ["callee:00c3a1b4:8"]]
+ 00c41d38 ["INT_ADD", "register:40f0:8", ["const:c41d38:8", "const:4:8"]]
+ 00c41d38 ["CALL", null, ["callee:00c3a1b4:8"]]
- 00c41c9c bytes 1fe1ff97
+ 00c41d38 bytes 1fe1ff97
- 00c417a4 ["COPY", "tmp:0:8", ["const:adc:8"]]
- 00c417a4 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
- 00c417a4 ["INT_SCARRY", "register:106:1", ["register:4070:8", "tmp:0:8"]]
- 00c417a4 ["INT_ADD", "tmp:1:8", ["register:4070:8", "tmp:0:8"]]
+ 00c41840 ["COPY", "tmp:0:8", ["const:b1c:8"]]
+ 00c41840 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
+ 00c41840 ["INT_SCARRY", "register:106:1", ["register:4070:8", "tmp:0:8"]]
+ 00c41840 ["INT_ADD", "tmp:1:8", ["register:4070:8", "tmp:0:8"]]
- 00c417a4 bytes ce712b91
+ 00c41840 bytes ce712c91
- 00c417ac ["COPY", "register:4078:8", ["const:c417bc:8"]]
- 00c417ac bytes 8f000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d358f05680c51d2768511a6db38cedaa"></a>

### [`00c420d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md) → [`00c4216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) FUN_00c4216c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 3件 [`00c4955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 3件 [`00c495f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c422fc",
      "incomplete_value": false,
      "site": "00c422fc",
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
            "const:640:8"
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
    "old": {
      "definition_site": "00c42324",
      "incomplete_value": false,
      "site": "00c42324",
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
            "const:e5b:8"
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
    "old": {
      "definition_site": "00c423d4",
      "incomplete_value": false,
      "site": "00c423d4",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c42398",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c423c0",
      "DATA",
      [
        "storage",
        "002c0e5b",
        null,
        null
      ]
    ],
    [
      "00c42470",
      "DATA",
      [
        "storage",
        "00c987b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42398",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c423c0",
      "DATA",
      [
        "storage",
        "002c0e9b",
        null,
        null
      ]
    ],
    [
      "00c42470",
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c422cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md#insn-00c422cc) · [`00c422f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md#insn-00c422f0) · [`00c42314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md#insn-00c42314)
- 新版 `00c42368`（命令位置の公開資料なし） · `00c4238c`（命令位置の公開資料なし） · `00c423b0`（命令位置の公開資料なし）

~~~diff
- 00c422cc ["INT_ADD", "register:40f0:8", ["const:c422cc:8", "const:4:8"]]
- 00c422cc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c42368 ["INT_ADD", "register:40f0:8", ["const:c42368:8", "const:4:8"]]
+ 00c42368 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c422cc bytes 555f0094
+ 00c42368 bytes 625f0094
- 00c422f0 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c422f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c422f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c422f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4238c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4238c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4238c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4238c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c422f0 bytes 4a011991
+ 00c4238c bytes 4a411c91
- 00c42314 ["COPY", "tmp:0:8", ["const:e5b:8"]]
- 00c42314 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c42314 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c42314 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c423b0 ["COPY", "tmp:0:8", ["const:e9b:8"]]
+ 00c423b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c423b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c423b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c42314 bytes 4a6d3991
+ 00c423b0 bytes 4a6d3a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68d2b97c90f497bbfc613e0ed4f87d9d"></a>

### [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) → [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) FUN_00c42528

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) · 呼出先 5件 [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) · 呼出先 5件 [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c42554",
      "incomplete_value": false,
      "site": "00c42554",
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
            "const:900:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c425f0",
      "DATA",
      [
        "storage",
        "00c98900",
        null,
        "undefined *"
      ]
    ],
    [
      "00c426a0",
      "DATA",
      [
        "storage",
        "00c98900",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42750",
      "DATA",
      [
        "storage",
        "00c98970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c425f0",
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c426a0",
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42750",
      "DATA",
      [
        "storage",
        "00c98a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c424ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md#insn-00c424ec) · [`00c424fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md#insn-00c424fc) · [`00c42524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md#insn-00c42524)
- 新版 `00c42588`（命令位置の公開資料なし） · `00c42598`（命令位置の公開資料なし） · `00c425c0`（命令位置の公開資料なし）

~~~diff
- 00c424ec ["INT_ADD", "register:40f0:8", ["const:c424ec:8", "const:4:8"]]
- 00c424ec ["CALL", null, ["callee:00c3e04c:8"]]
+ 00c42588 ["INT_ADD", "register:40f0:8", ["const:c42588:8", "const:4:8"]]
+ 00c42588 ["CALL", null, ["callee:00c3e04c:8"]]
- 00c424ec bytes b1eeff97
+ 00c42588 bytes b1eeff97
- 00c424fc ["INT_ADD", "register:40f0:8", ["const:c424fc:8", "const:4:8"]]
- 00c424fc ["CALL", null, ["local:b0:8"]]
+ 00c42598 ["INT_ADD", "register:40f0:8", ["const:c42598:8", "const:4:8"]]
+ 00c42598 ["CALL", null, ["local:b0:8"]]
- 00c424fc bytes e4ffff97
+ 00c42598 bytes e4ffff97
- 00c42524 ["INT_ADD", "register:40f0:8", ["const:c42524:8", "const:4:8"]]
- 00c42524 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c425c0 ["INT_ADD", "register:40f0:8", ["const:c425c0:8", "const:4:8"]]
+ 00c425c0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c42524 bytes bf5e0094
+ 00c425c0 bytes cc5e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2824e8db9e4549fad76ac42093842543"></a>

### [`00c426f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md) → [`00c42790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md) FUN_00c42790

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c42758",
      "incomplete_value": true,
      "site": "00c42758",
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
      "00c427f4",
      "DATA",
      [
        "storage",
        "00c989e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c427f4",
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md#insn-00c42728) · [`00c4274c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md#insn-00c4274c) · [`00c42794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md#insn-00c42794)
- 新版 `00c427c4`（命令位置の公開資料なし） · `00c427e8`（命令位置の公開資料なし） · `00c42830`（命令位置の公開資料なし）

~~~diff
- 00c42728 ["INT_ADD", "register:40f0:8", ["const:c42728:8", "const:4:8"]]
- 00c42728 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
+ 00c427c4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c42728 bytes 3e5e0094
+ 00c427c4 bytes 4b5e0094
- 00c4274c ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00c4274c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4274c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4274c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c427e8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00c427e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c427e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c427e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4274c bytes 08812791
+ 00c427e8 bytes 08c12a91
- 00c42794 ["INT_ADD", "register:40f0:8", ["const:c42794:8", "const:4:8"]]
- 00c42794 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c42830 ["INT_ADD", "register:40f0:8", ["const:c42830:8", "const:4:8"]]
+ 00c42830 ["CALL", null, ["callee:00c580f0:8"]]
- 00c42794 bytes 23560094
+ 00c42830 bytes 30560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a1e727ee9bcea2ee0bc5bd14860b98b"></a>

### [`00c42798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md) → [`00c42834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md) FUN_00c42834

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c428b4",
      "incomplete_value": false,
      "site": "00c428b4",
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
            "const:a50:8"
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
      "00c42950",
      "DATA",
      [
        "storage",
        "00c98a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42950",
      "DATA",
      [
        "storage",
        "00c98b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c427b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md#insn-00c427b4) · [`00c427c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md#insn-00c427c4) · [`00c42880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md#insn-00c42880)
- 新版 `00c42850`（命令位置の公開資料なし） · `00c42860`（命令位置の公開資料なし） · `00c4291c`（命令位置の公開資料なし）

~~~diff
- 00c427b4 ["INT_ADD", "register:40f0:8", ["const:c427b4:8", "const:4:8"]]
- 00c427b4 ["CALL", null, ["callee:00c3ad68:8"]]
+ 00c42850 ["INT_ADD", "register:40f0:8", ["const:c42850:8", "const:4:8"]]
+ 00c42850 ["CALL", null, ["callee:00c3ad68:8"]]
- 00c427b4 bytes 46e1ff97
+ 00c42850 bytes 46e1ff97
- 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
- 00c427c4 ["CALL", null, ["callee:00c3fe18:8"]]
+ 00c42860 ["INT_ADD", "register:40f0:8", ["const:c42860:8", "const:4:8"]]
+ 00c42860 ["CALL", null, ["callee:00c3fe18:8"]]
- 00c427c4 bytes 6ef5ff97
+ 00c42860 bytes 6ef5ff97
- 00c42880 ["INT_ADD", "register:40f0:8", ["const:c42880:8", "const:4:8"]]
- 00c42880 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4291c ["INT_ADD", "register:40f0:8", ["const:c4291c:8", "const:4:8"]]
+ 00c4291c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c42880 bytes e85d0094
+ 00c4291c bytes f55d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a0d29c7d44760f55924c28fd49220d6"></a>

### [`00c42900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md) → [`00c4299c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md) FUN_00c4299c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c42968",
      "incomplete_value": false,
      "site": "00c42968",
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
            "const:40:8"
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
    "old": {
      "definition_site": "00c42994",
      "incomplete_value": false,
      "site": "00c42994",
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
            "const:e8a:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c42a04",
      "DATA",
      [
        "storage",
        "00c98040",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42a30",
      "DATA",
      [
        "storage",
        "002b7e8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c42a04",
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42a30",
      "DATA",
      [
        "storage",
        "002b7eca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md#insn-00c42938) · [`00c4295c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md#insn-00c4295c) · [`00c4297c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md#insn-00c4297c)
- 新版 `00c429d4`（命令位置の公開資料なし） · `00c429f8`（命令位置の公開資料なし） · `00c42a18`（命令位置の公開資料なし）

~~~diff
- 00c42938 ["INT_ADD", "register:40f0:8", ["const:c42938:8", "const:4:8"]]
- 00c42938 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c429d4 ["INT_ADD", "register:40f0:8", ["const:c429d4:8", "const:4:8"]]
+ 00c429d4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c42938 bytes ba5d0094
+ 00c429d4 bytes c75d0094
- 00c4295c ["COPY", "tmp:0:8", ["const:40:8"]]
- 00c4295c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4295c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4295c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c429f8 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00c429f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c429f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c429f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4295c bytes 08010191
+ 00c429f8 bytes 08410491
- 00c4297c ["COPY", "tmp:0:8", ["const:e8a:8"]]
- 00c4297c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4297c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4297c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c42a18 ["COPY", "tmp:0:8", ["const:eca:8"]]
+ 00c42a18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c42a18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c42a18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4297c bytes 29293a91
+ 00c42a18 bytes 29293b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386d190716295fc27abf05daa27e1f1a"></a>

### [`00c429c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md) → [`00c42a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md) FUN_00c42a5c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 9件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 9件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c42e50",
      "incomplete_value": false,
      "site": "00c42e50",
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
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c42d48",
      "DATA",
      [
        "storage",
        "00c98ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42ddc",
      "DATA",
      [
        "storage",
        "00c98b30",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42ddc",
      "DATA",
      [
        "storage",
        "00c98ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42d48",
      "DATA",
      [
        "storage",
        "00c98b90",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42ddc",
      "DATA",
      [
        "storage",
        "00c98c00",
        null,
        "undefined *"
      ]
    ],
    [
      "00c42ddc",
      "DATA",
      [
        "storage",
        "00c98c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md#insn-00c42a5c) · [`00c42aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md#insn-00c42aa4) · [`00c42ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md#insn-00c42ad4)
- 新版 `00c42af8`（命令位置の公開資料なし） · `00c42b40`（命令位置の公開資料なし） · `00c42b70`（命令位置の公開資料なし）

~~~diff
- 00c42a5c ["INT_ADD", "register:40f0:8", ["const:c42a5c:8", "const:4:8"]]
- 00c42a5c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c42af8 ["INT_ADD", "register:40f0:8", ["const:c42af8:8", "const:4:8"]]
+ 00c42af8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c42a5c bytes 915d0094
+ 00c42af8 bytes 9e5d0094
- 00c42aa4 ["INT_ADD", "register:40f0:8", ["const:c42aa4:8", "const:4:8"]]
- 00c42aa4 ["CALL", null, ["callee:00c3ad68:8"]]
+ 00c42b40 ["INT_ADD", "register:40f0:8", ["const:c42b40:8", "const:4:8"]]
+ 00c42b40 ["CALL", null, ["callee:00c3ad68:8"]]
- 00c42aa4 bytes 8ae0ff97
+ 00c42b40 bytes 8ae0ff97
- 00c42ad4 ["INT_ADD", "register:40f0:8", ["const:c42ad4:8", "const:4:8"]]
- 00c42ad4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c42b70 ["INT_ADD", "register:40f0:8", ["const:c42b70:8", "const:4:8"]]
+ 00c42b70 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c42ad4 bytes 535d0094
+ 00c42b70 bytes 605d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2533b6e1e48f57718adcd22eec314fb"></a>

### [`00c42e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md) → [`00c42f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md) FUN_00c42f2c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 8件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 8件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c43174",
      "incomplete_value": true,
      "site": "00c43174",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c43038",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43210",
      "DATA",
      [
        "storage",
        "00c98c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43038",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43210",
      "DATA",
      [
        "storage",
        "00c98d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md#insn-00c42eb8) · [`00c42ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md#insn-00c42ec8) · [`00c42f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md#insn-00c42f60)
- 新版 `00c42f54`（命令位置の公開資料なし） · `00c42f64`（命令位置の公開資料なし） · `00c42ffc`（命令位置の公開資料なし）

~~~diff
- 00c42eb8 ["INT_ADD", "register:40f0:8", ["const:c42eb8:8", "const:4:8"]]
- 00c42eb8 ["CALL", null, ["callee:00c3ad68:8"]]
+ 00c42f54 ["INT_ADD", "register:40f0:8", ["const:c42f54:8", "const:4:8"]]
+ 00c42f54 ["CALL", null, ["callee:00c3ad68:8"]]
- 00c42eb8 bytes 85dfff97
+ 00c42f54 bytes 85dfff97
- 00c42ec8 ["INT_ADD", "register:40f0:8", ["const:c42ec8:8", "const:4:8"]]
- 00c42ec8 ["CALL", null, ["callee:00c3fe18:8"]]
+ 00c42f64 ["INT_ADD", "register:40f0:8", ["const:c42f64:8", "const:4:8"]]
+ 00c42f64 ["CALL", null, ["callee:00c3fe18:8"]]
- 00c42ec8 bytes adf3ff97
+ 00c42f64 bytes adf3ff97
- 00c42f60 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c42f60 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 00c42f60 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 00c42f60 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 00c42ffc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c42ffc ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 00c42ffc ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 00c42ffc ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 00c42f60 bytes 9c031991
+ 00c42ffc bytes 9c431c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea35a0767f12a542b5617cb64296968"></a>

### [`00c433d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md) → [`00c43474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md) FUN_00c43474

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4343c",
      "incomplete_value": false,
      "site": "00c4343c",
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
      "00c434d8",
      "DATA",
      [
        "storage",
        "00c98d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c434d8",
      "DATA",
      [
        "storage",
        "00c98e30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4340c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md#insn-00c4340c) · [`00c43430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md#insn-00c43430) · [`00c43470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md#insn-00c43470)
- 新版 `00c434a8`（命令位置の公開資料なし） · `00c434cc`（命令位置の公開資料なし） · `00c4350c`（命令位置の公開資料なし）

~~~diff
- 00c4340c ["INT_ADD", "register:40f0:8", ["const:c4340c:8", "const:4:8"]]
- 00c4340c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c434a8 ["INT_ADD", "register:40f0:8", ["const:c434a8:8", "const:4:8"]]
+ 00c434a8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4340c bytes 055b0094
+ 00c434a8 bytes 125b0094
- 00c43430 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00c43430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c434cc ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00c434cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c434cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c434cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43430 bytes 08813591
+ 00c434cc bytes 08c13891
- 00c43470 ["INT_ADD", "register:40f0:8", ["const:c43470:8", "const:4:8"]]
- 00c43470 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4350c ["INT_ADD", "register:40f0:8", ["const:c4350c:8", "const:4:8"]]
+ 00c4350c ["CALL", null, ["callee:00c580f0:8"]]
- 00c43470 bytes ec520094
+ 00c4350c bytes f9520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-672c1d29e5193b855a8ed02525a44aad"></a>

### [`00c43474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md) → [`00c43510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md) FUN_00c43510

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c434dc",
      "incomplete_value": false,
      "site": "00c434dc",
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
            "const:9e0:8"
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
      "00c43578",
      "DATA",
      [
        "storage",
        "00c989e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43578",
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c434ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md#insn-00c434ac) · [`00c434d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md#insn-00c434d0) · [`00c4351c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md#insn-00c4351c)
- 新版 `00c43548`（命令位置の公開資料なし） · `00c4356c`（命令位置の公開資料なし） · `00c435b8`（命令位置の公開資料なし）

~~~diff
- 00c434ac ["INT_ADD", "register:40f0:8", ["const:c434ac:8", "const:4:8"]]
- 00c434ac ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c43548 ["INT_ADD", "register:40f0:8", ["const:c43548:8", "const:4:8"]]
+ 00c43548 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c434ac bytes dd5a0094
+ 00c43548 bytes ea5a0094
- 00c434d0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00c434d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c434d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c434d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4356c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00c4356c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4356c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4356c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c434d0 bytes 08812791
+ 00c4356c bytes 08c12a91
- 00c4351c ["INT_ADD", "register:40f0:8", ["const:c4351c:8", "const:4:8"]]
- 00c4351c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c435b8 ["INT_ADD", "register:40f0:8", ["const:c435b8:8", "const:4:8"]]
+ 00c435b8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4351c bytes c1520094
+ 00c435b8 bytes ce520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a329a25e16ed7dc2ac2270ee76aaab93"></a>

### [`00c435cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md) → [`00c43668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md) FUN_00c43668

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c43630",
      "incomplete_value": true,
      "site": "00c43630",
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
            "const:dd0:8"
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
      "00c436cc",
      "DATA",
      [
        "storage",
        "00c98dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c436cc",
      "DATA",
      [
        "storage",
        "00c98ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md#insn-00c43600) · [`00c43624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md#insn-00c43624) · [`00c43668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md#insn-00c43668)
- 新版 `00c4369c`（命令位置の公開資料なし） · `00c436c0`（命令位置の公開資料なし） · `00c43704`（命令位置の公開資料なし）

~~~diff
- 00c43600 ["INT_ADD", "register:40f0:8", ["const:c43600:8", "const:4:8"]]
- 00c43600 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4369c ["INT_ADD", "register:40f0:8", ["const:c4369c:8", "const:4:8"]]
+ 00c4369c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c43600 bytes 885a0094
+ 00c4369c bytes 955a0094
- 00c43624 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00c43624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c436c0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00c436c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c436c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c436c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43624 bytes 08413791
+ 00c436c0 bytes 08813a91
- 00c43668 ["INT_ADD", "register:40f0:8", ["const:c43668:8", "const:4:8"]]
- 00c43668 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c43704 ["INT_ADD", "register:40f0:8", ["const:c43704:8", "const:4:8"]]
+ 00c43704 ["CALL", null, ["callee:00c580f0:8"]]
- 00c43668 bytes 6e520094
+ 00c43704 bytes 7b520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e6d57a9cccbdf5acfa1caafcded7092"></a>

### [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) → [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) FUN_00c43708

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 7件 [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3ea94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 7件 [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.34% / 新版 97.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c43740",
      "incomplete_value": false,
      "site": "00c43740",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c43a40",
      "incomplete_value": false,
      "site": "00c43a40",
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
            "const:540:8"
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
    "old": {
      "definition_site": "00c43b10",
      "incomplete_value": false,
      "site": "00c43b10",
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
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c437dc",
      "DATA",
      [
        "storage",
        "00c99000",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43910",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43954",
      "DATA",
      [
        "storage",
        "00c98e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c437dc",
      "DATA",
      [
        "storage",
        "00c990d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43910",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43954",
      "DATA",
      [
        "storage",
        "00c98f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c436e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md#insn-00c436e4) · [`00c4370c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md#insn-00c4370c) · [`00c43734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md#insn-00c43734)
- 新版 `00c43780`（命令位置の公開資料なし） · `00c437a8`（命令位置の公開資料なし） · `00c437d0`（命令位置の公開資料なし）

~~~diff
- 00c436e4 ["INT_ADD", "register:40f0:8", ["const:c436e4:8", "const:4:8"]]
- 00c436e4 ["CALL", null, ["callee:00c4b848:8"]]
+ 00c43780 ["INT_ADD", "register:40f0:8", ["const:c43780:8", "const:4:8"]]
+ 00c43780 ["CALL", null, ["callee:00c4b848:8"]]
- 00c436e4 bytes 32200094
+ 00c43780 bytes 32200094
- 00c4370c ["INT_ADD", "register:40f0:8", ["const:c4370c:8", "const:4:8"]]
- 00c4370c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c437a8 ["INT_ADD", "register:40f0:8", ["const:c437a8:8", "const:4:8"]]
+ 00c437a8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4370c bytes 455a0094
+ 00c437a8 bytes 525a0094
- 00c43734 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00c43734 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c43734 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c43734 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c437d0 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 00c437d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c437d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c437d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c43734 bytes 4a010091
+ 00c437d0 bytes 4a410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5d60749feca20652c68899f7a43dc57"></a>

### [`00c43ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md) → [`00c43d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md) FUN_00c43d7c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c43d54",
      "incomplete_value": false,
      "site": "00c43d54",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c43df0",
      "DATA",
      [
        "storage",
        "00c97b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43df0",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md#insn-00c43d24) · [`00c43d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md#insn-00c43d48) · [`00c43da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md#insn-00c43da8)
- 新版 `00c43dc0`（命令位置の公開資料なし） · `00c43de4`（命令位置の公開資料なし） · `00c43e44`（命令位置の公開資料なし）

~~~diff
- 00c43d24 ["INT_ADD", "register:40f0:8", ["const:c43d24:8", "const:4:8"]]
- 00c43d24 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c43dc0 ["INT_ADD", "register:40f0:8", ["const:c43dc0:8", "const:4:8"]]
+ 00c43dc0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c43d24 bytes bf580094
+ 00c43dc0 bytes cc580094
- 00c43d48 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00c43d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c43de4 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00c43de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c43de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43d48 bytes 08c12d91
+ 00c43de4 bytes 08013191
- 00c43da8 ["INT_ADD", "register:40f0:8", ["const:c43da8:8", "const:4:8"]]
- 00c43da8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c43e44 ["INT_ADD", "register:40f0:8", ["const:c43e44:8", "const:4:8"]]
+ 00c43e44 ["CALL", null, ["callee:00c580f0:8"]]
- 00c43da8 bytes 9e500094
+ 00c43e44 bytes ab500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd16c06e577f8e6227169f51d94861b"></a>

### [`00c442c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md) → [`00c4435c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md) FUN_00c4435c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c44330",
      "incomplete_value": false,
      "site": "00c44330",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c443cc",
      "DATA",
      [
        "storage",
        "00c97be0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c443cc",
      "DATA",
      [
        "storage",
        "00c97cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c44300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md#insn-00c44300) · [`00c44324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md#insn-00c44324) · [`00c4437c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md#insn-00c4437c)
- 新版 `00c4439c`（命令位置の公開資料なし） · `00c443c0`（命令位置の公開資料なし） · `00c44418`（命令位置の公開資料なし）

~~~diff
- 00c44300 ["INT_ADD", "register:40f0:8", ["const:c44300:8", "const:4:8"]]
- 00c44300 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4439c ["INT_ADD", "register:40f0:8", ["const:c4439c:8", "const:4:8"]]
+ 00c4439c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c44300 bytes 48570094
+ 00c4439c bytes 55570094
- 00c44324 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00c44324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c44324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c44324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c443c0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00c443c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c443c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c443c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c44324 bytes 08812f91
+ 00c443c0 bytes 08c13291
- 00c4437c ["INT_ADD", "register:40f0:8", ["const:c4437c:8", "const:4:8"]]
- 00c4437c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c44418 ["INT_ADD", "register:40f0:8", ["const:c44418:8", "const:4:8"]]
+ 00c44418 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4437c bytes 294f0094
+ 00c44418 bytes 364f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1197dccf9d1ad65ecc53196f310b87"></a>

### [`00c46238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md) → [`00c462d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) FUN_00c462d4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 3件 [`00c3ab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c462e0",
      "incomplete_value": false,
      "site": "00c462e0",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4637c",
      "DATA",
      [
        "storage",
        "00c980b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4637c",
      "DATA",
      [
        "storage",
        "00c98180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md#insn-00c46260) · [`00c462a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md#insn-00c462a8) · [`00c462dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md#insn-00c462dc)
- 新版 `00c462fc`（命令位置の公開資料なし） · `00c46344`（命令位置の公開資料なし） · `00c46378`（命令位置の公開資料なし）

~~~diff
- 00c46260 ["INT_ADD", "register:40f0:8", ["const:c46260:8", "const:4:8"]]
- 00c46260 ["CALL", null, ["callee:00c3ac28:8"]]
+ 00c462fc ["INT_ADD", "register:40f0:8", ["const:c462fc:8", "const:4:8"]]
+ 00c462fc ["CALL", null, ["callee:00c3ac28:8"]]
- 00c46260 bytes 4bd2ff97
+ 00c462fc bytes 4bd2ff97
- 00c462a8 ["INT_ADD", "register:40f0:8", ["const:c462a8:8", "const:4:8"]]
- 00c462a8 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c46344 ["INT_ADD", "register:40f0:8", ["const:c46344:8", "const:4:8"]]
+ 00c46344 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c462a8 bytes 5e4f0094
+ 00c46344 bytes 6b4f0094
- 00c462dc ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00c462dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c462dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c462dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c46378 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 00c46378 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c46378 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c46378 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c462dc bytes 29c10291
+ 00c46378 bytes 29010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2493b9fac85d72778fb8e38b13a6a0e9"></a>

### [`00c4632c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md) → [`00c463c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md) FUN_00c463c8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4639c",
      "incomplete_value": false,
      "site": "00c463a8",
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
            "const:120:8"
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
      "00c46444",
      "DATA",
      [
        "storage",
        "00c98120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46444",
      "DATA",
      [
        "storage",
        "00c981f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md#insn-00c46360) · [`00c4639c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md#insn-00c4639c) · [`00c463d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md#insn-00c463d0)
- 新版 `00c463fc`（命令位置の公開資料なし） · `00c46438`（命令位置の公開資料なし） · `00c4646c`（命令位置の公開資料なし）

~~~diff
- 00c46360 ["INT_ADD", "register:40f0:8", ["const:c46360:8", "const:4:8"]]
- 00c46360 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c463fc ["INT_ADD", "register:40f0:8", ["const:c463fc:8", "const:4:8"]]
+ 00c463fc ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c46360 bytes 304f0094
+ 00c463fc bytes 3d4f0094
- 00c4639c ["COPY", "tmp:0:8", ["const:120:8"]]
- 00c4639c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4639c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4639c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46438 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00c46438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4639c bytes 08810491
+ 00c46438 bytes 08c10791
- 00c463d0 ["INT_ADD", "register:40f0:8", ["const:c463d0:8", "const:4:8"]]
- 00c463d0 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4646c ["INT_ADD", "register:40f0:8", ["const:c4646c:8", "const:4:8"]]
+ 00c4646c ["CALL", null, ["callee:00c580f0:8"]]
- 00c463d0 bytes 14470094
+ 00c4646c bytes 21470094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbe5212a57168c56dee7d412a6f6c19a"></a>

### [`00c463d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md) → [`00c46470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md) FUN_00c46470

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c46438",
      "incomplete_value": false,
      "site": "00c46438",
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
            "const:2e0:8"
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
      "00c464d4",
      "DATA",
      [
        "storage",
        "00c982e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c464d4",
      "DATA",
      [
        "storage",
        "00c983b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md#insn-00c46408) · [`00c4642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md#insn-00c4642c) · [`00c46470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md#insn-00c46470)
- 新版 `00c464a4`（命令位置の公開資料なし） · `00c464c8`（命令位置の公開資料なし） · `00c4650c`（命令位置の公開資料なし）

~~~diff
- 00c46408 ["INT_ADD", "register:40f0:8", ["const:c46408:8", "const:4:8"]]
- 00c46408 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c464a4 ["INT_ADD", "register:40f0:8", ["const:c464a4:8", "const:4:8"]]
+ 00c464a4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c46408 bytes 064f0094
+ 00c464a4 bytes 134f0094
- 00c4642c ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 00c4642c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4642c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4642c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c464c8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 00c464c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c464c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c464c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4642c bytes 08810b91
+ 00c464c8 bytes 08c10e91
- 00c46470 ["INT_ADD", "register:40f0:8", ["const:c46470:8", "const:4:8"]]
- 00c46470 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4650c ["INT_ADD", "register:40f0:8", ["const:c4650c:8", "const:4:8"]]
+ 00c4650c ["CALL", null, ["callee:00c580f0:8"]]
- 00c46470 bytes ec460094
+ 00c4650c bytes f9460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0768a39dda5f185f09424ba860a92240"></a>

### [`00c46474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md) → [`00c46510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md) FUN_00c46510

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c464e0",
      "incomplete_value": false,
      "site": "00c464e0",
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
            "const:640:8"
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
      "00c4657c",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4657c",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c464a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md#insn-00c464a8) · [`00c464d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md#insn-00c464d0) · [`00c464d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md#insn-00c464d8)
- 新版 `00c46544`（命令位置の公開資料なし） · `00c4656c`（命令位置の公開資料なし） · `00c46574`（命令位置の公開資料なし）

~~~diff
- 00c464a8 ["INT_ADD", "register:40f0:8", ["const:c464a8:8", "const:4:8"]]
- 00c464a8 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c46544 ["INT_ADD", "register:40f0:8", ["const:c46544:8", "const:4:8"]]
+ 00c46544 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c464a8 bytes de4e0094
+ 00c46544 bytes eb4e0094
- 00c464d0 ["INT_ADD", "register:40f0:8", ["const:c464d0:8", "const:4:8"]]
- 00c464d0 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c4656c ["INT_ADD", "register:40f0:8", ["const:c4656c:8", "const:4:8"]]
+ 00c4656c ["CALL", null, ["callee:00c580b0:8"]]
- 00c464d0 bytes c4460094
+ 00c4656c bytes d1460094
- 00c464d8 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c464d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c464d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c464d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c46574 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c46574 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c46574 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c46574 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c464d8 bytes 29011991
+ 00c46574 bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f89dbd85af816091b54405d78bdc32"></a>

### [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) → [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) FUN_00c465bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 14件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md)
- 新版 呼出元 2件 [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 14件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c46640",
      "incomplete_value": false,
      "site": "00c46640",
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
            "const:640:8"
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
    "old": {
      "definition_site": "00c46668",
      "incomplete_value": false,
      "site": "00c46668",
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
            "const:d88:8"
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
    "old": {
      "definition_site": "00c467f4",
      "incomplete_value": false,
      "site": "00c467f4",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c466dc",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c46704",
      "DATA",
      [
        "storage",
        "002b8d88",
        null,
        "string"
      ]
    ],
    [
      "00c46890",
      "DATA",
      [
        "storage",
        "00c98350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c466dc",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c46704",
      "DATA",
      [
        "storage",
        "002b8d34",
        null,
        "string"
      ]
    ],
    [
      "00c46890",
      "DATA",
      [
        "storage",
        "00c98420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md#insn-00c46c34) · [`00c46c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md#insn-00c46c58) · [`00c46610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md#insn-00c46610)
- 新版 `00c46cd0`（命令位置の公開資料なし） · `00c46cf4`（命令位置の公開資料なし） · `00c466ac`（命令位置の公開資料なし）

~~~diff
- 00c46c34 ["INT_ADD", "register:40f0:8", ["const:c46c34:8", "const:4:8"]]
- 00c46c34 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c46cd0 ["INT_ADD", "register:40f0:8", ["const:c46cd0:8", "const:4:8"]]
+ 00c46cd0 ["CALL", null, ["callee:00c380a8:8"]]
- 00c46c34 bytes f6c4ff97
+ 00c46cd0 bytes f6c4ff97
- 00c46c58 ["INT_ADD", "register:40f0:8", ["const:c46c58:8", "const:4:8"]]
- 00c46c58 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c46cf4 ["INT_ADD", "register:40f0:8", ["const:c46cf4:8", "const:4:8"]]
+ 00c46cf4 ["CALL", null, ["callee:00c380a8:8"]]
- 00c46c58 bytes edc4ff97
+ 00c46cf4 bytes edc4ff97
- 00c46610 ["INT_ADD", "register:40f0:8", ["const:c46610:8", "const:4:8"]]
- 00c46610 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c466ac ["INT_ADD", "register:40f0:8", ["const:c466ac:8", "const:4:8"]]
+ 00c466ac ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c46610 bytes 844e0094
+ 00c466ac bytes 914e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-228ca69ecb46ba7ac6ff3efeffdd4ab8"></a>

### [`00c46ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md) → [`00c46d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md) FUN_00c46d3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c46d04",
      "incomplete_value": false,
      "site": "00c46d04",
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
            "const:6d0:8"
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
      "00c46da0",
      "DATA",
      [
        "storage",
        "00c986d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46da0",
      "DATA",
      [
        "storage",
        "00c987a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md#insn-00c46cd4) · [`00c46cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md#insn-00c46cf8) · [`00c46d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md#insn-00c46d3c)
- 新版 `00c46d70`（命令位置の公開資料なし） · `00c46d94`（命令位置の公開資料なし） · `00c46dd8`（命令位置の公開資料なし）

~~~diff
- 00c46cd4 ["INT_ADD", "register:40f0:8", ["const:c46cd4:8", "const:4:8"]]
- 00c46cd4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c46d70 ["INT_ADD", "register:40f0:8", ["const:c46d70:8", "const:4:8"]]
+ 00c46d70 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c46cd4 bytes d34c0094
+ 00c46d70 bytes e04c0094
- 00c46cf8 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00c46cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46d94 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00c46d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46cf8 bytes 08411b91
+ 00c46d94 bytes 08811e91
- 00c46d3c ["INT_ADD", "register:40f0:8", ["const:c46d3c:8", "const:4:8"]]
- 00c46d3c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c46dd8 ["INT_ADD", "register:40f0:8", ["const:c46dd8:8", "const:4:8"]]
+ 00c46dd8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c46d3c bytes b9440094
+ 00c46dd8 bytes c6440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a95120c7b2f9c7ade856b45d8d1984c"></a>

### [`00c46d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md) → [`00c46ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md) FUN_00c46ddc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c46da8",
      "incomplete_value": false,
      "site": "00c46da8",
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
            "const:740:8"
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
      "00c46e44",
      "DATA",
      [
        "storage",
        "00c98740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46e44",
      "DATA",
      [
        "storage",
        "00c98810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md#insn-00c46d78) · [`00c46d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md#insn-00c46d9c) · [`00c46de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md#insn-00c46de8)
- 新版 `00c46e14`（命令位置の公開資料なし） · `00c46e38`（命令位置の公開資料なし） · `00c46e84`（命令位置の公開資料なし）

~~~diff
- 00c46d78 ["INT_ADD", "register:40f0:8", ["const:c46d78:8", "const:4:8"]]
- 00c46d78 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c46e14 ["INT_ADD", "register:40f0:8", ["const:c46e14:8", "const:4:8"]]
+ 00c46e14 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c46d78 bytes aa4c0094
+ 00c46e14 bytes b74c0094
- 00c46d9c ["COPY", "tmp:0:8", ["const:740:8"]]
- 00c46d9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46d9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46d9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46e38 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00c46e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46d9c bytes 08011d91
+ 00c46e38 bytes 08412091
- 00c46de8 ["INT_ADD", "register:40f0:8", ["const:c46de8:8", "const:4:8"]]
- 00c46de8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c46e84 ["INT_ADD", "register:40f0:8", ["const:c46e84:8", "const:4:8"]]
+ 00c46e84 ["CALL", null, ["callee:00c580f0:8"]]
- 00c46de8 bytes 8e440094
+ 00c46e84 bytes 9b440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870aec35a34d376f9ead46887dbb64dd"></a>

### [`00c47190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md) → [`00c4722c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md) FUN_00c4722c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c472b4",
      "incomplete_value": false,
      "site": "00c472cc",
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
            "const:d80:8"
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
      "00c47350",
      "PARAM",
      [
        "storage",
        "002b8d80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c47350",
      "PARAM",
      [
        "storage",
        "002b8d2c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c472cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md#insn-00c472cc) · [`00c472b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md#insn-00c472b4) · [`00c47300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md#insn-00c47300)
- 新版 `00c47368`（命令位置の公開資料なし） · `00c47350`（命令位置の公開資料なし） · `00c4739c`（命令位置の公開資料なし）

~~~diff
- 00c472cc ["INT_ADD", "register:40f0:8", ["const:c472cc:8", "const:4:8"]]
- 00c472cc ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00c47368 ["INT_ADD", "register:40f0:8", ["const:c47368:8", "const:4:8"]]
+ 00c47368 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00c472cc bytes 8d5b0094
+ 00c47368 bytes 9a5b0094
- 00c472b4 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00c472b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c472b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c472b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c47350 ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00c47350 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47350 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47350 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c472b4 bytes 42003691
+ 00c47350 bytes 42b03491
- 00c47300 ["INT_ADD", "register:40f0:8", ["const:c47300:8", "const:4:8"]]
- 00c47300 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4739c ["INT_ADD", "register:40f0:8", ["const:c4739c:8", "const:4:8"]]
+ 00c4739c ["CALL", null, ["callee:00c5a170:8"]]
- 00c47300 bytes 684b0094
+ 00c4739c bytes 754b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4360a8999423ab9bf7828d0c926d6e63"></a>

### [`00c4734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md) → [`00c473e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md) FUN_00c473e8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c47488",
      "incomplete_value": false,
      "site": "00c47498",
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
            "const:51d:8"
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
      "00c47524",
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c47524",
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md#insn-00c47498) · [`00c47488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md#insn-00c47488) · [`00c474cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md#insn-00c474cc)
- 新版 `00c47534`（命令位置の公開資料なし） · `00c47524`（命令位置の公開資料なし） · `00c47568`（命令位置の公開資料なし）

~~~diff
- 00c47498 ["INT_ADD", "register:40f0:8", ["const:c47498:8", "const:4:8"]]
- 00c47498 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00c47534 ["INT_ADD", "register:40f0:8", ["const:c47534:8", "const:4:8"]]
+ 00c47534 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00c47498 bytes 1a5b0094
+ 00c47534 bytes 275b0094
- 00c47488 ["COPY", "tmp:0:8", ["const:51d:8"]]
- 00c47488 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c47488 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c47488 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c47524 ["COPY", "tmp:0:8", ["const:4c1:8"]]
+ 00c47524 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47524 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47524 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c47488 bytes 42741491
+ 00c47524 bytes 42041391
- 00c474cc ["INT_ADD", "register:40f0:8", ["const:c474cc:8", "const:4:8"]]
- 00c474cc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c47568 ["INT_ADD", "register:40f0:8", ["const:c47568:8", "const:4:8"]]
+ 00c47568 ["CALL", null, ["callee:00c5a170:8"]]
- 00c474cc bytes f54a0094
+ 00c47568 bytes 024b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c625105ebad325b54b40b6633c762ec"></a>

### [`00c47518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md) → [`00c475b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md) FUN_00c475b4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c4768c",
      "incomplete_value": false,
      "site": "00c476a0",
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
            "const:e4e:8"
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
      "00c47728",
      "PARAM",
      [
        "storage",
        "002b9e4e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c47728",
      "PARAM",
      [
        "storage",
        "002b9dfa",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c476a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md#insn-00c476a0) · [`00c4768c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md#insn-00c4768c) · [`00c476d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md#insn-00c476d4)
- 新版 `00c4773c`（命令位置の公開資料なし） · `00c47728`（命令位置の公開資料なし） · `00c47770`（命令位置の公開資料なし）

~~~diff
- 00c476a0 ["INT_ADD", "register:40f0:8", ["const:c476a0:8", "const:4:8"]]
- 00c476a0 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00c4773c ["INT_ADD", "register:40f0:8", ["const:c4773c:8", "const:4:8"]]
+ 00c4773c ["CALL", null, ["callee:00c5e1d0:8"]]
- 00c476a0 bytes 985a0094
+ 00c4773c bytes a55a0094
- 00c4768c ["COPY", "tmp:0:8", ["const:e4e:8"]]
- 00c4768c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c4768c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c4768c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c47728 ["COPY", "tmp:0:8", ["const:dfa:8"]]
+ 00c47728 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47728 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47728 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c4768c bytes 42383991
+ 00c47728 bytes 42e83791
- 00c476d4 ["INT_ADD", "register:40f0:8", ["const:c476d4:8", "const:4:8"]]
- 00c476d4 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c47770 ["INT_ADD", "register:40f0:8", ["const:c47770:8", "const:4:8"]]
+ 00c47770 ["CALL", null, ["callee:00c5a170:8"]]
- 00c476d4 bytes 734a0094
+ 00c47770 bytes 804a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f9969f0cafdd6c1b7c706136c00ef3"></a>

### [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) → [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) FUN_00c478d0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) · 呼出先 14件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md)
- 新版 呼出元 3件 [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 14件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.80% / 新版 96.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c47950",
      "incomplete_value": false,
      "site": "00c47950",
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
            "const:3c0:8"
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
    "old": {
      "definition_site": "00c47a28",
      "incomplete_value": false,
      "site": "00c47a28",
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
            "const:3c0:8"
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
    "old": {
      "definition_site": "00c47ae8",
      "incomplete_value": false,
      "site": "00c47ae8",
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
            "const:3c0:8"
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
      "00c479ec",
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47ac4",
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47b84",
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c479ec",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47ac4",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      "00c47b84",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md#insn-00c47d44) · [`00c48160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md#insn-00c48160) · [`00c48170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md#insn-00c48170)
- 新版 `00c47de0`（命令位置の公開資料なし） · `00c481fc`（命令位置の公開資料なし） · `00c4820c`（命令位置の公開資料なし）

~~~diff
- 00c47d44 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00c47d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c47d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c47d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c47de0 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 00c47de0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c47de0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c47de0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c47d44 bytes 08811291
+ 00c47de0 bytes 08c11591
- 00c48160 ["INT_ADD", "register:40f0:8", ["const:c48160:8", "const:4:8"]]
- 00c48160 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c481fc ["INT_ADD", "register:40f0:8", ["const:c481fc:8", "const:4:8"]]
+ 00c481fc ["CALL", null, ["callee:00c380a8:8"]]
- 00c48160 bytes abbfff97
+ 00c481fc bytes abbfff97
- 00c48170 ["INT_ADD", "register:40f0:8", ["const:c48170:8", "const:4:8"]]
- 00c48170 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c4820c ["INT_ADD", "register:40f0:8", ["const:c4820c:8", "const:4:8"]]
+ 00c4820c ["CALL", null, ["callee:00c5b210:8"]]
- 00c48170 bytes f44b0094
+ 00c4820c bytes 014c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d838c978387dd32215b6a0b91468eb5"></a>

### [`00c481a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md) → [`00c4823c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md) FUN_00c4823c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c46520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4821c",
      "incomplete_value": false,
      "site": "00c4821c",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c482b8",
      "DATA",
      [
        "storage",
        "00c98660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c482b8",
      "DATA",
      [
        "storage",
        "00c98730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c481ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md#insn-00c481ec) · [`00c48210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md#insn-00c48210) · [`00c4827c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md#insn-00c4827c)
- 新版 `00c48288`（命令位置の公開資料なし） · `00c482ac`（命令位置の公開資料なし） · `00c48318`（命令位置の公開資料なし）

~~~diff
- 00c481ec ["INT_ADD", "register:40f0:8", ["const:c481ec:8", "const:4:8"]]
- 00c481ec ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c48288 ["INT_ADD", "register:40f0:8", ["const:c48288:8", "const:4:8"]]
+ 00c48288 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c481ec bytes 8d470094
+ 00c48288 bytes 9a470094
- 00c48210 ["COPY", "tmp:0:8", ["const:660:8"]]
- 00c48210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c48210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c48210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c482ac ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00c482ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c482ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c482ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c48210 bytes 08811991
+ 00c482ac bytes 08c11c91
- 00c4827c ["INT_ADD", "register:40f0:8", ["const:c4827c:8", "const:4:8"]]
- 00c4827c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c48318 ["INT_ADD", "register:40f0:8", ["const:c48318:8", "const:4:8"]]
+ 00c48318 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4827c bytes 693f0094
+ 00c48318 bytes 763f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1bddc706d09da00c92747cac468e6d6"></a>

### [`00c48280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md) → [`00c4831c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md) FUN_00c4831c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c482dc",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:ee2:8"
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
    "old": {
      "definition_site": "00c482e4",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:896:8"
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
    "old": {
      "definition_site": "00c482ec",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c48378",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c48380",
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      "00c48388",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c48378",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c48380",
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      "00c48388",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c482f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md#insn-00c482f4) · [`00c482dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md#insn-00c482dc) · [`00c482e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md#insn-00c482e4)
- 新版 `00c48390`（命令位置の公開資料なし） · `00c48378`（命令位置の公開資料なし） · `00c48380`（命令位置の公開資料なし）

~~~diff
- 00c482f4 ["INT_ADD", "register:40f0:8", ["const:c482f4:8", "const:4:8"]]
- 00c482f4 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c48390 ["INT_ADD", "register:40f0:8", ["const:c48390:8", "const:4:8"]]
+ 00c48390 ["CALL", null, ["callee:00c380a8:8"]]
- 00c482f4 bytes 46bfff97
+ 00c48390 bytes 46bfff97
- 00c482dc ["COPY", "tmp:0:8", ["const:ee2:8"]]
- 00c482dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c482dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c482dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c48378 ["COPY", "tmp:0:8", ["const:e95:8"]]
+ 00c48378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c48378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c48378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c482dc bytes 00883b91
+ 00c48378 bytes 00543a91
- 00c482e4 ["COPY", "tmp:0:8", ["const:896:8"]]
- 00c482e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c482e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c482e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c48380 ["COPY", "tmp:0:8", ["const:8c7:8"]]
+ 00c48380 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c48380 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c48380 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c482e4 bytes 21582291
+ 00c48380 bytes 211c2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5ffbcd549d66378f76e81a215e4a029"></a>

### [`00c4844c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md) → [`00c484e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md) FUN_00c484e8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c47834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c484b0",
      "incomplete_value": false,
      "site": "00c484b0",
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
      "00c4854c",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4854c",
      "DATA",
      [
        "storage",
        "00c986c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md#insn-00c48480) · [`00c484a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md#insn-00c484a4) · [`00c484e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md#insn-00c484e8)
- 新版 `00c4851c`（命令位置の公開資料なし） · `00c48540`（命令位置の公開資料なし） · `00c48584`（命令位置の公開資料なし）

~~~diff
- 00c48480 ["INT_ADD", "register:40f0:8", ["const:c48480:8", "const:4:8"]]
- 00c48480 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4851c ["INT_ADD", "register:40f0:8", ["const:c4851c:8", "const:4:8"]]
+ 00c4851c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c48480 bytes e8460094
+ 00c4851c bytes f5460094
- 00c484a4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c484a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c484a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c484a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c48540 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c48540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c48540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c48540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c484a4 bytes 08c11791
+ 00c48540 bytes 08011b91
- 00c484e8 ["INT_ADD", "register:40f0:8", ["const:c484e8:8", "const:4:8"]]
- 00c484e8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c48584 ["INT_ADD", "register:40f0:8", ["const:c48584:8", "const:4:8"]]
+ 00c48584 ["CALL", null, ["callee:00c580f0:8"]]
- 00c484e8 bytes ce3e0094
+ 00c48584 bytes db3e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33feceaa4d4c4655f63ccd4e1b388d09"></a>

### [`00c48720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md) → [`00c487bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md) FUN_00c487bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c48778",
      "incomplete_value": true,
      "site": "00c48784",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d9e:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c48814",
      "READ",
      [
        "storage",
        "002a1d9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48814",
      "READ",
      [
        "storage",
        "002a1d51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4875c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md#insn-00c4875c) · [`00c48770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md#insn-00c48770) · [`00c487a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md#insn-00c487a4)
- 新版 `00c487f8`（命令位置の公開資料なし） · `00c4880c`（命令位置の公開資料なし） · `00c48840`（命令位置の公開資料なし）

~~~diff
- 00c4875c ["INT_ADD", "register:40f0:8", ["const:c4875c:8", "const:4:8"]]
- 00c4875c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c487f8 ["INT_ADD", "register:40f0:8", ["const:c487f8:8", "const:4:8"]]
+ 00c487f8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4875c bytes 51460094
+ 00c487f8 bytes 5e460094
- 00c48770 ["COPY", "tmp:0:8", ["const:d9e:8"]]
- 00c48770 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c48770 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c48770 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4880c ["COPY", "tmp:0:8", ["const:d51:8"]]
+ 00c4880c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4880c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4880c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c48770 bytes 29793691
+ 00c4880c bytes 29453591
- 00c487a4 ["INT_ADD", "register:40f0:8", ["const:c487a4:8", "const:4:8"]]
- 00c487a4 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c48840 ["INT_ADD", "register:40f0:8", ["const:c48840:8", "const:4:8"]]
+ 00c48840 ["CALL", null, ["callee:00c5b210:8"]]
- 00c487a4 bytes 674a0094
+ 00c48840 bytes 744a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edd61617c99ea4ac9b1189acbc094564"></a>

### [`00c48a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md) → [`00c48b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md) FUN_00c48b0c

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c48ad8",
      "incomplete_value": true,
      "site": "00c48ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b50:8"
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
    "old": {
      "definition_site": "00c48b44",
      "incomplete_value": true,
      "site": "00c48b50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:943:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c48b74",
      "READ",
      [
        "storage",
        "002bfb50",
        null,
        "string"
      ]
    ],
    [
      "00c48be0",
      "READ",
      [
        "storage",
        "002b0943",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48b74",
      "READ",
      [
        "storage",
        "002bfafc",
        null,
        "string"
      ]
    ],
    [
      "00c48be0",
      "READ",
      [
        "storage",
        "002b08e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md#insn-00c48b80) · [`00c48abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md#insn-00c48abc) · [`00c48ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md#insn-00c48ad0)
- 新版 `00c48c1c`（命令位置の公開資料なし） · `00c48b58`（命令位置の公開資料なし） · `00c48b6c`（命令位置の公開資料なし）

~~~diff
- 00c48b80 ["INT_ADD", "register:40f0:8", ["const:c48b80:8", "const:4:8"]]
- 00c48b80 ["CALL", null, ["callee:00c5b210:8"]]
+ 00c48c1c ["INT_ADD", "register:40f0:8", ["const:c48c1c:8", "const:4:8"]]
+ 00c48c1c ["CALL", null, ["callee:00c5b210:8"]]
- 00c48b80 bytes 70490094
+ 00c48c1c bytes 7d490094
- 00c48abc ["INT_ADD", "register:40f0:8", ["const:c48abc:8", "const:4:8"]]
- 00c48abc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48b58 ["INT_ADD", "register:40f0:8", ["const:c48b58:8", "const:4:8"]]
+ 00c48b58 ["CALL", null, ["callee:00c5a170:8"]]
- 00c48abc bytes 79450094
+ 00c48b58 bytes 86450094
- 00c48ad0 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00c48ad0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c48ad0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c48ad0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c48b6c ["COPY", "tmp:0:8", ["const:afc:8"]]
+ 00c48b6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48b6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48b6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c48ad0 bytes 29412d91
+ 00c48b6c bytes 29f12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f15fb204d7fd4024d623711a6e4785"></a>

### [`00c48b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md) → [`00c48c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md) FUN_00c48c28

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c48c2c",
      "incomplete_value": true,
      "site": "00c48c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c48cc8",
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48cc8",
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md#insn-00c48bb8) · [`00c48bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md#insn-00c48bdc) · [`00c48c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md#insn-00c48c10)
- 新版 `00c48c54`（命令位置の公開資料なし） · `00c48c78`（命令位置の公開資料なし） · `00c48cac`（命令位置の公開資料なし）

~~~diff
- 00c48bb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48bb8 ["INT_ADD", "register:40f0:8", ["const:c48bb8:8", "const:4:8"]]
- 00c48bb8 ["CALLIND", null, ["register:0:8"]]
+ 00c48c54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48c54 ["INT_ADD", "register:40f0:8", ["const:c48c54:8", "const:4:8"]]
+ 00c48c54 ["CALLIND", null, ["register:0:8"]]
- 00c48bb8 bytes 00013fd6
+ 00c48c54 bytes 00013fd6
- 00c48bdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48bdc ["INT_ADD", "register:40f0:8", ["const:c48bdc:8", "const:4:8"]]
- 00c48bdc ["CALLIND", null, ["register:0:8"]]
+ 00c48c78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48c78 ["INT_ADD", "register:40f0:8", ["const:c48c78:8", "const:4:8"]]
+ 00c48c78 ["CALLIND", null, ["register:0:8"]]
- 00c48bdc bytes 00013fd6
+ 00c48c78 bytes 00013fd6
- 00c48c10 ["INT_ADD", "register:40f0:8", ["const:c48c10:8", "const:4:8"]]
- 00c48c10 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c48cac ["INT_ADD", "register:40f0:8", ["const:c48cac:8", "const:4:8"]]
+ 00c48cac ["CALL", null, ["callee:00c5a170:8"]]
- 00c48c10 bytes 24450094
+ 00c48cac bytes 31450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65c11a4f12942e9443c0b3eb7ceda04"></a>

### [`00c4955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md) → [`00c495f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) FUN_00c495f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c420d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c4216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c495c0",
      "incomplete_value": false,
      "site": "00c495c0",
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
            "const:7b0:8"
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
      "00c4965c",
      "DATA",
      [
        "storage",
        "00c987b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4965c",
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c49590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md#insn-00c49590) · [`00c495b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md#insn-00c495b4) · [`00c495f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md#insn-00c495f8)
- 新版 `00c4962c`（命令位置の公開資料なし） · `00c49650`（命令位置の公開資料なし） · `00c49694`（命令位置の公開資料なし）

~~~diff
- 00c49590 ["INT_ADD", "register:40f0:8", ["const:c49590:8", "const:4:8"]]
- 00c49590 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4962c ["INT_ADD", "register:40f0:8", ["const:c4962c:8", "const:4:8"]]
+ 00c4962c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c49590 bytes a4420094
+ 00c4962c bytes b1420094
- 00c495b4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00c495b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c495b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c495b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c49650 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00c49650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c49650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c49650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c495b4 bytes 08c11e91
+ 00c49650 bytes 08012291
- 00c495f8 ["INT_ADD", "register:40f0:8", ["const:c495f8:8", "const:4:8"]]
- 00c495f8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c49694 ["INT_ADD", "register:40f0:8", ["const:c49694:8", "const:4:8"]]
+ 00c49694 ["CALL", null, ["callee:00c580f0:8"]]
- 00c495f8 bytes 8a3a0094
+ 00c49694 bytes 973a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db85b6327d3185dee3f4c51ebe83ce70"></a>

### [`00c496f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md) → [`00c4978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md) FUN_00c4978c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c498d0",
      "incomplete_value": false,
      "site": "00c498d4",
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
            "const:890:8"
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
    "old": {
      "definition_site": "00c49c08",
      "incomplete_value": false,
      "site": "00c49c0c",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c49970",
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ],
    [
      "00c49ca8",
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c49970",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ],
    [
      "00c49ca8",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c49744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md#insn-00c49744) · [`00c497c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md#insn-00c497c0) · [`00c497f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md#insn-00c497f0)
- 新版 `00c497e0`（命令位置の公開資料なし） · `00c4985c`（命令位置の公開資料なし） · `00c4988c`（命令位置の公開資料なし）

~~~diff
- 00c49744 ["INT_ADD", "register:40f0:8", ["const:c49744:8", "const:4:8"]]
- 00c49744 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c497e0 ["INT_ADD", "register:40f0:8", ["const:c497e0:8", "const:4:8"]]
+ 00c497e0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c49744 bytes 57420094
+ 00c497e0 bytes 64420094
- 00c497c0 ["INT_ADD", "register:40f0:8", ["const:c497c0:8", "const:4:8"]]
- 00c497c0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4985c ["INT_ADD", "register:40f0:8", ["const:c4985c:8", "const:4:8"]]
+ 00c4985c ["CALL", null, ["callee:00c5a170:8"]]
- 00c497c0 bytes 38420094
+ 00c4985c bytes 45420094
- 00c497f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c497f0 ["INT_ADD", "register:40f0:8", ["const:c497f0:8", "const:4:8"]]
- 00c497f0 ["CALLIND", null, ["register:0:8"]]
+ 00c4988c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4988c ["INT_ADD", "register:40f0:8", ["const:c4988c:8", "const:4:8"]]
+ 00c4988c ["CALLIND", null, ["register:0:8"]]
- 00c497f0 bytes 00013fd6
+ 00c4988c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21c9e1d1c220a865ec6961586c9bac7"></a>

### [`00c4a818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md) → [`00c4a8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md) FUN_00c4a8b4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4a9d8",
      "incomplete_value": true,
      "site": "00c4a9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
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
      "00c4aa74",
      "READ",
      [
        "storage",
        "002b18f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4aa74",
      "READ",
      [
        "storage",
        "002b1894",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4a860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md#insn-00c4a860) · [`00c4a8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md#insn-00c4a8cc) · [`00c4a900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md#insn-00c4a900)
- 新版 `00c4a8fc`（命令位置の公開資料なし） · `00c4a968`（命令位置の公開資料なし） · `00c4a99c`（命令位置の公開資料なし）

~~~diff
- 00c4a860 ["INT_ADD", "register:40f0:8", ["const:c4a860:8", "const:4:8"]]
- 00c4a860 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4a8fc ["INT_ADD", "register:40f0:8", ["const:c4a8fc:8", "const:4:8"]]
+ 00c4a8fc ["CALL", null, ["callee:00c5a170:8"]]
- 00c4a860 bytes 103e0094
+ 00c4a8fc bytes 1d3e0094
- 00c4a8cc ["INT_ADD", "register:40f0:8", ["const:c4a8cc:8", "const:4:8"]]
- 00c4a8cc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4a968 ["INT_ADD", "register:40f0:8", ["const:c4a968:8", "const:4:8"]]
+ 00c4a968 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4a8cc bytes f53d0094
+ 00c4a968 bytes 023e0094
- 00c4a900 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a900 ["INT_ADD", "register:40f0:8", ["const:c4a900:8", "const:4:8"]]
- 00c4a900 ["CALLIND", null, ["register:0:8"]]
+ 00c4a99c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a99c ["INT_ADD", "register:40f0:8", ["const:c4a99c:8", "const:4:8"]]
+ 00c4a99c ["CALLIND", null, ["register:0:8"]]
- 00c4a900 bytes 00013fd6
+ 00c4a99c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a9ff0637f425d9e6ef37310e1c4f98f"></a>

### [`00c4ab04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md) → [`00c4aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md) FUN_00c4aba0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4ab68",
      "incomplete_value": true,
      "site": "00c4ab78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:302:8"
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
      "00c4ac04",
      "READ",
      [
        "storage",
        "002bc302",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ac04",
      "READ",
      [
        "storage",
        "002bc2ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md#insn-00c4ab48) · [`00c4ab60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md#insn-00c4ab60) · [`00c4ab98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md#insn-00c4ab98)
- 新版 `00c4abe4`（命令位置の公開資料なし） · `00c4abfc`（命令位置の公開資料なし） · `00c4ac34`（命令位置の公開資料なし）

~~~diff
- 00c4ab48 ["INT_ADD", "register:40f0:8", ["const:c4ab48:8", "const:4:8"]]
- 00c4ab48 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4abe4 ["INT_ADD", "register:40f0:8", ["const:c4abe4:8", "const:4:8"]]
+ 00c4abe4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ab48 bytes 563d0094
+ 00c4abe4 bytes 633d0094
- 00c4ab60 ["COPY", "tmp:0:8", ["const:302:8"]]
- 00c4ab60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ab60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ab60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4abfc ["COPY", "tmp:0:8", ["const:2ae:8"]]
+ 00c4abfc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4abfc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4abfc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4ab60 bytes 4a090c91
+ 00c4abfc bytes 4ab90a91
- 00c4ab98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ab98 ["INT_ADD", "register:40f0:8", ["const:c4ab98:8", "const:4:8"]]
- 00c4ab98 ["CALLIND", null, ["register:0:8"]]
+ 00c4ac34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ac34 ["INT_ADD", "register:40f0:8", ["const:c4ac34:8", "const:4:8"]]
+ 00c4ac34 ["CALLIND", null, ["register:0:8"]]
- 00c4ab98 bytes 00013fd6
+ 00c4ac34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d96d04240f7368927ad43fa994b74b4"></a>

### [`00c4ac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md) → [`00c4acc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md) FUN_00c4acc4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4ac8c",
      "incomplete_value": true,
      "site": "00c4ac9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
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
      "00c4ad28",
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ad28",
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ac6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md#insn-00c4ac6c) · [`00c4ac84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md#insn-00c4ac84) · [`00c4acbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md#insn-00c4acbc)
- 新版 `00c4ad08`（命令位置の公開資料なし） · `00c4ad20`（命令位置の公開資料なし） · `00c4ad58`（命令位置の公開資料なし）

~~~diff
- 00c4ac6c ["INT_ADD", "register:40f0:8", ["const:c4ac6c:8", "const:4:8"]]
- 00c4ac6c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4ad08 ["INT_ADD", "register:40f0:8", ["const:c4ad08:8", "const:4:8"]]
+ 00c4ad08 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ac6c bytes 0d3d0094
+ 00c4ad08 bytes 1a3d0094
- 00c4ac84 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00c4ac84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ac84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ac84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4ad20 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00c4ad20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4ad20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4ad20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4ac84 bytes 4a413991
+ 00c4ad20 bytes 4a413a91
- 00c4acbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4acbc ["INT_ADD", "register:40f0:8", ["const:c4acbc:8", "const:4:8"]]
- 00c4acbc ["CALLIND", null, ["register:0:8"]]
+ 00c4ad58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ad58 ["INT_ADD", "register:40f0:8", ["const:c4ad58:8", "const:4:8"]]
+ 00c4ad58 ["CALLIND", null, ["register:0:8"]]
- 00c4acbc bytes 00013fd6
+ 00c4ad58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c2b1b72622526ce1f2333a75defb32d"></a>

### [`00c4b0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md) → [`00c4b140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md) FUN_00c4b140

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4b1c4",
      "incomplete_value": true,
      "site": "00c4b1d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea4:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4b260",
      "READ",
      [
        "storage",
        "002b7ea4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4b260",
      "READ",
      [
        "storage",
        "002b7ee4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md#insn-00c4b0d0) · [`00c4b0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md#insn-00c4b0f4) · [`00c4b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md#insn-00c4b120)
- 新版 `00c4b16c`（命令位置の公開資料なし） · `00c4b190`（命令位置の公開資料なし） · `00c4b1bc`（命令位置の公開資料なし）

~~~diff
- 00c4b0d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b0d0 ["INT_ADD", "register:40f0:8", ["const:c4b0d0:8", "const:4:8"]]
- 00c4b0d0 ["CALLIND", null, ["register:0:8"]]
+ 00c4b16c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b16c ["INT_ADD", "register:40f0:8", ["const:c4b16c:8", "const:4:8"]]
+ 00c4b16c ["CALLIND", null, ["register:0:8"]]
- 00c4b0d0 bytes 00013fd6
+ 00c4b16c bytes 00013fd6
- 00c4b0f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b0f4 ["INT_ADD", "register:40f0:8", ["const:c4b0f4:8", "const:4:8"]]
- 00c4b0f4 ["CALLIND", null, ["register:0:8"]]
+ 00c4b190 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b190 ["INT_ADD", "register:40f0:8", ["const:c4b190:8", "const:4:8"]]
+ 00c4b190 ["CALLIND", null, ["register:0:8"]]
- 00c4b0f4 bytes 00013fd6
+ 00c4b190 bytes 00013fd6
- 00c4b120 ["INT_ADD", "register:40f0:8", ["const:c4b120:8", "const:4:8"]]
- 00c4b120 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4b1bc ["INT_ADD", "register:40f0:8", ["const:c4b1bc:8", "const:4:8"]]
+ 00c4b1bc ["CALL", null, ["callee:00c5a170:8"]]
- 00c4b120 bytes e03b0094
+ 00c4b1bc bytes ed3b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-381ac6042bf040ef7cf497d4fa8d6942"></a>

### [`00c4b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md) → [`00c4b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md) FUN_00c4b450

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4b41c",
      "incomplete_value": true,
      "site": "00c4b428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
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
    "old": {
      "definition_site": "00c4b4a8",
      "incomplete_value": false,
      "site": "00c4b4ac",
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
            "const:890:8"
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
      "00c4b4b8",
      "READ",
      [
        "storage",
        "002ac580",
        null,
        "string"
      ]
    ],
    [
      "00c4b548",
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4b4b8",
      "READ",
      [
        "storage",
        "002ac524",
        null,
        "string"
      ]
    ],
    [
      "00c4b548",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md#insn-00c4b3fc) · [`00c4b414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md#insn-00c4b414) · [`00c4b468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md#insn-00c4b468)
- 新版 `00c4b498`（命令位置の公開資料なし） · `00c4b4b0`（命令位置の公開資料なし） · `00c4b504`（命令位置の公開資料なし）

~~~diff
- 00c4b3fc ["INT_ADD", "register:40f0:8", ["const:c4b3fc:8", "const:4:8"]]
- 00c4b3fc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4b498 ["INT_ADD", "register:40f0:8", ["const:c4b498:8", "const:4:8"]]
+ 00c4b498 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4b3fc bytes 293b0094
+ 00c4b498 bytes 363b0094
- 00c4b414 ["COPY", "tmp:0:8", ["const:580:8"]]
- 00c4b414 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4b414 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4b414 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4b4b0 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00c4b4b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4b4b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4b4b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4b414 bytes 4a011691
+ 00c4b4b0 bytes 4a911491
- 00c4b468 ["INT_ADD", "register:40f0:8", ["const:c4b468:8", "const:4:8"]]
- 00c4b468 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4b504 ["INT_ADD", "register:40f0:8", ["const:c4b504:8", "const:4:8"]]
+ 00c4b504 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4b468 bytes 0e3b0094
+ 00c4b504 bytes 1b3b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc382aa134fa2825074c80cc9ecd4c3"></a>

### [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) → [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) FUN_00c4b848

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 6件 [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) [`00c4bb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 6件 [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4bbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4b8ac",
      "incomplete_value": false,
      "site": "00c4b8ac",
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
            "const:540:8"
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
    "old": {
      "definition_site": "00c4b954",
      "incomplete_value": false,
      "site": "00c4b954",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4ba14",
      "incomplete_value": false,
      "site": "00c4ba14",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4b948",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4b9f0",
      "DATA",
      [
        "storage",
        "00c98eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4bab0",
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4b948",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4b9f0",
      "DATA",
      [
        "storage",
        "00c98f80",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4bab0",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md#insn-00c4b948) · [`00c4b818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md#insn-00c4b818) · [`00c4b828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md#insn-00c4b828)
- 新版 `00c4b9e4`（命令位置の公開資料なし） · `00c4b8b4`（命令位置の公開資料なし） · `00c4b8c4`（命令位置の公開資料なし）

~~~diff
- 00c4b948 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00c4b948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4b948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4b948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4b9e4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00c4b9e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4b9e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4b9e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4b948 bytes 29c13a91
+ 00c4b9e4 bytes 29013e91
- 00c4b818 ["INT_ADD", "register:40f0:8", ["const:c4b818:8", "const:4:8"]]
- 00c4b818 ["CALL", null, ["callee:00c4bbf8:8"]]
+ 00c4b8b4 ["INT_ADD", "register:40f0:8", ["const:c4b8b4:8", "const:4:8"]]
+ 00c4b8b4 ["CALL", null, ["callee:00c4bbf8:8"]]
- 00c4b818 bytes d1000094
+ 00c4b8b4 bytes d1000094
- 00c4b828 ["INT_ADD", "register:40f0:8", ["const:c4b828:8", "const:4:8"]]
- 00c4b828 ["CALL", null, ["callee:00c3e04c:8"]]
+ 00c4b8c4 ["INT_ADD", "register:40f0:8", ["const:c4b8c4:8", "const:4:8"]]
+ 00c4b8c4 ["CALL", null, ["callee:00c3e04c:8"]]
- 00c4b828 bytes e2c9ff97
+ 00c4b8c4 bytes e2c9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba61d7f4260f24c122ba95711162d5e"></a>

### [`00c4bb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md) → [`00c4bbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) FUN_00c4bbf8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c4b7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) · 呼出先 5件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) · 呼出先 5件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.29% / 新版 97.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4bca8",
      "incomplete_value": false,
      "site": "00c4bca8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4be94",
      "incomplete_value": false,
      "site": "00c4be94",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4bc50",
      "READ",
      [
        "storage",
        "00c97960",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bc60",
      "READ",
      [
        "storage",
        "00c97961",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bc8c",
      "READ",
      [
        "storage",
        "00c97970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c4bc50",
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bc60",
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4bc8c",
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4bd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md#insn-00c4bd44) · [`00c4bb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md#insn-00c4bb94) · [`00c4bc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md#insn-00c4bc40)
- 新版 `00c4bde0`（命令位置の公開資料なし） · `00c4bc30`（命令位置の公開資料なし） · `00c4bcdc`（命令位置の公開資料なし）

~~~diff
- 00c4bd44 ["INT_ADD", "register:40f0:8", ["const:c4bd44:8", "const:4:8"]]
- 00c4bd44 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4bde0 ["INT_ADD", "register:40f0:8", ["const:c4bde0:8", "const:4:8"]]
+ 00c4bde0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4bd44 bytes b7380094
+ 00c4bde0 bytes c4380094
- 00c4bb94 ["COPY", "register:4060:8", ["const:c97780:8"]]
+ 00c4bc30 ["COPY", "register:4060:8", ["const:c97850:8"]]
- 00c4bb94 bytes 6cdf2510
+ 00c4bc30 bytes 0ce12510
- 00c4bc40 ["INT_ADD", "register:40f0:8", ["const:c4bc40:8", "const:4:8"]]
- 00c4bc40 ["CALL", null, ["callee:00c3ad68:8"]]
+ 00c4bcdc ["INT_ADD", "register:40f0:8", ["const:c4bcdc:8", "const:4:8"]]
+ 00c4bcdc ["CALL", null, ["callee:00c3ad68:8"]]
- 00c4bc40 bytes 23bcff97
+ 00c4bcdc bytes 23bcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639a297ad2a7e360d8b13a444f6876f5"></a>

### [`00c4bf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md) → [`00c4c014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md) FUN_00c4c014

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4bfdc",
      "incomplete_value": true,
      "site": "00c4bfec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:695:8"
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
      "00c4c078",
      "READ",
      [
        "storage",
        "002bd695",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c078",
      "READ",
      [
        "storage",
        "002bd641",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4bfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md#insn-00c4bfbc) · [`00c4bfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md#insn-00c4bfd4) · [`00c4c00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md#insn-00c4c00c)
- 新版 `00c4c058`（命令位置の公開資料なし） · `00c4c070`（命令位置の公開資料なし） · `00c4c0a8`（命令位置の公開資料なし）

~~~diff
- 00c4bfbc ["INT_ADD", "register:40f0:8", ["const:c4bfbc:8", "const:4:8"]]
- 00c4bfbc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c058 ["INT_ADD", "register:40f0:8", ["const:c4c058:8", "const:4:8"]]
+ 00c4c058 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4bfbc bytes 39380094
+ 00c4c058 bytes 46380094
- 00c4bfd4 ["COPY", "tmp:0:8", ["const:695:8"]]
- 00c4bfd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4bfd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4bfd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4c070 ["COPY", "tmp:0:8", ["const:641:8"]]
+ 00c4c070 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c070 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c070 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4bfd4 bytes 4a551a91
+ 00c4c070 bytes 4a051991
- 00c4c00c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c00c ["INT_ADD", "register:40f0:8", ["const:c4c00c:8", "const:4:8"]]
- 00c4c00c ["CALLIND", null, ["register:0:8"]]
+ 00c4c0a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c0a8 ["INT_ADD", "register:40f0:8", ["const:c4c0a8:8", "const:4:8"]]
+ 00c4c0a8 ["CALLIND", null, ["register:0:8"]]
- 00c4c00c bytes 00013fd6
+ 00c4c0a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074751cc4f97372ddea5d575cad81d42"></a>

### [`00c4c05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md) → [`00c4c0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md) FUN_00c4c0f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4c0c0",
      "incomplete_value": true,
      "site": "00c4c0d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:30d:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4c15c",
      "READ",
      [
        "storage",
        "002bc30d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c15c",
      "READ",
      [
        "storage",
        "002bc2b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md#insn-00c4c0a0) · [`00c4c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md#insn-00c4c0b8) · [`00c4c0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md#insn-00c4c0f4)
- 新版 `00c4c13c`（命令位置の公開資料なし） · `00c4c154`（命令位置の公開資料なし） · `00c4c190`（命令位置の公開資料なし）

~~~diff
- 00c4c0a0 ["INT_ADD", "register:40f0:8", ["const:c4c0a0:8", "const:4:8"]]
- 00c4c0a0 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c13c ["INT_ADD", "register:40f0:8", ["const:c4c13c:8", "const:4:8"]]
+ 00c4c13c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c0a0 bytes 00380094
+ 00c4c13c bytes 0d380094
- 00c4c0b8 ["COPY", "tmp:0:8", ["const:30d:8"]]
- 00c4c0b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4c0b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4c0b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4c154 ["COPY", "tmp:0:8", ["const:2b9:8"]]
+ 00c4c154 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c154 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c154 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4c0b8 bytes 4a350c91
+ 00c4c154 bytes 4ae50a91
- 00c4c0f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c0f4 ["INT_ADD", "register:40f0:8", ["const:c4c0f4:8", "const:4:8"]]
- 00c4c0f4 ["CALLIND", null, ["register:0:8"]]
+ 00c4c190 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c190 ["INT_ADD", "register:40f0:8", ["const:c4c190:8", "const:4:8"]]
+ 00c4c190 ["CALLIND", null, ["register:0:8"]]
- 00c4c0f4 bytes 00013fd6
+ 00c4c190 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6e1520fa5bd446407298d7ee4417083"></a>

### [`00c4c338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md) → [`00c4c3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md) FUN_00c4c3d4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c4c4cc",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:ee2:8"
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
    "old": {
      "definition_site": "00c4c4d4",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:896:8"
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
    "old": {
      "definition_site": "00c4c4dc",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4c4d8",
      "READ",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ],
    [
      "00c4c4d8",
      "READ",
      [
        "storage",
        "002bd69f",
        null,
        "string"
      ]
    ],
    [
      "00c4c4d8",
      "READ",
      [
        "storage",
        "002b8d98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c4d8",
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      "00c4c4d8",
      "READ",
      [
        "storage",
        "002bd64b",
        null,
        "string"
      ]
    ],
    [
      "00c4c4d8",
      "READ",
      [
        "storage",
        "002b8d44",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md#insn-00c4c4e4) · [`00c4c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md#insn-00c4c380) · [`00c4c3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md#insn-00c4c3d4)
- 新版 `00c4c580`（命令位置の公開資料なし） · `00c4c41c`（命令位置の公開資料なし） · `00c4c470`（命令位置の公開資料なし）

~~~diff
- 00c4c4e4 ["INT_ADD", "register:40f0:8", ["const:c4c4e4:8", "const:4:8"]]
- 00c4c4e4 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c4c580 ["INT_ADD", "register:40f0:8", ["const:c4c580:8", "const:4:8"]]
+ 00c4c580 ["CALL", null, ["callee:00c380a8:8"]]
- 00c4c4e4 bytes caaeff97
+ 00c4c580 bytes caaeff97
- 00c4c380 ["INT_ADD", "register:40f0:8", ["const:c4c380:8", "const:4:8"]]
- 00c4c380 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c41c ["INT_ADD", "register:40f0:8", ["const:c4c41c:8", "const:4:8"]]
+ 00c4c41c ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c380 bytes 48370094
+ 00c4c41c bytes 55370094
- 00c4c3d4 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00c4c3d4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c4c3d4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c4c3d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c4c470 ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00c4c470 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c4c470 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c4c470 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c4c3d4 bytes b58e3c91
+ 00c4c470 bytes b53e3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a5a77cce2ecbe74cb9057df9c8f2682"></a>

### [`00c4c4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md) → [`00c4c58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md) FUN_00c4c58c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 83.64% / 新版 83.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c4c5b0",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:ee2:8"
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
    "old": {
      "definition_site": "00c4c5b8",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:896:8"
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
    "old": {
      "definition_site": "00c4c5c0",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4c5ac",
      "DATA",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ],
    [
      "00c4c5dc",
      "DATA",
      [
        "storage",
        "002b7eb0",
        null,
        "string"
      ]
    ],
    [
      "00c4c614",
      "READ",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c5ac",
      "DATA",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      "00c4c5dc",
      "DATA",
      [
        "storage",
        "002b7ef0",
        null,
        "string"
      ]
    ],
    [
      "00c4c614",
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md#insn-00c4c5c8) · [`00c4c510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md#insn-00c4c510) · [`00c4c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md#insn-00c4c530)
- 新版 `00c4c664`（命令位置の公開資料なし） · `00c4c5ac`（命令位置の公開資料なし） · `00c4c5cc`（命令位置の公開資料なし）

~~~diff
- 00c4c5c8 ["INT_ADD", "register:40f0:8", ["const:c4c5c8:8", "const:4:8"]]
- 00c4c5c8 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c4c664 ["INT_ADD", "register:40f0:8", ["const:c4c664:8", "const:4:8"]]
+ 00c4c664 ["CALL", null, ["callee:00c380a8:8"]]
- 00c4c5c8 bytes 91aeff97
+ 00c4c664 bytes 91aeff97
- 00c4c510 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00c4c510 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c4c510 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c4c510 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c4c5ac ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00c4c5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4c5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4c5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c4c510 bytes 008c3c91
+ 00c4c5ac bytes 003c3b91
- 00c4c530 ["COPY", "tmp:0:8", ["const:69f:8"]]
- 00c4c530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4c530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4c530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4c5cc ["COPY", "tmp:0:8", ["const:64b:8"]]
+ 00c4c5cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4c5cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4c5cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4c530 bytes 087d1a91
+ 00c4c5cc bytes 082d1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-062dbec4934932bdbe8e286b736ef7b9"></a>

### [`00c4c5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md) → [`00c4c670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md) FUN_00c4c670

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.01% / 新版 93.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4c714",
      "incomplete_value": true,
      "site": "00c4c71c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab0:8"
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
    "old": {
      "definition_site": "00c4c718",
      "incomplete_value": true,
      "site": "00c4c720",
      "value": [
        "LOAD",
        "16",
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
    "old": {
      "definition_site": "00c4c780",
      "incomplete_value": true,
      "site": "00c4c788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:196:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4c7b0",
      "READ",
      [
        "storage",
        "002b4ab0",
        null,
        "string"
      ]
    ],
    [
      "00c4c7b4",
      "READ",
      [
        "storage",
        "002b4abd",
        null,
        "string"
      ]
    ],
    [
      "00c4c81c",
      "READ",
      [
        "storage",
        "002bb196",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c7b0",
      "READ",
      [
        "storage",
        "002b4ae1",
        null,
        "string"
      ]
    ],
    [
      "00c4c7b4",
      "READ",
      [
        "storage",
        "002b4aee",
        null,
        "string"
      ]
    ],
    [
      "00c4c81c",
      "READ",
      [
        "storage",
        "002bb142",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md#insn-00c4c61c) · [`00c4c660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md#insn-00c4c660) · [`00c4c698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md#insn-00c4c698)
- 新版 `00c4c6b8`（命令位置の公開資料なし） · `00c4c6fc`（命令位置の公開資料なし） · `00c4c734`（命令位置の公開資料なし）

~~~diff
- 00c4c61c ["INT_ADD", "register:40f0:8", ["const:c4c61c:8", "const:4:8"]]
- 00c4c61c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c6b8 ["INT_ADD", "register:40f0:8", ["const:c4c6b8:8", "const:4:8"]]
+ 00c4c6b8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c61c bytes a1360094
+ 00c4c6b8 bytes ae360094
- 00c4c660 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c660 ["INT_ADD", "register:40f0:8", ["const:c4c660:8", "const:4:8"]]
- 00c4c660 ["CALLIND", null, ["register:0:8"]]
+ 00c4c6fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c6fc ["INT_ADD", "register:40f0:8", ["const:c4c6fc:8", "const:4:8"]]
+ 00c4c6fc ["CALLIND", null, ["register:0:8"]]
- 00c4c660 bytes 00013fd6
+ 00c4c6fc bytes 00013fd6
- 00c4c698 ["INT_ADD", "register:40f0:8", ["const:c4c698:8", "const:4:8"]]
- 00c4c698 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4c734 ["INT_ADD", "register:40f0:8", ["const:c4c734:8", "const:4:8"]]
+ 00c4c734 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4c698 bytes 82360094
+ 00c4c734 bytes 8f360094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5307f85fb2fdf095a35d614061a7be"></a>

### [`00c4c810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md) → [`00c4c8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md) FUN_00c4c8ac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00c4c830",
      "incomplete_value": true,
      "site": "00c4c834",
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
                "const:d88:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4c8bc",
      "DATA",
      [
        "storage",
        "00313d58",
        null,
        null
      ]
    ],
    [
      "00c4c8c8",
      "DATA",
      [
        "storage",
        "00313d88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4c8bc",
      "DATA",
      [
        "storage",
        "00313d98",
        null,
        null
      ]
    ],
    [
      "00c4c8c8",
      "DATA",
      [
        "storage",
        "00313dc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md#insn-00c4c81c) · [`00c4c824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md#insn-00c4c824) · [`00c4c828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md#insn-00c4c828)
- 新版 `00c4c8b8`（命令位置の公開資料なし） · `00c4c8c4`（命令位置の公開資料なし）

~~~diff
- 00c4c81c ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00c4c81c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c81c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c81c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4c8b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00c4c8b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c8b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c8b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c81c bytes 29613591
+ 00c4c8b8 bytes 29613691
- 00c4c824 ["COPY", "register:4048:8", ["const:313000:8"]]
- 00c4c824 bytes 29b6fff0
- 00c4c828 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00c4c828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4c8c4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00c4c8c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c8c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c8c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c828 bytes 29213691
+ 00c4c8c4 bytes 29213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c986d41e391a5112aba1fa4ccf1d6be"></a>

### [`00c4cb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md) → [`00c4cba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md) FUN_00c4cba0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4cb74",
      "incomplete_value": false,
      "site": "00c4cb74",
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
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4cc10",
      "DATA",
      [
        "storage",
        "00c99230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4cc10",
      "DATA",
      [
        "storage",
        "00c99300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4cb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md#insn-00c4cb44) · [`00c4cb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md#insn-00c4cb70) · [`00c4cbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md#insn-00c4cbc0)
- 新版 `00c4cbe0`（命令位置の公開資料なし） · `00c4cc0c`（命令位置の公開資料なし） · `00c4cc5c`（命令位置の公開資料なし）

~~~diff
- 00c4cb44 ["INT_ADD", "register:40f0:8", ["const:c4cb44:8", "const:4:8"]]
- 00c4cb44 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4cbe0 ["INT_ADD", "register:40f0:8", ["const:c4cbe0:8", "const:4:8"]]
+ 00c4cbe0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4cb44 bytes 37350094
+ 00c4cbe0 bytes 44350094
- 00c4cb70 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00c4cb70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4cb70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4cb70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4cc0c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 00c4cc0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4cc0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4cc0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4cb70 bytes 29c10891
+ 00c4cc0c bytes 29010c91
- 00c4cbc0 ["INT_ADD", "register:40f0:8", ["const:c4cbc0:8", "const:4:8"]]
- 00c4cbc0 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4cc5c ["INT_ADD", "register:40f0:8", ["const:c4cc5c:8", "const:4:8"]]
+ 00c4cc5c ["CALL", null, ["callee:00c580f0:8"]]
- 00c4cbc0 bytes 182d0094
+ 00c4cc5c bytes 252d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0388417e819e0b2b7eae8850189ff51"></a>

### [`00c4cdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md) → [`00c4ce88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md) FUN_00c4ce88

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4ce84",
      "incomplete_value": true,
      "site": "00c4ce94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:294:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4cf20",
      "READ",
      [
        "storage",
        "002a5294",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4cf20",
      "READ",
      [
        "storage",
        "002a5238",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md#insn-00c4ce18) · [`00c4ce3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md#insn-00c4ce3c) · [`00c4ce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md#insn-00c4ce68)
- 新版 `00c4ceb4`（命令位置の公開資料なし） · `00c4ced8`（命令位置の公開資料なし） · `00c4cf04`（命令位置の公開資料なし）

~~~diff
- 00c4ce18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ce18 ["INT_ADD", "register:40f0:8", ["const:c4ce18:8", "const:4:8"]]
- 00c4ce18 ["CALLIND", null, ["register:0:8"]]
+ 00c4ceb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ceb4 ["INT_ADD", "register:40f0:8", ["const:c4ceb4:8", "const:4:8"]]
+ 00c4ceb4 ["CALLIND", null, ["register:0:8"]]
- 00c4ce18 bytes 00013fd6
+ 00c4ceb4 bytes 00013fd6
- 00c4ce3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ce3c ["INT_ADD", "register:40f0:8", ["const:c4ce3c:8", "const:4:8"]]
- 00c4ce3c ["CALLIND", null, ["register:0:8"]]
+ 00c4ced8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4ced8 ["INT_ADD", "register:40f0:8", ["const:c4ced8:8", "const:4:8"]]
+ 00c4ced8 ["CALLIND", null, ["register:0:8"]]
- 00c4ce3c bytes 00013fd6
+ 00c4ced8 bytes 00013fd6
- 00c4ce68 ["INT_ADD", "register:40f0:8", ["const:c4ce68:8", "const:4:8"]]
- 00c4ce68 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4cf04 ["INT_ADD", "register:40f0:8", ["const:c4cf04:8", "const:4:8"]]
+ 00c4cf04 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4ce68 bytes 8e340094
+ 00c4cf04 bytes 9b340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b621be58914d7e2c0e66be9f953e1ead"></a>

### [`00c4d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md) → [`00c4d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md) FUN_00c4d18c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4d15c",
      "incomplete_value": false,
      "site": "00c4d15c",
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
            "const:640:8"
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
      "00c4d1f8",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4d1f8",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md#insn-00c4d124) · [`00c4d14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md#insn-00c4d14c) · [`00c4d154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md#insn-00c4d154)
- 新版 `00c4d1c0`（命令位置の公開資料なし） · `00c4d1e8`（命令位置の公開資料なし） · `00c4d1f0`（命令位置の公開資料なし）

~~~diff
- 00c4d124 ["INT_ADD", "register:40f0:8", ["const:c4d124:8", "const:4:8"]]
- 00c4d124 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4d1c0 ["INT_ADD", "register:40f0:8", ["const:c4d1c0:8", "const:4:8"]]
+ 00c4d1c0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4d124 bytes bf330094
+ 00c4d1c0 bytes cc330094
- 00c4d14c ["INT_ADD", "register:40f0:8", ["const:c4d14c:8", "const:4:8"]]
- 00c4d14c ["CALL", null, ["callee:00c580b0:8"]]
+ 00c4d1e8 ["INT_ADD", "register:40f0:8", ["const:c4d1e8:8", "const:4:8"]]
+ 00c4d1e8 ["CALL", null, ["callee:00c580b0:8"]]
- 00c4d14c bytes a52b0094
+ 00c4d1e8 bytes b22b0094
- 00c4d154 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c4d154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4d154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4d154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4d1f0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4d1f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d1f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d1f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4d154 bytes 29011991
+ 00c4d1f0 bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbdbaa9b06b09517dc5603714265e32e"></a>

### [`00c4d19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md) → [`00c4d238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md) FUN_00c4d238

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4d204",
      "incomplete_value": false,
      "site": "00c4d204",
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
      "00c4d2a0",
      "DATA",
      [
        "storage",
        "00c993f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4d2a0",
      "DATA",
      [
        "storage",
        "00c994c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md#insn-00c4d1d4) · [`00c4d1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md#insn-00c4d1f8) · [`00c4d240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md#insn-00c4d240)
- 新版 `00c4d270`（命令位置の公開資料なし） · `00c4d294`（命令位置の公開資料なし） · `00c4d2dc`（命令位置の公開資料なし）

~~~diff
- 00c4d1d4 ["INT_ADD", "register:40f0:8", ["const:c4d1d4:8", "const:4:8"]]
- 00c4d1d4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4d270 ["INT_ADD", "register:40f0:8", ["const:c4d270:8", "const:4:8"]]
+ 00c4d270 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4d1d4 bytes 93330094
+ 00c4d270 bytes a0330094
- 00c4d1f8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00c4d1f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4d1f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4d1f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4d294 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00c4d294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4d294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4d294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4d1f8 bytes 08c10f91
+ 00c4d294 bytes 08011391
- 00c4d240 ["INT_ADD", "register:40f0:8", ["const:c4d240:8", "const:4:8"]]
- 00c4d240 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4d2dc ["INT_ADD", "register:40f0:8", ["const:c4d2dc:8", "const:4:8"]]
+ 00c4d2dc ["CALL", null, ["callee:00c580f0:8"]]
- 00c4d240 bytes 782b0094
+ 00c4d2dc bytes 852b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9e4f9a71c97c0ca717d1ca27856e5ba"></a>

### [`00c4d7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md) → [`00c4d868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md) FUN_00c4d868

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4d830",
      "incomplete_value": true,
      "site": "00c4d844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e7c:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4d8cc",
      "READ",
      [
        "storage",
        "002a3e7c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d8cc",
      "READ",
      [
        "storage",
        "002a3e2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md#insn-00c4d810) · [`00c4d828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md#insn-00c4d828) · [`00c4d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md#insn-00c4d858)
- 新版 `00c4d8ac`（命令位置の公開資料なし） · `00c4d8c4`（命令位置の公開資料なし） · `00c4d8f4`（命令位置の公開資料なし）

~~~diff
- 00c4d810 ["INT_ADD", "register:40f0:8", ["const:c4d810:8", "const:4:8"]]
- 00c4d810 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4d8ac ["INT_ADD", "register:40f0:8", ["const:c4d8ac:8", "const:4:8"]]
+ 00c4d8ac ["CALL", null, ["callee:00c5a170:8"]]
- 00c4d810 bytes 24320094
+ 00c4d8ac bytes 31320094
- 00c4d828 ["COPY", "tmp:0:8", ["const:e7c:8"]]
- 00c4d828 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4d828 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4d828 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4d8c4 ["COPY", "tmp:0:8", ["const:e2f:8"]]
+ 00c4d8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4d828 bytes 4af13991
+ 00c4d8c4 bytes 4abd3891
- 00c4d858 ["INT_ADD", "register:40f0:8", ["const:c4d858:8", "const:4:8"]]
- 00c4d858 ["CALL", null, ["callee:00c451e0:8"]]
+ 00c4d8f4 ["INT_ADD", "register:40f0:8", ["const:c4d8f4:8", "const:4:8"]]
+ 00c4d8f4 ["CALL", null, ["callee:00c451e0:8"]]
- 00c4d858 bytes 3bdeff97
+ 00c4d8f4 bytes 3bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2da44fe64e9e46109c3499d1c0e2b34"></a>

### [`00c4dac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md) → [`00c4db64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md) FUN_00c4db64

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4dc60",
      "incomplete_value": true,
      "site": "00c4dc6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
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
    "old": {
      "definition_site": "00c4dcc8",
      "incomplete_value": true,
      "site": "00c4dcd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b03:8"
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
    "old": {
      "definition_site": "00c4de28",
      "incomplete_value": true,
      "site": "00c4de38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4dcfc",
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      "00c4dd64",
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ],
    [
      "00c4dec4",
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4dcfc",
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      "00c4dd64",
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ],
    [
      "00c4dec4",
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4db18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md#insn-00c4db18) · [`00c4db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md#insn-00c4db40) · [`00c4db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md#insn-00c4db78)
- 新版 `00c4dbb4`（命令位置の公開資料なし） · `00c4dbdc`（命令位置の公開資料なし） · `00c4dc14`（命令位置の公開資料なし）

~~~diff
- 00c4db18 ["INT_ADD", "register:40f0:8", ["const:c4db18:8", "const:4:8"]]
- 00c4db18 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4dbb4 ["INT_ADD", "register:40f0:8", ["const:c4dbb4:8", "const:4:8"]]
+ 00c4dbb4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4db18 bytes 62310094
+ 00c4dbb4 bytes 6f310094
- 00c4db40 ["INT_ADD", "register:40f0:8", ["const:c4db40:8", "const:4:8"]]
- 00c4db40 ["CALL", null, ["callee:00c451e0:8"]]
+ 00c4dbdc ["INT_ADD", "register:40f0:8", ["const:c4dbdc:8", "const:4:8"]]
+ 00c4dbdc ["CALL", null, ["callee:00c451e0:8"]]
- 00c4db40 bytes 81ddff97
+ 00c4dbdc bytes 81ddff97
- 00c4db78 ["INT_ADD", "register:40f0:8", ["const:c4db78:8", "const:4:8"]]
- 00c4db78 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4dc14 ["INT_ADD", "register:40f0:8", ["const:c4dc14:8", "const:4:8"]]
+ 00c4dc14 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4db78 bytes 4a310094
+ 00c4dc14 bytes 57310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe8e18d1b3b65d7f787834842cc72533"></a>

### [`00c4e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md) → [`00c4e0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md) FUN_00c4e0dc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 8件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 8件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.24% / 新版 97.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4e238",
      "incomplete_value": false,
      "site": "00c4e238",
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
            "const:640:8"
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
    "old": {
      "definition_site": "00c4e25c",
      "incomplete_value": false,
      "site": "00c4e25c",
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
            "const:9ef:8"
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
    "old": {
      "definition_site": "00c4e2e8",
      "incomplete_value": false,
      "site": "00c4e2e8",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4e2d4",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e2f8",
      "DATA",
      [
        "storage",
        "002a89ef",
        null,
        "string"
      ]
    ],
    [
      "00c4e384",
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e2d4",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e2f8",
      "DATA",
      [
        "storage",
        "002a8993",
        null,
        "string"
      ]
    ],
    [
      "00c4e384",
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md#insn-00c4e144) · [`00c4e18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md#insn-00c4e18c) · [`00c4e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md#insn-00c4e1bc)
- 新版 `00c4e1e0`（命令位置の公開資料なし） · `00c4e228`（命令位置の公開資料なし） · `00c4e258`（命令位置の公開資料なし）

~~~diff
- 00c4e144 ["INT_ADD", "register:40f0:8", ["const:c4e144:8", "const:4:8"]]
- 00c4e144 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4e1e0 ["INT_ADD", "register:40f0:8", ["const:c4e1e0:8", "const:4:8"]]
+ 00c4e1e0 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4e144 bytes d72f0094
+ 00c4e1e0 bytes e42f0094
- 00c4e18c ["INT_ADD", "register:40f0:8", ["const:c4e18c:8", "const:4:8"]]
- 00c4e18c ["CALL", null, ["callee:00c3ad68:8"]]
+ 00c4e228 ["INT_ADD", "register:40f0:8", ["const:c4e228:8", "const:4:8"]]
+ 00c4e228 ["CALL", null, ["callee:00c3ad68:8"]]
- 00c4e18c bytes d0b2ff97
+ 00c4e228 bytes d0b2ff97
- 00c4e1bc ["INT_ADD", "register:40f0:8", ["const:c4e1bc:8", "const:4:8"]]
- 00c4e1bc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4e258 ["INT_ADD", "register:40f0:8", ["const:c4e258:8", "const:4:8"]]
+ 00c4e258 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4e1bc bytes 992f0094
+ 00c4e258 bytes a62f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2749b11be45437b4dd269df9eff4dd3f"></a>

### [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) → [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) FUN_00c4e684

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) · 呼出先 5件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3e5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c4e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 5件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4e7e0",
      "incomplete_value": false,
      "site": "00c4e7e0",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4e868",
      "incomplete_value": false,
      "site": "00c4e868",
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
            "const:a10:8"
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
    "old": {
      "definition_site": "00c4e978",
      "incomplete_value": false,
      "site": "00c4e978",
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
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4e87c",
      "DATA",
      [
        "storage",
        "00c99a80",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e904",
      "DATA",
      [
        "storage",
        "00c99a10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4ea14",
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e87c",
      "DATA",
      [
        "storage",
        "00c99b50",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4e904",
      "DATA",
      [
        "storage",
        "00c99ae0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4ea14",
      "DATA",
      [
        "storage",
        "00c99a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md#insn-00c4e704) · [`00c4e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md#insn-00c4e780) · [`00c4e7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md#insn-00c4e7a8)
- 新版 `00c4e7a0`（命令位置の公開資料なし） · `00c4e81c`（命令位置の公開資料なし） · `00c4e844`（命令位置の公開資料なし）

~~~diff
- 00c4e704 ["INT_ADD", "register:40f0:8", ["const:c4e704:8", "const:4:8"]]
- 00c4e704 ["CALL", null, ["callee:00c3e660:8"]]
+ 00c4e7a0 ["INT_ADD", "register:40f0:8", ["const:c4e7a0:8", "const:4:8"]]
+ 00c4e7a0 ["CALL", null, ["callee:00c3e660:8"]]
- 00c4e704 bytes b0bfff97
+ 00c4e7a0 bytes b0bfff97
- 00c4e780 ["INT_ADD", "register:40f0:8", ["const:c4e780:8", "const:4:8"]]
- 00c4e780 ["CALL", null, ["callee:00c3ad68:8"]]
+ 00c4e81c ["INT_ADD", "register:40f0:8", ["const:c4e81c:8", "const:4:8"]]
+ 00c4e81c ["CALL", null, ["callee:00c3ad68:8"]]
- 00c4e780 bytes 53b1ff97
+ 00c4e81c bytes 53b1ff97
- 00c4e7a8 ["INT_ADD", "register:40f0:8", ["const:c4e7a8:8", "const:4:8"]]
- 00c4e7a8 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4e844 ["INT_ADD", "register:40f0:8", ["const:c4e844:8", "const:4:8"]]
+ 00c4e844 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4e7a8 bytes 1e2e0094
+ 00c4e844 bytes 2b2e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f2717541a9d1974502ad948d72fa9b"></a>

### [`00c4e9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md) → [`00c4ea5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md) FUN_00c4ea5c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4ea2c",
      "incomplete_value": false,
      "site": "00c4ea2c",
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
            "const:640:8"
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
      "00c4eac8",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4eac8",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md#insn-00c4e9f4) · [`00c4ea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md#insn-00c4ea1c) · [`00c4ea24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md#insn-00c4ea24)
- 新版 `00c4ea90`（命令位置の公開資料なし） · `00c4eab8`（命令位置の公開資料なし） · `00c4eac0`（命令位置の公開資料なし）

~~~diff
- 00c4e9f4 ["INT_ADD", "register:40f0:8", ["const:c4e9f4:8", "const:4:8"]]
- 00c4e9f4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4ea90 ["INT_ADD", "register:40f0:8", ["const:c4ea90:8", "const:4:8"]]
+ 00c4ea90 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4e9f4 bytes 8b2d0094
+ 00c4ea90 bytes 982d0094
- 00c4ea1c ["INT_ADD", "register:40f0:8", ["const:c4ea1c:8", "const:4:8"]]
- 00c4ea1c ["CALL", null, ["callee:00c580b0:8"]]
+ 00c4eab8 ["INT_ADD", "register:40f0:8", ["const:c4eab8:8", "const:4:8"]]
+ 00c4eab8 ["CALL", null, ["callee:00c580b0:8"]]
- 00c4ea1c bytes 71250094
+ 00c4eab8 bytes 7e250094
- 00c4ea24 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c4ea24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4ea24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4ea24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4eac0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4eac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4eac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4eac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4ea24 bytes 29011991
+ 00c4eac0 bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aff495d78cda07ecd59249cc6baf042a"></a>

### [`00c4ea6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md) → [`00c4eb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md) FUN_00c4eb08

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00c4ead8",
      "incomplete_value": false,
      "site": "00c4ead8",
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
            "const:640:8"
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
      "00c4eb74",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4eb74",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4eaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md#insn-00c4eaa0) · [`00c4eac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md#insn-00c4eac8) · [`00c4ead0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md#insn-00c4ead0)
- 新版 `00c4eb3c`（命令位置の公開資料なし） · `00c4eb64`（命令位置の公開資料なし） · `00c4eb6c`（命令位置の公開資料なし）

~~~diff
- 00c4eaa0 ["INT_ADD", "register:40f0:8", ["const:c4eaa0:8", "const:4:8"]]
- 00c4eaa0 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4eb3c ["INT_ADD", "register:40f0:8", ["const:c4eb3c:8", "const:4:8"]]
+ 00c4eb3c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4eaa0 bytes 602d0094
+ 00c4eb3c bytes 6d2d0094
- 00c4eac8 ["INT_ADD", "register:40f0:8", ["const:c4eac8:8", "const:4:8"]]
- 00c4eac8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c4eb64 ["INT_ADD", "register:40f0:8", ["const:c4eb64:8", "const:4:8"]]
+ 00c4eb64 ["CALL", null, ["callee:00c580b0:8"]]
- 00c4eac8 bytes 46250094
+ 00c4eb64 bytes 53250094
- 00c4ead0 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c4ead0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4ead0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4ead0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4eb6c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4eb6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4eb6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4eb6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4ead0 bytes 29011991
+ 00c4eb6c bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

