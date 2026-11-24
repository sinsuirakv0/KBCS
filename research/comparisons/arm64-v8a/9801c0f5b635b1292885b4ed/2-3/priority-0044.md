# v16.0.1 → v16.0.2 · 最優先の変更候補 (44)

[一覧の目次](README.md)

<a id="compare-4a901b2bc620f54b567f2e902a28e98d"></a>

### [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) → [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) FUN_00826e14

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0082a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md) [`008317f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md) · 呼出先 10件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00824330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/00824330.md) [`008244dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/008244dc.md) [`0082467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/0082467c.md)
- 新版 呼出元 2件 [`0082a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082a7f8.md) [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) · 呼出先 10件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00824388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824388.md) [`00824534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/00824534.md) [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00827148",
      "incomplete_value": true,
      "site": "00827150",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008270f0",
      "incomplete_value": true,
      "site": "008270f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00826e50",
      "value": [
        "leaf",
        "ram:8246d4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00826df8",
      "value": [
        "leaf",
        "ram:82467c:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00826e98",
      "incomplete_value": false,
      "site": "00826e9c",
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
      "definition_site": "00826e40",
      "incomplete_value": false,
      "site": "00826e44",
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
      "00826e50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082467c"
      ]
    ],
    [
      "00826e98",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "00826fe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      "00826e50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008246d4"
      ]
    ],
    [
      "00826e98",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ],
    [
      "00826fe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00826df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md#insn-00826df8) · [`00826e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md#insn-00826e44) · [`00826f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md#insn-00826f90)
- 新版 `00826e50`（命令位置の公開資料なし） · `00826e9c`（命令位置の公開資料なし） · `00826fe8`（命令位置の公開資料なし）

~~~diff
- 00826df8 ["INT_ADD", "register:40f0:8", ["const:826df8:8", "const:4:8"]]
- 00826df8 ["CALL", null, ["ram:82467c:8"]]
+ 00826e50 ["INT_ADD", "register:40f0:8", ["const:826e50:8", "const:4:8"]]
+ 00826e50 ["CALL", null, ["ram:8246d4:8"]]
- 00826df8 bytes 21f6ff97
+ 00826e50 bytes 21f6ff97
- 00826e44 ["INT_ADD", "register:40f0:8", ["const:826e44:8", "const:4:8"]]
- 00826e44 ["CALL", null, ["callee:00442970:8"]]
+ 00826e9c ["INT_ADD", "register:40f0:8", ["const:826e9c:8", "const:4:8"]]
+ 00826e9c ["CALL", null, ["callee:00442970:8"]]
- 00826e44 bytes bb6ef097
+ 00826e9c bytes b56ef097
- 00826f90 ["INT_ADD", "register:40f0:8", ["const:826f90:8", "const:4:8"]]
- 00826f90 ["CALL", null, ["ram:a65dec:8"]]
+ 00826fe8 ["INT_ADD", "register:40f0:8", ["const:826fe8:8", "const:4:8"]]
+ 00826fe8 ["CALL", null, ["ram:a65e5c:8"]]
- 00826f90 bytes 97fb0894
+ 00826fe8 bytes 9dfb0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91e435ea7b709c8da20066efe2cc1b7d"></a>

### [`00827178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827178.md) → [`008271d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/008271d0.md) FUN_008271d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00829574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) [`0082ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md) · 呼出先 13件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a46784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md) [`00a468c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468c8.md)
- 新版 呼出元 2件 [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) [`0082acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082acc0.md) · 呼出先 13件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a467d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a467d8.md) [`00a4691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4691c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00827350",
      "incomplete_value": false,
      "site": "00827354",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "008272f8",
      "incomplete_value": false,
      "site": "008272fc",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00827210",
      "incomplete_value": true,
      "site": "00827210",
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
      "definition_site": "008271b8",
      "incomplete_value": true,
      "site": "008271b8",
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
      "definition_site": "00827218",
      "incomplete_value": false,
      "site": "00827228",
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
      "definition_site": "008271c0",
      "incomplete_value": false,
      "site": "008271d0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082720c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00827218",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00827220",
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
      "0082720c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00827218",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00827220",
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


#### 変更候補の命令位置

- 旧版 [`008271d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827178.md#insn-008271d0) · [`008272a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827178.md#insn-008272a4) · [`00827458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827178.md#insn-00827458)
- 新版 `00827228`（命令位置の公開資料なし） · `008272fc`（命令位置の公開資料なし） · `008274b0`（命令位置の公開資料なし）

~~~diff
- 008271d0 ["INT_ADD", "register:40f0:8", ["const:8271d0:8", "const:4:8"]]
- 008271d0 ["CALL", null, ["callee:00c586e0:8"]]
+ 00827228 ["INT_ADD", "register:40f0:8", ["const:827228:8", "const:4:8"]]
+ 00827228 ["CALL", null, ["callee:00c586e0:8"]]
- 008271d0 bytes 10c51094
+ 00827228 bytes 2ec51094
- 008272a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008272a4 ["INT_ADD", "register:40f0:8", ["const:8272a4:8", "const:4:8"]]
- 008272a4 ["CALLIND", null, ["register:0:8"]]
+ 008272fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008272fc ["INT_ADD", "register:40f0:8", ["const:8272fc:8", "const:4:8"]]
+ 008272fc ["CALLIND", null, ["register:0:8"]]
- 008272a4 bytes 00013fd6
+ 008272fc bytes 00013fd6
- 00827458 ["INT_ADD", "register:40f0:8", ["const:827458:8", "const:4:8"]]
- 00827458 ["CALL", null, ["callee:00442970:8"]]
+ 008274b0 ["INT_ADD", "register:40f0:8", ["const:8274b0:8", "const:4:8"]]
+ 008274b0 ["CALL", null, ["callee:00442970:8"]]
- 00827458 bytes 366df097
+ 008274b0 bytes 306df097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c3e225409e1f84c111ba29c15e90402"></a>

### [`008274f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008274f4.md) → [`0082754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/0082754c.md) FUN_0082754c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0082ab78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ab78.md) · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`00a468f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468f0.md)
- 新版 呼出元 1件 [`0082abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082abd0.md) · 呼出先 7件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`00a46944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46944.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008276bc",
      "incomplete_value": false,
      "site": "008276c0",
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
      "definition_site": "00827664",
      "incomplete_value": false,
      "site": "00827668",
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
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008276bc",
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
      "008276bc",
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


#### 変更候補の命令位置

- 旧版 [`00827668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008274f4.md#insn-00827668) · [`00827508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008274f4.md#insn-00827508) · [`00827518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008274f4.md#insn-00827518)
- 新版 `008276c0`（命令位置の公開資料なし） · `00827560`（命令位置の公開資料なし） · `00827570`（命令位置の公開資料なし）

~~~diff
- 00827668 ["INT_ADD", "register:40f0:8", ["const:827668:8", "const:4:8"]]
- 00827668 ["CALL", null, ["callee:00442970:8"]]
+ 008276c0 ["INT_ADD", "register:40f0:8", ["const:8276c0:8", "const:4:8"]]
+ 008276c0 ["CALL", null, ["callee:00442970:8"]]
- 00827668 bytes b26cf097
+ 008276c0 bytes ac6cf097
- 00827508 ["INT_ADD", "register:40f0:8", ["const:827508:8", "const:4:8"]]
- 00827508 ["CALL", null, ["callee:00851550:8"]]
+ 00827560 ["INT_ADD", "register:40f0:8", ["const:827560:8", "const:4:8"]]
+ 00827560 ["CALL", null, ["callee:00851550:8"]]
- 00827508 bytes fca70094
+ 00827560 bytes fca70094
- 00827518 ["INT_ADD", "register:40f0:8", ["const:827518:8", "const:4:8"]]
- 00827518 ["CALL", null, ["callee:008b7a20:8"]]
+ 00827570 ["INT_ADD", "register:40f0:8", ["const:827570:8", "const:4:8"]]
+ 00827570 ["CALL", null, ["callee:008b7a20:8"]]
- 00827518 bytes 2c410294
+ 00827570 bytes 2c410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-974251416f6a4e680d4141dac8238217"></a>

### [`008276c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008276c0.md) → [`00827718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827718.md) FUN_00827718

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008317f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ab04fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab04fc.md)
- 新版 呼出元 1件 [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00ab056c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab056c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00827814",
      "incomplete_value": false,
      "site": "00827818",
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
      "definition_site": "008277bc",
      "incomplete_value": false,
      "site": "008277c0",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008278a0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00827848",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00827914",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008278bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00827814",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "008278a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00827914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00827814",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ],
    [
      "008278a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00827914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008277c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008276c0.md#insn-008277c0) · [`00827848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008276c0.md#insn-00827848) · [`008278b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008276c0.md#insn-008278b4)
- 新版 `00827818`（命令位置の公開資料なし） · `008278a0`（命令位置の公開資料なし） · `0082790c`（命令位置の公開資料なし）

~~~diff
- 008277c0 ["INT_ADD", "register:40f0:8", ["const:8277c0:8", "const:4:8"]]
- 008277c0 ["CALL", null, ["callee:00442970:8"]]
+ 00827818 ["INT_ADD", "register:40f0:8", ["const:827818:8", "const:4:8"]]
+ 00827818 ["CALL", null, ["callee:00442970:8"]]
- 008277c0 bytes 5c6cf097
+ 00827818 bytes 566cf097
- 00827848 ["INT_ADD", "register:40f0:8", ["const:827848:8", "const:4:8"]]
- 00827848 ["CALL", null, ["ram:47acf4:8"]]
+ 008278a0 ["INT_ADD", "register:40f0:8", ["const:8278a0:8", "const:4:8"]]
+ 008278a0 ["CALL", null, ["ram:47ad34:8"]]
- 00827848 bytes 2b4df197
+ 008278a0 bytes 254df197
- 008278b4 ["INT_ADD", "register:40f0:8", ["const:8278b4:8", "const:4:8"]]
- 008278b4 ["CALL", null, ["callee:00ab056c:8"]]
+ 0082790c ["INT_ADD", "register:40f0:8", ["const:82790c:8", "const:4:8"]]
+ 0082790c ["CALL", null, ["callee:00ab056c:8"]]
- 008278b4 bytes 12230a94
+ 0082790c bytes 18230a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3f6d474bf4d7d71b1b74b789ad4d38"></a>

### [`00827918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md) → [`00827970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827970.md) FUN_00827970

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008317f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md) · 呼出先 34件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 1件 [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) · 呼出先 34件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.44% / 新版 91.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 5件, `store_value` 28件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00827b48",
      "incomplete_value": false,
      "site": "00827b48",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00827af0",
      "incomplete_value": false,
      "site": "00827af0",
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
            "const:538:8"
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
      "definition_site": "00827b98",
      "incomplete_value": false,
      "site": "00827b98",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00827b40",
      "incomplete_value": false,
      "site": "00827b40",
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
            "const:5b8:8"
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
      "definition_site": "00827f04",
      "incomplete_value": true,
      "site": "00827f14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ca9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00827eac",
      "incomplete_value": true,
      "site": "00827ebc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d05:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 78,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00827a34",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "00827b48",
      "DATA",
      [
        "storage",
        "00c7e538",
        null,
        "undefined *"
      ]
    ],
    [
      "00827b98",
      "DATA",
      [
        "storage",
        "00c7e5b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00827a34",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ],
    [
      "00827b48",
      "DATA",
      [
        "storage",
        "00c7e608",
        null,
        "undefined *"
      ]
    ],
    [
      "00827b98",
      "DATA",
      [
        "storage",
        "00c7e688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008279e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md#insn-008279e0) · [`00827b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md#insn-00827b48) · [`00827b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/00827918.md#insn-00827b84)
- 新版 `00827a38`（命令位置の公開資料なし） · `00827ba0`（命令位置の公開資料なし） · `00827bdc`（命令位置の公開資料なし）

~~~diff
- 008279e0 ["INT_ADD", "register:40f0:8", ["const:8279e0:8", "const:4:8"]]
- 008279e0 ["CALL", null, ["callee:00442970:8"]]
+ 00827a38 ["INT_ADD", "register:40f0:8", ["const:827a38:8", "const:4:8"]]
+ 00827a38 ["CALL", null, ["callee:00442970:8"]]
- 008279e0 bytes d46bf097
+ 00827a38 bytes ce6bf097
- 00827b48 ["INT_ADD", "register:40f0:8", ["const:827b48:8", "const:4:8"]]
- 00827b48 ["CALL", null, ["callee:0057bee8:8"]]
+ 00827ba0 ["INT_ADD", "register:40f0:8", ["const:827ba0:8", "const:4:8"]]
+ 00827ba0 ["CALL", null, ["callee:0057bee8:8"]]
- 00827b48 bytes d850f597
+ 00827ba0 bytes d250f597
- 00827b84 ["INT_ADD", "register:40f0:8", ["const:827b84:8", "const:4:8"]]
- 00827b84 ["CALL", null, ["ram:80645c:8"]]
+ 00827bdc ["INT_ADD", "register:40f0:8", ["const:827bdc:8", "const:4:8"]]
+ 00827bdc ["CALL", null, ["ram:8064b4:8"]]
- 00827b84 bytes 367aff97
+ 00827bdc bytes 367aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0991a83e1f1b657cdb7f42d0ddada516"></a>

### [`00828bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00828/00828bdc.md) → [`00828c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00828/00828c34.md) FUN_00828c34

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008317f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md) · 呼出先 22件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0081fdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081f/0081fdc8.md) [`0082907c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md)
- 新版 呼出元 1件 [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) · 呼出先 22件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0081fe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081f/0081fe20.md) [`008290d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008290d4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.71% / 新版 89.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00828cb8",
      "incomplete_value": true,
      "site": "00828cc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00828c60",
      "incomplete_value": true,
      "site": "00828c70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00828ccc",
      "incomplete_value": true,
      "site": "00828ccc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00828c74",
      "incomplete_value": true,
      "site": "00828c74",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00828cc0",
      "incomplete_value": true,
      "site": "00828cd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00828c68",
      "incomplete_value": true,
      "site": "00828c78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00828cb8",
      "READ",
      [
        "storage",
        "002b406d",
        null,
        "string"
      ]
    ],
    [
      "00828cbc",
      "READ",
      [
        "storage",
        "002b407c",
        null,
        "string"
      ]
    ],
    [
      "00828cc0",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00828cb8",
      "READ",
      [
        "storage",
        "002b409e",
        null,
        "string"
      ]
    ],
    [
      "00828cbc",
      "READ",
      [
        "storage",
        "002b40ad",
        null,
        "string"
      ]
    ],
    [
      "00828cc0",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00828c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00828/00828bdc.md#insn-00828c1c) · [`00828d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00828/00828bdc.md#insn-00828d14) · [`00828d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00828/00828bdc.md#insn-00828d94)
- 新版 `00828c74`（命令位置の公開資料なし） · `00828d6c`（命令位置の公開資料なし） · `00828dec`（命令位置の公開資料なし）

~~~diff
- 00828c1c ["INT_ADD", "register:40f0:8", ["const:828c1c:8", "const:4:8"]]
- 00828c1c ["CALL", null, ["callee:00851550:8"]]
+ 00828c74 ["INT_ADD", "register:40f0:8", ["const:828c74:8", "const:4:8"]]
+ 00828c74 ["CALL", null, ["callee:00851550:8"]]
- 00828c1c bytes 37a20094
+ 00828c74 bytes 37a20094
- 00828d14 ["INT_ADD", "register:40f0:8", ["const:828d14:8", "const:4:8"]]
- 00828d14 ["CALL", null, ["ram:47acf4:8"]]
+ 00828d6c ["INT_ADD", "register:40f0:8", ["const:828d6c:8", "const:4:8"]]
+ 00828d6c ["CALL", null, ["ram:47ad34:8"]]
- 00828d14 bytes f847f197
+ 00828d6c bytes f247f197
- 00828d94 ["INT_ADD", "register:40f0:8", ["const:828d94:8", "const:4:8"]]
- 00828d94 ["CALL", null, ["callee:008bad20:8"]]
+ 00828dec ["INT_ADD", "register:40f0:8", ["const:828dec:8", "const:4:8"]]
+ 00828dec ["CALL", null, ["callee:008bad20:8"]]
- 00828d94 bytes cd470294
+ 00828dec bytes cd470294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3a35f4cf31f29e628992fa883b442f1"></a>

### [`0082907c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md) → [`008290d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008290d4.md) FUN_008290d4

採用 · 移動量 `+0x58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00828bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00828/00828bdc.md) [`008312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008208dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/008208dc.md) [`00830274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830274.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00828c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00828/00828c34.md) [`0083134c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md) · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00820934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820934.md) [`008302cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008302cc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082911c",
      "incomplete_value": true,
      "site": "0082912c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:12d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008290c4",
      "incomplete_value": true,
      "site": "008290d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fe:8"
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
      "definition_site": "00829120",
      "incomplete_value": true,
      "site": "00829130",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008290c8",
      "incomplete_value": true,
      "site": "008290d8",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00829124",
      "incomplete_value": true,
      "site": "00829134",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008290cc",
      "incomplete_value": true,
      "site": "008290dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0082911c",
      "READ",
      [
        "storage",
        "002a90fe",
        null,
        "string"
      ]
    ],
    [
      "00829120",
      "READ",
      [
        "storage",
        "002a910e",
        null,
        "string"
      ]
    ],
    [
      "00829124",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0082911c",
      "READ",
      [
        "storage",
        "002a912d",
        null,
        "string"
      ]
    ],
    [
      "00829120",
      "READ",
      [
        "storage",
        "002a913d",
        null,
        "string"
      ]
    ],
    [
      "00829124",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00829134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md#insn-00829134) · [`008290b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md#insn-008290b4) · [`008290bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md#insn-008290bc)
- 新版 `0082918c`（命令位置の公開資料なし） · `0082910c`（命令位置の公開資料なし） · `00829114`（命令位置の公開資料なし）

~~~diff
- 00829134 ["INT_ADD", "register:40f0:8", ["const:829134:8", "const:4:8"]]
- 00829134 ["CALL", null, ["callee:00c57f80:8"]]
+ 0082918c ["INT_ADD", "register:40f0:8", ["const:82918c:8", "const:4:8"]]
+ 0082918c ["CALL", null, ["callee:00c57f80:8"]]
- 00829134 bytes 5fbb1094
+ 0082918c bytes 7dbb1094
- 008290b4 ["INT_ADD", "register:40f0:8", ["const:8290b4:8", "const:4:8"]]
- 008290b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0082910c ["INT_ADD", "register:40f0:8", ["const:82910c:8", "const:4:8"]]
+ 0082910c ["CALL", null, ["callee:00c57f60:8"]]
- 008290b4 bytes 77bb1094
+ 0082910c bytes 95bb1094
- 008290bc ["COPY", "tmp:0:8", ["const:fe:8"]]
- 008290bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008290bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008290bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00829114 ["COPY", "tmp:0:8", ["const:12d:8"]]
+ 00829114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00829114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00829114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008290bc bytes 08f90391
+ 00829114 bytes 08b50491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90beec527a749c3d0ebbdcad52507a4"></a>

### [`00829394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md) → [`008293ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008293ec.md) FUN_008293ec

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00828bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00828/00828bdc.md) [`0082be68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082be68.md) [`008312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md) · 呼出先 5件 [`0081cb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081cb88.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) [`008307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`00828c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00828/00828c34.md) [`0082c008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c008.md) [`0083134c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md) · 呼出先 5件 [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md) [`00830664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830664.md) [`00830850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

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
      "site": "008294d4",
      "value": [
        "leaf",
        "ram:81cbe0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082947c",
      "value": [
        "leaf",
        "ram:81cb88:8"
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
      "008294d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cb88"
      ]
    ]
  ],
  "added": [
    [
      "008294d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cbe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082947c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md#insn-0082947c) · [`008293c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md#insn-008293c0) · [`00829410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829394.md#insn-00829410)
- 新版 `008294d4`（命令位置の公開資料なし） · `00829418`（命令位置の公開資料なし） · `00829468`（命令位置の公開資料なし）

~~~diff
- 0082947c ["INT_ADD", "register:40f0:8", ["const:82947c:8", "const:4:8"]]
- 0082947c ["CALL", null, ["ram:81cb88:8"]]
+ 008294d4 ["INT_ADD", "register:40f0:8", ["const:8294d4:8", "const:4:8"]]
+ 008294d4 ["CALL", null, ["ram:81cbe0:8"]]
- 0082947c bytes c3cdff97
+ 008294d4 bytes c3cdff97
- 008293c0 ["INT_ADD", "register:40f0:8", ["const:8293c0:8", "const:4:8"]]
- 008293c0 ["CALL", null, ["callee:00851550:8"]]
+ 00829418 ["INT_ADD", "register:40f0:8", ["const:829418:8", "const:4:8"]]
+ 00829418 ["CALL", null, ["callee:00851550:8"]]
- 008293c0 bytes 4ea00094
+ 00829418 bytes 4ea00094
- 00829410 ["INT_ADD", "register:40f0:8", ["const:829410:8", "const:4:8"]]
- 00829410 ["CALL", null, ["callee:00830850:8"]]
+ 00829468 ["INT_ADD", "register:40f0:8", ["const:829468:8", "const:4:8"]]
+ 00829468 ["CALL", null, ["callee:00830850:8"]]
- 00829410 bytes fa1c0094
+ 00829468 bytes fa1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-861954ed3d5c1ced0448479faf3b18ea"></a>

### [`00829574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) → [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) FUN_008295cc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`0082dda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md) · 呼出先 31件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 2件 [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) [`0082ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082ddfc.md) · 呼出先 31件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c9a8.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.59% / 新版 91.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `call_target` 4件, `store_destination` 17件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00829ad0",
      "incomplete_value": true,
      "site": "00829ae0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00829a78",
      "incomplete_value": true,
      "site": "00829a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d91:8"
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
      "definition_site": "00829b3c",
      "incomplete_value": true,
      "site": "00829b54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00829ae4",
      "incomplete_value": true,
      "site": "00829afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00829c4c",
      "incomplete_value": true,
      "site": "00829c5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00829bf4",
      "incomplete_value": true,
      "site": "00829c04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d91:8"
              ]
            ]
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
      "0082994c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00829960",
      "READ",
      [
        "storage",
        "002b2d91",
        null,
        "string"
      ]
    ],
    [
      "0082997c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d1ac"
      ]
    ]
  ],
  "added": [
    [
      "0082994c",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "00829960",
      "READ",
      [
        "storage",
        "002b2dc2",
        null,
        "string"
      ]
    ],
    [
      "0082997c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d204"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00829924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md#insn-00829924) · [`00829a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md#insn-00829a94) · [`00829b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md#insn-00829b40)
- 新版 `0082997c`（命令位置の公開資料なし） · `00829aec`（命令位置の公開資料なし） · `00829b98`（命令位置の公開資料なし）

~~~diff
- 00829924 ["INT_ADD", "register:40f0:8", ["const:829924:8", "const:4:8"]]
- 00829924 ["CALL", null, ["ram:71d1ac:8"]]
+ 0082997c ["INT_ADD", "register:40f0:8", ["const:82997c:8", "const:4:8"]]
+ 0082997c ["CALL", null, ["ram:71d204:8"]]
- 00829924 bytes 22cefb97
+ 0082997c bytes 22cefb97
- 00829a94 ["INT_ADD", "register:40f0:8", ["const:829a94:8", "const:4:8"]]
- 00829a94 ["CALL", null, ["ram:71d1ac:8"]]
+ 00829aec ["INT_ADD", "register:40f0:8", ["const:829aec:8", "const:4:8"]]
+ 00829aec ["CALL", null, ["ram:71d204:8"]]
- 00829a94 bytes c6cdfb97
+ 00829aec bytes c6cdfb97
- 00829b40 ["INT_ADD", "register:40f0:8", ["const:829b40:8", "const:4:8"]]
- 00829b40 ["CALL", null, ["callee:0047e64c:8"]]
+ 00829b98 ["INT_ADD", "register:40f0:8", ["const:829b98:8", "const:4:8"]]
+ 00829b98 ["CALL", null, ["callee:0047e64c:8"]]
- 00829b40 bytes b352f197
+ 00829b98 bytes ad52f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109c66b9aaadf9b682ec00d0bcb2a5aa"></a>

### [`0082a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md) → [`0082a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082a7f8.md) FUN_0082a7f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00829574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) [`0082dda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md) · 呼出先 9件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`007286d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/007286d8.md) [`00728750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728750.md) [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) [`0082ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082ddfc.md) · 呼出先 9件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00728730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728730.md) [`007287a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/007287a8.md) [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.45% / 新版 99.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0082a940",
      "incomplete_value": false,
      "site": "0082a944",
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
      "definition_site": "0082a8e8",
      "incomplete_value": false,
      "site": "0082a8ec",
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
      "0082a940",
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
      "0082a940",
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


#### 変更候補の命令位置

- 旧版 [`0082a8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md#insn-0082a8ec) · [`0082a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md#insn-0082a808) · [`0082a85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082a7a0.md#insn-0082a85c)
- 新版 `0082a944`（命令位置の公開資料なし） · `0082a860`（命令位置の公開資料なし） · `0082a8b4`（命令位置の公開資料なし）

~~~diff
- 0082a8ec ["INT_ADD", "register:40f0:8", ["const:82a8ec:8", "const:4:8"]]
- 0082a8ec ["CALL", null, ["callee:00442970:8"]]
+ 0082a944 ["INT_ADD", "register:40f0:8", ["const:82a944:8", "const:4:8"]]
+ 0082a944 ["CALL", null, ["callee:00442970:8"]]
- 0082a8ec bytes 1160f097
+ 0082a944 bytes 0b60f097
- 0082a808 ["INT_ADD", "register:40f0:8", ["const:82a808:8", "const:4:8"]]
- 0082a808 ["CALL", null, ["callee:00851550:8"]]
+ 0082a860 ["INT_ADD", "register:40f0:8", ["const:82a860:8", "const:4:8"]]
+ 0082a860 ["CALL", null, ["callee:00851550:8"]]
- 0082a808 bytes 3c9b0094
+ 0082a860 bytes 3c9b0094
- 0082a85c ["INT_ADD", "register:40f0:8", ["const:82a85c:8", "const:4:8"]]
- 0082a85c ["CALL", null, ["callee:00851550:8"]]
+ 0082a8b4 ["INT_ADD", "register:40f0:8", ["const:82a8b4:8", "const:4:8"]]
+ 0082a8b4 ["CALL", null, ["callee:00851550:8"]]
- 0082a85c bytes 279b0094
+ 0082a8b4 bytes 279b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d059c3b166b85775989da3e26b7f2e1"></a>

### [`0082ac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md) → [`0082acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082acc0.md) FUN_0082acc0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) · 呼出先 26件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)
- 新版 呼出元 1件 [`0082d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d800.md) · 呼出先 26件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082b1d4",
      "incomplete_value": true,
      "site": "0082b1d4",
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
      "definition_site": "0082b17c",
      "incomplete_value": true,
      "site": "0082b17c",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0082ad04",
      "incomplete_value": true,
      "site": "0082ad04",
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
      "definition_site": "0082acac",
      "incomplete_value": true,
      "site": "0082acac",
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
      "definition_site": "0082ad0c",
      "incomplete_value": false,
      "site": "0082ad20",
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
      "definition_site": "0082acb4",
      "incomplete_value": false,
      "site": "0082acc8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082ad00",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082ad0c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082ad14",
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
      "0082ad00",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082ad0c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082ad14",
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


#### 変更候補の命令位置

- 旧版 [`0082acc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md#insn-0082acc8) · [`0082b124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md#insn-0082b124) · [`0082aca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082ac68.md#insn-0082aca8)
- 新版 `0082ad20`（命令位置の公開資料なし） · `0082b17c`（命令位置の公開資料なし） · `0082ad00`（命令位置の公開資料なし）

~~~diff
- 0082acc8 ["INT_ADD", "register:40f0:8", ["const:82acc8:8", "const:4:8"]]
- 0082acc8 ["CALL", null, ["callee:00c586e0:8"]]
+ 0082ad20 ["INT_ADD", "register:40f0:8", ["const:82ad20:8", "const:4:8"]]
+ 0082ad20 ["CALL", null, ["callee:00c586e0:8"]]
- 0082acc8 bytes 52b61094
+ 0082ad20 bytes 70b61094
- 0082b124 ["INT_ADD", "register:40f0:8", ["const:82b124:8", "const:4:8"]]
- 0082b124 ["CALL", null, ["callee:00851550:8"]]
+ 0082b17c ["INT_ADD", "register:40f0:8", ["const:82b17c:8", "const:4:8"]]
+ 0082b17c ["CALL", null, ["callee:00851550:8"]]
- 0082b124 bytes f5980094
+ 0082b17c bytes f5980094
- 0082aca8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 0082aca8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082ad00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0082ad00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0082aca8 bytes 08bd44f9
+ 0082ad00 bytes 083d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac82c5a07dd792684743bf23f0e0280"></a>

### [`0082b620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b620.md) → [`0082b678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082b678.md) FUN_0082b678

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) · 呼出先 13件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00831d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d38.md) [`00831d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d3c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) · 呼出先 13件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00831d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d90.md) [`00831d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.45% / 新版 90.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082b7d4",
      "incomplete_value": false,
      "site": "0082b7d4",
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
      "definition_site": "0082b77c",
      "incomplete_value": false,
      "site": "0082b77c",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082b85c",
      "incomplete_value": true,
      "site": "0082b85c",
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
      "definition_site": "0082b804",
      "incomplete_value": true,
      "site": "0082b804",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0082b6b8",
      "incomplete_value": true,
      "site": "0082b6b8",
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
      "definition_site": "0082b660",
      "incomplete_value": true,
      "site": "0082b660",
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
      "0082b6b4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082b6c0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082b6c8",
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
      "0082b6b4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082b6c0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082b6c8",
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


#### 変更候補の命令位置

- 旧版 [`0082b67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b620.md#insn-0082b67c) · [`0082b65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b620.md#insn-0082b65c) · [`0082b668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b620.md#insn-0082b668)
- 新版 `0082b6d4`（命令位置の公開資料なし） · `0082b6b4`（命令位置の公開資料なし） · `0082b6c0`（命令位置の公開資料なし）

~~~diff
- 0082b67c ["INT_ADD", "register:40f0:8", ["const:82b67c:8", "const:4:8"]]
- 0082b67c ["CALL", null, ["callee:00c586e0:8"]]
+ 0082b6d4 ["INT_ADD", "register:40f0:8", ["const:82b6d4:8", "const:4:8"]]
+ 0082b6d4 ["CALL", null, ["callee:00c586e0:8"]]
- 0082b67c bytes e5b31094
+ 0082b6d4 bytes 03b41094
- 0082b65c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 0082b65c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082b6b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0082b6b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0082b65c bytes 08bd44f9
+ 0082b6b4 bytes 083d45f9
- 0082b668 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0082b668 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0082b668 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0082b668 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0082b6c0 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0082b6c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0082b6c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0082b6c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0082b668 bytes 21603991
+ 0082b6c0 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52cf0ea725768382076b87f5fa7a87cd"></a>

### [`0082b900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b900.md) → [`0082b958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082b958.md) FUN_0082b958

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) · 呼出先 16件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00831edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831edc.md) [`00831ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) · 呼出先 16件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00831f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f34.md) [`00831f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082bb10",
      "incomplete_value": false,
      "site": "0082bb10",
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
      "definition_site": "0082bab8",
      "incomplete_value": false,
      "site": "0082bab8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0082b98c",
      "incomplete_value": true,
      "site": "0082b98c",
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
      "definition_site": "0082b934",
      "incomplete_value": true,
      "site": "0082b934",
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
      "definition_site": "0082b994",
      "incomplete_value": false,
      "site": "0082b9a8",
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
      "definition_site": "0082b93c",
      "incomplete_value": false,
      "site": "0082b950",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082b988",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082b994",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082b99c",
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
      "0082b988",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082b994",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082b99c",
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


#### 変更候補の命令位置

- 旧版 [`0082b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b900.md#insn-0082b950) · [`0082b9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b900.md#insn-0082b9a8) · [`0082b930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b900.md#insn-0082b930)
- 新版 `0082b9a8`（命令位置の公開資料なし） · `0082ba00`（命令位置の公開資料なし） · `0082b988`（命令位置の公開資料なし）

~~~diff
- 0082b950 ["INT_ADD", "register:40f0:8", ["const:82b950:8", "const:4:8"]]
- 0082b950 ["CALL", null, ["callee:00c586e0:8"]]
+ 0082b9a8 ["INT_ADD", "register:40f0:8", ["const:82b9a8:8", "const:4:8"]]
+ 0082b9a8 ["CALL", null, ["callee:00c586e0:8"]]
- 0082b950 bytes 30b31094
+ 0082b9a8 bytes 4eb31094
- 0082b9a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0082b9a8 ["INT_ADD", "register:40f0:8", ["const:82b9a8:8", "const:4:8"]]
- 0082b9a8 ["CALLIND", null, ["register:0:8"]]
+ 0082ba00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082ba00 ["INT_ADD", "register:40f0:8", ["const:82ba00:8", "const:4:8"]]
+ 0082ba00 ["CALLIND", null, ["register:0:8"]]
- 0082b9a8 bytes 00013fd6
+ 0082ba00 bytes 00013fd6
- 0082b930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 0082b930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082b988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0082b988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0082b930 bytes 08bd44f9
+ 0082b988 bytes 083d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1d10c1c6335b67d518671c69ed61eae"></a>

### [`0082bc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082bc58.md) → [`0082bcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082bcb0.md) FUN_0082bcb0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) · 呼出先 12件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00831fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fec.md) [`00831ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)
- 新版 呼出元 1件 [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) · 呼出先 12件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00832044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832044.md) [`00832048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832048.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7044.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.52% / 新版 92.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082bd44",
      "incomplete_value": false,
      "site": "0082bd44",
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
      "definition_site": "0082bcec",
      "incomplete_value": false,
      "site": "0082bcec",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0082bde8",
      "incomplete_value": false,
      "site": "0082bdec",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "0082bd90",
      "incomplete_value": false,
      "site": "0082bd94",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0082bcf0",
      "incomplete_value": true,
      "site": "0082bcf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0082bc98",
      "incomplete_value": true,
      "site": "0082bc9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0082bcd0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082bcdc",
      "PARAM",
      [
        "storage",
        "00c7e510",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082bcec",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0082bcd0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082bcdc",
      "PARAM",
      [
        "storage",
        "00c7e5e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082bcec",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082bc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082bc58.md#insn-0082bc94) · [`0082bc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082bc58.md#insn-0082bc9c) · [`0082bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082bc58.md#insn-0082bc78)
- 新版 `0082bcec`（命令位置の公開資料なし） · `0082bcf4`（命令位置の公開資料なし） · `0082bcd0`（命令位置の公開資料なし）

~~~diff
- 0082bc94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 0082bc94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082bcec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0082bcec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0082bc94 bytes 08bd44f9
+ 0082bcec bytes 083d45f9
- 0082bc9c ["INT_ADD", "register:40f0:8", ["const:82bc9c:8", "const:4:8"]]
- 0082bc9c ["CALL", null, ["callee:00c586e0:8"]]
+ 0082bcf4 ["INT_ADD", "register:40f0:8", ["const:82bcf4:8", "const:4:8"]]
+ 0082bcf4 ["CALL", null, ["callee:00c586e0:8"]]
- 0082bc9c bytes 5db21094
+ 0082bcf4 bytes 7bb21094
- 0082bc78 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0082bc78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0082bc78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0082bc78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0082bcd0 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0082bcd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0082bcd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0082bcd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0082bc78 bytes 21603991
+ 0082bcd0 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62b5a9ade2e0fe259f8915a9fdd1c45"></a>

### [`0082c384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c384.md) → [`0082c3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c3dc.md) FUN_0082c3dc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) · 呼出先 5件 [`0081cb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081cb88.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md) [`008307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008307f8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) · 呼出先 5件 [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md) [`00830664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830664.md) [`00830850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830850.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.84% / 新版 97.84%

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
      "site": "0082c4e8",
      "value": [
        "leaf",
        "ram:81cbe0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082c490",
      "value": [
        "leaf",
        "ram:81cb88:8"
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
      "0082c4e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cb88"
      ]
    ],
    [
      "0082c5d0",
      "READ",
      [
        "storage",
        "002c3230",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0082c4e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cbe0"
      ]
    ],
    [
      "0082c5d0",
      "READ",
      [
        "storage",
        "002c3270",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082c490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c384.md#insn-0082c490) · [`0082c3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c384.md#insn-0082c3e8) · [`0082c3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c384.md#insn-0082c3f8)
- 新版 `0082c4e8`（命令位置の公開資料なし） · `0082c440`（命令位置の公開資料なし） · `0082c450`（命令位置の公開資料なし）

~~~diff
- 0082c490 ["INT_ADD", "register:40f0:8", ["const:82c490:8", "const:4:8"]]
- 0082c490 ["CALL", null, ["ram:81cb88:8"]]
+ 0082c4e8 ["INT_ADD", "register:40f0:8", ["const:82c4e8:8", "const:4:8"]]
+ 0082c4e8 ["CALL", null, ["ram:81cbe0:8"]]
- 0082c490 bytes bec1ff97
+ 0082c4e8 bytes bec1ff97
- 0082c3e8 ["INT_ADD", "register:40f0:8", ["const:82c3e8:8", "const:4:8"]]
- 0082c3e8 ["CALL", null, ["callee:00830664:8"]]
+ 0082c440 ["INT_ADD", "register:40f0:8", ["const:82c440:8", "const:4:8"]]
+ 0082c440 ["CALL", null, ["callee:00830664:8"]]
- 0082c3e8 bytes 89100094
+ 0082c440 bytes 89100094
- 0082c3f8 ["INT_ADD", "register:40f0:8", ["const:82c3f8:8", "const:4:8"]]
- 0082c3f8 ["CALL", null, ["callee:00851550:8"]]
+ 0082c450 ["INT_ADD", "register:40f0:8", ["const:82c450:8", "const:4:8"]]
+ 0082c450 ["CALL", null, ["callee:00851550:8"]]
- 0082c3f8 bytes 40940094
+ 0082c450 bytes 40940094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27e5af0c448a84b139158be5fc945bcd"></a>

### [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) → [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) FUN_0082c734

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) · 呼出先 9件 [`0081cb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081cb88.md) [`0082b620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b620.md) [`0082b900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082b900.md) [`0082bc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082bc58.md) [`0082be68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082b/0082be68.md)
- 新版 呼出元 1件 [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) · 呼出先 9件 [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md) [`0082b678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082b678.md) [`0082b958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082b958.md) [`0082bcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082bcb0.md) [`0082bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082bec0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.96% / 新版 97.96%

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
      "site": "0082c790",
      "value": [
        "leaf",
        "ram:82bec0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082c738",
      "value": [
        "leaf",
        "ram:82be68:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082c83c",
      "value": [
        "leaf",
        "ram:81cbe0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082c7e4",
      "value": [
        "leaf",
        "ram:81cb88:8"
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
      "0082c790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082be68"
      ]
    ],
    [
      "0082c83c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cb88"
      ]
    ]
  ],
  "added": [
    [
      "0082c790",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082bec0"
      ]
    ],
    [
      "0082c83c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cbe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082c738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md#insn-0082c738) · [`0082c7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md#insn-0082c7e4) · [`0082c6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md#insn-0082c6fc)
- 新版 `0082c790`（命令位置の公開資料なし） · `0082c83c`（命令位置の公開資料なし） · `0082c754`（命令位置の公開資料なし）

~~~diff
- 0082c738 ["INT_ADD", "register:40f0:8", ["const:82c738:8", "const:4:8"]]
- 0082c738 ["CALL", null, ["ram:82be68:8"]]
+ 0082c790 ["INT_ADD", "register:40f0:8", ["const:82c790:8", "const:4:8"]]
+ 0082c790 ["CALL", null, ["ram:82bec0:8"]]
- 0082c738 bytes ccfdff97
+ 0082c790 bytes ccfdff97
- 0082c7e4 ["INT_ADD", "register:40f0:8", ["const:82c7e4:8", "const:4:8"]]
- 0082c7e4 ["CALL", null, ["ram:81cb88:8"]]
+ 0082c83c ["INT_ADD", "register:40f0:8", ["const:82c83c:8", "const:4:8"]]
+ 0082c83c ["CALL", null, ["ram:81cbe0:8"]]
- 0082c7e4 bytes e9c0ff97
+ 0082c83c bytes e9c0ff97
- 0082c6fc ["INT_ADD", "register:40f0:8", ["const:82c6fc:8", "const:4:8"]]
- 0082c6fc ["CALL", null, ["callee:00851550:8"]]
+ 0082c754 ["INT_ADD", "register:40f0:8", ["const:82c754:8", "const:4:8"]]
+ 0082c754 ["CALL", null, ["callee:00851550:8"]]
- 0082c6fc bytes 7f930094
+ 0082c754 bytes 7f930094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77b4c35cf34a388b040fd8772eaeecb0"></a>

### [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) → [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) FUN_0082c8bc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) [`00831d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d40.md) [`00831ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee4.md) · 呼出先 16件 [`0081cb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081cb88.md) [`0082aa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082a/0082aa78.md) [`0082c5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c5e0.md) [`0082dda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082dda4.md) [`0083060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083060c.md)
- 新版 呼出元 3件 [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) [`00831d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md) [`00831f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md) · 呼出先 16件 [`0081cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081cbe0.md) [`0082aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082aad0.md) [`0082c638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c638.md) [`0082ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082ddfc.md) [`00830664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830664.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.25% / 新版 99.25%

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
      "site": "0082ca7c",
      "value": [
        "leaf",
        "ram:81cbe0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082ca24",
      "value": [
        "leaf",
        "ram:81cb88:8"
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
      "0082ca7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cb88"
      ]
    ],
    [
      "0082cbf8",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "0082cc00",
      "PARAM",
      [
        "storage",
        "003104a1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0082ca7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cbe0"
      ]
    ],
    [
      "0082cbf8",
      "READ",
      [
        "storage",
        "00c9b5f0",
        null,
        "pointer"
      ]
    ],
    [
      "0082cc00",
      "PARAM",
      [
        "storage",
        "003104e1",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082ca24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md#insn-0082ca24) · [`0082c8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md#insn-0082c8ec) · [`0082c934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md#insn-0082c934)
- 新版 `0082ca7c`（命令位置の公開資料なし） · `0082c944`（命令位置の公開資料なし） · `0082c98c`（命令位置の公開資料なし）

~~~diff
- 0082ca24 ["INT_ADD", "register:40f0:8", ["const:82ca24:8", "const:4:8"]]
- 0082ca24 ["CALL", null, ["ram:81cb88:8"]]
+ 0082ca7c ["INT_ADD", "register:40f0:8", ["const:82ca7c:8", "const:4:8"]]
+ 0082ca7c ["CALL", null, ["ram:81cbe0:8"]]
- 0082ca24 bytes 59c0ff97
+ 0082ca7c bytes 59c0ff97
- 0082c8ec ["INT_ADD", "register:40f0:8", ["const:82c8ec:8", "const:4:8"]]
- 0082c8ec ["CALL", null, ["callee:0082aad0:8"]]
+ 0082c944 ["INT_ADD", "register:40f0:8", ["const:82c944:8", "const:4:8"]]
+ 0082c944 ["CALL", null, ["callee:0082aad0:8"]]
- 0082c8ec bytes 63f8ff97
+ 0082c944 bytes 63f8ff97
- 0082c934 ["INT_ADD", "register:40f0:8", ["const:82c934:8", "const:4:8"]]
- 0082c934 ["CALL", null, ["callee:00c53da0:8"]]
+ 0082c98c ["INT_ADD", "register:40f0:8", ["const:82c98c:8", "const:4:8"]]
+ 0082c98c ["CALL", null, ["callee:00c53da0:8"]]
- 0082c934 bytes f39c1094
+ 0082c98c bytes 059d1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9a8ce001784a1cc1cc2da09edbfabc6"></a>

### [`0082d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md) → [`0082d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d800.md) FUN_0082d800

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) · 呼出先 16件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0081c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c2f4.md)
- 新版 呼出元 1件 [`0082fbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082fbc4.md) · 呼出先 16件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`004690a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/004690a8.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0081c34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c34c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.49% / 新版 98.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0082d8b8",
      "incomplete_value": true,
      "site": "0082d8b8",
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
      "definition_site": "0082d860",
      "incomplete_value": true,
      "site": "0082d860",
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
      "definition_site": "0082d8c0",
      "incomplete_value": false,
      "site": "0082d8d0",
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
      "definition_site": "0082d868",
      "incomplete_value": false,
      "site": "0082d878",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0082d8c8",
      "incomplete_value": false,
      "site": "0082d8d0",
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
      "definition_site": "0082d870",
      "incomplete_value": false,
      "site": "0082d878",
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
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082d8b4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082d8c0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082d8c8",
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
      "0082d8b4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082d8c0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082d8c8",
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


#### 変更候補の命令位置

- 旧版 [`0082d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md#insn-0082d878) · [`0082d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md#insn-0082d8d0) · [`0082db58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d7a8.md#insn-0082db58)
- 新版 `0082d8d0`（命令位置の公開資料なし） · `0082d928`（命令位置の公開資料なし） · `0082dbb0`（命令位置の公開資料なし）

~~~diff
- 0082d878 ["INT_ADD", "register:40f0:8", ["const:82d878:8", "const:4:8"]]
- 0082d878 ["CALL", null, ["callee:00c586e0:8"]]
+ 0082d8d0 ["INT_ADD", "register:40f0:8", ["const:82d8d0:8", "const:4:8"]]
+ 0082d8d0 ["CALL", null, ["callee:00c586e0:8"]]
- 0082d878 bytes 66ab1094
+ 0082d8d0 bytes 84ab1094
- 0082d8d0 ["INT_ADD", "register:40f0:8", ["const:82d8d0:8", "const:4:8"]]
- 0082d8d0 ["CALL", null, ["callee:004690a8:8"]]
+ 0082d928 ["INT_ADD", "register:40f0:8", ["const:82d928:8", "const:4:8"]]
+ 0082d928 ["CALL", null, ["callee:004690a8:8"]]
- 0082d8d0 bytes e6edf097
+ 0082d928 bytes e0edf097
- 0082db58 ["INT_ADD", "register:40f0:8", ["const:82db58:8", "const:4:8"]]
- 0082db58 ["CALL", null, ["ram:81cb88:8"]]
+ 0082dbb0 ["INT_ADD", "register:40f0:8", ["const:82dbb0:8", "const:4:8"]]
+ 0082dbb0 ["CALL", null, ["ram:81cbe0:8"]]
- 0082db58 bytes 0cbcff97
+ 0082dbb0 bytes 0cbcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e009fce82465ce126008e586214a5ba"></a>

### [`0082df60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df60.md) → [`0082dfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082dfb8.md) FUN_0082dfb8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 20件 [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e778.md) [`0046e788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e788.md) [`0046ed8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ed8c.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 20件 [`0046e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b0.md) [`0046e7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b8.md) [`0046e7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7c8.md) [`0046edcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046edcc.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082e108",
      "incomplete_value": true,
      "site": "0082e11c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082e0b0",
      "incomplete_value": true,
      "site": "0082e0c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee9:8"
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
      "definition_site": "0082e0b4",
      "incomplete_value": true,
      "site": "0082e0b4",
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
      "definition_site": "0082e05c",
      "incomplete_value": true,
      "site": "0082e05c",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082dfe0",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082df88",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "0082dfe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0082e0b0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082e0bc",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0082dfe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0082e0b0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082e0bc",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082df88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df60.md#insn-0082df88) · [`0082e028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df60.md#insn-0082e028) · [`0082e06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df60.md#insn-0082e06c)
- 新版 `0082dfe0`（命令位置の公開資料なし） · `0082e080`（命令位置の公開資料なし） · `0082e0c4`（命令位置の公開資料なし）

~~~diff
- 0082df88 ["INT_ADD", "register:40f0:8", ["const:82df88:8", "const:4:8"]]
- 0082df88 ["CALL", null, ["ram:48ccf8:8"]]
+ 0082dfe0 ["INT_ADD", "register:40f0:8", ["const:82dfe0:8", "const:4:8"]]
+ 0082dfe0 ["CALL", null, ["ram:48cd38:8"]]
- 0082df88 bytes 5c7bf197
+ 0082dfe0 bytes 567bf197
- 0082e028 ["INT_ADD", "register:40f0:8", ["const:82e028:8", "const:4:8"]]
- 0082e028 ["CALL", null, ["callee:00851550:8"]]
+ 0082e080 ["INT_ADD", "register:40f0:8", ["const:82e080:8", "const:4:8"]]
+ 0082e080 ["CALL", null, ["callee:00851550:8"]]
- 0082e028 bytes 348d0094
+ 0082e080 bytes 348d0094
- 0082e06c ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0082e06c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0082e06c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0082e06c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0082e0c4 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0082e0c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0082e0c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0082e0c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0082e06c bytes 42a03991
+ 0082e0c4 bytes 42e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8792ab43051c678cd097fe66083d44c"></a>

### [`0082e320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082e320.md) → [`0082e378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082e378.md) FUN_0082e378

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0082df60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082df60.md) [`00b3cad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3cad8.md) · 呼出先 17件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md)
- 新版 呼出元 2件 [`0082dfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082dfb8.md) [`00b3cb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3cb74.md) · 呼出先 17件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082e3d4",
      "incomplete_value": true,
      "site": "0082e3ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:948:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082e37c",
      "incomplete_value": true,
      "site": "0082e394",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a4:8"
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
      "definition_site": "0082e3f4",
      "incomplete_value": true,
      "site": "0082e404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082e39c",
      "incomplete_value": true,
      "site": "0082e3ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b15:8"
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
      "definition_site": "0082e4f8",
      "incomplete_value": true,
      "site": "0082e4f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082e4a0",
      "incomplete_value": true,
      "site": "0082e4a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:847:8"
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
      "0082e3b8",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0082e3d4",
      "READ",
      [
        "storage",
        "002ab9a4",
        null,
        "string"
      ]
    ],
    [
      "0082e3f4",
      "READ",
      [
        "storage",
        "002adb15",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0082e3b8",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "0082e3d4",
      "READ",
      [
        "storage",
        "002ab948",
        null,
        "string"
      ]
    ],
    [
      "0082e3f4",
      "READ",
      [
        "storage",
        "002adab9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082e354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082e320.md#insn-0082e354) · [`0082e404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082e320.md#insn-0082e404) · [`0082e688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082e320.md#insn-0082e688)
- 新版 `0082e3ac`（命令位置の公開資料なし） · `0082e45c`（命令位置の公開資料なし） · `0082e6e0`（命令位置の公開資料なし）

~~~diff
- 0082e354 ["COPY", "register:40c8:8", ["const:ca4000:8"]]
+ 0082e3ac ["COPY", "register:40c8:8", ["const:ca5000:8"]]
- 0082e354 bytes b92300d0
+ 0082e3ac bytes b92300f0
- 0082e404 ["COPY", "register:0:8", ["register:4040:8"]]
- 0082e404 ["INT_ADD", "register:40f0:8", ["const:82e404:8", "const:4:8"]]
- 0082e404 ["CALLIND", null, ["register:0:8"]]
+ 0082e45c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0082e45c ["INT_ADD", "register:40f0:8", ["const:82e45c:8", "const:4:8"]]
+ 0082e45c ["CALLIND", null, ["register:0:8"]]
- 0082e404 bytes 00013fd6
+ 0082e45c bytes 00013fd6
- 0082e688 ["INT_ADD", "register:40f0:8", ["const:82e688:8", "const:4:8"]]
- 0082e688 ["CALL", null, ["callee:0047e91c:8"]]
+ 0082e6e0 ["INT_ADD", "register:40f0:8", ["const:82e6e0:8", "const:4:8"]]
+ 0082e6e0 ["CALL", null, ["callee:0047e91c:8"]]
- 0082e688 bytes 9540f197
+ 0082e6e0 bytes 8f40f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b669f72dc5efd492012b26d46af0c2f2"></a>

### [`0082ea48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ea48.md) → [`0082eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082eaa0.md) FUN_0082eaa0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 9件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md)
- 新版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 9件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "0082eab0",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0082ea58",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "0082eab0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0082ead8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082eadc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0082eab0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0082ead8",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082eadc",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082ea58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ea48.md#insn-0082ea58) · [`0082ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ea48.md#insn-0082ea5c) · [`0082ea70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ea48.md#insn-0082ea70)
- 新版 `0082eab0`（命令位置の公開資料なし） · `0082eab4`（命令位置の公開資料なし） · `0082eac8`（命令位置の公開資料なし）

~~~diff
- 0082ea58 ["INT_ADD", "register:40f0:8", ["const:82ea58:8", "const:4:8"]]
- 0082ea58 ["CALL", null, ["ram:48ccf8:8"]]
+ 0082eab0 ["INT_ADD", "register:40f0:8", ["const:82eab0:8", "const:4:8"]]
+ 0082eab0 ["CALL", null, ["ram:48cd38:8"]]
- 0082ea58 bytes a878f197
+ 0082eab0 bytes a278f197
- 0082ea5c ["INT_ADD", "register:40f0:8", ["const:82ea5c:8", "const:4:8"]]
- 0082ea5c ["CALL", null, ["callee:0048dc8c:8"]]
+ 0082eab4 ["INT_ADD", "register:40f0:8", ["const:82eab4:8", "const:4:8"]]
+ 0082eab4 ["CALL", null, ["callee:0048dc8c:8"]]
- 0082ea5c bytes 7c7cf197
+ 0082eab4 bytes 767cf197
- 0082ea70 ["INT_ADD", "register:40f0:8", ["const:82ea70:8", "const:4:8"]]
- 0082ea70 ["CALL", null, ["callee:004678a0:8"]]
+ 0082eac8 ["INT_ADD", "register:40f0:8", ["const:82eac8:8", "const:4:8"]]
+ 0082eac8 ["CALL", null, ["callee:004678a0:8"]]
- 0082ea70 bytes 7ce3f097
+ 0082eac8 bytes 76e3f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300a146c08c7e11d887dc298d0741e85"></a>

### [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) → [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) FUN_0082ee78

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 23件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) [`008378d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md) [`00838a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a6c.md) [`00838a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a70.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 23件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0082c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c734.md) [`00837930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md) [`00838ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ac4.md) [`00838ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ac8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.35% / 新版 89.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0082eeb4",
      "incomplete_value": false,
      "site": "0082eeb4",
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
      "definition_site": "0082ee5c",
      "incomplete_value": false,
      "site": "0082ee5c",
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082eeac",
      "incomplete_value": true,
      "site": "0082eeb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0082ee54",
      "incomplete_value": true,
      "site": "0082ee5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0082eeb8",
      "incomplete_value": false,
      "site": "0082eeb8",
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
      "definition_site": "0082ee60",
      "incomplete_value": false,
      "site": "0082ee60",
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
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082eeac",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082eeb0",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "0082eeb4",
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
      "0082eeac",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082eeb0",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "0082eeb4",
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


#### 変更候補の命令位置

- 旧版 [`0082ee54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md#insn-0082ee54) · [`0082ee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md#insn-0082ee5c) · [`0082ee60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md#insn-0082ee60)
- 新版 `0082eeac`（命令位置の公開資料なし） · `0082eeb4`（命令位置の公開資料なし） · `0082eeb8`（命令位置の公開資料なし）

~~~diff
- 0082ee54 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
- 0082ee54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082eeac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 0082eeac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0082ee54 bytes c9be44f9
+ 0082eeac bytes c93e45f9
- 0082ee5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
- 0082ee5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0082eeb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 0082eeb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0082ee5c bytes 09b504f9
+ 0082eeb4 bytes 093505f9
- 0082ee60 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
- 0082ee60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0082eeb8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 0082eeb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0082ee60 bytes cabe04f9
+ 0082eeb8 bytes ca3e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3785723033f3ad5ec5e16c8b0def3a65"></a>

### [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) → [`0082f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082f180.md) FUN_0082f180

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044c25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc4c.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c29c.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dc8c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0082f228",
      "incomplete_value": true,
      "site": "0082f228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f1d0",
      "incomplete_value": true,
      "site": "0082f1d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b2:8"
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
      "definition_site": "0082f410",
      "incomplete_value": true,
      "site": "0082f410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f3b8",
      "incomplete_value": true,
      "site": "0082f3b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b2:8"
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
      "definition_site": "0082f454",
      "incomplete_value": true,
      "site": "0082f454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0082f3fc",
      "incomplete_value": true,
      "site": "0082f3fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0082f1e0",
      "DATA",
      [
        "storage",
        "0039b8c4",
        "fde_0039b8c4",
        "dword"
      ]
    ],
    [
      "0082f204",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0082f214",
      "READ",
      [
        "storage",
        "002b85b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0082f1e0",
      "DATA",
      [
        "storage",
        "0039b8c4",
        null,
        "qword"
      ]
    ],
    [
      "0082f204",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0082f214",
      "READ",
      [
        "storage",
        "002b855e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0082f1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md#insn-0082f1ac) · [`0082f230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md#insn-0082f230) · [`0082f288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md#insn-0082f288)
- 新版 `0082f204`（命令位置の公開資料なし） · `0082f288`（命令位置の公開資料なし） · `0082f2e0`（命令位置の公開資料なし）

~~~diff
- 0082f1ac ["INT_ADD", "register:40f0:8", ["const:82f1ac:8", "const:4:8"]]
- 0082f1ac ["CALL", null, ["ram:48ccf8:8"]]
+ 0082f204 ["INT_ADD", "register:40f0:8", ["const:82f204:8", "const:4:8"]]
+ 0082f204 ["CALL", null, ["ram:48cd38:8"]]
- 0082f1ac bytes d376f197
+ 0082f204 bytes cd76f197
- 0082f230 ["INT_ADD", "register:40f0:8", ["const:82f230:8", "const:4:8"]]
- 0082f230 ["CALL", null, ["ram:48ccf8:8"]]
+ 0082f288 ["INT_ADD", "register:40f0:8", ["const:82f288:8", "const:4:8"]]
+ 0082f288 ["CALL", null, ["ram:48cd38:8"]]
- 0082f230 bytes b276f197
+ 0082f288 bytes ac76f197
- 0082f288 ["INT_ADD", "register:40f0:8", ["const:82f288:8", "const:4:8"]]
- 0082f288 ["CALL", null, ["callee:00c57f80:8"]]
+ 0082f2e0 ["INT_ADD", "register:40f0:8", ["const:82f2e0:8", "const:4:8"]]
+ 0082f2e0 ["CALL", null, ["callee:00c57f80:8"]]
- 0082f288 bytes 0aa31094
+ 0082f2e0 bytes 28a31094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-262b7d5d9d63a2021674db136d86407c"></a>

### [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) → [`0082fbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082fbc4.md) FUN_0082fbc4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 22件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f1c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)
- 新版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 22件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f5c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0082fbe0",
      "incomplete_value": true,
      "site": "0082fbe0",
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
      "definition_site": "0082fb88",
      "incomplete_value": true,
      "site": "0082fb88",
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
      "definition_site": "0082fbf0",
      "incomplete_value": false,
      "site": "0082fc04",
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
      "definition_site": "0082fb98",
      "incomplete_value": false,
      "site": "0082fbac",
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
      "definition_site": "0082fbf8",
      "incomplete_value": false,
      "site": "0082fc04",
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
      "definition_site": "0082fba0",
      "incomplete_value": false,
      "site": "0082fbac",
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
      "0082fbdc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0082fbf0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082fbf8",
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
      "0082fbdc",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0082fbf0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0082fbf8",
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


#### 変更候補の命令位置

- 旧版 [`0082fbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md#insn-0082fbac) · [`0082fb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md#insn-0082fb84) · [`0082fb98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md#insn-0082fb98)
- 新版 `0082fc04`（命令位置の公開資料なし） · `0082fbdc`（命令位置の公開資料なし） · `0082fbf0`（命令位置の公開資料なし）

~~~diff
- 0082fbac ["INT_ADD", "register:40f0:8", ["const:82fbac:8", "const:4:8"]]
- 0082fbac ["CALL", null, ["callee:00c586e0:8"]]
+ 0082fc04 ["INT_ADD", "register:40f0:8", ["const:82fc04:8", "const:4:8"]]
+ 0082fc04 ["CALL", null, ["callee:00c586e0:8"]]
- 0082fbac bytes 99a21094
+ 0082fc04 bytes b7a21094
- 0082fb84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 0082fb84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0082fbdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0082fbdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0082fb84 bytes 08bd44f9
+ 0082fbdc bytes 083d45f9
- 0082fb98 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0082fb98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0082fb98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0082fb98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0082fbf0 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0082fbf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0082fbf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0082fbf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0082fb98 bytes 21603991
+ 0082fbf0 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb35fb3539fa91364955e674e3365975"></a>

### [`0083004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md) → [`008300a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008300a4.md) FUN_008300a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0081a814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081a/0081a814.md) [`0081c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081c550.md) [`0082071c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/0082071c.md) [`0082fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fd6c.md) [`0083069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083069c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 5件 [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`0081c5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081c/0081c5a8.md) [`00820774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/00820774.md) [`0082fdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082fdc4.md) [`008306f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/008306f4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "008300b0",
      "incomplete_value": false,
      "site": "008300b4",
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
      "definition_site": "00830058",
      "incomplete_value": false,
      "site": "0083005c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008300b0",
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
      "008300b0",
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


#### 変更候補の命令位置

- 旧版 [`0083005c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md#insn-0083005c) · [`00830058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/0083004c.md#insn-00830058)
- 新版 `008300b4`（命令位置の公開資料なし） · `008300b0`（命令位置の公開資料なし）

~~~diff
- 0083005c ["INT_ADD", "register:40f0:8", ["const:83005c:8", "const:4:8"]]
- 0083005c ["CALL", null, ["callee:0043b7b8:8"]]
+ 008300b4 ["INT_ADD", "register:40f0:8", ["const:8300b4:8", "const:4:8"]]
+ 008300b4 ["CALL", null, ["callee:0043b7b8:8"]]
- 0083005c bytes c72df097
+ 008300b4 bytes c12df097
- 00830058 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00830058 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00830058 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00830058 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008300b0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 008300b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008300b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008300b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00830058 bytes 00303d91
+ 008300b0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bd70312743ab52671d9c168fb9feb36"></a>

### [`008302f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008302f8.md) → [`00830350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830350.md) FUN_00830350

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00830354",
      "incomplete_value": true,
      "site": "00830358",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008302fc",
      "incomplete_value": true,
      "site": "00830300",
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
            "const:430:8"
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
      "00830358",
      "DATA",
      [
        "storage",
        "00c7e430",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00830358",
      "DATA",
      [
        "storage",
        "00c7e500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008302fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008302f8.md#insn-008302fc)
- 新版 `00830354`（命令位置の公開資料なし）

~~~diff
- 008302fc ["COPY", "tmp:0:8", ["const:430:8"]]
- 008302fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008302fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008302fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830354 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00830354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008302fc bytes 08c11091
+ 00830354 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2e38e530afbd0f9d2d027a8c8da404"></a>

### [`00830400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830400.md) → [`00830458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830458.md) FUN_00830458

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0083045c",
      "incomplete_value": false,
      "site": "00830460",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830404",
      "incomplete_value": false,
      "site": "00830408",
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
            "const:480:8"
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
      "00830460",
      "DATA",
      [
        "storage",
        "00c7e480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00830460",
      "DATA",
      [
        "storage",
        "00c7e550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830400.md#insn-00830404)
- 新版 `0083045c`（命令位置の公開資料なし）

~~~diff
- 00830404 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00830404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083045c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0083045c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083045c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083045c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830404 bytes 08011291
+ 0083045c bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-400d0162d5738d1b6713452c3a20983a"></a>

### [`00830410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830410.md) → [`00830468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830468.md) FUN_00830468

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00830478",
      "incomplete_value": false,
      "site": "00830480",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830420",
      "incomplete_value": false,
      "site": "00830428",
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
            "const:480:8"
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
      "00830480",
      "DATA",
      [
        "storage",
        "00c7e480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00830480",
      "DATA",
      [
        "storage",
        "00c7e550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830410.md#insn-00830420) · [`0083042c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830410.md#insn-0083042c)
- 新版 `00830478`（命令位置の公開資料なし） · `00830484`（命令位置の公開資料なし）

~~~diff
- 00830420 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00830420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830478 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00830478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830420 bytes 08011291
+ 00830478 bytes 08411591
- 0083042c ["INT_ADD", "register:40f0:8", ["const:83042c:8", "const:4:8"]]
- 0083042c ["CALL", null, ["callee:00c57f70:8"]]
+ 00830484 ["INT_ADD", "register:40f0:8", ["const:830484:8", "const:4:8"]]
+ 00830484 ["CALL", null, ["callee:00c57f70:8"]]
- 0083042c bytes 9d9e1094
+ 00830484 bytes bb9e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5347e939b22eaea114aef31d37c1db2"></a>

### [`008305c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008305c4.md) → [`0083061c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083061c.md) FUN_0083061c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00830620",
      "incomplete_value": false,
      "site": "00830624",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008305c8",
      "incomplete_value": false,
      "site": "008305cc",
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
            "const:4d0:8"
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
      "00830624",
      "DATA",
      [
        "storage",
        "00c7e4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830624",
      "DATA",
      [
        "storage",
        "00c7e5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008305c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008305c4.md#insn-008305c8)
- 新版 `00830620`（命令位置の公開資料なし）

~~~diff
- 008305c8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 008305c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008305c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008305c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830620 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00830620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008305c8 bytes 08411391
+ 00830620 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48a8a58510a886a6f5046beb24d00c3"></a>

### [`008305d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008305d4.md) → [`0083062c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/0083062c.md) FUN_0083062c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0083063c",
      "incomplete_value": false,
      "site": "00830644",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008305e4",
      "incomplete_value": false,
      "site": "008305ec",
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
            "const:4d0:8"
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
      "00830644",
      "DATA",
      [
        "storage",
        "00c7e4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830644",
      "DATA",
      [
        "storage",
        "00c7e5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008305e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008305d4.md#insn-008305e4) · [`008305f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/008305d4.md#insn-008305f0)
- 新版 `0083063c`（命令位置の公開資料なし） · `00830648`（命令位置の公開資料なし）

~~~diff
- 008305e4 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 008305e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008305e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008305e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083063c ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 0083063c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083063c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083063c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008305e4 bytes 08411391
+ 0083063c bytes 08811691
- 008305f0 ["INT_ADD", "register:40f0:8", ["const:8305f0:8", "const:4:8"]]
- 008305f0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00830648 ["INT_ADD", "register:40f0:8", ["const:830648:8", "const:4:8"]]
+ 00830648 ["CALL", null, ["callee:00c57f70:8"]]
- 008305f0 bytes 2c9e1094
+ 00830648 bytes 4a9e1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7858d19a5bc04aae8a978afc1f74bba9"></a>

### [`00830ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830ab0.md) → [`00830b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b08.md) FUN_00830b08

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0082467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00824/0082467c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`008246d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00824/008246d4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00830b14",
      "incomplete_value": false,
      "site": "00830b18",
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
      "definition_site": "00830abc",
      "incomplete_value": false,
      "site": "00830ac0",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00830b14",
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
      "00830b14",
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


#### 変更候補の命令位置

- 旧版 [`00830ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830ab0.md#insn-00830ac0) · [`00830abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830ab0.md#insn-00830abc)
- 新版 `00830b18`（命令位置の公開資料なし） · `00830b14`（命令位置の公開資料なし）

~~~diff
- 00830ac0 ["INT_ADD", "register:40f0:8", ["const:830ac0:8", "const:4:8"]]
- 00830ac0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00830b18 ["INT_ADD", "register:40f0:8", ["const:830b18:8", "const:4:8"]]
+ 00830b18 ["CALL", null, ["callee:0043b7b8:8"]]
- 00830ac0 bytes 2e2bf097
+ 00830b18 bytes 282bf097
- 00830abc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00830abc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00830abc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00830abc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00830b14 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00830b14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00830b14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00830b14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00830abc bytes 00303d91
+ 00830b14 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-240606b3196e5468c79c7307ec01b3a6"></a>

### [`00830ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830ac8.md) → [`00830b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b20.md) FUN_00830b20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00830b44",
      "incomplete_value": true,
      "site": "00830b48",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830aec",
      "incomplete_value": true,
      "site": "00830af0",
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
            "const:538:8"
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
      "00830b48",
      "DATA",
      [
        "storage",
        "00c7e538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830b48",
      "DATA",
      [
        "storage",
        "00c7e608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830ac8.md#insn-00830adc) · [`00830aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830ac8.md#insn-00830aec)
- 新版 `00830b34`（命令位置の公開資料なし） · `00830b44`（命令位置の公開資料なし）

~~~diff
- 00830adc ["INT_ADD", "register:40f0:8", ["const:830adc:8", "const:4:8"]]
- 00830adc ["CALL", null, ["callee:00c57f60:8"]]
+ 00830b34 ["INT_ADD", "register:40f0:8", ["const:830b34:8", "const:4:8"]]
+ 00830b34 ["CALL", null, ["callee:00c57f60:8"]]
- 00830adc bytes ed9c1094
+ 00830b34 bytes 0b9d1094
- 00830aec ["COPY", "tmp:0:8", ["const:538:8"]]
- 00830aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830b44 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00830b44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830b44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830b44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830aec bytes 08e11491
+ 00830b44 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7aa424a7b4ec3e904b70318b56a9cd8"></a>

### [`00830b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830b08.md) → [`00830b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830b60.md) FUN_00830b60

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00830b64",
      "incomplete_value": false,
      "site": "00830b68",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830b0c",
      "incomplete_value": false,
      "site": "00830b10",
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
            "const:538:8"
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
      "00830b68",
      "DATA",
      [
        "storage",
        "00c7e538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830b68",
      "DATA",
      [
        "storage",
        "00c7e608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830b08.md#insn-00830b0c)
- 新版 `00830b64`（命令位置の公開資料なし）

~~~diff
- 00830b0c ["COPY", "tmp:0:8", ["const:538:8"]]
- 00830b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830b64 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00830b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830b0c bytes 08e11491
+ 00830b64 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f75e7949bad28c34ff2f996b2c40eb5"></a>

### [`00830b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830b9c.md) → [`00830bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830bf4.md) FUN_00830bf4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00830c18",
      "incomplete_value": false,
      "site": "00830c18",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830bc0",
      "incomplete_value": false,
      "site": "00830bc0",
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
            "const:5b8:8"
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
      "00830c18",
      "DATA",
      [
        "storage",
        "00c7e5b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830c18",
      "DATA",
      [
        "storage",
        "00c7e688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830b9c.md#insn-00830bb0) · [`00830bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830b9c.md#insn-00830bbc)
- 新版 `00830c08`（命令位置の公開資料なし） · `00830c14`（命令位置の公開資料なし）

~~~diff
- 00830bb0 ["INT_ADD", "register:40f0:8", ["const:830bb0:8", "const:4:8"]]
- 00830bb0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00830c08 ["INT_ADD", "register:40f0:8", ["const:830c08:8", "const:4:8"]]
+ 00830c08 ["CALL", null, ["callee:00c57f60:8"]]
- 00830bb0 bytes b89c1094
+ 00830c08 bytes d69c1094
- 00830bbc ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00830bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830c14 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00830c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830bbc bytes 08e11691
+ 00830c14 bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a00347022c7174d7936ae80d518da17"></a>

### [`00830bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830bd0.md) → [`00830c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830c28.md) FUN_00830c28

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00830c34",
      "incomplete_value": false,
      "site": "00830c34",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830bdc",
      "incomplete_value": false,
      "site": "00830bdc",
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
            "const:5b8:8"
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
      "00830c34",
      "DATA",
      [
        "storage",
        "00c7e5b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830c34",
      "DATA",
      [
        "storage",
        "00c7e688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830bd0.md#insn-00830bd8)
- 新版 `00830c30`（命令位置の公開資料なし）

~~~diff
- 00830bd8 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00830bd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00830bd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00830bd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00830c30 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00830c30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00830c30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00830c30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00830bd8 bytes 29e11691
+ 00830c30 bytes 29211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ca1545f253bc6e3807fe37d5ec772f"></a>

### [`00830c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830c78.md) → [`00830cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830cd0.md) FUN_00830cd0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00830cdc",
      "incomplete_value": false,
      "site": "00830ce8",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830c84",
      "incomplete_value": false,
      "site": "00830c90",
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
            "const:638:8"
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
      "00830ce8",
      "DATA",
      [
        "storage",
        "00c7e638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830ce8",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830c78.md#insn-00830c84)
- 新版 `00830cdc`（命令位置の公開資料なし）

~~~diff
- 00830c84 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00830c84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00830c84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00830c84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00830cdc ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00830cdc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00830cdc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00830cdc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00830c84 bytes 4ae11891
+ 00830cdc bytes 4a211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad88c1acb457ddd8ff68e082d1f73879"></a>

### [`00830cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830cbc.md) → [`00830d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d14.md) FUN_00830d14

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00830d2c",
      "incomplete_value": false,
      "site": "00830d38",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830cd4",
      "incomplete_value": false,
      "site": "00830ce0",
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
            "const:638:8"
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
      "00830d38",
      "DATA",
      [
        "storage",
        "00c7e638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830d38",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830cbc.md#insn-00830cd4) · [`00830d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830cbc.md#insn-00830d04)
- 新版 `00830d2c`（命令位置の公開資料なし） · `00830d5c`（命令位置の公開資料なし）

~~~diff
- 00830cd4 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00830cd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830cd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830cd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830d2c ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00830d2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830d2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830d2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830cd4 bytes 08e11891
+ 00830d2c bytes 08211c91
- 00830d04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00830d04 ["INT_ADD", "register:40f0:8", ["const:830d04:8", "const:4:8"]]
- 00830d04 ["CALLIND", null, ["register:0:8"]]
+ 00830d5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00830d5c ["INT_ADD", "register:40f0:8", ["const:830d5c:8", "const:4:8"]]
+ 00830d5c ["CALLIND", null, ["register:0:8"]]
- 00830d04 bytes 00013fd6
+ 00830d5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f7a75c1fd190811bc5c2f68c82b9e2"></a>

### [`00830d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830d18.md) → [`00830d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830d70.md) FUN_00830d70

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00830d9c",
      "incomplete_value": false,
      "site": "00830d9c",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830d44",
      "incomplete_value": false,
      "site": "00830d44",
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
            "const:638:8"
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
      "00830d9c",
      "DATA",
      [
        "storage",
        "00c7e638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830d9c",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830d18.md#insn-00830d2c) · [`00830d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830d18.md#insn-00830d3c) · [`00830d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830d18.md#insn-00830d60)
- 新版 `00830d84`（命令位置の公開資料なし） · `00830d94`（命令位置の公開資料なし） · `00830db8`（命令位置の公開資料なし）

~~~diff
- 00830d2c ["INT_ADD", "register:40f0:8", ["const:830d2c:8", "const:4:8"]]
- 00830d2c ["CALL", null, ["callee:00c57f60:8"]]
+ 00830d84 ["INT_ADD", "register:40f0:8", ["const:830d84:8", "const:4:8"]]
+ 00830d84 ["CALL", null, ["callee:00c57f60:8"]]
- 00830d2c bytes 599c1094
+ 00830d84 bytes 779c1094
- 00830d3c ["COPY", "tmp:0:8", ["const:638:8"]]
- 00830d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830d94 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00830d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830d3c bytes 08e11891
+ 00830d94 bytes 08211c91
- 00830d60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00830d60 ["INT_ADD", "register:40f0:8", ["const:830d60:8", "const:4:8"]]
- 00830d60 ["CALLIND", null, ["register:0:8"]]
+ 00830db8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00830db8 ["INT_ADD", "register:40f0:8", ["const:830db8:8", "const:4:8"]]
+ 00830db8 ["CALLIND", null, ["register:0:8"]]
- 00830d60 bytes 00013fd6
+ 00830db8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5ac77455b7f3f88948ea51c86a0717"></a>

### [`00830da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830da0.md) → [`00830df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830df8.md) FUN_00830df8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00830e14",
      "incomplete_value": false,
      "site": "00830e14",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830dbc",
      "incomplete_value": false,
      "site": "00830dbc",
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
            "const:638:8"
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
      "00830e14",
      "DATA",
      [
        "storage",
        "00c7e638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00830e14",
      "DATA",
      [
        "storage",
        "00c7e708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830da0.md#insn-00830db8) · [`00830ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830da0.md#insn-00830ddc)
- 新版 `00830e10`（命令位置の公開資料なし） · `00830e34`（命令位置の公開資料なし）

~~~diff
- 00830db8 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00830db8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00830db8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00830db8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00830e10 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00830e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00830e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00830e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00830db8 bytes 29e11891
+ 00830e10 bytes 29211c91
- 00830ddc ["COPY", "register:0:8", ["register:4048:8"]]
- 00830ddc ["INT_ADD", "register:40f0:8", ["const:830ddc:8", "const:4:8"]]
- 00830ddc ["CALLIND", null, ["register:0:8"]]
+ 00830e34 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00830e34 ["INT_ADD", "register:40f0:8", ["const:830e34:8", "const:4:8"]]
+ 00830e34 ["CALLIND", null, ["register:0:8"]]
- 00830ddc bytes 20013fd6
+ 00830e34 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fdc0c1e5936ac7a21a24e1ae8d77363"></a>

### [`00830e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e9c.md) → [`00830ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ef4.md) FUN_00830ef4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00acacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acacc8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00acad38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acad38.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00830f1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00830f1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00830ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e9c.md#insn-00830ec4) · [`00830ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e9c.md#insn-00830ed0) · [`00830ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e9c.md#insn-00830ef4)
- 新版 `00830f1c`（命令位置の公開資料なし） · `00830f28`（命令位置の公開資料なし） · `00830f4c`（命令位置の公開資料なし）

~~~diff
- 00830ec4 ["INT_ADD", "register:40f0:8", ["const:830ec4:8", "const:4:8"]]
- 00830ec4 ["CALL", null, ["ram:47acf4:8"]]
+ 00830f1c ["INT_ADD", "register:40f0:8", ["const:830f1c:8", "const:4:8"]]
+ 00830f1c ["CALL", null, ["ram:47ad34:8"]]
- 00830ec4 bytes 8c27f197
+ 00830f1c bytes 8627f197
- 00830ed0 ["INT_ADD", "register:40f0:8", ["const:830ed0:8", "const:4:8"]]
- 00830ed0 ["CALL", null, ["callee:0047ce14:8"]]
+ 00830f28 ["INT_ADD", "register:40f0:8", ["const:830f28:8", "const:4:8"]]
+ 00830f28 ["CALL", null, ["callee:0047ce14:8"]]
- 00830ed0 bytes c12ff197
+ 00830f28 bytes bb2ff197
- 00830ef4 ["INT_ADD", "register:40f0:8", ["const:830ef4:8", "const:4:8"]]
- 00830ef4 ["CALL", null, ["callee:00851550:8"]]
+ 00830f4c ["INT_ADD", "register:40f0:8", ["const:830f4c:8", "const:4:8"]]
+ 00830f4c ["CALL", null, ["callee:00851550:8"]]
- 00830ef4 bytes 81810094
+ 00830f4c bytes 81810094
~~~


<a id="compare-f3065836b5490c338e0135feb6cac1c0"></a>

### [`00830f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f44.md) → [`00830f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f9c.md) FUN_00830f9c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00830fb4",
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
      "00830fb4",
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


#### 変更候補の命令位置

- 旧版 [`00830f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f44.md#insn-00830f50)
- 新版 `00830fa8`（命令位置の公開資料なし）

~~~diff
- 00830f50 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00830f50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00830f50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00830f50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00830fa8 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00830fa8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00830fa8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00830fa8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00830f50 bytes 4ae11a91
+ 00830fa8 bytes 4a211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9bdab91f679b9ce9752103ee64e930d"></a>

### [`00830f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f88.md) → [`00830fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830fe0.md) FUN_00830fe0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831004",
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
      "00831004",
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


#### 変更候補の命令位置

- 旧版 [`00830fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f88.md#insn-00830fa0) · [`00830fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f88.md#insn-00830fd0)
- 新版 `00830ff8`（命令位置の公開資料なし） · `00831028`（命令位置の公開資料なし）

~~~diff
- 00830fa0 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00830fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00830fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00830fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00830ff8 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00830ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00830ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00830ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00830fa0 bytes 08e11a91
+ 00830ff8 bytes 08211e91
- 00830fd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00830fd0 ["INT_ADD", "register:40f0:8", ["const:830fd0:8", "const:4:8"]]
- 00830fd0 ["CALLIND", null, ["register:0:8"]]
+ 00831028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00831028 ["INT_ADD", "register:40f0:8", ["const:831028:8", "const:4:8"]]
+ 00831028 ["CALLIND", null, ["register:0:8"]]
- 00830fd0 bytes 00013fd6
+ 00831028 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e30980af5b37c33956e6f250bd972e"></a>

### [`00830fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830fe4.md) → [`0083103c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083103c.md) FUN_0083103c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831068",
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
      "00831068",
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


#### 変更候補の命令位置

- 旧版 [`00830ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830fe4.md#insn-00830ff8) · [`00831008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830fe4.md#insn-00831008) · [`0083102c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830fe4.md#insn-0083102c)
- 新版 `00831050`（命令位置の公開資料なし） · `00831060`（命令位置の公開資料なし） · `00831084`（命令位置の公開資料なし）

~~~diff
- 00830ff8 ["INT_ADD", "register:40f0:8", ["const:830ff8:8", "const:4:8"]]
- 00830ff8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00831050 ["INT_ADD", "register:40f0:8", ["const:831050:8", "const:4:8"]]
+ 00831050 ["CALL", null, ["callee:00c57f60:8"]]
- 00830ff8 bytes a69b1094
+ 00831050 bytes c49b1094
- 00831008 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00831008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831060 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00831060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831008 bytes 08e11a91
+ 00831060 bytes 08211e91
- 0083102c ["COPY", "register:0:8", ["register:4040:8"]]
- 0083102c ["INT_ADD", "register:40f0:8", ["const:83102c:8", "const:4:8"]]
- 0083102c ["CALLIND", null, ["register:0:8"]]
+ 00831084 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00831084 ["INT_ADD", "register:40f0:8", ["const:831084:8", "const:4:8"]]
+ 00831084 ["CALLIND", null, ["register:0:8"]]
- 0083102c bytes 00013fd6
+ 00831084 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a76425cf70a9756027312bf8fa0e9a"></a>

### [`0083106c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083106c.md) → [`008310c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008310c4.md) FUN_008310c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008310e0",
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
      "008310e0",
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


#### 変更候補の命令位置

- 旧版 [`00831084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083106c.md#insn-00831084) · [`008310a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083106c.md#insn-008310a8)
- 新版 `008310dc`（命令位置の公開資料なし） · `00831100`（命令位置の公開資料なし）

~~~diff
- 00831084 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00831084 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831084 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831084 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008310dc ["COPY", "tmp:0:8", ["const:788:8"]]
+ 008310dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008310dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008310dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831084 bytes 29e11a91
+ 008310dc bytes 29211e91
- 008310a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 008310a8 ["INT_ADD", "register:40f0:8", ["const:8310a8:8", "const:4:8"]]
- 008310a8 ["CALLIND", null, ["register:0:8"]]
+ 00831100 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00831100 ["INT_ADD", "register:40f0:8", ["const:831100:8", "const:4:8"]]
+ 00831100 ["CALLIND", null, ["register:0:8"]]
- 008310a8 bytes 20013fd6
+ 00831100 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f7831a058ac044fa6a7c63cebe4870"></a>

### [`00831168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831168.md) → [`008311c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008311c0.md) FUN_008311c0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008311e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008311e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831168.md#insn-00831190) · [`0083119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831168.md#insn-0083119c)
- 新版 `008311e8`（命令位置の公開資料なし） · `008311f4`（命令位置の公開資料なし）

~~~diff
- 00831190 ["INT_ADD", "register:40f0:8", ["const:831190:8", "const:4:8"]]
- 00831190 ["CALL", null, ["ram:47acf4:8"]]
+ 008311e8 ["INT_ADD", "register:40f0:8", ["const:8311e8:8", "const:4:8"]]
+ 008311e8 ["CALL", null, ["ram:47ad34:8"]]
- 00831190 bytes d926f197
+ 008311e8 bytes d326f197
- 0083119c ["INT_ADD", "register:40f0:8", ["const:83119c:8", "const:4:8"]]
- 0083119c ["CALL", null, ["callee:0047ce14:8"]]
+ 008311f4 ["INT_ADD", "register:40f0:8", ["const:8311f4:8", "const:4:8"]]
+ 008311f4 ["CALL", null, ["callee:0047ce14:8"]]
- 0083119c bytes 0e2ff197
+ 008311f4 bytes 082ff197
~~~


<a id="compare-3af18f760fd387ebc2a2acc3491c3b9e"></a>

### [`008311e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008311e0.md) → [`00831238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831238.md) FUN_00831238

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083125c",
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
      "0083125c",
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


#### 変更候補の命令位置

- 旧版 [`008311f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008311e0.md#insn-008311f4) · [`00831200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008311e0.md#insn-00831200)
- 新版 `0083124c`（命令位置の公開資料なし） · `00831258`（命令位置の公開資料なし）

~~~diff
- 008311f4 ["INT_ADD", "register:40f0:8", ["const:8311f4:8", "const:4:8"]]
- 008311f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0083124c ["INT_ADD", "register:40f0:8", ["const:83124c:8", "const:4:8"]]
+ 0083124c ["CALL", null, ["callee:00c57f60:8"]]
- 008311f4 bytes 279b1094
+ 0083124c bytes 459b1094
- 00831200 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00831200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831258 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 00831258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831200 bytes 08e11c91
+ 00831258 bytes 08212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30c141e583e8081e3114df4365bc898"></a>

### [`00831214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831214.md) → [`0083126c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083126c.md) FUN_0083126c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831278",
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
      "00831278",
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


#### 変更候補の命令位置

- 旧版 [`0083121c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831214.md#insn-0083121c)
- 新版 `00831274`（命令位置の公開資料なし）

~~~diff
- 0083121c ["COPY", "tmp:0:8", ["const:738:8"]]
- 0083121c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083121c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083121c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00831274 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 00831274 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00831274 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00831274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083121c bytes 29e11c91
+ 00831274 bytes 29212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15365cc6ee19a4abb0846bc1a5fd5af"></a>

### [`00831230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831230.md) → [`00831288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831288.md) FUN_00831288

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008312ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008312ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831230.md#insn-00831254) · [`00831260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831230.md#insn-00831260)
- 新版 `008312ac`（命令位置の公開資料なし） · `008312b8`（命令位置の公開資料なし）

~~~diff
- 00831254 ["INT_ADD", "register:40f0:8", ["const:831254:8", "const:4:8"]]
- 00831254 ["CALL", null, ["ram:47acf4:8"]]
+ 008312ac ["INT_ADD", "register:40f0:8", ["const:8312ac:8", "const:4:8"]]
+ 008312ac ["CALL", null, ["ram:47ad34:8"]]
- 00831254 bytes a826f197
+ 008312ac bytes a226f197
- 00831260 ["INT_ADD", "register:40f0:8", ["const:831260:8", "const:4:8"]]
- 00831260 ["CALL", null, ["callee:0047ce14:8"]]
+ 008312b8 ["INT_ADD", "register:40f0:8", ["const:8312b8:8", "const:4:8"]]
+ 008312b8 ["CALL", null, ["callee:0047ce14:8"]]
- 00831260 bytes dd2ef197
+ 008312b8 bytes d72ef197
~~~


<a id="compare-ec2000498b9937007b7fa41bf879497a"></a>

### [`008312a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312a4.md) → [`008312fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312fc.md) FUN_008312fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831320",
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
      "00831320",
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


#### 変更候補の命令位置

- 旧版 [`008312b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312a4.md#insn-008312b8) · [`008312c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312a4.md#insn-008312c4)
- 新版 `00831310`（命令位置の公開資料なし） · `0083131c`（命令位置の公開資料なし）

~~~diff
- 008312b8 ["INT_ADD", "register:40f0:8", ["const:8312b8:8", "const:4:8"]]
- 008312b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00831310 ["INT_ADD", "register:40f0:8", ["const:831310:8", "const:4:8"]]
+ 00831310 ["CALL", null, ["callee:00c57f60:8"]]
- 008312b8 bytes f69a1094
+ 00831310 bytes 149b1094
- 008312c4 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 008312c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008312c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008312c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083131c ["COPY", "tmp:0:8", ["const:888:8"]]
+ 0083131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008312c4 bytes 08e11e91
+ 0083131c bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2887589fb7bed137ca4c29e3a115f5b6"></a>

### [`008312d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312d8.md) → [`00831330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831330.md) FUN_00831330

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083133c",
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
      "0083133c",
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


#### 変更候補の命令位置

- 旧版 [`008312e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312d8.md#insn-008312e0)
- 新版 `00831338`（命令位置の公開資料なし）

~~~diff
- 008312e0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 008312e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008312e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008312e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00831338 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00831338 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00831338 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00831338 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008312e0 bytes 29e11e91
+ 00831338 bytes 29212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f639f16420e51f95bb23d7a70218f891"></a>

### [`008312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md) → [`0083134c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md) FUN_0083134c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0081fdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081f/0081fdc8.md) [`0082907c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0081fe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081f/0081fe20.md) [`008290d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008290d4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00831424",
      "READ",
      [
        "storage",
        "002b406d",
        null,
        "string"
      ]
    ],
    [
      "00831428",
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
      "00831390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00831424",
      "READ",
      [
        "storage",
        "002b409e",
        null,
        "string"
      ]
    ],
    [
      "00831428",
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


#### 変更候補の命令位置

- 旧版 [`00831338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md#insn-00831338) · [`00831388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md#insn-00831388) · [`0083138c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md#insn-0083138c)
- 新版 `00831390`（命令位置の公開資料なし） · `008313e0`（命令位置の公開資料なし） · `008313e4`（命令位置の公開資料なし）

~~~diff
- 00831338 ["INT_ADD", "register:40f0:8", ["const:831338:8", "const:4:8"]]
- 00831338 ["CALL", null, ["ram:47acf4:8"]]
+ 00831390 ["INT_ADD", "register:40f0:8", ["const:831390:8", "const:4:8"]]
+ 00831390 ["CALL", null, ["ram:47ad34:8"]]
- 00831338 bytes 6f26f197
+ 00831390 bytes 6926f197
- 00831388 ["INT_ADD", "register:40f0:8", ["const:831388:8", "const:4:8"]]
- 00831388 ["CALL", null, ["callee:0081fe20:8"]]
+ 008313e0 ["INT_ADD", "register:40f0:8", ["const:8313e0:8", "const:4:8"]]
+ 008313e0 ["CALL", null, ["callee:0081fe20:8"]]
- 00831388 bytes 90baff97
+ 008313e0 bytes 90baff97
- 0083138c ["INT_ADD", "register:40f0:8", ["const:83138c:8", "const:4:8"]]
- 0083138c ["CALL", null, ["callee:00851550:8"]]
+ 008313e4 ["INT_ADD", "register:40f0:8", ["const:8313e4:8", "const:4:8"]]
+ 008313e4 ["CALL", null, ["callee:00851550:8"]]
- 0083138c bytes 5b800094
+ 008313e4 bytes 5b800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c316797a3bb7cb87c45e4f1455415e3c"></a>

### [`008316cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008316cc.md) → [`00831724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831724.md) FUN_00831724

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831748",
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
      "00831748",
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


#### 変更候補の命令位置

- 旧版 [`008316e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008316cc.md#insn-008316e0) · [`008316ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008316cc.md#insn-008316ec)
- 新版 `00831738`（命令位置の公開資料なし） · `00831744`（命令位置の公開資料なし）

~~~diff
- 008316e0 ["INT_ADD", "register:40f0:8", ["const:8316e0:8", "const:4:8"]]
- 008316e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00831738 ["INT_ADD", "register:40f0:8", ["const:831738:8", "const:4:8"]]
+ 00831738 ["CALL", null, ["callee:00c57f60:8"]]
- 008316e0 bytes ec991094
+ 00831738 bytes 0a9a1094
- 008316ec ["COPY", "tmp:0:8", ["const:828:8"]]
- 008316ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008316ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008316ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831744 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00831744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008316ec bytes 08a12091
+ 00831744 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee9a4a173f7aff2b6c16d82b8c82cfb5"></a>

### [`00831700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831700.md) → [`00831758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831758.md) FUN_00831758

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831764",
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
      "00831764",
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


#### 変更候補の命令位置

- 旧版 [`00831708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831700.md#insn-00831708)
- 新版 `00831760`（命令位置の公開資料なし）

~~~diff
- 00831708 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00831708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00831760 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00831760 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00831760 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00831760 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831708 bytes 29a12091
+ 00831760 bytes 29e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-521d0701f3aec5e18132bcf7c65b47b9"></a>

### [`0083171c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083171c.md) → [`00831774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831774.md) FUN_00831774

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00831798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083171c.md#insn-00831740) · [`0083174c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083171c.md#insn-0083174c)
- 新版 `00831798`（命令位置の公開資料なし） · `008317a4`（命令位置の公開資料なし）

~~~diff
- 00831740 ["INT_ADD", "register:40f0:8", ["const:831740:8", "const:4:8"]]
- 00831740 ["CALL", null, ["ram:47acf4:8"]]
+ 00831798 ["INT_ADD", "register:40f0:8", ["const:831798:8", "const:4:8"]]
+ 00831798 ["CALL", null, ["ram:47ad34:8"]]
- 00831740 bytes 6d25f197
+ 00831798 bytes 6725f197
- 0083174c ["INT_ADD", "register:40f0:8", ["const:83174c:8", "const:4:8"]]
- 0083174c ["CALL", null, ["callee:0047ce14:8"]]
+ 008317a4 ["INT_ADD", "register:40f0:8", ["const:8317a4:8", "const:4:8"]]
+ 008317a4 ["CALL", null, ["callee:0047ce14:8"]]
- 0083174c bytes a22df197
+ 008317a4 bytes 9c2df197
~~~


<a id="compare-e951b47e88c770d80a02bb79532f9741"></a>

### [`0083178c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083178c.md) → [`008317e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317e4.md) FUN_008317e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00829574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 1件 [`008295cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008317f0",
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
      "008317f0",
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


#### 変更候補の命令位置

- 旧版 [`0083179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083178c.md#insn-0083179c) · [`00831798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083178c.md#insn-00831798)
- 新版 `008317f4`（命令位置の公開資料なし） · `008317f0`（命令位置の公開資料なし）

~~~diff
- 0083179c ["INT_ADD", "register:40f0:8", ["const:83179c:8", "const:4:8"]]
- 0083179c ["CALL", null, ["callee:00442970:8"]]
+ 008317f4 ["INT_ADD", "register:40f0:8", ["const:8317f4:8", "const:4:8"]]
+ 008317f4 ["CALL", null, ["callee:00442970:8"]]
- 0083179c bytes 6544f097
+ 008317f4 bytes 5f44f097
- 00831798 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00831798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00831798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00831798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008317f0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 008317f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008317f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008317f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00831798 bytes 00303d91
+ 008317f0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ea917165d5fc338c8eb43c5cfc92bcf"></a>

### [`008317a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317a4.md) → [`008317fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317fc.md) FUN_008317fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831820",
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
      "00831820",
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


#### 変更候補の命令位置

- 旧版 [`008317b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317a4.md#insn-008317b8) · [`008317c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317a4.md#insn-008317c4)
- 新版 `00831810`（命令位置の公開資料なし） · `0083181c`（命令位置の公開資料なし）

~~~diff
- 008317b8 ["INT_ADD", "register:40f0:8", ["const:8317b8:8", "const:4:8"]]
- 008317b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00831810 ["INT_ADD", "register:40f0:8", ["const:831810:8", "const:4:8"]]
+ 00831810 ["CALL", null, ["callee:00c57f60:8"]]
- 008317b8 bytes b6991094
+ 00831810 bytes d4991094
- 008317c4 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 008317c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008317c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008317c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083181c ["COPY", "tmp:0:8", ["const:988:8"]]
+ 0083181c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083181c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083181c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008317c4 bytes 08e12291
+ 0083181c bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a680ea2823ac1ea575282df0b959832"></a>

### [`008317d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317d8.md) → [`00831830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831830.md) FUN_00831830

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083183c",
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
      "0083183c",
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


#### 変更候補の命令位置

- 旧版 [`008317e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317d8.md#insn-008317e0)
- 新版 `00831838`（命令位置の公開資料なし）

~~~diff
- 008317e0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 008317e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008317e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008317e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00831838 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 00831838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00831838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00831838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008317e0 bytes 29e12291
+ 00831838 bytes 29212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22dae9038ebff1e43b3a37c262bda617"></a>

### [`008317f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md) → [`0083184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) FUN_0083184c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00826dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) [`008276c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008276c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00826e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) [`00827718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827718.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831884",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00831a30",
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
      "00831884",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00831a30",
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


#### 変更候補の命令位置

- 旧版 [`0083182c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md#insn-0083182c) · [`008319dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md#insn-008319dc) · [`00831858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md#insn-00831858)
- 新版 `00831884`（命令位置の公開資料なし） · `00831a34`（命令位置の公開資料なし） · `008318b0`（命令位置の公開資料なし）

~~~diff
- 0083182c ["INT_ADD", "register:40f0:8", ["const:83182c:8", "const:4:8"]]
- 0083182c ["CALL", null, ["ram:47acf4:8"]]
+ 00831884 ["INT_ADD", "register:40f0:8", ["const:831884:8", "const:4:8"]]
+ 00831884 ["CALL", null, ["ram:47ad34:8"]]
- 0083182c bytes 3225f197
+ 00831884 bytes 2c25f197
- 008319dc ["INT_ADD", "register:40f0:8", ["const:8319dc:8", "const:4:8"]]
- 008319dc ["CALL", null, ["callee:00442970:8"]]
+ 00831a34 ["INT_ADD", "register:40f0:8", ["const:831a34:8", "const:4:8"]]
+ 00831a34 ["CALL", null, ["callee:00442970:8"]]
- 008319dc bytes d543f097
+ 00831a34 bytes cf43f097
- 00831858 ["INT_ADD", "register:40f0:8", ["const:831858:8", "const:4:8"]]
- 00831858 ["CALL", null, ["callee:00851550:8"]]
+ 008318b0 ["INT_ADD", "register:40f0:8", ["const:8318b0:8", "const:4:8"]]
+ 008318b0 ["CALL", null, ["callee:00851550:8"]]
- 00831858 bytes 287f0094
+ 008318b0 bytes 287f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbb76573ea2b256baa14fac075d2e303"></a>

### [`00831ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ce8.md) → [`00831d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d40.md) FUN_00831d40

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831d64",
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
      "00831d64",
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


#### 変更候補の命令位置

- 旧版 [`00831cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ce8.md#insn-00831cfc) · [`00831d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ce8.md#insn-00831d08)
- 新版 `00831d54`（命令位置の公開資料なし） · `00831d60`（命令位置の公開資料なし）

~~~diff
- 00831cfc ["INT_ADD", "register:40f0:8", ["const:831cfc:8", "const:4:8"]]
- 00831cfc ["CALL", null, ["callee:00c57f60:8"]]
+ 00831d54 ["INT_ADD", "register:40f0:8", ["const:831d54:8", "const:4:8"]]
+ 00831d54 ["CALL", null, ["callee:00c57f60:8"]]
- 00831cfc bytes 65981094
+ 00831d54 bytes 83981094
- 00831d08 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00831d08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831d08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831d08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831d60 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00831d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831d08 bytes 08e12491
+ 00831d60 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0efde19d2b733b5d110d8f6fb8052a3"></a>

### [`00831d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d20.md) → [`00831d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d78.md) FUN_00831d78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831d80",
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
      "00831d80",
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


#### 変更候補の命令位置

- 旧版 [`00831d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d20.md#insn-00831d24)
- 新版 `00831d7c`（命令位置の公開資料なし）

~~~diff
- 00831d24 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00831d24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831d24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831d24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831d7c ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00831d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831d24 bytes 08e12491
+ 00831d7c bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3616bcff310af031785dbf764177183"></a>

### [`00831d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d40.md) → [`00831d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md) FUN_00831d98

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831dc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00831dcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00831dc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00831dcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d40.md#insn-00831d68) · [`00831d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d40.md#insn-00831d74) · [`00831dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d40.md#insn-00831dcc)
- 新版 `00831dc0`（命令位置の公開資料なし） · `00831dcc`（命令位置の公開資料なし） · `00831e24`（命令位置の公開資料なし）

~~~diff
- 00831d68 ["INT_ADD", "register:40f0:8", ["const:831d68:8", "const:4:8"]]
- 00831d68 ["CALL", null, ["ram:47acf4:8"]]
+ 00831dc0 ["INT_ADD", "register:40f0:8", ["const:831dc0:8", "const:4:8"]]
+ 00831dc0 ["CALL", null, ["ram:47ad34:8"]]
- 00831d68 bytes e323f197
+ 00831dc0 bytes dd23f197
- 00831d74 ["INT_ADD", "register:40f0:8", ["const:831d74:8", "const:4:8"]]
- 00831d74 ["CALL", null, ["ram:47acf4:8"]]
+ 00831dcc ["INT_ADD", "register:40f0:8", ["const:831dcc:8", "const:4:8"]]
+ 00831dcc ["CALL", null, ["ram:47ad34:8"]]
- 00831d74 bytes e023f197
+ 00831dcc bytes da23f197
- 00831dcc ["INT_ADD", "register:40f0:8", ["const:831dcc:8", "const:4:8"]]
- 00831dcc ["CALL", null, ["callee:00851550:8"]]
+ 00831e24 ["INT_ADD", "register:40f0:8", ["const:831e24:8", "const:4:8"]]
+ 00831e24 ["CALL", null, ["callee:00851550:8"]]
- 00831dcc bytes cb7d0094
+ 00831e24 bytes cb7d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1c3a4024d2f19ab2c69b9d353ef9b34"></a>

### [`00831e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831e94.md) → [`00831eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831eec.md) FUN_00831eec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831f10",
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
      "00831f10",
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


#### 変更候補の命令位置

- 旧版 [`00831ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831e94.md#insn-00831ea8) · [`00831eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831e94.md#insn-00831eb4)
- 新版 `00831f00`（命令位置の公開資料なし） · `00831f0c`（命令位置の公開資料なし）

~~~diff
- 00831ea8 ["INT_ADD", "register:40f0:8", ["const:831ea8:8", "const:4:8"]]
- 00831ea8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00831f00 ["INT_ADD", "register:40f0:8", ["const:831f00:8", "const:4:8"]]
+ 00831f00 ["CALL", null, ["callee:00c57f60:8"]]
- 00831ea8 bytes fa971094
+ 00831f00 bytes 18981094
- 00831eb4 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00831eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00831f0c ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00831f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00831f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00831f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831eb4 bytes 08e12691
+ 00831f0c bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e004005325d05d775dfb7c2eecd32eb2"></a>

### [`00831ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ec8.md) → [`00831f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f20.md) FUN_00831f20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831f2c",
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
      "00831f2c",
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


#### 変更候補の命令位置

- 旧版 [`00831ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ec8.md#insn-00831ed0)
- 新版 `00831f28`（命令位置の公開資料なし）

~~~diff
- 00831ed0 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00831ed0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831ed0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831ed0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00831f28 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00831f28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00831f28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00831f28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831ed0 bytes 29e12691
+ 00831f28 bytes 29212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f9a05dccb4e26f74584e86782a3647"></a>

### [`00831ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee4.md) → [`00831f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md) FUN_00831f3c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a4692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4692c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00831f60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00831f6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00831f60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00831f6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00831f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee4.md#insn-00831f08) · [`00831f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee4.md#insn-00831f14) · [`00831f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee4.md#insn-00831f40)
- 新版 `00831f60`（命令位置の公開資料なし） · `00831f6c`（命令位置の公開資料なし） · `00831f98`（命令位置の公開資料なし）

~~~diff
- 00831f08 ["INT_ADD", "register:40f0:8", ["const:831f08:8", "const:4:8"]]
- 00831f08 ["CALL", null, ["ram:47acf4:8"]]
+ 00831f60 ["INT_ADD", "register:40f0:8", ["const:831f60:8", "const:4:8"]]
+ 00831f60 ["CALL", null, ["ram:47ad34:8"]]
- 00831f08 bytes 7b23f197
+ 00831f60 bytes 7523f197
- 00831f14 ["INT_ADD", "register:40f0:8", ["const:831f14:8", "const:4:8"]]
- 00831f14 ["CALL", null, ["ram:47acf4:8"]]
+ 00831f6c ["INT_ADD", "register:40f0:8", ["const:831f6c:8", "const:4:8"]]
+ 00831f6c ["CALL", null, ["ram:47ad34:8"]]
- 00831f14 bytes 7823f197
+ 00831f6c bytes 7223f197
- 00831f40 ["INT_ADD", "register:40f0:8", ["const:831f40:8", "const:4:8"]]
- 00831f40 ["CALL", null, ["callee:008b6efc:8"]]
+ 00831f98 ["INT_ADD", "register:40f0:8", ["const:831f98:8", "const:4:8"]]
+ 00831f98 ["CALL", null, ["callee:008b6efc:8"]]
- 00831f40 bytes d9130294
+ 00831f98 bytes d9130294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95957b901dbca356af364e031a91ea6e"></a>

### [`00831fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fa4.md) → [`00831ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ffc.md) FUN_00831ffc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00832020",
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
      "00832020",
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


#### 変更候補の命令位置

- 旧版 [`00831fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fa4.md#insn-00831fb8) · [`00831fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fa4.md#insn-00831fc4)
- 新版 `00832010`（命令位置の公開資料なし） · `0083201c`（命令位置の公開資料なし）

~~~diff
- 00831fb8 ["INT_ADD", "register:40f0:8", ["const:831fb8:8", "const:4:8"]]
- 00831fb8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00832010 ["INT_ADD", "register:40f0:8", ["const:832010:8", "const:4:8"]]
+ 00832010 ["CALL", null, ["callee:00c57f60:8"]]
- 00831fb8 bytes b6971094
+ 00832010 bytes d4971094
- 00831fc4 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00831fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00831fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00831fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083201c ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 0083201c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083201c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083201c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00831fc4 bytes 08e12891
+ 0083201c bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f7db30b8fc0a6e427db88c434c1bc18"></a>

### [`00831fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fd8.md) → [`00832030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832030.md) FUN_00832030

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083203c",
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
      "0083203c",
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


#### 変更候補の命令位置

- 旧版 [`00831fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fd8.md#insn-00831fe0)
- 新版 `00832038`（命令位置の公開資料なし）

~~~diff
- 00831fe0 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00831fe0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00831fe0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00831fe0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00832038 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00832038 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00832038 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00832038 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00831fe0 bytes 29e12891
+ 00832038 bytes 29212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8dea733c1f9b2fcab55a1e4bdf6dcaa"></a>

### [`00831ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md) → [`0083204c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md) FUN_0083204c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0082d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083206c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00832078",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0083206c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00832078",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00832014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md#insn-00832014) · [`00832020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md#insn-00832020) · [`00832034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md#insn-00832034)
- 新版 `0083206c`（命令位置の公開資料なし） · `00832078`（命令位置の公開資料なし） · `0083208c`（命令位置の公開資料なし）

~~~diff
- 00832014 ["INT_ADD", "register:40f0:8", ["const:832014:8", "const:4:8"]]
- 00832014 ["CALL", null, ["ram:47acf4:8"]]
+ 0083206c ["INT_ADD", "register:40f0:8", ["const:83206c:8", "const:4:8"]]
+ 0083206c ["CALL", null, ["ram:47ad34:8"]]
- 00832014 bytes 3823f197
+ 0083206c bytes 3223f197
- 00832020 ["INT_ADD", "register:40f0:8", ["const:832020:8", "const:4:8"]]
- 00832020 ["CALL", null, ["ram:47acf4:8"]]
+ 00832078 ["INT_ADD", "register:40f0:8", ["const:832078:8", "const:4:8"]]
+ 00832078 ["CALL", null, ["ram:47ad34:8"]]
- 00832020 bytes 3523f197
+ 00832078 bytes 2f23f197
- 00832034 ["INT_ADD", "register:40f0:8", ["const:832034:8", "const:4:8"]]
- 00832034 ["CALL", null, ["callee:00851550:8"]]
+ 0083208c ["INT_ADD", "register:40f0:8", ["const:83208c:8", "const:4:8"]]
+ 0083208c ["CALL", null, ["callee:00851550:8"]]
- 00832034 bytes 317d0094
+ 0083208c bytes 317d0094
~~~


<a id="compare-27f2e2e65639b4038cf3b9a62ff1d932"></a>

### [`00832084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/00832084.md) → [`008320dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320dc.md) FUN_008320dc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00832100",
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
      "00832100",
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


#### 変更候補の命令位置

- 旧版 [`00832098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/00832084.md#insn-00832098) · [`008320a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/00832084.md#insn-008320a4)
- 新版 `008320f0`（命令位置の公開資料なし） · `008320fc`（命令位置の公開資料なし）

~~~diff
- 00832098 ["INT_ADD", "register:40f0:8", ["const:832098:8", "const:4:8"]]
- 00832098 ["CALL", null, ["callee:00c57f60:8"]]
+ 008320f0 ["INT_ADD", "register:40f0:8", ["const:8320f0:8", "const:4:8"]]
+ 008320f0 ["CALL", null, ["callee:00c57f60:8"]]
- 00832098 bytes 7e971094
+ 008320f0 bytes 9c971094
- 008320a4 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 008320a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008320a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008320a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008320fc ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 008320fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008320fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008320fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008320a4 bytes 08e12a91
+ 008320fc bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e475635ed4774ee58a5851011ce5221b"></a>

### [`008320d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) → [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) FUN_0083212c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)
- 新版 呼出元 0件  · 呼出先 41件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00832178",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0083219c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008322a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cb88"
      ]
    ]
  ],
  "added": [
    [
      "00832178",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0083219c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008322a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cbe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00832120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md#insn-00832120) · [`00832144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md#insn-00832144) · [`0083224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md#insn-0083224c)
- 新版 `00832178`（命令位置の公開資料なし） · `0083219c`（命令位置の公開資料なし） · `008322a4`（命令位置の公開資料なし）

~~~diff
- 00832120 ["INT_ADD", "register:40f0:8", ["const:832120:8", "const:4:8"]]
- 00832120 ["CALL", null, ["ram:47acf4:8"]]
+ 00832178 ["INT_ADD", "register:40f0:8", ["const:832178:8", "const:4:8"]]
+ 00832178 ["CALL", null, ["ram:47ad34:8"]]
- 00832120 bytes f522f197
+ 00832178 bytes ef22f197
- 00832144 ["INT_ADD", "register:40f0:8", ["const:832144:8", "const:4:8"]]
- 00832144 ["CALL", null, ["ram:47acf4:8"]]
+ 0083219c ["INT_ADD", "register:40f0:8", ["const:83219c:8", "const:4:8"]]
+ 0083219c ["CALL", null, ["ram:47ad34:8"]]
- 00832144 bytes ec22f197
+ 0083219c bytes e622f197
- 0083224c ["INT_ADD", "register:40f0:8", ["const:83224c:8", "const:4:8"]]
- 0083224c ["CALL", null, ["ram:81cb88:8"]]
+ 008322a4 ["INT_ADD", "register:40f0:8", ["const:8322a4:8", "const:4:8"]]
+ 008322a4 ["CALL", null, ["ram:81cbe0:8"]]
- 0083224c bytes 4faaff97
+ 008322a4 bytes 4faaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054a37af70571560346e1a41acee628a"></a>

### [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) → [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) FUN_0083418c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`008320d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) [`00835168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md) [`0083526c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md) [`00835500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md) [`00835604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 7件 [`0083212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) [`008351c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md) [`008352c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md) [`00835558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md) [`0083565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00834198",
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
      "00834198",
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


#### 変更候補の命令位置

- 旧版 [`00834144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md#insn-00834144) · [`00834140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md#insn-00834140)
- 新版 `0083419c`（命令位置の公開資料なし） · `00834198`（命令位置の公開資料なし）

~~~diff
- 00834144 ["INT_ADD", "register:40f0:8", ["const:834144:8", "const:4:8"]]
- 00834144 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0083419c ["INT_ADD", "register:40f0:8", ["const:83419c:8", "const:4:8"]]
+ 0083419c ["CALL", null, ["callee:0043b7b8:8"]]
- 00834144 bytes 8d1df097
+ 0083419c bytes 871df097
- 00834140 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00834140 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00834140 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00834140 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00834198 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00834198 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00834198 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00834198 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00834140 bytes 00303d91
+ 00834198 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9144ccbaa1056ef04fb01444ab6e331"></a>

### [`00835104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835104.md) → [`0083515c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083515c.md) FUN_0083515c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083516c",
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
      "0083516c",
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


#### 変更候補の命令位置

- 旧版 [`00835110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835104.md#insn-00835110)
- 新版 `00835168`（命令位置の公開資料なし）

~~~diff
- 00835110 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00835110 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835110 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835110 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00835168 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00835168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00835168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00835168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835110 bytes 29a12c91
+ 00835168 bytes 29e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86e3f71184bbec0c1bf3b5d9be004ea"></a>

### [`00835128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835128.md) → [`00835180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835180.md) FUN_00835180

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083518c",
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
      "0083518c",
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


#### 変更候補の命令位置

- 旧版 [`00835130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835128.md#insn-00835130) · [`00835154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835128.md#insn-00835154)
- 新版 `00835188`（命令位置の公開資料なし） · `008351ac`（命令位置の公開資料なし）

~~~diff
- 00835130 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00835130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00835188 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00835188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00835188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00835188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835130 bytes 29a12c91
+ 00835188 bytes 29e12f91
- 00835154 ["INT_ADD", "register:40f0:8", ["const:835154:8", "const:4:8"]]
- 00835154 ["CALL", null, ["callee:00c57f80:8"]]
+ 008351ac ["INT_ADD", "register:40f0:8", ["const:8351ac:8", "const:4:8"]]
+ 008351ac ["CALL", null, ["callee:00c57f80:8"]]
- 00835154 bytes 578b1094
+ 008351ac bytes 758b1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986392779d833a03009311784443d9f6"></a>

### [`00835168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md) → [`008351c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md) FUN_008351c0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008351f4",
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
      "008351f4",
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


#### 変更候補の命令位置

- 旧版 [`00835184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md#insn-00835184) · [`00835190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md#insn-00835190) · [`00835194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md#insn-00835194)
- 新版 `008351dc`（命令位置の公開資料なし） · `008351e8`（命令位置の公開資料なし）

~~~diff
- 00835184 ["INT_ADD", "register:40f0:8", ["const:835184:8", "const:4:8"]]
- 00835184 ["CALL", null, ["callee:00c57f60:8"]]
+ 008351dc ["INT_ADD", "register:40f0:8", ["const:8351dc:8", "const:4:8"]]
+ 008351dc ["CALL", null, ["callee:00c57f60:8"]]
- 00835184 bytes 438b1094
+ 008351dc bytes 618b1094
- 00835190 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00835190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00835190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00835190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008351e8 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 008351e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008351e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008351e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00835190 bytes 08a12c91
+ 008351e8 bytes 08e12f91
- 00835194 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00835194 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013a54dd5d8e83720d893277d624fbc4"></a>

### [`0083526c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md) → [`008352c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md) FUN_008352c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008352f4",
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
      "008352f4",
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


#### 変更候補の命令位置

- 旧版 [`00835294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md#insn-00835294) · [`008352d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md#insn-008352d4) · [`00835310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md#insn-00835310)
- 新版 `008352ec`（命令位置の公開資料なし） · `0083532c`（命令位置の公開資料なし） · `00835368`（命令位置の公開資料なし）

~~~diff
- 00835294 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00835294 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00835294 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00835294 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008352ec ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 008352ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008352ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008352ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00835294 bytes 4aa12c91
+ 008352ec bytes 4ae12f91
- 008352d4 ["INT_ADD", "register:40f0:8", ["const:8352d4:8", "const:4:8"]]
- 008352d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0083532c ["INT_ADD", "register:40f0:8", ["const:83532c:8", "const:4:8"]]
+ 0083532c ["CALL", null, ["callee:00c57f60:8"]]
- 008352d4 bytes ef8a1094
+ 0083532c bytes 0d8b1094
- 00835310 ["INT_ADD", "register:40f0:8", ["const:835310:8", "const:4:8"]]
- 00835310 ["CALL", null, ["callee:00c580d0:8"]]
+ 00835368 ["INT_ADD", "register:40f0:8", ["const:835368:8", "const:4:8"]]
+ 00835368 ["CALL", null, ["callee:00c580d0:8"]]
- 00835310 bytes 3c8b1094
+ 00835368 bytes 5a8b1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ad3181850ffeeb16ed07a461d1e2c01"></a>

### [`008353a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008353a4.md) → [`008353fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353fc.md) FUN_008353fc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a83260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a832d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a832d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00835430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008353d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008353a4.md#insn-008353d8) · [`008353d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008353a4.md#insn-008353d4) · [`008353fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008353a4.md#insn-008353fc)
- 新版 `00835430`（命令位置の公開資料なし） · `0083542c`（命令位置の公開資料なし） · `00835454`（命令位置の公開資料なし）

~~~diff
- 008353d8 ["INT_ADD", "register:40f0:8", ["const:8353d8:8", "const:4:8"]]
- 008353d8 ["CALL", null, ["ram:47acf4:8"]]
+ 00835430 ["INT_ADD", "register:40f0:8", ["const:835430:8", "const:4:8"]]
+ 00835430 ["CALL", null, ["ram:47ad34:8"]]
- 008353d8 bytes 4716f197
+ 00835430 bytes 4116f197
- 008353d4 ["INT_ADD", "register:40f0:8", ["const:8353d4:8", "const:4:8"]]
- 008353d4 ["CALL", null, ["callee:008b91d0:8"]]
+ 0083542c ["INT_ADD", "register:40f0:8", ["const:83542c:8", "const:4:8"]]
+ 0083542c ["CALL", null, ["callee:008b91d0:8"]]
- 008353d4 bytes 690f0294
+ 0083542c bytes 690f0294
- 008353fc ["INT_ADD", "register:40f0:8", ["const:8353fc:8", "const:4:8"]]
- 008353fc ["CALL", null, ["callee:00851550:8"]]
+ 00835454 ["INT_ADD", "register:40f0:8", ["const:835454:8", "const:4:8"]]
+ 00835454 ["CALL", null, ["callee:00851550:8"]]
- 008353fc bytes 3f700094
+ 00835454 bytes 3f700094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68496a4d73c889b8a332eac7418a02a"></a>

### [`0083549c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083549c.md) → [`008354f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354f4.md) FUN_008354f4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835504",
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
      "00835504",
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


#### 変更候補の命令位置

- 旧版 [`008354a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083549c.md#insn-008354a8)
- 新版 `00835500`（命令位置の公開資料なし）

~~~diff
- 008354a8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 008354a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008354a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008354a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00835500 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00835500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00835500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00835500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008354a8 bytes 29a12e91
+ 00835500 bytes 29e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6081efa8d28f52db420684ed85de682"></a>

### [`008354c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008354c0.md) → [`00835518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835518.md) FUN_00835518

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835524",
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
      "00835524",
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


#### 変更候補の命令位置

- 旧版 [`008354c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008354c0.md#insn-008354c8) · [`008354ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008354c0.md#insn-008354ec)
- 新版 `00835520`（命令位置の公開資料なし） · `00835544`（命令位置の公開資料なし）

~~~diff
- 008354c8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 008354c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008354c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008354c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00835520 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00835520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00835520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00835520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008354c8 bytes 29a12e91
+ 00835520 bytes 29e13191
- 008354ec ["INT_ADD", "register:40f0:8", ["const:8354ec:8", "const:4:8"]]
- 008354ec ["CALL", null, ["callee:00c57f80:8"]]
+ 00835544 ["INT_ADD", "register:40f0:8", ["const:835544:8", "const:4:8"]]
+ 00835544 ["CALL", null, ["callee:00c57f80:8"]]
- 008354ec bytes 718a1094
+ 00835544 bytes 8f8a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1c126961728a19e0a44cbca7173f8a"></a>

### [`00835500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md) → [`00835558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md) FUN_00835558

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083558c",
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
      "0083558c",
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


#### 変更候補の命令位置

- 旧版 [`0083551c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md#insn-0083551c) · [`00835528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md#insn-00835528) · [`0083552c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md#insn-0083552c)
- 新版 `00835574`（命令位置の公開資料なし） · `00835580`（命令位置の公開資料なし）

~~~diff
- 0083551c ["INT_ADD", "register:40f0:8", ["const:83551c:8", "const:4:8"]]
- 0083551c ["CALL", null, ["callee:00c57f60:8"]]
+ 00835574 ["INT_ADD", "register:40f0:8", ["const:835574:8", "const:4:8"]]
+ 00835574 ["CALL", null, ["callee:00c57f60:8"]]
- 0083551c bytes 5d8a1094
+ 00835574 bytes 7b8a1094
- 00835528 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00835528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00835528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00835528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00835580 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00835580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00835580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00835580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00835528 bytes 08a12e91
+ 00835580 bytes 08e13191
- 0083552c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0083552c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fad30cee4d7ad73a27e26a70239c0d6e"></a>

### [`00835604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md) → [`0083565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md) FUN_0083565c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083568c",
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
      "0083568c",
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


#### 変更候補の命令位置

- 旧版 [`0083562c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md#insn-0083562c) · [`0083566c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md#insn-0083566c) · [`008356a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md#insn-008356a8)
- 新版 `00835684`（命令位置の公開資料なし） · `008356c4`（命令位置の公開資料なし） · `00835700`（命令位置の公開資料なし）

~~~diff
- 0083562c ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 0083562c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083562c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083562c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00835684 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00835684 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00835684 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00835684 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083562c bytes 4aa12e91
+ 00835684 bytes 4ae13191
- 0083566c ["INT_ADD", "register:40f0:8", ["const:83566c:8", "const:4:8"]]
- 0083566c ["CALL", null, ["callee:00c57f60:8"]]
+ 008356c4 ["INT_ADD", "register:40f0:8", ["const:8356c4:8", "const:4:8"]]
+ 008356c4 ["CALL", null, ["callee:00c57f60:8"]]
- 0083566c bytes 098a1094
+ 008356c4 bytes 278a1094
- 008356a8 ["INT_ADD", "register:40f0:8", ["const:8356a8:8", "const:4:8"]]
- 008356a8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00835700 ["INT_ADD", "register:40f0:8", ["const:835700:8", "const:4:8"]]
+ 00835700 ["CALL", null, ["callee:00c580d0:8"]]
- 008356a8 bytes 568a1094
+ 00835700 bytes 748a1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab98bb3893b8f083ed1113ae63d099a7"></a>

### [`00835918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835918.md) → [`00835970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835970.md) FUN_00835970

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835980",
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
      "00835980",
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


#### 変更候補の命令位置

- 旧版 [`00835924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835918.md#insn-00835924)
- 新版 `0083597c`（命令位置の公開資料なし）

~~~diff
- 00835924 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00835924 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00835924 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00835924 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083597c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0083597c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083597c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083597c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00835924 bytes 29a13091
+ 0083597c bytes 29e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f52baab93d7ee32f2eb8e704b0d021"></a>

### [`0083597c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083597c.md) → [`008359d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008359d4.md) FUN_008359d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835a08",
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
      "00835a08",
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


#### 変更候補の命令位置

- 旧版 [`00835998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083597c.md#insn-00835998) · [`008359a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083597c.md#insn-008359a4) · [`008359a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083597c.md#insn-008359a8)
- 新版 `008359f0`（命令位置の公開資料なし） · `008359fc`（命令位置の公開資料なし）

~~~diff
- 00835998 ["INT_ADD", "register:40f0:8", ["const:835998:8", "const:4:8"]]
- 00835998 ["CALL", null, ["callee:00c57f60:8"]]
+ 008359f0 ["INT_ADD", "register:40f0:8", ["const:8359f0:8", "const:4:8"]]
+ 008359f0 ["CALL", null, ["callee:00c57f60:8"]]
- 00835998 bytes 3e891094
+ 008359f0 bytes 5c891094
- 008359a4 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 008359a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008359a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008359a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008359fc ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 008359fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008359fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008359fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008359a4 bytes 08a13091
+ 008359fc bytes 08e13391
- 008359a8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 008359a8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01bc72328e1f7598822fd3b712ce8969"></a>

### [`00835a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835a80.md) → [`00835ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835ad8.md) FUN_00835ad8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835b08",
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
      "00835b08",
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


#### 変更候補の命令位置

- 旧版 [`00835aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835a80.md#insn-00835aa8) · [`00835ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835a80.md#insn-00835ae8) · [`00835b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835a80.md#insn-00835b24)
- 新版 `00835b00`（命令位置の公開資料なし） · `00835b40`（命令位置の公開資料なし） · `00835b7c`（命令位置の公開資料なし）

~~~diff
- 00835aa8 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00835aa8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00835aa8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00835aa8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00835b00 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00835b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00835b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00835b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00835aa8 bytes 4aa13091
+ 00835b00 bytes 4ae13391
- 00835ae8 ["INT_ADD", "register:40f0:8", ["const:835ae8:8", "const:4:8"]]
- 00835ae8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00835b40 ["INT_ADD", "register:40f0:8", ["const:835b40:8", "const:4:8"]]
+ 00835b40 ["CALL", null, ["callee:00c57f60:8"]]
- 00835ae8 bytes ea881094
+ 00835b40 bytes 08891094
- 00835b24 ["INT_ADD", "register:40f0:8", ["const:835b24:8", "const:4:8"]]
- 00835b24 ["CALL", null, ["callee:00c580d0:8"]]
+ 00835b7c ["INT_ADD", "register:40f0:8", ["const:835b7c:8", "const:4:8"]]
+ 00835b7c ["CALL", null, ["callee:00c580d0:8"]]
- 00835b24 bytes 37891094
+ 00835b7c bytes 55891094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16870dd48b513fed8eb20d9cabff6ce1"></a>

### [`00835bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835bb8.md) → [`00835c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md) FUN_00835c10

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`0055a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5e4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008628a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/008628a8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`0055a624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a624.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00862900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862900.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835c94",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00835c98",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00835ca0",
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
      "00835c94",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00835c98",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00835ca0",
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


#### 変更候補の命令位置

- 旧版 [`00835c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835bb8.md#insn-00835c54) · [`00835be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835bb8.md#insn-00835be0) · [`00835bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835bb8.md#insn-00835bec)
- 新版 `00835cac`（命令位置の公開資料なし） · `00835c38`（命令位置の公開資料なし） · `00835c44`（命令位置の公開資料なし）

~~~diff
- 00835c54 ["INT_ADD", "register:40f0:8", ["const:835c54:8", "const:4:8"]]
- 00835c54 ["CALL", null, ["callee:00c586e0:8"]]
+ 00835cac ["INT_ADD", "register:40f0:8", ["const:835cac:8", "const:4:8"]]
+ 00835cac ["CALL", null, ["callee:00c586e0:8"]]
- 00835c54 bytes 6f8a1094
+ 00835cac bytes 8d8a1094
- 00835be0 ["INT_ADD", "register:40f0:8", ["const:835be0:8", "const:4:8"]]
- 00835be0 ["CALL", null, ["callee:008b92e8:8"]]
+ 00835c38 ["INT_ADD", "register:40f0:8", ["const:835c38:8", "const:4:8"]]
+ 00835c38 ["CALL", null, ["callee:008b92e8:8"]]
- 00835be0 bytes ac0d0294
+ 00835c38 bytes ac0d0294
- 00835bec ["INT_ADD", "register:40f0:8", ["const:835bec:8", "const:4:8"]]
- 00835bec ["CALL", null, ["callee:008b92f0:8"]]
+ 00835c44 ["INT_ADD", "register:40f0:8", ["const:835c44:8", "const:4:8"]]
+ 00835c44 ["CALL", null, ["callee:008b92f0:8"]]
- 00835bec bytes ab0d0294
+ 00835c44 bytes ab0d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0aa0e4ba536edcfae2d44f1131ddef8"></a>

### [`00835d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d6c.md) → [`00835dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835dc4.md) FUN_00835dc4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835ddc",
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
      "00835ddc",
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


#### 変更候補の命令位置

- 旧版 [`00835d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d6c.md#insn-00835d78) · [`00835d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d6c.md#insn-00835d80)
- 新版 `00835dd0`（命令位置の公開資料なし） · `00835dd8`（命令位置の公開資料なし）

~~~diff
- 00835d78 ["INT_ADD", "register:40f0:8", ["const:835d78:8", "const:4:8"]]
- 00835d78 ["CALL", null, ["callee:00c57f60:8"]]
+ 00835dd0 ["INT_ADD", "register:40f0:8", ["const:835dd0:8", "const:4:8"]]
+ 00835dd0 ["CALL", null, ["callee:00c57f60:8"]]
- 00835d78 bytes 46881094
+ 00835dd0 bytes 64881094
- 00835d80 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00835d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00835d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00835d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00835dd8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00835dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00835dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00835dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00835d80 bytes 08a13291
+ 00835dd8 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9393847917240ab50811ff7960c987e4"></a>

### [`00835d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d90.md) → [`00835de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835de8.md) FUN_00835de8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835df0",
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
      "00835df0",
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


#### 変更候補の命令位置

- 旧版 [`00835d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d90.md#insn-00835d94)
- 新版 `00835dec`（命令位置の公開資料なし）

~~~diff
- 00835d94 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00835d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00835d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00835d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00835dec ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00835dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00835dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00835dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00835d94 bytes 08a13291
+ 00835dec bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a9287fe30d60264061092ddd351a959"></a>

### [`00835da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835da8.md) → [`00835e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e00.md) FUN_00835e00

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00835e24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00835e24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00835dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835da8.md#insn-00835dcc) · [`00835dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835da8.md#insn-00835dd8)
- 新版 `00835e24`（命令位置の公開資料なし） · `00835e30`（命令位置の公開資料なし）

~~~diff
- 00835dcc ["INT_ADD", "register:40f0:8", ["const:835dcc:8", "const:4:8"]]
- 00835dcc ["CALL", null, ["ram:47acf4:8"]]
+ 00835e24 ["INT_ADD", "register:40f0:8", ["const:835e24:8", "const:4:8"]]
+ 00835e24 ["CALL", null, ["ram:47ad34:8"]]
- 00835dcc bytes ca13f197
+ 00835e24 bytes c413f197
- 00835dd8 ["INT_ADD", "register:40f0:8", ["const:835dd8:8", "const:4:8"]]
- 00835dd8 ["CALL", null, ["callee:0047ce14:8"]]
+ 00835e30 ["INT_ADD", "register:40f0:8", ["const:835e30:8", "const:4:8"]]
+ 00835e30 ["CALL", null, ["callee:0047ce14:8"]]
- 00835dd8 bytes ff1bf197
+ 00835e30 bytes f91bf197
~~~


<a id="compare-4f224810783d964c59fbf373fe8c1d63"></a>

### [`00835fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fcc.md) → [`00836024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836024.md) FUN_00836024

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00835e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835e18.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00835e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e70.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00836030",
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
      "00836030",
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


#### 変更候補の命令位置

- 旧版 [`00835fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fcc.md#insn-00835fdc) · [`00835fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fcc.md#insn-00835fd8)
- 新版 `00836034`（命令位置の公開資料なし） · `00836030`（命令位置の公開資料なし）

~~~diff
- 00835fdc ["INT_ADD", "register:40f0:8", ["const:835fdc:8", "const:4:8"]]
- 00835fdc ["CALL", null, ["callee:0043b7b8:8"]]
+ 00836034 ["INT_ADD", "register:40f0:8", ["const:836034:8", "const:4:8"]]
+ 00836034 ["CALL", null, ["callee:0043b7b8:8"]]
- 00835fdc bytes e715f097
+ 00836034 bytes e115f097
- 00835fd8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00835fd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00835fd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00835fd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00836030 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00836030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00836030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00836030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00835fd8 bytes 00303d91
+ 00836030 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e231f12f06ac0b343aedfd2f033ac72d"></a>

### [`008378d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md) → [`00837930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md) FUN_00837930

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0067e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md) [`00862c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/00862c50.md) [`00864538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864538.md)
- 新版 呼出元 1件 [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0067e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e1dc.md) [`00862ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862ca8.md) [`00864590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864590.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.05% / 新版 85.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00837974",
      "DATA",
      [
        "storage",
        "00c7ed38",
        null,
        "pointer"
      ]
    ],
    [
      "00837984",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008379a4",
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
      "00837974",
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      "00837984",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008379a4",
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


#### 変更候補の命令位置

- 旧版 [`00837920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md#insn-00837920) · [`00837998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md#insn-00837998) · [`008379cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md#insn-008379cc)
- 新版 `00837978`（命令位置の公開資料なし） · `008379f0`（命令位置の公開資料なし） · `00837a24`（命令位置の公開資料なし）

~~~diff
- 00837920 ["COPY", "register:40c0:8", ["const:ca4000:8"]]
+ 00837978 ["COPY", "register:40c0:8", ["const:ca5000:8"]]
- 00837920 bytes 782300b0
+ 00837978 bytes 782300d0
- 00837998 ["INT_ADD", "register:40f0:8", ["const:837998:8", "const:4:8"]]
- 00837998 ["CALL", null, ["callee:0047e64c:8"]]
+ 008379f0 ["INT_ADD", "register:40f0:8", ["const:8379f0:8", "const:4:8"]]
+ 008379f0 ["CALL", null, ["callee:0047e64c:8"]]
- 00837998 bytes 1d1bf197
+ 008379f0 bytes 171bf197
- 008379cc ["COPY", "register:0:8", ["register:4040:8"]]
- 008379cc ["INT_ADD", "register:40f0:8", ["const:8379cc:8", "const:4:8"]]
- 008379cc ["CALLIND", null, ["register:0:8"]]
+ 00837a24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00837a24 ["INT_ADD", "register:40f0:8", ["const:837a24:8", "const:4:8"]]
+ 00837a24 ["CALLIND", null, ["register:0:8"]]
- 008379cc bytes 00013fd6
+ 00837a24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e748c1394f138742a19d5863924e651"></a>

### [`00838888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838888.md) → [`008388e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008388e0.md) FUN_008388e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008388fc",
      "DATA",
      [
        "storage",
        "00c7ed38",
        null,
        "pointer"
      ]
    ],
    [
      "00838968",
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
      "008388fc",
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      "00838968",
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


#### 変更候補の命令位置

- 旧版 [`008388a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838888.md#insn-008388a0) · [`008388b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838888.md#insn-008388b4) · [`008388c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838888.md#insn-008388c8)
- 新版 `008388f8`（命令位置の公開資料なし） · `0083890c`（命令位置の公開資料なし） · `00838920`（命令位置の公開資料なし）

~~~diff
- 008388a0 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 008388a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008388a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008388a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008388f8 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 008388f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008388f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008388f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008388a0 bytes 08e13491
+ 008388f8 bytes 08213891
- 008388b4 ["INT_ADD", "register:40f0:8", ["const:8388b4:8", "const:4:8"]]
- 008388b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0083890c ["INT_ADD", "register:40f0:8", ["const:83890c:8", "const:4:8"]]
+ 0083890c ["CALL", null, ["callee:00c53da0:8"]]
- 008388b4 bytes 136d1094
+ 0083890c bytes 256d1094
- 008388c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008388c8 ["INT_ADD", "register:40f0:8", ["const:8388c8:8", "const:4:8"]]
- 008388c8 ["CALLIND", null, ["register:0:8"]]
+ 00838920 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00838920 ["INT_ADD", "register:40f0:8", ["const:838920:8", "const:4:8"]]
+ 00838920 ["CALLIND", null, ["register:0:8"]]
- 008388c8 bytes 00013fd6
+ 00838920 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77479d72c5f62c0ad4b88e2f8991326b"></a>

### [`00838950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838950.md) → [`008389a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008389a8.md) FUN_008389a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008389c4",
      "DATA",
      [
        "storage",
        "00c7ed38",
        null,
        "pointer"
      ]
    ],
    [
      "00838a30",
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
      "008389c4",
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      "00838a30",
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


#### 変更候補の命令位置

- 旧版 [`00838968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838950.md#insn-00838968) · [`0083897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838950.md#insn-0083897c) · [`00838990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838950.md#insn-00838990)
- 新版 `008389c0`（命令位置の公開資料なし） · `008389d4`（命令位置の公開資料なし） · `008389e8`（命令位置の公開資料なし）

~~~diff
- 00838968 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00838968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008389c0 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 008389c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008389c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008389c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838968 bytes 08e13491
+ 008389c0 bytes 08213891
- 0083897c ["INT_ADD", "register:40f0:8", ["const:83897c:8", "const:4:8"]]
- 0083897c ["CALL", null, ["callee:00c53da0:8"]]
+ 008389d4 ["INT_ADD", "register:40f0:8", ["const:8389d4:8", "const:4:8"]]
+ 008389d4 ["CALL", null, ["callee:00c53da0:8"]]
- 0083897c bytes e16c1094
+ 008389d4 bytes f36c1094
- 00838990 ["COPY", "register:0:8", ["register:4040:8"]]
- 00838990 ["INT_ADD", "register:40f0:8", ["const:838990:8", "const:4:8"]]
- 00838990 ["CALLIND", null, ["register:0:8"]]
+ 008389e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008389e8 ["INT_ADD", "register:40f0:8", ["const:8389e8:8", "const:4:8"]]
+ 008389e8 ["CALLIND", null, ["register:0:8"]]
- 00838990 bytes 00013fd6
+ 008389e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a222d86f539b1f6652db8524e32b16e0"></a>

### [`00838a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a24.md) → [`00838a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838a7c.md) FUN_00838a7c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838aa0",
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
      "00838aa0",
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


#### 変更候補の命令位置

- 旧版 [`00838a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a24.md#insn-00838a38) · [`00838a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a24.md#insn-00838a44)
- 新版 `00838a90`（命令位置の公開資料なし） · `00838a9c`（命令位置の公開資料なし）

~~~diff
- 00838a38 ["INT_ADD", "register:40f0:8", ["const:838a38:8", "const:4:8"]]
- 00838a38 ["CALL", null, ["callee:00c57f60:8"]]
+ 00838a90 ["INT_ADD", "register:40f0:8", ["const:838a90:8", "const:4:8"]]
+ 00838a90 ["CALL", null, ["callee:00c57f60:8"]]
- 00838a38 bytes 167d1094
+ 00838a90 bytes 347d1094
- 00838a44 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00838a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00838a9c ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00838a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00838a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00838a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838a44 bytes 08613591
+ 00838a9c bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ae17b10b8bf89b24094f3ce2b52dd3"></a>

### [`00838a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a58.md) → [`00838ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ab0.md) FUN_00838ab0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838abc",
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
      "00838abc",
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


#### 変更候補の命令位置

- 旧版 [`00838a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a58.md#insn-00838a60)
- 新版 `00838ab8`（命令位置の公開資料なし）

~~~diff
- 00838a60 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00838a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838ab8 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00838ab8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838ab8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838ab8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838a60 bytes 29613591
+ 00838ab8 bytes 29a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b9d72f06c3e76e8077cbbe53fff99c"></a>

### [`00838ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ac0.md) → [`00838b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b18.md) FUN_00838b18

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838b3c",
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
      "00838b3c",
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


#### 変更候補の命令位置

- 旧版 [`00838ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ac0.md#insn-00838ad4) · [`00838ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ac0.md#insn-00838ae0)
- 新版 `00838b2c`（命令位置の公開資料なし） · `00838b38`（命令位置の公開資料なし）

~~~diff
- 00838ad4 ["INT_ADD", "register:40f0:8", ["const:838ad4:8", "const:4:8"]]
- 00838ad4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00838b2c ["INT_ADD", "register:40f0:8", ["const:838b2c:8", "const:4:8"]]
+ 00838b2c ["CALL", null, ["callee:00c57f60:8"]]
- 00838ad4 bytes ef7c1094
+ 00838b2c bytes 0d7d1094
- 00838ae0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00838ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00838b38 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00838b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00838b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00838b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838ae0 bytes 08613791
+ 00838b38 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-385f0d7daf92cd538ada8996ce4a578c"></a>

### [`00838af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838af4.md) → [`00838b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b4c.md) FUN_00838b4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838b58",
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
      "00838b58",
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


#### 変更候補の命令位置

- 旧版 [`00838afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838af4.md#insn-00838afc)
- 新版 `00838b54`（命令位置の公開資料なし）

~~~diff
- 00838afc ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00838afc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838afc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838afc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838b54 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00838b54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838b54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838b54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838afc bytes 29613791
+ 00838b54 bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0771fbd4180bbcf3c47141a569e4e11f"></a>

### [`00838b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b50.md) → [`00838ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ba8.md) FUN_00838ba8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838bcc",
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
      "00838bcc",
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


#### 変更候補の命令位置

- 旧版 [`00838b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b50.md#insn-00838b64) · [`00838b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b50.md#insn-00838b70)
- 新版 `00838bbc`（命令位置の公開資料なし） · `00838bc8`（命令位置の公開資料なし）

~~~diff
- 00838b64 ["INT_ADD", "register:40f0:8", ["const:838b64:8", "const:4:8"]]
- 00838b64 ["CALL", null, ["callee:00c57f60:8"]]
+ 00838bbc ["INT_ADD", "register:40f0:8", ["const:838bbc:8", "const:4:8"]]
+ 00838bbc ["CALL", null, ["callee:00c57f60:8"]]
- 00838b64 bytes cb7c1094
+ 00838bbc bytes e97c1094
- 00838b70 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00838b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00838bc8 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00838bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00838bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00838bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838b70 bytes 08613991
+ 00838bc8 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a10358a1213dc1e177908771507be074"></a>

### [`00838b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b84.md) → [`00838bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bdc.md) FUN_00838bdc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838be8",
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
      "00838be8",
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


#### 変更候補の命令位置

- 旧版 [`00838b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b84.md#insn-00838b8c)
- 新版 `00838be4`（命令位置の公開資料なし）

~~~diff
- 00838b8c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00838b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838be4 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00838be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838b8c bytes 29613991
+ 00838be4 bytes 29a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82adde48855d5b19efd6afec2d28ebd6"></a>

### [`00838ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md) → [`00838bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md) FUN_00838bf8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0082d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md) [`00838d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d00.md) [`00838d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d04.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0082d2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`00838d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d58.md) [`00838d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d5c.md) [`00acac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838c2c",
      "DATA",
      [
        "storage",
        "00c7eec8",
        null,
        "undefined *"
      ]
    ],
    [
      "00838c68",
      "READ",
      [
        "storage",
        "00c7eee8",
        null,
        "pointer"
      ]
    ],
    [
      "00838c68",
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
      "00838c2c",
      "DATA",
      [
        "storage",
        "00c7ef98",
        null,
        "undefined *"
      ]
    ],
    [
      "00838c68",
      "READ",
      [
        "storage",
        "00c7efb8",
        null,
        "pointer"
      ]
    ],
    [
      "00838c68",
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


#### 変更候補の命令位置

- 旧版 [`00838bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md#insn-00838bc4) · [`00838bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md#insn-00838bcc) · [`00838be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md#insn-00838be8)
- 新版 `00838c1c`（命令位置の公開資料なし） · `00838c24`（命令位置の公開資料なし） · `00838c40`（命令位置の公開資料なし）

~~~diff
- 00838bc4 ["INT_ADD", "register:40f0:8", ["const:838bc4:8", "const:4:8"]]
- 00838bc4 ["CALL", null, ["callee:0082d2e8:8"]]
+ 00838c1c ["INT_ADD", "register:40f0:8", ["const:838c1c:8", "const:4:8"]]
+ 00838c1c ["CALL", null, ["callee:0082d2e8:8"]]
- 00838bc4 bytes b3d1ff97
+ 00838c1c bytes b3d1ff97
- 00838bcc ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 00838bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00838c24 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00838c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00838c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00838c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838bcc bytes 08213b91
+ 00838c24 bytes 08613e91
- 00838be8 ["INT_ADD", "register:40f0:8", ["const:838be8:8", "const:4:8"]]
- 00838be8 ["CALL", null, ["callee:00acac44:8"]]
+ 00838c40 ["INT_ADD", "register:40f0:8", ["const:838c40:8", "const:4:8"]]
+ 00838c40 ["CALL", null, ["callee:00acac44:8"]]
- 00838be8 bytes fb470a94
+ 00838c40 bytes 01480a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e755cce7aa917a7d1129ad5df444164"></a>

### [`00838cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cb8.md) → [`00838d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d10.md) FUN_00838d10

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838d34",
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
      "00838d34",
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


#### 変更候補の命令位置

- 旧版 [`00838ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cb8.md#insn-00838ccc) · [`00838cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cb8.md#insn-00838cd8)
- 新版 `00838d24`（命令位置の公開資料なし） · `00838d30`（命令位置の公開資料なし）

~~~diff
- 00838ccc ["INT_ADD", "register:40f0:8", ["const:838ccc:8", "const:4:8"]]
- 00838ccc ["CALL", null, ["callee:00c57f60:8"]]
+ 00838d24 ["INT_ADD", "register:40f0:8", ["const:838d24:8", "const:4:8"]]
+ 00838d24 ["CALL", null, ["callee:00c57f60:8"]]
- 00838ccc bytes 717c1094
+ 00838d24 bytes 8f7c1094
- 00838cd8 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 00838cd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00838cd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00838cd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00838d30 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00838d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00838d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00838d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00838cd8 bytes 08213b91
+ 00838d30 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb59043e82895c001d922bb5e38e7fd"></a>

### [`00838cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cec.md) → [`00838d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d44.md) FUN_00838d44

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838d50",
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
      "00838d50",
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


#### 変更候補の命令位置

- 旧版 [`00838cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cec.md#insn-00838cf4)
- 新版 `00838d4c`（命令位置の公開資料なし）

~~~diff
- 00838cf4 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 00838cf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838cf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838cf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838d4c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00838d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838cf4 bytes 29213b91
+ 00838d4c bytes 29613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9922613db618fa71677eb46e604bfd5"></a>

### [`00838d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d08.md) → [`00838d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d60.md) FUN_00838d60

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`007562a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bb70.md) [`00ac863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac863c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085bbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bbc8.md) [`00ac86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac86ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_value, call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00838d98",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00838d9c",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "00838da4",
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
      "00838d98",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00838d9c",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00838da4",
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


#### 変更候補の命令位置

- 旧版 [`00838d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d08.md#insn-00838d20) · [`00838d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d08.md#insn-00838d4c) · [`00838d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d08.md#insn-00838d50)
- 新版 `00838d78`（命令位置の公開資料なし） · `00838da4`（命令位置の公開資料なし） · `00838da8`（命令位置の公開資料なし）

~~~diff
- 00838d20 ["INT_ADD", "register:40f0:8", ["const:838d20:8", "const:4:8"]]
- 00838d20 ["CALL", null, ["callee:00851550:8"]]
+ 00838d78 ["INT_ADD", "register:40f0:8", ["const:838d78:8", "const:4:8"]]
+ 00838d78 ["CALL", null, ["callee:00851550:8"]]
- 00838d20 bytes f6610094
+ 00838d78 bytes f6610094
- 00838d4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
- 00838d4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00838da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 00838da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00838d4c bytes 09b504f9
+ 00838da4 bytes 093505f9
- 00838d50 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
- 00838d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00838da8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 00838da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00838d50 bytes cabe04f9
+ 00838da8 bytes ca3e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

