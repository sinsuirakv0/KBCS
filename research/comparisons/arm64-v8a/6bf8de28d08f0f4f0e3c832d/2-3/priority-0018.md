# v16.0.2 → v16.0.3 · 最優先の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-48da99702aa65ec84af0ff4fab7f0066"></a>

### [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) → [`00583c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md) FUN_00583c0c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005838e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838e4.md) [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) · 呼出先 25件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00583e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md) [`00587168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587168.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 2件 [`00583c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c04.md) [`00584c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584c98.md) · 呼出先 25件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00584138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584138.md) [`00587488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587488.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.63% / 新版 93.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00583c94",
      "incomplete_value": true,
      "site": "00583ca8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:730:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583974",
      "incomplete_value": true,
      "site": "00583988",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6e0:8"
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
      "definition_site": "00583ca0",
      "incomplete_value": true,
      "site": "00583cb0",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583980",
      "incomplete_value": true,
      "site": "00583990",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
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
      "definition_site": "00583ca0",
      "incomplete_value": true,
      "site": "00583cb0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00583980",
      "incomplete_value": true,
      "site": "00583990",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00583c64",
      "READ",
      [
        "storage",
        "002ad8b3",
        null,
        "string"
      ]
    ],
    [
      "00583c6c",
      "READ",
      [
        "storage",
        "002ad8b9",
        null,
        "string"
      ]
    ],
    [
      "00583c94",
      "READ",
      [
        "storage",
        "002c26e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00583c64",
      "READ",
      [
        "storage",
        "002ad980",
        null,
        "string"
      ]
    ],
    [
      "00583c6c",
      "READ",
      [
        "storage",
        "002ad986",
        null,
        "string"
      ]
    ],
    [
      "00583c94",
      "READ",
      [
        "storage",
        "002c2730",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md#insn-00583c80) · [`00583cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md#insn-00583cb0) · [`00583cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md#insn-00583cb8)
- 新版 [`00583fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md#insn-00583fa0) · [`00583fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md#insn-00583fd0) · [`00583fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md#insn-00583fd8)

~~~diff
- 00583c80 ["INT_ADD", "register:40f0:8", ["const:583c80:8", "const:4:8"]]
- 00583c80 ["CALL", null, ["callee:00587488:8"]]
+ 00583fa0 ["INT_ADD", "register:40f0:8", ["const:583fa0:8", "const:4:8"]]
+ 00583fa0 ["CALL", null, ["callee:00587488:8"]]
- 00583c80 bytes 3a0d0094
+ 00583fa0 bytes 3a0d0094
- 00583cb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00583cb0 ["INT_ADD", "register:40f0:8", ["const:583cb0:8", "const:4:8"]]
- 00583cb0 ["CALLIND", null, ["register:0:8"]]
+ 00583fd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00583fd0 ["INT_ADD", "register:40f0:8", ["const:583fd0:8", "const:4:8"]]
+ 00583fd0 ["CALLIND", null, ["register:0:8"]]
- 00583cb0 bytes 00013fd6
+ 00583fd0 bytes 00013fd6
- 00583cb8 ["INT_ADD", "register:40f0:8", ["const:583cb8:8", "const:4:8"]]
- 00583cb8 ["CALL", null, ["callee:0058ac1c:8"]]
+ 00583fd8 ["INT_ADD", "register:40f0:8", ["const:583fd8:8", "const:4:8"]]
+ 00583fd8 ["CALL", null, ["callee:0058ac1c:8"]]
- 00583cb8 bytes 111b0094
+ 00583fd8 bytes 111b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69436c575ecc6ac020d101529a9d8e9"></a>

### [`00583e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md) → [`00584138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584138.md) FUN_00584138

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`00583c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md) [`0058450c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md) · 呼出先 7件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00584248",
      "incomplete_value": false,
      "site": "00584250",
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
            "const:1de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583f28",
      "incomplete_value": false,
      "site": "00583f30",
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
            "const:19e:8"
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
      "definition_site": "005842ac",
      "incomplete_value": false,
      "site": "005842b4",
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
            "const:de9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583f8c",
      "incomplete_value": false,
      "site": "00583f94",
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
            "const:d12:8"
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
      "definition_site": "00584310",
      "incomplete_value": false,
      "site": "00584318",
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
            "const:98d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583ff0",
      "incomplete_value": false,
      "site": "00583ff8",
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
            "const:8c0:8"
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
      "00584248",
      "PARAM",
      [
        "storage",
        "002a019e",
        null,
        "string"
      ]
    ],
    [
      "005842ac",
      "PARAM",
      [
        "storage",
        "002b0d12",
        null,
        "string"
      ]
    ],
    [
      "00584310",
      "PARAM",
      [
        "storage",
        "002ac8c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00584248",
      "PARAM",
      [
        "storage",
        "002a01de",
        null,
        "string"
      ]
    ],
    [
      "005842ac",
      "PARAM",
      [
        "storage",
        "002b0de9",
        null,
        "string"
      ]
    ],
    [
      "00584310",
      "PARAM",
      [
        "storage",
        "002ac98d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md#insn-00583f30) · [`00583f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md#insn-00583f94) · [`00583ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md#insn-00583ff8)
- 新版 [`00584250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584138.md#insn-00584250) · [`005842b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584138.md#insn-005842b4) · [`00584318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584138.md#insn-00584318)

~~~diff
- 00583f30 ["INT_ADD", "register:40f0:8", ["const:583f30:8", "const:4:8"]]
- 00583f30 ["CALL", null, ["callee:00c59010:8"]]
+ 00584250 ["INT_ADD", "register:40f0:8", ["const:584250:8", "const:4:8"]]
+ 00584250 ["CALL", null, ["callee:00c59010:8"]]
- 00583f30 bytes 44501b94
+ 00584250 bytes 70531b94
- 00583f94 ["INT_ADD", "register:40f0:8", ["const:583f94:8", "const:4:8"]]
- 00583f94 ["CALL", null, ["callee:00c59010:8"]]
+ 005842b4 ["INT_ADD", "register:40f0:8", ["const:5842b4:8", "const:4:8"]]
+ 005842b4 ["CALL", null, ["callee:00c59010:8"]]
- 00583f94 bytes 2b501b94
+ 005842b4 bytes 57531b94
- 00583ff8 ["INT_ADD", "register:40f0:8", ["const:583ff8:8", "const:4:8"]]
- 00583ff8 ["CALL", null, ["callee:00c59010:8"]]
+ 00584318 ["INT_ADD", "register:40f0:8", ["const:584318:8", "const:4:8"]]
+ 00584318 ["CALL", null, ["callee:00c59010:8"]]
- 00583ff8 bytes 12501b94
+ 00584318 bytes 3e531b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b3c827eae17125baa016681a74d0630"></a>

### [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) → [`0058450c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md) FUN_0058450c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005841e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841e4.md) · 呼出先 27件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00583e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md) [`00586850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586850.md) [`005869b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005869b4.md) [`0058728c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md)
- 新版 呼出元 1件 [`00584504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584504.md) · 呼出先 27件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00584138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584138.md) [`00586b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586b70.md) [`00586cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586cd4.md) [`005875ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005875ac.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005845a4",
      "incomplete_value": true,
      "site": "005845b0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:730:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584284",
      "incomplete_value": true,
      "site": "00584290",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:6e0:8"
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
      "definition_site": "00584880",
      "incomplete_value": false,
      "site": "00584890",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584560",
      "incomplete_value": false,
      "site": "00584570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005849f0",
      "value": [
        "leaf",
        "ram:58a268:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005846d0",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "ordinal": 42,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00584570",
      "READ",
      [
        "storage",
        "002ad8b3",
        null,
        "string"
      ]
    ],
    [
      "00584578",
      "READ",
      [
        "storage",
        "002ad8b9",
        null,
        "string"
      ]
    ],
    [
      "005845a0",
      "READ",
      [
        "storage",
        "002a438f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00584570",
      "READ",
      [
        "storage",
        "002ad980",
        null,
        "string"
      ]
    ],
    [
      "00584578",
      "READ",
      [
        "storage",
        "002ad986",
        null,
        "string"
      ]
    ],
    [
      "005845a0",
      "READ",
      [
        "storage",
        "002a445a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00584570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md#insn-00584570) · [`005845b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md#insn-005845b0) · [`005846d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md#insn-005846d0)
- 新版 [`00584890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md#insn-00584890) · [`005848d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md#insn-005848d0) · [`005849f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md#insn-005849f0)

~~~diff
- 00584570 ["INT_ADD", "register:40f0:8", ["const:584570:8", "const:4:8"]]
- 00584570 ["CALL", null, ["callee:005875ac:8"]]
+ 00584890 ["INT_ADD", "register:40f0:8", ["const:584890:8", "const:4:8"]]
+ 00584890 ["CALL", null, ["callee:005875ac:8"]]
- 00584570 bytes 470b0094
+ 00584890 bytes 470b0094
- 005845b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005845b0 ["INT_ADD", "register:40f0:8", ["const:5845b0:8", "const:4:8"]]
- 005845b0 ["CALLIND", null, ["register:0:8"]]
+ 005848d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005848d0 ["INT_ADD", "register:40f0:8", ["const:5848d0:8", "const:4:8"]]
+ 005848d0 ["CALLIND", null, ["register:0:8"]]
- 005845b0 bytes 00013fd6
+ 005848d0 bytes 00013fd6
- 005846d0 ["INT_ADD", "register:40f0:8", ["const:5846d0:8", "const:4:8"]]
- 005846d0 ["CALL", null, ["ram:589f48:8"]]
+ 005849f0 ["INT_ADD", "register:40f0:8", ["const:5849f0:8", "const:4:8"]]
+ 005849f0 ["CALL", null, ["ram:58a268:8"]]
- 005846d0 bytes 1e160094
+ 005849f0 bytes 1e160094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98610454d227c90e171e864bf228cead"></a>

### [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) → [`00584c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584c98.md) FUN_00584c98

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005874a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874a8.md) [`00587508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587508.md) [`0058788c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058788c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00583c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md) [`005877c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005877c8.md) [`00587828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587828.md) [`00587bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587bac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00584cdc",
      "incomplete_value": false,
      "site": "00584ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005849bc",
      "incomplete_value": false,
      "site": "005849c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      "definition_site": "00584d08",
      "incomplete_value": false,
      "site": "00584d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005849e8",
      "incomplete_value": false,
      "site": "005849f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "definition_site": "00584d78",
      "incomplete_value": false,
      "site": "00584d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584a58",
      "incomplete_value": false,
      "site": "00584a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00584ce4",
      "DATA",
      [
        "storage",
        "00c6cb28",
        null,
        "pointer"
      ]
    ],
    [
      "00584d10",
      "DATA",
      [
        "storage",
        "00c6cb78",
        null,
        "pointer"
      ]
    ],
    [
      "00584d78",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00584ce4",
      "DATA",
      [
        "storage",
        "00c6daf8",
        null,
        "pointer"
      ]
    ],
    [
      "00584d10",
      "DATA",
      [
        "storage",
        "00c6db48",
        null,
        "pointer"
      ]
    ],
    [
      "00584d78",
      "DATA",
      [
        "storage",
        "00c6db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005849b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md#insn-005849b0) · [`005849b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md#insn-005849b8) · [`005849bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md#insn-005849bc)
- 新版 [`00584cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584c98.md#insn-00584cd0) · [`00584cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584c98.md#insn-00584cd8) · [`00584cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/00584c98.md#insn-00584cdc)

~~~diff
- 005849b0 ["INT_ADD", "register:40f0:8", ["const:5849b0:8", "const:4:8"]]
- 005849b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00584cd0 ["INT_ADD", "register:40f0:8", ["const:584cd0:8", "const:4:8"]]
+ 00584cd0 ["CALL", null, ["callee:00c58f30:8"]]
- 005849b0 bytes 6c4d1b94
+ 00584cd0 bytes 98501b94
- 005849b8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00584cd8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005849b8 bytes 48370090
+ 00584cd8 bytes 483700b0
- 005849bc ["COPY", "tmp:0:8", ["const:b28:8"]]
- 005849bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005849bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005849bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00584cdc ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00584cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00584cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00584cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005849bc bytes 08a12c91
+ 00584cdc bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48c9eee80a75d1ce2238d4fae637d6d"></a>

### [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) → [`0058572c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/0058572c.md) FUN_0058572c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`0058660c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058660c.md) · 呼出先 10件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00587f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md) [`00587fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md) [`00588134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588134.md)
- 新版 呼出元 2件 [`00585a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md) [`0058692c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/0058692c.md) · 呼出先 10件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00588274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588274.md) [`005882c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005882c4.md) [`00588454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588454.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00585958",
      "incomplete_value": true,
      "site": "00585958",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00585638",
      "incomplete_value": true,
      "site": "00585638",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058575c",
      "incomplete_value": true,
      "site": "0058575c",
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
      "definition_site": "0058543c",
      "incomplete_value": true,
      "site": "0058543c",
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
      "definition_site": "005857ec",
      "incomplete_value": true,
      "site": "005857ec",
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
      "definition_site": "005854cc",
      "incomplete_value": true,
      "site": "005854cc",
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
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00585758",
      "READ",
      [
        "storage",
        "00ca6440",
        null,
        "undefined8"
      ]
    ],
    [
      "005857a0",
      "READ",
      [
        "storage",
        "00ca64f0",
        null,
        "undefined8"
      ]
    ],
    [
      "005857c4",
      "PARAM",
      [
        "storage",
        "00ca6438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00585758",
      "READ",
      [
        "storage",
        "00ca7400",
        null,
        "undefined8"
      ]
    ],
    [
      "005857a0",
      "READ",
      [
        "storage",
        "00ca74b0",
        null,
        "undefined8"
      ]
    ],
    [
      "005857c4",
      "PARAM",
      [
        "storage",
        "00ca73f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005854ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md#insn-005854ac) · [`00585564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md#insn-00585564) · [`00585638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md#insn-00585638)
- 新版 [`005857cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/0058572c.md#insn-005857cc) · [`00585884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/0058572c.md#insn-00585884) · [`00585958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/0058572c.md#insn-00585958)

~~~diff
- 005854ac ["INT_ADD", "register:40f0:8", ["const:5854ac:8", "const:4:8"]]
- 005854ac ["CALL", null, ["callee:00588454:8"]]
+ 005857cc ["INT_ADD", "register:40f0:8", ["const:5857cc:8", "const:4:8"]]
+ 005857cc ["CALL", null, ["callee:00588454:8"]]
- 005854ac bytes 220b0094
+ 005857cc bytes 220b0094
- 00585564 ["INT_ADD", "register:40f0:8", ["const:585564:8", "const:4:8"]]
- 00585564 ["CALL", null, ["callee:005882c4:8"]]
+ 00585884 ["INT_ADD", "register:40f0:8", ["const:585884:8", "const:4:8"]]
+ 00585884 ["CALL", null, ["callee:005882c4:8"]]
- 00585564 bytes 900a0094
+ 00585884 bytes 900a0094
- 00585638 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
- 00585638 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00585958 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e0:8"]]
+ 00585958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00585638 bytes 281102f9
+ 00585958 bytes 28f101f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5532657c7eb6c1257cb38e3902ab76b"></a>

### [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) → [`00585a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md) Java_jp_co_ponos_battlecats_MyActivity_newResponse

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0057e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md) [`00581e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e50.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`0057e3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3f0.md) [`00582170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582170.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 3件, `store_condition` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00585b88",
      "incomplete_value": false,
      "site": "00585b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00585868",
      "incomplete_value": false,
      "site": "00585874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00585f28",
      "incomplete_value": true,
      "site": "00585f28",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00585c08",
      "incomplete_value": true,
      "site": "00585c08",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00585a74",
      "incomplete_value": true,
      "site": "00585a74",
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
      "definition_site": "00585754",
      "incomplete_value": true,
      "site": "00585754",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00585a6c",
      "READ",
      [
        "storage",
        "00ca6428",
        null,
        "undefined8"
      ]
    ],
    [
      "00585ab8",
      "READ",
      [
        "storage",
        "00ca6478",
        null,
        "undefined8"
      ]
    ],
    [
      "00585b94",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00585a6c",
      "READ",
      [
        "storage",
        "00ca73e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00585ab8",
      "READ",
      [
        "storage",
        "00ca7438",
        null,
        "undefined8"
      ]
    ],
    [
      "00585b94",
      "DATA",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058575c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md#insn-0058575c) · [`00585c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md#insn-00585c08) · [`0058572c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md#insn-0058572c)
- 新版 [`00585a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md#insn-00585a7c) · [`00585f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md#insn-00585f28) · [`00585a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md#insn-00585a4c)

~~~diff
- 0058575c ["COPY", "tmp:0:8", ["const:428:8"]]
- 0058575c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058575c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058575c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00585a7c ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00585a7c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00585a7c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00585a7c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058575c bytes 73a21091
+ 00585a7c bytes 73a20f91
- 00585c08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
- 00585c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00585f28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e0:8"]]
+ 00585f28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00585c08 bytes 281102f9
+ 00585f28 bytes 28f101f9
- 0058572c ["COPY", "register:40d0:8", ["const:ca6000:8"]]
+ 00585a4c ["COPY", "register:40d0:8", ["const:ca7000:8"]]
- 0058572c bytes 1a3900b0
+ 00585a4c bytes 1a3900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8533d333016b65699a1c120e5819cc2a"></a>

### [`00585f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md) → [`00586270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586270.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseCodeHeaders

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00585d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md) [`00588394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`005860b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/005860b0.md) [`005886b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005886b4.md) [`00589cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589cb4.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005862a4",
      "incomplete_value": true,
      "site": "005862a4",
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
      "definition_site": "00585f84",
      "incomplete_value": true,
      "site": "00585f84",
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
      "definition_site": "005863bc",
      "incomplete_value": true,
      "site": "005863bc",
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
      "definition_site": "0058609c",
      "incomplete_value": true,
      "site": "0058609c",
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "0058609c"
      ],
      [
        "FALL_THROUGH",
        "005863bc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005863bc",
      "incomplete_value": true,
      "site": "005863dc",
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
      "definition_site": "0058609c",
      "incomplete_value": true,
      "site": "005860bc",
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
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058629c",
      "READ",
      [
        "storage",
        "00ca6440",
        null,
        "undefined8"
      ]
    ],
    [
      "005862f8",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ],
    [
      "005863b4",
      "READ",
      [
        "storage",
        "00ca63e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058629c",
      "READ",
      [
        "storage",
        "00ca7400",
        null,
        "undefined8"
      ]
    ],
    [
      "005862f8",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ],
    [
      "005863b4",
      "READ",
      [
        "storage",
        "00ca73a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00585f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md#insn-00585f74) · [`00585f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md#insn-00585f78) · [`00585f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md#insn-00585f88)
- 新版 [`00586294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586270.md#insn-00586294) · [`00586298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586270.md#insn-00586298) · [`005862a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586270.md#insn-005862a8)

~~~diff
- 00585f74 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 00586294 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 00585f74 bytes 083900b0
+ 00586294 bytes 083900b0
- 00585f78 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00585f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00585f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00585f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00586298 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00586298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00586298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00586298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00585f78 bytes 08011191
+ 00586298 bytes 08011091
- 00585f88 ["COPY", "register:40b0:8", ["const:ca6000:8"]]
+ 005862a8 ["COPY", "register:40b0:8", ["const:ca7000:8"]]
- 00585f88 bytes 163900b0
+ 005862a8 bytes 163900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b4595d62d3b46634890efbce544d818"></a>

### [`00586324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md) → [`00586644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586644.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseData

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0057e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md) [`00581e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e50.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0057e3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3f0.md) [`00582170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582170.md) [`00589f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00586674",
      "incomplete_value": true,
      "site": "00586674",
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
      "definition_site": "00586354",
      "incomplete_value": true,
      "site": "00586354",
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
      "definition_site": "005867b4",
      "incomplete_value": true,
      "site": "005867b4",
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
      "definition_site": "00586494",
      "incomplete_value": true,
      "site": "00586494",
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00586494"
      ],
      [
        "FALL_THROUGH",
        "005867b4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005867b4",
      "incomplete_value": true,
      "site": "005867d4",
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
      "definition_site": "00586494",
      "incomplete_value": true,
      "site": "005864b4",
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00586670",
      "READ",
      [
        "storage",
        "00ca6440",
        null,
        "undefined8"
      ]
    ],
    [
      "005866c8",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005866f8",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00586670",
      "READ",
      [
        "storage",
        "00ca7400",
        null,
        "undefined8"
      ]
    ],
    [
      "005866c8",
      "READ",
      [
        "storage",
        "00ca7480",
        null,
        "undefined8"
      ]
    ],
    [
      "005866f8",
      "DATA",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md#insn-00586348) · [`0058634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md#insn-0058634c) · [`00586358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md#insn-00586358)
- 新版 [`00586668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586644.md#insn-00586668) · [`0058666c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586644.md#insn-0058666c) · [`00586678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586644.md#insn-00586678)

~~~diff
- 00586348 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 00586668 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 00586348 bytes 08390090
+ 00586668 bytes 083900b0
- 0058634c ["COPY", "tmp:0:8", ["const:440:8"]]
- 0058634c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058634c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058634c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058666c ["COPY", "tmp:0:8", ["const:400:8"]]
+ 0058666c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058666c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058666c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058634c bytes 08011191
+ 0058666c bytes 08011091
- 00586358 ["COPY", "register:40c0:8", ["const:ca6000:8"]]
+ 00586678 ["COPY", "register:40c0:8", ["const:ca7000:8"]]
- 00586358 bytes 18390090
+ 00586678 bytes 183900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3235a2692e387f13cd2c3cc78232a97"></a>

### [`0058661c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058661c.md) → [`0058693c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/0058693c.md) FUN_0058693c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058671c.md) · 呼出先 4件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00586a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586a3c.md) · 呼出先 4件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00586958",
      "incomplete_value": false,
      "site": "0058695c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00586638",
      "incomplete_value": false,
      "site": "0058663c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "0058695c",
      "DATA",
      [
        "storage",
        "00c6c9b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058695c",
      "DATA",
      [
        "storage",
        "00c6d988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058661c.md#insn-00586634) · [`00586638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058661c.md#insn-00586638) · [`00586674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058661c.md#insn-00586674)
- 新版 [`00586954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/0058693c.md#insn-00586954) · [`00586958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/0058693c.md#insn-00586958) · [`00586994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/0058693c.md#insn-00586994)

~~~diff
- 00586634 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00586954 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00586634 bytes 283700d0
+ 00586954 bytes 283700f0
- 00586638 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00586638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00586638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00586638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00586958 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 00586958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00586958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00586958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00586638 bytes 08e12691
+ 00586958 bytes 08212691
- 00586674 ["INT_ADD", "register:40f0:8", ["const:586674:8", "const:4:8"]]
- 00586674 ["CALL", null, ["callee:00c54d90:8"]]
+ 00586994 ["INT_ADD", "register:40f0:8", ["const:586994:8", "const:4:8"]]
+ 00586994 ["CALL", null, ["callee:00c54d90:8"]]
- 00586674 bytes cb351b94
+ 00586994 bytes ff381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c729755e1733c28fb63405065d84945d"></a>

### [`00586740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586740.md) → [`00586a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586a60.md) FUN_00586a60

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00586a78",
      "incomplete_value": false,
      "site": "00586a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00586758",
      "incomplete_value": false,
      "site": "0058675c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00586a7c",
      "DATA",
      [
        "storage",
        "00c6c998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00586a7c",
      "DATA",
      [
        "storage",
        "00c6d968",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00586754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586740.md#insn-00586754) · [`00586758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586740.md#insn-00586758) · [`0058678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586740.md#insn-0058678c)
- 新版 [`00586a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586a60.md#insn-00586a74) · [`00586a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586a60.md#insn-00586a78) · [`00586aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586a60.md#insn-00586aac)

~~~diff
- 00586754 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00586a74 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00586754 bytes 293700d0
+ 00586a74 bytes 293700f0
- 00586758 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00586758 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00586758 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00586758 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00586a78 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00586a78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00586a78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00586a78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00586758 bytes 29612691
+ 00586a78 bytes 29a12591
- 0058678c ["INT_ADD", "register:40f0:8", ["const:58678c:8", "const:4:8"]]
- 0058678c ["CALL", null, ["callee:00c58f50:8"]]
+ 00586aac ["INT_ADD", "register:40f0:8", ["const:586aac:8", "const:4:8"]]
+ 00586aac ["CALL", null, ["callee:00c58f50:8"]]
- 0058678c bytes fd451b94
+ 00586aac bytes 29491b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b44b94520ccfa9de0a03aed26e5a974e"></a>

### [`005867c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005867c8.md) → [`00586ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586ae8.md) FUN_00586ae8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00586b00",
      "incomplete_value": false,
      "site": "00586b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005867e0",
      "incomplete_value": false,
      "site": "005867e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00586b04",
      "DATA",
      [
        "storage",
        "00c6c998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00586b04",
      "DATA",
      [
        "storage",
        "00c6d968",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005867dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005867c8.md#insn-005867dc) · [`005867e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005867c8.md#insn-005867e0) · [`00586808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005867c8.md#insn-00586808)
- 新版 [`00586afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586ae8.md#insn-00586afc) · [`00586b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586ae8.md#insn-00586b00) · [`00586b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586ae8.md#insn-00586b28)

~~~diff
- 005867dc ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00586afc ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 005867dc bytes 293700d0
+ 00586afc bytes 293700f0
- 005867e0 ["COPY", "tmp:0:8", ["const:998:8"]]
- 005867e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005867e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005867e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00586b00 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00586b00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00586b00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00586b00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005867e0 bytes 29612691
+ 00586b00 bytes 29a12591
- 00586808 ["INT_ADD", "register:40f0:8", ["const:586808:8", "const:4:8"]]
- 00586808 ["CALL", null, ["callee:00c58f50:8"]]
+ 00586b28 ["INT_ADD", "register:40f0:8", ["const:586b28:8", "const:4:8"]]
+ 00586b28 ["CALL", null, ["callee:00c58f50:8"]]
- 00586808 bytes de451b94
+ 00586b28 bytes 0a491b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be7e27906e4b15620d21bee216273ad7"></a>

### [`00587118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587118.md) → [`00587438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587438.md) FUN_00587438

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "0058743c",
      "incomplete_value": false,
      "site": "00587440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058711c",
      "incomplete_value": false,
      "site": "00587120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00587440",
      "DATA",
      [
        "storage",
        "00c6cad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587440",
      "DATA",
      [
        "storage",
        "00c6daa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587118.md#insn-00587118) · [`0058711c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587118.md#insn-0058711c)
- 新版 [`00587438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587438.md#insn-00587438) · [`0058743c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587438.md#insn-0058743c)

~~~diff
- 00587118 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00587438 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587118 bytes 283700b0
+ 00587438 bytes 283700d0
- 0058711c ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0058711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058743c ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0058743c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058743c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058743c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058711c bytes 08612b91
+ 0058743c bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85c723c6d2d043a06e25f49ae48652c7"></a>

### [`00587468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587468.md) → [`00587788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587788.md) FUN_00587788

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "0058778c",
      "incomplete_value": false,
      "site": "00587790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058746c",
      "incomplete_value": false,
      "site": "00587470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00587790",
      "DATA",
      [
        "storage",
        "00c6cb28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587790",
      "DATA",
      [
        "storage",
        "00c6daf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587468.md#insn-00587468) · [`0058746c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587468.md#insn-0058746c)
- 新版 [`00587788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587788.md#insn-00587788) · [`0058778c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587788.md#insn-0058778c)

~~~diff
- 00587468 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00587788 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587468 bytes 283700b0
+ 00587788 bytes 283700d0
- 0058746c ["COPY", "tmp:0:8", ["const:b28:8"]]
- 0058746c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058746c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058746c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058778c ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 0058778c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058778c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058778c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058746c bytes 08a12c91
+ 0058778c bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a03db7b1094c68acf013337cfe701394"></a>

### [`00587478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587478.md) → [`00587798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587798.md) FUN_00587798

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005877a8",
      "incomplete_value": false,
      "site": "005877b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587488",
      "incomplete_value": false,
      "site": "00587490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      "005877b0",
      "DATA",
      [
        "storage",
        "00c6cb28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005877b0",
      "DATA",
      [
        "storage",
        "00c6daf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587478.md#insn-00587484) · [`00587488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587478.md#insn-00587488) · [`00587494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587478.md#insn-00587494)
- 新版 [`005877a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587798.md#insn-005877a4) · [`005877a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587798.md#insn-005877a8) · [`005877b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587798.md#insn-005877b4)

~~~diff
- 00587484 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005877a4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587484 bytes 283700b0
+ 005877a4 bytes 283700d0
- 00587488 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00587488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005877a8 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 005877a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005877a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005877a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587488 bytes 08a12c91
+ 005877a8 bytes 08e12b91
- 00587494 ["INT_ADD", "register:40f0:8", ["const:587494:8", "const:4:8"]]
- 00587494 ["CALL", null, ["callee:00c58f40:8"]]
+ 005877b4 ["INT_ADD", "register:40f0:8", ["const:5877b4:8", "const:4:8"]]
+ 005877b4 ["CALL", null, ["callee:00c58f40:8"]]
- 00587494 bytes b7421b94
+ 005877b4 bytes e3451b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2dea05d4e75a52be8721deb2da72708"></a>

### [`005874b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874b4.md) → [`005877d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005877d4.md) FUN_005877d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005877f8",
      "incomplete_value": true,
      "site": "005877f8",
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
      "definition_site": "005874d8",
      "incomplete_value": true,
      "site": "005874d8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005877ec",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "005877f8",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005877ec",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "005877f8",
      "DATA",
      [
        "storage",
        "00c93d78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005874c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874b4.md#insn-005874c0) · [`005874cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874b4.md#insn-005874cc) · [`005874dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874b4.md#insn-005874dc)
- 新版 [`005877e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005877d4.md#insn-005877e0) · [`005877ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005877d4.md#insn-005877ec) · [`005877fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005877d4.md#insn-005877fc)

~~~diff
- 005874c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005877e0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005874c0 bytes 883800f0
+ 005877e0 bytes a8380090
- 005874cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 005874cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005877ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 005877ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005874cc bytes 089146f9
+ 005877ec bytes 087946f9
- 005874dc ["INT_ADD", "register:40f0:8", ["const:5874dc:8", "const:4:8"]]
- 005874dc ["CALL", null, ["callee:00c59170:8"]]
+ 005877fc ["INT_ADD", "register:40f0:8", ["const:5877fc:8", "const:4:8"]]
+ 005877fc ["CALL", null, ["callee:00c59170:8"]]
- 005874dc bytes 31431b94
+ 005877fc bytes 5d461b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f0f139b78483e1e8c5fec9bc64e3f6"></a>

### [`00587628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587628.md) → [`00587948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587948.md) FUN_00587948

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005874a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874a8.md) · 呼出先 12件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)
- 新版 呼出元 1件 [`005877c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005877c8.md) · 呼出先 12件 [`0045aa28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa28.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.15% / 新版 93.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005879ec",
      "incomplete_value": true,
      "site": "005879f0",
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
      "definition_site": "005876cc",
      "incomplete_value": true,
      "site": "005876d0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005879c8",
      "incomplete_value": true,
      "site": "005879d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005876a8",
      "incomplete_value": true,
      "site": "005876b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005879c4",
      "incomplete_value": false,
      "site": "005879d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:45a000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005876a4",
      "incomplete_value": false,
      "site": "005876b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:45a000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005879c4",
      "PARAM",
      [
        "storage",
        "0045a708",
        null,
        null
      ]
    ],
    [
      "005879c8",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005879c8",
      "PARAM",
      [
        "storage",
        "00c92d80",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005879c4",
      "PARAM",
      [
        "storage",
        "0045aa28",
        null,
        null
      ]
    ],
    [
      "005879c8",
      "READ",
      [
        "storage",
        "00c9bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "005879c8",
      "PARAM",
      [
        "storage",
        "00c93d50",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005876b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587628.md#insn-005876b0) · [`00587668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587628.md#insn-00587668) · [`00587680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587628.md#insn-00587680)
- 新版 [`005879d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587948.md#insn-005879d0) · [`00587988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587948.md#insn-00587988) · [`005879a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587948.md#insn-005879a0)

~~~diff
- 005876b0 ["INT_ADD", "register:40f0:8", ["const:5876b0:8", "const:4:8"]]
- 005876b0 ["CALL", null, ["callee:00c593d0:8"]]
+ 005879d0 ["INT_ADD", "register:40f0:8", ["const:5879d0:8", "const:4:8"]]
+ 005879d0 ["CALL", null, ["callee:00c593d0:8"]]
- 005876b0 bytes 54431b94
+ 005879d0 bytes 80461b94
- 00587668 ["INT_ADD", "register:40f0:8", ["const:587668:8", "const:4:8"]]
- 00587668 ["CALL", null, ["callee:00c59390:8"]]
+ 00587988 ["INT_ADD", "register:40f0:8", ["const:587988:8", "const:4:8"]]
+ 00587988 ["CALL", null, ["callee:00c59390:8"]]
- 00587668 bytes 56431b94
+ 00587988 bytes 82461b94
- 00587680 ["INT_ADD", "register:40f0:8", ["const:587680:8", "const:4:8"]]
- 00587680 ["CALL", null, ["callee:00c593b0:8"]]
+ 005879a0 ["INT_ADD", "register:40f0:8", ["const:5879a0:8", "const:4:8"]]
+ 005879a0 ["CALL", null, ["callee:00c593b0:8"]]
- 00587680 bytes 58431b94
+ 005879a0 bytes 84461b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69398a3e8bdcd21780371c2ccd81342c"></a>

### [`00587750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587750.md) → [`00587a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587a70.md) FUN_00587a70

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00587a84",
      "incomplete_value": false,
      "site": "00587a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587764",
      "incomplete_value": false,
      "site": "00587768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00587a88",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587a88",
      "DATA",
      [
        "storage",
        "00c6db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587750.md#insn-00587760) · [`00587764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587750.md#insn-00587764) · [`00587778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587750.md#insn-00587778)
- 新版 [`00587a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587a70.md#insn-00587a80) · [`00587a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587a70.md#insn-00587a84) · [`00587a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587a70.md#insn-00587a98)

~~~diff
- 00587760 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00587a80 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587760 bytes 283700b0
+ 00587a80 bytes 283700d0
- 00587764 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00587764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587a84 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00587a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587764 bytes 08012f91
+ 00587a84 bytes 08412e91
- 00587778 ["INT_ADD", "register:40f0:8", ["const:587778:8", "const:4:8"]]
- 00587778 ["CALL", null, ["callee:00c54d90:8"]]
+ 00587a98 ["INT_ADD", "register:40f0:8", ["const:587a98:8", "const:4:8"]]
+ 00587a98 ["CALL", null, ["callee:00c54d90:8"]]
- 00587778 bytes 8a311b94
+ 00587a98 bytes be341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9940205ff8c765f5c9586982f1eac15"></a>

### [`005877ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005877ac.md) → [`00587acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587acc.md) FUN_00587acc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00587ae4",
      "incomplete_value": false,
      "site": "00587ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005877c4",
      "incomplete_value": false,
      "site": "005877c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00587ae8",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587ae8",
      "DATA",
      [
        "storage",
        "00c6db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005877c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005877ac.md#insn-005877c0) · [`005877c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005877ac.md#insn-005877c4) · [`005877d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005877ac.md#insn-005877d8)
- 新版 [`00587ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587acc.md#insn-00587ae0) · [`00587ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587acc.md#insn-00587ae4) · [`00587af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587acc.md#insn-00587af8)

~~~diff
- 005877c0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00587ae0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005877c0 bytes 283700b0
+ 00587ae0 bytes 283700d0
- 005877c4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 005877c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005877c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005877c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ae4 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00587ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005877c4 bytes 08012f91
+ 00587ae4 bytes 08412e91
- 005877d8 ["INT_ADD", "register:40f0:8", ["const:5877d8:8", "const:4:8"]]
- 005877d8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00587af8 ["INT_ADD", "register:40f0:8", ["const:587af8:8", "const:4:8"]]
+ 00587af8 ["CALL", null, ["callee:00c54d90:8"]]
- 005877d8 bytes 72311b94
+ 00587af8 bytes a6341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bec81a3ed2cb6ed2d1bae412e47d9d6"></a>

### [`00587808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587808.md) → [`00587b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b28.md) FUN_00587b28

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00587b4c",
      "incomplete_value": false,
      "site": "00587b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058782c",
      "incomplete_value": false,
      "site": "0058782c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00587b4c",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587b4c",
      "DATA",
      [
        "storage",
        "00c6db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058781c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587808.md#insn-0058781c) · [`00587824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587808.md#insn-00587824) · [`00587828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587808.md#insn-00587828)
- 新版 [`00587b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b28.md#insn-00587b3c) · [`00587b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b28.md#insn-00587b44) · [`00587b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b28.md#insn-00587b48)

~~~diff
- 0058781c ["INT_ADD", "register:40f0:8", ["const:58781c:8", "const:4:8"]]
- 0058781c ["CALL", null, ["callee:00c58f30:8"]]
+ 00587b3c ["INT_ADD", "register:40f0:8", ["const:587b3c:8", "const:4:8"]]
+ 00587b3c ["CALL", null, ["callee:00c58f30:8"]]
- 0058781c bytes d1411b94
+ 00587b3c bytes fd441b94
- 00587824 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00587b44 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00587824 bytes 293700b0
+ 00587b44 bytes 293700d0
- 00587828 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00587828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00587828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00587828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00587b48 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00587b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00587b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00587b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00587828 bytes 29012f91
+ 00587b48 bytes 29412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12dd6f990a2d83e68601adeb0e5a4166"></a>

### [`00587858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587858.md) → [`00587b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b78.md) FUN_00587b78

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

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
      "definition_site": "00587b84",
      "incomplete_value": false,
      "site": "00587b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587864",
      "incomplete_value": false,
      "site": "00587864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00587b84",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587b84",
      "DATA",
      [
        "storage",
        "00c6db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587858.md#insn-0058785c) · [`00587860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587858.md#insn-00587860) · [`00587880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587858.md#insn-00587880)
- 新版 [`00587b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b78.md#insn-00587b7c) · [`00587b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b78.md#insn-00587b80) · [`00587ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587b78.md#insn-00587ba0)

~~~diff
- 0058785c ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00587b7c ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058785c bytes 293700b0
+ 00587b7c bytes 293700d0
- 00587860 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00587860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00587860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00587860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00587b80 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00587b80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00587b80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00587b80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00587860 bytes 29012f91
+ 00587b80 bytes 29412e91
- 00587880 ["INT_ADD", "register:40f0:8", ["const:587880:8", "const:4:8"]]
- 00587880 ["CALL", null, ["callee:00c54d60:8"]]
+ 00587ba0 ["INT_ADD", "register:40f0:8", ["const:587ba0:8", "const:4:8"]]
+ 00587ba0 ["CALL", null, ["callee:00c54d60:8"]]
- 00587880 bytes 3c311b94
+ 00587ba0 bytes 70341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b78194e71fa4b7ef6d8d41fb6fbf996"></a>

### [`00587dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587dd4.md) → [`005880f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005880f4.md) FUN_005880f4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00587c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00587fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/00587fb4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00588100",
      "incomplete_value": false,
      "site": "00588104",
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
      "definition_site": "00587de0",
      "incomplete_value": false,
      "site": "00587de4",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00588100",
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
      "00588100",
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


#### 変更候補の命令位置

- 旧版 [`00587de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587dd4.md#insn-00587de4) · [`00587ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587dd4.md#insn-00587ddc) · [`00587de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587dd4.md#insn-00587de0)
- 新版 [`00588104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005880f4.md#insn-00588104) · [`005880fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005880f4.md#insn-005880fc) · [`00588100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005880f4.md#insn-00588100)

~~~diff
- 00587de4 ["INT_ADD", "register:40f0:8", ["const:587de4:8", "const:4:8"]]
- 00587de4 ["CALL", null, ["callee:0043bad8:8"]]
+ 00588104 ["INT_ADD", "register:40f0:8", ["const:588104:8", "const:4:8"]]
+ 00588104 ["CALL", null, ["callee:0043bad8:8"]]
- 00587de4 bytes 75cefa97
+ 00588104 bytes 75cefa97
- 00587ddc ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005880fc ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00587ddc bytes 80e9ff90
+ 005880fc bytes 80e9ff90
- 00587de0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00587de0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00587de0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00587de0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00588100 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00588100 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00588100 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00588100 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00587de0 bytes 00303e91
+ 00588100 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2036146a92a4a741cc6c97d63ca5bce9"></a>

### [`00587de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587de8.md) → [`00588108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588108.md) FUN_00588108

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00585364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00585684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585684.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588124",
      "incomplete_value": false,
      "site": "00588124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587e04",
      "incomplete_value": false,
      "site": "00587e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588130",
      "incomplete_value": false,
      "site": "00588130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587e10",
      "incomplete_value": false,
      "site": "00587e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00588124",
      "DATA",
      [
        "storage",
        "00c6cc40",
        null,
        "undefined *"
      ]
    ],
    [
      "00588130",
      "DATA",
      [
        "storage",
        "00c6c9b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588124",
      "DATA",
      [
        "storage",
        "00c6dc10",
        null,
        "undefined *"
      ]
    ],
    [
      "00588130",
      "DATA",
      [
        "storage",
        "00c6d988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587de8.md#insn-00587df8) · [`00587dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587de8.md#insn-00587dfc) · [`00587e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587de8.md#insn-00587e08)
- 新版 [`00588118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588108.md#insn-00588118) · [`0058811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588108.md#insn-0058811c)

~~~diff
- 00587df8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588118 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587df8 bytes 283700b0
+ 00588118 bytes 283700b0
- 00587dfc ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00587dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058811c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0058811c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058811c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058811c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587dfc bytes 08013191
+ 0058811c bytes 08413091
- 00587e08 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00587e08 bytes 283700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1cb93005563d69a69081dbc5179dc1d"></a>

### [`00587ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ec4.md) → [`005881e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881e4.md) FUN_005881e4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "005881e8",
      "incomplete_value": false,
      "site": "005881ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587ec8",
      "incomplete_value": false,
      "site": "00587ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "005881ec",
      "DATA",
      [
        "storage",
        "00c6cc40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005881ec",
      "DATA",
      [
        "storage",
        "00c6dc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ec4.md#insn-00587ec4) · [`00587ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ec4.md#insn-00587ec8)
- 新版 [`005881e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881e4.md#insn-005881e4) · [`005881e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881e4.md#insn-005881e8)

~~~diff
- 00587ec4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005881e4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587ec4 bytes 283700b0
+ 005881e4 bytes 283700b0
- 00587ec8 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00587ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005881e8 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 005881e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005881e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005881e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587ec8 bytes 08013191
+ 005881e8 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7d3b2400fe531edb29450f17c20cee"></a>

### [`00587ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ed4.md) → [`005881f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881f4.md) FUN_005881f4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00588204",
      "incomplete_value": true,
      "site": "0058820c",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587ee4",
      "incomplete_value": true,
      "site": "00587eec",
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
            "const:c40:8"
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
      "0058820c",
      "DATA",
      [
        "storage",
        "00c6cc40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058820c",
      "DATA",
      [
        "storage",
        "00c6dc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ed4.md#insn-00587ee0) · [`00587ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ed4.md#insn-00587ee4) · [`00587ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ed4.md#insn-00587ef0)
- 新版 [`00588200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881f4.md#insn-00588200) · [`00588204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881f4.md#insn-00588204) · [`00588210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005881f4.md#insn-00588210)

~~~diff
- 00587ee0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588200 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587ee0 bytes 283700b0
+ 00588200 bytes 283700b0
- 00587ee4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00587ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588204 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00588204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587ee4 bytes 08013191
+ 00588204 bytes 08413091
- 00587ef0 ["INT_ADD", "register:40f0:8", ["const:587ef0:8", "const:4:8"]]
- 00587ef0 ["CALL", null, ["callee:00c58f40:8"]]
+ 00588210 ["INT_ADD", "register:40f0:8", ["const:588210:8", "const:4:8"]]
+ 00588210 ["CALL", null, ["callee:00c58f40:8"]]
- 00587ef0 bytes 20401b94
+ 00588210 bytes 4c431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93701c4c57ecb1fbeea67d2686c3050b"></a>

### [`00587f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f14.md) → [`00588234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588234.md) FUN_00588234

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "00588238",
      "incomplete_value": false,
      "site": "0058823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587f18",
      "incomplete_value": false,
      "site": "00587f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "0058823c",
      "DATA",
      [
        "storage",
        "00c6cc90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058823c",
      "DATA",
      [
        "storage",
        "00c6dc60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f14.md#insn-00587f14) · [`00587f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f14.md#insn-00587f18)
- 新版 [`00588234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588234.md#insn-00588234) · [`00588238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588234.md#insn-00588238)

~~~diff
- 00587f14 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588234 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587f14 bytes 283700b0
+ 00588234 bytes 283700b0
- 00587f18 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00587f18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587f18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587f18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588238 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00588238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587f18 bytes 08413291
+ 00588238 bytes 08813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e1ab623c6ef714ffc8875e653c1bd77"></a>

### [`00587f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f24.md) → [`00588244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588244.md) FUN_00588244

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588254",
      "incomplete_value": false,
      "site": "0058825c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587f34",
      "incomplete_value": false,
      "site": "00587f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "0058825c",
      "DATA",
      [
        "storage",
        "00c6cc90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058825c",
      "DATA",
      [
        "storage",
        "00c6dc60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f24.md#insn-00587f30) · [`00587f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f24.md#insn-00587f34) · [`00587f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f24.md#insn-00587f40)
- 新版 [`00588250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588244.md#insn-00588250) · [`00588254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588244.md#insn-00588254) · [`00588260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588244.md#insn-00588260)

~~~diff
- 00587f30 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588250 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587f30 bytes 283700b0
+ 00588250 bytes 283700b0
- 00587f34 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00587f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588254 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 00588254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587f34 bytes 08413291
+ 00588254 bytes 08813191
- 00587f40 ["INT_ADD", "register:40f0:8", ["const:587f40:8", "const:4:8"]]
- 00587f40 ["CALL", null, ["callee:00c58f40:8"]]
+ 00588260 ["INT_ADD", "register:40f0:8", ["const:588260:8", "const:4:8"]]
+ 00588260 ["CALL", null, ["callee:00c58f40:8"]]
- 00587f40 bytes 0c401b94
+ 00588260 bytes 38431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0210ff74b6b63d582ea601f8224336d3"></a>

### [`00587f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md) → [`00588274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588274.md) FUN_00588274

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) · 呼出先 2件 [`005870b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0058572c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/0058572c.md) · 呼出先 2件 [`005873d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00587/005873d8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588288",
      "incomplete_value": false,
      "site": "00588290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587f68",
      "incomplete_value": false,
      "site": "00587f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "00588290",
      "DATA",
      [
        "storage",
        "00c6c968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588290",
      "DATA",
      [
        "storage",
        "00c6d938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md#insn-00587f64) · [`00587f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md#insn-00587f68) · [`00587f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md#insn-00587f78)
- 新版 [`00588284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588274.md#insn-00588284) · [`00588288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588274.md#insn-00588288) · [`00588298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588274.md#insn-00588298)

~~~diff
- 00587f64 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588284 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00587f64 bytes 283700b0
+ 00588284 bytes 283700b0
- 00587f68 ["COPY", "tmp:0:8", ["const:968:8"]]
- 00587f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588288 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00588288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587f68 bytes 08a12591
+ 00588288 bytes 08e12491
- 00587f78 ["INT_ADD", "register:40f0:8", ["const:587f78:8", "const:4:8"]]
- 00587f78 ["CALL", null, ["callee:005873d8:8"]]
+ 00588298 ["INT_ADD", "register:40f0:8", ["const:588298:8", "const:4:8"]]
+ 00588298 ["CALL", null, ["callee:005873d8:8"]]
- 00587f78 bytes 50fcff97
+ 00588298 bytes 50fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3340e4adf481099c7ebf1d3d6e92d552"></a>

### [`00587fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md) → [`005882c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005882c4.md) FUN_005882c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0058572c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/0058572c.md) · 呼出先 7件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588374",
      "incomplete_value": false,
      "site": "0058837c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588054",
      "incomplete_value": false,
      "site": "0058805c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "0058837c",
      "DATA",
      [
        "storage",
        "00c6c968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058837c",
      "DATA",
      [
        "storage",
        "00c6d938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md#insn-00587fdc) · [`00588028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md#insn-00588028) · [`00588048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md#insn-00588048)
- 新版 [`005882fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005882c4.md#insn-005882fc) · [`00588348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005882c4.md#insn-00588348) · [`00588368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005882c4.md#insn-00588368)

~~~diff
- 00587fdc ["INT_ADD", "register:40f0:8", ["const:587fdc:8", "const:4:8"]]
- 00587fdc ["CALL", null, ["callee:00c59080:8"]]
+ 005882fc ["INT_ADD", "register:40f0:8", ["const:5882fc:8", "const:4:8"]]
+ 005882fc ["CALL", null, ["callee:00c59080:8"]]
- 00587fdc bytes 35401b94
+ 005882fc bytes 61431b94
- 00588028 ["INT_ADD", "register:40f0:8", ["const:588028:8", "const:4:8"]]
- 00588028 ["CALL", null, ["callee:00c58f30:8"]]
+ 00588348 ["INT_ADD", "register:40f0:8", ["const:588348:8", "const:4:8"]]
+ 00588348 ["CALL", null, ["callee:00c58f30:8"]]
- 00588028 bytes ce3f1b94
+ 00588348 bytes fa421b94
- 00588048 ["INT_ADD", "register:40f0:8", ["const:588048:8", "const:4:8"]]
- 00588048 ["CALL", null, ["callee:00c590a0:8"]]
+ 00588368 ["INT_ADD", "register:40f0:8", ["const:588368:8", "const:4:8"]]
+ 00588368 ["CALL", null, ["callee:00c590a0:8"]]
- 00588048 bytes 22401b94
+ 00588368 bytes 4e431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06a8409019101d68962b3862efa9cb4"></a>

### [`00588394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md) → [`005886b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005886b4.md) FUN_005886b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`00585f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00586c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md)
- 新版 呼出元 2件 [`00585a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md) [`00586270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586270.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00586f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005886cc",
      "incomplete_value": false,
      "site": "005886d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005883ac",
      "incomplete_value": false,
      "site": "005883b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "definition_site": "005886dc",
      "incomplete_value": false,
      "site": "005886e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005883bc",
      "incomplete_value": false,
      "site": "005883c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "005886d0",
      "DATA",
      [
        "storage",
        "00c6cc90",
        null,
        "pointer"
      ]
    ],
    [
      "005886e8",
      "DATA",
      [
        "storage",
        "00c6c968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005886d0",
      "DATA",
      [
        "storage",
        "00c6dc60",
        null,
        "pointer"
      ]
    ],
    [
      "005886e8",
      "DATA",
      [
        "storage",
        "00c6d938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005883a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md#insn-005883a8) · [`005883ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md#insn-005883ac) · [`005883b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md#insn-005883b8)
- 新版 [`005886c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005886b4.md#insn-005886c8) · [`005886cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005886b4.md#insn-005886cc)

~~~diff
- 005883a8 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 005886c8 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 005883a8 bytes 29370090
+ 005886c8 bytes 293700b0
- 005883ac ["COPY", "tmp:0:8", ["const:c90:8"]]
- 005883ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005883ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005883ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005886cc ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 005886cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005886cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005886cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005883ac bytes 29413291
+ 005886cc bytes 29813191
- 005883b8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005883b8 bytes 28370090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88526b5799c6b06b6fb01a5b3447988f"></a>

### [`00588464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588464.md) → [`00588784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588784.md) _INIT_32

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0058335c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058335c.md) [`0058338c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058338c.md) [`005833bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833bc.md) [`005833c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833c4.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0058367c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/0058367c.md) [`005836ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836ac.md) [`005836dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836dc.md) [`005836e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/005836e4.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件, `store_value` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005887ac",
      "incomplete_value": false,
      "site": "005887ac",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:380:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058848c",
      "incomplete_value": false,
      "site": "0058848c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:3c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005887c8",
      "incomplete_value": false,
      "site": "005887c8",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:3b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005884a8",
      "incomplete_value": false,
      "site": "005884a8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005887e8",
      "incomplete_value": false,
      "site": "005887e8",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:3e0:8"
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
      "definition_site": "005884c8",
      "incomplete_value": false,
      "site": "005884c8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:420:8"
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
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058879c",
      "PARAM",
      [
        "storage",
        "00ca63c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00588484",
      "PARAM",
      [
        "storage",
        "0058335c",
        null,
        null
      ]
    ],
    [
      "005887a8",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058879c",
      "PARAM",
      [
        "storage",
        "00ca7380",
        null,
        "undefined8"
      ]
    ],
    [
      "005887a4",
      "PARAM",
      [
        "storage",
        "0058367c",
        null,
        null
      ]
    ],
    [
      "005887a8",
      "PARAM",
      [
        "storage",
        "00c64030",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588464.md#insn-00588490) · [`005884ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588464.md#insn-005884ac) · [`005884d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588464.md#insn-005884d4)

~~~diff
- 00588490 ["INT_ADD", "register:40f0:8", ["const:588490:8", "const:4:8"]]
- 00588490 ["CALL", null, ["callee:00c58ed0:8"]]
- 00588490 bytes 9c3e1b94
- 005884ac ["INT_ADD", "register:40f0:8", ["const:5884ac:8", "const:4:8"]]
- 005884ac ["CALL", null, ["callee:00c58ed0:8"]]
- 005884ac bytes 953e1b94
- 005884d4 ["INT_ADD", "register:40f0:8", ["const:5884d4:8", "const:4:8"]]
- 005884d4 ["CALL", null, ["callee:00c58ed0:8"]]
- 005884d4 bytes 8b3e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9c88a764f7978d75bd877f7e308076"></a>

### [`00588508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md) → [`00588828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588828.md) FUN_00588828

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0059763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059763c.md) · 呼出先 2件 [`00594978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0059795c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059795c.md) · 呼出先 2件 [`00594c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c98.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588860",
      "incomplete_value": false,
      "site": "0058886c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588540",
      "incomplete_value": false,
      "site": "0058854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "0058886c",
      "DATA",
      [
        "storage",
        "00c6cce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058886c",
      "DATA",
      [
        "storage",
        "00c6dcb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md#insn-00588534) · [`0058853c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md#insn-0058853c) · [`00588540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md#insn-00588540)
- 新版 [`00588854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588828.md#insn-00588854) · [`0058885c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588828.md#insn-0058885c) · [`00588860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588828.md#insn-00588860)

~~~diff
- 00588534 ["INT_ADD", "register:40f0:8", ["const:588534:8", "const:4:8"]]
- 00588534 ["CALL", null, ["callee:00c58f30:8"]]
+ 00588854 ["INT_ADD", "register:40f0:8", ["const:588854:8", "const:4:8"]]
+ 00588854 ["CALL", null, ["callee:00c58f30:8"]]
- 00588534 bytes 8b3e1b94
+ 00588854 bytes b7411b94
- 0058853c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058885c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058853c bytes 28370090
+ 0058885c bytes 283700b0
- 00588540 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00588540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588860 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00588860 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588860 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588540 bytes 08813391
+ 00588860 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46730f3f09006dd6eb62309fe1dcb3c1"></a>

### [`0058859c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058859c.md) → [`005888bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888bc.md) FUN_005888bc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "005888c0",
      "incomplete_value": false,
      "site": "005888c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005885a0",
      "incomplete_value": false,
      "site": "005885a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "005888c4",
      "DATA",
      [
        "storage",
        "00c6cce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005888c4",
      "DATA",
      [
        "storage",
        "00c6dcb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058859c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058859c.md#insn-0058859c) · [`005885a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058859c.md#insn-005885a0)
- 新版 [`005888bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888bc.md#insn-005888bc) · [`005888c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888bc.md#insn-005888c0)

~~~diff
- 0058859c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005888bc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058859c bytes 28370090
+ 005888bc bytes 283700b0
- 005885a0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 005885a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005885a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005885a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005888c0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 005888c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005888c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005888c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005885a0 bytes 08813391
+ 005888c0 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273e6ef73c33b595736a55d6012b8fa6"></a>

### [`005885ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885ac.md) → [`005888cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888cc.md) FUN_005888cc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005888dc",
      "incomplete_value": false,
      "site": "005888e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005885bc",
      "incomplete_value": false,
      "site": "005885c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "005888e4",
      "DATA",
      [
        "storage",
        "00c6cce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005888e4",
      "DATA",
      [
        "storage",
        "00c6dcb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005885b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885ac.md#insn-005885b8) · [`005885bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885ac.md#insn-005885bc) · [`005885c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885ac.md#insn-005885c8)
- 新版 [`005888d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888cc.md#insn-005888d8) · [`005888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888cc.md#insn-005888dc) · [`005888e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888cc.md#insn-005888e8)

~~~diff
- 005885b8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005888d8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005885b8 bytes 28370090
+ 005888d8 bytes 283700b0
- 005885bc ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 005885bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005885bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005885bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005888dc ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 005888dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005888dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005888dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005885bc bytes 08813391
+ 005888dc bytes 08c13291
- 005885c8 ["INT_ADD", "register:40f0:8", ["const:5885c8:8", "const:4:8"]]
- 005885c8 ["CALL", null, ["callee:00c58f40:8"]]
+ 005888e8 ["INT_ADD", "register:40f0:8", ["const:5888e8:8", "const:4:8"]]
+ 005888e8 ["CALL", null, ["callee:00c58f40:8"]]
- 005885c8 bytes 6a3e1b94
+ 005888e8 bytes 96411b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d09a2955a963000596e7a66d4d2e16f"></a>

### [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) → [`00588958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588958.md) FUN_00588958

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00588c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md) · 呼出先 7件 [`00588d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md) [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00588f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588f20.md) · 呼出先 7件 [`0058904c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058904c.md) [`0058af84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588988",
      "incomplete_value": false,
      "site": "0058899c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588668",
      "incomplete_value": false,
      "site": "0058867c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "0058899c",
      "DATA",
      [
        "storage",
        "00c6cd30",
        null,
        "undefined *"
      ]
    ],
    [
      "00588a6c",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058899c",
      "DATA",
      [
        "storage",
        "00c6dd00",
        null,
        "undefined *"
      ]
    ],
    [
      "00588a6c",
      "DATA",
      [
        "storage",
        "00c6d300",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md#insn-00588664) · [`00588668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md#insn-00588668) · [`00588698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md#insn-00588698)
- 新版 [`00588984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588958.md#insn-00588984) · [`00588988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588958.md#insn-00588988) · [`005889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588958.md#insn-005889b8)

~~~diff
- 00588664 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588984 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00588664 bytes 28370090
+ 00588984 bytes 283700b0
- 00588668 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00588668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588988 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00588988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588668 bytes 08c13491
+ 00588988 bytes 08013491
- 00588698 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588698 ["INT_ADD", "register:40f0:8", ["const:588698:8", "const:4:8"]]
- 00588698 ["CALLIND", null, ["register:0:8"]]
+ 005889b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005889b8 ["INT_ADD", "register:40f0:8", ["const:5889b8:8", "const:4:8"]]
+ 005889b8 ["CALLIND", null, ["register:0:8"]]
- 00588698 bytes 00013fd6
+ 005889b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f63836df497dd2b275f75b005aae6e84"></a>

### [`00588820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588820.md) → [`00588b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b40.md) FUN_00588b40

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588b54",
      "incomplete_value": false,
      "site": "00588b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588834",
      "incomplete_value": false,
      "site": "00588838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "00588b58",
      "DATA",
      [
        "storage",
        "00c6cd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588b58",
      "DATA",
      [
        "storage",
        "00c6dd00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588820.md#insn-00588830) · [`00588834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588820.md#insn-00588834) · [`00588848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588820.md#insn-00588848)
- 新版 [`00588b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b40.md#insn-00588b50) · [`00588b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b40.md#insn-00588b54) · [`00588b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b40.md#insn-00588b68)

~~~diff
- 00588830 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588b50 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00588830 bytes 28370090
+ 00588b50 bytes 283700b0
- 00588834 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00588834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588b54 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00588b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588834 bytes 08c13491
+ 00588b54 bytes 08013491
- 00588848 ["INT_ADD", "register:40f0:8", ["const:588848:8", "const:4:8"]]
- 00588848 ["CALL", null, ["callee:00c54d90:8"]]
+ 00588b68 ["INT_ADD", "register:40f0:8", ["const:588b68:8", "const:4:8"]]
+ 00588b68 ["CALL", null, ["callee:00c54d90:8"]]
- 00588848 bytes 562d1b94
+ 00588b68 bytes 8a301b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0287c9bd8f2d9c04dc34e62af1b36734"></a>

### [`0058887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058887c.md) → [`00588b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b9c.md) FUN_00588b9c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588bb4",
      "incomplete_value": false,
      "site": "00588bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588894",
      "incomplete_value": false,
      "site": "00588898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00588bb8",
      "DATA",
      [
        "storage",
        "00c6cd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588bb8",
      "DATA",
      [
        "storage",
        "00c6dd00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058887c.md#insn-00588890) · [`00588894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058887c.md#insn-00588894) · [`005888a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058887c.md#insn-005888a8)
- 新版 [`00588bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b9c.md#insn-00588bb0) · [`00588bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b9c.md#insn-00588bb4) · [`00588bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588b9c.md#insn-00588bc8)

~~~diff
- 00588890 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00588bb0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00588890 bytes 28370090
+ 00588bb0 bytes 283700b0
- 00588894 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00588894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588bb4 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00588bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588894 bytes 08c13491
+ 00588bb4 bytes 08013491
- 005888a8 ["INT_ADD", "register:40f0:8", ["const:5888a8:8", "const:4:8"]]
- 005888a8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00588bc8 ["INT_ADD", "register:40f0:8", ["const:588bc8:8", "const:4:8"]]
+ 00588bc8 ["CALL", null, ["callee:00c54d90:8"]]
- 005888a8 bytes 3e2d1b94
+ 00588bc8 bytes 72301b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa006944cd5cdca6171e05b858eb50ab"></a>

### [`00588c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md) → [`00588f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588f20.md) FUN_00588f20

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00588b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588b38.md) [`00597644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597644.md) · 呼出先 6件 [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) [`0059763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059763c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00588e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588e58.md) [`00597964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597964.md) · 呼出先 6件 [`00588958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588958.md) [`0059795c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059795c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00588f70",
      "incomplete_value": false,
      "site": "00588f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588c50",
      "incomplete_value": false,
      "site": "00588c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "00588f7c",
      "DATA",
      [
        "storage",
        "00c6ba10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588f7c",
      "DATA",
      [
        "storage",
        "00c6c9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md#insn-00588c34) · [`00588c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md#insn-00588c44) · [`00588c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md#insn-00588c4c)
- 新版 [`00588f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588f20.md#insn-00588f54) · [`00588f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588f20.md#insn-00588f64) · [`00588f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588f20.md#insn-00588f6c)

~~~diff
- 00588c34 ["INT_ADD", "register:40f0:8", ["const:588c34:8", "const:4:8"]]
- 00588c34 ["CALL", null, ["callee:0059795c:8"]]
+ 00588f54 ["INT_ADD", "register:40f0:8", ["const:588f54:8", "const:4:8"]]
+ 00588f54 ["CALL", null, ["callee:0059795c:8"]]
- 00588c34 bytes 823a0094
+ 00588f54 bytes 823a0094
- 00588c44 ["INT_ADD", "register:40f0:8", ["const:588c44:8", "const:4:8"]]
- 00588c44 ["CALL", null, ["callee:00c58f30:8"]]
+ 00588f64 ["INT_ADD", "register:40f0:8", ["const:588f64:8", "const:4:8"]]
+ 00588f64 ["CALL", null, ["callee:00c58f30:8"]]
- 00588c44 bytes c73c1b94
+ 00588f64 bytes f33f1b94
- 00588c4c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00588f6c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00588c4c bytes 083700f0
+ 00588f6c bytes 28370090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d1e590bbb2b593612ee0a7d4fa912e1"></a>

### [`00588e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md) → [`00589158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589158.md) FUN_00589158

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043af64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af64.md) · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 1件 [`0043b284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b284.md) · 呼出先 3件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 72.41% / 新版 72.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058916c",
      "incomplete_value": false,
      "site": "00589170",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588e4c",
      "incomplete_value": false,
      "site": "00588e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "00589198",
      "incomplete_value": true,
      "site": "00589198",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "00588e78",
      "incomplete_value": true,
      "site": "00588e78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
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
      "definition_site": "00589188",
      "incomplete_value": true,
      "site": "00589198",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca7000:8"
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
    "old": {
      "definition_site": "00588e68",
      "incomplete_value": true,
      "site": "00588e78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058916c",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00589188",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "005891a4",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058916c",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "00589188",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "005891a4",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md#insn-00588e50) · [`00588e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md#insn-00588e78) · [`00588e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md#insn-00588e88)
- 新版 [`00589170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589158.md#insn-00589170) · [`00589198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589158.md#insn-00589198) · [`005891a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589158.md#insn-005891a8)

~~~diff
- 00588e50 ["INT_ADD", "register:40f0:8", ["const:588e50:8", "const:4:8"]]
- 00588e50 ["CALL", null, ["callee:00c5b390:8"]]
+ 00589170 ["INT_ADD", "register:40f0:8", ["const:589170:8", "const:4:8"]]
+ 00589170 ["CALL", null, ["callee:00c5b390:8"]]
- 00588e50 bytes 5c451b94
+ 00589170 bytes 88481b94
- 00588e78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588e78 ["INT_ADD", "register:40f0:8", ["const:588e78:8", "const:4:8"]]
- 00588e78 ["CALLIND", null, ["register:0:8"]]
+ 00589198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589198 ["INT_ADD", "register:40f0:8", ["const:589198:8", "const:4:8"]]
+ 00589198 ["CALLIND", null, ["register:0:8"]]
- 00588e78 bytes 00013fd6
+ 00589198 bytes 00013fd6
- 00588e88 ["INT_ADD", "register:40f0:8", ["const:588e88:8", "const:4:8"]]
- 00588e88 ["CALL", null, ["callee:00c591e0:8"]]
+ 005891a8 ["INT_ADD", "register:40f0:8", ["const:5891a8:8", "const:4:8"]]
+ 005891a8 ["CALL", null, ["callee:00c591e0:8"]]
- 00588e88 bytes e23c1b94
+ 005891a8 bytes 0e401b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c3dbfbf1b775600eec24e3703216c42"></a>

### [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) → [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) FUN_005891cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 138件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) · 呼出先 2件 [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 138件 [`00497a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md) [`00497c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md) [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00571b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md) [`00571ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571ccc.md) · 呼出先 2件 [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005891dc",
      "incomplete_value": false,
      "site": "005891e0",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588ebc",
      "incomplete_value": false,
      "site": "00588ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "00589208",
      "incomplete_value": true,
      "site": "00589208",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "00588ee8",
      "incomplete_value": true,
      "site": "00588ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
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
      "definition_site": "005891fc",
      "incomplete_value": true,
      "site": "00589208",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca7000:8"
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
    "old": {
      "definition_site": "00588edc",
      "incomplete_value": true,
      "site": "00588ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005891dc",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "005891fc",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "00589214",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005891dc",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "005891fc",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "00589214",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md#insn-00588ec0) · [`00588ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md#insn-00588ee8) · [`00588ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md#insn-00588ef8)
- 新版 [`005891e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md#insn-005891e0) · [`00589208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md#insn-00589208) · [`00589218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md#insn-00589218)

~~~diff
- 00588ec0 ["INT_ADD", "register:40f0:8", ["const:588ec0:8", "const:4:8"]]
- 00588ec0 ["CALL", null, ["callee:00c5b390:8"]]
+ 005891e0 ["INT_ADD", "register:40f0:8", ["const:5891e0:8", "const:4:8"]]
+ 005891e0 ["CALL", null, ["callee:00c5b390:8"]]
- 00588ec0 bytes 40451b94
+ 005891e0 bytes 6c481b94
- 00588ee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588ee8 ["INT_ADD", "register:40f0:8", ["const:588ee8:8", "const:4:8"]]
- 00588ee8 ["CALLIND", null, ["register:0:8"]]
+ 00589208 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589208 ["INT_ADD", "register:40f0:8", ["const:589208:8", "const:4:8"]]
+ 00589208 ["CALLIND", null, ["register:0:8"]]
- 00588ee8 bytes 00013fd6
+ 00589208 bytes 00013fd6
- 00588ef8 ["INT_ADD", "register:40f0:8", ["const:588ef8:8", "const:4:8"]]
- 00588ef8 ["CALL", null, ["callee:00c591e0:8"]]
+ 00589218 ["INT_ADD", "register:40f0:8", ["const:589218:8", "const:4:8"]]
+ 00589218 ["CALL", null, ["callee:00c591e0:8"]]
- 00588ef8 bytes c63c1b94
+ 00589218 bytes f23f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d23994d8e54e17da2e0424d6f07c268"></a>

### [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) → [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) FUN_0058922c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00588e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md) [`005897d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md) [`00589834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md) [`005898a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005898a0.md) [`0058a2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md) · 呼出先 3件 [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 11件 [`00589158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589158.md) [`00589af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589af0.md) [`00589b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589b54.md) [`00589bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bc0.md) [`0058a614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a614.md) · 呼出先 3件 [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md) [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00589258",
      "incomplete_value": false,
      "site": "0058925c",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588f38",
      "incomplete_value": false,
      "site": "00588f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "00589284",
      "incomplete_value": true,
      "site": "00589284",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "00588f64",
      "incomplete_value": true,
      "site": "00588f64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
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
      "definition_site": "00589274",
      "incomplete_value": true,
      "site": "00589284",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca7000:8"
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
    "old": {
      "definition_site": "00588f54",
      "incomplete_value": true,
      "site": "00588f64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00589258",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00589274",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "00589290",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589258",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "00589274",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "00589290",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md#insn-00588f3c) · [`00588f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md#insn-00588f64) · [`00588f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md#insn-00588f74)
- 新版 [`0058925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md#insn-0058925c) · [`00589284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md#insn-00589284) · [`00589294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md#insn-00589294)

~~~diff
- 00588f3c ["INT_ADD", "register:40f0:8", ["const:588f3c:8", "const:4:8"]]
- 00588f3c ["CALL", null, ["callee:00c5b390:8"]]
+ 0058925c ["INT_ADD", "register:40f0:8", ["const:58925c:8", "const:4:8"]]
+ 0058925c ["CALL", null, ["callee:00c5b390:8"]]
- 00588f3c bytes 21451b94
+ 0058925c bytes 4d481b94
- 00588f64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588f64 ["INT_ADD", "register:40f0:8", ["const:588f64:8", "const:4:8"]]
- 00588f64 ["CALLIND", null, ["register:0:8"]]
+ 00589284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589284 ["INT_ADD", "register:40f0:8", ["const:589284:8", "const:4:8"]]
+ 00589284 ["CALLIND", null, ["register:0:8"]]
- 00588f64 bytes 00013fd6
+ 00589284 bytes 00013fd6
- 00588f74 ["INT_ADD", "register:40f0:8", ["const:588f74:8", "const:4:8"]]
- 00588f74 ["CALL", null, ["callee:00c591e0:8"]]
+ 00589294 ["INT_ADD", "register:40f0:8", ["const:589294:8", "const:4:8"]]
+ 00589294 ["CALL", null, ["callee:00c591e0:8"]]
- 00588f74 bytes a73c1b94
+ 00589294 bytes d33f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072dded3f34ee667f4bb6bd7c4e74934"></a>

### [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) → [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) FUN_005894bc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 122件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) · 呼出先 0件 
- 新版 呼出元 122件 [`00497a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md) [`00497c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md) [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00571b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md) [`00571ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571ccc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "005894c0",
      "incomplete_value": false,
      "site": "005894c4",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005891a0",
      "incomplete_value": false,
      "site": "005891a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "005894c0",
      "DATA",
      [
        "storage",
        "00ca6458",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005894c0",
      "DATA",
      [
        "storage",
        "00ca7418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md#insn-0058919c) · [`005891a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md#insn-005891a0)
- 新版 [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md#insn-005894bc) · [`005894c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md#insn-005894c0)

~~~diff
- 0058919c ["COPY", "register:4000:8", ["const:ca6000:8"]]
+ 005894bc ["COPY", "register:4000:8", ["const:ca7000:8"]]
- 0058919c bytes e03800b0
+ 005894bc bytes e03800d0
- 005891a0 ["COPY", "tmp:0:8", ["const:458:8"]]
- 005891a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005891a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005891a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005894c0 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 005894c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005894c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005894c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005891a0 bytes 00601191
+ 005894c0 bytes 00601091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d3585b5d3553c014f61504f3d1eca2d"></a>

### [`005891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891a8.md) → [`005894c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894c8.md) FUN_005894c8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058d4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d4d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005894d4",
      "incomplete_value": false,
      "site": "005894d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005891b4",
      "incomplete_value": false,
      "site": "005891b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "005894d4",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005894d4",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891a8.md#insn-005891a8) · [`005891ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891a8.md#insn-005891ac)
- 新版 [`005894c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894c8.md#insn-005894c8) · [`005894cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894c8.md#insn-005894cc)

~~~diff
- 005891a8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005894c8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005891a8 bytes 083700f0
+ 005894c8 bytes 28370090
- 005891ac ["COPY", "tmp:0:8", ["const:db8:8"]]
- 005891ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005891ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005891ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005894cc ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 005894cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005894cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005894cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005891ac bytes 08e13691
+ 005894cc bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b9fff10a5acfd9040547ecd7309828"></a>

### [`005891d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md) → [`005894f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894f0.md) FUN_005894f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md) · 呼出先 4件 [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0058a5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a5c0.md) · 呼出先 4件 [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589520",
      "incomplete_value": false,
      "site": "00589520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589200",
      "incomplete_value": false,
      "site": "00589200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "00589520",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589520",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ],
    [
      "00589594",
      "DATA",
      [
        "storage",
        "00562928",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005891f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md#insn-005891f8) · [`005891fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md#insn-005891fc) · [`00589224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md#insn-00589224)
- 新版 [`00589518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894f0.md#insn-00589518) · [`0058951c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894f0.md#insn-0058951c) · [`00589544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894f0.md#insn-00589544)

~~~diff
- 005891f8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00589518 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005891f8 bytes 083700f0
+ 00589518 bytes 28370090
- 005891fc ["COPY", "tmp:0:8", ["const:db8:8"]]
- 005891fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005891fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005891fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058951c ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0058951c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058951c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058951c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005891fc bytes 08e13691
+ 0058951c bytes 08213691
- 00589224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589224 ["INT_ADD", "register:40f0:8", ["const:589224:8", "const:4:8"]]
- 00589224 ["CALLIND", null, ["register:0:8"]]
+ 00589544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589544 ["INT_ADD", "register:40f0:8", ["const:589544:8", "const:4:8"]]
+ 00589544 ["CALLIND", null, ["register:0:8"]]
- 00589224 bytes 00013fd6
+ 00589544 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d22dd3d7f7e2f04722341e459706924"></a>

### [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) → [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) FUN_00589680

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 130件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0058a9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md) [`0058ab14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 130件 [`00497a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md) [`00497c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md) [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00571b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b60.md) [`00571ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571ccc.md) · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0058ad0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ad0c.md) [`0058ae34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ae34.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00589770",
      "incomplete_value": false,
      "site": "00589774",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589450",
      "incomplete_value": false,
      "site": "00589454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "00589794",
      "incomplete_value": false,
      "site": "00589798",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589474",
      "incomplete_value": false,
      "site": "00589478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005897c0",
      "incomplete_value": true,
      "site": "005897c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "005894a0",
      "incomplete_value": true,
      "site": "005894a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00589770",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00589794",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "005897ac",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589770",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "00589794",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "005897ac",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md#insn-00589454) · [`00589478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md#insn-00589478) · [`005894a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md#insn-005894a0)
- 新版 [`00589774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md#insn-00589774) · [`00589798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md#insn-00589798) · [`005897c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md#insn-005897c0)

~~~diff
- 00589454 ["INT_ADD", "register:40f0:8", ["const:589454:8", "const:4:8"]]
- 00589454 ["CALL", null, ["callee:00c5b390:8"]]
+ 00589774 ["INT_ADD", "register:40f0:8", ["const:589774:8", "const:4:8"]]
+ 00589774 ["CALL", null, ["callee:00c5b390:8"]]
- 00589454 bytes db431b94
+ 00589774 bytes 07471b94
- 00589478 ["INT_ADD", "register:40f0:8", ["const:589478:8", "const:4:8"]]
- 00589478 ["CALL", null, ["callee:00c5b390:8"]]
+ 00589798 ["INT_ADD", "register:40f0:8", ["const:589798:8", "const:4:8"]]
+ 00589798 ["CALL", null, ["callee:00c5b390:8"]]
- 00589478 bytes d2431b94
+ 00589798 bytes fe461b94
- 005894a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005894a0 ["INT_ADD", "register:40f0:8", ["const:5894a0:8", "const:4:8"]]
- 005894a0 ["CALLIND", null, ["register:0:8"]]
+ 005897c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005897c0 ["INT_ADD", "register:40f0:8", ["const:5897c0:8", "const:4:8"]]
+ 005897c0 ["CALLIND", null, ["register:0:8"]]
- 005894a0 bytes 00013fd6
+ 005897c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f88eec1b06291b4b76a1e11eced2db2"></a>

### [`005897d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md) → [`00589af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589af0.md) FUN_00589af0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0057e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md) [`0057e874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md) [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)
- 新版 呼出元 3件 [`0057e83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e83c.md) [`0057eb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eb94.md) [`0058231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md) · 呼出先 1件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589b08",
      "incomplete_value": false,
      "site": "00589b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005897e8",
      "incomplete_value": false,
      "site": "005897e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00589b08",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589b08",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005897dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md#insn-005897dc) · [`005897e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md#insn-005897e0) · [`005897e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md#insn-005897e4)
- 新版 [`00589afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589af0.md#insn-00589afc) · [`00589b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589af0.md#insn-00589b00)

~~~diff
- 005897dc ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00589afc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005897dc bytes 083700f0
+ 00589afc bytes 28370090
- 005897e0 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 005897e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005897e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005897e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589b00 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00589b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005897e0 bytes 08e13691
+ 00589b00 bytes 08213691
- 005897e4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005897e4 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c108938b7763bc0720c679821501bc"></a>

### [`00589834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md) → [`00589b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589b54.md) FUN_00589b54

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589b68",
      "incomplete_value": false,
      "site": "00589b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589848",
      "incomplete_value": false,
      "site": "0058984c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "00589b6c",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589b6c",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md#insn-00589844) · [`00589848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md#insn-00589848) · [`0058985c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md#insn-0058985c)
- 新版 [`00589b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589b54.md#insn-00589b64) · [`00589b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589b54.md#insn-00589b68) · [`00589b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589b54.md#insn-00589b7c)

~~~diff
- 00589844 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00589b64 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00589844 bytes 083700f0
+ 00589b64 bytes 28370090
- 00589848 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00589848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589b68 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00589b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589848 bytes 08e13691
+ 00589b68 bytes 08213691
- 0058985c ["INT_ADD", "register:40f0:8", ["const:58985c:8", "const:4:8"]]
- 0058985c ["CALL", null, ["callee:0058922c:8"]]
+ 00589b7c ["INT_ADD", "register:40f0:8", ["const:589b7c:8", "const:4:8"]]
+ 00589b7c ["CALL", null, ["callee:0058922c:8"]]
- 0058985c bytes acfdff97
+ 00589b7c bytes acfdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-814c0525be2c0dc06bd58073f98ff615"></a>

### [`00589910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589910.md) → [`00589c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589c30.md) FUN_00589c30

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 55件 [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) [`00571e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571e58.md) [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) · 呼出先 0件 
- 新版 呼出元 55件 [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00571e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571e54.md) [`00572178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572178.md) [`00572458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md) [`0057260c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589c64",
      "incomplete_value": false,
      "site": "00589c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589944",
      "incomplete_value": false,
      "site": "00589944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "00589c64",
      "DATA",
      [
        "storage",
        "00c6cdd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589c64",
      "DATA",
      [
        "storage",
        "00c6dda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589910.md#insn-0058993c) · [`00589940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589910.md#insn-00589940) · [`00589964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589910.md#insn-00589964)
- 新版 [`00589c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589c30.md#insn-00589c5c) · [`00589c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589c30.md#insn-00589c60) · [`00589c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589c30.md#insn-00589c84)

~~~diff
- 0058993c ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00589c5c ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058993c bytes 093700f0
+ 00589c5c bytes 29370090
- 00589940 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00589940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00589940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00589940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589c60 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00589c60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589c60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589c60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00589940 bytes 29613791
+ 00589c60 bytes 29a13691
- 00589964 ["COPY", "register:0:8", ["register:4048:8"]]
- 00589964 ["INT_ADD", "register:40f0:8", ["const:589964:8", "const:4:8"]]
- 00589964 ["CALLIND", null, ["register:0:8"]]
+ 00589c84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00589c84 ["INT_ADD", "register:40f0:8", ["const:589c84:8", "const:4:8"]]
+ 00589c84 ["CALLIND", null, ["register:0:8"]]
- 00589964 bytes 20013fd6
+ 00589c84 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd1161f596e8a502a716b3149cad9e2c"></a>

### [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) → [`00589f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md) FUN_00589f48

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005808c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md) [`00582218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md) [`005823a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md) [`00582534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md) [`005826b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md) · 呼出先 0件 
- 新版 呼出元 7件 [`00580be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580be8.md) [`00582538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582538.md) [`005826c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005826c0.md) [`00582854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582854.md) [`005829d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005829d0.md) · 呼出先 0件 

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
      "definition_site": "00589f68",
      "incomplete_value": false,
      "site": "00589f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589c48",
      "incomplete_value": false,
      "site": "00589c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "00589f68",
      "DATA",
      [
        "storage",
        "00c6cdf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589f68",
      "DATA",
      [
        "storage",
        "00c6ddc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md#insn-00589c40) · [`00589c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md#insn-00589c44) · [`00589c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md#insn-00589c68)
- 新版 [`00589f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md#insn-00589f60) · [`00589f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md#insn-00589f64) · [`00589f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md#insn-00589f88)

~~~diff
- 00589c40 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00589f60 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00589c40 bytes 083700f0
+ 00589f60 bytes 28370090
- 00589c44 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00589c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589f64 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00589f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589c44 bytes 08e13791
+ 00589f64 bytes 08213791
- 00589c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589c68 ["INT_ADD", "register:40f0:8", ["const:589c68:8", "const:4:8"]]
- 00589c68 ["CALLIND", null, ["register:0:8"]]
+ 00589f88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589f88 ["INT_ADD", "register:40f0:8", ["const:589f88:8", "const:4:8"]]
+ 00589f88 ["CALLIND", null, ["register:0:8"]]
- 00589c68 bytes 00013fd6
+ 00589f88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96581bf36369840ba978155f4bb80a3b"></a>

### [`00589cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589cc4.md) → [`00589fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589fe4.md) FUN_00589fe4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005800d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005803f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803f8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00589ff8",
      "incomplete_value": false,
      "site": "0058a000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589cd8",
      "incomplete_value": false,
      "site": "00589ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "0058a000",
      "DATA",
      [
        "storage",
        "00c6cdf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058a000",
      "DATA",
      [
        "storage",
        "00c6ddc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589cc4.md#insn-00589cd4) · [`00589cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589cc4.md#insn-00589cd8) · [`00589cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589cc4.md#insn-00589cf4)
- 新版 [`00589ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589fe4.md#insn-00589ff4) · [`00589ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589fe4.md#insn-00589ff8) · [`0058a014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589fe4.md#insn-0058a014)

~~~diff
- 00589cd4 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00589ff4 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00589cd4 bytes 093700f0
+ 00589ff4 bytes 29370090
- 00589cd8 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00589cd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00589cd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00589cd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589ff8 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00589ff8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589ff8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589ff8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00589cd8 bytes 29e13791
+ 00589ff8 bytes 29213791
- 00589cf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589cf4 ["INT_ADD", "register:40f0:8", ["const:589cf4:8", "const:4:8"]]
- 00589cf4 ["CALLIND", null, ["register:0:8"]]
+ 0058a014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a014 ["INT_ADD", "register:40f0:8", ["const:58a014:8", "const:4:8"]]
+ 0058a014 ["CALLIND", null, ["register:0:8"]]
- 00589cf4 bytes 00013fd6
+ 0058a014 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c987d75cf411113b1440f31b043aa281"></a>

### [`00589d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md) → [`0058a028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a028.md) FUN_0058a028

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00582218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00582538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582538.md) · 呼出先 0件 

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
      "definition_site": "0058a044",
      "incomplete_value": false,
      "site": "0058a044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589d24",
      "incomplete_value": false,
      "site": "00589d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "0058a044",
      "DATA",
      [
        "storage",
        "00c6cdf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058a044",
      "DATA",
      [
        "storage",
        "00c6ddc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md#insn-00589d18) · [`00589d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md#insn-00589d1c) · [`00589d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md#insn-00589d54)
- 新版 [`0058a038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a028.md#insn-0058a038) · [`0058a03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a028.md#insn-0058a03c) · [`0058a074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a028.md#insn-0058a074)

~~~diff
- 00589d18 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058a038 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00589d18 bytes 083700f0
+ 0058a038 bytes 083700f0
- 00589d1c ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00589d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a03c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 0058a03c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a03c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a03c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589d1c bytes 08e13791
+ 0058a03c bytes 08213791
- 00589d54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589d54 ["INT_ADD", "register:40f0:8", ["const:589d54:8", "const:4:8"]]
- 00589d54 ["CALLIND", null, ["register:0:8"]]
+ 0058a074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a074 ["INT_ADD", "register:40f0:8", ["const:58a074:8", "const:4:8"]]
+ 0058a074 ["CALLIND", null, ["register:0:8"]]
- 00589d54 bytes 00013fd6
+ 0058a074 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11441df7338462e036717d85fe7f78a4"></a>

### [`0058a088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a088.md) → [`0058a3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a3a8.md) FUN_0058a3a8

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00589f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589f48.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a268.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "0058a3b8",
      "value": [
        "leaf",
        "ram:58a268:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0058a098",
      "value": [
        "leaf",
        "ram:589f48:8"
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
      "0058a3b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ],
  "added": [
    [
      "0058a3b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058a268"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a088.md#insn-0058a098)
- 新版 [`0058a3b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a3a8.md#insn-0058a3b8)

~~~diff
- 0058a098 ["INT_ADD", "register:40f0:8", ["const:58a098:8", "const:4:8"]]
- 0058a098 ["CALL", null, ["ram:589f48:8"]]
+ 0058a3b8 ["INT_ADD", "register:40f0:8", ["const:58a3b8:8", "const:4:8"]]
+ 0058a3b8 ["CALL", null, ["ram:58a268:8"]]
- 0058a098 bytes acffff97
+ 0058a3b8 bytes acffff97
~~~


<a id="compare-6dc67b746bf971f9b748bd984dcfb15c"></a>

### [`0058a0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a0ac.md) → [`0058a3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a3cc.md) FUN_0058a3cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a3e0",
      "incomplete_value": false,
      "site": "0058a3e4",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a0c0",
      "incomplete_value": false,
      "site": "0058a0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "0058a40c",
      "incomplete_value": true,
      "site": "0058a40c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "0058a0ec",
      "incomplete_value": true,
      "site": "0058a0ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
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
      "definition_site": "0058a400",
      "incomplete_value": true,
      "site": "0058a40c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca7000:8"
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
    "old": {
      "definition_site": "0058a0e0",
      "incomplete_value": true,
      "site": "0058a0ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058a3e0",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058a400",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a418",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a3e0",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "0058a400",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a418",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a0ac.md#insn-0058a0c4) · [`0058a0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a0ac.md#insn-0058a0ec) · [`0058a0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a0ac.md#insn-0058a0fc)
- 新版 [`0058a3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a3cc.md#insn-0058a3e4) · [`0058a40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a3cc.md#insn-0058a40c) · [`0058a41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a3cc.md#insn-0058a41c)

~~~diff
- 0058a0c4 ["INT_ADD", "register:40f0:8", ["const:58a0c4:8", "const:4:8"]]
- 0058a0c4 ["CALL", null, ["callee:00c5b390:8"]]
+ 0058a3e4 ["INT_ADD", "register:40f0:8", ["const:58a3e4:8", "const:4:8"]]
+ 0058a3e4 ["CALL", null, ["callee:00c5b390:8"]]
- 0058a0c4 bytes bf401b94
+ 0058a3e4 bytes eb431b94
- 0058a0ec ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a0ec ["INT_ADD", "register:40f0:8", ["const:58a0ec:8", "const:4:8"]]
- 0058a0ec ["CALLIND", null, ["register:0:8"]]
+ 0058a40c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a40c ["INT_ADD", "register:40f0:8", ["const:58a40c:8", "const:4:8"]]
+ 0058a40c ["CALLIND", null, ["register:0:8"]]
- 0058a0ec bytes 00013fd6
+ 0058a40c bytes 00013fd6
- 0058a0fc ["INT_ADD", "register:40f0:8", ["const:58a0fc:8", "const:4:8"]]
- 0058a0fc ["CALL", null, ["callee:00c591e0:8"]]
+ 0058a41c ["INT_ADD", "register:40f0:8", ["const:58a41c:8", "const:4:8"]]
+ 0058a41c ["CALL", null, ["callee:00c591e0:8"]]
- 0058a0fc bytes 45381b94
+ 0058a41c bytes 713b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce39f173ef09d23246eb36572ab5294"></a>

### [`0058a11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a11c.md) → [`0058a43c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a43c.md) FUN_0058a43c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a450",
      "incomplete_value": false,
      "site": "0058a454",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a130",
      "incomplete_value": false,
      "site": "0058a134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "definition_site": "0058a47c",
      "incomplete_value": true,
      "site": "0058a47c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "0058a15c",
      "incomplete_value": true,
      "site": "0058a15c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
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
      "definition_site": "0058a470",
      "incomplete_value": true,
      "site": "0058a47c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca7000:8"
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
    "old": {
      "definition_site": "0058a150",
      "incomplete_value": true,
      "site": "0058a15c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058a450",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058a470",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a488",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a450",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "0058a470",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a488",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a11c.md#insn-0058a134) · [`0058a15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a11c.md#insn-0058a15c) · [`0058a16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a11c.md#insn-0058a16c)
- 新版 [`0058a454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a43c.md#insn-0058a454) · [`0058a47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a43c.md#insn-0058a47c) · [`0058a48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a43c.md#insn-0058a48c)

~~~diff
- 0058a134 ["INT_ADD", "register:40f0:8", ["const:58a134:8", "const:4:8"]]
- 0058a134 ["CALL", null, ["callee:00c5b390:8"]]
+ 0058a454 ["INT_ADD", "register:40f0:8", ["const:58a454:8", "const:4:8"]]
+ 0058a454 ["CALL", null, ["callee:00c5b390:8"]]
- 0058a134 bytes a3401b94
+ 0058a454 bytes cf431b94
- 0058a15c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a15c ["INT_ADD", "register:40f0:8", ["const:58a15c:8", "const:4:8"]]
- 0058a15c ["CALLIND", null, ["register:0:8"]]
+ 0058a47c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a47c ["INT_ADD", "register:40f0:8", ["const:58a47c:8", "const:4:8"]]
+ 0058a47c ["CALLIND", null, ["register:0:8"]]
- 0058a15c bytes 00013fd6
+ 0058a47c bytes 00013fd6
- 0058a16c ["INT_ADD", "register:40f0:8", ["const:58a16c:8", "const:4:8"]]
- 0058a16c ["CALL", null, ["callee:00c591e0:8"]]
+ 0058a48c ["INT_ADD", "register:40f0:8", ["const:58a48c:8", "const:4:8"]]
+ 0058a48c ["CALL", null, ["callee:00c591e0:8"]]
- 0058a16c bytes 29381b94
+ 0058a48c bytes 553b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b21d44f46552c100e72fb43de008d0df"></a>

### [`0058a18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a18c.md) → [`0058a4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a4ac.md) FUN_0058a4ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.55% / 新版 89.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058a4f4",
      "incomplete_value": true,
      "site": "0058a4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "0058a1d4",
      "incomplete_value": true,
      "site": "0058a1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
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
      "definition_site": "0058a4e4",
      "incomplete_value": true,
      "site": "0058a4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca7000:8"
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
    "old": {
      "definition_site": "0058a1c4",
      "incomplete_value": true,
      "site": "0058a1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a500",
      "incomplete_value": true,
      "site": "0058a504",
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
      "definition_site": "0058a1e0",
      "incomplete_value": true,
      "site": "0058a1e4",
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
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058a4c4",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058a4e4",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a500",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a4c4",
      "PARAM",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "0058a4e4",
      "READ",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a500",
      "READ",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a18c.md#insn-0058a1d4) · [`0058a1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a18c.md#insn-0058a1e4) · [`0058a1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a18c.md#insn-0058a1a0)
- 新版 [`0058a4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a4ac.md#insn-0058a4f4) · [`0058a504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a4ac.md#insn-0058a504) · [`0058a4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a4ac.md#insn-0058a4c0)

~~~diff
- 0058a1d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a1d4 ["INT_ADD", "register:40f0:8", ["const:58a1d4:8", "const:4:8"]]
- 0058a1d4 ["CALLIND", null, ["register:0:8"]]
+ 0058a4f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a4f4 ["INT_ADD", "register:40f0:8", ["const:58a4f4:8", "const:4:8"]]
+ 0058a4f4 ["CALLIND", null, ["register:0:8"]]
- 0058a1d4 bytes 00013fd6
+ 0058a4f4 bytes 00013fd6
- 0058a1e4 ["INT_ADD", "register:40f0:8", ["const:58a1e4:8", "const:4:8"]]
- 0058a1e4 ["CALL", null, ["callee:00c591e0:8"]]
+ 0058a504 ["INT_ADD", "register:40f0:8", ["const:58a504:8", "const:4:8"]]
+ 0058a504 ["CALL", null, ["callee:00c591e0:8"]]
- 0058a1e4 bytes 0b381b94
+ 0058a504 bytes 373b1b94
- 0058a1a0 ["COPY", "register:4000:8", ["const:ca3000:8"]]
+ 0058a4c0 ["COPY", "register:4000:8", ["const:ca4000:8"]]
- 0058a1a0 bytes c03800b0
+ 0058a4c0 bytes c03800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f1eab80425d714b2dffe1a179d05e31"></a>

### [`0058a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md) → [`0058a5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a5c0.md) FUN_0058a5c0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 1件 [`005891d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md)
- 新版 呼出元 2件 [`00583c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md) [`0058450c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md) · 呼出先 1件 [`005894f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a600",
      "incomplete_value": false,
      "site": "0058a604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a2e0",
      "incomplete_value": false,
      "site": "0058a2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "definition_site": "0058a5dc",
      "incomplete_value": false,
      "site": "0058a5e8",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a2bc",
      "incomplete_value": false,
      "site": "0058a2c8",
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
            "const:78a:8"
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
      "0058a5dc",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "0058a604",
      "DATA",
      [
        "storage",
        "00c6ce30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a5dc",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "0058a604",
      "DATA",
      [
        "storage",
        "00c6de00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md#insn-0058a2c8) · [`0058a2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md#insn-0058a2bc) · [`0058a2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md#insn-0058a2d8)
- 新版 [`0058a5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a5c0.md#insn-0058a5e8) · [`0058a5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a5c0.md#insn-0058a5dc) · [`0058a5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a5c0.md#insn-0058a5f8)

~~~diff
- 0058a2c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a2c8 ["INT_ADD", "register:40f0:8", ["const:58a2c8:8", "const:4:8"]]
- 0058a2c8 ["CALLIND", null, ["register:0:8"]]
+ 0058a5e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a5e8 ["INT_ADD", "register:40f0:8", ["const:58a5e8:8", "const:4:8"]]
+ 0058a5e8 ["CALLIND", null, ["register:0:8"]]
- 0058a2c8 bytes 00013fd6
+ 0058a5e8 bytes 00013fd6
- 0058a2bc ["COPY", "tmp:0:8", ["const:78a:8"]]
- 0058a2bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058a2bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058a2bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058a5dc ["COPY", "tmp:0:8", ["const:8e2:8"]]
+ 0058a5dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a5dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a5dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058a2bc bytes 21281e91
+ 0058a5dc bytes 21882391
- 0058a2d8 ["INT_ADD", "register:40f0:8", ["const:58a2d8:8", "const:4:8"]]
- 0058a2d8 ["CALL", null, ["callee:005894f0:8"]]
+ 0058a5f8 ["INT_ADD", "register:40f0:8", ["const:58a5f8:8", "const:4:8"]]
+ 0058a5f8 ["CALL", null, ["callee:005894f0:8"]]
- 0058a2d8 bytes befbff97
+ 0058a5f8 bytes befbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8c82101162ce47d5074044ce55c709"></a>

### [`0058a2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md) → [`0058a614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a614.md) FUN_0058a614

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00583c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md) [`0058450c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md) · 呼出先 7件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.71% / 新版 89.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a67c",
      "incomplete_value": true,
      "site": "0058a684",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a35c",
      "incomplete_value": true,
      "site": "0058a364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be0:8"
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
      "definition_site": "0058a678",
      "incomplete_value": true,
      "site": "0058a688",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a358",
      "incomplete_value": true,
      "site": "0058a368",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a8c:8"
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
      "definition_site": "0058a678",
      "incomplete_value": true,
      "site": "0058a688",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058a358",
      "incomplete_value": true,
      "site": "0058a368",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058a678",
      "READ",
      [
        "storage",
        "002bda8c",
        null,
        "string"
      ]
    ],
    [
      "0058a678",
      "READ",
      [
        "storage",
        "002bda9c",
        null,
        "string"
      ]
    ],
    [
      "0058a67c",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058a660",
      "DATA",
      [
        "storage",
        "00747570",
        null,
        null
      ]
    ],
    [
      "0058a678",
      "READ",
      [
        "storage",
        "002bdb6a",
        null,
        "string"
      ]
    ],
    [
      "0058a678",
      "READ",
      [
        "storage",
        "002bdb7a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md#insn-0058a348) · [`0058a350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md#insn-0058a350) · [`0058a354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md#insn-0058a354)
- 新版 [`0058a668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a614.md#insn-0058a668) · [`0058a670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a614.md#insn-0058a670)

~~~diff
- 0058a348 ["INT_ADD", "register:40f0:8", ["const:58a348:8", "const:4:8"]]
- 0058a348 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058a668 ["INT_ADD", "register:40f0:8", ["const:58a668:8", "const:4:8"]]
+ 0058a668 ["CALL", null, ["callee:00c58f30:8"]]
- 0058a348 bytes 06371b94
+ 0058a668 bytes 323a1b94
- 0058a350 ["COPY", "tmp:0:8", ["const:a8c:8"]]
- 0058a350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a670 ["COPY", "tmp:0:8", ["const:b6a:8"]]
+ 0058a670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a350 bytes 08312a91
+ 0058a670 bytes 08a92d91
- 0058a354 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0058a354 bytes c9e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63745bc6c1c307e85d67548f2c186700"></a>

### [`0058a584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a584.md) → [`0058a8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a8a4.md) FUN_0058a8a4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)
- 新版 呼出元 5件 [`005727c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md) [`0057921c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/0057921c.md) [`0057b4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b4c4.md) [`00583c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583c0c.md) [`0058450c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00584/0058450c.md) · 呼出先 1件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a91c",
      "incomplete_value": false,
      "site": "0058a91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a5fc",
      "incomplete_value": false,
      "site": "0058a5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a954",
      "incomplete_value": false,
      "site": "0058a958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a634",
      "incomplete_value": false,
      "site": "0058a638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058a8c4",
      "incomplete_value": true,
      "site": "0058a8d4",
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
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a5a4",
      "incomplete_value": true,
      "site": "0058a5b4",
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
            "const:a44:8"
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
      "0058a8c4",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "0058a8e4",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a91c",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a8c4",
      "PARAM",
      [
        "storage",
        "002aeb11",
        null,
        "string"
      ]
    ],
    [
      "0058a8e4",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a91c",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a584.md#insn-0058a5b4) · [`0058a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a584.md#insn-0058a5d0) · [`0058a5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a584.md#insn-0058a5a4)
- 新版 [`0058a8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a8a4.md#insn-0058a8d4) · [`0058a8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a8a4.md#insn-0058a8f0) · [`0058a8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a8a4.md#insn-0058a8c4)

~~~diff
- 0058a5b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a5b4 ["INT_ADD", "register:40f0:8", ["const:58a5b4:8", "const:4:8"]]
- 0058a5b4 ["CALLIND", null, ["register:0:8"]]
+ 0058a8d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a8d4 ["INT_ADD", "register:40f0:8", ["const:58a8d4:8", "const:4:8"]]
+ 0058a8d4 ["CALLIND", null, ["register:0:8"]]
- 0058a5b4 bytes 00013fd6
+ 0058a8d4 bytes 00013fd6
- 0058a5d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a5d0 ["INT_ADD", "register:40f0:8", ["const:58a5d0:8", "const:4:8"]]
- 0058a5d0 ["CALLIND", null, ["register:0:8"]]
+ 0058a8f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a8f0 ["INT_ADD", "register:40f0:8", ["const:58a8f0:8", "const:4:8"]]
+ 0058a8f0 ["CALLIND", null, ["register:0:8"]]
- 0058a5d0 bytes 00013fd6
+ 0058a8f0 bytes 00013fd6
- 0058a5a4 ["COPY", "tmp:0:8", ["const:a44:8"]]
- 0058a5a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058a5a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058a5a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058a8c4 ["COPY", "tmp:0:8", ["const:b11:8"]]
+ 0058a8c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a8c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a8c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058a5a4 bytes 21102991
+ 0058a8c4 bytes 21442c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e3bcc7827fcd49d517a0b8505dc84d"></a>

### [`0058a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md) → [`0058a984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a984.md) FUN_0058a984

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)
- 新版 呼出元 3件 [`00572fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md) [`005741e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005741e0.md) [`00574440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574440.md) · 呼出先 1件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a9ac",
      "incomplete_value": true,
      "site": "0058a9ac",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a68c",
      "incomplete_value": true,
      "site": "0058a68c",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a9d4",
      "incomplete_value": false,
      "site": "0058a9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a6b4",
      "incomplete_value": false,
      "site": "0058a6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "0058a9ac",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ],
    [
      "0058a9d8",
      "DATA",
      [
        "storage",
        "00c6ce50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058a9ac",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ],
    [
      "0058a9d8",
      "DATA",
      [
        "storage",
        "00c6de20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md#insn-0058a67c) · [`0058a680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md#insn-0058a680) · [`0058a684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md#insn-0058a684)
- 新版 [`0058a99c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a984.md#insn-0058a99c) · [`0058a9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a984.md#insn-0058a9a0)

~~~diff
- 0058a67c ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 0058a99c ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058a67c bytes 093700d0
+ 0058a99c bytes 093700f0
- 0058a680 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0058a680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058a680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058a680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058a9a0 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0058a9a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a9a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a9a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058a680 bytes 29e13691
+ 0058a9a0 bytes 29213691
- 0058a684 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0058a684 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a79cf0ad3c0ce288fce1d52b1a53eb"></a>

### [`0058a830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a830.md) → [`0058ab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab50.md) JNI_OnLoad

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058914c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058914c.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058946c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058946c.md) [`00c5b3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b3a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ab64",
      "incomplete_value": false,
      "site": "0058ab64",
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
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a844",
      "incomplete_value": false,
      "site": "0058a844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "definition_site": "0058ab6c",
      "incomplete_value": false,
      "site": "0058ab70",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a84c",
      "incomplete_value": false,
      "site": "0058a850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "definition_site": "0058ab60",
      "incomplete_value": false,
      "site": "0058ab70",
      "value": [
        "leaf",
        "const:58946c:8"
      ]
    },
    "old": {
      "definition_site": "0058a840",
      "incomplete_value": false,
      "site": "0058a850",
      "value": [
        "leaf",
        "const:58914c:8"
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
      "0058ab60",
      "PARAM",
      [
        "storage",
        "0058914c",
        null,
        null
      ]
    ],
    [
      "0058ab64",
      "WRITE",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ab6c",
      "PARAM",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ab60",
      "PARAM",
      [
        "storage",
        "0058946c",
        null,
        null
      ]
    ],
    [
      "0058ab64",
      "WRITE",
      [
        "storage",
        "00ca7410",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ab6c",
      "PARAM",
      [
        "storage",
        "00ca7450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a830.md#insn-0058a844) · [`0058a850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a830.md#insn-0058a850) · [`0058a838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a830.md#insn-0058a838)
- 新版 [`0058ab64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab50.md#insn-0058ab64) · [`0058ab70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab50.md#insn-0058ab70) · [`0058ab58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab50.md#insn-0058ab58)

~~~diff
- 0058a844 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
- 0058a844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0058ab64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:410:8"]]
+ 0058ab64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0058a844 bytes 002902f9
+ 0058ab64 bytes 000902f9
- 0058a850 ["INT_ADD", "register:40f0:8", ["const:58a850:8", "const:4:8"]]
- 0058a850 ["CALL", null, ["callee:00c5b3a0:8"]]
+ 0058ab70 ["INT_ADD", "register:40f0:8", ["const:58ab70:8", "const:4:8"]]
+ 0058ab70 ["CALL", null, ["callee:00c5b3a0:8"]]
- 0058a850 bytes e03e1b94
+ 0058ab70 bytes 0c421b94
- 0058a838 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0058ab58 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0058a838 bytes e8380090
+ 0058ab58 bytes e83800b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38614ac8932e92807d2fa2e238d4c0f1"></a>

### [`0058a864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a864.md) → [`0058ab84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab84.md) FUN_0058ab84

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ab98",
      "incomplete_value": false,
      "site": "0058ab9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a878",
      "incomplete_value": false,
      "site": "0058a87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0058ab9c",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058ab9c",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a864.md#insn-0058a874) · [`0058a878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a864.md#insn-0058a878) · [`0058a88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a864.md#insn-0058a88c)
- 新版 [`0058ab94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab84.md#insn-0058ab94) · [`0058ab98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab84.md#insn-0058ab98) · [`0058abac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab84.md#insn-0058abac)

~~~diff
- 0058a874 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058ab94 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058a874 bytes 083700d0
+ 0058ab94 bytes 083700f0
- 0058a878 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0058a878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ab98 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0058ab98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ab98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ab98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a878 bytes 08e13691
+ 0058ab98 bytes 08213691
- 0058a88c ["INT_ADD", "register:40f0:8", ["const:58a88c:8", "const:4:8"]]
- 0058a88c ["CALL", null, ["callee:0058922c:8"]]
+ 0058abac ["INT_ADD", "register:40f0:8", ["const:58abac:8", "const:4:8"]]
+ 0058abac ["CALL", null, ["callee:0058922c:8"]]
- 0058a88c bytes a0f9ff97
+ 0058abac bytes a0f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5aaf29c2c00526fde805aa120f04dba"></a>

### [`0058a8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8b0.md) → [`0058abd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058abd0.md) FUN_0058abd0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058abe4",
      "incomplete_value": false,
      "site": "0058abe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a8c4",
      "incomplete_value": false,
      "site": "0058a8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0058abe8",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058abe8",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8b0.md#insn-0058a8c0) · [`0058a8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8b0.md#insn-0058a8c4) · [`0058a8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8b0.md#insn-0058a8d8)
- 新版 [`0058abe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058abd0.md#insn-0058abe0) · [`0058abe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058abd0.md#insn-0058abe4) · [`0058abf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058abd0.md#insn-0058abf8)

~~~diff
- 0058a8c0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058abe0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058a8c0 bytes 083700d0
+ 0058abe0 bytes 083700f0
- 0058a8c4 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0058a8c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a8c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a8c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058abe4 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0058abe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058abe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058abe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a8c4 bytes 08e13691
+ 0058abe4 bytes 08213691
- 0058a8d8 ["INT_ADD", "register:40f0:8", ["const:58a8d8:8", "const:4:8"]]
- 0058a8d8 ["CALL", null, ["callee:0058922c:8"]]
+ 0058abf8 ["INT_ADD", "register:40f0:8", ["const:58abf8:8", "const:4:8"]]
+ 0058abf8 ["CALL", null, ["callee:0058922c:8"]]
- 0058a8d8 bytes 8df9ff97
+ 0058abf8 bytes 8df9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-216e303452034ceca1341b2558dfaef7"></a>

### [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md) → [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md) FUN_0058ac1c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 65件 [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) [`00571e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571e58.md) [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) · 呼出先 2件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md)
- 新版 呼出元 65件 [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00571e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571e54.md) [`00572178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572178.md) [`00572458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md) [`0057260c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md) · 呼出先 2件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md)

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
      "definition_site": "0058ac30",
      "incomplete_value": false,
      "site": "0058ac34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a910",
      "incomplete_value": false,
      "site": "0058a914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0058ac34",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058ac34",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md#insn-0058a90c) · [`0058a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md#insn-0058a910) · [`0058a924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md#insn-0058a924)
- 新版 [`0058ac2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md#insn-0058ac2c) · [`0058ac30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md#insn-0058ac30) · [`0058ac44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md#insn-0058ac44)

~~~diff
- 0058a90c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058ac2c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058a90c bytes 083700d0
+ 0058ac2c bytes 083700f0
- 0058a910 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0058a910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ac30 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0058ac30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a910 bytes 08e13691
+ 0058ac30 bytes 08213691
- 0058a924 ["INT_ADD", "register:40f0:8", ["const:58a924:8", "const:4:8"]]
- 0058a924 ["CALL", null, ["callee:0058922c:8"]]
+ 0058ac44 ["INT_ADD", "register:40f0:8", ["const:58ac44:8", "const:4:8"]]
+ 0058ac44 ["CALL", null, ["callee:0058922c:8"]]
- 0058a924 bytes 7af9ff97
+ 0058ac44 bytes 7af9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2370b2ab9059051d14a27a96551f644"></a>

### [`0058a940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a940.md) → [`0058ac60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac60.md) FUN_0058ac60

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0058922c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/0058922c.md) [`0058acac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058acac.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ac74",
      "incomplete_value": false,
      "site": "0058ac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a954",
      "incomplete_value": false,
      "site": "0058a958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0058ac78",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058ac78",
      "DATA",
      [
        "storage",
        "00c6dd88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a940.md#insn-0058a950) · [`0058a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a940.md#insn-0058a954) · [`0058a968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a940.md#insn-0058a968)
- 新版 [`0058ac70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac60.md#insn-0058ac70) · [`0058ac74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac60.md#insn-0058ac74) · [`0058ac88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac60.md#insn-0058ac88)

~~~diff
- 0058a950 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058ac70 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058a950 bytes 083700d0
+ 0058ac70 bytes 083700f0
- 0058a954 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0058a954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ac74 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0058ac74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a954 bytes 08e13691
+ 0058ac74 bytes 08213691
- 0058a968 ["INT_ADD", "register:40f0:8", ["const:58a968:8", "const:4:8"]]
- 0058a968 ["CALL", null, ["callee:0058922c:8"]]
+ 0058ac88 ["INT_ADD", "register:40f0:8", ["const:58ac88:8", "const:4:8"]]
+ 0058ac88 ["CALL", null, ["callee:0058922c:8"]]
- 0058a968 bytes 69f9ff97
+ 0058ac88 bytes 69f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e3b3c940251b0bccb7b4df2ad9684e"></a>

### [`0058ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac24.md) → [`0058af44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af44.md) _INIT_33

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058af5c",
      "incomplete_value": false,
      "site": "0058af5c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ac3c",
      "incomplete_value": false,
      "site": "0058ac3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058af5c",
      "incomplete_value": false,
      "site": "0058af5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ac3c",
      "incomplete_value": false,
      "site": "0058ac3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058af5c",
      "incomplete_value": false,
      "site": "0058af5c",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:418:8"
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
      "definition_site": "0058ac3c",
      "incomplete_value": false,
      "site": "0058ac3c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:458:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058af48",
      "PARAM",
      [
        "storage",
        "00ca6458",
        null,
        "undefined8"
      ]
    ],
    [
      "0058af58",
      "PARAM",
      [
        "storage",
        "0058a8fc",
        null,
        null
      ]
    ],
    [
      "0058af5c",
      "WRITE",
      [
        "storage",
        "00ca6458",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058af48",
      "PARAM",
      [
        "storage",
        "00ca7418",
        null,
        "undefined8"
      ]
    ],
    [
      "0058af58",
      "PARAM",
      [
        "storage",
        "0058ac1c",
        null,
        null
      ]
    ],
    [
      "0058af5c",
      "WRITE",
      [
        "storage",
        "00ca7418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac24.md#insn-0058ac24) · [`0058ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac24.md#insn-0058ac28) · [`0058ac2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac24.md#insn-0058ac2c)
- 新版 [`0058af44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af44.md#insn-0058af44) · [`0058af48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af44.md#insn-0058af48) · [`0058af4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af44.md#insn-0058af4c)

~~~diff
- 0058ac24 ["COPY", "register:4008:8", ["const:ca6000:8"]]
+ 0058af44 ["COPY", "register:4008:8", ["const:ca7000:8"]]
- 0058ac24 bytes e1380090
+ 0058af44 bytes e13800b0
- 0058ac28 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0058ac28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058ac28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058ac28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058af48 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0058af48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058af48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058af48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058ac28 bytes 21601191
+ 0058af48 bytes 21601091
- 0058ac2c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058af4c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058ac2c bytes 083700d0
+ 0058af4c bytes 083700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-debcdd3d9264aae4b00a03cee01cc2c5"></a>

### [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) → [`0058af84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md) FUN_0058af84

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`0057cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md) [`0057d4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md) [`0057de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de50.md) [`00580b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md) [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 5件 [`0057d218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d218.md) [`0057d7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d7f4.md) [`0057e170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e170.md) [`00580e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580e90.md) [`00588958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588958.md) · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058afac",
      "incomplete_value": false,
      "site": "0058afb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ac8c",
      "incomplete_value": false,
      "site": "0058ac90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "0058afb0",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058afb0",
      "DATA",
      [
        "storage",
        "00c6deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ac88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md#insn-0058ac88) · [`0058ac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md#insn-0058ac8c) · [`0058aca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md#insn-0058aca4)
- 新版 [`0058afa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md#insn-0058afa8) · [`0058afac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md#insn-0058afac) · [`0058afc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md#insn-0058afc4)

~~~diff
- 0058ac88 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058afa8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058ac88 bytes 083700d0
+ 0058afa8 bytes 083700f0
- 0058ac8c ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 0058ac8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ac8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ac8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058afac ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0058afac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058afac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058afac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ac8c bytes 08813b91
+ 0058afac bytes 08c13a91
- 0058aca4 ["INT_ADD", "register:40f0:8", ["const:58aca4:8", "const:4:8"]]
- 0058aca4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058afc4 ["INT_ADD", "register:40f0:8", ["const:58afc4:8", "const:4:8"]]
+ 0058afc4 ["CALL", null, ["callee:00c58f30:8"]]
- 0058aca4 bytes af341b94
+ 0058afc4 bytes db371b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0f79ab8ec794015f9c27a096574690d"></a>

### [`0058b58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b58c.md) → [`0058b8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8ac.md) FUN_0058b8ac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0058b8b8",
      "incomplete_value": false,
      "site": "0058b8bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b598",
      "incomplete_value": false,
      "site": "0058b59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058b8bc",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b8bc",
      "DATA",
      [
        "storage",
        "00c6deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b58c.md#insn-0058b594) · [`0058b598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b58c.md#insn-0058b598)
- 新版 [`0058b8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8ac.md#insn-0058b8b4) · [`0058b8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8ac.md#insn-0058b8b8)

~~~diff
- 0058b594 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 0058b8b4 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058b594 bytes 093700b0
+ 0058b8b4 bytes 093700d0
- 0058b598 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 0058b598 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b598 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b598 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b8b8 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0058b8b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b8b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b8b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b598 bytes 29813b91
+ 0058b8b8 bytes 29c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-175ba25d411b2921d3b155ad866b132e"></a>

### [`0058b5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5b0.md) → [`0058b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8d0.md) FUN_0058b8d0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0058b8d8",
      "incomplete_value": false,
      "site": "0058b8dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b5b8",
      "incomplete_value": false,
      "site": "0058b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058b8dc",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b8dc",
      "DATA",
      [
        "storage",
        "00c6deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5b0.md#insn-0058b5b4) · [`0058b5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5b0.md#insn-0058b5b8) · [`0058b5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5b0.md#insn-0058b5dc)
- 新版 [`0058b8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8d0.md#insn-0058b8d4) · [`0058b8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8d0.md#insn-0058b8d8) · [`0058b8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b8d0.md#insn-0058b8fc)

~~~diff
- 0058b5b4 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 0058b8d4 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058b5b4 bytes 093700b0
+ 0058b8d4 bytes 093700d0
- 0058b5b8 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 0058b5b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b8d8 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0058b8d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b8d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b8d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b5b8 bytes 29813b91
+ 0058b8d8 bytes 29c13a91
- 0058b5dc ["INT_ADD", "register:40f0:8", ["const:58b5dc:8", "const:4:8"]]
- 0058b5dc ["CALL", null, ["callee:00c58f50:8"]]
+ 0058b8fc ["INT_ADD", "register:40f0:8", ["const:58b8fc:8", "const:4:8"]]
+ 0058b8fc ["CALL", null, ["callee:00c58f50:8"]]
- 0058b5dc bytes 69321b94
+ 0058b8fc bytes 95351b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52c83f19b6b83f3398a04074582a2fb3"></a>

### [`0058b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5f0.md) → [`0058b910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b910.md) FUN_0058b910

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0058b91c",
      "incomplete_value": false,
      "site": "0058b920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b5fc",
      "incomplete_value": false,
      "site": "0058b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0058b920",
      "DATA",
      [
        "storage",
        "00c6cf18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b920",
      "DATA",
      [
        "storage",
        "00c6dee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5f0.md#insn-0058b5f8) · [`0058b5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5f0.md#insn-0058b5fc)
- 新版 [`0058b918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b910.md#insn-0058b918) · [`0058b91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b910.md#insn-0058b91c)

~~~diff
- 0058b5f8 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 0058b918 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058b5f8 bytes 093700b0
+ 0058b918 bytes 093700d0
- 0058b5fc ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0058b5fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b91c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0058b91c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b91c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b91c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b5fc bytes 29613c91
+ 0058b91c bytes 29a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e226ab9c9d32989b8b140c15f22581c6"></a>

### [`0058b614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b614.md) → [`0058b934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b934.md) FUN_0058b934

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0058b93c",
      "incomplete_value": false,
      "site": "0058b940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b61c",
      "incomplete_value": false,
      "site": "0058b620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0058b940",
      "DATA",
      [
        "storage",
        "00c6cf18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b940",
      "DATA",
      [
        "storage",
        "00c6dee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b614.md#insn-0058b618) · [`0058b61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b614.md#insn-0058b61c) · [`0058b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b614.md#insn-0058b640)
- 新版 [`0058b938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b934.md#insn-0058b938) · [`0058b93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b934.md#insn-0058b93c) · [`0058b960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b934.md#insn-0058b960)

~~~diff
- 0058b618 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 0058b938 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058b618 bytes 093700b0
+ 0058b938 bytes 093700d0
- 0058b61c ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0058b61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b93c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0058b93c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b93c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b93c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b61c bytes 29613c91
+ 0058b93c bytes 29a13b91
- 0058b640 ["INT_ADD", "register:40f0:8", ["const:58b640:8", "const:4:8"]]
- 0058b640 ["CALL", null, ["callee:00c58f50:8"]]
+ 0058b960 ["INT_ADD", "register:40f0:8", ["const:58b960:8", "const:4:8"]]
+ 0058b960 ["CALL", null, ["callee:00c58f50:8"]]
- 0058b640 bytes 50321b94
+ 0058b960 bytes 7c351b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d0a7d5528170de52ef4ae25404950eb"></a>

### [`0058b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md) → [`0058b974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b974.md) FUN_0058b974

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0058adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058adac.md) [`0058ae08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md) [`0058af7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058af7c.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 3件 [`0058b0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b0cc.md) [`0058b128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b128.md) [`0058b29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b29c.md) · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b99c",
      "incomplete_value": false,
      "site": "0058b9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b67c",
      "incomplete_value": false,
      "site": "0058b684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "definition_site": "0058b9b0",
      "incomplete_value": false,
      "site": "0058b9b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b690",
      "incomplete_value": false,
      "site": "0058b690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "0058b9a4",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ],
    [
      "0058b9b0",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b9a4",
      "DATA",
      [
        "storage",
        "00c6d300",
        null,
        "pointer"
      ]
    ],
    [
      "0058b9b0",
      "DATA",
      [
        "storage",
        "00c6deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md#insn-0058b674) · [`0058b678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md#insn-0058b678) · [`0058b67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md#insn-0058b67c)
- 新版 [`0058b994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b974.md#insn-0058b994) · [`0058b998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b974.md#insn-0058b998) · [`0058b99c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b974.md#insn-0058b99c)

~~~diff
- 0058b674 ["INT_ADD", "register:40f0:8", ["const:58b674:8", "const:4:8"]]
- 0058b674 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058b994 ["INT_ADD", "register:40f0:8", ["const:58b994:8", "const:4:8"]]
+ 0058b994 ["CALL", null, ["callee:00c58f30:8"]]
- 0058b674 bytes 3b321b94
+ 0058b994 bytes 67351b94
- 0058b678 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058b998 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058b678 bytes 083700b0
+ 0058b998 bytes 083700d0
- 0058b67c ["COPY", "tmp:0:8", ["const:330:8"]]
- 0058b67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b99c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0058b99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b67c bytes 08c10c91
+ 0058b99c bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf727ca756b7fbedd1cdc637e4a04bc"></a>

### [`0058b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md) → [`0058bb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bb54.md) FUN_0058bb54

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0058b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b210.md) [`0058b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b2b4.md) [`0058b428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b428.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 3件 [`0058b530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b530.md) [`0058b5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b5d4.md) [`0058b748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058b748.md) · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bb7c",
      "incomplete_value": false,
      "site": "0058bb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b85c",
      "incomplete_value": false,
      "site": "0058b864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "definition_site": "0058bb90",
      "incomplete_value": false,
      "site": "0058bb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b870",
      "incomplete_value": false,
      "site": "0058b870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0058bb84",
      "DATA",
      [
        "storage",
        "00c6cfb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058bb90",
      "DATA",
      [
        "storage",
        "00c6cf18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058bb84",
      "DATA",
      [
        "storage",
        "00c6df88",
        null,
        "undefined *"
      ]
    ],
    [
      "0058bb90",
      "DATA",
      [
        "storage",
        "00c6dee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md#insn-0058b854) · [`0058b858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md#insn-0058b858) · [`0058b85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md#insn-0058b85c)
- 新版 [`0058bb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bb54.md#insn-0058bb74) · [`0058bb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bb54.md#insn-0058bb78) · [`0058bb7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bb54.md#insn-0058bb7c)

~~~diff
- 0058b854 ["INT_ADD", "register:40f0:8", ["const:58b854:8", "const:4:8"]]
- 0058b854 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058bb74 ["INT_ADD", "register:40f0:8", ["const:58bb74:8", "const:4:8"]]
+ 0058bb74 ["CALL", null, ["callee:00c58f30:8"]]
- 0058b854 bytes c3311b94
+ 0058bb74 bytes ef341b94
- 0058b858 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058bb78 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058b858 bytes 083700b0
+ 0058bb78 bytes 083700d0
- 0058b85c ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0058b85c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b85c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b85c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058bb7c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0058bb7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bb7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bb7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b85c bytes 08e13e91
+ 0058bb7c bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab6b0c12062aee534749583ac73948ff"></a>

### [`0058b90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b90c.md) → [`0058bc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc2c.md) FUN_0058bc2c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "0058bc30",
      "incomplete_value": false,
      "site": "0058bc34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b910",
      "incomplete_value": false,
      "site": "0058b914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "0058bc34",
      "DATA",
      [
        "storage",
        "00c6cfb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058bc34",
      "DATA",
      [
        "storage",
        "00c6df88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b90c.md#insn-0058b90c) · [`0058b910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b90c.md#insn-0058b910)
- 新版 [`0058bc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc2c.md#insn-0058bc2c) · [`0058bc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc2c.md#insn-0058bc30)

~~~diff
- 0058b90c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058bc2c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058b90c bytes 083700b0
+ 0058bc2c bytes 083700d0
- 0058b910 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0058b910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058bc30 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0058bc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b910 bytes 08e13e91
+ 0058bc30 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-063f49c592cb7073680015fdff4ed306"></a>

### [`0058b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b91c.md) → [`0058bc3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc3c.md) FUN_0058bc3c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bc4c",
      "incomplete_value": false,
      "site": "0058bc54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b92c",
      "incomplete_value": false,
      "site": "0058b934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "0058bc54",
      "DATA",
      [
        "storage",
        "00c6cfb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058bc54",
      "DATA",
      [
        "storage",
        "00c6df88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b91c.md#insn-0058b928) · [`0058b92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b91c.md#insn-0058b92c) · [`0058b938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b91c.md#insn-0058b938)
- 新版 [`0058bc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc3c.md#insn-0058bc48) · [`0058bc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc3c.md#insn-0058bc4c) · [`0058bc58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bc3c.md#insn-0058bc58)

~~~diff
- 0058b928 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058bc48 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058b928 bytes 083700b0
+ 0058bc48 bytes 083700d0
- 0058b92c ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0058b92c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b92c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b92c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058bc4c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0058bc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b92c bytes 08e13e91
+ 0058bc4c bytes 08213e91
- 0058b938 ["INT_ADD", "register:40f0:8", ["const:58b938:8", "const:4:8"]]
- 0058b938 ["CALL", null, ["callee:00c58f40:8"]]
+ 0058bc58 ["INT_ADD", "register:40f0:8", ["const:58bc58:8", "const:4:8"]]
+ 0058bc58 ["CALL", null, ["callee:00c58f40:8"]]
- 0058b938 bytes 8e311b94
+ 0058bc58 bytes ba341b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc7ef3455e96502220358c6e5df1ff8e"></a>

### [`0058b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b984.md) → [`0058bca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bca4.md) FUN_0058bca4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597660.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00597980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597980.md) · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bcf8",
      "incomplete_value": true,
      "site": "0058bcf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:11d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b9d8",
      "incomplete_value": true,
      "site": "0058b9d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e:8"
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
      "definition_site": "0058bd00",
      "incomplete_value": true,
      "site": "0058bd00",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058b9e0",
      "incomplete_value": true,
      "site": "0058b9e0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bcfc",
      "incomplete_value": true,
      "site": "0058bd14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b9dc",
      "incomplete_value": true,
      "site": "0058b9f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
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
      "0058bce0",
      "READ",
      [
        "storage",
        "002b904e",
        null,
        "string"
      ]
    ],
    [
      "0058bce8",
      "READ",
      [
        "storage",
        "002b9054",
        null,
        "string"
      ]
    ],
    [
      "0058bcfc",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bce0",
      "READ",
      [
        "storage",
        "002b911d",
        null,
        "string"
      ]
    ],
    [
      "0058bce8",
      "READ",
      [
        "storage",
        "002b9123",
        null,
        "string"
      ]
    ],
    [
      "0058bcfc",
      "READ",
      [
        "storage",
        "002a0fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b984.md#insn-0058b9a8) · [`0058b9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b984.md#insn-0058b9b0) · [`0058b9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b984.md#insn-0058b9bc)
- 新版 [`0058bcc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bca4.md#insn-0058bcc8) · [`0058bcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bca4.md#insn-0058bcd0) · [`0058bcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bca4.md#insn-0058bcdc)

~~~diff
- 0058b9a8 ["INT_ADD", "register:40f0:8", ["const:58b9a8:8", "const:4:8"]]
- 0058b9a8 ["CALL", null, ["callee:005891cc:8"]]
+ 0058bcc8 ["INT_ADD", "register:40f0:8", ["const:58bcc8:8", "const:4:8"]]
+ 0058bcc8 ["CALL", null, ["callee:005891cc:8"]]
- 0058b9a8 bytes 41f5ff97
+ 0058bcc8 bytes 41f5ff97
- 0058b9b0 ["INT_ADD", "register:40f0:8", ["const:58b9b0:8", "const:4:8"]]
- 0058b9b0 ["CALL", null, ["callee:005894bc:8"]]
+ 0058bcd0 ["INT_ADD", "register:40f0:8", ["const:58bcd0:8", "const:4:8"]]
+ 0058bcd0 ["CALL", null, ["callee:005894bc:8"]]
- 0058b9b0 bytes fbf5ff97
+ 0058bcd0 bytes fbf5ff97
- 0058b9bc ["COPY", "tmp:0:8", ["const:4e:8"]]
- 0058b9bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b9bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b9bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058bcdc ["COPY", "tmp:0:8", ["const:11d:8"]]
+ 0058bcdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058bcdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058bcdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b9bc bytes 29390191
+ 0058bcdc bytes 29750491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdc92c8437eaf5e284a866eac1880422"></a>

### [`0058bb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bb1c.md) → [`0058be3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058be3c.md) FUN_0058be3c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597664.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00597984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597984.md) · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058be94",
      "incomplete_value": true,
      "site": "0058be94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f24:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bb74",
      "incomplete_value": true,
      "site": "0058bb74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e46:8"
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
      "definition_site": "0058bea8",
      "incomplete_value": true,
      "site": "0058beb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bb88",
      "incomplete_value": true,
      "site": "0058bb98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
              ]
            ]
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
      "0058be84",
      "READ",
      [
        "storage",
        "002bee46",
        null,
        "string"
      ]
    ],
    [
      "0058bea8",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058be84",
      "READ",
      [
        "storage",
        "002bef24",
        null,
        "string"
      ]
    ],
    [
      "0058bea8",
      "READ",
      [
        "storage",
        "002a0fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bb1c.md#insn-0058bb40) · [`0058bb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bb1c.md#insn-0058bb48) · [`0058bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bb1c.md#insn-0058bb60)
- 新版 [`0058be60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058be3c.md#insn-0058be60) · [`0058be68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058be3c.md#insn-0058be68) · [`0058be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058be3c.md#insn-0058be80)

~~~diff
- 0058bb40 ["INT_ADD", "register:40f0:8", ["const:58bb40:8", "const:4:8"]]
- 0058bb40 ["CALL", null, ["callee:005891cc:8"]]
+ 0058be60 ["INT_ADD", "register:40f0:8", ["const:58be60:8", "const:4:8"]]
+ 0058be60 ["CALL", null, ["callee:005891cc:8"]]
- 0058bb40 bytes dbf4ff97
+ 0058be60 bytes dbf4ff97
- 0058bb48 ["INT_ADD", "register:40f0:8", ["const:58bb48:8", "const:4:8"]]
- 0058bb48 ["CALL", null, ["callee:005894bc:8"]]
+ 0058be68 ["INT_ADD", "register:40f0:8", ["const:58be68:8", "const:4:8"]]
+ 0058be68 ["CALL", null, ["callee:005894bc:8"]]
- 0058bb48 bytes 95f5ff97
+ 0058be68 bytes 95f5ff97
- 0058bb60 ["COPY", "tmp:0:8", ["const:e46:8"]]
- 0058bb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058bb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058bb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058be80 ["COPY", "tmp:0:8", ["const:f24:8"]]
+ 0058be80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058be80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058be80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058bb60 bytes 08193991
+ 0058be80 bytes 08913c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-631bdaed3fb29e1a05162a8c381b22e7"></a>

### [`0058bcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bcb8.md) → [`0058bfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bfd8.md) FUN_0058bfd8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597668.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00597988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597988.md) · 呼出先 11件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c02c",
      "incomplete_value": true,
      "site": "0058c02c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bd0c",
      "incomplete_value": true,
      "site": "0058bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b5:8"
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
      "definition_site": "0058c040",
      "incomplete_value": true,
      "site": "0058c048",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bd20",
      "incomplete_value": true,
      "site": "0058bd28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cc5:8"
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
      "definition_site": "0058c04c",
      "incomplete_value": true,
      "site": "0058c04c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058bd2c",
      "incomplete_value": true,
      "site": "0058bd2c",
      "value": [
        "LOAD",
        "8",
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
      "0058c020",
      "READ",
      [
        "storage",
        "002a43b5",
        null,
        "string"
      ]
    ],
    [
      "0058c040",
      "READ",
      [
        "storage",
        "002b3cc5",
        null,
        "string"
      ]
    ],
    [
      "0058c044",
      "READ",
      [
        "storage",
        "002b3cd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c020",
      "READ",
      [
        "storage",
        "002a4480",
        null,
        "string"
      ]
    ],
    [
      "0058c040",
      "READ",
      [
        "storage",
        "002b3da3",
        null,
        "string"
      ]
    ],
    [
      "0058c044",
      "READ",
      [
        "storage",
        "002b3db0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bcb8.md#insn-0058bcdc) · [`0058bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bcb8.md#insn-0058bce4) · [`0058bcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bcb8.md#insn-0058bcfc)
- 新版 [`0058bffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bfd8.md#insn-0058bffc) · [`0058c004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bfd8.md#insn-0058c004) · [`0058c01c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058b/0058bfd8.md#insn-0058c01c)

~~~diff
- 0058bcdc ["INT_ADD", "register:40f0:8", ["const:58bcdc:8", "const:4:8"]]
- 0058bcdc ["CALL", null, ["callee:005891cc:8"]]
+ 0058bffc ["INT_ADD", "register:40f0:8", ["const:58bffc:8", "const:4:8"]]
+ 0058bffc ["CALL", null, ["callee:005891cc:8"]]
- 0058bcdc bytes 74f4ff97
+ 0058bffc bytes 74f4ff97
- 0058bce4 ["INT_ADD", "register:40f0:8", ["const:58bce4:8", "const:4:8"]]
- 0058bce4 ["CALL", null, ["callee:005894bc:8"]]
+ 0058c004 ["INT_ADD", "register:40f0:8", ["const:58c004:8", "const:4:8"]]
+ 0058c004 ["CALL", null, ["callee:005894bc:8"]]
- 0058bce4 bytes 2ef5ff97
+ 0058c004 bytes 2ef5ff97
- 0058bcfc ["COPY", "tmp:0:8", ["const:3b5:8"]]
- 0058bcfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058bcfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058bcfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058c01c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0058c01c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058c01c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058c01c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058bcfc bytes 08d50e91
+ 0058c01c bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda63ef617398d4a1e30cf146400181d"></a>

### [`0058be7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058be7c.md) → [`0058c19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c19c.md) FUN_0058c19c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597670.md) · 呼出先 9件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00597990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597990.md) · 呼出先 9件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c1e4",
      "incomplete_value": true,
      "site": "0058c1f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058bec4",
      "incomplete_value": true,
      "site": "0058bed0",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c1e0",
      "incomplete_value": true,
      "site": "0058c1f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bec0",
      "incomplete_value": true,
      "site": "0058bed8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f8:8"
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
      "definition_site": "0058c1fc",
      "incomplete_value": true,
      "site": "0058c20c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bedc",
      "incomplete_value": true,
      "site": "0058beec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0058c1e0",
      "READ",
      [
        "storage",
        "002a20f8",
        null,
        "string"
      ]
    ],
    [
      "0058c1e4",
      "READ",
      [
        "storage",
        "002a2108",
        null,
        "string"
      ]
    ],
    [
      "0058c1fc",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058c1e0",
      "READ",
      [
        "storage",
        "002a21c3",
        null,
        "string"
      ]
    ],
    [
      "0058c1e4",
      "READ",
      [
        "storage",
        "002a21d3",
        null,
        "string"
      ]
    ],
    [
      "0058c1fc",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058be9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058be7c.md#insn-0058be9c) · [`0058bea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058be7c.md#insn-0058bea4) · [`0058beb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058be7c.md#insn-0058beb0)
- 新版 [`0058c1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c19c.md#insn-0058c1bc) · [`0058c1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c19c.md#insn-0058c1c4) · [`0058c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c19c.md#insn-0058c1d0)

~~~diff
- 0058be9c ["INT_ADD", "register:40f0:8", ["const:58be9c:8", "const:4:8"]]
- 0058be9c ["CALL", null, ["callee:005891cc:8"]]
+ 0058c1bc ["INT_ADD", "register:40f0:8", ["const:58c1bc:8", "const:4:8"]]
+ 0058c1bc ["CALL", null, ["callee:005891cc:8"]]
- 0058be9c bytes 04f4ff97
+ 0058c1bc bytes 04f4ff97
- 0058bea4 ["INT_ADD", "register:40f0:8", ["const:58bea4:8", "const:4:8"]]
- 0058bea4 ["CALL", null, ["callee:005894bc:8"]]
+ 0058c1c4 ["INT_ADD", "register:40f0:8", ["const:58c1c4:8", "const:4:8"]]
+ 0058c1c4 ["CALL", null, ["callee:005894bc:8"]]
- 0058bea4 bytes bef4ff97
+ 0058c1c4 bytes bef4ff97
- 0058beb0 ["INT_ADD", "register:40f0:8", ["const:58beb0:8", "const:4:8"]]
- 0058beb0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058c1d0 ["INT_ADD", "register:40f0:8", ["const:58c1d0:8", "const:4:8"]]
+ 0058c1d0 ["CALL", null, ["callee:00c58f30:8"]]
- 0058beb0 bytes 2c301b94
+ 0058c1d0 bytes 58331b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff9664ae7283cd1f26e3010b15734c59"></a>

### [`0058c004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c004.md) → [`0058c324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c324.md) FUN_0058c324

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059766c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059766c.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`0059798c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059798c.md) · 呼出先 11件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

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
      "definition_site": "0058c38c",
      "incomplete_value": true,
      "site": "0058c394",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c06c",
      "incomplete_value": true,
      "site": "0058c074",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cc5:8"
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
      "definition_site": "0058c398",
      "incomplete_value": true,
      "site": "0058c398",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058c078",
      "incomplete_value": true,
      "site": "0058c078",
      "value": [
        "LOAD",
        "8",
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
      "0058c38c",
      "READ",
      [
        "storage",
        "002b3cc5",
        null,
        "string"
      ]
    ],
    [
      "0058c390",
      "READ",
      [
        "storage",
        "002b3cd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c38c",
      "READ",
      [
        "storage",
        "002b3da3",
        null,
        "string"
      ]
    ],
    [
      "0058c390",
      "READ",
      [
        "storage",
        "002b3db0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c004.md#insn-0058c028) · [`0058c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c004.md#insn-0058c030) · [`0058c068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c004.md#insn-0058c068)
- 新版 [`0058c348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c324.md#insn-0058c348) · [`0058c350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c324.md#insn-0058c350) · [`0058c388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c324.md#insn-0058c388)

~~~diff
- 0058c028 ["INT_ADD", "register:40f0:8", ["const:58c028:8", "const:4:8"]]
- 0058c028 ["CALL", null, ["callee:005891cc:8"]]
+ 0058c348 ["INT_ADD", "register:40f0:8", ["const:58c348:8", "const:4:8"]]
+ 0058c348 ["CALL", null, ["callee:005891cc:8"]]
- 0058c028 bytes a1f3ff97
+ 0058c348 bytes a1f3ff97
- 0058c030 ["INT_ADD", "register:40f0:8", ["const:58c030:8", "const:4:8"]]
- 0058c030 ["CALL", null, ["callee:005894bc:8"]]
+ 0058c350 ["INT_ADD", "register:40f0:8", ["const:58c350:8", "const:4:8"]]
+ 0058c350 ["CALL", null, ["callee:005894bc:8"]]
- 0058c030 bytes 5bf4ff97
+ 0058c350 bytes 5bf4ff97
- 0058c068 ["COPY", "tmp:0:8", ["const:cc5:8"]]
- 0058c068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058c068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058c068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058c388 ["COPY", "tmp:0:8", ["const:da3:8"]]
+ 0058c388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058c388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058c388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058c068 bytes 08153391
+ 0058c388 bytes 088d3691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946f3d0a1956257dbd34fb07f029b730"></a>

### [`0058c1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c1c8.md) → [`0058c4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c4e8.md) FUN_0058c4e8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597674.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00597994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597994.md) · 呼出先 11件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c524",
      "incomplete_value": true,
      "site": "0058c53c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c204",
      "incomplete_value": true,
      "site": "0058c21c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d19:8"
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
      "definition_site": "0058c540",
      "incomplete_value": true,
      "site": "0058c54c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:56b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c220",
      "incomplete_value": true,
      "site": "0058c22c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48d:8"
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
      "definition_site": "0058c550",
      "incomplete_value": true,
      "site": "0058c550",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058c230",
      "incomplete_value": true,
      "site": "0058c230",
      "value": [
        "LOAD",
        "8",
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
      "0058c524",
      "READ",
      [
        "storage",
        "002b0d19",
        null,
        "string"
      ]
    ],
    [
      "0058c540",
      "READ",
      [
        "storage",
        "002bb48d",
        null,
        "string"
      ]
    ],
    [
      "0058c544",
      "READ",
      [
        "storage",
        "002bb49a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c524",
      "READ",
      [
        "storage",
        "002b0df0",
        null,
        "string"
      ]
    ],
    [
      "0058c540",
      "READ",
      [
        "storage",
        "002bb56b",
        null,
        "string"
      ]
    ],
    [
      "0058c544",
      "READ",
      [
        "storage",
        "002bb578",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c1c8.md#insn-0058c1ec) · [`0058c1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c1c8.md#insn-0058c1f4) · [`0058c200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c1c8.md#insn-0058c200)
- 新版 [`0058c50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c4e8.md#insn-0058c50c) · [`0058c514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c4e8.md#insn-0058c514) · [`0058c520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c4e8.md#insn-0058c520)

~~~diff
- 0058c1ec ["INT_ADD", "register:40f0:8", ["const:58c1ec:8", "const:4:8"]]
- 0058c1ec ["CALL", null, ["callee:005891cc:8"]]
+ 0058c50c ["INT_ADD", "register:40f0:8", ["const:58c50c:8", "const:4:8"]]
+ 0058c50c ["CALL", null, ["callee:005891cc:8"]]
- 0058c1ec bytes 30f3ff97
+ 0058c50c bytes 30f3ff97
- 0058c1f4 ["INT_ADD", "register:40f0:8", ["const:58c1f4:8", "const:4:8"]]
- 0058c1f4 ["CALL", null, ["callee:005894bc:8"]]
+ 0058c514 ["INT_ADD", "register:40f0:8", ["const:58c514:8", "const:4:8"]]
+ 0058c514 ["CALL", null, ["callee:005894bc:8"]]
- 0058c1f4 bytes eaf3ff97
+ 0058c514 bytes eaf3ff97
- 0058c200 ["COPY", "tmp:0:8", ["const:d19:8"]]
- 0058c200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058c200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058c200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058c520 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 0058c520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058c520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058c520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058c200 bytes 29653491
+ 0058c520 bytes 29c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f983509c00e6ef2a05c2fa1cf40a0a46"></a>

### [`0058c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c330.md) → [`0058c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c650.md) FUN_0058c650

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597678.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00597998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597998.md) · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c6a0",
      "incomplete_value": true,
      "site": "0058c6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c380",
      "incomplete_value": true,
      "site": "0058c380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:961:8"
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
      "0058c690",
      "READ",
      [
        "storage",
        "002a7961",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c690",
      "READ",
      [
        "storage",
        "002a7ab9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c330.md#insn-0058c354) · [`0058c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c330.md#insn-0058c35c) · [`0058c368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c330.md#insn-0058c368)
- 新版 [`0058c674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c650.md#insn-0058c674) · [`0058c67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c650.md#insn-0058c67c) · [`0058c688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c650.md#insn-0058c688)

~~~diff
- 0058c354 ["INT_ADD", "register:40f0:8", ["const:58c354:8", "const:4:8"]]
- 0058c354 ["CALL", null, ["callee:005891cc:8"]]
+ 0058c674 ["INT_ADD", "register:40f0:8", ["const:58c674:8", "const:4:8"]]
+ 0058c674 ["CALL", null, ["callee:005891cc:8"]]
- 0058c354 bytes d6f2ff97
+ 0058c674 bytes d6f2ff97
- 0058c35c ["INT_ADD", "register:40f0:8", ["const:58c35c:8", "const:4:8"]]
- 0058c35c ["CALL", null, ["callee:005894bc:8"]]
+ 0058c67c ["INT_ADD", "register:40f0:8", ["const:58c67c:8", "const:4:8"]]
+ 0058c67c ["CALL", null, ["callee:005894bc:8"]]
- 0058c35c bytes 90f3ff97
+ 0058c67c bytes 90f3ff97
- 0058c368 ["COPY", "tmp:0:8", ["const:961:8"]]
- 0058c368 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058c368 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058c368 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058c688 ["COPY", "tmp:0:8", ["const:ab9:8"]]
+ 0058c688 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058c688 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058c688 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058c368 bytes 29852591
+ 0058c688 bytes 29e52a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5efe83d895ef5c0b8f209b72dbc3cedf"></a>

### [`0058c468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md) → [`0058c788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c788.md) FUN_0058c788

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597680.md) · 呼出先 9件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`005979a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979a0.md) · 呼出先 9件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`0057c8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c8fc.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058c7b0",
      "incomplete_value": false,
      "site": "0058c7bc",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c490",
      "incomplete_value": false,
      "site": "0058c49c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "definition_site": "0058c7b8",
      "incomplete_value": true,
      "site": "0058c7bc",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c498",
      "incomplete_value": true,
      "site": "0058c49c",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058c7b0",
      "PARAM",
      [
        "storage",
        "00ca6498",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c7b8",
      "READ",
      [
        "storage",
        "00ca64a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c7c0",
      "WRITE",
      [
        "storage",
        "00ca6498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c7b0",
      "PARAM",
      [
        "storage",
        "00ca7458",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c7b8",
      "READ",
      [
        "storage",
        "00ca7460",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c7c0",
      "WRITE",
      [
        "storage",
        "00ca7458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md#insn-0058c49c) · [`0058c480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md#insn-0058c480) · [`0058c484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md#insn-0058c484)
- 新版 [`0058c7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c788.md#insn-0058c7bc) · [`0058c7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c788.md#insn-0058c7a0) · [`0058c7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c788.md#insn-0058c7a4)

~~~diff
- 0058c49c ["INT_ADD", "register:40f0:8", ["const:58c49c:8", "const:4:8"]]
- 0058c49c ["CALL", null, ["callee:0057c8fc:8"]]
+ 0058c7bc ["INT_ADD", "register:40f0:8", ["const:58c7bc:8", "const:4:8"]]
+ 0058c7bc ["CALL", null, ["callee:0057c8fc:8"]]
- 0058c49c bytes 50c0ff97
+ 0058c7bc bytes 50c0ff97
- 0058c480 ["COPY", "register:4098:8", ["const:ca6000:8"]]
+ 0058c7a0 ["COPY", "register:4098:8", ["const:ca7000:8"]]
- 0058c480 bytes d33800d0
+ 0058c7a0 bytes d33800f0
- 0058c484 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0058c484 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058c484 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058c484 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058c7a4 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0058c7a4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c7a4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c7a4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058c484 bytes 73621291
+ 0058c7a4 bytes 73621191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c682545fdb9440962b71a4fc3605788"></a>

### [`0058c5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c5a4.md) → [`0058c8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c8c4.md) FUN_0058c8c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597684.md) · 呼出先 12件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`005979a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979a4.md) · 呼出先 12件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058c914",
      "incomplete_value": true,
      "site": "0058c914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c5f4",
      "incomplete_value": true,
      "site": "0058c5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40b:8"
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
      "definition_site": "0058c990",
      "incomplete_value": true,
      "site": "0058c990",
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
      "definition_site": "0058c670",
      "incomplete_value": true,
      "site": "0058c670",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0058ca5c",
      "incomplete_value": false,
      "site": "0058ca60",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c73c",
      "incomplete_value": false,
      "site": "0058c740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058c908",
      "READ",
      [
        "storage",
        "002ba40b",
        null,
        "string"
      ]
    ],
    [
      "0058c978",
      "PARAM",
      [
        "storage",
        "00ca64b0",
        null,
        null
      ]
    ],
    [
      "0058c988",
      "READ",
      [
        "storage",
        "00ca64a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c908",
      "READ",
      [
        "storage",
        "002ba4e9",
        null,
        "string"
      ]
    ],
    [
      "0058c978",
      "PARAM",
      [
        "storage",
        "00ca7470",
        null,
        null
      ]
    ],
    [
      "0058c988",
      "READ",
      [
        "storage",
        "00ca7460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c5a4.md#insn-0058c740) · [`0058c5cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c5a4.md#insn-0058c5cc) · [`0058c5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c5a4.md#insn-0058c5d4)
- 新版 [`0058ca60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c8c4.md#insn-0058ca60) · [`0058c8ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c8c4.md#insn-0058c8ec) · [`0058c8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058c8c4.md#insn-0058c8f4)

~~~diff
- 0058c740 ["INT_ADD", "register:40f0:8", ["const:58c740:8", "const:4:8"]]
- 0058c740 ["CALL", null, ["callee:00c59190:8"]]
+ 0058ca60 ["INT_ADD", "register:40f0:8", ["const:58ca60:8", "const:4:8"]]
+ 0058ca60 ["CALL", null, ["callee:00c59190:8"]]
- 0058c740 bytes a02e1b94
+ 0058ca60 bytes cc311b94
- 0058c5cc ["INT_ADD", "register:40f0:8", ["const:58c5cc:8", "const:4:8"]]
- 0058c5cc ["CALL", null, ["callee:005891cc:8"]]
+ 0058c8ec ["INT_ADD", "register:40f0:8", ["const:58c8ec:8", "const:4:8"]]
+ 0058c8ec ["CALL", null, ["callee:005891cc:8"]]
- 0058c5cc bytes 38f2ff97
+ 0058c8ec bytes 38f2ff97
- 0058c5d4 ["INT_ADD", "register:40f0:8", ["const:58c5d4:8", "const:4:8"]]
- 0058c5d4 ["CALL", null, ["callee:005894bc:8"]]
+ 0058c8f4 ["INT_ADD", "register:40f0:8", ["const:58c8f4:8", "const:4:8"]]
+ 0058c8f4 ["CALL", null, ["callee:005894bc:8"]]
- 0058c5d4 bytes f2f2ff97
+ 0058c8f4 bytes f2f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74276ea1443227e9da3018227fa8f35b"></a>

### [`0058c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md) → [`0058cb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cb24.md) FUN_0058cb24

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597688.md) · 呼出先 6件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md)
- 新版 呼出元 1件 [`005979a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979a8.md) · 呼出先 6件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058cc7c",
      "incomplete_value": true,
      "site": "0058cc7c",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c95c",
      "incomplete_value": true,
      "site": "0058c95c",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058cb68",
      "incomplete_value": true,
      "site": "0058cb68",
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
      "definition_site": "0058c848",
      "incomplete_value": true,
      "site": "0058c848",
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
      "definition_site": "0058cc78",
      "incomplete_value": true,
      "site": "0058cc78",
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
      "definition_site": "0058c958",
      "incomplete_value": true,
      "site": "0058c958",
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
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058cb54",
      "PARAM",
      [
        "storage",
        "00ca64b0",
        null,
        null
      ]
    ],
    [
      "0058cb64",
      "READ",
      [
        "storage",
        "00ca64a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058cbbc",
      "READ",
      [
        "storage",
        "00ca64f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058cb54",
      "PARAM",
      [
        "storage",
        "00ca7470",
        null,
        null
      ]
    ],
    [
      "0058cb64",
      "READ",
      [
        "storage",
        "00ca7460",
        null,
        "undefined8"
      ]
    ],
    [
      "0058cbbc",
      "READ",
      [
        "storage",
        "00ca74b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md#insn-0058c838) · [`0058c95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md#insn-0058c95c) · [`0058c9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md#insn-0058c9b4)
- 新版 [`0058cb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cb24.md#insn-0058cb58) · [`0058cc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cb24.md#insn-0058cc7c) · [`0058ccd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cb24.md#insn-0058ccd4)

~~~diff
- 0058c838 ["INT_ADD", "register:40f0:8", ["const:58c838:8", "const:4:8"]]
- 0058c838 ["CALL", null, ["callee:00c59180:8"]]
+ 0058cb58 ["INT_ADD", "register:40f0:8", ["const:58cb58:8", "const:4:8"]]
+ 0058cb58 ["CALL", null, ["callee:00c59180:8"]]
- 0058c838 bytes 5e2e1b94
+ 0058cb58 bytes 8a311b94
- 0058c95c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:498:8"]]
- 0058c95c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0058cc7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:458:8"]]
+ 0058cc7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0058c95c bytes 284d02f9
+ 0058cc7c bytes 282d02f9
- 0058c9b4 ["INT_ADD", "register:40f0:8", ["const:58c9b4:8", "const:4:8"]]
- 0058c9b4 ["CALL", null, ["callee:00c59190:8"]]
+ 0058ccd4 ["INT_ADD", "register:40f0:8", ["const:58ccd4:8", "const:4:8"]]
+ 0058ccd4 ["CALL", null, ["callee:00c59190:8"]]
- 0058c9b4 bytes 032e1b94
+ 0058ccd4 bytes 2f311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5124f6eedfdf77cf4b00120d48e82b"></a>

### [`0058ca8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ca8c.md) → [`0058cdac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cdac.md) FUN_0058cdac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059768c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059768c.md) · 呼出先 13件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`005979ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979ac.md) · 呼出先 13件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ce00",
      "incomplete_value": true,
      "site": "0058ce00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:8f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cae0",
      "incomplete_value": true,
      "site": "0058cae0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:79c:8"
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
      "definition_site": "0058ce14",
      "incomplete_value": true,
      "site": "0058ce24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058caf4",
      "incomplete_value": true,
      "site": "0058cb04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
              ]
            ]
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
      "0058cdf4",
      "READ",
      [
        "storage",
        "002a679c",
        null,
        "string"
      ]
    ],
    [
      "0058ce14",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058cdf4",
      "READ",
      [
        "storage",
        "002a68f4",
        null,
        "string"
      ]
    ],
    [
      "0058ce14",
      "READ",
      [
        "storage",
        "002a0fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058cab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ca8c.md#insn-0058cab0) · [`0058cab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ca8c.md#insn-0058cab8) · [`0058cad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ca8c.md#insn-0058cad0)
- 新版 [`0058cdd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cdac.md#insn-0058cdd0) · [`0058cdd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cdac.md#insn-0058cdd8) · [`0058cdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cdac.md#insn-0058cdf0)

~~~diff
- 0058cab0 ["INT_ADD", "register:40f0:8", ["const:58cab0:8", "const:4:8"]]
- 0058cab0 ["CALL", null, ["callee:005891cc:8"]]
+ 0058cdd0 ["INT_ADD", "register:40f0:8", ["const:58cdd0:8", "const:4:8"]]
+ 0058cdd0 ["CALL", null, ["callee:005891cc:8"]]
- 0058cab0 bytes fff0ff97
+ 0058cdd0 bytes fff0ff97
- 0058cab8 ["INT_ADD", "register:40f0:8", ["const:58cab8:8", "const:4:8"]]
- 0058cab8 ["CALL", null, ["callee:005894bc:8"]]
+ 0058cdd8 ["INT_ADD", "register:40f0:8", ["const:58cdd8:8", "const:4:8"]]
+ 0058cdd8 ["CALL", null, ["callee:005894bc:8"]]
- 0058cab8 bytes b9f1ff97
+ 0058cdd8 bytes b9f1ff97
- 0058cad0 ["COPY", "tmp:0:8", ["const:79c:8"]]
- 0058cad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058cad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058cad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058cdf0 ["COPY", "tmp:0:8", ["const:8f4:8"]]
+ 0058cdf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058cdf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058cdf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058cad0 bytes 08711e91
+ 0058cdf0 bytes 08d12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f2241aaae681bd3e812896c45983a3"></a>

### [`0058ccf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccf0.md) → [`0058d010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d010.md) FUN_0058d010

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597694.md) · 呼出先 13件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`005979b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979b4.md) · 呼出先 13件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.79% / 新版 93.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d09c",
      "incomplete_value": true,
      "site": "0058d0a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cd7c",
      "incomplete_value": true,
      "site": "0058cd84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fc0:8"
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
      "definition_site": "0058d098",
      "incomplete_value": true,
      "site": "0058d0a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:68f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cd78",
      "incomplete_value": true,
      "site": "0058cd88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c2:8"
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
      "definition_site": "0058d098",
      "incomplete_value": true,
      "site": "0058d0a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058cd78",
      "incomplete_value": true,
      "site": "0058cd88",
      "value": [
        "LOAD",
        "16",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058d098",
      "READ",
      [
        "storage",
        "002ab5c2",
        null,
        "string"
      ]
    ],
    [
      "0058d098",
      "READ",
      [
        "storage",
        "002ab5d2",
        null,
        "string"
      ]
    ],
    [
      "0058d09c",
      "READ",
      [
        "storage",
        "002c2fc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058d098",
      "READ",
      [
        "storage",
        "002ab68f",
        null,
        "string"
      ]
    ],
    [
      "0058d098",
      "READ",
      [
        "storage",
        "002ab69f",
        null,
        "string"
      ]
    ],
    [
      "0058d09c",
      "READ",
      [
        "storage",
        "002c3010",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ce54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccf0.md#insn-0058ce54) · [`0058cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccf0.md#insn-0058cd38) · [`0058cd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccf0.md#insn-0058cd40)
- 新版 [`0058d174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d010.md#insn-0058d174) · [`0058d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d010.md#insn-0058d058) · [`0058d060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d010.md#insn-0058d060)

~~~diff
- 0058ce54 ["INT_ADD", "register:40f0:8", ["const:58ce54:8", "const:4:8"]]
- 0058ce54 ["CALL", null, ["callee:0058f794:8"]]
+ 0058d174 ["INT_ADD", "register:40f0:8", ["const:58d174:8", "const:4:8"]]
+ 0058d174 ["CALL", null, ["callee:0058f794:8"]]
- 0058ce54 bytes 88090094
+ 0058d174 bytes 88090094
- 0058cd38 ["INT_ADD", "register:40f0:8", ["const:58cd38:8", "const:4:8"]]
- 0058cd38 ["CALL", null, ["callee:005891cc:8"]]
+ 0058d058 ["INT_ADD", "register:40f0:8", ["const:58d058:8", "const:4:8"]]
+ 0058d058 ["CALL", null, ["callee:005891cc:8"]]
- 0058cd38 bytes 5df0ff97
+ 0058d058 bytes 5df0ff97
- 0058cd40 ["INT_ADD", "register:40f0:8", ["const:58cd40:8", "const:4:8"]]
- 0058cd40 ["CALL", null, ["callee:005894bc:8"]]
+ 0058d060 ["INT_ADD", "register:40f0:8", ["const:58d060:8", "const:4:8"]]
+ 0058d060 ["CALL", null, ["callee:005894bc:8"]]
- 0058cd40 bytes 17f1ff97
+ 0058d060 bytes 17f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e63cde76385ea82cf1e69392ac7c440a"></a>

### [`0058cf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058cf98.md) → [`0058d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d2b8.md) FUN_0058d2b8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597698.md) · 呼出先 12件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`005979b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979b8.md) · 呼出先 12件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d30c",
      "incomplete_value": true,
      "site": "0058d30c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cfec",
      "incomplete_value": true,
      "site": "0058cfec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:28c:8"
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
      "definition_site": "0058d318",
      "incomplete_value": true,
      "site": "0058d328",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:56b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cff8",
      "incomplete_value": true,
      "site": "0058d008",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48d:8"
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
      "definition_site": "0058d32c",
      "incomplete_value": true,
      "site": "0058d32c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058d00c",
      "incomplete_value": true,
      "site": "0058d00c",
      "value": [
        "LOAD",
        "8",
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
      "0058d2f8",
      "READ",
      [
        "storage",
        "002a128c",
        null,
        "string"
      ]
    ],
    [
      "0058d318",
      "READ",
      [
        "storage",
        "002bb48d",
        null,
        "string"
      ]
    ],
    [
      "0058d320",
      "READ",
      [
        "storage",
        "002bb49a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d2f8",
      "READ",
      [
        "storage",
        "002a12cc",
        null,
        "string"
      ]
    ],
    [
      "0058d318",
      "READ",
      [
        "storage",
        "002bb56b",
        null,
        "string"
      ]
    ],
    [
      "0058d320",
      "READ",
      [
        "storage",
        "002bb578",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058cf98.md#insn-0058d0c8) · [`0058cfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058cf98.md#insn-0058cfc0) · [`0058cfc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058cf98.md#insn-0058cfc8)
- 新版 [`0058d3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d2b8.md#insn-0058d3e8) · [`0058d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d2b8.md#insn-0058d2e0) · [`0058d2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d2b8.md#insn-0058d2e8)

~~~diff
- 0058d0c8 ["INT_ADD", "register:40f0:8", ["const:58d0c8:8", "const:4:8"]]
- 0058d0c8 ["CALL", null, ["callee:0058f794:8"]]
+ 0058d3e8 ["INT_ADD", "register:40f0:8", ["const:58d3e8:8", "const:4:8"]]
+ 0058d3e8 ["CALL", null, ["callee:0058f794:8"]]
- 0058d0c8 bytes eb080094
+ 0058d3e8 bytes eb080094
- 0058cfc0 ["INT_ADD", "register:40f0:8", ["const:58cfc0:8", "const:4:8"]]
- 0058cfc0 ["CALL", null, ["callee:005891cc:8"]]
+ 0058d2e0 ["INT_ADD", "register:40f0:8", ["const:58d2e0:8", "const:4:8"]]
+ 0058d2e0 ["CALL", null, ["callee:005891cc:8"]]
- 0058cfc0 bytes bbefff97
+ 0058d2e0 bytes bbefff97
- 0058cfc8 ["INT_ADD", "register:40f0:8", ["const:58cfc8:8", "const:4:8"]]
- 0058cfc8 ["CALL", null, ["callee:005894bc:8"]]
+ 0058d2e8 ["INT_ADD", "register:40f0:8", ["const:58d2e8:8", "const:4:8"]]
+ 0058d2e8 ["CALL", null, ["callee:005894bc:8"]]
- 0058cfc8 bytes 75f0ff97
+ 0058d2e8 bytes 75f0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20064b6bed70d07f8d4899f5de5c3f44"></a>

### [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) → [`0058d4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d4d0.md) FUN_0058d4d0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058ed00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md) · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`005891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891a8.md)
- 新版 呼出元 1件 [`0058f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f020.md) · 呼出先 15件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`005894c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894c8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d54c",
      "incomplete_value": true,
      "site": "0058d564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ac6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d22c",
      "incomplete_value": true,
      "site": "0058d244",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:96e:8"
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
      "definition_site": "0058d584",
      "incomplete_value": true,
      "site": "0058d58c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d264",
      "incomplete_value": true,
      "site": "0058d26c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:be0:8"
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
      "definition_site": "0058d68c",
      "incomplete_value": true,
      "site": "0058d68c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1cd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d36c",
      "incomplete_value": true,
      "site": "0058d36c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18d:8"
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
      "0058d50c",
      "DATA",
      [
        "storage",
        "00c6d008",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d54c",
      "READ",
      [
        "storage",
        "002a796e",
        null,
        "string"
      ]
    ],
    [
      "0058d580",
      "READ",
      [
        "storage",
        "002a1296",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d50c",
      "DATA",
      [
        "storage",
        "00c6dfd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d54c",
      "READ",
      [
        "storage",
        "002a7ac6",
        null,
        "string"
      ]
    ],
    [
      "0058d580",
      "READ",
      [
        "storage",
        "002a12d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md#insn-0058d1d4) · [`0058d1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md#insn-0058d1f0) · [`0058d1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md#insn-0058d1f8)
- 新版 [`0058d4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d4d0.md#insn-0058d4f4) · [`0058d510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d4d0.md#insn-0058d510) · [`0058d518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d4d0.md#insn-0058d518)

~~~diff
- 0058d1d4 ["COPY", "tmp:0:8", ["const:8:8"]]
- 0058d1d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058d1d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058d1d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058d4f4 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0058d4f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058d4f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058d4f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058d1d4 bytes 29210091
+ 0058d4f4 bytes 29613f91
- 0058d1f0 ["INT_ADD", "register:40f0:8", ["const:58d1f0:8", "const:4:8"]]
- 0058d1f0 ["CALL", null, ["callee:005894c8:8"]]
+ 0058d510 ["INT_ADD", "register:40f0:8", ["const:58d510:8", "const:4:8"]]
+ 0058d510 ["CALL", null, ["callee:005894c8:8"]]
- 0058d1f0 bytes eeefff97
+ 0058d510 bytes eeefff97
- 0058d1f8 ["INT_ADD", "register:40f0:8", ["const:58d1f8:8", "const:4:8"]]
- 0058d1f8 ["CALL", null, ["callee:005894c8:8"]]
+ 0058d518 ["INT_ADD", "register:40f0:8", ["const:58d518:8", "const:4:8"]]
+ 0058d518 ["CALL", null, ["callee:005894c8:8"]]
- 0058d1f8 bytes ecefff97
+ 0058d518 bytes ecefff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58bcb496c9a0c3cd8b4193b88d1fc7d1"></a>

### [`0058d644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d644.md) → [`0058d964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d964.md) FUN_0058d964

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d9d8",
      "incomplete_value": true,
      "site": "0058d9e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d6b8",
      "incomplete_value": true,
      "site": "0058d6c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:960:8"
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
      "definition_site": "0058d9d4",
      "incomplete_value": true,
      "site": "0058d9e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:12:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d6b4",
      "incomplete_value": true,
      "site": "0058d6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fc8:8"
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
      "definition_site": "0058d9d4",
      "incomplete_value": true,
      "site": "0058d9e4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058d6b4",
      "incomplete_value": true,
      "site": "0058d6c4",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058d9d4",
      "READ",
      [
        "storage",
        "002bffc8",
        null,
        "string"
      ]
    ],
    [
      "0058d9d4",
      "READ",
      [
        "storage",
        "002bffd8",
        null,
        "string"
      ]
    ],
    [
      "0058d9d8",
      "READ",
      [
        "storage",
        "002c2960",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058d9d4",
      "READ",
      [
        "storage",
        "002c0012",
        null,
        "string"
      ]
    ],
    [
      "0058d9d4",
      "READ",
      [
        "storage",
        "002c0022",
        null,
        "string"
      ]
    ],
    [
      "0058d9d8",
      "READ",
      [
        "storage",
        "002c29b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d644.md#insn-0058d670) · [`0058d678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d644.md#insn-0058d678) · [`0058d6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d644.md#insn-0058d6a4)
- 新版 [`0058d990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d964.md#insn-0058d990) · [`0058d998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d964.md#insn-0058d998) · [`0058d9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d964.md#insn-0058d9c4)

~~~diff
- 0058d670 ["INT_ADD", "register:40f0:8", ["const:58d670:8", "const:4:8"]]
- 0058d670 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058d990 ["INT_ADD", "register:40f0:8", ["const:58d990:8", "const:4:8"]]
+ 0058d990 ["CALL", null, ["callee:00589ba0:8"]]
- 0058d670 bytes 84f0ff97
+ 0058d990 bytes 84f0ff97
- 0058d678 ["INT_ADD", "register:40f0:8", ["const:58d678:8", "const:4:8"]]
- 0058d678 ["CALL", null, ["callee:005891cc:8"]]
+ 0058d998 ["INT_ADD", "register:40f0:8", ["const:58d998:8", "const:4:8"]]
+ 0058d998 ["CALL", null, ["callee:005891cc:8"]]
- 0058d678 bytes 0deeff97
+ 0058d998 bytes 0deeff97
- 0058d6a4 ["INT_ADD", "register:40f0:8", ["const:58d6a4:8", "const:4:8"]]
- 0058d6a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058d9c4 ["INT_ADD", "register:40f0:8", ["const:58d9c4:8", "const:4:8"]]
+ 0058d9c4 ["CALL", null, ["callee:00c58f30:8"]]
- 0058d6a4 bytes 2f2a1b94
+ 0058d9c4 bytes 5b2d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f91191df45d61b97fd12c1caafd325b"></a>

### [`0058d818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d818.md) → [`0058db38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058db38.md) FUN_0058db38

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058db94",
      "incomplete_value": true,
      "site": "0058db94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:98f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d874",
      "incomplete_value": true,
      "site": "0058d874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c2:8"
              ]
            ]
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
      "0058db88",
      "READ",
      [
        "storage",
        "002ad8c2",
        null,
        "string"
      ]
    ],
    [
      "0058dba8",
      "READ",
      [
        "storage",
        "002afaec",
        null,
        "string"
      ]
    ],
    [
      "0058dbac",
      "READ",
      [
        "storage",
        "002afafa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058db88",
      "READ",
      [
        "storage",
        "002ad98f",
        null,
        "string"
      ]
    ],
    [
      "0058dba8",
      "READ",
      [
        "storage",
        "002afbc3",
        null,
        "string"
      ]
    ],
    [
      "0058dbac",
      "READ",
      [
        "storage",
        "002afbd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d818.md#insn-0058d844) · [`0058d84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d818.md#insn-0058d84c) · [`0058d864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d818.md#insn-0058d864)
- 新版 [`0058db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058db38.md#insn-0058db64) · [`0058db6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058db38.md#insn-0058db6c) · [`0058db84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058db38.md#insn-0058db84)

~~~diff
- 0058d844 ["INT_ADD", "register:40f0:8", ["const:58d844:8", "const:4:8"]]
- 0058d844 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058db64 ["INT_ADD", "register:40f0:8", ["const:58db64:8", "const:4:8"]]
+ 0058db64 ["CALL", null, ["callee:00589ba0:8"]]
- 0058d844 bytes 0ff0ff97
+ 0058db64 bytes 0ff0ff97
- 0058d84c ["INT_ADD", "register:40f0:8", ["const:58d84c:8", "const:4:8"]]
- 0058d84c ["CALL", null, ["callee:005891cc:8"]]
+ 0058db6c ["INT_ADD", "register:40f0:8", ["const:58db6c:8", "const:4:8"]]
+ 0058db6c ["CALL", null, ["callee:005891cc:8"]]
- 0058d84c bytes 98edff97
+ 0058db6c bytes 98edff97
- 0058d864 ["COPY", "tmp:0:8", ["const:8c2:8"]]
- 0058d864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058d864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058d864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058db84 ["COPY", "tmp:0:8", ["const:98f:8"]]
+ 0058db84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058db84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058db84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058d864 bytes 08092391
+ 0058db84 bytes 083d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a87a2bcbfa67ae565f5c6431ff46ab2"></a>

### [`0058d9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d9f0.md) → [`0058dd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058dd10.md) FUN_0058dd10

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dd84",
      "incomplete_value": true,
      "site": "0058dd90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058da64",
      "incomplete_value": true,
      "site": "0058da70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f3:8"
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
      "definition_site": "0058dd94",
      "incomplete_value": true,
      "site": "0058dd94",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058da74",
      "incomplete_value": true,
      "site": "0058da74",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
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
      "0058dd84",
      "READ",
      [
        "storage",
        "002bb4f3",
        null,
        "string"
      ]
    ],
    [
      "0058dd88",
      "READ",
      [
        "storage",
        "002bb501",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058dd84",
      "READ",
      [
        "storage",
        "002bb5d1",
        null,
        "string"
      ]
    ],
    [
      "0058dd88",
      "READ",
      [
        "storage",
        "002bb5df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d9f0.md#insn-0058da20) · [`0058da2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d9f0.md#insn-0058da2c) · [`0058da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d9f0.md#insn-0058da60)
- 新版 [`0058dd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058dd10.md#insn-0058dd40) · [`0058dd4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058dd10.md#insn-0058dd4c) · [`0058dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058dd10.md#insn-0058dd80)

~~~diff
- 0058da20 ["INT_ADD", "register:40f0:8", ["const:58da20:8", "const:4:8"]]
- 0058da20 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058dd40 ["INT_ADD", "register:40f0:8", ["const:58dd40:8", "const:4:8"]]
+ 0058dd40 ["CALL", null, ["callee:00589ba0:8"]]
- 0058da20 bytes 98efff97
+ 0058dd40 bytes 98efff97
- 0058da2c ["INT_ADD", "register:40f0:8", ["const:58da2c:8", "const:4:8"]]
- 0058da2c ["CALL", null, ["callee:005891cc:8"]]
+ 0058dd4c ["INT_ADD", "register:40f0:8", ["const:58dd4c:8", "const:4:8"]]
+ 0058dd4c ["CALL", null, ["callee:005891cc:8"]]
- 0058da2c bytes 20edff97
+ 0058dd4c bytes 20edff97
- 0058da60 ["COPY", "tmp:0:8", ["const:4f3:8"]]
- 0058da60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058da60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058da60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058dd80 ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 0058dd80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058dd80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058dd80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058da60 bytes 29cd1391
+ 0058dd80 bytes 29451791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa9f665af33304637425f576821603e4"></a>

### [`0058dbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dbcc.md) → [`0058deec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058deec.md) FUN_0058deec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 11件 [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058df60",
      "incomplete_value": true,
      "site": "0058df68",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:48b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dc40",
      "incomplete_value": true,
      "site": "0058dc48",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:3c0:8"
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
      "definition_site": "0058df6c",
      "incomplete_value": true,
      "site": "0058df6c",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dc4c",
      "incomplete_value": true,
      "site": "0058dc4c",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
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
      "0058df60",
      "READ",
      [
        "storage",
        "002a43c0",
        null,
        "string"
      ]
    ],
    [
      "0058df64",
      "READ",
      [
        "storage",
        "002a43ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058df60",
      "READ",
      [
        "storage",
        "002a448b",
        null,
        "string"
      ]
    ],
    [
      "0058df64",
      "READ",
      [
        "storage",
        "002a4499",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058dbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dbcc.md#insn-0058dbf8) · [`0058dc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dbcc.md#insn-0058dc00) · [`0058dc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dbcc.md#insn-0058dc3c)
- 新版 [`0058df18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058deec.md#insn-0058df18) · [`0058df20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058deec.md#insn-0058df20) · [`0058df5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058deec.md#insn-0058df5c)

~~~diff
- 0058dbf8 ["INT_ADD", "register:40f0:8", ["const:58dbf8:8", "const:4:8"]]
- 0058dbf8 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058df18 ["INT_ADD", "register:40f0:8", ["const:58df18:8", "const:4:8"]]
+ 0058df18 ["CALL", null, ["callee:00589ba0:8"]]
- 0058dbf8 bytes 22efff97
+ 0058df18 bytes 22efff97
- 0058dc00 ["INT_ADD", "register:40f0:8", ["const:58dc00:8", "const:4:8"]]
- 0058dc00 ["CALL", null, ["callee:005891cc:8"]]
+ 0058df20 ["INT_ADD", "register:40f0:8", ["const:58df20:8", "const:4:8"]]
+ 0058df20 ["CALL", null, ["callee:005891cc:8"]]
- 0058dc00 bytes abecff97
+ 0058df20 bytes abecff97
- 0058dc3c ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 0058dc3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058dc3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058dc3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058df5c ["COPY", "tmp:0:8", ["const:48b:8"]]
+ 0058df5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058df5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058df5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058dc3c bytes 08010f91
+ 0058df5c bytes 082d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33591092827c585f86d63a3c586c5011"></a>

### [`0058dda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dda0.md) → [`0058e0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e0c0.md) FUN_0058e0c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e130",
      "incomplete_value": true,
      "site": "0058e138",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:adb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058de10",
      "incomplete_value": true,
      "site": "0058de18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:983:8"
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
      "definition_site": "0058e13c",
      "incomplete_value": true,
      "site": "0058e13c",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058de1c",
      "incomplete_value": true,
      "site": "0058de1c",
      "value": [
        "LOAD",
        "8",
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
                "const:e:8"
              ]
            ]
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
      "0058e130",
      "READ",
      [
        "storage",
        "002a7983",
        null,
        "string"
      ]
    ],
    [
      "0058e134",
      "READ",
      [
        "storage",
        "002a7991",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e130",
      "READ",
      [
        "storage",
        "002a7adb",
        null,
        "string"
      ]
    ],
    [
      "0058e134",
      "READ",
      [
        "storage",
        "002a7ae9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ddcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dda0.md#insn-0058ddcc) · [`0058ddd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dda0.md#insn-0058ddd4) · [`0058de0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dda0.md#insn-0058de0c)
- 新版 [`0058e0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e0c0.md#insn-0058e0ec) · [`0058e0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e0c0.md#insn-0058e0f4) · [`0058e12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e0c0.md#insn-0058e12c)

~~~diff
- 0058ddcc ["INT_ADD", "register:40f0:8", ["const:58ddcc:8", "const:4:8"]]
- 0058ddcc ["CALL", null, ["callee:00589ba0:8"]]
+ 0058e0ec ["INT_ADD", "register:40f0:8", ["const:58e0ec:8", "const:4:8"]]
+ 0058e0ec ["CALL", null, ["callee:00589ba0:8"]]
- 0058ddcc bytes adeeff97
+ 0058e0ec bytes adeeff97
- 0058ddd4 ["INT_ADD", "register:40f0:8", ["const:58ddd4:8", "const:4:8"]]
- 0058ddd4 ["CALL", null, ["callee:005891cc:8"]]
+ 0058e0f4 ["INT_ADD", "register:40f0:8", ["const:58e0f4:8", "const:4:8"]]
+ 0058e0f4 ["CALL", null, ["callee:005891cc:8"]]
- 0058ddd4 bytes 36ecff97
+ 0058e0f4 bytes 36ecff97
- 0058de0c ["COPY", "tmp:0:8", ["const:983:8"]]
- 0058de0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058de0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058de0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058e12c ["COPY", "tmp:0:8", ["const:adb:8"]]
+ 0058e12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058e12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058e12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058de0c bytes 080d2691
+ 0058e12c bytes 086d2b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e0516d4f3bd7f90e01cd9b95d32fe5"></a>

### [`0058df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058df70.md) → [`0058e290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e290.md) FUN_0058e290

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.43% / 新版 89.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e2ec",
      "incomplete_value": true,
      "site": "0058e2ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dfcc",
      "incomplete_value": true,
      "site": "0058dfcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
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
      "definition_site": "0058e30c",
      "incomplete_value": true,
      "site": "0058e314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dfec",
      "incomplete_value": true,
      "site": "0058dff4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be0:8"
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
      "definition_site": "0058e308",
      "incomplete_value": true,
      "site": "0058e318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dfe8",
      "incomplete_value": true,
      "site": "0058dff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e2dc",
      "READ",
      [
        "storage",
        "002a799a",
        null,
        "string"
      ]
    ],
    [
      "0058e308",
      "READ",
      [
        "storage",
        "002ac8e7",
        null,
        "string"
      ]
    ],
    [
      "0058e308",
      "READ",
      [
        "storage",
        "002ac8f7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e2dc",
      "READ",
      [
        "storage",
        "002a7af2",
        null,
        "string"
      ]
    ],
    [
      "0058e308",
      "READ",
      [
        "storage",
        "002ac9b4",
        null,
        "string"
      ]
    ],
    [
      "0058e308",
      "READ",
      [
        "storage",
        "002ac9c4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058dfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058df70.md#insn-0058dfa4) · [`0058dfac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058df70.md#insn-0058dfac) · [`0058dfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058df70.md#insn-0058dfb4)
- 新版 [`0058e2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e290.md#insn-0058e2c4) · [`0058e2cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e290.md#insn-0058e2cc) · [`0058e2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e290.md#insn-0058e2d4)

~~~diff
- 0058dfa4 ["INT_ADD", "register:40f0:8", ["const:58dfa4:8", "const:4:8"]]
- 0058dfa4 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058e2c4 ["INT_ADD", "register:40f0:8", ["const:58e2c4:8", "const:4:8"]]
+ 0058e2c4 ["CALL", null, ["callee:00589ba0:8"]]
- 0058dfa4 bytes 37eeff97
+ 0058e2c4 bytes 37eeff97
- 0058dfac ["INT_ADD", "register:40f0:8", ["const:58dfac:8", "const:4:8"]]
- 0058dfac ["CALL", null, ["callee:005891cc:8"]]
+ 0058e2cc ["INT_ADD", "register:40f0:8", ["const:58e2cc:8", "const:4:8"]]
+ 0058e2cc ["CALL", null, ["callee:005891cc:8"]]
- 0058dfac bytes c0ebff97
+ 0058e2cc bytes c0ebff97
- 0058dfb4 ["COPY", "tmp:0:8", ["const:99a:8"]]
- 0058dfb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058dfb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058dfb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058e2d4 ["COPY", "tmp:0:8", ["const:af2:8"]]
+ 0058e2d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e2d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e2d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058dfb4 bytes 29692691
+ 0058e2d4 bytes 29c92b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f3a3e27b12bc6228bf7723611949f81"></a>

### [`0058e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e1d0.md) → [`0058e4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e4f0.md) FUN_0058e4f0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.13% / 新版 87.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e554",
      "incomplete_value": true,
      "site": "0058e554",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e234",
      "incomplete_value": true,
      "site": "0058e234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8cd:8"
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
      "definition_site": "0058e570",
      "incomplete_value": true,
      "site": "0058e578",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e250",
      "incomplete_value": true,
      "site": "0058e258",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "0058e56c",
      "incomplete_value": true,
      "site": "0058e57c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e24c",
      "incomplete_value": true,
      "site": "0058e25c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f93:8"
              ]
            ]
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
      "0058e540",
      "READ",
      [
        "storage",
        "002ad8cd",
        null,
        "string"
      ]
    ],
    [
      "0058e56c",
      "READ",
      [
        "storage",
        "002b4f93",
        null,
        "string"
      ]
    ],
    [
      "0058e56c",
      "READ",
      [
        "storage",
        "002b4fa3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e540",
      "READ",
      [
        "storage",
        "002ad99a",
        null,
        "string"
      ]
    ],
    [
      "0058e56c",
      "READ",
      [
        "storage",
        "002b5071",
        null,
        "string"
      ]
    ],
    [
      "0058e56c",
      "READ",
      [
        "storage",
        "002b5081",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e1d0.md#insn-0058e204) · [`0058e20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e1d0.md#insn-0058e20c) · [`0058e218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e1d0.md#insn-0058e218)
- 新版 [`0058e524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e4f0.md#insn-0058e524) · [`0058e52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e4f0.md#insn-0058e52c) · [`0058e538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e4f0.md#insn-0058e538)

~~~diff
- 0058e204 ["INT_ADD", "register:40f0:8", ["const:58e204:8", "const:4:8"]]
- 0058e204 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058e524 ["INT_ADD", "register:40f0:8", ["const:58e524:8", "const:4:8"]]
+ 0058e524 ["CALL", null, ["callee:00589ba0:8"]]
- 0058e204 bytes 9fedff97
+ 0058e524 bytes 9fedff97
- 0058e20c ["INT_ADD", "register:40f0:8", ["const:58e20c:8", "const:4:8"]]
- 0058e20c ["CALL", null, ["callee:005891cc:8"]]
+ 0058e52c ["INT_ADD", "register:40f0:8", ["const:58e52c:8", "const:4:8"]]
+ 0058e52c ["CALL", null, ["callee:005891cc:8"]]
- 0058e20c bytes 28ebff97
+ 0058e52c bytes 28ebff97
- 0058e218 ["COPY", "tmp:0:8", ["const:8cd:8"]]
- 0058e218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058e218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058e218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058e538 ["COPY", "tmp:0:8", ["const:99a:8"]]
+ 0058e538 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e538 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e538 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058e218 bytes 29352391
+ 0058e538 bytes 29692691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02b8b086689a55ac36173a2d97cdd0e6"></a>

### [`0058e3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md) → [`0058e6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e6d8.md) FUN_0058e6d8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e754",
      "incomplete_value": true,
      "site": "0058e75c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e434",
      "incomplete_value": true,
      "site": "0058e43c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "0058e750",
      "incomplete_value": true,
      "site": "0058e760",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6bb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e430",
      "incomplete_value": true,
      "site": "0058e440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5ee:8"
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
      "definition_site": "0058e750",
      "incomplete_value": true,
      "site": "0058e760",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058e430",
      "incomplete_value": true,
      "site": "0058e440",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e750",
      "READ",
      [
        "storage",
        "002ab5ee",
        null,
        "string"
      ]
    ],
    [
      "0058e750",
      "READ",
      [
        "storage",
        "002ab5fe",
        null,
        "string"
      ]
    ],
    [
      "0058e754",
      "READ",
      [
        "storage",
        "002c23e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e750",
      "READ",
      [
        "storage",
        "002ab6bb",
        null,
        "string"
      ]
    ],
    [
      "0058e750",
      "READ",
      [
        "storage",
        "002ab6cb",
        null,
        "string"
      ]
    ],
    [
      "0058e754",
      "READ",
      [
        "storage",
        "002c2430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md#insn-0058e3ec) · [`0058e3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md#insn-0058e3f4) · [`0058e420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md#insn-0058e420)
- 新版 [`0058e70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e6d8.md#insn-0058e70c) · [`0058e714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e6d8.md#insn-0058e714) · [`0058e740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058e6d8.md#insn-0058e740)

~~~diff
- 0058e3ec ["INT_ADD", "register:40f0:8", ["const:58e3ec:8", "const:4:8"]]
- 0058e3ec ["CALL", null, ["callee:00589ba0:8"]]
+ 0058e70c ["INT_ADD", "register:40f0:8", ["const:58e70c:8", "const:4:8"]]
+ 0058e70c ["CALL", null, ["callee:00589ba0:8"]]
- 0058e3ec bytes 25edff97
+ 0058e70c bytes 25edff97
- 0058e3f4 ["INT_ADD", "register:40f0:8", ["const:58e3f4:8", "const:4:8"]]
- 0058e3f4 ["CALL", null, ["callee:005891cc:8"]]
+ 0058e714 ["INT_ADD", "register:40f0:8", ["const:58e714:8", "const:4:8"]]
+ 0058e714 ["CALL", null, ["callee:005891cc:8"]]
- 0058e3f4 bytes aeeaff97
+ 0058e714 bytes aeeaff97
- 0058e420 ["INT_ADD", "register:40f0:8", ["const:58e420:8", "const:4:8"]]
- 0058e420 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058e740 ["INT_ADD", "register:40f0:8", ["const:58e740:8", "const:4:8"]]
+ 0058e740 ["CALL", null, ["callee:00c58f30:8"]]
- 0058e420 bytes d0261b94
+ 0058e740 bytes fc291b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1ae6b3ce160ebcd8c0771751fb4a39"></a>

### [`0058e788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md) → [`0058eaa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058eaa8.md) FUN_0058eaa8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058eb24",
      "incomplete_value": true,
      "site": "0058eb2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e804",
      "incomplete_value": true,
      "site": "0058e80c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "0058eb20",
      "incomplete_value": true,
      "site": "0058eb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e800",
      "incomplete_value": true,
      "site": "0058e810",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fd3:8"
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
      "definition_site": "0058eb20",
      "incomplete_value": true,
      "site": "0058eb30",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058e800",
      "incomplete_value": true,
      "site": "0058e810",
      "value": [
        "LOAD",
        "16",
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
      "0058eb20",
      "READ",
      [
        "storage",
        "002b4fd3",
        null,
        "string"
      ]
    ],
    [
      "0058eb20",
      "READ",
      [
        "storage",
        "002b4fe3",
        null,
        "string"
      ]
    ],
    [
      "0058eb24",
      "READ",
      [
        "storage",
        "002c23e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058eb20",
      "READ",
      [
        "storage",
        "002b50b1",
        null,
        "string"
      ]
    ],
    [
      "0058eb20",
      "READ",
      [
        "storage",
        "002b50c1",
        null,
        "string"
      ]
    ],
    [
      "0058eb24",
      "READ",
      [
        "storage",
        "002c2430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md#insn-0058e7bc) · [`0058e7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md#insn-0058e7c4) · [`0058e7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md#insn-0058e7f0)
- 新版 [`0058eadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058eaa8.md#insn-0058eadc) · [`0058eae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058eaa8.md#insn-0058eae4) · [`0058eb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058eaa8.md#insn-0058eb10)

~~~diff
- 0058e7bc ["INT_ADD", "register:40f0:8", ["const:58e7bc:8", "const:4:8"]]
- 0058e7bc ["CALL", null, ["callee:00589ba0:8"]]
+ 0058eadc ["INT_ADD", "register:40f0:8", ["const:58eadc:8", "const:4:8"]]
+ 0058eadc ["CALL", null, ["callee:00589ba0:8"]]
- 0058e7bc bytes 31ecff97
+ 0058eadc bytes 31ecff97
- 0058e7c4 ["INT_ADD", "register:40f0:8", ["const:58e7c4:8", "const:4:8"]]
- 0058e7c4 ["CALL", null, ["callee:005891cc:8"]]
+ 0058eae4 ["INT_ADD", "register:40f0:8", ["const:58eae4:8", "const:4:8"]]
+ 0058eae4 ["CALL", null, ["callee:005891cc:8"]]
- 0058e7c4 bytes bae9ff97
+ 0058eae4 bytes bae9ff97
- 0058e7f0 ["INT_ADD", "register:40f0:8", ["const:58e7f0:8", "const:4:8"]]
- 0058e7f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0058eb10 ["INT_ADD", "register:40f0:8", ["const:58eb10:8", "const:4:8"]]
+ 0058eb10 ["CALL", null, ["callee:00c58f30:8"]]
- 0058e7f0 bytes dc251b94
+ 0058eb10 bytes 08291b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42ce4127a1c2eec7ee2bb2bef6f2b190"></a>

### [`0058e96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md) → [`0058ec8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058ec8c.md) FUN_0058ec8c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589ba0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.07% / 新版 88.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ece8",
      "incomplete_value": true,
      "site": "0058ece8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:361:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e9c8",
      "incomplete_value": true,
      "site": "0058e9c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:317:8"
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
      "definition_site": "0058ed08",
      "incomplete_value": true,
      "site": "0058ed10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e9e8",
      "incomplete_value": true,
      "site": "0058e9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e60:8"
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
      "definition_site": "0058ed04",
      "incomplete_value": true,
      "site": "0058ed14",
      "value": [
        "LOAD",
        "16",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e9e4",
      "incomplete_value": true,
      "site": "0058e9f4",
      "value": [
        "LOAD",
        "16",
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
                "const:20:8"
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
      "0058ecd8",
      "READ",
      [
        "storage",
        "002c1317",
        null,
        "string"
      ]
    ],
    [
      "0058ed04",
      "READ",
      [
        "storage",
        "002a43f7",
        null,
        "string"
      ]
    ],
    [
      "0058ed04",
      "READ",
      [
        "storage",
        "002a4407",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058ecd8",
      "READ",
      [
        "storage",
        "002c1361",
        null,
        "string"
      ]
    ],
    [
      "0058ed04",
      "READ",
      [
        "storage",
        "002a44c2",
        null,
        "string"
      ]
    ],
    [
      "0058ed04",
      "READ",
      [
        "storage",
        "002a44d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md#insn-0058e9a0) · [`0058e9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md#insn-0058e9a8) · [`0058e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md#insn-0058e9b0)
- 新版 [`0058ecc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058ec8c.md#insn-0058ecc0) · [`0058ecc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058ec8c.md#insn-0058ecc8) · [`0058ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058e/0058ec8c.md#insn-0058ecd0)

~~~diff
- 0058e9a0 ["INT_ADD", "register:40f0:8", ["const:58e9a0:8", "const:4:8"]]
- 0058e9a0 ["CALL", null, ["callee:00589ba0:8"]]
+ 0058ecc0 ["INT_ADD", "register:40f0:8", ["const:58ecc0:8", "const:4:8"]]
+ 0058ecc0 ["CALL", null, ["callee:00589ba0:8"]]
- 0058e9a0 bytes b8ebff97
+ 0058ecc0 bytes b8ebff97
- 0058e9a8 ["INT_ADD", "register:40f0:8", ["const:58e9a8:8", "const:4:8"]]
- 0058e9a8 ["CALL", null, ["callee:005891cc:8"]]
+ 0058ecc8 ["INT_ADD", "register:40f0:8", ["const:58ecc8:8", "const:4:8"]]
+ 0058ecc8 ["CALL", null, ["callee:005891cc:8"]]
- 0058e9a8 bytes 41e9ff97
+ 0058ecc8 bytes 41e9ff97
- 0058e9b0 ["COPY", "tmp:0:8", ["const:317:8"]]
- 0058e9b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058e9b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058e9b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058ecd0 ["COPY", "tmp:0:8", ["const:361:8"]]
+ 0058ecd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058ecd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058ecd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058e9b0 bytes 295d0c91
+ 0058ecd0 bytes 29850d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6fc860e900ba309312ceb3d90615eee"></a>

### [`0058ed00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md) → [`0058f020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f020.md) FUN_0058f020

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) · 呼出先 2件 [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0059821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059821c.md) · 呼出先 2件 [`0058d4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058d/0058d4d0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f048",
      "incomplete_value": false,
      "site": "0058f054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ed28",
      "incomplete_value": false,
      "site": "0058ed34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "0058f054",
      "DATA",
      [
        "storage",
        "00c6d090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f054",
      "DATA",
      [
        "storage",
        "00c6e060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md#insn-0058ed1c) · [`0058ed24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md#insn-0058ed24) · [`0058ed28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md#insn-0058ed28)
- 新版 [`0058f03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f020.md#insn-0058f03c) · [`0058f044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f020.md#insn-0058f044) · [`0058f048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f020.md#insn-0058f048)

~~~diff
- 0058ed1c ["INT_ADD", "register:40f0:8", ["const:58ed1c:8", "const:4:8"]]
- 0058ed1c ["CALL", null, ["callee:00c58f30:8"]]
+ 0058f03c ["INT_ADD", "register:40f0:8", ["const:58f03c:8", "const:4:8"]]
+ 0058f03c ["CALL", null, ["callee:00c58f30:8"]]
- 0058ed1c bytes 91241b94
+ 0058f03c bytes bd271b94
- 0058ed24 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0058f044 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0058ed24 bytes e83600f0
+ 0058f044 bytes e83600f0
- 0058ed28 ["COPY", "tmp:0:8", ["const:90:8"]]
- 0058ed28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ed28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ed28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f048 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0058f048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ed28 bytes 08410291
+ 0058f048 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee88f42f1ae12917ec7e1c1adc97341c"></a>

### [`0058eee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md) → [`0058f200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f200.md) FUN_0058f200

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f04.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00598224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598224.md) · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f26c",
      "incomplete_value": true,
      "site": "0058f27c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ef4c",
      "incomplete_value": true,
      "site": "0058ef5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
              ]
            ]
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
      "0058f248",
      "READ",
      [
        "storage",
        "002b750b",
        null,
        "string"
      ]
    ],
    [
      "0058f26c",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058f248",
      "READ",
      [
        "storage",
        "002b75da",
        null,
        "string"
      ]
    ],
    [
      "0058f26c",
      "READ",
      [
        "storage",
        "002a0fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md#insn-0058ef04) · [`0058ef0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md#insn-0058ef0c) · [`0058ef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md#insn-0058ef24)
- 新版 [`0058f224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f200.md#insn-0058f224) · [`0058f22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f200.md#insn-0058f22c) · [`0058f244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f200.md#insn-0058f244)

~~~diff
- 0058ef04 ["INT_ADD", "register:40f0:8", ["const:58ef04:8", "const:4:8"]]
- 0058ef04 ["CALL", null, ["callee:005891cc:8"]]
+ 0058f224 ["INT_ADD", "register:40f0:8", ["const:58f224:8", "const:4:8"]]
+ 0058f224 ["CALL", null, ["callee:005891cc:8"]]
- 0058ef04 bytes eae7ff97
+ 0058f224 bytes eae7ff97
- 0058ef0c ["INT_ADD", "register:40f0:8", ["const:58ef0c:8", "const:4:8"]]
- 0058ef0c ["CALL", null, ["callee:005894bc:8"]]
+ 0058f22c ["INT_ADD", "register:40f0:8", ["const:58f22c:8", "const:4:8"]]
+ 0058f22c ["CALL", null, ["callee:005894bc:8"]]
- 0058ef0c bytes a4e8ff97
+ 0058f22c bytes a4e8ff97
- 0058ef24 ["COPY", "tmp:0:8", ["const:50b:8"]]
- 0058ef24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ef24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ef24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f244 ["COPY", "tmp:0:8", ["const:5da:8"]]
+ 0058f244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ef24 bytes 082d1491
+ 0058f244 bytes 08691791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d482e4581a0ab5cd6499c0e5b799ab9f"></a>

### [`0058f08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md) → [`0058f3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f3ac.md) FUN_0058f3ac

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`00598228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598228.md) · 呼出先 14件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f420",
      "incomplete_value": true,
      "site": "0058f42c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f100",
      "incomplete_value": true,
      "site": "0058f10c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:9c0:8"
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
      "0058f41c",
      "READ",
      [
        "storage",
        "002a2111",
        null,
        "string"
      ]
    ],
    [
      "0058f41c",
      "READ",
      [
        "storage",
        "002a2121",
        null,
        "string"
      ]
    ],
    [
      "0058f420",
      "READ",
      [
        "storage",
        "002c29c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058f41c",
      "READ",
      [
        "storage",
        "002a21dc",
        null,
        "string"
      ]
    ],
    [
      "0058f41c",
      "READ",
      [
        "storage",
        "002a21ec",
        null,
        "string"
      ]
    ],
    [
      "0058f420",
      "READ",
      [
        "storage",
        "002c2a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md#insn-0058f0b8) · [`0058f0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md#insn-0058f0c0) · [`0058f0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md#insn-0058f0ec)
- 新版 [`0058f3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f3ac.md#insn-0058f3d8) · [`0058f3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f3ac.md#insn-0058f3e0) · [`0058f40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f3ac.md#insn-0058f40c)

~~~diff
- 0058f0b8 ["INT_ADD", "register:40f0:8", ["const:58f0b8:8", "const:4:8"]]
- 0058f0b8 ["CALL", null, ["callee:005891cc:8"]]
+ 0058f3d8 ["INT_ADD", "register:40f0:8", ["const:58f3d8:8", "const:4:8"]]
+ 0058f3d8 ["CALL", null, ["callee:005891cc:8"]]
- 0058f0b8 bytes 7de7ff97
+ 0058f3d8 bytes 7de7ff97
- 0058f0c0 ["INT_ADD", "register:40f0:8", ["const:58f0c0:8", "const:4:8"]]
- 0058f0c0 ["CALL", null, ["callee:005894bc:8"]]
+ 0058f3e0 ["INT_ADD", "register:40f0:8", ["const:58f3e0:8", "const:4:8"]]
+ 0058f3e0 ["CALL", null, ["callee:005894bc:8"]]
- 0058f0c0 bytes 37e8ff97
+ 0058f3e0 bytes 37e8ff97
- 0058f0ec ["INT_ADD", "register:40f0:8", ["const:58f0ec:8", "const:4:8"]]
- 0058f0ec ["CALL", null, ["callee:00c58f30:8"]]
+ 0058f40c ["INT_ADD", "register:40f0:8", ["const:58f40c:8", "const:4:8"]]
+ 0058f40c ["CALL", null, ["callee:00c58f30:8"]]
- 0058f0ec bytes 9d231b94
+ 0058f40c bytes c9261b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

