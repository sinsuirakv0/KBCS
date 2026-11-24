# v16.0.2 → v16.0.3 · 最優先の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-248b4889a80453a5d6365e6825a5eab2"></a>

### [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) → [`00489524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/00489524.md) FUN_00489524

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004891d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004891d4.md) [`00635b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00635/00635b20.md) · 呼出先 15件 [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`004881b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004881b8.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 2件 [`004894f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/004894f4.md) [`00635ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00635/00635ed0.md) · 呼出先 15件 [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004884d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004884d8.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00489564",
      "incomplete_value": false,
      "site": "0048956c",
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
      "definition_site": "00489244",
      "incomplete_value": false,
      "site": "0048924c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048972c",
      "incomplete_value": true,
      "site": "00489730",
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
      "definition_site": "0048940c",
      "incomplete_value": true,
      "site": "00489410",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00489728",
      "incomplete_value": true,
      "site": "00489734",
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
      "definition_site": "00489408",
      "incomplete_value": true,
      "site": "00489414",
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
      "0048956c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00489708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004896dc"
      ]
    ],
    [
      "00489718",
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
      "0048956c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00489708",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004899fc"
      ]
    ],
    [
      "00489718",
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


#### 変更候補の命令位置

- 旧版 [`004893e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md#insn-004893e8) · [`0048923c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md#insn-0048923c) · [`00489240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md#insn-00489240)
- 新版 [`00489708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/00489524.md#insn-00489708) · [`0048955c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/00489524.md#insn-0048955c) · [`00489560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/00489524.md#insn-00489560)

~~~diff
- 004893e8 ["INT_ADD", "register:40f0:8", ["const:4893e8:8", "const:4:8"]]
- 004893e8 ["CALL", null, ["ram:4896dc:8"]]
+ 00489708 ["INT_ADD", "register:40f0:8", ["const:489708:8", "const:4:8"]]
+ 00489708 ["CALL", null, ["ram:4899fc:8"]]
- 004893e8 bytes bd000094
+ 00489708 bytes bd000094
- 0048923c ["INT_ADD", "register:40f0:8", ["const:48923c:8", "const:4:8"]]
- 0048923c ["CALL", null, ["callee:00488180:8"]]
+ 0048955c ["INT_ADD", "register:40f0:8", ["const:48955c:8", "const:4:8"]]
+ 0048955c ["CALL", null, ["callee:00488180:8"]]
- 0048923c bytes 09fbff97
+ 0048955c bytes 09fbff97
- 00489240 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00489560 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00489240 bytes c83e00f0
+ 00489560 bytes e83e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e685d81dd7fff35e0402b4eb4ffa50"></a>

### [`00489fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md) → [`0048a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md) FUN_0048a2d0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0048a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a77c.md) [`0048a874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a874.md) · 呼出先 21件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048a6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a6d0.md) [`0048a72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a72c.md) [`0048b624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b624.md) [`0048b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b838.md)
- 新版 呼出元 2件 [`0048aa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa9c.md) [`0048ab94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048ab94.md) · 呼出先 21件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0048a9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a9f0.md) [`0048aa4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa4c.md) [`0048b944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b944.md) [`0048bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048bb58.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 79.67% / 新版 79.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `call_target` 3件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0048a4e0",
      "incomplete_value": true,
      "site": "0048a4e4",
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
                "register:4000:8"
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
      "definition_site": "0048a1c0",
      "incomplete_value": true,
      "site": "0048a1c4",
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
                "register:4000:8"
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
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048a304",
      "incomplete_value": false,
      "site": "0048a310",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00489fe4",
      "incomplete_value": false,
      "site": "00489ff0",
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
            "const:150:8"
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
      "site": "0048a320",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048a000",
      "value": [
        "leaf",
        "ram:48cd38:8"
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
      "0048a304",
      "PARAM",
      [
        "storage",
        "00ca5150",
        null,
        null
      ]
    ],
    [
      "0048a320",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0048a324",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004939b8"
      ]
    ]
  ],
  "added": [
    [
      "0048a304",
      "PARAM",
      [
        "storage",
        "00ca6110",
        null,
        null
      ]
    ],
    [
      "0048a320",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "0048a324",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00493cd8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md#insn-00489ff0) · [`0048a000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md#insn-0048a000) · [`0048a004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md#insn-0048a004)
- 新版 [`0048a310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md#insn-0048a310) · [`0048a320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md#insn-0048a320) · [`0048a324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md#insn-0048a324)

~~~diff
- 00489ff0 ["INT_ADD", "register:40f0:8", ["const:489ff0:8", "const:4:8"]]
- 00489ff0 ["CALL", null, ["callee:00c59180:8"]]
+ 0048a310 ["INT_ADD", "register:40f0:8", ["const:48a310:8", "const:4:8"]]
+ 0048a310 ["CALL", null, ["callee:00c59180:8"]]
- 00489ff0 bytes 70381f94
+ 0048a310 bytes 9c3b1f94
- 0048a000 ["INT_ADD", "register:40f0:8", ["const:48a000:8", "const:4:8"]]
- 0048a000 ["CALL", null, ["ram:48cd38:8"]]
+ 0048a320 ["INT_ADD", "register:40f0:8", ["const:48a320:8", "const:4:8"]]
+ 0048a320 ["CALL", null, ["ram:48d058:8"]]
- 0048a000 bytes 4e0b0094
+ 0048a320 bytes 4e0b0094
- 0048a004 ["INT_ADD", "register:40f0:8", ["const:48a004:8", "const:4:8"]]
- 0048a004 ["CALL", null, ["ram:4939b8:8"]]
+ 0048a324 ["INT_ADD", "register:40f0:8", ["const:48a324:8", "const:4:8"]]
+ 0048a324 ["CALL", null, ["ram:493cd8:8"]]
- 0048a004 bytes 6d260094
+ 0048a324 bytes 6d260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8814db232ca5e44bfcbc23e9fb15045f"></a>

### [`0048a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a77c.md) → [`0048aa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa9c.md) FUN_0048aa9c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`00631334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00631/00631334.md) [`0066d6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d6e0.md) [`0073ee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073ee8c.md) [`0074c928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0074c/0074c928.md) [`007538cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/007538cc.md) · 呼出先 4件 [`00489fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489fb0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 11件 [`006316e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00631/006316e4.md) [`0066da90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066da90.md) [`0073f23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f23c.md) [`0074ccd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0074c/0074ccd8.md) [`00753c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00753/00753c7c.md) · 呼出先 4件 [`0048a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2d0.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048aabc",
      "incomplete_value": false,
      "site": "0048aacc",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048a79c",
      "incomplete_value": false,
      "site": "0048a7ac",
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
            "const:c0:8"
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
      "0048aabc",
      "PARAM",
      [
        "storage",
        "00ca50c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0048aabc",
      "PARAM",
      [
        "storage",
        "00ca6080",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048a7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a77c.md#insn-0048a7ac) · [`0048a798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a77c.md#insn-0048a798) · [`0048a79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a77c.md#insn-0048a79c)
- 新版 [`0048aacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa9c.md#insn-0048aacc) · [`0048aab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa9c.md#insn-0048aab8) · [`0048aabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048aa9c.md#insn-0048aabc)

~~~diff
- 0048a7ac ["INT_ADD", "register:40f0:8", ["const:48a7ac:8", "const:4:8"]]
- 0048a7ac ["CALL", null, ["callee:0048a2d0:8"]]
+ 0048aacc ["INT_ADD", "register:40f0:8", ["const:48aacc:8", "const:4:8"]]
+ 0048aacc ["CALL", null, ["callee:0048a2d0:8"]]
- 0048a7ac bytes 01feff97
+ 0048aacc bytes 01feff97
- 0048a798 ["COPY", "register:4000:8", ["const:ca5000:8"]]
+ 0048aab8 ["COPY", "register:4000:8", ["const:ca6000:8"]]
- 0048a798 bytes c04000f0
+ 0048aab8 bytes e0400090
- 0048a79c ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0048a79c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048a79c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048a79c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048aabc ["COPY", "tmp:0:8", ["const:80:8"]]
+ 0048aabc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048aabc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048aabc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048a79c bytes 00000391
+ 0048aabc bytes 00000291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4773d95cc2067558a43bf1c20c51c3ed"></a>

### [`0048ac60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac60.md) → [`0048af80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048af80.md) FUN_0048af80

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008536f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/008536f8.md) · 呼出先 4件 [`004894e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md) [`004896dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004896dc.md) [`0048aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048aa90.md) [`0055e664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e664.md)
- 新版 呼出元 1件 [`008546a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00854/008546a4.md) · 呼出先 4件 [`00489808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/00489808.md) [`004899fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00489/004899fc.md) [`0048adb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048adb0.md) [`0055e984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055e984.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "0048afe4",
      "value": [
        "leaf",
        "ram:4899fc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048acc4",
      "value": [
        "leaf",
        "ram:4896dc:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048afe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004896dc"
      ]
    ]
  ],
  "added": [
    [
      "0048afe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004899fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048acc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac60.md#insn-0048acc4) · [`0048ac78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac60.md#insn-0048ac78) · [`0048acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac60.md#insn-0048acb0)
- 新版 [`0048afe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048af80.md#insn-0048afe4) · [`0048af98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048af80.md#insn-0048af98) · [`0048afd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048af80.md#insn-0048afd0)

~~~diff
- 0048acc4 ["INT_ADD", "register:40f0:8", ["const:48acc4:8", "const:4:8"]]
- 0048acc4 ["CALL", null, ["ram:4896dc:8"]]
+ 0048afe4 ["INT_ADD", "register:40f0:8", ["const:48afe4:8", "const:4:8"]]
+ 0048afe4 ["CALL", null, ["ram:4899fc:8"]]
- 0048acc4 bytes 86faff97
+ 0048afe4 bytes 86faff97
- 0048ac78 ["INT_ADD", "register:40f0:8", ["const:48ac78:8", "const:4:8"]]
- 0048ac78 ["CALL", null, ["callee:0055e984:8"]]
+ 0048af98 ["INT_ADD", "register:40f0:8", ["const:48af98:8", "const:4:8"]]
+ 0048af98 ["CALL", null, ["callee:0055e984:8"]]
- 0048ac78 bytes 7b4e0394
+ 0048af98 bytes 7b4e0394
- 0048acb0 ["INT_ADD", "register:40f0:8", ["const:48acb0:8", "const:4:8"]]
- 0048acb0 ["CALL", null, ["callee:0048adb0:8"]]
+ 0048afd0 ["INT_ADD", "register:40f0:8", ["const:48afd0:8", "const:4:8"]]
+ 0048afd0 ["CALL", null, ["callee:0048adb0:8"]]
- 0048acb0 bytes 78ffff97
+ 0048afd0 bytes 78ffff97
~~~


<a id="compare-5035fee3348db3628a46c70c052e7bac"></a>

### [`0048b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b3d0.md) → [`0048b6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b6f0.md) FUN_0048b6f0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008519ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/008519ac.md) [`00b2c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md) · 呼出先 1件 [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)
- 新版 呼出元 2件 [`00852958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852958.md) [`00b2d290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2d290.md) · 呼出先 1件 [`00c594d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594d0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b708",
      "incomplete_value": true,
      "site": "0048b708",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b3e8",
      "incomplete_value": true,
      "site": "0048b3e8",
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
            "const:a8:8"
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
      "definition_site": "0048b724",
      "incomplete_value": true,
      "site": "0048b724",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0048b404",
      "incomplete_value": true,
      "site": "0048b404",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b728",
      "incomplete_value": false,
      "site": "0048b728",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b408",
      "incomplete_value": false,
      "site": "0048b408",
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
            "const:b0:8"
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
      "0048b6f8",
      "READ",
      [
        "storage",
        "00ca50a8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b704",
      "PARAM",
      [
        "storage",
        "00ca50a8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b708",
      "WRITE",
      [
        "storage",
        "00ca50a8",
        null,
        "undefined2"
      ]
    ]
  ],
  "added": [
    [
      "0048b6f8",
      "READ",
      [
        "storage",
        "00ca6068",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b704",
      "PARAM",
      [
        "storage",
        "00ca6068",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b708",
      "WRITE",
      [
        "storage",
        "00ca6068",
        null,
        "undefined2"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048b3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b3d0.md#insn-0048b3e8) · [`0048b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b3d0.md#insn-0048b3d0) · [`0048b3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b3d0.md#insn-0048b3d8)
- 新版 [`0048b708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b6f0.md#insn-0048b708) · [`0048b6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b6f0.md#insn-0048b6f0) · [`0048b6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b6f0.md#insn-0048b6f8)

~~~diff
- 0048b3e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
- 0048b3e8 ["COPY", "tmp:1:4", ["const:0:4"]]
- 0048b3e8 ["COPY", "tmp:2:4", ["tmp:1:4"]]
- 0048b3e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
+ 0048b708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
+ 0048b708 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 0048b708 ["COPY", "tmp:2:4", ["tmp:1:4"]]
+ 0048b708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
- 0048b3e8 bytes 1f510179
+ 0048b708 bytes 1fd10079
- 0048b3d0 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0048b6f0 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0048b3d0 bytes c84000d0
+ 0048b6f0 bytes c84000f0
- 0048b3d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
- 0048b3d8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0048b3d8 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0048b6f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
+ 0048b6f8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0048b6f8 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 0048b3d8 bytes 09a14239
+ 0048b6f8 bytes 09a14139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcb043740e4a2cbbda3ec60e79739d2b"></a>

### [`0048b584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b584.md) → [`0048b8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b8a4.md) FUN_0048b8a4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0048b410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b410.md) [`00877c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877c78.md) [`00ac878c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac878c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`0048b730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b730.md) [`00878c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878c24.md) [`00ac9780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9780.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0048b8b0",
      "incomplete_value": false,
      "site": "0048b8b4",
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
      "definition_site": "0048b590",
      "incomplete_value": false,
      "site": "0048b594",
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
      "0048b8b0",
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
      "0048b8b0",
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

- 旧版 [`0048b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b584.md#insn-0048b594) · [`0048b58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b584.md#insn-0048b58c) · [`0048b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b584.md#insn-0048b590)
- 新版 [`0048b8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b8a4.md#insn-0048b8b4) · [`0048b8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b8a4.md#insn-0048b8ac) · [`0048b8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048b/0048b8a4.md#insn-0048b8b0)

~~~diff
- 0048b594 ["INT_ADD", "register:40f0:8", ["const:48b594:8", "const:4:8"]]
- 0048b594 ["CALL", null, ["callee:0043bad8:8"]]
+ 0048b8b4 ["INT_ADD", "register:40f0:8", ["const:48b8b4:8", "const:4:8"]]
+ 0048b8b4 ["CALL", null, ["callee:0043bad8:8"]]
- 0048b594 bytes 89c0fe97
+ 0048b8b4 bytes 89c0fe97
- 0048b58c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0048b8ac ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0048b58c bytes 60f1ff90
+ 0048b8ac bytes 60f1ffb0
- 0048b590 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0048b590 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048b590 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048b590 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048b8b0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0048b8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048b590 bytes 00303e91
+ 0048b8b0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e7d3e46ffd99ca0b7c0d9bb7e503db4"></a>

### [`0048c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md) → [`0048c360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048c360.md) FUN_0048c360

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0048c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md) [`008b4ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b4/008b4ae4.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`00944804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00944/00944804.md) [`009a773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 6件 [`0048c360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048c360.md) [`008b5a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b5/008b5a90.md) [`0093c770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0093c/0093c770.md) [`009457b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00945/009457b0.md) [`009a86e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a8/009a86e8.md) · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048c4b8",
      "incomplete_value": false,
      "site": "0048c4c0",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c198",
      "incomplete_value": false,
      "site": "0048c1a0",
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
            "const:f93:8"
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
      "definition_site": "0048c574",
      "incomplete_value": false,
      "site": "0048c57c",
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
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c254",
      "incomplete_value": false,
      "site": "0048c25c",
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
            "const:e27:8"
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
      "definition_site": "0048c58c",
      "incomplete_value": false,
      "site": "0048c598",
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
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c26c",
      "incomplete_value": false,
      "site": "0048c278",
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
            "const:f29:8"
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
      "0048c4b8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0048c574",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0048c58c",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048c4b8",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "0048c574",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "0048c58c",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048c1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md#insn-0048c1a0) · [`0048c25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md#insn-0048c25c) · [`0048c278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md#insn-0048c278)
- 新版 [`0048c4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048c360.md#insn-0048c4c0) · [`0048c57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048c360.md#insn-0048c57c) · [`0048c598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048c360.md#insn-0048c598)

~~~diff
- 0048c1a0 ["INT_ADD", "register:40f0:8", ["const:48c1a0:8", "const:4:8"]]
- 0048c1a0 ["CALL", null, ["callee:004421f4:8"]]
+ 0048c4c0 ["INT_ADD", "register:40f0:8", ["const:48c4c0:8", "const:4:8"]]
+ 0048c4c0 ["CALL", null, ["callee:004421f4:8"]]
- 0048c1a0 bytes 4dd7fe97
+ 0048c4c0 bytes 4dd7fe97
- 0048c25c ["INT_ADD", "register:40f0:8", ["const:48c25c:8", "const:4:8"]]
- 0048c25c ["CALL", null, ["callee:004421f4:8"]]
+ 0048c57c ["INT_ADD", "register:40f0:8", ["const:48c57c:8", "const:4:8"]]
+ 0048c57c ["CALL", null, ["callee:004421f4:8"]]
- 0048c25c bytes 1ed7fe97
+ 0048c57c bytes 1ed7fe97
- 0048c278 ["INT_ADD", "register:40f0:8", ["const:48c278:8", "const:4:8"]]
- 0048c278 ["CALL", null, ["callee:00442b54:8"]]
+ 0048c598 ["INT_ADD", "register:40f0:8", ["const:48c598:8", "const:4:8"]]
+ 0048c598 ["CALL", null, ["callee:00442b54:8"]]
- 0048c278 bytes 6fd9fe97
+ 0048c598 bytes 6fd9fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c158cd33dc7a49360bf2989f592ca6"></a>

### [`0048c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c978.md) → [`0048cc98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048cc98.md) _INIT_21

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048ccd4",
      "incomplete_value": true,
      "site": "0048ccf0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0048c9b4",
      "incomplete_value": true,
      "site": "0048c9d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0048ccf8",
      "incomplete_value": true,
      "site": "0048cd14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0048c9d8",
      "incomplete_value": true,
      "site": "0048c9f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0048cd18",
      "incomplete_value": true,
      "site": "0048cd34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0048c9f8",
      "incomplete_value": true,
      "site": "0048ca14",
      "value": [
        "LOAD",
        "16",
        [
          [
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048ccd4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0048ccf8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0048cd18",
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
      "0048ccd4",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0048ccf8",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0048cd18",
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


#### 変更候補の命令位置

- 旧版 [`0048cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c978.md#insn-0048cad8) · [`0048cbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c978.md#insn-0048cbac) · [`0048c9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c978.md#insn-0048c9a0)
- 新版 [`0048cdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048cc98.md#insn-0048cdf8) · [`0048cecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048cc98.md#insn-0048cecc) · [`0048ccc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048cc98.md#insn-0048ccc0)

~~~diff
- 0048cad8 ["INT_ADD", "register:40f0:8", ["const:48cad8:8", "const:4:8"]]
- 0048cad8 ["CALL", null, ["callee:0043bb58:8"]]
+ 0048cdf8 ["INT_ADD", "register:40f0:8", ["const:48cdf8:8", "const:4:8"]]
+ 0048cdf8 ["CALL", null, ["callee:0043bb58:8"]]
- 0048cad8 bytes 58bbfe97
+ 0048cdf8 bytes 58bbfe97
- 0048cbac ["INT_ADD", "register:40f0:8", ["const:48cbac:8", "const:4:8"]]
- 0048cbac ["CALL", null, ["callee:00c58ed0:8"]]
+ 0048cecc ["INT_ADD", "register:40f0:8", ["const:48cecc:8", "const:4:8"]]
+ 0048cecc ["CALL", null, ["callee:00c58ed0:8"]]
- 0048cbac bytes d52c1f94
+ 0048cecc bytes 01301f94
- 0048c9a0 ["COPY", "register:4098:8", ["const:ca5000:8"]]
+ 0048ccc0 ["COPY", "register:4098:8", ["const:ca6000:8"]]
- 0048c9a0 bytes d34000b0
+ 0048ccc0 bytes d34000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9e6e48f7e12f3cdad4ea691fcec6283"></a>

### [`0048cd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd08.md) → [`0048d028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d028.md) FUN_0048d028

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00840888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840888.md) · 呼出先 0件 

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
      "definition_site": "0048d02c",
      "incomplete_value": false,
      "site": "0048d034",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048cd0c",
      "incomplete_value": false,
      "site": "0048cd14",
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
            "const:9e8:8"
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
      "0048d034",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0048d034",
      "DATA",
      [
        "storage",
        "00c669b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048cd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd08.md#insn-0048cd08) · [`0048cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd08.md#insn-0048cd0c)
- 新版 [`0048d028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d028.md#insn-0048d028) · [`0048d02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d028.md#insn-0048d02c)

~~~diff
- 0048cd08 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 0048d028 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 0048cd08 bytes c83e00b0
+ 0048d028 bytes c83e00b0
- 0048cd0c ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0048cd0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048cd0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048cd0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048d02c ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 0048d02c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d02c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d02c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048cd0c bytes 08a12791
+ 0048d02c bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1344c50508f375a43aca3a9f722d7984"></a>

### [`0048cfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cfa8.md) → [`0048d2c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d2c8.md) FUN_0048d2c8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0048cfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cfa4.md) · 呼出先 12件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)
- 新版 呼出元 1件 [`0048d2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d2c4.md) · 呼出先 12件 [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md) [`00c59050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59050.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048d330",
      "incomplete_value": true,
      "site": "0048d334",
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
      "definition_site": "0048d010",
      "incomplete_value": true,
      "site": "0048d014",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048d32c",
      "incomplete_value": true,
      "site": "0048d338",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048d00c",
      "incomplete_value": true,
      "site": "0048d018",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0048d340",
      "incomplete_value": true,
      "site": "0048d340",
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
                "const:10:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "0048d020",
      "incomplete_value": true,
      "site": "0048d020",
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
                "const:10:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
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
      "0048d31c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0048d320",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0048d32c",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0048d31c",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "0048d320",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "0048d32c",
      "READ",
      [
        "storage",
        "00c942a8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cfa8.md#insn-0048d0b4) · [`0048cff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cfa8.md#insn-0048cff0) · [`0048cff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cfa8.md#insn-0048cff4)
- 新版 [`0048d3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d2c8.md#insn-0048d3d4) · [`0048d310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d2c8.md#insn-0048d310) · [`0048d314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d2c8.md#insn-0048d314)

~~~diff
- 0048d0b4 ["INT_ADD", "register:40f0:8", ["const:48d0b4:8", "const:4:8"]]
- 0048d0b4 ["CALL", null, ["callee:00c59320:8"]]
+ 0048d3d4 ["INT_ADD", "register:40f0:8", ["const:48d3d4:8", "const:4:8"]]
+ 0048d3d4 ["CALL", null, ["callee:00c59320:8"]]
- 0048d0b4 bytes a72c1f94
+ 0048d3d4 bytes d32f1f94
- 0048cff0 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 0048d310 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 0048cff0 bytes 794000d0
+ 0048d310 bytes 794000d0
- 0048cff4 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 0048d314 ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 0048cff4 bytes 784000d0
+ 0048d314 bytes 784000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fd99ecc3f5189f58279a998c5730db9"></a>

### [`0048d570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d570.md) → [`0048d890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d890.md) FUN_0048d890

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 6件 [`0055f0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d4.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00597658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597658.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) [`00a39150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39150.md) · 呼出先 6件 [`0055f3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f3f4.md) [`00597968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597968.md) [`00597978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597978.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

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
      "site": "0048d8dc",
      "value": [
        "leaf",
        "ram:55f3f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048d5bc",
      "value": [
        "leaf",
        "ram:55f0d4:8"
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
      "0048d8dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055f0d4"
      ]
    ]
  ],
  "added": [
    [
      "0048d8dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055f3f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d570.md#insn-0048d5bc) · [`0048d5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d570.md#insn-0048d5a4) · [`0048d5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d570.md#insn-0048d5d0)
- 新版 [`0048d8dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d890.md#insn-0048d8dc) · [`0048d8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d890.md#insn-0048d8c4) · [`0048d8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d890.md#insn-0048d8f0)

~~~diff
- 0048d5bc ["INT_ADD", "register:40f0:8", ["const:48d5bc:8", "const:4:8"]]
- 0048d5bc ["CALL", null, ["ram:55f0d4:8"]]
+ 0048d8dc ["INT_ADD", "register:40f0:8", ["const:48d8dc:8", "const:4:8"]]
+ 0048d8dc ["CALL", null, ["ram:55f3f4:8"]]
- 0048d5bc bytes c6460394
+ 0048d8dc bytes c6460394
- 0048d5a4 ["INT_ADD", "register:40f0:8", ["const:48d5a4:8", "const:4:8"]]
- 0048d5a4 ["CALL", null, ["callee:00597968:8"]]
+ 0048d8c4 ["INT_ADD", "register:40f0:8", ["const:48d8c4:8", "const:4:8"]]
+ 0048d8c4 ["CALL", null, ["callee:00597968:8"]]
- 0048d5a4 bytes 29280494
+ 0048d8c4 bytes 29280494
- 0048d5d0 ["INT_ADD", "register:40f0:8", ["const:48d5d0:8", "const:4:8"]]
- 0048d5d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0048d8f0 ["INT_ADD", "register:40f0:8", ["const:48d8f0:8", "const:4:8"]]
+ 0048d8f0 ["CALL", null, ["callee:00c54d90:8"]]
- 0048d5d0 bytes f4191f94
+ 0048d8f0 bytes 281d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d6fbcff47a3a307cd68ba4a0c52e355"></a>

### [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md) → [`0048f250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md) FUN_0048f250

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 22件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`0062ed3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062e/0062ed3c.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`00657fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md) [`006a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a9/006a97bc.md) · 呼出先 17件 [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) [`0048ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ec48.md) [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md)
- 新版 呼出元 22件 [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) [`0062f0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062f/0062f0ec.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`0065837c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/0065837c.md) [`006a9b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a9/006a9b6c.md) · 呼出先 17件 [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ec60.md) [`0048ef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ef68.md) [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md) [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048f304",
      "incomplete_value": false,
      "site": "0048f304",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048efe4",
      "incomplete_value": false,
      "site": "0048efe4",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f3d4",
      "incomplete_value": true,
      "site": "0048f3d4",
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
      "definition_site": "0048f0b4",
      "incomplete_value": true,
      "site": "0048f0b4",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f3d4",
      "incomplete_value": false,
      "site": "0048f3d4",
      "value": [
        "leaf",
        "const:48f6f8:8"
      ]
    },
    "old": {
      "definition_site": "0048f0b4",
      "incomplete_value": false,
      "site": "0048f0b4",
      "value": [
        "leaf",
        "const:48f3d8:8"
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
      "0048f2fc",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f304",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f370",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048f2fc",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f304",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f370",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md#insn-0048f0e4) · [`0048f22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md#insn-0048f22c) · [`0048f3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md#insn-0048f3d4)
- 新版 [`0048f404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md#insn-0048f404) · [`0048f54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md#insn-0048f54c) · [`0048f6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md#insn-0048f6f4)

~~~diff
- 0048f0e4 ["INT_ADD", "register:40f0:8", ["const:48f0e4:8", "const:4:8"]]
- 0048f0e4 ["CALL", null, ["callee:00550d64:8"]]
+ 0048f404 ["INT_ADD", "register:40f0:8", ["const:48f404:8", "const:4:8"]]
+ 0048f404 ["CALL", null, ["callee:00550d64:8"]]
- 0048f0e4 bytes 58060394
+ 0048f404 bytes 58060394
- 0048f22c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f22c ["INT_ADD", "register:40f0:8", ["const:48f22c:8", "const:4:8"]]
- 0048f22c ["CALLIND", null, ["register:0:8"]]
+ 0048f54c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f54c ["INT_ADD", "register:40f0:8", ["const:48f54c:8", "const:4:8"]]
+ 0048f54c ["CALLIND", null, ["register:0:8"]]
- 0048f22c bytes 00013fd6
+ 0048f54c bytes 00013fd6
- 0048f3d4 ["INT_ADD", "register:40f0:8", ["const:48f3d4:8", "const:4:8"]]
- 0048f3d4 ["CALL", null, ["callee:00c58f80:8"]]
+ 0048f6f4 ["INT_ADD", "register:40f0:8", ["const:48f6f4:8", "const:4:8"]]
+ 0048f6f4 ["CALL", null, ["callee:00c58f80:8"]]
- 0048f3d4 bytes f7221f94
+ 0048f6f4 bytes 23261f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b890c79790180fedbc45cba55ee5de0"></a>

### [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md) → [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md) FUN_0048f6f8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md) [`004901b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md) [`004906dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md) [`00491cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491cfc.md) [`00492160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md) · 呼出先 3件 [`00550a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a3c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 9件 [`0048f250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md) [`004904d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004904d4.md) [`004909fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004909fc.md) [`0049201c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/0049201c.md) [`00492480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md) · 呼出先 3件 [`00550d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d5c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048f714",
      "incomplete_value": false,
      "site": "0048f714",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f3f4",
      "incomplete_value": false,
      "site": "0048f3f4",
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
            "const:210:8"
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
      "definition_site": "0048f714",
      "incomplete_value": false,
      "site": "0048f714",
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
                "const:1d0:8"
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
      "definition_site": "0048f3f4",
      "incomplete_value": false,
      "site": "0048f3f4",
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
                "const:210:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0048f718",
      "incomplete_value": true,
      "site": "0048f718",
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
      "definition_site": "0048f3f8",
      "incomplete_value": true,
      "site": "0048f3f8",
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
      "0048f710",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f714",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f714",
      "WRITE",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0048f710",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f714",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f714",
      "WRITE",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md#insn-0048f3e4) · [`0048f3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md#insn-0048f3e8) · [`0048f3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md#insn-0048f3ec)
- 新版 [`0048f704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md#insn-0048f704) · [`0048f708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md#insn-0048f708) · [`0048f70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md#insn-0048f70c)

~~~diff
- 0048f3e4 ["INT_ADD", "register:40f0:8", ["const:48f3e4:8", "const:4:8"]]
- 0048f3e4 ["CALL", null, ["callee:00550d5c:8"]]
+ 0048f704 ["INT_ADD", "register:40f0:8", ["const:48f704:8", "const:4:8"]]
+ 0048f704 ["CALL", null, ["callee:00550d5c:8"]]
- 0048f3e4 bytes 96050394
+ 0048f704 bytes 96050394
- 0048f3e8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0048f708 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0048f3e8 bytes a84000d0
+ 0048f708 bytes a84000f0
- 0048f3ec ["COPY", "tmp:0:8", ["const:210:8"]]
- 0048f3ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048f3ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048f3ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048f70c ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0048f70c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048f70c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048f70c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048f3ec bytes 08410891
+ 0048f70c bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69505846b463f83eb9a144dc1eb03e5"></a>

### [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md) → [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md) FUN_0048f7c0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md) [`004901b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md) [`004906dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md) [`00490b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/00490b74.md) [`00491410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md) · 呼出先 17件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004463f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/004463f8.md) [`0044986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/0044986c.md) [`00449a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md) [`00550a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a48.md)
- 新版 呼出元 8件 [`0048f250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md) [`004904d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004904d4.md) [`004909fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004909fc.md) [`00490e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/00490e94.md) [`00491730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00491/00491730.md) · 呼出先 17件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00446718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446718.md) [`00449b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449b8c.md) [`00449d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md) [`00550d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d68.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048fb24",
      "incomplete_value": true,
      "site": "0048fb38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:372:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f804",
      "incomplete_value": true,
      "site": "0048f818",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a5:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0048fb28",
      "incomplete_value": true,
      "site": "0048fb3c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0048f808",
      "incomplete_value": true,
      "site": "0048f81c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048fb2c",
      "incomplete_value": true,
      "site": "0048fb40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048f80c",
      "incomplete_value": true,
      "site": "0048f820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048f8d8",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f9a4",
      "PARAM",
      [
        "storage",
        "002ae637",
        null,
        "string"
      ]
    ],
    [
      "0048f9b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004463f8"
      ]
    ]
  ],
  "added": [
    [
      "0048f8d8",
      "READ",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f9a4",
      "PARAM",
      [
        "storage",
        "002ae704",
        null,
        "string"
      ]
    ],
    [
      "0048f9b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00446718"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md#insn-0048f5dc) · [`0048f690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md#insn-0048f690) · [`0048f9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md#insn-0048f9b0)
- 新版 [`0048f8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md#insn-0048f8fc) · [`0048f9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md#insn-0048f9b0) · [`0048fcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md#insn-0048fcd0)

~~~diff
- 0048f5dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f5dc ["INT_ADD", "register:40f0:8", ["const:48f5dc:8", "const:4:8"]]
- 0048f5dc ["CALLIND", null, ["register:0:8"]]
+ 0048f8fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f8fc ["INT_ADD", "register:40f0:8", ["const:48f8fc:8", "const:4:8"]]
+ 0048f8fc ["CALLIND", null, ["register:0:8"]]
- 0048f5dc bytes 00013fd6
+ 0048f8fc bytes 00013fd6
- 0048f690 ["INT_ADD", "register:40f0:8", ["const:48f690:8", "const:4:8"]]
- 0048f690 ["CALL", null, ["ram:4463f8:8"]]
+ 0048f9b0 ["INT_ADD", "register:40f0:8", ["const:48f9b0:8", "const:4:8"]]
+ 0048f9b0 ["CALL", null, ["ram:446718:8"]]
- 0048f690 bytes 5adbfe97
+ 0048f9b0 bytes 5adbfe97
- 0048f9b0 ["INT_ADD", "register:40f0:8", ["const:48f9b0:8", "const:4:8"]]
- 0048f9b0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0048fcd0 ["INT_ADD", "register:40f0:8", ["const:48fcd0:8", "const:4:8"]]
+ 0048fcd0 ["CALL", null, ["callee:00c54d90:8"]]
- 0048f9b0 bytes fc101f94
+ 0048fcd0 bytes 30141f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d8665110fc9f4c8785213224e930a8b"></a>

### [`004901b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md) → [`004904d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004904d4.md) FUN_004904d4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 21件 [`0046cb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb44.md) [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) [`0048ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ec48.md) [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 21件 [`0046ce64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046ce64.md) [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ec60.md) [`0048ef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ef68.md) [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.59% / 新版 87.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490538",
      "incomplete_value": true,
      "site": "0049054c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2d5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490218",
      "incomplete_value": true,
      "site": "0049022c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:206:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490610",
      "incomplete_value": false,
      "site": "00490610",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004902f0",
      "incomplete_value": false,
      "site": "004902f0",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004906b8",
      "incomplete_value": true,
      "site": "004906b8",
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
      "definition_site": "00490398",
      "incomplete_value": true,
      "site": "00490398",
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
      "00490538",
      "READ",
      [
        "storage",
        "002b7206",
        null,
        "string"
      ]
    ],
    [
      "0049055c",
      "READ",
      [
        "storage",
        "002c3de8",
        null,
        "undefined8"
      ]
    ],
    [
      "00490584",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00490538",
      "READ",
      [
        "storage",
        "002b72d5",
        null,
        "string"
      ]
    ],
    [
      "0049055c",
      "READ",
      [
        "storage",
        "002c3e38",
        null,
        "undefined8"
      ]
    ],
    [
      "00490584",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00490240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md#insn-00490240) · [`0049026c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md#insn-0049026c) · [`004903cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004901b4.md#insn-004903cc)
- 新版 [`00490560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004904d4.md#insn-00490560) · [`0049058c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004904d4.md#insn-0049058c) · [`004906ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004904d4.md#insn-004906ec)

~~~diff
- 00490240 ["INT_ADD", "register:40f0:8", ["const:490240:8", "const:4:8"]]
- 00490240 ["CALL", null, ["callee:00937758:8"]]
+ 00490560 ["INT_ADD", "register:40f0:8", ["const:490560:8", "const:4:8"]]
+ 00490560 ["CALL", null, ["callee:00937758:8"]]
- 00490240 bytes 5b991294
+ 00490560 bytes 7e9c1294
- 0049026c ["INT_ADD", "register:40f0:8", ["const:49026c:8", "const:4:8"]]
- 0049026c ["CALL", null, ["ram:46cb44:8"]]
+ 0049058c ["INT_ADD", "register:40f0:8", ["const:49058c:8", "const:4:8"]]
+ 0049058c ["CALL", null, ["ram:46ce64:8"]]
- 0049026c bytes 3672ff97
+ 0049058c bytes 3672ff97
- 004903cc ["INT_ADD", "register:40f0:8", ["const:4903cc:8", "const:4:8"]]
- 004903cc ["CALL", null, ["callee:00550d64:8"]]
+ 004906ec ["INT_ADD", "register:40f0:8", ["const:4906ec:8", "const:4:8"]]
+ 004906ec ["CALL", null, ["callee:00550d64:8"]]
- 004903cc bytes 9e010394
+ 004906ec bytes 9e010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-039173647e8c24ec996ba1a2d6ebe4c4"></a>

### [`004906dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md) → [`004909fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004909fc.md) FUN_004909fc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009808bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00980/009808bc.md) · 呼出先 17件 [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) [`0048ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ec48.md) [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md)
- 新版 呼出元 1件 [`00981868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00981/00981868.md) · 呼出先 17件 [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ec60.md) [`0048ef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ef68.md) [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md) [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490ae0",
      "incomplete_value": false,
      "site": "00490ae0",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004907c0",
      "incomplete_value": false,
      "site": "004907c0",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490b74",
      "incomplete_value": true,
      "site": "00490b74",
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
      "definition_site": "00490854",
      "incomplete_value": true,
      "site": "00490854",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00490b74",
      "incomplete_value": false,
      "site": "00490b74",
      "value": [
        "leaf",
        "const:48f6f8:8"
      ]
    },
    "old": {
      "definition_site": "00490854",
      "incomplete_value": false,
      "site": "00490854",
      "value": [
        "leaf",
        "const:48f3d8:8"
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
      "00490a6c",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00490a74",
      "READ",
      [
        "storage",
        "00ca4d94",
        null,
        "undefined4"
      ]
    ],
    [
      "00490ad8",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00490a6c",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      "00490a74",
      "READ",
      [
        "storage",
        "00ca5d54",
        null,
        "undefined4"
      ]
    ],
    [
      "00490ad8",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004907a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md#insn-004907a8) · [`004909c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md#insn-004909c8) · [`00490720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/004906dc.md#insn-00490720)
- 新版 [`00490ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004909fc.md#insn-00490ac8) · [`00490ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004909fc.md#insn-00490ce8) · [`00490a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/004909fc.md#insn-00490a40)

~~~diff
- 004907a8 ["INT_ADD", "register:40f0:8", ["const:4907a8:8", "const:4:8"]]
- 004907a8 ["CALL", null, ["callee:00550d6c:8"]]
+ 00490ac8 ["INT_ADD", "register:40f0:8", ["const:490ac8:8", "const:4:8"]]
+ 00490ac8 ["CALL", null, ["callee:00550d6c:8"]]
- 004907a8 bytes a9000394
+ 00490ac8 bytes a9000394
- 004909c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004909c8 ["INT_ADD", "register:40f0:8", ["const:4909c8:8", "const:4:8"]]
- 004909c8 ["CALLIND", null, ["register:0:8"]]
+ 00490ce8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00490ce8 ["INT_ADD", "register:40f0:8", ["const:490ce8:8", "const:4:8"]]
+ 00490ce8 ["CALLIND", null, ["register:0:8"]]
- 004909c8 bytes 00013fd6
+ 00490ce8 bytes 00013fd6
- 00490720 ["INT_ADD", "register:40f0:8", ["const:490720:8", "const:4:8"]]
- 00490720 ["CALL", null, ["callee:00550d60:8"]]
+ 00490a40 ["INT_ADD", "register:40f0:8", ["const:490a40:8", "const:4:8"]]
+ 00490a40 ["CALL", null, ["callee:00550d60:8"]]
- 00490720 bytes c8000394
+ 00490a40 bytes c8000394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aae223d028a277155fe4a3d10d2c3a2d"></a>

### [`00490b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/00490b74.md) → [`00490e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/00490e94.md) FUN_00490e94

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0088c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md) · 呼出先 21件 [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) [`0046cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb9c.md) [`0048dd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e530.md)
- 新版 呼出元 3件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`0088d4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d4b0.md) · 呼出先 21件 [`0046ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046ce6c.md) [`0046cebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cebc.md) [`0048e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e0a0.md) [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048e850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e850.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.87% / 新版 88.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490f1c",
      "incomplete_value": false,
      "site": "00490f1c",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490bfc",
      "incomplete_value": false,
      "site": "00490bfc",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00491260",
      "incomplete_value": false,
      "site": "00491260",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490f40",
      "incomplete_value": false,
      "site": "00490f40",
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
            "const:c28:8"
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
      "definition_site": "00491320",
      "incomplete_value": true,
      "site": "00491334",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491000",
      "incomplete_value": true,
      "site": "00491014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20f:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00490f14",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "00490f1c",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00490fc0",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00490f14",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00490f1c",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00490fc0",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00490c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/00490b74.md#insn-00490c20) · [`00490d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/00490b74.md#insn-00490d00) · [`00491220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/00490b74.md#insn-00491220)
- 新版 [`00490f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/00490e94.md#insn-00490f40) · [`00491020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/00490e94.md#insn-00491020) · [`00491540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00490/00490e94.md#insn-00491540)

~~~diff
- 00490c20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00490c20 ["INT_ADD", "register:40f0:8", ["const:490c20:8", "const:4:8"]]
- 00490c20 ["CALLIND", null, ["register:0:8"]]
+ 00490f40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00490f40 ["INT_ADD", "register:40f0:8", ["const:490f40:8", "const:4:8"]]
+ 00490f40 ["CALLIND", null, ["register:0:8"]]
- 00490c20 bytes 00013fd6
+ 00490f40 bytes 00013fd6
- 00490d00 ["COPY", "tmp:0:8", ["const:221:8"]]
- 00490d00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00490d00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00490d00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00491020 ["COPY", "tmp:0:8", ["const:1e1:8"]]
+ 00491020 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00491020 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00491020 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00490d00 bytes 4a850891
+ 00491020 bytes 4a850791
- 00491220 ["COPY", "register:0:8", ["register:4040:8"]]
- 00491220 ["INT_ADD", "register:40f0:8", ["const:491220:8", "const:4:8"]]
- 00491220 ["CALLIND", null, ["register:0:8"]]
+ 00491540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00491540 ["INT_ADD", "register:40f0:8", ["const:491540:8", "const:4:8"]]
+ 00491540 ["CALLIND", null, ["register:0:8"]]
- 00491220 bytes 00013fd6
+ 00491540 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6698dda1ed511b3c3f55d813f1fbf0ed"></a>

### [`00491410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md) → [`00491730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00491/00491730.md) FUN_00491730

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0083f4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f4c0.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0086f974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f974.md) · 呼出先 20件 [`0048dd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e530.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md) [`00493ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493ff0.md)
- 新版 呼出元 3件 [`0084046c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/0084046c.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`00870920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00870/00870920.md) · 呼出先 20件 [`0048e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e0a0.md) [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048e850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e850.md) [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md) [`00494310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494310.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.45% / 新版 87.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004917e4",
      "incomplete_value": false,
      "site": "004917e4",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004914c4",
      "incomplete_value": false,
      "site": "004914c4",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00491b5c",
      "incomplete_value": false,
      "site": "00491b5c",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049183c",
      "incomplete_value": false,
      "site": "0049183c",
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
            "const:d28:8"
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
      "definition_site": "00491c08",
      "incomplete_value": true,
      "site": "00491c24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004918e8",
      "incomplete_value": true,
      "site": "00491904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20f:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004917dc",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "004917e4",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00491870",
      "READ",
      [
        "storage",
        "002c4400",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004917dc",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "004917e4",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00491870",
      "READ",
      [
        "storage",
        "002c4450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049151c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md#insn-0049151c) · [`004917b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md#insn-004917b0) · [`00491834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md#insn-00491834)
- 新版 [`0049183c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00491/00491730.md#insn-0049183c) · [`00491ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00491/00491730.md#insn-00491ad0) · [`00491b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00491/00491730.md#insn-00491b54)

~~~diff
- 0049151c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049151c ["INT_ADD", "register:40f0:8", ["const:49151c:8", "const:4:8"]]
- 0049151c ["CALLIND", null, ["register:0:8"]]
+ 0049183c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049183c ["INT_ADD", "register:40f0:8", ["const:49183c:8", "const:4:8"]]
+ 0049183c ["CALLIND", null, ["register:0:8"]]
- 0049151c bytes 00013fd6
+ 0049183c bytes 00013fd6
- 004917b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c38:8"]]
- 004917b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00491ad0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c08:8"]]
+ 00491ad0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004917b0 bytes 291d46f9
+ 00491ad0 bytes 290546f9
- 00491834 ["COPY", "register:4048:8", ["const:c65000:8"]]
+ 00491b54 ["COPY", "register:4048:8", ["const:c66000:8"]]
- 00491834 bytes a93e0090
+ 00491b54 bytes a93e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02a69b4e7bd31a07cb62d2b05f96ff2c"></a>

### [`00491cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491cfc.md) → [`0049201c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/0049201c.md) FUN_0049201c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0062b754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062b/0062b754.md) · 呼出先 17件 [`0046cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb9c.md) [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) [`0048ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ec48.md) [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md)
- 新版 呼出元 1件 [`0062bb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062b/0062bb04.md) · 呼出先 17件 [`0046cebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cebc.md) [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ec60.md) [`0048ef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ef68.md) [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004920a0",
      "incomplete_value": false,
      "site": "004920a0",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491d80",
      "incomplete_value": false,
      "site": "00491d80",
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
            "const:210:8"
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
      "definition_site": "00492164",
      "incomplete_value": true,
      "site": "00492164",
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
      "definition_site": "00491e44",
      "incomplete_value": true,
      "site": "00491e44",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00492164",
      "incomplete_value": false,
      "site": "00492164",
      "value": [
        "leaf",
        "const:48f6f8:8"
      ]
    },
    "old": {
      "definition_site": "00491e44",
      "incomplete_value": false,
      "site": "00491e44",
      "value": [
        "leaf",
        "const:48f3d8:8"
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
      "00492098",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "004920a0",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "0049210c",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00492098",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "004920a0",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0049210c",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00491e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491cfc.md#insn-00491e18) · [`00491f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491cfc.md#insn-00491f98) · [`00491d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491cfc.md#insn-00491d3c)
- 新版 [`00492138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/0049201c.md#insn-00492138) · [`004922b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/0049201c.md#insn-004922b8) · [`0049205c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/0049201c.md#insn-0049205c)

~~~diff
- 00491e18 ["INT_ADD", "register:40f0:8", ["const:491e18:8", "const:4:8"]]
- 00491e18 ["CALL", null, ["callee:0046cebc:8"]]
+ 00492138 ["INT_ADD", "register:40f0:8", ["const:492138:8", "const:4:8"]]
+ 00492138 ["CALL", null, ["callee:0046cebc:8"]]
- 00491e18 bytes 616bff97
+ 00492138 bytes 616bff97
- 00491f98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00491f98 ["INT_ADD", "register:40f0:8", ["const:491f98:8", "const:4:8"]]
- 00491f98 ["CALLIND", null, ["register:0:8"]]
+ 004922b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004922b8 ["INT_ADD", "register:40f0:8", ["const:4922b8:8", "const:4:8"]]
+ 004922b8 ["CALLIND", null, ["register:0:8"]]
- 00491f98 bytes 00013fd6
+ 004922b8 bytes 00013fd6
- 00491d3c ["INT_ADD", "register:40f0:8", ["const:491d3c:8", "const:4:8"]]
- 00491d3c ["CALL", null, ["callee:00550d60:8"]]
+ 0049205c ["INT_ADD", "register:40f0:8", ["const:49205c:8", "const:4:8"]]
+ 0049205c ["CALL", null, ["callee:00550d60:8"]]
- 00491d3c bytes 41fb0294
+ 0049205c bytes 41fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5986c34871d79c002fe0c3ba8876c23e"></a>

### [`00492160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md) → [`00492480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md) FUN_00492480

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`006da6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da6c8.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) [`008d9c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c58.md) · 呼出先 17件 [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) [`0048ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ec48.md) [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md)
- 新版 呼出元 6件 [`006daa78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa78.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`0089c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c290.md) [`008dac04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008dac04.md) · 呼出先 17件 [`0046ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046ce6c.md) [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048ec60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ec60.md) [`0048ef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048ef68.md) [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.22% / 新版 86.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004924f8",
      "incomplete_value": false,
      "site": "004924f8",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004921d8",
      "incomplete_value": false,
      "site": "004921d8",
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
            "const:210:8"
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
      "definition_site": "004925b0",
      "incomplete_value": true,
      "site": "004925b0",
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
      "definition_site": "00492290",
      "incomplete_value": true,
      "site": "00492290",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004925b0",
      "incomplete_value": false,
      "site": "004925b0",
      "value": [
        "leaf",
        "const:48f6f8:8"
      ]
    },
    "old": {
      "definition_site": "00492290",
      "incomplete_value": false,
      "site": "00492290",
      "value": [
        "leaf",
        "const:48f3d8:8"
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
      "004924f0",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "004924f8",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00492564",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004924f0",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "004924f8",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00492564",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md#insn-00492264) · [`004923e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md#insn-004923e8) · [`00492194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md#insn-00492194)
- 新版 [`00492584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md#insn-00492584) · [`00492708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md#insn-00492708) · [`004924b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md#insn-004924b4)

~~~diff
- 00492264 ["INT_ADD", "register:40f0:8", ["const:492264:8", "const:4:8"]]
- 00492264 ["CALL", null, ["callee:0046ce6c:8"]]
+ 00492584 ["INT_ADD", "register:40f0:8", ["const:492584:8", "const:4:8"]]
+ 00492584 ["CALL", null, ["callee:0046ce6c:8"]]
- 00492264 bytes 3a6aff97
+ 00492584 bytes 3a6aff97
- 004923e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004923e8 ["INT_ADD", "register:40f0:8", ["const:4923e8:8", "const:4:8"]]
- 004923e8 ["CALLIND", null, ["register:0:8"]]
+ 00492708 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492708 ["INT_ADD", "register:40f0:8", ["const:492708:8", "const:4:8"]]
+ 00492708 ["CALLIND", null, ["register:0:8"]]
- 004923e8 bytes 00013fd6
+ 00492708 bytes 00013fd6
- 00492194 ["INT_ADD", "register:40f0:8", ["const:492194:8", "const:4:8"]]
- 00492194 ["CALL", null, ["callee:00550d60:8"]]
+ 004924b4 ["INT_ADD", "register:40f0:8", ["const:4924b4:8", "const:4:8"]]
+ 004924b4 ["CALL", null, ["callee:00550d60:8"]]
- 00492194 bytes 2bfa0294
+ 004924b4 bytes 2bfa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11d0262ae1d1b7ca7e526de0d1f0babe"></a>

### [`004925ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004925ac.md) → [`004928cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/004928cc.md) FUN_004928cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md) · 呼出先 1件 [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md)
- 新版 呼出元 1件 [`00b2ded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2ded8.md) · 呼出先 1件 [`0046ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046ce6c.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004928ec",
      "incomplete_value": true,
      "site": "004928ec",
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
      "definition_site": "004925cc",
      "incomplete_value": true,
      "site": "004925cc",
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
      "definition_site": "004929ac",
      "incomplete_value": false,
      "site": "004929b0",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049268c",
      "incomplete_value": false,
      "site": "00492690",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004929e8",
      "incomplete_value": false,
      "site": "004929ec",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004926c8",
      "incomplete_value": false,
      "site": "004926cc",
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
      "004928e8",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "004928f8",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00492900",
      "READ",
      [
        "storage",
        "00ca4d9c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "004928e8",
      "READ",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "004928f8",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      "00492900",
      "READ",
      [
        "storage",
        "00ca5d5c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004925ac.md#insn-00492690) · [`004926cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004925ac.md#insn-004926cc) · [`00492764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004925ac.md#insn-00492764)
- 新版 [`004929b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/004928cc.md#insn-004929b0) · [`004929ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/004928cc.md#insn-004929ec) · [`00492a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/004928cc.md#insn-00492a84)

~~~diff
- 00492690 ["INT_ADD", "register:40f0:8", ["const:492690:8", "const:4:8"]]
- 00492690 ["CALL", null, ["callee:0046ce6c:8"]]
+ 004929b0 ["INT_ADD", "register:40f0:8", ["const:4929b0:8", "const:4:8"]]
+ 004929b0 ["CALL", null, ["callee:0046ce6c:8"]]
- 00492690 bytes 2f69ff97
+ 004929b0 bytes 2f69ff97
- 004926cc ["INT_ADD", "register:40f0:8", ["const:4926cc:8", "const:4:8"]]
- 004926cc ["CALL", null, ["callee:0046ce6c:8"]]
+ 004929ec ["INT_ADD", "register:40f0:8", ["const:4929ec:8", "const:4:8"]]
+ 004929ec ["CALL", null, ["callee:0046ce6c:8"]]
- 004926cc bytes 2069ff97
+ 004929ec bytes 2069ff97
- 00492764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00492764 ["INT_ADD", "register:40f0:8", ["const:492764:8", "const:4:8"]]
- 00492764 ["CALLIND", null, ["register:0:8"]]
+ 00492a84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492a84 ["INT_ADD", "register:40f0:8", ["const:492a84:8", "const:4:8"]]
+ 00492a84 ["CALLIND", null, ["register:0:8"]]
- 00492764 bytes 00013fd6
+ 00492a84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eeb96939e1d7df63d2c8ca09ec80335"></a>

### [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) → [`00492c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md) FUN_00492c0c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 29件 [`007aed90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed90.md) [`00865168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) [`00872078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872078.md) [`008722a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008722a8.md) [`0087f164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md) · 呼出先 9件 [`0048dd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e530.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md) [`00493ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493ff0.md)
- 新版 呼出元 29件 [`007af574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af574.md) [`00866114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866114.md) [`00873024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873024.md) [`00873254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873254.md) [`00880110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/00880110.md) · 呼出先 9件 [`0048e0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e0a0.md) [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md) [`0048e850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e850.md) [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md) [`00494310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494310.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.64% / 新版 82.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492cc8",
      "incomplete_value": true,
      "site": "00492cc8",
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
      "definition_site": "004929a8",
      "incomplete_value": true,
      "site": "004929a8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00492cc8",
      "incomplete_value": false,
      "site": "00492cc8",
      "value": [
        "leaf",
        "const:48e850:8"
      ]
    },
    "old": {
      "definition_site": "004929a8",
      "incomplete_value": false,
      "site": "004929a8",
      "value": [
        "leaf",
        "const:48e530:8"
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492ce0",
      "incomplete_value": true,
      "site": "00492ce0",
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
      "definition_site": "004929c0",
      "incomplete_value": true,
      "site": "004929c0",
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
      "00492cac",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ],
    [
      "00492cb0",
      "READ",
      [
        "storage",
        "00c9ada0",
        null,
        "pointer"
      ]
    ],
    [
      "00492cc8",
      "DATA",
      [
        "storage",
        "00c65ac8",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "00492cac",
      "READ",
      [
        "storage",
        "00c9bd68",
        null,
        "pointer"
      ]
    ],
    [
      "00492cb0",
      "READ",
      [
        "storage",
        "00c9bd70",
        null,
        "pointer"
      ]
    ],
    [
      "00492cc8",
      "DATA",
      [
        "storage",
        "00c66a98",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004929dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md#insn-004929dc) · [`00492940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md#insn-00492940) · [`00492978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md#insn-00492978)
- 新版 [`00492cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md#insn-00492cfc) · [`00492c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md#insn-00492c60) · [`00492c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492c0c.md#insn-00492c98)

~~~diff
- 004929dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004929dc ["INT_ADD", "register:40f0:8", ["const:4929dc:8", "const:4:8"]]
- 004929dc ["CALLIND", null, ["register:0:8"]]
+ 00492cfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492cfc ["INT_ADD", "register:40f0:8", ["const:492cfc:8", "const:4:8"]]
+ 00492cfc ["CALLIND", null, ["register:0:8"]]
- 004929dc bytes 00013fd6
+ 00492cfc bytes 00013fd6
- 00492940 ["INT_ADD", "register:40f0:8", ["const:492940:8", "const:4:8"]]
- 00492940 ["CALL", null, ["callee:0048e418:8"]]
+ 00492c60 ["INT_ADD", "register:40f0:8", ["const:492c60:8", "const:4:8"]]
+ 00492c60 ["CALL", null, ["callee:0048e418:8"]]
- 00492940 bytes eeedff97
+ 00492c60 bytes eeedff97
- 00492978 ["INT_ADD", "register:40f0:8", ["const:492978:8", "const:4:8"]]
- 00492978 ["CALL", null, ["callee:0048e418:8"]]
+ 00492c98 ["INT_ADD", "register:40f0:8", ["const:492c98:8", "const:4:8"]]
+ 00492c98 ["CALL", null, ["callee:0048e418:8"]]
- 00492978 bytes e0edff97
+ 00492c98 bytes e0edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aaf8b47dafe63d5f11a1fa8aa5d7046"></a>

### [`00492b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492b60.md) → [`00492e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492e80.md) FUN_00492e80

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00893bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893bdc.md) · 呼出先 3件 [`00550a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a3c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00894b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894b88.md) · 呼出先 3件 [`00550d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d5c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.93% / 新版 83.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492ed0",
      "incomplete_value": false,
      "site": "00492ed0",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492bb0",
      "incomplete_value": false,
      "site": "00492bb0",
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
            "const:210:8"
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
      "definition_site": "00492ed0",
      "incomplete_value": false,
      "site": "00492ed0",
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
                "const:1d0:8"
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
      "definition_site": "00492bb0",
      "incomplete_value": false,
      "site": "00492bb0",
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
                "const:210:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00492e98",
      "incomplete_value": true,
      "site": "00492e98",
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
      "definition_site": "00492b78",
      "incomplete_value": true,
      "site": "00492b78",
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
      "00492e94",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00492eb0",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00492ecc",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00492e94",
      "READ",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00492eb0",
      "READ",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00492ecc",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492b60.md#insn-00492b6c) · [`00492b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492b60.md#insn-00492b74) · [`00492b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492b60.md#insn-00492b88)
- 新版 [`00492e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492e80.md#insn-00492e8c) · [`00492e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492e80.md#insn-00492e94) · [`00492ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492e80.md#insn-00492ea8)

~~~diff
- 00492b6c ["COPY", "register:40a0:8", ["const:ca5000:8"]]
+ 00492e8c ["COPY", "register:40a0:8", ["const:ca6000:8"]]
- 00492b6c bytes 944000f0
+ 00492e8c bytes b4400090
- 00492b74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:210:8"]]
- 00492b74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492e94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1d0:8"]]
+ 00492e94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00492b74 bytes 880a41f9
+ 00492e94 bytes 88ea40f9
- 00492b88 ["COPY", "register:0:8", ["register:4048:8"]]
- 00492b88 ["INT_ADD", "register:40f0:8", ["const:492b88:8", "const:4:8"]]
- 00492b88 ["CALLIND", null, ["register:0:8"]]
+ 00492ea8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00492ea8 ["INT_ADD", "register:40f0:8", ["const:492ea8:8", "const:4:8"]]
+ 00492ea8 ["CALLIND", null, ["register:0:8"]]
- 00492b88 bytes 20013fd6
+ 00492ea8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b840b77000487c225d8740ae2cb77f3"></a>

### [`00492c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md) → [`00492f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492f60.md) FUN_00492f60

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`008801e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/008801e4.md) [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 3件 [`00550a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a3c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 11件 [`007ac83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007ac83c.md) [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) [`00881190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881190.md) [`0088275c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088275c.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 3件 [`00550d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d5c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492f80",
      "incomplete_value": false,
      "site": "00492f80",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492c60",
      "incomplete_value": false,
      "site": "00492c60",
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
            "const:210:8"
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
      "definition_site": "00492f80",
      "incomplete_value": false,
      "site": "00492f80",
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
                "const:1d0:8"
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
      "definition_site": "00492c60",
      "incomplete_value": false,
      "site": "00492c60",
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
                "const:210:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00492f84",
      "incomplete_value": true,
      "site": "00492f84",
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
      "definition_site": "00492c64",
      "incomplete_value": true,
      "site": "00492c64",
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
      "00492f7c",
      "READ",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ],
    [
      "00492f80",
      "WRITE",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00492f80",
      "WRITE",
      [
        "storage",
        "00ca5218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00492f7c",
      "READ",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00492f80",
      "WRITE",
      [
        "storage",
        "00ca61d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00492f80",
      "WRITE",
      [
        "storage",
        "00ca61d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md#insn-00492c50) · [`00492c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md#insn-00492c54) · [`00492c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md#insn-00492c58)
- 新版 [`00492f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492f60.md#insn-00492f70) · [`00492f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492f60.md#insn-00492f74) · [`00492f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492f60.md#insn-00492f78)

~~~diff
- 00492c50 ["INT_ADD", "register:40f0:8", ["const:492c50:8", "const:4:8"]]
- 00492c50 ["CALL", null, ["callee:00550d5c:8"]]
+ 00492f70 ["INT_ADD", "register:40f0:8", ["const:492f70:8", "const:4:8"]]
+ 00492f70 ["CALL", null, ["callee:00550d5c:8"]]
- 00492c50 bytes 7bf70294
+ 00492f70 bytes 7bf70294
- 00492c54 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 00492f74 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 00492c54 bytes 884000f0
+ 00492f74 bytes a8400090
- 00492c58 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00492c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00492c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00492c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00492f78 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 00492f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00492f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00492f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00492c58 bytes 08410891
+ 00492f78 bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9583af89120867241d65692a3fd8b4d6"></a>

### [`00493048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493048.md) → [`00493368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493368.md) FUN_00493368

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00493314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493314.md) [`004944c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944c4.md) [`004944c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944c8.md) [`00550a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a50.md)
- 新版 呼出元 5件 [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`00877f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md) · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00493634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493634.md) [`004947e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004947e4.md) [`004947e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004947e8.md) [`00550d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004933b8",
      "incomplete_value": false,
      "site": "004933b8",
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
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00493098",
      "incomplete_value": false,
      "site": "00493098",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004933d4",
      "incomplete_value": false,
      "site": "004933d4",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004930b4",
      "incomplete_value": false,
      "site": "004930b4",
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
            "const:e28:8"
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
      "definition_site": "004934a0",
      "incomplete_value": true,
      "site": "004934a0",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00493180",
      "incomplete_value": true,
      "site": "00493180",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004933a4",
      "READ",
      [
        "storage",
        "00ca52a0",
        null,
        "undefined1"
      ]
    ],
    [
      "004933b0",
      "READ",
      [
        "storage",
        "00ca5280",
        null,
        "undefined4"
      ]
    ],
    [
      "004933b8",
      "WRITE",
      [
        "storage",
        "00ca5280",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "004933a4",
      "READ",
      [
        "storage",
        "00ca6260",
        null,
        "undefined1"
      ]
    ],
    [
      "004933b0",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined4"
      ]
    ],
    [
      "004933b8",
      "WRITE",
      [
        "storage",
        "00ca6240",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00493098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493048.md#insn-00493098) · [`00493180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493048.md#insn-00493180) · [`0049324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493048.md#insn-0049324c)
- 新版 [`004933b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493368.md#insn-004933b8) · [`004934a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493368.md#insn-004934a0) · [`0049356c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493368.md#insn-0049356c)

~~~diff
- 00493098 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 00493098 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
+ 004933b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
+ 004933b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
- 00493098 bytes 158102b9
+ 004933b8 bytes 154102b9
- 00493180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
- 00493180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 004934a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:248:8"]]
+ 004934a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00493180 bytes 094501f9
+ 004934a0 bytes 092501f9
- 0049324c ["INT_ADD", "register:40f0:8", ["const:49324c:8", "const:4:8"]]
- 0049324c ["CALL", null, ["callee:00c58ef0:8"]]
+ 0049356c ["INT_ADD", "register:40f0:8", ["const:49356c:8", "const:4:8"]]
+ 0049356c ["CALL", null, ["callee:00c58ef0:8"]]
- 0049324c bytes 35131f94
+ 0049356c bytes 61161f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5b550a8a9257cb48e00b63c915334e9"></a>

### [`0049331c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md) → [`0049363c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049363c.md) FUN_0049363c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`0086f974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f974.md) [`008831b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/008831b0.md) [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00493314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493314.md) [`00494bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494bbc.md) [`00550a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 4件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`00870920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00870/00870920.md) [`0088415c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088415c.md) [`00915e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00915/00915e30.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00493634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493634.md) [`00494edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494edc.md) [`00550d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d70.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 89.45% / 新版 89.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00493694",
      "incomplete_value": false,
      "site": "00493694",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00493374",
      "incomplete_value": false,
      "site": "00493374",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004936fc",
      "incomplete_value": false,
      "site": "004936fc",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004933dc",
      "incomplete_value": false,
      "site": "004933dc",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0049384c",
      "incomplete_value": true,
      "site": "0049384c",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049352c",
      "incomplete_value": true,
      "site": "0049352c",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049367c",
      "READ",
      [
        "storage",
        "00ca52c8",
        null,
        "undefined1"
      ]
    ],
    [
      "0049368c",
      "READ",
      [
        "storage",
        "00ca52a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00493694",
      "WRITE",
      [
        "storage",
        "00ca52a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0049367c",
      "READ",
      [
        "storage",
        "00ca6288",
        null,
        "undefined1"
      ]
    ],
    [
      "0049368c",
      "READ",
      [
        "storage",
        "00ca6268",
        null,
        "undefined4"
      ]
    ],
    [
      "00493694",
      "WRITE",
      [
        "storage",
        "00ca6268",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00493374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md#insn-00493374) · [`0049352c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md#insn-0049352c) · [`004935e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/0049331c.md#insn-004935e8)
- 新版 [`00493694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049363c.md#insn-00493694) · [`0049384c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049363c.md#insn-0049384c) · [`00493908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049363c.md#insn-00493908)

~~~diff
- 00493374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
- 00493374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
+ 00493694 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
+ 00493694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
- 00493374 bytes 18a902b9
+ 00493694 bytes 186902b9
- 0049352c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 0049352c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0049384c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 0049384c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0049352c bytes 095901f9
+ 0049384c bytes 093901f9
- 004935e8 ["INT_ADD", "register:40f0:8", ["const:4935e8:8", "const:4:8"]]
- 004935e8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00493908 ["INT_ADD", "register:40f0:8", ["const:493908:8", "const:4:8"]]
+ 00493908 ["CALL", null, ["callee:00c58ef0:8"]]
- 004935e8 bytes 4e121f94
+ 00493908 bytes 7a151f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b61bc0e955ec45114711fe5cf0502d"></a>

### [`004940cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004940cc.md) → [`004943ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004943ec.md) FUN_004943ec

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0049440c",
      "incomplete_value": false,
      "site": "00494410",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004940ec",
      "incomplete_value": false,
      "site": "004940f0",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00494410",
      "DATA",
      [
        "storage",
        "00c65c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494410",
      "DATA",
      [
        "storage",
        "00c66bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004940e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004940cc.md#insn-004940e0) · [`004940e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004940cc.md#insn-004940e8) · [`004940ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004940cc.md#insn-004940ec)
- 新版 [`00494400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004943ec.md#insn-00494400) · [`00494408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004943ec.md#insn-00494408) · [`0049440c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004943ec.md#insn-0049440c)

~~~diff
- 004940e0 ["INT_ADD", "register:40f0:8", ["const:4940e0:8", "const:4:8"]]
- 004940e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00494400 ["INT_ADD", "register:40f0:8", ["const:494400:8", "const:4:8"]]
+ 00494400 ["CALL", null, ["callee:00c58f30:8"]]
- 004940e0 bytes a00f1f94
+ 00494400 bytes cc121f94
- 004940e8 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494408 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004940e8 bytes 883e00b0
+ 00494408 bytes 883e00d0
- 004940ec ["COPY", "tmp:0:8", ["const:c28:8"]]
- 004940ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004940ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004940ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049440c ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 0049440c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049440c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049440c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004940ec bytes 08a13091
+ 0049440c bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad3bb9c70f722e9fe8059b128bbfa4f3"></a>

### [`00494104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494104.md) → [`00494424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494424.md) FUN_00494424

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494428",
      "incomplete_value": false,
      "site": "0049442c",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494108",
      "incomplete_value": false,
      "site": "0049410c",
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
      "0049442c",
      "DATA",
      [
        "storage",
        "00c65c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049442c",
      "DATA",
      [
        "storage",
        "00c66bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494104.md#insn-00494104) · [`00494108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494104.md#insn-00494108)
- 新版 [`00494424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494424.md#insn-00494424) · [`00494428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494424.md#insn-00494428)

~~~diff
- 00494104 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494424 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494104 bytes 883e00b0
+ 00494424 bytes 883e00d0
- 00494108 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00494108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494428 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00494428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494108 bytes 08a13091
+ 00494428 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5585f6276c576dea20978271eb53eedd"></a>

### [`0049416c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049416c.md) → [`0049448c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049448c.md) FUN_0049448c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004944ac",
      "incomplete_value": false,
      "site": "004944b0",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049418c",
      "incomplete_value": false,
      "site": "00494190",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004944b0",
      "DATA",
      [
        "storage",
        "00c65ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004944b0",
      "DATA",
      [
        "storage",
        "00c66c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049416c.md#insn-00494180) · [`00494188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049416c.md#insn-00494188) · [`0049418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049416c.md#insn-0049418c)
- 新版 [`004944a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049448c.md#insn-004944a0) · [`004944a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049448c.md#insn-004944a8) · [`004944ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049448c.md#insn-004944ac)

~~~diff
- 00494180 ["INT_ADD", "register:40f0:8", ["const:494180:8", "const:4:8"]]
- 00494180 ["CALL", null, ["callee:00c58f30:8"]]
+ 004944a0 ["INT_ADD", "register:40f0:8", ["const:4944a0:8", "const:4:8"]]
+ 004944a0 ["CALL", null, ["callee:00c58f30:8"]]
- 00494180 bytes 780f1f94
+ 004944a0 bytes a4121f94
- 00494188 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 004944a8 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494188 bytes 883e00b0
+ 004944a8 bytes 883e00d0
- 0049418c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 0049418c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049418c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049418c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004944ac ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 004944ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004944ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004944ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049418c bytes 08a13291
+ 004944ac bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ddc46c2f10578ef2d4d722e413906fb"></a>

### [`004941a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004941a4.md) → [`004944c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004944c4.md) FUN_004944c4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004944c8",
      "incomplete_value": false,
      "site": "004944cc",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004941a8",
      "incomplete_value": false,
      "site": "004941ac",
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
      "004944cc",
      "DATA",
      [
        "storage",
        "00c65ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004944cc",
      "DATA",
      [
        "storage",
        "00c66c78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004941a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004941a4.md#insn-004941a4) · [`004941a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004941a4.md#insn-004941a8)
- 新版 [`004944c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004944c4.md#insn-004944c4) · [`004944c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004944c4.md#insn-004944c8)

~~~diff
- 004941a4 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 004944c4 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004941a4 bytes 883e00b0
+ 004944c4 bytes 883e00d0
- 004941a8 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 004941a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004941a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004941a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004944c8 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 004944c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004944c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004944c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004941a8 bytes 08a13291
+ 004944c8 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd2e7b7d67bd26520d7b2bb871417544"></a>

### [`0049420c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049420c.md) → [`0049452c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049452c.md) FUN_0049452c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0049454c",
      "incomplete_value": false,
      "site": "00494550",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049422c",
      "incomplete_value": false,
      "site": "00494230",
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
            "const:d28:8"
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
      "00494550",
      "DATA",
      [
        "storage",
        "00c65d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494550",
      "DATA",
      [
        "storage",
        "00c66cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049420c.md#insn-00494220) · [`00494228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049420c.md#insn-00494228) · [`0049422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/0049420c.md#insn-0049422c)
- 新版 [`00494540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049452c.md#insn-00494540) · [`00494548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049452c.md#insn-00494548) · [`0049454c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/0049452c.md#insn-0049454c)

~~~diff
- 00494220 ["INT_ADD", "register:40f0:8", ["const:494220:8", "const:4:8"]]
- 00494220 ["CALL", null, ["callee:00c58f30:8"]]
+ 00494540 ["INT_ADD", "register:40f0:8", ["const:494540:8", "const:4:8"]]
+ 00494540 ["CALL", null, ["callee:00c58f30:8"]]
- 00494220 bytes 500f1f94
+ 00494540 bytes 7c121f94
- 00494228 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494548 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494228 bytes 883e00b0
+ 00494548 bytes 883e00d0
- 0049422c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0049422c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049422c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049422c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049454c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 0049454c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049454c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049454c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049422c bytes 08a13491
+ 0049454c bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddda5f313578e307a6623706d3a0faf0"></a>

### [`00494244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494244.md) → [`00494564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494564.md) FUN_00494564

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494568",
      "incomplete_value": false,
      "site": "0049456c",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494248",
      "incomplete_value": false,
      "site": "0049424c",
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
            "const:d28:8"
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
      "0049456c",
      "DATA",
      [
        "storage",
        "00c65d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049456c",
      "DATA",
      [
        "storage",
        "00c66cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494244.md#insn-00494244) · [`00494248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494244.md#insn-00494248)
- 新版 [`00494564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494564.md#insn-00494564) · [`00494568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494564.md#insn-00494568)

~~~diff
- 00494244 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494564 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494244 bytes 883e00b0
+ 00494564 bytes 883e00d0
- 00494248 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00494248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494568 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00494568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494248 bytes 08a13491
+ 00494568 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43c85295ef166c2ae57967ee77f8082"></a>

### [`004942ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942ac.md) → [`004945cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004945cc.md) FUN_004945cc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004945ec",
      "incomplete_value": false,
      "site": "004945f0",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004942cc",
      "incomplete_value": false,
      "site": "004942d0",
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
            "const:da8:8"
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
      "004945f0",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004945f0",
      "DATA",
      [
        "storage",
        "00c66d78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004942c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942ac.md#insn-004942c0) · [`004942c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942ac.md#insn-004942c8) · [`004942cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942ac.md#insn-004942cc)
- 新版 [`004945e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004945cc.md#insn-004945e0) · [`004945e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004945cc.md#insn-004945e8) · [`004945ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004945cc.md#insn-004945ec)

~~~diff
- 004942c0 ["INT_ADD", "register:40f0:8", ["const:4942c0:8", "const:4:8"]]
- 004942c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004945e0 ["INT_ADD", "register:40f0:8", ["const:4945e0:8", "const:4:8"]]
+ 004945e0 ["CALL", null, ["callee:00c58f30:8"]]
- 004942c0 bytes 280f1f94
+ 004945e0 bytes 54121f94
- 004942c8 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 004945e8 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004942c8 bytes 883e00b0
+ 004945e8 bytes 883e00d0
- 004942cc ["COPY", "tmp:0:8", ["const:da8:8"]]
- 004942cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004942cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004942cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004945ec ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 004945ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004945ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004945ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004942cc bytes 08a13691
+ 004945ec bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ebf044ac50ecbd5ead02a6ae14a60ab"></a>

### [`004942e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942e4.md) → [`00494604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494604.md) FUN_00494604

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494608",
      "incomplete_value": false,
      "site": "0049460c",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004942e8",
      "incomplete_value": false,
      "site": "004942ec",
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
            "const:da8:8"
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
      "0049460c",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049460c",
      "DATA",
      [
        "storage",
        "00c66d78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004942e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942e4.md#insn-004942e4) · [`004942e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004942e4.md#insn-004942e8)
- 新版 [`00494604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494604.md#insn-00494604) · [`00494608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494604.md#insn-00494608)

~~~diff
- 004942e4 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494604 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004942e4 bytes 883e00b0
+ 00494604 bytes 883e00d0
- 004942e8 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 004942e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004942e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004942e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494608 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00494608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004942e8 bytes 08a13691
+ 00494608 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad7d3f409ee1522856faf5332dc26648"></a>

### [`00494474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494474.md) → [`00494794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494794.md) FUN_00494794

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004947b4",
      "incomplete_value": false,
      "site": "004947b8",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494494",
      "incomplete_value": false,
      "site": "00494498",
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
            "const:e28:8"
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
      "004947b8",
      "DATA",
      [
        "storage",
        "00c65e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004947b8",
      "DATA",
      [
        "storage",
        "00c66df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494474.md#insn-00494488) · [`00494490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494474.md#insn-00494490) · [`00494494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494474.md#insn-00494494)
- 新版 [`004947a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494794.md#insn-004947a8) · [`004947b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494794.md#insn-004947b0) · [`004947b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494794.md#insn-004947b4)

~~~diff
- 00494488 ["INT_ADD", "register:40f0:8", ["const:494488:8", "const:4:8"]]
- 00494488 ["CALL", null, ["callee:00c58f30:8"]]
+ 004947a8 ["INT_ADD", "register:40f0:8", ["const:4947a8:8", "const:4:8"]]
+ 004947a8 ["CALL", null, ["callee:00c58f30:8"]]
- 00494488 bytes b60e1f94
+ 004947a8 bytes e2111f94
- 00494490 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 004947b0 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494490 bytes 883e00b0
+ 004947b0 bytes 883e00d0
- 00494494 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00494494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004947b4 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 004947b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004947b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004947b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494494 bytes 08a13891
+ 004947b4 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b101ea01762ea4c26f4fe9227396e6e"></a>

### [`004944ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944ac.md) → [`004947cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004947cc.md) FUN_004947cc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004947d0",
      "incomplete_value": false,
      "site": "004947d4",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004944b0",
      "incomplete_value": false,
      "site": "004944b4",
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
            "const:e28:8"
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
      "004947d4",
      "DATA",
      [
        "storage",
        "00c65e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004947d4",
      "DATA",
      [
        "storage",
        "00c66df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004944ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944ac.md#insn-004944ac) · [`004944b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004944ac.md#insn-004944b0)
- 新版 [`004947cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004947cc.md#insn-004947cc) · [`004947d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/004947cc.md#insn-004947d0)

~~~diff
- 004944ac ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 004947cc ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004944ac bytes 883e00b0
+ 004947cc bytes 883e00d0
- 004944b0 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 004944b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004944b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004944b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004947d0 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 004947d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004947d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004947d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004944b0 bytes 08a13891
+ 004947d0 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f526ed2dff8e76b7501dcca0a7808302"></a>

### [`004949dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004949dc.md) → [`00494cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494cfc.md) FUN_00494cfc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00494d08",
      "incomplete_value": false,
      "site": "00494d14",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004949e8",
      "incomplete_value": false,
      "site": "004949f4",
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
            "const:eb8:8"
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
      "00494d14",
      "DATA",
      [
        "storage",
        "00c65eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494d14",
      "DATA",
      [
        "storage",
        "00c66e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004949e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004949dc.md#insn-004949e4) · [`004949e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/004949dc.md#insn-004949e8)
- 新版 [`00494d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494cfc.md#insn-00494d04) · [`00494d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494cfc.md#insn-00494d08)

~~~diff
- 004949e4 ["COPY", "register:4050:8", ["const:c65000:8"]]
+ 00494d04 ["COPY", "register:4050:8", ["const:c66000:8"]]
- 004949e4 bytes 8a3e00b0
+ 00494d04 bytes 8a3e00d0
- 004949e8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 004949e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004949e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004949e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00494d08 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00494d08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00494d08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00494d08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004949e8 bytes 4ae13a91
+ 00494d08 bytes 4a213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b953f6f41eacff01bb26df2ae991c43"></a>

### [`00494a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a20.md) → [`00494d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d40.md) FUN_00494d40

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00494d58",
      "incomplete_value": false,
      "site": "00494d64",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494a38",
      "incomplete_value": false,
      "site": "00494a44",
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
            "const:eb8:8"
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
      "00494d64",
      "DATA",
      [
        "storage",
        "00c65eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494d64",
      "DATA",
      [
        "storage",
        "00c66e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a20.md#insn-00494a34) · [`00494a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a20.md#insn-00494a38) · [`00494a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a20.md#insn-00494a68)
- 新版 [`00494d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d40.md#insn-00494d54) · [`00494d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d40.md#insn-00494d58) · [`00494d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d40.md#insn-00494d88)

~~~diff
- 00494a34 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494d54 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494a34 bytes 883e00b0
+ 00494d54 bytes 883e00d0
- 00494a38 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00494a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494d58 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00494d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494a38 bytes 08e13a91
+ 00494d58 bytes 08213a91
- 00494a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494a68 ["INT_ADD", "register:40f0:8", ["const:494a68:8", "const:4:8"]]
- 00494a68 ["CALLIND", null, ["register:0:8"]]
+ 00494d88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494d88 ["INT_ADD", "register:40f0:8", ["const:494d88:8", "const:4:8"]]
+ 00494d88 ["CALLIND", null, ["register:0:8"]]
- 00494a68 bytes 00013fd6
+ 00494d88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad8f71515afcc78fe6d7b8db41f6b598"></a>

### [`00494a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a7c.md) → [`00494d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d9c.md) FUN_00494d9c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00494dc8",
      "incomplete_value": false,
      "site": "00494dc8",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494aa8",
      "incomplete_value": false,
      "site": "00494aa8",
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
            "const:eb8:8"
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
      "00494dc8",
      "DATA",
      [
        "storage",
        "00c65eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494dc8",
      "DATA",
      [
        "storage",
        "00c66e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a7c.md#insn-00494a90) · [`00494a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a7c.md#insn-00494a9c) · [`00494aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494a7c.md#insn-00494aa0)
- 新版 [`00494db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d9c.md#insn-00494db0) · [`00494dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d9c.md#insn-00494dbc) · [`00494dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494d9c.md#insn-00494dc0)

~~~diff
- 00494a90 ["INT_ADD", "register:40f0:8", ["const:494a90:8", "const:4:8"]]
- 00494a90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00494db0 ["INT_ADD", "register:40f0:8", ["const:494db0:8", "const:4:8"]]
+ 00494db0 ["CALL", null, ["callee:00c58f30:8"]]
- 00494a90 bytes 340d1f94
+ 00494db0 bytes 60101f94
- 00494a9c ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494dbc ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494a9c bytes 883e00b0
+ 00494dbc bytes 883e00d0
- 00494aa0 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00494aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494dc0 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00494dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494aa0 bytes 08e13a91
+ 00494dc0 bytes 08213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4967c5ea2f20b5fa478d030e42f56487"></a>

### [`00494b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494b0c.md) → [`00494e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494e2c.md) FUN_00494e2c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00494e4c",
      "incomplete_value": false,
      "site": "00494e4c",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494b2c",
      "incomplete_value": false,
      "site": "00494b2c",
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
            "const:eb8:8"
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
      "00494e4c",
      "DATA",
      [
        "storage",
        "00c65eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494e4c",
      "DATA",
      [
        "storage",
        "00c66e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494b0c.md#insn-00494b24) · [`00494b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494b0c.md#insn-00494b28) · [`00494b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494b0c.md#insn-00494b48)
- 新版 [`00494e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494e2c.md#insn-00494e44) · [`00494e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494e2c.md#insn-00494e48) · [`00494e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494e2c.md#insn-00494e68)

~~~diff
- 00494b24 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00494e44 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00494b24 bytes 883e00b0
+ 00494e44 bytes 883e00d0
- 00494b28 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00494b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494e48 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00494e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494b28 bytes 08e13a91
+ 00494e48 bytes 08213a91
- 00494b48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494b48 ["INT_ADD", "register:40f0:8", ["const:494b48:8", "const:4:8"]]
- 00494b48 ["CALLIND", null, ["register:0:8"]]
+ 00494e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494e68 ["INT_ADD", "register:40f0:8", ["const:494e68:8", "const:4:8"]]
+ 00494e68 ["CALLIND", null, ["register:0:8"]]
- 00494b48 bytes 00013fd6
+ 00494e68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-babdbc82ac53659a0bf19d884429cef3"></a>

### [`00494c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494c0c.md) → [`00494f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494f2c.md) FUN_00494f2c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00494554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494554.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00494874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494874.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00494f70",
      "incomplete_value": false,
      "site": "00494f78",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494c50",
      "incomplete_value": false,
      "site": "00494c58",
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
            "const:2b0:8"
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
      "00494f70",
      "PARAM",
      [
        "storage",
        "00ca52b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00494f70",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494c0c.md#insn-00494c58) · [`00494c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494c0c.md#insn-00494c48) · [`00494c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494c0c.md#insn-00494c4c)
- 新版 [`00494f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494f2c.md#insn-00494f78) · [`00494f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494f2c.md#insn-00494f68) · [`00494f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494f2c.md#insn-00494f6c)

~~~diff
- 00494c58 ["INT_ADD", "register:40f0:8", ["const:494c58:8", "const:4:8"]]
- 00494c58 ["CALL", null, ["callee:00494874:8"]]
+ 00494f78 ["INT_ADD", "register:40f0:8", ["const:494f78:8", "const:4:8"]]
+ 00494f78 ["CALL", null, ["callee:00494874:8"]]
- 00494c58 bytes 3ffeff97
+ 00494f78 bytes 3ffeff97
- 00494c48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494c48 ["INT_ADD", "register:40f0:8", ["const:494c48:8", "const:4:8"]]
- 00494c48 ["CALLIND", null, ["register:0:8"]]
+ 00494f68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494f68 ["INT_ADD", "register:40f0:8", ["const:494f68:8", "const:4:8"]]
+ 00494f68 ["CALLIND", null, ["register:0:8"]]
- 00494c48 bytes 00013fd6
+ 00494f68 bytes 00013fd6
- 00494c4c ["COPY", "register:4000:8", ["const:ca5000:8"]]
+ 00494f6c ["COPY", "register:4000:8", ["const:ca6000:8"]]
- 00494c4c bytes 804000b0
+ 00494f6c bytes 804000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acc87460559b10ada23ac8c7a5cee1c4"></a>

### [`00494e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494e48.md) → [`00495168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495168.md) _INIT_22

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`0048dca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dca8.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`0048dfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048dfc8.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 15件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004951a8",
      "incomplete_value": true,
      "site": "004951c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00494e88",
      "incomplete_value": true,
      "site": "00494ea4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004951cc",
      "incomplete_value": true,
      "site": "004951e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00494eac",
      "incomplete_value": true,
      "site": "00494ec8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004951ec",
      "incomplete_value": true,
      "site": "00495208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00494ecc",
      "incomplete_value": true,
      "site": "00494ee8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "004951a8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "004951cc",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "004951ec",
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
      "004951a8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "004951cc",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "004951ec",
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


#### 変更候補の命令位置

- 旧版 [`00494fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494e48.md#insn-00494fac) · [`00495084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494e48.md#insn-00495084) · [`004950bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494e48.md#insn-004950bc)
- 新版 [`004952cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495168.md#insn-004952cc) · [`004953a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495168.md#insn-004953a4) · [`004953dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495168.md#insn-004953dc)

~~~diff
- 00494fac ["INT_ADD", "register:40f0:8", ["const:494fac:8", "const:4:8"]]
- 00494fac ["CALL", null, ["callee:0043bb58:8"]]
+ 004952cc ["INT_ADD", "register:40f0:8", ["const:4952cc:8", "const:4:8"]]
+ 004952cc ["CALL", null, ["callee:0043bb58:8"]]
- 00494fac bytes 239afe97
+ 004952cc bytes 239afe97
- 00495084 ["INT_ADD", "register:40f0:8", ["const:495084:8", "const:4:8"]]
- 00495084 ["CALL", null, ["callee:00c58ed0:8"]]
+ 004953a4 ["INT_ADD", "register:40f0:8", ["const:4953a4:8", "const:4:8"]]
+ 004953a4 ["CALL", null, ["callee:00c58ed0:8"]]
- 00495084 bytes 9f0b1f94
+ 004953a4 bytes cb0e1f94
- 004950bc ["INT_ADD", "register:40f0:8", ["const:4950bc:8", "const:4:8"]]
- 004950bc ["CALL", null, ["callee:00c58ed0:8"]]
+ 004953dc ["INT_ADD", "register:40f0:8", ["const:4953dc:8", "const:4:8"]]
+ 004953dc ["CALL", null, ["callee:00c58ed0:8"]]
- 004950bc bytes 910b1f94
+ 004953dc bytes bd0e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcbe83cfc64af5986746927e9afb3cbe"></a>

### [`004952c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952c0.md) → [`004955e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/004955e0.md) FUN_004955e0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) [`00b2b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b990.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) [`00b2c984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2c/00b2c984.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049560c",
      "incomplete_value": true,
      "site": "00495618",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ff0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004952ec",
      "incomplete_value": true,
      "site": "004952f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa0:8"
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
      "definition_site": "004955e8",
      "incomplete_value": true,
      "site": "004955e8",
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
      "definition_site": "004952c8",
      "incomplete_value": true,
      "site": "004952c8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "004952c8"
      ],
      [
        "FALL_THROUGH",
        "004955e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "004955e8",
      "incomplete_value": true,
      "site": "004955f0",
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
      "definition_site": "004952c8",
      "incomplete_value": true,
      "site": "004952d0",
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
      "004955e4",
      "READ",
      [
        "storage",
        "00ca5310",
        null,
        "undefined8"
      ]
    ],
    [
      "0049560c",
      "READ",
      [
        "storage",
        "002c2fa0",
        null,
        null
      ]
    ],
    [
      "0049561c",
      "READ",
      [
        "storage",
        "00ca5308",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004955e4",
      "READ",
      [
        "storage",
        "00ca62d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0049560c",
      "READ",
      [
        "storage",
        "002c2ff0",
        null,
        null
      ]
    ],
    [
      "0049561c",
      "READ",
      [
        "storage",
        "00ca62c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004952c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952c0.md#insn-004952c0) · [`004952c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952c0.md#insn-004952c4) · [`004952e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952c0.md#insn-004952e4)
- 新版 [`004955e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/004955e0.md#insn-004955e0) · [`004955e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/004955e0.md#insn-004955e4) · [`00495604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/004955e0.md#insn-00495604)

~~~diff
- 004952c0 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 004955e0 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 004952c0 bytes 88400090
+ 004955e0 bytes 884000b0
- 004952c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
- 004952c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004955e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
+ 004955e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004952c4 bytes 088941f9
+ 004955e4 bytes 086941f9
- 004952e4 ["COPY", "register:40a8:8", ["const:ca5000:8"]]
+ 00495604 ["COPY", "register:40a8:8", ["const:ca6000:8"]]
- 004952e4 bytes 95400090
+ 00495604 bytes 954000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31407fb02d7b22e11ab48b6da9f12fc8"></a>

### [`00495414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md) → [`00495734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495734.md) FUN_00495734

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00853360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853360.md) [`00853cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cd0.md) [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) · 呼出先 2件 [`00495d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495d84.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 5件 [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`0085430c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00854/0085430c.md) [`00854c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00854/00854c7c.md) [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) [`008776f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md) · 呼出先 2件 [`004960a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/004960a4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004957f0",
      "incomplete_value": true,
      "site": "004957f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004954d0",
      "incomplete_value": true,
      "site": "004954d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00495750",
      "incomplete_value": true,
      "site": "00495750",
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
      "definition_site": "00495430",
      "incomplete_value": true,
      "site": "00495430",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004957a8",
      "incomplete_value": false,
      "site": "004957ac",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495488",
      "incomplete_value": false,
      "site": "0049548c",
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
            "const:2e8:8"
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
      "0049574c",
      "READ",
      [
        "storage",
        "00ca5310",
        null,
        "undefined8"
      ]
    ],
    [
      "00495764",
      "READ",
      [
        "storage",
        "00ca5310",
        null,
        "undefined8"
      ]
    ],
    [
      "00495770",
      "READ",
      [
        "storage",
        "00ca52f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049574c",
      "READ",
      [
        "storage",
        "00ca62d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00495764",
      "READ",
      [
        "storage",
        "00ca62d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00495770",
      "READ",
      [
        "storage",
        "00ca62b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md#insn-0049548c) · [`004954d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md#insn-004954d0) · [`00495424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md#insn-00495424)
- 新版 [`004957ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495734.md#insn-004957ac) · [`004957f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495734.md#insn-004957f0) · [`00495744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495734.md#insn-00495744)

~~~diff
- 0049548c ["INT_ADD", "register:40f0:8", ["const:49548c:8", "const:4:8"]]
- 0049548c ["CALL", null, ["callee:004960a4:8"]]
+ 004957ac ["INT_ADD", "register:40f0:8", ["const:4957ac:8", "const:4:8"]]
+ 004957ac ["CALL", null, ["callee:004960a4:8"]]
- 0049548c bytes 3e020094
+ 004957ac bytes 3e020094
- 004954d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:310:8"]]
- 004954d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 004957f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2d0:8"]]
+ 004957f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 004954d0 bytes a88a01f9
+ 004957f0 bytes a86a01f9
- 00495424 ["COPY", "register:40a8:8", ["const:ca5000:8"]]
+ 00495744 ["COPY", "register:40a8:8", ["const:ca6000:8"]]
- 00495424 bytes 95400090
+ 00495744 bytes 954000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cab7b6fb1dbca23c137bd9aea0fd79d"></a>

### [`004954f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004954f8.md) → [`00495818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495818.md) FUN_00495818

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 2件 [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00495844",
      "incomplete_value": true,
      "site": "0049584c",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495524",
      "incomplete_value": true,
      "site": "0049552c",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00495820",
      "incomplete_value": true,
      "site": "00495820",
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
      "definition_site": "00495500",
      "incomplete_value": true,
      "site": "00495500",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00495500"
      ],
      [
        "FALL_THROUGH",
        "00495820"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00495820",
      "incomplete_value": true,
      "site": "0049584c",
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
      "definition_site": "00495500",
      "incomplete_value": true,
      "site": "0049552c",
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
      "0049581c",
      "READ",
      [
        "storage",
        "00ca5310",
        null,
        "undefined8"
      ]
    ],
    [
      "0049582c",
      "READ",
      [
        "storage",
        "00ca5308",
        null,
        "undefined8"
      ]
    ],
    [
      "00495830",
      "READ",
      [
        "storage",
        "00ca52f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049581c",
      "READ",
      [
        "storage",
        "00ca62d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0049582c",
      "READ",
      [
        "storage",
        "00ca62c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00495830",
      "READ",
      [
        "storage",
        "00ca62b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004954f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004954f8.md#insn-004954f8) · [`004954fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004954f8.md#insn-004954fc) · [`00495504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004954f8.md#insn-00495504)
- 新版 [`00495818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495818.md#insn-00495818) · [`0049581c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495818.md#insn-0049581c) · [`00495824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495818.md#insn-00495824)

~~~diff
- 004954f8 ["COPY", "register:4048:8", ["const:ca5000:8"]]
+ 00495818 ["COPY", "register:4048:8", ["const:ca6000:8"]]
- 004954f8 bytes 89400090
+ 00495818 bytes 894000b0
- 004954fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:310:8"]]
- 004954fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049581c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d0:8"]]
+ 0049581c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004954fc bytes 298941f9
+ 0049581c bytes 296941f9
- 00495504 ["COPY", "register:4048:8", ["const:ca5000:8"]]
+ 00495824 ["COPY", "register:4048:8", ["const:ca6000:8"]]
- 00495504 bytes 89400090
+ 00495824 bytes 894000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e389d07f16a10b132ff38b0eafbd1ed"></a>

### [`00495558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md) → [`00495878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495878.md) FUN_00495878

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 19件 [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`00468a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468a00.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md)
- 新版 呼出元 1件 [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) · 呼出先 19件 [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md) [`00468d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468d20.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004958e8",
      "incomplete_value": true,
      "site": "004958f0",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004955c8",
      "incomplete_value": true,
      "site": "004955d0",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00495dcc",
      "incomplete_value": false,
      "site": "00495dcc",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495aac",
      "incomplete_value": false,
      "site": "00495aac",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004958b4",
      "incomplete_value": true,
      "site": "004958b4",
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
      "definition_site": "00495594",
      "incomplete_value": true,
      "site": "00495594",
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
      "004958b0",
      "READ",
      [
        "storage",
        "00ca5310",
        null,
        "undefined8"
      ]
    ],
    [
      "004958c4",
      "READ",
      [
        "storage",
        "00ca5308",
        null,
        "undefined8"
      ]
    ],
    [
      "004958c8",
      "READ",
      [
        "storage",
        "00ca52f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004958b0",
      "READ",
      [
        "storage",
        "00ca62d0",
        null,
        "undefined8"
      ]
    ],
    [
      "004958c4",
      "READ",
      [
        "storage",
        "00ca62c8",
        null,
        "undefined8"
      ]
    ],
    [
      "004958c8",
      "READ",
      [
        "storage",
        "00ca62b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md#insn-00495740) · [`00495750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md#insn-00495750) · [`0049578c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495558.md#insn-0049578c)
- 新版 [`00495a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495878.md#insn-00495a60) · [`00495a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495878.md#insn-00495a70) · [`00495aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495878.md#insn-00495aac)

~~~diff
- 00495740 ["INT_ADD", "register:40f0:8", ["const:495740:8", "const:4:8"]]
- 00495740 ["CALL", null, ["callee:00c596b0:8"]]
+ 00495a60 ["INT_ADD", "register:40f0:8", ["const:495a60:8", "const:4:8"]]
+ 00495a60 ["CALL", null, ["callee:00c596b0:8"]]
- 00495740 bytes e80b1f94
+ 00495a60 bytes 140f1f94
- 00495750 ["INT_ADD", "register:40f0:8", ["const:495750:8", "const:4:8"]]
- 00495750 ["CALL", null, ["callee:0046ce6c:8"]]
+ 00495a70 ["INT_ADD", "register:40f0:8", ["const:495a70:8", "const:4:8"]]
+ 00495a70 ["CALL", null, ["callee:0046ce6c:8"]]
- 00495750 bytes ff5cff97
+ 00495a70 bytes ff5cff97
- 0049578c ["INT_ADD", "register:40f0:8", ["const:49578c:8", "const:4:8"]]
- 0049578c ["CALL", null, ["callee:004699bc:8"]]
+ 00495aac ["INT_ADD", "register:40f0:8", ["const:495aac:8", "const:4:8"]]
+ 00495aac ["CALL", null, ["callee:004699bc:8"]]
- 0049578c bytes c44fff97
+ 00495aac bytes c44fff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-092e2a092078befe0f4e3388fae32218"></a>

### [`004966e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004966e4.md) → [`00496a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496a04.md) _INIT_23

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`004952bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952bc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`004955dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/004955dc.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 6件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00496a40",
      "incomplete_value": true,
      "site": "00496a5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00496720",
      "incomplete_value": true,
      "site": "0049673c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00496a64",
      "incomplete_value": true,
      "site": "00496a80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00496744",
      "incomplete_value": true,
      "site": "00496760",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00496a84",
      "incomplete_value": true,
      "site": "00496aa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00496764",
      "incomplete_value": true,
      "site": "00496780",
      "value": [
        "LOAD",
        "16",
        [
          [
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00496a40",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00496a64",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00496a84",
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
      "00496a40",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00496a64",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00496a84",
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


#### 変更候補の命令位置

- 旧版 [`00496844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004966e4.md#insn-00496844) · [`0049691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004966e4.md#insn-0049691c) · [`00496940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/004966e4.md#insn-00496940)
- 新版 [`00496b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496a04.md#insn-00496b64) · [`00496c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496a04.md#insn-00496c3c) · [`00496c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496a04.md#insn-00496c60)

~~~diff
- 00496844 ["INT_ADD", "register:40f0:8", ["const:496844:8", "const:4:8"]]
- 00496844 ["CALL", null, ["callee:0043bb58:8"]]
+ 00496b64 ["INT_ADD", "register:40f0:8", ["const:496b64:8", "const:4:8"]]
+ 00496b64 ["CALL", null, ["callee:0043bb58:8"]]
- 00496844 bytes fd93fe97
+ 00496b64 bytes fd93fe97
- 0049691c ["INT_ADD", "register:40f0:8", ["const:49691c:8", "const:4:8"]]
- 0049691c ["CALL", null, ["callee:00c58ed0:8"]]
+ 00496c3c ["INT_ADD", "register:40f0:8", ["const:496c3c:8", "const:4:8"]]
+ 00496c3c ["CALL", null, ["callee:00c58ed0:8"]]
- 0049691c bytes 79051f94
+ 00496c3c bytes a5081f94
- 00496940 ["INT_ADD", "register:40f0:8", ["const:496940:8", "const:4:8"]]
- 00496940 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00496c60 ["INT_ADD", "register:40f0:8", ["const:496c60:8", "const:4:8"]]
+ 00496c60 ["CALL", null, ["callee:00c58ed0:8"]]
- 00496940 bytes 70051f94
+ 00496c60 bytes 9c081f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841d960a159d736cdd1095e321aec19f"></a>

### [`00496a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496a9c.md) → [`00496dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496dbc.md) FUN_00496dbc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`007685fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/007685fc.md) [`00768848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768848.md) [`00768a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768a80.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md) · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00550c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c6c.md) [`0059705c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md)
- 新版 呼出元 6件 [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md) [`007689d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007689d8.md) [`00768c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768c24.md) [`00768e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768e5c.md) [`007692c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007692c4.md) · 呼出先 12件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00550f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f8c.md) [`0059737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059737c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00496ecc",
      "incomplete_value": false,
      "site": "00496ed4",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496bac",
      "incomplete_value": false,
      "site": "00496bb4",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00496eec",
      "incomplete_value": false,
      "site": "00496eec",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496bcc",
      "incomplete_value": false,
      "site": "00496bcc",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00496f70",
      "incomplete_value": false,
      "site": "00496f78",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496c50",
      "incomplete_value": false,
      "site": "00496c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "00496ed4",
      "DATA",
      [
        "storage",
        "00c65f60",
        null,
        "undefined *"
      ]
    ],
    [
      "00496eec",
      "DATA",
      [
        "storage",
        "00c65fb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00496f78",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00496ed4",
      "DATA",
      [
        "storage",
        "00c66f30",
        null,
        "undefined *"
      ]
    ],
    [
      "00496eec",
      "DATA",
      [
        "storage",
        "00c66f80",
        null,
        "undefined *"
      ]
    ],
    [
      "00496f78",
      "DATA",
      [
        "storage",
        "00c64b30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496a9c.md#insn-00496ad0) · [`00496b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496a9c.md#insn-00496b38) · [`00496b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496a9c.md#insn-00496b60)
- 新版 [`00496df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496dbc.md#insn-00496df0) · [`00496e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496dbc.md#insn-00496e58) · [`00496e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496dbc.md#insn-00496e80)

~~~diff
- 00496ad0 ["INT_ADD", "register:40f0:8", ["const:496ad0:8", "const:4:8"]]
- 00496ad0 ["CALL", null, ["callee:00550f8c:8"]]
+ 00496df0 ["INT_ADD", "register:40f0:8", ["const:496df0:8", "const:4:8"]]
+ 00496df0 ["CALL", null, ["callee:00550f8c:8"]]
- 00496ad0 bytes 67e80294
+ 00496df0 bytes 67e80294
- 00496b38 ["INT_ADD", "register:40f0:8", ["const:496b38:8", "const:4:8"]]
- 00496b38 ["CALL", null, ["callee:00c58f30:8"]]
+ 00496e58 ["INT_ADD", "register:40f0:8", ["const:496e58:8", "const:4:8"]]
+ 00496e58 ["CALL", null, ["callee:00c58f30:8"]]
- 00496b38 bytes 0a051f94
+ 00496e58 bytes 36081f94
- 00496b60 ["INT_ADD", "register:40f0:8", ["const:496b60:8", "const:4:8"]]
- 00496b60 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00496e80 ["INT_ADD", "register:40f0:8", ["const:496e80:8", "const:4:8"]]
+ 00496e80 ["CALL", null, ["callee:00c58fe0:8"]]
- 00496b60 bytes 2c051f94
+ 00496e80 bytes 58081f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b2e9f290e6a21ac72ff2327c249f116"></a>

### [`00496df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496df8.md) → [`00497118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497118.md) FUN_00497118

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
      "definition_site": "0049711c",
      "incomplete_value": false,
      "site": "00497120",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496dfc",
      "incomplete_value": false,
      "site": "00496e00",
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
            "const:f60:8"
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
      "00497120",
      "DATA",
      [
        "storage",
        "00c65f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497120",
      "DATA",
      [
        "storage",
        "00c66f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496df8.md#insn-00496df8) · [`00496dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496df8.md#insn-00496dfc)
- 新版 [`00497118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497118.md#insn-00497118) · [`0049711c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497118.md#insn-0049711c)

~~~diff
- 00496df8 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00497118 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00496df8 bytes 683e00f0
+ 00497118 bytes 683e00f0
- 00496dfc ["COPY", "tmp:0:8", ["const:f60:8"]]
- 00496dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00496dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00496dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049711c ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 0049711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00496dfc bytes 08813d91
+ 0049711c bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c584d84b3d0fa5b2b12a8ee7b477b9eb"></a>

### [`00496e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e08.md) → [`00497128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497128.md) FUN_00497128

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
      "definition_site": "00497138",
      "incomplete_value": false,
      "site": "00497140",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496e18",
      "incomplete_value": false,
      "site": "00496e20",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00497140",
      "DATA",
      [
        "storage",
        "00c65f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497140",
      "DATA",
      [
        "storage",
        "00c66f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e08.md#insn-00496e14) · [`00496e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e08.md#insn-00496e18) · [`00496e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e08.md#insn-00496e24)
- 新版 [`00497134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497128.md#insn-00497134) · [`00497138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497128.md#insn-00497138) · [`00497144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497128.md#insn-00497144)

~~~diff
- 00496e14 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00497134 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00496e14 bytes 683e00f0
+ 00497134 bytes 683e00f0
- 00496e18 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 00496e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00496e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00496e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00497138 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 00497138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00497138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00497138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00496e18 bytes 08813d91
+ 00497138 bytes 08c13c91
- 00496e24 ["INT_ADD", "register:40f0:8", ["const:496e24:8", "const:4:8"]]
- 00496e24 ["CALL", null, ["callee:00c58f40:8"]]
+ 00497144 ["INT_ADD", "register:40f0:8", ["const:497144:8", "const:4:8"]]
+ 00497144 ["CALL", null, ["callee:00c58f40:8"]]
- 00496e24 bytes 53041f94
+ 00497144 bytes 7f071f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68903d1e2ceb1b3e3e92792255580226"></a>

### [`00496e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e38.md) → [`00497158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497158.md) FUN_00497158

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00497170",
      "incomplete_value": false,
      "site": "00497174",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496e50",
      "incomplete_value": false,
      "site": "00496e54",
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
            "const:fb0:8"
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
      "00497174",
      "DATA",
      [
        "storage",
        "00c65fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497174",
      "DATA",
      [
        "storage",
        "00c66f80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e38.md#insn-00496e4c) · [`00496e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e38.md#insn-00496e50) · [`00496e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496e38.md#insn-00496e64)
- 新版 [`0049716c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497158.md#insn-0049716c) · [`00497170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497158.md#insn-00497170) · [`00497184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497158.md#insn-00497184)

~~~diff
- 00496e4c ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 0049716c ["COPY", "register:4040:8", ["const:c66000:8"]]
- 00496e4c bytes 683e00f0
+ 0049716c bytes 683e00f0
- 00496e50 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00496e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00496e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00496e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00497170 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00497170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00497170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00497170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00496e50 bytes 08c13e91
+ 00497170 bytes 08013e91
- 00496e64 ["INT_ADD", "register:40f0:8", ["const:496e64:8", "const:4:8"]]
- 00496e64 ["CALL", null, ["callee:00c54d90:8"]]
+ 00497184 ["INT_ADD", "register:40f0:8", ["const:497184:8", "const:4:8"]]
+ 00497184 ["CALL", null, ["callee:00c54d90:8"]]
- 00496e64 bytes cff31e94
+ 00497184 bytes 03f71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83f8507ddb8864eac550d30b2f29cd28"></a>

### [`00497078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497078.md) → [`00497398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497398.md) FUN_00497398

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00597150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597150.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md) [`00597470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597470.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004973e0",
      "incomplete_value": true,
      "site": "004973e8",
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
      "definition_site": "004970c0",
      "incomplete_value": true,
      "site": "004970c8",
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
      "004973d4",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ],
    [
      "004973e8",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00497410",
      "READ",
      [
        "storage",
        "00c6d6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004973d4",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "004973e8",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00497410",
      "READ",
      [
        "storage",
        "00c6e6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004970a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497078.md#insn-004970a8) · [`004970ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497078.md#insn-004970ac) · [`004970b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497078.md#insn-004970b4)
- 新版 [`004973c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497398.md#insn-004973c8) · [`004973cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497398.md#insn-004973cc) · [`004973d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497398.md#insn-004973d4)

~~~diff
- 004970a8 ["INT_ADD", "register:40f0:8", ["const:4970a8:8", "const:4:8"]]
- 004970a8 ["CALL", null, ["callee:00c58f30:8"]]
+ 004973c8 ["INT_ADD", "register:40f0:8", ["const:4973c8:8", "const:4:8"]]
+ 004973c8 ["CALL", null, ["callee:00c58f30:8"]]
- 004970a8 bytes ae031f94
+ 004973c8 bytes da061f94
- 004970ac ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004973cc ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004970ac bytes 094000f0
+ 004973cc bytes 29400090
- 004970b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cf0:8"]]
- 004970b4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004973d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
+ 004973d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004970b4 bytes 297946f9
+ 004973d4 bytes 296146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba7884bb1595c768752acb0ff7c4502"></a>

### [`00497154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497154.md) → [`00497474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497474.md) FUN_00497474

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00597150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597150.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md) [`00597470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597470.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004974c4",
      "incomplete_value": true,
      "site": "004974cc",
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
      "definition_site": "004971a4",
      "incomplete_value": true,
      "site": "004971ac",
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
      "004974b8",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ],
    [
      "004974cc",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "004974f4",
      "READ",
      [
        "storage",
        "00c6d6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004974b8",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "004974cc",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ],
    [
      "004974f4",
      "READ",
      [
        "storage",
        "00c6e6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497154.md#insn-00497188) · [`0049718c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497154.md#insn-0049718c) · [`00497198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497154.md#insn-00497198)
- 新版 [`004974a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497474.md#insn-004974a8) · [`004974ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497474.md#insn-004974ac) · [`004974b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497474.md#insn-004974b8)

~~~diff
- 00497188 ["INT_ADD", "register:40f0:8", ["const:497188:8", "const:4:8"]]
- 00497188 ["CALL", null, ["callee:00c58f30:8"]]
+ 004974a8 ["INT_ADD", "register:40f0:8", ["const:4974a8:8", "const:4:8"]]
+ 004974a8 ["CALL", null, ["callee:00c58f30:8"]]
- 00497188 bytes 76031f94
+ 004974a8 bytes a2061f94
- 0049718c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004974ac ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0049718c bytes 094000f0
+ 004974ac bytes 29400090
- 00497198 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cf0:8"]]
- 00497198 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004974b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
+ 004974b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00497198 bytes 297946f9
+ 004974b8 bytes 296146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca2252b5b511ddecc4106f9f870ea34"></a>

### [`0049723c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049723c.md) → [`0049755c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049755c.md) FUN_0049755c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00597150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597150.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md) [`00597470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597470.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004975a8",
      "incomplete_value": true,
      "site": "004975b0",
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
      "definition_site": "00497288",
      "incomplete_value": true,
      "site": "00497290",
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
      "0049759c",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ],
    [
      "004975b0",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "004975d8",
      "READ",
      [
        "storage",
        "00c6d6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049759c",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "004975b0",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ],
    [
      "004975d8",
      "READ",
      [
        "storage",
        "00c6e6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049726c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049723c.md#insn-0049726c) · [`00497270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049723c.md#insn-00497270) · [`0049727c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049723c.md#insn-0049727c)
- 新版 [`0049758c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049755c.md#insn-0049758c) · [`00497590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049755c.md#insn-00497590) · [`0049759c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049755c.md#insn-0049759c)

~~~diff
- 0049726c ["INT_ADD", "register:40f0:8", ["const:49726c:8", "const:4:8"]]
- 0049726c ["CALL", null, ["callee:00c58f30:8"]]
+ 0049758c ["INT_ADD", "register:40f0:8", ["const:49758c:8", "const:4:8"]]
+ 0049758c ["CALL", null, ["callee:00c58f30:8"]]
- 0049726c bytes 3d031f94
+ 0049758c bytes 69061f94
- 00497270 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00497590 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00497270 bytes 094000f0
+ 00497590 bytes 29400090
- 0049727c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cf0:8"]]
- 0049727c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049759c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
+ 0049759c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049727c bytes 297946f9
+ 0049759c bytes 296146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2ea4f82a38f8ad0c73e05c5ab39817"></a>

### [`0049731c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049731c.md) → [`0049763c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049763c.md) FUN_0049763c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00597150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597150.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md) [`00597470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597470.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497684",
      "incomplete_value": true,
      "site": "0049768c",
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
      "definition_site": "00497364",
      "incomplete_value": true,
      "site": "0049736c",
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
      "00497678",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ],
    [
      "0049768c",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "004976b4",
      "READ",
      [
        "storage",
        "00c6d6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497678",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "0049768c",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ],
    [
      "004976b4",
      "READ",
      [
        "storage",
        "00c6e6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049734c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049731c.md#insn-0049734c) · [`00497350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049731c.md#insn-00497350) · [`00497358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/0049731c.md#insn-00497358)
- 新版 [`0049766c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049763c.md#insn-0049766c) · [`00497670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049763c.md#insn-00497670) · [`00497678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/0049763c.md#insn-00497678)

~~~diff
- 0049734c ["INT_ADD", "register:40f0:8", ["const:49734c:8", "const:4:8"]]
- 0049734c ["CALL", null, ["callee:00c58f30:8"]]
+ 0049766c ["INT_ADD", "register:40f0:8", ["const:49766c:8", "const:4:8"]]
+ 0049766c ["CALL", null, ["callee:00c58f30:8"]]
- 0049734c bytes 05031f94
+ 0049766c bytes 31061f94
- 00497350 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00497670 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00497350 bytes 094000f0
+ 00497670 bytes 29400090
- 00497358 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cf0:8"]]
- 00497358 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497678 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
+ 00497678 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00497358 bytes 297946f9
+ 00497678 bytes 296146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6d0191cadf14b59cb3b4a2830cdd7c"></a>

### [`00497400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497400.md) → [`00497720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497720.md) FUN_00497720

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00550d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`00451d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451d38.md) [`00551098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/00551098.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497798",
      "incomplete_value": true,
      "site": "004977a0",
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
      "definition_site": "00497478",
      "incomplete_value": true,
      "site": "00497480",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004977a8",
      "incomplete_value": true,
      "site": "004977a8",
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
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "00497488",
      "incomplete_value": true,
      "site": "00497488",
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
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004977a8",
      "incomplete_value": true,
      "site": "004977a8",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497488",
      "incomplete_value": true,
      "site": "00497488",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
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
      "00497794",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00497798",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0049779c",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00497794",
      "READ",
      [
        "storage",
        "00c9bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00497798",
      "READ",
      [
        "storage",
        "00c94188",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0049779c",
      "READ",
      [
        "storage",
        "00c941c8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497400.md#insn-00497430) · [`0049743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497400.md#insn-0049743c) · [`00497448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497400.md#insn-00497448)
- 新版 [`00497750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497720.md#insn-00497750) · [`0049775c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497720.md#insn-0049775c) · [`00497768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497720.md#insn-00497768)

~~~diff
- 00497430 ["INT_ADD", "register:40f0:8", ["const:497430:8", "const:4:8"]]
- 00497430 ["CALL", null, ["callee:00451c10:8"]]
+ 00497750 ["INT_ADD", "register:40f0:8", ["const:497750:8", "const:4:8"]]
+ 00497750 ["CALL", null, ["callee:00451c10:8"]]
- 00497430 bytes 30e9fe97
+ 00497750 bytes 30e9fe97
- 0049743c ["INT_ADD", "register:40f0:8", ["const:49743c:8", "const:4:8"]]
- 0049743c ["CALL", null, ["callee:00451d38:8"]]
+ 0049775c ["INT_ADD", "register:40f0:8", ["const:49775c:8", "const:4:8"]]
+ 0049775c ["CALL", null, ["callee:00451d38:8"]]
- 0049743c bytes 77e9fe97
+ 0049775c bytes 77e9fe97
- 00497448 ["INT_ADD", "register:40f0:8", ["const:497448:8", "const:4:8"]]
- 00497448 ["CALL", null, ["callee:00c59250:8"]]
+ 00497768 ["INT_ADD", "register:40f0:8", ["const:497768:8", "const:4:8"]]
+ 00497768 ["CALL", null, ["callee:00c59250:8"]]
- 00497448 bytes 8e031f94
+ 00497768 bytes ba061f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ab71b69899eaf2e423b5e11fbe6a4b0"></a>

### [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) → [`00497a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md) FUN_00497a04

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048cec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec0.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`0048d1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e0.md) · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497a40",
      "incomplete_value": true,
      "site": "00497a58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497720",
      "incomplete_value": true,
      "site": "00497738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:94b:8"
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
      "definition_site": "00497a5c",
      "incomplete_value": true,
      "site": "00497a70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049773c",
      "incomplete_value": true,
      "site": "00497750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00497a40",
      "READ",
      [
        "storage",
        "002b094b",
        null,
        "string"
      ]
    ],
    [
      "00497a5c",
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
      "00497a40",
      "READ",
      [
        "storage",
        "002b0a22",
        null,
        "string"
      ]
    ],
    [
      "00497a5c",
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

- 旧版 [`00497708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md#insn-00497708) · [`00497710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md#insn-00497710) · [`0049771c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md#insn-0049771c)
- 新版 [`00497a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md#insn-00497a28) · [`00497a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md#insn-00497a30) · [`00497a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497a04.md#insn-00497a3c)

~~~diff
- 00497708 ["INT_ADD", "register:40f0:8", ["const:497708:8", "const:4:8"]]
- 00497708 ["CALL", null, ["callee:005891cc:8"]]
+ 00497a28 ["INT_ADD", "register:40f0:8", ["const:497a28:8", "const:4:8"]]
+ 00497a28 ["CALL", null, ["callee:005891cc:8"]]
- 00497708 bytes e9c50394
+ 00497a28 bytes e9c50394
- 00497710 ["INT_ADD", "register:40f0:8", ["const:497710:8", "const:4:8"]]
- 00497710 ["CALL", null, ["callee:005894bc:8"]]
+ 00497a30 ["INT_ADD", "register:40f0:8", ["const:497a30:8", "const:4:8"]]
+ 00497a30 ["CALL", null, ["callee:005894bc:8"]]
- 00497710 bytes a3c60394
+ 00497a30 bytes a3c60394
- 0049771c ["COPY", "tmp:0:8", ["const:94b:8"]]
- 0049771c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049771c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049771c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00497a3c ["COPY", "tmp:0:8", ["const:a22:8"]]
+ 00497a3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00497a3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00497a3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049771c bytes 292d2591
+ 00497a3c bytes 29892891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a793c12fe8d9f65a86b5086a50c961"></a>

### [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) → [`00497c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md) FUN_00497c30

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) · 呼出先 8件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`0048d1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b0.md) · 呼出先 8件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497c70",
      "incomplete_value": true,
      "site": "00497c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497950",
      "incomplete_value": true,
      "site": "00497968",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2c3:8"
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
      "00497c70",
      "READ",
      [
        "storage",
        "002ab2c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00497c70",
      "READ",
      [
        "storage",
        "002ab390",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md#insn-00497930) · [`00497938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md#insn-00497938) · [`00497944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md#insn-00497944)
- 新版 [`00497c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md#insn-00497c50) · [`00497c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md#insn-00497c58) · [`00497c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497c30.md#insn-00497c64)

~~~diff
- 00497930 ["INT_ADD", "register:40f0:8", ["const:497930:8", "const:4:8"]]
- 00497930 ["CALL", null, ["callee:005891cc:8"]]
+ 00497c50 ["INT_ADD", "register:40f0:8", ["const:497c50:8", "const:4:8"]]
+ 00497c50 ["CALL", null, ["callee:005891cc:8"]]
- 00497930 bytes 5fc50394
+ 00497c50 bytes 5fc50394
- 00497938 ["INT_ADD", "register:40f0:8", ["const:497938:8", "const:4:8"]]
- 00497938 ["CALL", null, ["callee:005894bc:8"]]
+ 00497c58 ["INT_ADD", "register:40f0:8", ["const:497c58:8", "const:4:8"]]
+ 00497c58 ["CALL", null, ["callee:005894bc:8"]]
- 00497938 bytes 19c60394
+ 00497c58 bytes 19c60394
- 00497944 ["COPY", "tmp:0:8", ["const:2c3:8"]]
- 00497944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00497944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00497944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00497c64 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00497c64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00497c64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00497c64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00497944 bytes 290d0b91
+ 00497c64 bytes 29410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2003e84b4bf84f2e698a88edf43650e"></a>

### [`00497b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497b24.md) → [`00497e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497e44.md) FUN_00497e44

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00635530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00635/00635530.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006358e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00635/006358e0.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00497e84",
      "incomplete_value": false,
      "site": "00497e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497b64",
      "incomplete_value": false,
      "site": "00497b68",
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
            "const:48:8"
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
      "definition_site": "00497ecc",
      "incomplete_value": false,
      "site": "00497ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497bac",
      "incomplete_value": false,
      "site": "00497bb0",
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
            "const:98:8"
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
      "00497e88",
      "DATA",
      [
        "storage",
        "00c66048",
        null,
        "undefined *"
      ]
    ],
    [
      "00497ed0",
      "DATA",
      [
        "storage",
        "00c66098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497e88",
      "DATA",
      [
        "storage",
        "00c67018",
        null,
        "undefined *"
      ]
    ],
    [
      "00497ed0",
      "DATA",
      [
        "storage",
        "00c67068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497b24.md#insn-00497b58) · [`00497b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497b24.md#insn-00497b60) · [`00497b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497b24.md#insn-00497b64)
- 新版 [`00497e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497e44.md#insn-00497e78) · [`00497e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497e44.md#insn-00497e80) · [`00497e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497e44.md#insn-00497e84)

~~~diff
- 00497b58 ["INT_ADD", "register:40f0:8", ["const:497b58:8", "const:4:8"]]
- 00497b58 ["CALL", null, ["callee:00c58f30:8"]]
+ 00497e78 ["INT_ADD", "register:40f0:8", ["const:497e78:8", "const:4:8"]]
+ 00497e78 ["CALL", null, ["callee:00c58f30:8"]]
- 00497b58 bytes 02011f94
+ 00497e78 bytes 2e041f94
- 00497b60 ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00497e80 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 00497b60 bytes 683e00f0
+ 00497e80 bytes 883e0090
- 00497b64 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00497b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00497b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00497b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00497e84 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00497e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00497e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00497e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00497b64 bytes 08210191
+ 00497e84 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca9a2b2644041158ab356bcc82997ee"></a>

### [`00497cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md) → [`00497fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497fdc.md) FUN_00497fdc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00635530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00635/00635530.md) · 呼出先 7件 [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58240.md)
- 新版 呼出元 2件 [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`006358e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00635/006358e0.md) · 呼出先 7件 [`00498434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00498024",
      "incomplete_value": true,
      "site": "00498028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497d04",
      "incomplete_value": true,
      "site": "00497d08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00498010",
      "incomplete_value": false,
      "site": "00498014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:6fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497cf0",
      "incomplete_value": false,
      "site": "00497cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:62d:8"
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
      "00498010",
      "PARAM",
      [
        "storage",
        "002ad62d",
        null,
        "string"
      ]
    ],
    [
      "00498024",
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
      "00498010",
      "PARAM",
      [
        "storage",
        "002ad6fa",
        null,
        "string"
      ]
    ],
    [
      "00498024",
      "READ",
      [
        "storage",
        "002c3fd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md#insn-00497cf4) · [`00497cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md#insn-00497cf0) · [`00497d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497cbc.md#insn-00497d04)
- 新版 [`00498014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497fdc.md#insn-00498014) · [`00498010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497fdc.md#insn-00498010) · [`00498024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497fdc.md#insn-00498024)

~~~diff
- 00497cf4 ["INT_ADD", "register:40f0:8", ["const:497cf4:8", "const:4:8"]]
- 00497cf4 ["CALL", null, ["callee:00c59510:8"]]
+ 00498014 ["INT_ADD", "register:40f0:8", ["const:498014:8", "const:4:8"]]
+ 00498014 ["CALL", null, ["callee:00c59510:8"]]
- 00497cf4 bytes 13021f94
+ 00498014 bytes 3f051f94
- 00497cf0 ["COPY", "tmp:0:8", ["const:62d:8"]]
- 00497cf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00497cf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00497cf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00498010 ["COPY", "tmp:0:8", ["const:6fa:8"]]
+ 00498010 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00498010 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00498010 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00497cf0 bytes 00b41891
+ 00498010 bytes 00e81b91
- 00497d04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
- 00497d04 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00497d04 ["COPY", "register:5008:8", ["const:0:8"]]
- 00497d04 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00498024 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
+ 00498024 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00498024 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00498024 ["COPY", "register:5010:8", ["const:0:8"]]
- 00497d04 bytes 00c147fd
+ 00498024 bytes 00e947fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15c87ecf57603d9fac7ebe57bcd64e62"></a>

### [`00497e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md) → [`00498154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498154.md) FUN_00498154

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00635530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00635/00635530.md) · 呼出先 11件 [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) [`00498d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`006358e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00635/006358e0.md) · 呼出先 11件 [`00498434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md) [`0049905c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004981a4",
      "incomplete_value": true,
      "site": "004981a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497e84",
      "incomplete_value": true,
      "site": "00497e88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00498190",
      "incomplete_value": false,
      "site": "00498194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:6fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497e70",
      "incomplete_value": false,
      "site": "00497e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:62d:8"
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
      "definition_site": "004982b4",
      "incomplete_value": false,
      "site": "004982c4",
      "value": [
        "leaf",
        "const:49905c:8"
      ]
    },
    "old": {
      "definition_site": "00497f94",
      "incomplete_value": false,
      "site": "00497fa4",
      "value": [
        "leaf",
        "const:498d3c:8"
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00498190",
      "PARAM",
      [
        "storage",
        "002ad62d",
        null,
        "string"
      ]
    ],
    [
      "004981a4",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ],
    [
      "004982b4",
      "PARAM",
      [
        "storage",
        "00498d3c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00498190",
      "PARAM",
      [
        "storage",
        "002ad6fa",
        null,
        "string"
      ]
    ],
    [
      "004981a4",
      "READ",
      [
        "storage",
        "002c3fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "004982b4",
      "PARAM",
      [
        "storage",
        "0049905c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md#insn-00497e74) · [`00497fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md#insn-00497fa4) · [`00498038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md#insn-00498038)
- 新版 [`00498194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498154.md#insn-00498194) · [`004982c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498154.md#insn-004982c4) · [`00498358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498154.md#insn-00498358)

~~~diff
- 00497e74 ["INT_ADD", "register:40f0:8", ["const:497e74:8", "const:4:8"]]
- 00497e74 ["CALL", null, ["callee:00c59510:8"]]
+ 00498194 ["INT_ADD", "register:40f0:8", ["const:498194:8", "const:4:8"]]
+ 00498194 ["CALL", null, ["callee:00c59510:8"]]
- 00497e74 bytes b3011f94
+ 00498194 bytes df041f94
- 00497fa4 ["INT_ADD", "register:40f0:8", ["const:497fa4:8", "const:4:8"]]
- 00497fa4 ["CALL", null, ["callee:00c591b0:8"]]
+ 004982c4 ["INT_ADD", "register:40f0:8", ["const:4982c4:8", "const:4:8"]]
+ 004982c4 ["CALL", null, ["callee:00c591b0:8"]]
- 00497fa4 bytes 8f001f94
+ 004982c4 bytes bb031f94
- 00498038 ["INT_ADD", "register:40f0:8", ["const:498038:8", "const:4:8"]]
- 00498038 ["CALL", null, ["callee:00c591c0:8"]]
+ 00498358 ["INT_ADD", "register:40f0:8", ["const:498358:8", "const:4:8"]]
+ 00498358 ["CALL", null, ["callee:00c591c0:8"]]
- 00498038 bytes 6e001f94
+ 00498358 bytes 9a031f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-327ddc84cfde323304bcc7baa9f7ddd9"></a>

### [`00498388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md) → [`004986a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md) FUN_004986a8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00498724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md) [`006333b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) [`00633824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/00633824.md) [`008536f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/008536f8.md) · 呼出先 4件 [`00498114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498114.md) [`00498620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498620.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c586f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586f0.md)
- 新版 呼出元 4件 [`00498a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md) [`00633764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00633/00633764.md) [`00633bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00633/00633bd4.md) [`008546a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00854/008546a4.md) · 呼出先 4件 [`00498434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498434.md) [`00498940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498940.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c596c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049872c",
      "incomplete_value": true,
      "site": "00498738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049840c",
      "incomplete_value": true,
      "site": "00498418",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b0:8"
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
      "0049872c",
      "READ",
      [
        "storage",
        "002c40b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049872c",
      "READ",
      [
        "storage",
        "002c4100",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004983b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md#insn-004983b0) · [`004983f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md#insn-004983f0) · [`0049840c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md#insn-0049840c)
- 新版 [`004986d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md#insn-004986d0) · [`00498710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md#insn-00498710) · [`0049872c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md#insn-0049872c)

~~~diff
- 004983b0 ["INT_ADD", "register:40f0:8", ["const:4983b0:8", "const:4:8"]]
- 004983b0 ["CALL", null, ["callee:00c596c0:8"]]
+ 004986d0 ["INT_ADD", "register:40f0:8", ["const:4986d0:8", "const:4:8"]]
+ 004986d0 ["CALL", null, ["callee:00c596c0:8"]]
- 004983b0 bytes d0001f94
+ 004986d0 bytes fc031f94
- 004983f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004983f0 ["INT_ADD", "register:40f0:8", ["const:4983f0:8", "const:4:8"]]
- 004983f0 ["CALLIND", null, ["register:0:8"]]
+ 00498710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00498710 ["INT_ADD", "register:40f0:8", ["const:498710:8", "const:4:8"]]
+ 00498710 ["CALLIND", null, ["register:0:8"]]
- 004983f0 bytes 00013fd6
+ 00498710 bytes 00013fd6
- 0049840c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b0:8"]]
- 0049840c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0049840c ["COPY", "register:5008:8", ["const:0:8"]]
- 0049840c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0049872c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 0049872c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049872c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0049872c ["COPY", "register:5010:8", ["const:0:8"]]
- 0049840c bytes 005940fd
+ 0049872c bytes 008140fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275a4d34699c6335f0bb8b02e033c030"></a>

### [`00498724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md) → [`00498a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md) FUN_00498a44

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00635b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00635/00635b20.md) [`006360b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00636/006360b8.md) [`0086afac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086afac.md) [`0086b22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md) · 呼出先 6件 [`00498388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498388.md) [`0049ad24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad24.md) [`0049ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ad34.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 4件 [`00635ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00635/00635ed0.md) [`00636468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00636/00636468.md) [`0086bf58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bf58.md) [`0086c1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c1d8.md) · 呼出先 6件 [`004986a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/004986a8.md) [`0049b044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b044.md) [`0049b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b054.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "00498a98",
      "incomplete_value": false,
      "site": "00498a98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498778",
      "incomplete_value": false,
      "site": "00498778",
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
            "const:1e8:8"
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
      "00498a98",
      "DATA",
      [
        "storage",
        "00c661e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00498ad0",
      "READ",
      [
        "storage",
        "00c66208",
        null,
        "pointer"
      ]
    ],
    [
      "00498ad0",
      "READ",
      [
        "storage",
        "00c66210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498a98",
      "DATA",
      [
        "storage",
        "00c671b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00498ad0",
      "READ",
      [
        "storage",
        "00c671d8",
        null,
        "pointer"
      ]
    ],
    [
      "00498ad0",
      "READ",
      [
        "storage",
        "00c671e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md#insn-00498758) · [`00498764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md#insn-00498764) · [`0049876c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md#insn-0049876c)
- 新版 [`00498a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md#insn-00498a78) · [`00498a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md#insn-00498a84) · [`00498a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md#insn-00498a8c)

~~~diff
- 00498758 ["INT_ADD", "register:40f0:8", ["const:498758:8", "const:4:8"]]
- 00498758 ["CALL", null, ["callee:00c54d60:8"]]
+ 00498a78 ["INT_ADD", "register:40f0:8", ["const:498a78:8", "const:4:8"]]
+ 00498a78 ["CALL", null, ["callee:00c54d60:8"]]
- 00498758 bytes 86ed1e94
+ 00498a78 bytes baf01e94
- 00498764 ["INT_ADD", "register:40f0:8", ["const:498764:8", "const:4:8"]]
- 00498764 ["CALL", null, ["callee:00c54d60:8"]]
+ 00498a84 ["INT_ADD", "register:40f0:8", ["const:498a84:8", "const:4:8"]]
+ 00498a84 ["CALL", null, ["callee:00c54d60:8"]]
- 00498764 bytes 83ed1e94
+ 00498a84 bytes b7f01e94
- 0049876c ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00498a8c ["COPY", "register:4040:8", ["const:c67000:8"]]
- 0049876c bytes 683e00d0
+ 00498a8c bytes 683e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fff2fe511322cf52d23ef893bc1e46e"></a>

### [`0049891c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049891c.md) → [`00498c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c3c.md) FUN_00498c3c

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
      "definition_site": "00498c40",
      "incomplete_value": false,
      "site": "00498c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498920",
      "incomplete_value": false,
      "site": "00498924",
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
            "const:48:8"
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
      "00498c44",
      "DATA",
      [
        "storage",
        "00c66048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498c44",
      "DATA",
      [
        "storage",
        "00c67018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049891c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049891c.md#insn-0049891c) · [`00498920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049891c.md#insn-00498920)
- 新版 [`00498c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c3c.md#insn-00498c3c) · [`00498c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c3c.md#insn-00498c40)

~~~diff
- 0049891c ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00498c3c ["COPY", "register:4040:8", ["const:c67000:8"]]
- 0049891c bytes 683e00d0
+ 00498c3c bytes 683e00f0
- 00498920 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00498920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00498920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00498920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00498c40 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00498c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00498c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00498c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00498920 bytes 08210191
+ 00498c40 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbc76edfc4fab8ce448a346cd23e0b0d"></a>

### [`0049892c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049892c.md) → [`00498c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c4c.md) FUN_00498c4c

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
      "definition_site": "00498c5c",
      "incomplete_value": false,
      "site": "00498c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049893c",
      "incomplete_value": false,
      "site": "00498944",
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
            "const:48:8"
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
      "00498c64",
      "DATA",
      [
        "storage",
        "00c66048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498c64",
      "DATA",
      [
        "storage",
        "00c67018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049892c.md#insn-00498938) · [`0049893c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049892c.md#insn-0049893c) · [`00498948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/0049892c.md#insn-00498948)
- 新版 [`00498c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c4c.md#insn-00498c58) · [`00498c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c4c.md#insn-00498c5c) · [`00498c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498c4c.md#insn-00498c68)

~~~diff
- 00498938 ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00498c58 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 00498938 bytes 683e00d0
+ 00498c58 bytes 683e00f0
- 0049893c ["COPY", "tmp:0:8", ["const:48:8"]]
- 0049893c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049893c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049893c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00498c5c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00498c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00498c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00498c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049893c bytes 08210191
+ 00498c5c bytes 08610091
- 00498948 ["INT_ADD", "register:40f0:8", ["const:498948:8", "const:4:8"]]
- 00498948 ["CALL", null, ["callee:00c58f40:8"]]
+ 00498c68 ["INT_ADD", "register:40f0:8", ["const:498c68:8", "const:4:8"]]
+ 00498c68 ["CALL", null, ["callee:00c58f40:8"]]
- 00498948 bytes 8afd1e94
+ 00498c68 bytes b6001f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b9b003600245faceda536d2dced942"></a>

### [`00498b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b2c.md) → [`00498e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e4c.md) FUN_00498e4c

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
      "definition_site": "00498e50",
      "incomplete_value": false,
      "site": "00498e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498b30",
      "incomplete_value": false,
      "site": "00498b34",
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
            "const:98:8"
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
      "00498e54",
      "DATA",
      [
        "storage",
        "00c66098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498e54",
      "DATA",
      [
        "storage",
        "00c67068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b2c.md#insn-00498b2c) · [`00498b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b2c.md#insn-00498b30)
- 新版 [`00498e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e4c.md#insn-00498e4c) · [`00498e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e4c.md#insn-00498e50)

~~~diff
- 00498b2c ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00498e4c ["COPY", "register:4040:8", ["const:c67000:8"]]
- 00498b2c bytes 683e00d0
+ 00498e4c bytes 683e00f0
- 00498b30 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00498b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00498b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00498b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00498e50 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 00498e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00498e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00498e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00498b30 bytes 08610291
+ 00498e50 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daea46d8a7bf5f62ebb270b128516576"></a>

### [`00498b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b3c.md) → [`00498e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e5c.md) FUN_00498e5c

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
      "definition_site": "00498e6c",
      "incomplete_value": false,
      "site": "00498e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498b4c",
      "incomplete_value": false,
      "site": "00498b54",
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
            "const:98:8"
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
      "00498e74",
      "DATA",
      [
        "storage",
        "00c66098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498e74",
      "DATA",
      [
        "storage",
        "00c67068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b3c.md#insn-00498b48) · [`00498b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b3c.md#insn-00498b4c) · [`00498b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498b3c.md#insn-00498b58)
- 新版 [`00498e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e5c.md#insn-00498e68) · [`00498e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e5c.md#insn-00498e6c) · [`00498e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498e5c.md#insn-00498e78)

~~~diff
- 00498b48 ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00498e68 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 00498b48 bytes 683e00d0
+ 00498e68 bytes 683e00f0
- 00498b4c ["COPY", "tmp:0:8", ["const:98:8"]]
- 00498b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00498b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00498b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00498e6c ["COPY", "tmp:0:8", ["const:68:8"]]
+ 00498e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00498e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00498e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00498b4c bytes 08610291
+ 00498e6c bytes 08a10191
- 00498b58 ["INT_ADD", "register:40f0:8", ["const:498b58:8", "const:4:8"]]
- 00498b58 ["CALL", null, ["callee:00c58f40:8"]]
+ 00498e78 ["INT_ADD", "register:40f0:8", ["const:498e78:8", "const:4:8"]]
+ 00498e78 ["CALL", null, ["callee:00c58f40:8"]]
- 00498b58 bytes 06fd1e94
+ 00498e78 bytes 32001f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af89bb2b6af6f29a2db2897f0b18594"></a>

### [`00498d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md) → [`0049905c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md) FUN_0049905c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00497e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497e34.md) · 呼出先 15件 [`00499310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499310.md) [`004994b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/004994b0.md) [`00499780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499780.md) [`00499784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499784.md) [`00597690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597690.md)
- 新版 呼出元 1件 [`00498154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498154.md) · 呼出先 15件 [`00499630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499630.md) [`004997d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/004997d0.md) [`00499aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499aa0.md) [`00499aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499aa4.md) [`005979b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.54% / 新版 96.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004992c4",
      "incomplete_value": false,
      "site": "004992c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498fa4",
      "incomplete_value": false,
      "site": "00498fa4",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004990b0",
      "incomplete_value": false,
      "site": "004990b4",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498d90",
      "incomplete_value": false,
      "site": "00498d94",
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
            "const:6a3:8"
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
      "definition_site": "00499364",
      "incomplete_value": false,
      "site": "00499368",
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
            "const:165:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499044",
      "incomplete_value": false,
      "site": "00499048",
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
            "const:96:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004990b0",
      "PARAM",
      [
        "storage",
        "002ae6a3",
        null,
        "string"
      ]
    ],
    [
      "004992a8",
      "PARAM",
      [
        "storage",
        "002ba013",
        null,
        "string"
      ]
    ],
    [
      "004992c4",
      "DATA",
      [
        "storage",
        "00c66168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004990b0",
      "PARAM",
      [
        "storage",
        "002ae770",
        null,
        "string"
      ]
    ],
    [
      "004992a8",
      "PARAM",
      [
        "storage",
        "002ba0f1",
        null,
        "string"
      ]
    ],
    [
      "004992c4",
      "DATA",
      [
        "storage",
        "00c67138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md#insn-00498d94) · [`00499048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md#insn-00499048) · [`00498d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498d3c.md#insn-00498d74)
- 新版 [`004990b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md#insn-004990b4) · [`00499368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md#insn-00499368) · [`00499094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049905c.md#insn-00499094)

~~~diff
- 00498d94 ["INT_ADD", "register:40f0:8", ["const:498d94:8", "const:4:8"]]
- 00498d94 ["CALL", null, ["callee:00c59510:8"]]
+ 004990b4 ["INT_ADD", "register:40f0:8", ["const:4990b4:8", "const:4:8"]]
+ 004990b4 ["CALL", null, ["callee:00c59510:8"]]
- 00498d94 bytes ebfd1e94
+ 004990b4 bytes 17011f94
- 00499048 ["INT_ADD", "register:40f0:8", ["const:499048:8", "const:4:8"]]
- 00499048 ["CALL", null, ["callee:00c59510:8"]]
+ 00499368 ["INT_ADD", "register:40f0:8", ["const:499368:8", "const:4:8"]]
+ 00499368 ["CALL", null, ["callee:00c59510:8"]]
- 00499048 bytes 3efd1e94
+ 00499368 bytes 6a001f94
- 00498d74 ["INT_ADD", "register:40f0:8", ["const:498d74:8", "const:4:8"]]
- 00498d74 ["CALL", null, ["callee:00c591d0:8"]]
+ 00499094 ["INT_ADD", "register:40f0:8", ["const:499094:8", "const:4:8"]]
+ 00499094 ["CALL", null, ["callee:00c591d0:8"]]
- 00498d74 bytes 23fd1e94
+ 00499094 bytes 4f001f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78bc072a2d913cc9faaed1b05d7294c4"></a>

### [`0049961c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049961c.md) → [`0049993c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049993c.md) FUN_0049993c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00499960",
      "incomplete_value": false,
      "site": "00499964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499640",
      "incomplete_value": false,
      "site": "00499644",
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
            "const:e8:8"
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
      "00499964",
      "DATA",
      [
        "storage",
        "00c660e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499964",
      "DATA",
      [
        "storage",
        "00c670b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049961c.md#insn-00499630) · [`0049963c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049961c.md#insn-0049963c) · [`00499640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049961c.md#insn-00499640)
- 新版 [`00499950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049993c.md#insn-00499950) · [`0049995c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049993c.md#insn-0049995c) · [`00499960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049993c.md#insn-00499960)

~~~diff
- 00499630 ["INT_ADD", "register:40f0:8", ["const:499630:8", "const:4:8"]]
- 00499630 ["CALL", null, ["callee:00c58f30:8"]]
+ 00499950 ["INT_ADD", "register:40f0:8", ["const:499950:8", "const:4:8"]]
+ 00499950 ["CALL", null, ["callee:00c58f30:8"]]
- 00499630 bytes 4cfa1e94
+ 00499950 bytes 78fd1e94
- 0049963c ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 0049995c ["COPY", "register:4040:8", ["const:c67000:8"]]
- 0049963c bytes 683e00b0
+ 0049995c bytes 683e00d0
- 00499640 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00499640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00499640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00499640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499960 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 00499960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00499640 bytes 08a10391
+ 00499960 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb465ed5c62112abf86701187f0b888e"></a>

### [`0049965c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049965c.md) → [`0049997c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049997c.md) FUN_0049997c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00499980",
      "incomplete_value": false,
      "site": "00499984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499660",
      "incomplete_value": false,
      "site": "00499664",
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
            "const:e8:8"
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
      "00499984",
      "DATA",
      [
        "storage",
        "00c660e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499984",
      "DATA",
      [
        "storage",
        "00c670b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049965c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049965c.md#insn-0049965c) · [`00499660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/0049965c.md#insn-00499660)
- 新版 [`0049997c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049997c.md#insn-0049997c) · [`00499980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/0049997c.md#insn-00499980)

~~~diff
- 0049965c ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 0049997c ["COPY", "register:4040:8", ["const:c67000:8"]]
- 0049965c bytes 683e00b0
+ 0049997c bytes 683e00d0
- 00499660 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00499660 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00499660 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00499660 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499980 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 00499980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00499660 bytes 08a10391
+ 00499980 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f452e7ad91cb0c11a090f9dddf4d8178"></a>

### [`00499730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499730.md) → [`00499a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a50.md) FUN_00499a50

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00499a70",
      "incomplete_value": false,
      "site": "00499a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499750",
      "incomplete_value": false,
      "site": "00499754",
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
            "const:168:8"
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
      "00499a74",
      "DATA",
      [
        "storage",
        "00c66168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499a74",
      "DATA",
      [
        "storage",
        "00c67138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499730.md#insn-00499744) · [`0049974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499730.md#insn-0049974c) · [`00499750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499730.md#insn-00499750)
- 新版 [`00499a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a50.md#insn-00499a64) · [`00499a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a50.md#insn-00499a6c) · [`00499a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a50.md#insn-00499a70)

~~~diff
- 00499744 ["INT_ADD", "register:40f0:8", ["const:499744:8", "const:4:8"]]
- 00499744 ["CALL", null, ["callee:00c58f30:8"]]
+ 00499a64 ["INT_ADD", "register:40f0:8", ["const:499a64:8", "const:4:8"]]
+ 00499a64 ["CALL", null, ["callee:00c58f30:8"]]
- 00499744 bytes 07fa1e94
+ 00499a64 bytes 33fd1e94
- 0049974c ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00499a6c ["COPY", "register:4040:8", ["const:c67000:8"]]
- 0049974c bytes 683e00b0
+ 00499a6c bytes 683e00d0
- 00499750 ["COPY", "tmp:0:8", ["const:168:8"]]
- 00499750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00499750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00499750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499a70 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00499a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00499750 bytes 08a10591
+ 00499a70 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50213136a789f012c6f94877d0b1b0b0"></a>

### [`00499768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499768.md) → [`00499a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a88.md) FUN_00499a88

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00499a8c",
      "incomplete_value": false,
      "site": "00499a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049976c",
      "incomplete_value": false,
      "site": "00499770",
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
            "const:168:8"
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
      "00499a90",
      "DATA",
      [
        "storage",
        "00c66168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499a90",
      "DATA",
      [
        "storage",
        "00c67138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499768.md#insn-00499768) · [`0049976c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00499/00499768.md#insn-0049976c)
- 新版 [`00499a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a88.md#insn-00499a88) · [`00499a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00499/00499a88.md#insn-00499a8c)

~~~diff
- 00499768 ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00499a88 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 00499768 bytes 683e00b0
+ 00499a88 bytes 683e00d0
- 0049976c ["COPY", "tmp:0:8", ["const:168:8"]]
- 0049976c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049976c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049976c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499a8c ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00499a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049976c bytes 08a10591
+ 00499a8c bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff9570f889748d0ad9bdf3b7eeb4349c"></a>

### [`0049ac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac44.md) → [`0049af64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af64.md) FUN_0049af64

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "0049af70",
      "incomplete_value": false,
      "site": "0049af74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ac50",
      "incomplete_value": false,
      "site": "0049ac54",
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
            "const:1e8:8"
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
      "0049af74",
      "DATA",
      [
        "storage",
        "00c661e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049af74",
      "DATA",
      [
        "storage",
        "00c671b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ac4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac44.md#insn-0049ac4c) · [`0049ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac44.md#insn-0049ac50)
- 新版 [`0049af6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af64.md#insn-0049af6c) · [`0049af70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af64.md#insn-0049af70)

~~~diff
- 0049ac4c ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 0049af6c ["COPY", "register:4048:8", ["const:c67000:8"]]
- 0049ac4c bytes 693e0090
+ 0049af6c bytes 693e00b0
- 0049ac50 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0049ac50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049af70 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0049af70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049af70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049af70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049ac50 bytes 29a10791
+ 0049af70 bytes 29e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4b766d582b3d4afeb9eba21526bd3f0"></a>

### [`0049ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac64.md) → [`0049af84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af84.md) FUN_0049af84

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049af8c",
      "incomplete_value": false,
      "site": "0049af90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ac6c",
      "incomplete_value": false,
      "site": "0049ac70",
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
            "const:1e8:8"
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
      "0049af90",
      "DATA",
      [
        "storage",
        "00c661e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049af90",
      "DATA",
      [
        "storage",
        "00c671b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ac68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac64.md#insn-0049ac68) · [`0049ac6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac64.md#insn-0049ac6c) · [`0049ac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ac64.md#insn-0049ac8c)
- 新版 [`0049af88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af84.md#insn-0049af88) · [`0049af8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af84.md#insn-0049af8c) · [`0049afac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049af84.md#insn-0049afac)

~~~diff
- 0049ac68 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 0049af88 ["COPY", "register:4048:8", ["const:c67000:8"]]
- 0049ac68 bytes 693e0090
+ 0049af88 bytes 693e00b0
- 0049ac6c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0049ac6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049af8c ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0049af8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049af8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049af8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049ac6c bytes 29a10791
+ 0049af8c bytes 29e10691
- 0049ac8c ["INT_ADD", "register:40f0:8", ["const:49ac8c:8", "const:4:8"]]
- 0049ac8c ["CALL", null, ["callee:00c58f20:8"]]
+ 0049afac ["INT_ADD", "register:40f0:8", ["const:49afac:8", "const:4:8"]]
+ 0049afac ["CALL", null, ["callee:00c58f20:8"]]
- 0049ac8c bytes b1f41e94
+ 0049afac bytes ddf71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b47686995da8ef27b3857bec9232d9c5"></a>

### [`0049aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aca0.md) → [`0049afc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049afc0.md) FUN_0049afc0

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
      "definition_site": "0049afe4",
      "incomplete_value": false,
      "site": "0049afe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049acc4",
      "incomplete_value": false,
      "site": "0049acc4",
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
            "const:1e8:8"
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
      "0049afe4",
      "DATA",
      [
        "storage",
        "00c661e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049afe4",
      "DATA",
      [
        "storage",
        "00c671b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aca0.md#insn-0049acb4) · [`0049acbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aca0.md#insn-0049acbc) · [`0049acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049aca0.md#insn-0049acc0)
- 新版 [`0049afd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049afc0.md#insn-0049afd4) · [`0049afdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049afc0.md#insn-0049afdc) · [`0049afe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049a/0049afc0.md#insn-0049afe0)

~~~diff
- 0049acb4 ["INT_ADD", "register:40f0:8", ["const:49acb4:8", "const:4:8"]]
- 0049acb4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049afd4 ["INT_ADD", "register:40f0:8", ["const:49afd4:8", "const:4:8"]]
+ 0049afd4 ["CALL", null, ["callee:00c58f30:8"]]
- 0049acb4 bytes abf41e94
+ 0049afd4 bytes d7f71e94
- 0049acbc ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 0049afdc ["COPY", "register:4048:8", ["const:c67000:8"]]
- 0049acbc bytes 693e0090
+ 0049afdc bytes 693e00b0
- 0049acc0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0049acc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049acc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049acc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049afe0 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0049afe0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049afe0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049afe0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049acc0 bytes 29a10791
+ 0049afe0 bytes 29e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62bc53f1008bb29709ab7c326cac0826"></a>

### [`0049acf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049acf0.md) → [`0049b010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b010.md) FUN_0049b010

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
      "definition_site": "0049b01c",
      "incomplete_value": false,
      "site": "0049b01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049acfc",
      "incomplete_value": false,
      "site": "0049acfc",
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
            "const:1e8:8"
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
      "0049b01c",
      "DATA",
      [
        "storage",
        "00c661e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049b01c",
      "DATA",
      [
        "storage",
        "00c671b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049acf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049acf0.md#insn-0049acf4) · [`0049acf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049acf0.md#insn-0049acf8) · [`0049ad18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049acf0.md#insn-0049ad18)
- 新版 [`0049b014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b010.md#insn-0049b014) · [`0049b018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b010.md#insn-0049b018) · [`0049b038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b010.md#insn-0049b038)

~~~diff
- 0049acf4 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 0049b014 ["COPY", "register:4048:8", ["const:c67000:8"]]
- 0049acf4 bytes 693e0090
+ 0049b014 bytes 693e0090
- 0049acf8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0049acf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049acf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049acf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049b018 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0049b018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049b018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049b018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049acf8 bytes 29a10791
+ 0049b018 bytes 29e10691
- 0049ad18 ["INT_ADD", "register:40f0:8", ["const:49ad18:8", "const:4:8"]]
- 0049ad18 ["CALL", null, ["callee:00c54d60:8"]]
+ 0049b038 ["INT_ADD", "register:40f0:8", ["const:49b038:8", "const:4:8"]]
+ 0049b038 ["CALL", null, ["callee:00c54d60:8"]]
- 0049ad18 bytes 16e41e94
+ 0049b038 bytes 4ae71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-312d66ff1c3df653e3d3ecc79b2175d5"></a>

### [`0049ae6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ae6c.md) → [`0049b18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b18c.md) _INIT_24

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b1c8",
      "incomplete_value": true,
      "site": "0049b1e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049aea8",
      "incomplete_value": true,
      "site": "0049aec4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049b1ec",
      "incomplete_value": true,
      "site": "0049b208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049aecc",
      "incomplete_value": true,
      "site": "0049aee8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049b20c",
      "incomplete_value": true,
      "site": "0049b228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0049aeec",
      "incomplete_value": true,
      "site": "0049af08",
      "value": [
        "LOAD",
        "16",
        [
          [
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049b1c8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0049b1ec",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0049b20c",
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
      "0049b1c8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0049b1ec",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0049b20c",
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


#### 変更候補の命令位置

- 旧版 [`0049afcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ae6c.md#insn-0049afcc) · [`0049b0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ae6c.md#insn-0049b0a0) · [`0049ae94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049a/0049ae6c.md#insn-0049ae94)
- 新版 [`0049b2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b18c.md#insn-0049b2ec) · [`0049b3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b18c.md#insn-0049b3c0) · [`0049b1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b18c.md#insn-0049b1b4)

~~~diff
- 0049afcc ["INT_ADD", "register:40f0:8", ["const:49afcc:8", "const:4:8"]]
- 0049afcc ["CALL", null, ["callee:0043bb58:8"]]
+ 0049b2ec ["INT_ADD", "register:40f0:8", ["const:49b2ec:8", "const:4:8"]]
+ 0049b2ec ["CALL", null, ["callee:0043bb58:8"]]
- 0049afcc bytes 1b82fe97
+ 0049b2ec bytes 1b82fe97
- 0049b0a0 ["INT_ADD", "register:40f0:8", ["const:49b0a0:8", "const:4:8"]]
- 0049b0a0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0049b3c0 ["INT_ADD", "register:40f0:8", ["const:49b3c0:8", "const:4:8"]]
+ 0049b3c0 ["CALL", null, ["callee:00c58ed0:8"]]
- 0049b0a0 bytes 98f31e94
+ 0049b3c0 bytes c4f61e94
- 0049ae94 ["COPY", "register:4098:8", ["const:ca5000:8"]]
+ 0049b1b4 ["COPY", "register:4098:8", ["const:ca6000:8"]]
- 0049ae94 bytes 534000f0
+ 0049b1b4 bytes 534000f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93101f30abca9a351e759489fc8f25e5"></a>

### [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) → [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) FUN_0049b51c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0044673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044673c.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00446a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446a5c.md) · 呼出先 11件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b58c",
      "incomplete_value": true,
      "site": "0049b598",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b26c",
      "incomplete_value": true,
      "site": "0049b278",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
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
      "definition_site": "0049b588",
      "incomplete_value": true,
      "site": "0049b59c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b268",
      "incomplete_value": true,
      "site": "0049b27c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fd7:8"
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
      "definition_site": "0049b588",
      "incomplete_value": true,
      "site": "0049b59c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0049b268",
      "incomplete_value": true,
      "site": "0049b27c",
      "value": [
        "LOAD",
        "16",
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
      "0049b588",
      "READ",
      [
        "storage",
        "002c0fd7",
        null,
        "string"
      ]
    ],
    [
      "0049b588",
      "READ",
      [
        "storage",
        "002c0fe7",
        null,
        "string"
      ]
    ],
    [
      "0049b58c",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049b588",
      "READ",
      [
        "storage",
        "002c1021",
        null,
        "string"
      ]
    ],
    [
      "0049b588",
      "READ",
      [
        "storage",
        "002c1031",
        null,
        "string"
      ]
    ],
    [
      "0049b58c",
      "READ",
      [
        "storage",
        "002c23f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md#insn-0049b228) · [`0049b230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md#insn-0049b230) · [`0049b258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md#insn-0049b258)
- 新版 [`0049b548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md#insn-0049b548) · [`0049b550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md#insn-0049b550) · [`0049b578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md#insn-0049b578)

~~~diff
- 0049b228 ["INT_ADD", "register:40f0:8", ["const:49b228:8", "const:4:8"]]
- 0049b228 ["CALL", null, ["callee:005891cc:8"]]
+ 0049b548 ["INT_ADD", "register:40f0:8", ["const:49b548:8", "const:4:8"]]
+ 0049b548 ["CALL", null, ["callee:005891cc:8"]]
- 0049b228 bytes 21b70394
+ 0049b548 bytes 21b70394
- 0049b230 ["INT_ADD", "register:40f0:8", ["const:49b230:8", "const:4:8"]]
- 0049b230 ["CALL", null, ["callee:005894bc:8"]]
+ 0049b550 ["INT_ADD", "register:40f0:8", ["const:49b550:8", "const:4:8"]]
+ 0049b550 ["CALL", null, ["callee:005894bc:8"]]
- 0049b230 bytes dbb70394
+ 0049b550 bytes dbb70394
- 0049b258 ["INT_ADD", "register:40f0:8", ["const:49b258:8", "const:4:8"]]
- 0049b258 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049b578 ["INT_ADD", "register:40f0:8", ["const:49b578:8", "const:4:8"]]
+ 0049b578 ["CALL", null, ["callee:00c58f30:8"]]
- 0049b258 bytes 42f31e94
+ 0049b578 bytes 6ef61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04c5bfb51567981c68cd6bcc3b4fdfe"></a>

### [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) → [`0049b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md) FUN_0049b800

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) [`0049fb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md) [`0049fca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md) [`0049fe10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fe10.md) · 呼出先 4件 [`0047d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5f4.md) [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 4件 [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) [`0049fe50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fe50.md) [`0049ffc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049ffc8.md) [`004a0130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a0130.md) · 呼出先 4件 [`0047d914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d914.md) [`0047da18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047da18.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b8f4",
      "incomplete_value": false,
      "site": "0049b8fc",
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
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b5d4",
      "incomplete_value": false,
      "site": "0049b5dc",
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
            "const:a82:8"
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
      "definition_site": "0049b904",
      "incomplete_value": true,
      "site": "0049b908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b5e4",
      "incomplete_value": true,
      "site": "0049b5e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049b8fc",
      "DATA",
      [
        "storage",
        "002a8a82",
        null,
        "string"
      ]
    ],
    [
      "0049b904",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049b904",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049b8fc",
      "DATA",
      [
        "storage",
        "002a8bda",
        null,
        "string"
      ]
    ],
    [
      "0049b904",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049b904",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md#insn-0049b5e8) · [`0049b574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md#insn-0049b574) · [`0049b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md#insn-0049b5c4)
- 新版 [`0049b908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md#insn-0049b908) · [`0049b894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md#insn-0049b894) · [`0049b8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md#insn-0049b8e4)

~~~diff
- 0049b5e8 ["INT_ADD", "register:40f0:8", ["const:49b5e8:8", "const:4:8"]]
- 0049b5e8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049b908 ["INT_ADD", "register:40f0:8", ["const:49b908:8", "const:4:8"]]
+ 0049b908 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049b5e8 bytes 7ef21e94
+ 0049b908 bytes aaf51e94
- 0049b574 ["INT_ADD", "register:40f0:8", ["const:49b574:8", "const:4:8"]]
- 0049b574 ["CALL", null, ["callee:0047d914:8"]]
+ 0049b894 ["INT_ADD", "register:40f0:8", ["const:49b894:8", "const:4:8"]]
+ 0049b894 ["CALL", null, ["callee:0047d914:8"]]
- 0049b574 bytes 2088ff97
+ 0049b894 bytes 2088ff97
- 0049b5c4 ["INT_ADD", "register:40f0:8", ["const:49b5c4:8", "const:4:8"]]
- 0049b5c4 ["CALL", null, ["callee:0047da18:8"]]
+ 0049b8e4 ["INT_ADD", "register:40f0:8", ["const:49b8e4:8", "const:4:8"]]
+ 0049b8e4 ["CALL", null, ["callee:0047da18:8"]]
- 0049b5c4 bytes 4d88ff97
+ 0049b8e4 bytes 4d88ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d9c6f14e925e3a4b65f367ecec19d00"></a>

### [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) → [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) FUN_0049b9ec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0049b5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b5ec.md) · 呼出先 15件 [`0049b408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b414.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) [`0049ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ece4.md)
- 新版 呼出元 1件 [`0049b90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b90c.md) · 呼出先 15件 [`0049b728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b728.md) [`0049b734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b734.md) [`0049b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md) [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) [`0049f004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f004.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.22% / 新版 95.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049bea4",
      "incomplete_value": false,
      "site": "0049bea8",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bb84",
      "incomplete_value": false,
      "site": "0049bb88",
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
            "const:a95:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049be68",
      "incomplete_value": true,
      "site": "0049be6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bb48",
      "incomplete_value": true,
      "site": "0049bb4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "definition_site": "0049bec8",
      "incomplete_value": true,
      "site": "0049becc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bba8",
      "incomplete_value": true,
      "site": "0049bbac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "0049bbdc",
      "DATA",
      [
        "storage",
        "002ca71d",
        null,
        null
      ]
    ],
    [
      "0049bbe0",
      "DATA",
      [
        "storage",
        "002ca679",
        null,
        null
      ]
    ],
    [
      "0049bbe8",
      "DATA",
      [
        "storage",
        "002ca6a2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049bbdc",
      "DATA",
      [
        "storage",
        "002ca76d",
        null,
        null
      ]
    ],
    [
      "0049bbe0",
      "DATA",
      [
        "storage",
        "002ca6c9",
        null,
        null
      ]
    ],
    [
      "0049bbe8",
      "DATA",
      [
        "storage",
        "002ca6f2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md#insn-0049bb4c) · [`0049bbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md#insn-0049bbac)
- 新版 [`0049be6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md#insn-0049be6c) · [`0049bb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md#insn-0049bb88) · [`0049becc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md#insn-0049becc)

~~~diff
- 0049bb4c ["INT_ADD", "register:40f0:8", ["const:49bb4c:8", "const:4:8"]]
- 0049bb4c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049be6c ["INT_ADD", "register:40f0:8", ["const:49be6c:8", "const:4:8"]]
+ 0049be6c ["CALL", null, ["callee:00c58fb0:8"]]
- 0049bb4c bytes 25f11e94
+ 0049be6c bytes 51f41e94
+ 0049bb88 ["COPY", "register:4088:8", ["const:2ca000:8"]]
+ 0049bb88 bytes 71f1fff0
- 0049bbac ["INT_ADD", "register:40f0:8", ["const:49bbac:8", "const:4:8"]]
- 0049bbac ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049becc ["INT_ADD", "register:40f0:8", ["const:49becc:8", "const:4:8"]]
+ 0049becc ["CALL", null, ["callee:00c58fb0:8"]]
- 0049bbac bytes 0df11e94
+ 0049becc bytes 39f41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a0792cb620feda6fdaf8b2a6d1ae0d0"></a>

### [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) → [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) FUN_0049bfbc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 15件 [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) [`0049cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) [`0049ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md)
- 新版 呼出元 1件 [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) · 呼出先 15件 [`0047da18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047da18.md) [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) [`0049ce3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md) [`0049d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049c290",
      "incomplete_value": false,
      "site": "0049c294",
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
            "const:bda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bf70",
      "incomplete_value": false,
      "site": "0049bf74",
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
            "const:a82:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049c2b4",
      "incomplete_value": true,
      "site": "0049c2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bf94",
      "incomplete_value": true,
      "site": "0049bf98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "0049c294",
      "DATA",
      [
        "storage",
        "002a8a82",
        null,
        "string"
      ]
    ],
    [
      "0049c2b4",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049c2b4",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049c294",
      "DATA",
      [
        "storage",
        "002a8bda",
        null,
        "string"
      ]
    ],
    [
      "0049c2b4",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049c2b4",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md#insn-0049bf98) · [`0049bd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md#insn-0049bd1c) · [`0049bd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md#insn-0049bd54)
- 新版 [`0049c2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md#insn-0049c2b8) · [`0049c03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md#insn-0049c03c) · [`0049c074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md#insn-0049c074)

~~~diff
- 0049bf98 ["INT_ADD", "register:40f0:8", ["const:49bf98:8", "const:4:8"]]
- 0049bf98 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049c2b8 ["INT_ADD", "register:40f0:8", ["const:49c2b8:8", "const:4:8"]]
+ 0049c2b8 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049bf98 bytes 12f01e94
+ 0049c2b8 bytes 3ef31e94
- 0049bd1c ["INT_ADD", "register:40f0:8", ["const:49bd1c:8", "const:4:8"]]
- 0049bd1c ["CALL", null, ["callee:00c58f30:8"]]
+ 0049c03c ["INT_ADD", "register:40f0:8", ["const:49c03c:8", "const:4:8"]]
+ 0049c03c ["CALL", null, ["callee:00c58f30:8"]]
- 0049bd1c bytes 91f01e94
+ 0049c03c bytes bdf31e94
- 0049bd54 ["INT_ADD", "register:40f0:8", ["const:49bd54:8", "const:4:8"]]
- 0049bd54 ["CALL", null, ["callee:00c59130:8"]]
+ 0049c074 ["INT_ADD", "register:40f0:8", ["const:49c074:8", "const:4:8"]]
+ 0049c074 ["CALL", null, ["callee:00c59130:8"]]
- 0049bd54 bytes 03f11e94
+ 0049c074 bytes 2ff41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18950f1bfa63775263448bc8a8897efb"></a>

### [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) → [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) FUN_0049c6d8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 14件 [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) [`0049e944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0049f480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md) [`0049f76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md)
- 新版 呼出元 1件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) · 呼出先 14件 [`0049dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md) [`0049ec64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0049f7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f7a0.md) [`0049fa8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fa8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049cd54",
      "incomplete_value": false,
      "site": "0049cd58",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ca34",
      "incomplete_value": false,
      "site": "0049ca38",
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
            "const:a95:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049cd40",
      "incomplete_value": true,
      "site": "0049cd44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ca20",
      "incomplete_value": true,
      "site": "0049ca24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "definition_site": "0049cd78",
      "incomplete_value": true,
      "site": "0049cd7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ca58",
      "incomplete_value": true,
      "site": "0049ca5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049cd34",
      "DATA",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ],
    [
      "0049cd34",
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      "0049cd40",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049cd34",
      "DATA",
      [
        "storage",
        "002a654a",
        null,
        "string"
      ]
    ],
    [
      "0049cd34",
      "DATA",
      [
        "storage",
        "002b29f8",
        null,
        "string"
      ]
    ],
    [
      "0049cd40",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ca24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md#insn-0049ca24) · [`0049ca5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md#insn-0049ca5c) · [`0049c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md#insn-0049c478)
- 新版 [`0049cd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md#insn-0049cd44) · [`0049cd7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md#insn-0049cd7c) · [`0049c798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md#insn-0049c798)

~~~diff
- 0049ca24 ["INT_ADD", "register:40f0:8", ["const:49ca24:8", "const:4:8"]]
- 0049ca24 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049cd44 ["INT_ADD", "register:40f0:8", ["const:49cd44:8", "const:4:8"]]
+ 0049cd44 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049ca24 bytes 6fed1e94
+ 0049cd44 bytes 9bf01e94
- 0049ca5c ["INT_ADD", "register:40f0:8", ["const:49ca5c:8", "const:4:8"]]
- 0049ca5c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049cd7c ["INT_ADD", "register:40f0:8", ["const:49cd7c:8", "const:4:8"]]
+ 0049cd7c ["CALL", null, ["callee:00c58fb0:8"]]
- 0049ca5c bytes 61ed1e94
+ 0049cd7c bytes 8df01e94
- 0049c478 ["COPY", "tmp:0:8", ["const:6f4:8"]]
- 0049c478 ["INT_CARRY", "register:105:1", ["register:4078:8", "tmp:0:8"]]
- 0049c478 ["INT_SCARRY", "register:106:1", ["register:4078:8", "tmp:0:8"]]
- 0049c478 ["INT_ADD", "tmp:1:8", ["register:4078:8", "tmp:0:8"]]
+ 0049c798 ["COPY", "tmp:0:8", ["const:744:8"]]
+ 0049c798 ["INT_CARRY", "register:105:1", ["register:4078:8", "tmp:0:8"]]
+ 0049c798 ["INT_SCARRY", "register:106:1", ["register:4078:8", "tmp:0:8"]]
+ 0049c798 ["INT_ADD", "tmp:1:8", ["register:4078:8", "tmp:0:8"]]
- 0049c478 bytes efd11b91
+ 0049c798 bytes ef111d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9179ffd80bc98807fc82eeebb90a87f1"></a>

### [`0049cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) → [`0049ce3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md) FUN_0049ce3c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 5件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md) [`0049f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) · 呼出先 5件 [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md) [`0049fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d178",
      "incomplete_value": true,
      "site": "0049d17c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ce58",
      "incomplete_value": true,
      "site": "0049ce5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "0049d16c",
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      "0049d16c",
      "DATA",
      [
        "storage",
        "002a8a95",
        null,
        "string"
      ]
    ],
    [
      "0049d16c",
      "DATA",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049d16c",
      "DATA",
      [
        "storage",
        "002b29f8",
        null,
        "string"
      ]
    ],
    [
      "0049d16c",
      "DATA",
      [
        "storage",
        "002a8bed",
        null,
        "string"
      ]
    ],
    [
      "0049d16c",
      "DATA",
      [
        "storage",
        "002a654a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ce5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md#insn-0049ce5c) · [`0049cdc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md#insn-0049cdc0) · [`0049ce00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md#insn-0049ce00)
- 新版 [`0049d17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md#insn-0049d17c) · [`0049d0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md#insn-0049d0e0) · [`0049d120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md#insn-0049d120)

~~~diff
- 0049ce5c ["INT_ADD", "register:40f0:8", ["const:49ce5c:8", "const:4:8"]]
- 0049ce5c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049d17c ["INT_ADD", "register:40f0:8", ["const:49d17c:8", "const:4:8"]]
+ 0049d17c ["CALL", null, ["callee:00c58fb0:8"]]
- 0049ce5c bytes 61ec1e94
+ 0049d17c bytes 8def1e94
- 0049cdc0 ["INT_ADD", "register:40f0:8", ["const:49cdc0:8", "const:4:8"]]
- 0049cdc0 ["CALL", null, ["callee:0049f778:8"]]
+ 0049d0e0 ["INT_ADD", "register:40f0:8", ["const:49d0e0:8", "const:4:8"]]
+ 0049d0e0 ["CALL", null, ["callee:0049f778:8"]]
- 0049cdc0 bytes a6090094
+ 0049d0e0 bytes a6090094
- 0049ce00 ["INT_ADD", "register:40f0:8", ["const:49ce00:8", "const:4:8"]]
- 0049ce00 ["CALL", null, ["callee:0049f764:8"]]
+ 0049d120 ["INT_ADD", "register:40f0:8", ["const:49d120:8", "const:4:8"]]
+ 0049d120 ["CALL", null, ["callee:0049f764:8"]]
- 0049ce00 bytes 91090094
+ 0049d120 bytes 91090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fb997b63d5902082b9248e5b432c269"></a>

### [`0049ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md) → [`0049d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md) FUN_0049d180

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) · 呼出先 5件 [`0049d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md) [`0049dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md) [`0049df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0049bfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049bfbc.md) · 呼出先 5件 [`0049d824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md) [`0049e034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md) [`0049e2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d3d0",
      "incomplete_value": false,
      "site": "0049d3d8",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d0b0",
      "incomplete_value": false,
      "site": "0049d0b8",
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
            "const:a95:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d3e0",
      "incomplete_value": true,
      "site": "0049d3e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d0c0",
      "incomplete_value": true,
      "site": "0049d0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "0049d3d8",
      "DATA",
      [
        "storage",
        "002a8a95",
        null,
        "string"
      ]
    ],
    [
      "0049d3e0",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049d3e0",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d3d8",
      "DATA",
      [
        "storage",
        "002a8bed",
        null,
        "string"
      ]
    ],
    [
      "0049d3e0",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049d3e0",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md#insn-0049d0c4) · [`0049ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md#insn-0049ce94) · [`0049cea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md#insn-0049cea0)
- 新版 [`0049d3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md#insn-0049d3e4) · [`0049d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md#insn-0049d1b4) · [`0049d1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md#insn-0049d1c0)

~~~diff
- 0049d0c4 ["INT_ADD", "register:40f0:8", ["const:49d0c4:8", "const:4:8"]]
- 0049d0c4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049d3e4 ["INT_ADD", "register:40f0:8", ["const:49d3e4:8", "const:4:8"]]
+ 0049d3e4 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049d0c4 bytes c7eb1e94
+ 0049d3e4 bytes f3ee1e94
- 0049ce94 ["INT_ADD", "register:40f0:8", ["const:49ce94:8", "const:4:8"]]
- 0049ce94 ["CALL", null, ["callee:0049d824:8"]]
+ 0049d1b4 ["INT_ADD", "register:40f0:8", ["const:49d1b4:8", "const:4:8"]]
+ 0049d1b4 ["CALL", null, ["callee:0049d824:8"]]
- 0049ce94 bytes 9c010094
+ 0049d1b4 bytes 9c010094
- 0049cea0 ["INT_ADD", "register:40f0:8", ["const:49cea0:8", "const:4:8"]]
- 0049cea0 ["CALL", null, ["callee:0049e034:8"]]
+ 0049d1c0 ["INT_ADD", "register:40f0:8", ["const:49d1c0:8", "const:4:8"]]
+ 0049d1c0 ["CALL", null, ["callee:0049e034:8"]]
- 0049cea0 bytes 9d030094
+ 0049d1c0 bytes 9d030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-915924c261d5e513424f35da1e43cc86"></a>

### [`0049d2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md) → [`0049d5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md) FUN_0049d5d4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) · 呼出先 5件 [`0049e504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md) [`0049e714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e714.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) · 呼出先 5件 [`0049e824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e824.md) [`0049ea34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ea34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d70c",
      "incomplete_value": false,
      "site": "0049d714",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d3ec",
      "incomplete_value": false,
      "site": "0049d3f4",
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
            "const:9ae:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d71c",
      "incomplete_value": true,
      "site": "0049d720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d3fc",
      "incomplete_value": true,
      "site": "0049d400",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049d714",
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      "0049d71c",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049d71c",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d714",
      "DATA",
      [
        "storage",
        "002b29f8",
        null,
        "string"
      ]
    ],
    [
      "0049d71c",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049d71c",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md#insn-0049d400) · [`0049d37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md#insn-0049d37c) · [`0049d3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d2b4.md#insn-0049d3a8)
- 新版 [`0049d720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md#insn-0049d720) · [`0049d69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md#insn-0049d69c) · [`0049d6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d5d4.md#insn-0049d6c8)

~~~diff
- 0049d400 ["INT_ADD", "register:40f0:8", ["const:49d400:8", "const:4:8"]]
- 0049d400 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049d720 ["INT_ADD", "register:40f0:8", ["const:49d720:8", "const:4:8"]]
+ 0049d720 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049d400 bytes f8ea1e94
+ 0049d720 bytes 24ee1e94
- 0049d37c ["INT_ADD", "register:40f0:8", ["const:49d37c:8", "const:4:8"]]
- 0049d37c ["CALL", null, ["callee:0049e824:8"]]
+ 0049d69c ["INT_ADD", "register:40f0:8", ["const:49d69c:8", "const:4:8"]]
+ 0049d69c ["CALL", null, ["callee:0049e824:8"]]
- 0049d37c bytes 62040094
+ 0049d69c bytes 62040094
- 0049d3a8 ["INT_ADD", "register:40f0:8", ["const:49d3a8:8", "const:4:8"]]
- 0049d3a8 ["CALL", null, ["callee:0049ea34:8"]]
+ 0049d6c8 ["INT_ADD", "register:40f0:8", ["const:49d6c8:8", "const:4:8"]]
+ 0049d6c8 ["CALL", null, ["callee:0049ea34:8"]]
- 0049d3a8 bytes db040094
+ 0049d6c8 bytes db040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-786299c5dd7b8a3ee97da19cd6ddba90"></a>

### [`0049d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md) → [`0049d824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md) FUN_0049d824

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) [`0049ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md) · 呼出先 3件 [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) [`0049d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md) · 呼出先 3件 [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049dc00",
      "incomplete_value": false,
      "site": "0049dc08",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d8e0",
      "incomplete_value": false,
      "site": "0049d8e8",
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
            "const:a95:8"
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
      "definition_site": "0049dc10",
      "incomplete_value": true,
      "site": "0049dc14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d8f0",
      "incomplete_value": true,
      "site": "0049d8f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049d860",
      "DATA",
      [
        "storage",
        "002c2da0",
        null,
        null
      ]
    ],
    [
      "0049dc08",
      "DATA",
      [
        "storage",
        "002a8a95",
        null,
        "string"
      ]
    ],
    [
      "0049dc10",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049d860",
      "DATA",
      [
        "storage",
        "002c2df0",
        null,
        null
      ]
    ],
    [
      "0049dc08",
      "DATA",
      [
        "storage",
        "002a8bed",
        null,
        "string"
      ]
    ],
    [
      "0049dc10",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md#insn-0049d8f4) · [`0049d538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md#insn-0049d538) · [`0049d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d504.md#insn-0049d5e0)
- 新版 [`0049dc14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md#insn-0049dc14) · [`0049d858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md#insn-0049d858) · [`0049d900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d824.md#insn-0049d900)

~~~diff
- 0049d8f4 ["INT_ADD", "register:40f0:8", ["const:49d8f4:8", "const:4:8"]]
- 0049d8f4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049dc14 ["INT_ADD", "register:40f0:8", ["const:49dc14:8", "const:4:8"]]
+ 0049dc14 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049d8f4 bytes bbe91e94
+ 0049dc14 bytes e7ec1e94
- 0049d538 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 0049d538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0049d538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0049d538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049d858 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 0049d858 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049d858 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049d858 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0049d538 bytes 4a813691
+ 0049d858 bytes 4ac13791
- 0049d5e0 ["INT_ADD", "register:40f0:8", ["const:49d5e0:8", "const:4:8"]]
- 0049d5e0 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049d900 ["INT_ADD", "register:40f0:8", ["const:49d900:8", "const:4:8"]]
+ 0049d900 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049d5e0 bytes fefeff97
+ 0049d900 bytes fefeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9495dcb926fabb4f4c5bd23b05e36845"></a>

### [`0049d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md) → [`0049dc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dc18.md) FUN_0049dc18

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) · 呼出先 3件 [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) · 呼出先 3件 [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049dd68",
      "incomplete_value": false,
      "site": "0049dd70",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049da48",
      "incomplete_value": false,
      "site": "0049da50",
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
            "const:a95:8"
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
      "definition_site": "0049dd78",
      "incomplete_value": true,
      "site": "0049dd7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049da58",
      "incomplete_value": true,
      "site": "0049da5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049dd70",
      "DATA",
      [
        "storage",
        "002a8a95",
        null,
        "string"
      ]
    ],
    [
      "0049dd78",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049dd78",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049dd70",
      "DATA",
      [
        "storage",
        "002a8bed",
        null,
        "string"
      ]
    ],
    [
      "0049dd78",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049dd78",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049da5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md#insn-0049da5c) · [`0049da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md#insn-0049da00) · [`0049da14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d8f8.md#insn-0049da14)
- 新版 [`0049dd7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dc18.md#insn-0049dd7c) · [`0049dd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dc18.md#insn-0049dd20) · [`0049dd34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dc18.md#insn-0049dd34)

~~~diff
- 0049da5c ["INT_ADD", "register:40f0:8", ["const:49da5c:8", "const:4:8"]]
- 0049da5c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049dd7c ["INT_ADD", "register:40f0:8", ["const:49dd7c:8", "const:4:8"]]
+ 0049dd7c ["CALL", null, ["callee:00c58fb0:8"]]
- 0049da5c bytes 61e91e94
+ 0049dd7c bytes 8dec1e94
- 0049da00 ["INT_ADD", "register:40f0:8", ["const:49da00:8", "const:4:8"]]
- 0049da00 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049dd20 ["INT_ADD", "register:40f0:8", ["const:49dd20:8", "const:4:8"]]
+ 0049dd20 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049da00 bytes f6fdff97
+ 0049dd20 bytes f6fdff97
- 0049da14 ["INT_ADD", "register:40f0:8", ["const:49da14:8", "const:4:8"]]
- 0049da14 ["CALL", null, ["callee:0049d4f8:8"]]
+ 0049dd34 ["INT_ADD", "register:40f0:8", ["const:49dd34:8", "const:4:8"]]
+ 0049dd34 ["CALL", null, ["callee:0049d4f8:8"]]
- 0049da14 bytes f1fdff97
+ 0049dd34 bytes f1fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e429a3fe736e27641dc3cbadb57ef7c0"></a>

### [`0049dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md) → [`0049e034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md) FUN_0049e034

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049ce60.md) · 呼出先 4件 [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0049d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d180.md) · 呼出先 4件 [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049e288",
      "incomplete_value": false,
      "site": "0049e290",
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
            "const:b5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049df68",
      "incomplete_value": false,
      "site": "0049df70",
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
            "const:a8d:8"
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
      "definition_site": "0049e298",
      "incomplete_value": true,
      "site": "0049e29c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049df78",
      "incomplete_value": true,
      "site": "0049df7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "0049e290",
      "DATA",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      "0049e298",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049e298",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049e290",
      "DATA",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "0049e298",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049e298",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049df7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md#insn-0049df7c) · [`0049df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md#insn-0049df40) · [`0049df48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md#insn-0049df48)
- 新版 [`0049e29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md#insn-0049e29c) · [`0049e260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md#insn-0049e260) · [`0049e268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md#insn-0049e268)

~~~diff
- 0049df7c ["INT_ADD", "register:40f0:8", ["const:49df7c:8", "const:4:8"]]
- 0049df7c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049e29c ["INT_ADD", "register:40f0:8", ["const:49e29c:8", "const:4:8"]]
+ 0049e29c ["CALL", null, ["callee:00c58fb0:8"]]
- 0049df7c bytes 19e81e94
+ 0049e29c bytes 45eb1e94
- 0049df40 ["INT_ADD", "register:40f0:8", ["const:49df40:8", "const:4:8"]]
- 0049df40 ["CALL", null, ["callee:0049f764:8"]]
+ 0049e260 ["INT_ADD", "register:40f0:8", ["const:49e260:8", "const:4:8"]]
+ 0049e260 ["CALL", null, ["callee:0049f764:8"]]
- 0049df40 bytes 41050094
+ 0049e260 bytes 41050094
- 0049df48 ["INT_ADD", "register:40f0:8", ["const:49df48:8", "const:4:8"]]
- 0049df48 ["CALL", null, ["callee:0049f778:8"]]
+ 0049e268 ["INT_ADD", "register:40f0:8", ["const:49e268:8", "const:4:8"]]
+ 0049e268 ["CALL", null, ["callee:0049f778:8"]]
- 0049df48 bytes 44050094
+ 0049e268 bytes 44050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84cabd1fe886b9bd0ce51e4d761a8c8d"></a>

### [`0049e944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md) → [`0049ec64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md) FUN_0049ec64

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 8件 [`0049eaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md) [`0049f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) · 呼出先 8件 [`0049ee0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ee0c.md) [`0049fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ed9c",
      "incomplete_value": false,
      "site": "0049eda0",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ea7c",
      "incomplete_value": false,
      "site": "0049ea80",
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
            "const:a95:8"
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
      "definition_site": "0049edc0",
      "incomplete_value": false,
      "site": "0049edc4",
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
            "const:bfd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049eaa0",
      "incomplete_value": false,
      "site": "0049eaa4",
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
            "const:aa5:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049edac",
      "incomplete_value": true,
      "site": "0049edb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ea8c",
      "incomplete_value": true,
      "site": "0049ea90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "0049eda0",
      "DATA",
      [
        "storage",
        "002a8a95",
        null,
        "string"
      ]
    ],
    [
      "0049edac",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049edac",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049eda0",
      "DATA",
      [
        "storage",
        "002a8bed",
        null,
        "string"
      ]
    ],
    [
      "0049edac",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049edac",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md#insn-0049ea90) · [`0049eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md#insn-0049eab4) · [`0049e980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md#insn-0049e980)
- 新版 [`0049edb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md#insn-0049edb0) · [`0049edd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md#insn-0049edd4) · [`0049eca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md#insn-0049eca0)

~~~diff
- 0049ea90 ["INT_ADD", "register:40f0:8", ["const:49ea90:8", "const:4:8"]]
- 0049ea90 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049edb0 ["INT_ADD", "register:40f0:8", ["const:49edb0:8", "const:4:8"]]
+ 0049edb0 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049ea90 bytes 54e51e94
+ 0049edb0 bytes 80e81e94
- 0049eab4 ["INT_ADD", "register:40f0:8", ["const:49eab4:8", "const:4:8"]]
- 0049eab4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049edd4 ["INT_ADD", "register:40f0:8", ["const:49edd4:8", "const:4:8"]]
+ 0049edd4 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049eab4 bytes 4be51e94
+ 0049edd4 bytes 77e81e94
- 0049e980 ["INT_ADD", "register:40f0:8", ["const:49e980:8", "const:4:8"]]
- 0049e980 ["CALL", null, ["callee:00c58f30:8"]]
+ 0049eca0 ["INT_ADD", "register:40f0:8", ["const:49eca0:8", "const:4:8"]]
+ 0049eca0 ["CALL", null, ["callee:00c58f30:8"]]
- 0049e980 bytes 78e51e94
+ 0049eca0 bytes a4e81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8cf1204e558de4bf297424f9a8be045"></a>

### [`0049eaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md) → [`0049ee0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ee0c.md) FUN_0049ee0c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) [`0049e944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md) · 呼出先 2件 [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`0049dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md) [`0049ec64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md) · 呼出先 2件 [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049eee8",
      "incomplete_value": false,
      "site": "0049eef0",
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
            "const:bed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ebc8",
      "incomplete_value": false,
      "site": "0049ebd0",
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
            "const:a95:8"
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
      "definition_site": "0049eef8",
      "incomplete_value": true,
      "site": "0049eefc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ebd8",
      "incomplete_value": true,
      "site": "0049ebdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "0049eef0",
      "DATA",
      [
        "storage",
        "002a8a95",
        null,
        "string"
      ]
    ],
    [
      "0049eef8",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049eef8",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049eef0",
      "DATA",
      [
        "storage",
        "002a8bed",
        null,
        "string"
      ]
    ],
    [
      "0049eef8",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049eef8",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ebdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md#insn-0049ebdc) · [`0049ebc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md#insn-0049ebc0) · [`0049ebc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049eaec.md#insn-0049ebc8)
- 新版 [`0049eefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ee0c.md#insn-0049eefc) · [`0049eee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ee0c.md#insn-0049eee0) · [`0049eee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ee0c.md#insn-0049eee8)

~~~diff
- 0049ebdc ["INT_ADD", "register:40f0:8", ["const:49ebdc:8", "const:4:8"]]
- 0049ebdc ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049eefc ["INT_ADD", "register:40f0:8", ["const:49eefc:8", "const:4:8"]]
+ 0049eefc ["CALL", null, ["callee:00c58fb0:8"]]
- 0049ebdc bytes 01e51e94
+ 0049eefc bytes 2de81e94
- 0049ebc0 ["INT_ADD", "register:40f0:8", ["const:49ebc0:8", "const:4:8"]]
- 0049ebc0 ["CALL", null, ["callee:00c58f90:8"]]
+ 0049eee0 ["INT_ADD", "register:40f0:8", ["const:49eee0:8", "const:4:8"]]
+ 0049eee0 ["CALL", null, ["callee:00c58f90:8"]]
- 0049ebc0 bytes 00e51e94
+ 0049eee0 bytes 2ce81e94
- 0049ebc8 ["COPY", "tmp:0:8", ["const:a95:8"]]
- 0049ebc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049ebc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049ebc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049eee8 ["COPY", "tmp:0:8", ["const:bed:8"]]
+ 0049eee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049eee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049eee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049ebc8 bytes 08552a91
+ 0049eee8 bytes 08b52f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ea2ef9855f83388709172eabbbf71e"></a>

### [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) → [`0049f750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f750.md) FUN_0049f750

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 66件 [`0049c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c064.md) [`005b070c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b070c.md) [`005dd790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005dd/005dd790.md) [`005e2e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e2/005e2e80.md) [`005e7544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7544.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 66件 [`0049c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c384.md) [`005b0abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b0/005b0abc.md) [`005ddb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005dd/005ddb40.md) [`005e3230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e3/005e3230.md) [`005e78f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e7/005e78f4.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0049f75c",
      "incomplete_value": false,
      "site": "0049f760",
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
      "definition_site": "0049f43c",
      "incomplete_value": false,
      "site": "0049f440",
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
      "0049f75c",
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
      "0049f75c",
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

- 旧版 [`0049f440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md#insn-0049f440) · [`0049f438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md#insn-0049f438) · [`0049f43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md#insn-0049f43c)
- 新版 [`0049f760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f750.md#insn-0049f760) · [`0049f758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f750.md#insn-0049f758) · [`0049f75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f750.md#insn-0049f75c)

~~~diff
- 0049f440 ["INT_ADD", "register:40f0:8", ["const:49f440:8", "const:4:8"]]
- 0049f440 ["CALL", null, ["callee:00442c90:8"]]
+ 0049f760 ["INT_ADD", "register:40f0:8", ["const:49f760:8", "const:4:8"]]
+ 0049f760 ["CALL", null, ["callee:00442c90:8"]]
- 0049f440 bytes 4c8dfe97
+ 0049f760 bytes 4c8dfe97
- 0049f438 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049f758 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f438 bytes c0f0ff90
+ 0049f758 bytes c0f0ffb0
- 0049f43c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f43c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f43c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f43c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f75c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049f75c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f75c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f75c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f43c bytes 00303e91
+ 0049f75c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f95077b690974ad1a7e7f20a402b32e"></a>

### [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) → [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) FUN_0049f764

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0049cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) [`0049d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md) [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) [`0049dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md) [`0049df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 5件 [`0049ce3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md) [`0049d460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d460.md) [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md) [`0049e034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md) [`0049e2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0049f770",
      "incomplete_value": false,
      "site": "0049f774",
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
      "definition_site": "0049f450",
      "incomplete_value": false,
      "site": "0049f454",
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
      "0049f770",
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
      "0049f770",
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

- 旧版 [`0049f454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md#insn-0049f454) · [`0049f44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md#insn-0049f44c) · [`0049f450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md#insn-0049f450)
- 新版 [`0049f774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md#insn-0049f774) · [`0049f76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md#insn-0049f76c) · [`0049f770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md#insn-0049f770)

~~~diff
- 0049f454 ["INT_ADD", "register:40f0:8", ["const:49f454:8", "const:4:8"]]
- 0049f454 ["CALL", null, ["callee:00442c90:8"]]
+ 0049f774 ["INT_ADD", "register:40f0:8", ["const:49f774:8", "const:4:8"]]
+ 0049f774 ["CALL", null, ["callee:00442c90:8"]]
- 0049f454 bytes 478dfe97
+ 0049f774 bytes 478dfe97
- 0049f44c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049f76c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f44c bytes c0f0ff90
+ 0049f76c bytes c0f0ffb0
- 0049f450 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f770 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049f770 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f770 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f770 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f450 bytes 00303e91
+ 0049f770 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b1f5a29ffe635882e8ec544ae3c9fa3"></a>

### [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md) → [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md) FUN_0049f778

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0049cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) [`0049d140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d140.md) [`0049d1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049d1d8.md) [`0049dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049dd14.md) [`0049df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049df80.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 5件 [`0049ce3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md) [`0049d460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d460.md) [`0049d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049d4f8.md) [`0049e034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e034.md) [`0049e2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049e2a0.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0049f784",
      "incomplete_value": false,
      "site": "0049f788",
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
      "definition_site": "0049f464",
      "incomplete_value": false,
      "site": "0049f468",
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
      "0049f784",
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
      "0049f784",
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

- 旧版 [`0049f468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md#insn-0049f468) · [`0049f460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md#insn-0049f460) · [`0049f464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md#insn-0049f464)
- 新版 [`0049f788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md#insn-0049f788) · [`0049f780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md#insn-0049f780) · [`0049f784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md#insn-0049f784)

~~~diff
- 0049f468 ["INT_ADD", "register:40f0:8", ["const:49f468:8", "const:4:8"]]
- 0049f468 ["CALL", null, ["callee:00442c90:8"]]
+ 0049f788 ["INT_ADD", "register:40f0:8", ["const:49f788:8", "const:4:8"]]
+ 0049f788 ["CALL", null, ["callee:00442c90:8"]]
- 0049f468 bytes 428dfe97
+ 0049f788 bytes 428dfe97
- 0049f460 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049f780 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f460 bytes c0f0ff90
+ 0049f780 bytes c0f0ffb0
- 0049f464 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f464 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f464 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f464 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f784 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049f784 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f784 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f784 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f464 bytes 00303e91
+ 0049f784 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e246f2910e2be93d8c9d28d49ea27ff"></a>

### [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) → [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) FUN_0049f78c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 77件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) [`0049f480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f480.md) [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) [`004a21e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a21e8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 77件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) [`0049dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md) [`0049f7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f7a0.md) [`004a02b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a02b0.md) [`004a2508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2508.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0049f798",
      "incomplete_value": false,
      "site": "0049f79c",
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
      "definition_site": "0049f478",
      "incomplete_value": false,
      "site": "0049f47c",
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
      "0049f798",
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
      "0049f798",
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

- 旧版 [`0049f47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md#insn-0049f47c) · [`0049f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md#insn-0049f474) · [`0049f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md#insn-0049f478)
- 新版 [`0049f79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md#insn-0049f79c) · [`0049f794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md#insn-0049f794) · [`0049f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md#insn-0049f798)

~~~diff
- 0049f47c ["INT_ADD", "register:40f0:8", ["const:49f47c:8", "const:4:8"]]
- 0049f47c ["CALL", null, ["callee:0043bad8:8"]]
+ 0049f79c ["INT_ADD", "register:40f0:8", ["const:49f79c:8", "const:4:8"]]
+ 0049f79c ["CALL", null, ["callee:0043bad8:8"]]
- 0049f47c bytes cf70fe97
+ 0049f79c bytes cf70fe97
- 0049f474 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049f794 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f474 bytes c0f0ff90
+ 0049f794 bytes c0f0ffb0
- 0049f478 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f798 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049f798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f478 bytes 00303e91
+ 0049f798 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aa966e24c155916004d209af6a80d5e"></a>

### [`0049f8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f8f8.md) → [`0049fc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc18.md) FUN_0049fc18

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049f76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f76c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0049fa8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fa8c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0049fc24",
      "incomplete_value": false,
      "site": "0049fc28",
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
      "definition_site": "0049f904",
      "incomplete_value": false,
      "site": "0049f908",
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
      "0049fc24",
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
      "0049fc24",
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

- 旧版 [`0049f908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f8f8.md#insn-0049f908) · [`0049f900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f8f8.md#insn-0049f900) · [`0049f904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f8f8.md#insn-0049f904)
- 新版 [`0049fc28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc18.md#insn-0049fc28) · [`0049fc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc18.md#insn-0049fc20) · [`0049fc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc18.md#insn-0049fc24)

~~~diff
- 0049f908 ["INT_ADD", "register:40f0:8", ["const:49f908:8", "const:4:8"]]
- 0049f908 ["CALL", null, ["callee:0043bad8:8"]]
+ 0049fc28 ["INT_ADD", "register:40f0:8", ["const:49fc28:8", "const:4:8"]]
+ 0049fc28 ["CALL", null, ["callee:0043bad8:8"]]
- 0049f908 bytes ac6ffe97
+ 0049fc28 bytes ac6ffe97
- 0049f900 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049fc20 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f900 bytes c0f0ff90
+ 0049fc20 bytes c0f0ffb0
- 0049f904 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f904 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f904 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f904 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049fc24 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049fc24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049fc24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049fc24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f904 bytes 00303e91
+ 0049fc24 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc37b6be6a9107d53d0b07771a816a2"></a>

### [`0049f90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f90c.md) → [`0049fc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc2c.md) FUN_0049fc2c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0049fc38",
      "incomplete_value": false,
      "site": "0049fc3c",
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
      "definition_site": "0049f918",
      "incomplete_value": false,
      "site": "0049f91c",
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
      "0049fc38",
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
      "0049fc38",
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

- 旧版 [`0049f91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f90c.md#insn-0049f91c) · [`0049f914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f90c.md#insn-0049f914) · [`0049f918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f90c.md#insn-0049f918)
- 新版 [`0049fc3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc2c.md#insn-0049fc3c) · [`0049fc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc2c.md#insn-0049fc34) · [`0049fc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc2c.md#insn-0049fc38)

~~~diff
- 0049f91c ["INT_ADD", "register:40f0:8", ["const:49f91c:8", "const:4:8"]]
- 0049f91c ["CALL", null, ["callee:00442c90:8"]]
+ 0049fc3c ["INT_ADD", "register:40f0:8", ["const:49fc3c:8", "const:4:8"]]
+ 0049fc3c ["CALL", null, ["callee:00442c90:8"]]
- 0049f91c bytes 158cfe97
+ 0049fc3c bytes 158cfe97
- 0049f914 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049fc34 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f914 bytes c0f0ff90
+ 0049fc34 bytes c0f0ffb0
- 0049f918 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f918 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f918 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f918 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049fc38 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049fc38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049fc38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049fc38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f918 bytes 00303e91
+ 0049fc38 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234eb5cea9859026f8330665446a690e"></a>

### [`0049f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) → [`0049fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md) FUN_0049fc40

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) [`0049cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) [`0049e944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 4件 [`0049c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049c6d8.md) [`0049ce3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049c/0049ce3c.md) [`0049dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049d/0049dd80.md) [`0049ec64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049e/0049ec64.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0049fc4c",
      "incomplete_value": false,
      "site": "0049fc50",
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
      "definition_site": "0049f92c",
      "incomplete_value": false,
      "site": "0049f930",
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
      "0049fc4c",
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
      "0049fc4c",
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

- 旧版 [`0049f930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md#insn-0049f930) · [`0049f928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md#insn-0049f928) · [`0049f92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md#insn-0049f92c)
- 新版 [`0049fc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md#insn-0049fc50) · [`0049fc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md#insn-0049fc48) · [`0049fc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fc40.md#insn-0049fc4c)

~~~diff
- 0049f930 ["INT_ADD", "register:40f0:8", ["const:49f930:8", "const:4:8"]]
- 0049f930 ["CALL", null, ["callee:00442c90:8"]]
+ 0049fc50 ["INT_ADD", "register:40f0:8", ["const:49fc50:8", "const:4:8"]]
+ 0049fc50 ["CALL", null, ["callee:00442c90:8"]]
- 0049f930 bytes 108cfe97
+ 0049fc50 bytes 108cfe97
- 0049f928 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0049fc48 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0049f928 bytes c0f0ff90
+ 0049fc48 bytes c0f0ffb0
- 0049f92c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f92c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f92c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f92c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049fc4c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0049fc4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049fc4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049fc4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f92c bytes 00303e91
+ 0049fc4c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3441040892c0dd054ebeff12a0a0f93"></a>

### [`0049fabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fabc.md) → [`0049fddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fddc.md) FUN_0049fddc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`0049b9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b9ec.md) · 呼出先 2件 [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fe38",
      "incomplete_value": false,
      "site": "0049fe40",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fb18",
      "incomplete_value": false,
      "site": "0049fb20",
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
            "const:9ae:8"
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
      "definition_site": "0049fe48",
      "incomplete_value": true,
      "site": "0049fe4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fb28",
      "incomplete_value": true,
      "site": "0049fb2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
      "0049fe40",
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      "0049fe48",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe48",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049fe40",
      "DATA",
      [
        "storage",
        "002b29f8",
        null,
        "string"
      ]
    ],
    [
      "0049fe48",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe48",
      "PARAM",
      [
        "storage",
        "00c97ce0",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fb2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fabc.md#insn-0049fb2c) · [`0049fb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fabc.md#insn-0049fb10) · [`0049fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fabc.md#insn-0049fb18)
- 新版 [`0049fe4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fddc.md#insn-0049fe4c) · [`0049fe30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fddc.md#insn-0049fe30) · [`0049fe38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fddc.md#insn-0049fe38)

~~~diff
- 0049fb2c ["INT_ADD", "register:40f0:8", ["const:49fb2c:8", "const:4:8"]]
- 0049fb2c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049fe4c ["INT_ADD", "register:40f0:8", ["const:49fe4c:8", "const:4:8"]]
+ 0049fe4c ["CALL", null, ["callee:00c58fb0:8"]]
- 0049fb2c bytes 2de11e94
+ 0049fe4c bytes 59e41e94
- 0049fb10 ["INT_ADD", "register:40f0:8", ["const:49fb10:8", "const:4:8"]]
- 0049fb10 ["CALL", null, ["callee:00c58f90:8"]]
+ 0049fe30 ["INT_ADD", "register:40f0:8", ["const:49fe30:8", "const:4:8"]]
+ 0049fe30 ["CALL", null, ["callee:00c58f90:8"]]
- 0049fb10 bytes 2ce11e94
+ 0049fe30 bytes 58e41e94
- 0049fb18 ["COPY", "tmp:0:8", ["const:9ae:8"]]
- 0049fb18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049fb18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049fb18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049fe38 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 0049fe38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fe38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fe38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049fb18 bytes 08b92691
+ 0049fe38 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96771eecbfe368c8d7d0b51eb395cd32"></a>

### [`0049fb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md) → [`0049fe50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fe50.md) FUN_0049fe50

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 5件 [`0049b408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`004a02b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a02b0.md) · 呼出先 5件 [`0049b728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b728.md) [`0049b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fed4",
      "incomplete_value": true,
      "site": "0049feec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fbb4",
      "incomplete_value": true,
      "site": "0049fbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d10:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ff3c",
      "incomplete_value": false,
      "site": "0049ff44",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fc1c",
      "incomplete_value": false,
      "site": "0049fc24",
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
            "const:ad:8"
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
      "definition_site": "0049ff60",
      "incomplete_value": false,
      "site": "0049ff64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:104:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fc40",
      "incomplete_value": false,
      "site": "0049fc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:26:8"
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
      "0049fed4",
      "READ",
      [
        "storage",
        "002c2d10",
        null,
        null
      ]
    ],
    [
      "0049ff44",
      "DATA",
      [
        "storage",
        "002b80ad",
        null,
        "string"
      ]
    ],
    [
      "0049ff4c",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fed4",
      "READ",
      [
        "storage",
        "002c2d60",
        null,
        null
      ]
    ],
    [
      "0049ff44",
      "DATA",
      [
        "storage",
        "002b817c",
        null,
        "string"
      ]
    ],
    [
      "0049ff4c",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md#insn-0049fc30) · [`0049fc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md#insn-0049fc64) · [`0049fb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md#insn-0049fb70)
- 新版 [`0049ff50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fe50.md#insn-0049ff50) · [`0049ff84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fe50.md#insn-0049ff84) · [`0049fe90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049fe50.md#insn-0049fe90)

~~~diff
- 0049fc30 ["INT_ADD", "register:40f0:8", ["const:49fc30:8", "const:4:8"]]
- 0049fc30 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049ff50 ["INT_ADD", "register:40f0:8", ["const:49ff50:8", "const:4:8"]]
+ 0049ff50 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049fc30 bytes ece01e94
+ 0049ff50 bytes 18e41e94
- 0049fc64 ["INT_ADD", "register:40f0:8", ["const:49fc64:8", "const:4:8"]]
- 0049fc64 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0049ff84 ["INT_ADD", "register:40f0:8", ["const:49ff84:8", "const:4:8"]]
+ 0049ff84 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049fc64 bytes dfe01e94
+ 0049ff84 bytes 0be41e94
- 0049fb70 ["INT_ADD", "register:40f0:8", ["const:49fb70:8", "const:4:8"]]
- 0049fb70 ["CALL", null, ["callee:0049b728:8"]]
+ 0049fe90 ["INT_ADD", "register:40f0:8", ["const:49fe90:8", "const:4:8"]]
+ 0049fe90 ["CALL", null, ["callee:0049b728:8"]]
- 0049fb70 bytes 26eeff97
+ 0049fe90 bytes 26eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba39fa11781e2f0362f5d4ed4fda4a9"></a>

### [`0049fca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md) → [`0049ffc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049ffc8.md) FUN_0049ffc8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 5件 [`0049b408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`004a02b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a0/004a02b0.md) · 呼出先 5件 [`0049b728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b728.md) [`0049b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b800.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a008c",
      "incomplete_value": true,
      "site": "004a0098",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:560:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fd6c",
      "incomplete_value": true,
      "site": "0049fd78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004a00d4",
      "incomplete_value": false,
      "site": "004a00d8",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fdb4",
      "incomplete_value": false,
      "site": "0049fdb8",
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
            "const:96e:8"
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
      "definition_site": "004a00f4",
      "incomplete_value": true,
      "site": "004a00f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fdd4",
      "incomplete_value": true,
      "site": "0049fdd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "004a008c",
      "READ",
      [
        "storage",
        "002c2510",
        null,
        null
      ]
    ],
    [
      "004a00d8",
      "DATA",
      [
        "storage",
        "002b396e",
        null,
        "string"
      ]
    ],
    [
      "004a00f4",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a008c",
      "READ",
      [
        "storage",
        "002c2560",
        null,
        null
      ]
    ],
    [
      "004a00d8",
      "DATA",
      [
        "storage",
        "002b39b8",
        null,
        "string"
      ]
    ],
    [
      "004a00f4",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md#insn-0049fdd8) · [`0049fcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md#insn-0049fcd8) · [`0049fd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md#insn-0049fd30)
- 新版 [`004a00f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049ffc8.md#insn-004a00f8) · [`0049fff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049ffc8.md#insn-0049fff8) · [`004a0050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049ffc8.md#insn-004a0050)

~~~diff
- 0049fdd8 ["INT_ADD", "register:40f0:8", ["const:49fdd8:8", "const:4:8"]]
- 0049fdd8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004a00f8 ["INT_ADD", "register:40f0:8", ["const:4a00f8:8", "const:4:8"]]
+ 004a00f8 ["CALL", null, ["callee:00c58fb0:8"]]
- 0049fdd8 bytes 82e01e94
+ 004a00f8 bytes aee31e94
- 0049fcd8 ["INT_ADD", "register:40f0:8", ["const:49fcd8:8", "const:4:8"]]
- 0049fcd8 ["CALL", null, ["callee:0049b728:8"]]
+ 0049fff8 ["INT_ADD", "register:40f0:8", ["const:49fff8:8", "const:4:8"]]
+ 0049fff8 ["CALL", null, ["callee:0049b728:8"]]
- 0049fcd8 bytes ccedff97
+ 0049fff8 bytes ccedff97
- 0049fd30 ["INT_ADD", "register:40f0:8", ["const:49fd30:8", "const:4:8"]]
- 0049fd30 ["CALL", null, ["callee:0049b800:8"]]
+ 004a0050 ["INT_ADD", "register:40f0:8", ["const:4a0050:8", "const:4:8"]]
+ 004a0050 ["CALL", null, ["callee:0049b800:8"]]
- 0049fd30 bytes ecedff97
+ 004a0050 bytes ecedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

