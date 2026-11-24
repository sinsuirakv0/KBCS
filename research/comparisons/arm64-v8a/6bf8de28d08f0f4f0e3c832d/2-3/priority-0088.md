# v16.0.2 → v16.0.3 · 最優先の変更候補 (88)

[一覧の目次](README.md)

<a id="compare-3a5dffb19b3bc68266826005b8ea1482"></a>

### [`00c0fba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0fba4.md) → [`00c10b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c10b98.md) FUN_00c10b98

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0fb94.md) · 呼出先 12件 [`004596a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004596a8.md) [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c1ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c10b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c10b88.md) · 呼出先 12件 [`004599c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/004599c8.md) [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c1ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1ca70.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.02% / 新版 91.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10ed4",
      "incomplete_value": false,
      "site": "00c10ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fee0",
      "incomplete_value": false,
      "site": "00c0fee0",
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
            "const:d98:8"
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
      "definition_site": "00c10f14",
      "incomplete_value": false,
      "site": "00c10f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ff20",
      "incomplete_value": false,
      "site": "00c0ff20",
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
            "const:d98:8"
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
      "definition_site": "00c10f4c",
      "incomplete_value": true,
      "site": "00c10f4c",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ff58",
      "incomplete_value": true,
      "site": "00c0ff58",
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
            "const:d98:8"
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
      "00c10c94",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10c9c",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10ce4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c10c94",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10c9c",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10ce4",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c0fcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0fba4.md#insn-00c0fcbc) · [`00c0fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0fba4.md#insn-00c0fd14) · [`00c0fd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0fba4.md#insn-00c0fd4c)
- 新版 [`00c10cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c10b98.md#insn-00c10cb0) · [`00c10d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c10b98.md#insn-00c10d08) · [`00c10d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c10/00c10b98.md#insn-00c10d40)

~~~diff
- 00c0fcbc ["INT_ADD", "register:40f0:8", ["const:c0fcbc:8", "const:4:8"]]
- 00c0fcbc ["CALL", null, ["callee:00c11234:8"]]
+ 00c10cb0 ["INT_ADD", "register:40f0:8", ["const:c10cb0:8", "const:4:8"]]
+ 00c10cb0 ["CALL", null, ["callee:00c11234:8"]]
- 00c0fcbc bytes 61010094
+ 00c10cb0 bytes 61010094
- 00c0fd14 ["INT_ADD", "register:40f0:8", ["const:c0fd14:8", "const:4:8"]]
- 00c0fd14 ["CALL", null, ["callee:00c11234:8"]]
+ 00c10d08 ["INT_ADD", "register:40f0:8", ["const:c10d08:8", "const:4:8"]]
+ 00c10d08 ["CALL", null, ["callee:00c11234:8"]]
- 00c0fd14 bytes 4b010094
+ 00c10d08 bytes 4b010094
- 00c0fd4c ["INT_ADD", "register:40f0:8", ["const:c0fd4c:8", "const:4:8"]]
- 00c0fd4c ["CALL", null, ["callee:00c1ca70:8"]]
+ 00c10d40 ["INT_ADD", "register:40f0:8", ["const:c10d40:8", "const:4:8"]]
+ 00c10d40 ["CALL", null, ["callee:00c1ca70:8"]]
- 00c0fd4c bytes 4c2f0094
+ 00c10d40 bytes 4c2f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c92cf2810d3d2cf65cca04a0f2593dbd"></a>

### [`00c1001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1001c.md) → [`00c11010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11010.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPKv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`004596a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004596a8.md) [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004599c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/004599c8.md) [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11104",
      "incomplete_value": true,
      "site": "00c11104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10110",
      "incomplete_value": true,
      "site": "00c10110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c111f4",
      "incomplete_value": true,
      "site": "00c111f4",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10200",
      "incomplete_value": true,
      "site": "00c10200",
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
            "const:d98:8"
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
      "definition_site": "00c1110c",
      "incomplete_value": true,
      "site": "00c11110",
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
      "definition_site": "00c10118",
      "incomplete_value": true,
      "site": "00c1011c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1103c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11054",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c1105c",
      "PARAM",
      [
        "storage",
        "002a629f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1103c",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11054",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c1105c",
      "PARAM",
      [
        "storage",
        "002a63f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1001c.md#insn-00c10140) · [`00c101e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1001c.md#insn-00c101e4) · [`00c10200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1001c.md#insn-00c10200)
- 新版 [`00c11134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11010.md#insn-00c11134) · [`00c111d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11010.md#insn-00c111d8) · [`00c111f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11010.md#insn-00c111f4)

~~~diff
- 00c10140 ["INT_ADD", "register:40f0:8", ["const:c10140:8", "const:4:8"]]
- 00c10140 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c11134 ["INT_ADD", "register:40f0:8", ["const:c11134:8", "const:4:8"]]
+ 00c11134 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c10140 bytes 9c370194
+ 00c11134 bytes 93370194
- 00c101e4 ["INT_ADD", "register:40f0:8", ["const:c101e4:8", "const:4:8"]]
- 00c101e4 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c111d8 ["INT_ADD", "register:40f0:8", ["const:c111d8:8", "const:4:8"]]
+ 00c111d8 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c101e4 bytes 4f1f0194
+ 00c111d8 bytes 461f0194
- 00c10200 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d98:8"]]
- 00c10200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c111f4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d58:8"]]
+ 00c111f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c10200 bytes e0ce06f9
+ 00c111f4 bytes e0ae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd80b043d9143aed7a4bbfe580176147"></a>

### [`00c10370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10370.md) → [`00c11364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11364.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c113cc",
      "incomplete_value": true,
      "site": "00c113cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c103d8",
      "incomplete_value": true,
      "site": "00c103d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00c113d4",
      "incomplete_value": true,
      "site": "00c113d8",
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
      "definition_site": "00c103e0",
      "incomplete_value": true,
      "site": "00c103e4",
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
      "definition_site": "00c113f8",
      "incomplete_value": true,
      "site": "00c11400",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10404",
      "incomplete_value": true,
      "site": "00c1040c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "00c113c4",
      "READ",
      [
        "storage",
        "00c9bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00c113cc",
      "DATA",
      [
        "storage",
        "01127f98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c113d0",
      "READ",
      [
        "storage",
        "01127f98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c113c4",
      "READ",
      [
        "storage",
        "00c9cc68",
        null,
        "pointer"
      ]
    ],
    [
      "00c113cc",
      "DATA",
      [
        "storage",
        "01128f58",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c113d0",
      "READ",
      [
        "storage",
        "01128f58",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1040c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10370.md#insn-00c1040c) · [`00c103c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10370.md#insn-00c103c8) · [`00c103cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10370.md#insn-00c103cc)
- 新版 [`00c11400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11364.md#insn-00c11400) · [`00c113bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11364.md#insn-00c113bc) · [`00c113c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11364.md#insn-00c113c0)

~~~diff
- 00c1040c ["INT_ADD", "register:40f0:8", ["const:c1040c:8", "const:4:8"]]
- 00c1040c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c11400 ["INT_ADD", "register:40f0:8", ["const:c11400:8", "const:4:8"]]
+ 00c11400 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1040c bytes e9360194
+ 00c11400 bytes e0360194
- 00c103c8 ["INT_ADD", "register:40f0:8", ["const:c103c8:8", "const:4:8"]]
- 00c103c8 ["CALL", null, ["callee:00c59310:8"]]
+ 00c113bc ["INT_ADD", "register:40f0:8", ["const:c113bc:8", "const:4:8"]]
+ 00c113bc ["CALL", null, ["callee:00c59310:8"]]
- 00c103c8 bytes de1f0194
+ 00c113bc bytes d51f0194
- 00c103cc ["COPY", "register:40b0:8", ["const:c9b000:8"]]
+ 00c113c0 ["COPY", "register:40b0:8", ["const:c9c000:8"]]
- 00c103cc bytes 560400f0
+ 00c113c0 bytes 560400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3438d0aca538ad9816b8fc7c10b998ba"></a>

### [`00c10550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10550.md) → [`00c11544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11544.md) FUN_00c11544

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c10540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10540.md) · 呼出先 8件 [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 1件 [`00c11534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11534.md) · 呼出先 8件 [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11740",
      "incomplete_value": true,
      "site": "00c11740",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1074c",
      "incomplete_value": true,
      "site": "00c1074c",
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
            "const:d98:8"
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
      "definition_site": "00c11624",
      "incomplete_value": true,
      "site": "00c1163c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10630",
      "incomplete_value": true,
      "site": "00c10648",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c11720",
      "incomplete_value": false,
      "site": "00c11724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1072c",
      "incomplete_value": false,
      "site": "00c10730",
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
            "const:da0:8"
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
      "00c11618",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11624",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11720",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c11618",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11624",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11720",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10550.md#insn-00c10648) · [`00c10730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10550.md#insn-00c10730) · [`00c10748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10550.md#insn-00c10748)
- 新版 [`00c1163c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11544.md#insn-00c1163c) · [`00c11724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11544.md#insn-00c11724) · [`00c1173c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11544.md#insn-00c1173c)

~~~diff
- 00c10648 ["INT_ADD", "register:40f0:8", ["const:c10648:8", "const:4:8"]]
- 00c10648 ["CALL", null, ["callee:00c11234:8"]]
+ 00c1163c ["INT_ADD", "register:40f0:8", ["const:c1163c:8", "const:4:8"]]
+ 00c1163c ["CALL", null, ["callee:00c11234:8"]]
- 00c10648 bytes fefeff97
+ 00c1163c bytes fefeff97
- 00c10730 ["INT_ADD", "register:40f0:8", ["const:c10730:8", "const:4:8"]]
- 00c10730 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c11724 ["INT_ADD", "register:40f0:8", ["const:c11724:8", "const:4:8"]]
+ 00c11724 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c10730 bytes fc1d0194
+ 00c11724 bytes f31d0194
- 00c10748 ["INT_ADD", "register:40f0:8", ["const:c10748:8", "const:4:8"]]
- 00c10748 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c1173c ["INT_ADD", "register:40f0:8", ["const:c1173c:8", "const:4:8"]]
+ 00c1173c ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c10748 bytes ea320194
+ 00c1173c bytes e1320194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05b3a19d0c48724ca28018089bad70ac"></a>

### [`00c1079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1079c.md) → [`00c11790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11790.md) FUN_00c11790

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c1078c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1078c.md) · 呼出先 8件 [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 1件 [`00c11780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11780.md) · 呼出先 8件 [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1198c",
      "incomplete_value": true,
      "site": "00c1198c",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10998",
      "incomplete_value": true,
      "site": "00c10998",
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
            "const:d98:8"
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
      "definition_site": "00c11870",
      "incomplete_value": true,
      "site": "00c11888",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1087c",
      "incomplete_value": true,
      "site": "00c10894",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c1196c",
      "incomplete_value": false,
      "site": "00c11970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10978",
      "incomplete_value": false,
      "site": "00c1097c",
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
            "const:da0:8"
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
      "00c11864",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11870",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c1196c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c11864",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11870",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c1196c",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1079c.md#insn-00c10894) · [`00c1097c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1079c.md#insn-00c1097c) · [`00c10994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c1079c.md#insn-00c10994)
- 新版 [`00c11888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11790.md#insn-00c11888) · [`00c11970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11790.md#insn-00c11970) · [`00c11988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11790.md#insn-00c11988)

~~~diff
- 00c10894 ["INT_ADD", "register:40f0:8", ["const:c10894:8", "const:4:8"]]
- 00c10894 ["CALL", null, ["callee:00c11234:8"]]
+ 00c11888 ["INT_ADD", "register:40f0:8", ["const:c11888:8", "const:4:8"]]
+ 00c11888 ["CALL", null, ["callee:00c11234:8"]]
- 00c10894 bytes 6bfeff97
+ 00c11888 bytes 6bfeff97
- 00c1097c ["INT_ADD", "register:40f0:8", ["const:c1097c:8", "const:4:8"]]
- 00c1097c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c11970 ["INT_ADD", "register:40f0:8", ["const:c11970:8", "const:4:8"]]
+ 00c11970 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c1097c bytes 691d0194
+ 00c11970 bytes 601d0194
- 00c10994 ["INT_ADD", "register:40f0:8", ["const:c10994:8", "const:4:8"]]
- 00c10994 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c11988 ["INT_ADD", "register:40f0:8", ["const:c11988:8", "const:4:8"]]
+ 00c11988 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c10994 bytes 57320194
+ 00c11988 bytes 4e320194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5364b446be960ccbf63733d9a00f198a"></a>

### [`00c109e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c109e8.md) → [`00c119dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c119dc.md) FUN_00c119dc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c109d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c109d8.md) · 呼出先 8件 [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 1件 [`00c119cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c119cc.md) · 呼出先 8件 [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11bbc",
      "incomplete_value": true,
      "site": "00c11bbc",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10bc8",
      "incomplete_value": true,
      "site": "00c10bc8",
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
            "const:d98:8"
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
      "definition_site": "00c11b9c",
      "incomplete_value": false,
      "site": "00c11ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10ba8",
      "incomplete_value": false,
      "site": "00c10bac",
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
            "const:da0:8"
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
      "definition_site": "00c11bac",
      "incomplete_value": false,
      "site": "00c11bb8",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10bb8",
      "incomplete_value": false,
      "site": "00c10bc4",
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
            "const:1bc:8"
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
      "00c11a94",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11aa0",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11b9c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c11a94",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11aa0",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11b9c",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c109e8.md#insn-00c10bac) · [`00c10bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c109e8.md#insn-00c10bc4) · [`00c10bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c109e8.md#insn-00c10bc8)
- 新版 [`00c11ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c119dc.md#insn-00c11ba0) · [`00c11bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c119dc.md#insn-00c11bb8) · [`00c11bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c119dc.md#insn-00c11bbc)

~~~diff
- 00c10bac ["INT_ADD", "register:40f0:8", ["const:c10bac:8", "const:4:8"]]
- 00c10bac ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c11ba0 ["INT_ADD", "register:40f0:8", ["const:c11ba0:8", "const:4:8"]]
+ 00c11ba0 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c10bac bytes dd1c0194
+ 00c11ba0 bytes d41c0194
- 00c10bc4 ["INT_ADD", "register:40f0:8", ["const:c10bc4:8", "const:4:8"]]
- 00c10bc4 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c11bb8 ["INT_ADD", "register:40f0:8", ["const:c11bb8:8", "const:4:8"]]
+ 00c11bb8 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c10bc4 bytes cb310194
+ 00c11bb8 bytes c2310194
- 00c10bc8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d98:8"]]
- 00c10bc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c11bbc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d58:8"]]
+ 00c11bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c10bc8 bytes e0ce06f9
+ 00c11bbc bytes e0ae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-973562282ea477268b9276f32e338de2"></a>

### [`00c10c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10c18.md) → [`00c11c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11c0c.md) FUN_00c11c0c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c10c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10c08.md) · 呼出先 8件 [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 1件 [`00c11bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11bfc.md) · 呼出先 8件 [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11dec",
      "incomplete_value": true,
      "site": "00c11dec",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10df8",
      "incomplete_value": true,
      "site": "00c10df8",
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
            "const:d98:8"
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
      "definition_site": "00c11cd0",
      "incomplete_value": true,
      "site": "00c11ce8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10cdc",
      "incomplete_value": true,
      "site": "00c10cf4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c11dcc",
      "incomplete_value": false,
      "site": "00c11dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10dd8",
      "incomplete_value": false,
      "site": "00c10ddc",
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
            "const:da0:8"
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
      "00c11cc4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11cd0",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11dcc",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c11cc4",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11cd0",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11dcc",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10c18.md#insn-00c10cf4) · [`00c10ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10c18.md#insn-00c10ddc) · [`00c10df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10c18.md#insn-00c10df4)
- 新版 [`00c11ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11c0c.md#insn-00c11ce8) · [`00c11dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11c0c.md#insn-00c11dd0) · [`00c11de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11c0c.md#insn-00c11de8)

~~~diff
- 00c10cf4 ["INT_ADD", "register:40f0:8", ["const:c10cf4:8", "const:4:8"]]
- 00c10cf4 ["CALL", null, ["callee:00c11234:8"]]
+ 00c11ce8 ["INT_ADD", "register:40f0:8", ["const:c11ce8:8", "const:4:8"]]
+ 00c11ce8 ["CALL", null, ["callee:00c11234:8"]]
- 00c10cf4 bytes 53fdff97
+ 00c11ce8 bytes 53fdff97
- 00c10ddc ["INT_ADD", "register:40f0:8", ["const:c10ddc:8", "const:4:8"]]
- 00c10ddc ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c11dd0 ["INT_ADD", "register:40f0:8", ["const:c11dd0:8", "const:4:8"]]
+ 00c11dd0 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c10ddc bytes 511c0194
+ 00c11dd0 bytes 481c0194
- 00c10df4 ["INT_ADD", "register:40f0:8", ["const:c10df4:8", "const:4:8"]]
- 00c10df4 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c11de8 ["INT_ADD", "register:40f0:8", ["const:c11de8:8", "const:4:8"]]
+ 00c11de8 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c10df4 bytes 3f310194
+ 00c11de8 bytes 36310194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03241a88cf1f3bdce142489cab907d6e"></a>

### [`00c10e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e48.md) → [`00c11e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11e3c.md) FUN_00c11e3c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e38.md) · 呼出先 12件 [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c1ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c11e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11e2c.md) · 呼出先 12件 [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c1ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1ca70.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c12180",
      "incomplete_value": false,
      "site": "00c12180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1118c",
      "incomplete_value": false,
      "site": "00c1118c",
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
            "const:d98:8"
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
      "definition_site": "00c121c0",
      "incomplete_value": true,
      "site": "00c121c0",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c111cc",
      "incomplete_value": true,
      "site": "00c111cc",
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
            "const:d98:8"
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
      "definition_site": "00c121f8",
      "incomplete_value": true,
      "site": "00c121f8",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11204",
      "incomplete_value": true,
      "site": "00c11204",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c11f3c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11f48",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11f8c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c11f3c",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c11f48",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c11f8c",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c10f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e48.md#insn-00c10f64) · [`00c10fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e48.md#insn-00c10fbc) · [`00c10ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10e48.md#insn-00c10ff4)
- 新版 [`00c11f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11e3c.md#insn-00c11f58) · [`00c11fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11e3c.md#insn-00c11fb0) · [`00c11fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11e3c.md#insn-00c11fe8)

~~~diff
- 00c10f64 ["INT_ADD", "register:40f0:8", ["const:c10f64:8", "const:4:8"]]
- 00c10f64 ["CALL", null, ["callee:00c11234:8"]]
+ 00c11f58 ["INT_ADD", "register:40f0:8", ["const:c11f58:8", "const:4:8"]]
+ 00c11f58 ["CALL", null, ["callee:00c11234:8"]]
- 00c10f64 bytes b7fcff97
+ 00c11f58 bytes b7fcff97
- 00c10fbc ["INT_ADD", "register:40f0:8", ["const:c10fbc:8", "const:4:8"]]
- 00c10fbc ["CALL", null, ["callee:00c11234:8"]]
+ 00c11fb0 ["INT_ADD", "register:40f0:8", ["const:c11fb0:8", "const:4:8"]]
+ 00c11fb0 ["CALL", null, ["callee:00c11234:8"]]
- 00c10fbc bytes a1fcff97
+ 00c11fb0 bytes a1fcff97
- 00c10ff4 ["INT_ADD", "register:40f0:8", ["const:c10ff4:8", "const:4:8"]]
- 00c10ff4 ["CALL", null, ["callee:00c1ca70:8"]]
+ 00c11fe8 ["INT_ADD", "register:40f0:8", ["const:c11fe8:8", "const:4:8"]]
+ 00c11fe8 ["CALL", null, ["callee:00c1ca70:8"]]
- 00c10ff4 bytes a22a0094
+ 00c11fe8 bytes a22a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32b2200ea394e33412a380fe596a84e3"></a>

### [`00c112d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c112d8.md) → [`00c122cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c122cc.md) FUN_00c122cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c112c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c112c8.md) · 呼出先 12件 [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c1ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c122bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c122bc.md) · 呼出先 12件 [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c1ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1ca70.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c12608",
      "incomplete_value": false,
      "site": "00c12608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11614",
      "incomplete_value": false,
      "site": "00c11614",
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
            "const:d98:8"
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
      "definition_site": "00c12648",
      "incomplete_value": false,
      "site": "00c12648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11654",
      "incomplete_value": false,
      "site": "00c11654",
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
            "const:d98:8"
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
      "definition_site": "00c12680",
      "incomplete_value": true,
      "site": "00c12680",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1168c",
      "incomplete_value": true,
      "site": "00c1168c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c123c8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c123d0",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c12418",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c123c8",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c123d0",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c12418",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c113f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c112d8.md#insn-00c113f0) · [`00c11480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c112d8.md#insn-00c11480) · [`00c114ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c112d8.md#insn-00c114ac)
- 新版 [`00c123e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c122cc.md#insn-00c123e4) · [`00c12474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c122cc.md#insn-00c12474) · [`00c124a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c122cc.md#insn-00c124a0)

~~~diff
- 00c113f0 ["INT_ADD", "register:40f0:8", ["const:c113f0:8", "const:4:8"]]
- 00c113f0 ["CALL", null, ["callee:00c11234:8"]]
+ 00c123e4 ["INT_ADD", "register:40f0:8", ["const:c123e4:8", "const:4:8"]]
+ 00c123e4 ["CALL", null, ["callee:00c11234:8"]]
- 00c113f0 bytes 94fbff97
+ 00c123e4 bytes 94fbff97
- 00c11480 ["INT_ADD", "register:40f0:8", ["const:c11480:8", "const:4:8"]]
- 00c11480 ["CALL", null, ["callee:00c1ca70:8"]]
+ 00c12474 ["INT_ADD", "register:40f0:8", ["const:c12474:8", "const:4:8"]]
+ 00c12474 ["CALL", null, ["callee:00c1ca70:8"]]
- 00c11480 bytes 7f290094
+ 00c12474 bytes 7f290094
- 00c114ac ["INT_ADD", "register:40f0:8", ["const:c114ac:8", "const:4:8"]]
- 00c114ac ["CALL", null, ["callee:00c1ca70:8"]]
+ 00c124a0 ["INT_ADD", "register:40f0:8", ["const:c124a0:8", "const:4:8"]]
+ 00c124a0 ["CALL", null, ["callee:00c1ca70:8"]]
- 00c114ac bytes 74290094
+ 00c124a0 bytes 74290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc0b9ce2a7a676c5b349c1abc025960e"></a>

### [`00c11750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11750.md) → [`00c12744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12744.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPKv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c10240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c10/00c10240.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c11234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c11/00c11234.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c12934",
      "incomplete_value": true,
      "site": "00c12934",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11940",
      "incomplete_value": true,
      "site": "00c11940",
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
            "const:d98:8"
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
      "definition_site": "00c1278c",
      "incomplete_value": true,
      "site": "00c127a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11798",
      "incomplete_value": true,
      "site": "00c117b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c12794",
      "incomplete_value": false,
      "site": "00c127a8",
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
            "const:3f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c117a0",
      "incomplete_value": false,
      "site": "00c117b4",
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
            "const:29f:8"
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
      "00c12774",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1278c",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c12794",
      "PARAM",
      [
        "storage",
        "002a629f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c12774",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1278c",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c12794",
      "PARAM",
      [
        "storage",
        "002a63f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c117b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11750.md#insn-00c117b4) · [`00c1187c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11750.md#insn-00c1187c) · [`00c1193c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11750.md#insn-00c1193c)
- 新版 [`00c127a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12744.md#insn-00c127a8) · [`00c12870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12744.md#insn-00c12870) · [`00c12930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12744.md#insn-00c12930)

~~~diff
- 00c117b4 ["INT_ADD", "register:40f0:8", ["const:c117b4:8", "const:4:8"]]
- 00c117b4 ["CALL", null, ["callee:00c11234:8"]]
+ 00c127a8 ["INT_ADD", "register:40f0:8", ["const:c127a8:8", "const:4:8"]]
+ 00c127a8 ["CALL", null, ["callee:00c11234:8"]]
- 00c117b4 bytes a3faff97
+ 00c127a8 bytes a3faff97
- 00c1187c ["INT_ADD", "register:40f0:8", ["const:c1187c:8", "const:4:8"]]
- 00c1187c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c12870 ["INT_ADD", "register:40f0:8", ["const:c12870:8", "const:4:8"]]
+ 00c12870 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1187c bytes cd310194
+ 00c12870 bytes c4310194
- 00c1193c ["INT_ADD", "register:40f0:8", ["const:c1193c:8", "const:4:8"]]
- 00c1193c ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c12930 ["INT_ADD", "register:40f0:8", ["const:c12930:8", "const:4:8"]]
+ 00c12930 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c1193c bytes 6d2e0194
+ 00c12930 bytes 642e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4273a3c6034064dc6b400e42bd3d229e"></a>

### [`00c11b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11b80.md) → [`00c12b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12b74.md) _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e6a0.md) · 呼出先 4件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5f670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f670.md) · 呼出先 4件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c12bbc",
      "incomplete_value": true,
      "site": "00c12bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11bc8",
      "incomplete_value": true,
      "site": "00c11bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c12c24",
      "incomplete_value": true,
      "site": "00c12c24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c11c30",
      "incomplete_value": true,
      "site": "00c11c30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00c12bc8",
      "incomplete_value": true,
      "site": "00c12bcc",
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
      "definition_site": "00c11bd4",
      "incomplete_value": true,
      "site": "00c11bd8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c12ba4",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c12bbc",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c12bc4",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c12ba4",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c12bbc",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c12bc4",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c11c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11b80.md#insn-00c11c00) · [`00c11c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11b80.md#insn-00c11c64) · [`00c11ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11b80.md#insn-00c11ba4)
- 新版 [`00c12bf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12b74.md#insn-00c12bf4) · [`00c12c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12b74.md#insn-00c12c58) · [`00c12b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12b74.md#insn-00c12b98)

~~~diff
- 00c11c00 ["INT_ADD", "register:40f0:8", ["const:c11c00:8", "const:4:8"]]
- 00c11c00 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c12bf4 ["INT_ADD", "register:40f0:8", ["const:c12bf4:8", "const:4:8"]]
+ 00c12bf4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c11c00 bytes ec300194
+ 00c12bf4 bytes e3300194
- 00c11c64 ["INT_ADD", "register:40f0:8", ["const:c11c64:8", "const:4:8"]]
- 00c11c64 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c12c58 ["INT_ADD", "register:40f0:8", ["const:c12c58:8", "const:4:8"]]
+ 00c12c58 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c11c64 bytes d3300194
+ 00c12c58 bytes ca300194
- 00c11ba4 ["COPY", "register:40a8:8", ["const:c9a000:8"]]
+ 00c12b98 ["COPY", "register:40a8:8", ["const:c9b000:8"]]
- 00c11ba4 bytes 550400b0
+ 00c12b98 bytes 550400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-631651c7a82b8588cb0eee416dcf0a2a"></a>

### [`00c11f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11f74.md) → [`00c12f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12f68.md) _ZNSt6__ndk19__num_putIcE23__widen_and_group_floatEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e6b0.md) · 呼出先 7件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5f680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f680.md) · 呼出先 7件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c12fb0",
      "incomplete_value": true,
      "site": "00c12fb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11fbc",
      "incomplete_value": true,
      "site": "00c11fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c13018",
      "incomplete_value": true,
      "site": "00c13018",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c12024",
      "incomplete_value": true,
      "site": "00c12024",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00c131bc",
      "incomplete_value": true,
      "site": "00c131bc",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c121c8",
      "incomplete_value": true,
      "site": "00c121c8",
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
            "const:d98:8"
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
      "00c12f98",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c12fb0",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c12fb8",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c12f98",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c12fb0",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c12fb8",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c11ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11f74.md#insn-00c11ff4) · [`00c12058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11f74.md#insn-00c12058) · [`00c121c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11f74.md#insn-00c121c8)
- 新版 [`00c12fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12f68.md#insn-00c12fe8) · [`00c1304c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12f68.md#insn-00c1304c) · [`00c131bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12f68.md#insn-00c131bc)

~~~diff
- 00c11ff4 ["INT_ADD", "register:40f0:8", ["const:c11ff4:8", "const:4:8"]]
- 00c11ff4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c12fe8 ["INT_ADD", "register:40f0:8", ["const:c12fe8:8", "const:4:8"]]
+ 00c12fe8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c11ff4 bytes ef2f0194
+ 00c12fe8 bytes e62f0194
- 00c12058 ["INT_ADD", "register:40f0:8", ["const:c12058:8", "const:4:8"]]
- 00c12058 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c1304c ["INT_ADD", "register:40f0:8", ["const:c1304c:8", "const:4:8"]]
+ 00c1304c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c12058 bytes d62f0194
+ 00c1304c bytes cd2f0194
- 00c121c8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d98:8"]]
- 00c121c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c131bc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d58:8"]]
+ 00c131bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c121c8 bytes e0ce06f9
+ 00c131bc bytes e0ae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-731a67777630bdc06b50849b9b1fc7ee"></a>

### [`00c1256c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c1256c.md) → [`00c13560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c13560.md) _ZNSt6__ndk19__num_putIwE21__widen_and_group_intEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e6c0.md) · 呼出先 4件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5f690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f690.md) · 呼出先 4件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c135a8",
      "incomplete_value": true,
      "site": "00c135a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c125b4",
      "incomplete_value": true,
      "site": "00c125b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c13610",
      "incomplete_value": true,
      "site": "00c13610",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1261c",
      "incomplete_value": true,
      "site": "00c1261c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00c135b4",
      "incomplete_value": true,
      "site": "00c135b8",
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
      "definition_site": "00c125c0",
      "incomplete_value": true,
      "site": "00c125c4",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c13590",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c135a8",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c135b0",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c13590",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c135a8",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c135b0",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c125ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c1256c.md#insn-00c125ec) · [`00c12650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c1256c.md#insn-00c12650) · [`00c12590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c1256c.md#insn-00c12590)
- 新版 [`00c135e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c13560.md#insn-00c135e0) · [`00c13644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c13560.md#insn-00c13644) · [`00c13584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c13560.md#insn-00c13584)

~~~diff
- 00c125ec ["INT_ADD", "register:40f0:8", ["const:c125ec:8", "const:4:8"]]
- 00c125ec ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c135e0 ["INT_ADD", "register:40f0:8", ["const:c135e0:8", "const:4:8"]]
+ 00c135e0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c125ec bytes 712e0194
+ 00c135e0 bytes 682e0194
- 00c12650 ["INT_ADD", "register:40f0:8", ["const:c12650:8", "const:4:8"]]
- 00c12650 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c13644 ["INT_ADD", "register:40f0:8", ["const:c13644:8", "const:4:8"]]
+ 00c13644 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c12650 bytes 582e0194
+ 00c13644 bytes 4f2e0194
- 00c12590 ["COPY", "register:40b0:8", ["const:c9b000:8"]]
+ 00c13584 ["COPY", "register:40b0:8", ["const:c9c000:8"]]
- 00c12590 bytes 560400b0
+ 00c13584 bytes 560400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3588ac8a3878a2a10ecc9be96186e4c7"></a>

### [`00c12968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c12968.md) → [`00c1395c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c1395c.md) _ZNSt6__ndk19__num_putIwE23__widen_and_group_floatEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e6d0.md) · 呼出先 7件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5f6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f6a0.md) · 呼出先 7件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 96.71% / 新版 96.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c139a4",
      "incomplete_value": true,
      "site": "00c139a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c129b0",
      "incomplete_value": true,
      "site": "00c129b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c13ba8",
      "incomplete_value": true,
      "site": "00c13ba8",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c12bb4",
      "incomplete_value": true,
      "site": "00c12bb4",
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
            "const:d98:8"
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
      "definition_site": "00c13c28",
      "incomplete_value": false,
      "site": "00c13c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c12c34",
      "incomplete_value": false,
      "site": "00c12c34",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1398c",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c139a4",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c139ac",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1398c",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c139a4",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c139ac",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c12a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c12968.md#insn-00c12a4c) · [`00c12bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c12968.md#insn-00c12bb4) · [`00c12c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c12/00c12968.md#insn-00c12c34)
- 新版 [`00c13a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c1395c.md#insn-00c13a40) · [`00c13ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c1395c.md#insn-00c13ba8) · [`00c13c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c13/00c1395c.md#insn-00c13c28)

~~~diff
- 00c12a4c ["INT_ADD", "register:40f0:8", ["const:c12a4c:8", "const:4:8"]]
- 00c12a4c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c13a40 ["INT_ADD", "register:40f0:8", ["const:c13a40:8", "const:4:8"]]
+ 00c13a40 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c12a4c bytes 592d0194
+ 00c13a40 bytes 502d0194
- 00c12bb4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d98:8"]]
- 00c12bb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c13ba8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d58:8"]]
+ 00c13ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c12bb4 bytes e0ce06f9
+ 00c13ba8 bytes e0ae06f9
- 00c12c34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c12c34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c13c28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00c13c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c12c34 bytes 00cd06f9
+ 00c13c28 bytes 00ad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b37aa48a5a8d0b32219fc3675cf36f89"></a>

### [`00c13514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13514.md) → [`00c14508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14508.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c08ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c14548",
      "incomplete_value": true,
      "site": "00c14550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13554",
      "incomplete_value": true,
      "site": "00c1355c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c14558",
      "incomplete_value": true,
      "site": "00c1455c",
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
      "definition_site": "00c13564",
      "incomplete_value": true,
      "site": "00c13568",
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
      "definition_site": "00c14578",
      "incomplete_value": true,
      "site": "00c14580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13584",
      "incomplete_value": true,
      "site": "00c1358c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "00c14548",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c14550",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14554",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c14548",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c14550",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14554",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1358c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13514.md#insn-00c1358c) · [`00c1354c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13514.md#insn-00c1354c) · [`00c13550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13514.md#insn-00c13550)
- 新版 [`00c14580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14508.md#insn-00c14580) · [`00c14540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14508.md#insn-00c14540) · [`00c14544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14508.md#insn-00c14544)

~~~diff
- 00c1358c ["INT_ADD", "register:40f0:8", ["const:c1358c:8", "const:4:8"]]
- 00c1358c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c14580 ["INT_ADD", "register:40f0:8", ["const:c14580:8", "const:4:8"]]
+ 00c14580 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1358c bytes 892a0194
+ 00c14580 bytes 802a0194
- 00c1354c ["INT_ADD", "register:40f0:8", ["const:c1354c:8", "const:4:8"]]
- 00c1354c ["CALL", null, ["callee:00c59310:8"]]
+ 00c14540 ["INT_ADD", "register:40f0:8", ["const:c14540:8", "const:4:8"]]
+ 00c14540 ["CALL", null, ["callee:00c59310:8"]]
- 00c1354c bytes 7d130194
+ 00c14540 bytes 74130194
- 00c13550 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 00c14544 ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 00c13550 bytes 380400f0
+ 00c14544 bytes 380400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d3584ba0b01c5e603b9915fa7cfcb6a"></a>

### [`00c13728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13728.md) → [`00c1471c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c1471c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c08ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1475c",
      "incomplete_value": true,
      "site": "00c14764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13768",
      "incomplete_value": true,
      "site": "00c13770",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c1476c",
      "incomplete_value": true,
      "site": "00c14770",
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
      "definition_site": "00c13778",
      "incomplete_value": true,
      "site": "00c1377c",
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
      "definition_site": "00c1478c",
      "incomplete_value": true,
      "site": "00c14794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13798",
      "incomplete_value": true,
      "site": "00c137a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "00c1475c",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c14764",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14768",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1475c",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c14764",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14768",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c137a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13728.md#insn-00c137a0) · [`00c13760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13728.md#insn-00c13760) · [`00c13764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13728.md#insn-00c13764)
- 新版 [`00c14794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c1471c.md#insn-00c14794) · [`00c14754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c1471c.md#insn-00c14754) · [`00c14758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c1471c.md#insn-00c14758)

~~~diff
- 00c137a0 ["INT_ADD", "register:40f0:8", ["const:c137a0:8", "const:4:8"]]
- 00c137a0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c14794 ["INT_ADD", "register:40f0:8", ["const:c14794:8", "const:4:8"]]
+ 00c14794 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c137a0 bytes 042a0194
+ 00c14794 bytes fb290194
- 00c13760 ["INT_ADD", "register:40f0:8", ["const:c13760:8", "const:4:8"]]
- 00c13760 ["CALL", null, ["callee:00c59310:8"]]
+ 00c14754 ["INT_ADD", "register:40f0:8", ["const:c14754:8", "const:4:8"]]
+ 00c14754 ["CALL", null, ["callee:00c59310:8"]]
- 00c13760 bytes f8120194
+ 00c14754 bytes ef120194
- 00c13764 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 00c14758 ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 00c13764 bytes 380400f0
+ 00c14758 bytes 380400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2faa67a4c14c50f4a4208bdaf976c63"></a>

### [`00c1392c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1392c.md) → [`00c14920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14920.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c1593c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c15/00c1593c.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1495c",
      "incomplete_value": true,
      "site": "00c14964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13968",
      "incomplete_value": true,
      "site": "00c13970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c14990",
      "incomplete_value": true,
      "site": "00c14998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1399c",
      "incomplete_value": true,
      "site": "00c139a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c1498c",
      "incomplete_value": false,
      "site": "00c14998",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c13998",
      "incomplete_value": false,
      "site": "00c139a4",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c1495c",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c14964",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14968",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1495c",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c14964",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14968",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c139a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1392c.md#insn-00c139a4) · [`00c13960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1392c.md#insn-00c13960) · [`00c13964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c1392c.md#insn-00c13964)
- 新版 [`00c14998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14920.md#insn-00c14998) · [`00c14954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14920.md#insn-00c14954) · [`00c14958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14920.md#insn-00c14958)

~~~diff
- 00c139a4 ["INT_ADD", "register:40f0:8", ["const:c139a4:8", "const:4:8"]]
- 00c139a4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c14998 ["INT_ADD", "register:40f0:8", ["const:c14998:8", "const:4:8"]]
+ 00c14998 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c139a4 bytes 83290194
+ 00c14998 bytes 7a290194
- 00c13960 ["INT_ADD", "register:40f0:8", ["const:c13960:8", "const:4:8"]]
- 00c13960 ["CALL", null, ["callee:00c59310:8"]]
+ 00c14954 ["INT_ADD", "register:40f0:8", ["const:c14954:8", "const:4:8"]]
+ 00c14954 ["CALL", null, ["callee:00c59310:8"]]
- 00c13960 bytes 78120194
+ 00c14954 bytes 6f120194
- 00c13964 ["COPY", "register:40b8:8", ["const:c9a000:8"]]
+ 00c14958 ["COPY", "register:40b8:8", ["const:c9b000:8"]]
- 00c13964 bytes 370400f0
+ 00c14958 bytes 370400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91fcae7ef47313c72a697b0e83d93c47"></a>

### [`00c13ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13ab0.md) → [`00c14aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14aa4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c07bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07bb4.md) [`00c14948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14948.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c08ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c08ba8.md) [`00c1593c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c15/00c1593c.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.57% / 新版 97.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c14afc",
      "incomplete_value": true,
      "site": "00c14afc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13b08",
      "incomplete_value": true,
      "site": "00c13b08",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d00:8"
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
      "definition_site": "00c14cf0",
      "incomplete_value": true,
      "site": "00c14d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f3f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13cfc",
      "incomplete_value": true,
      "site": "00c13d10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eff:8"
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
      "definition_site": "00c14b04",
      "incomplete_value": true,
      "site": "00c14b08",
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
      "definition_site": "00c13b10",
      "incomplete_value": true,
      "site": "00c13b14",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c14af4",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c14afc",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14b00",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c14af4",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c14afc",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14b00",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c13b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13ab0.md#insn-00c13b3c) · [`00c13af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13ab0.md#insn-00c13af8) · [`00c13afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c13/00c13ab0.md#insn-00c13afc)
- 新版 [`00c14b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14aa4.md#insn-00c14b30) · [`00c14aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14aa4.md#insn-00c14aec) · [`00c14af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c14/00c14aa4.md#insn-00c14af0)

~~~diff
- 00c13b3c ["INT_ADD", "register:40f0:8", ["const:c13b3c:8", "const:4:8"]]
- 00c13b3c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c14b30 ["INT_ADD", "register:40f0:8", ["const:c14b30:8", "const:4:8"]]
+ 00c14b30 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c13b3c bytes 1d290194
+ 00c14b30 bytes 14290194
- 00c13af8 ["INT_ADD", "register:40f0:8", ["const:c13af8:8", "const:4:8"]]
- 00c13af8 ["CALL", null, ["callee:00c59310:8"]]
+ 00c14aec ["INT_ADD", "register:40f0:8", ["const:c14aec:8", "const:4:8"]]
+ 00c14aec ["CALL", null, ["callee:00c59310:8"]]
- 00c13af8 bytes 12120194
+ 00c14aec bytes 09120194
- 00c13afc ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00c14af0 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00c13afc bytes 3a0400f0
+ 00c14af0 bytes 3a0400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c2a577b9b0d7c6499c5d2541613f5df"></a>

### [`00c14c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14c8c.md) → [`00c15c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c15/00c15c80.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKwSC_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e700.md) · 呼出先 5件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5f6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f6d0.md) · 呼出先 5件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.68% / 新版 99.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c15d08",
      "incomplete_value": true,
      "site": "00c15d10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c14d14",
      "incomplete_value": true,
      "site": "00c14d1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c15d04",
      "incomplete_value": false,
      "site": "00c15d10",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c14d10",
      "incomplete_value": false,
      "site": "00c14d1c",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c15cd4",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c15cdc",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c15ce0",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c15cd4",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c15cdc",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c15ce0",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c14d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14c8c.md#insn-00c14d1c) · [`00c14cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14c8c.md#insn-00c14cd8) · [`00c14cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c14/00c14c8c.md#insn-00c14cdc)
- 新版 [`00c15d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c15/00c15c80.md#insn-00c15d10) · [`00c15ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c15/00c15c80.md#insn-00c15ccc) · [`00c15cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c15/00c15c80.md#insn-00c15cd0)

~~~diff
- 00c14d1c ["INT_ADD", "register:40f0:8", ["const:c14d1c:8", "const:4:8"]]
- 00c14d1c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c15d10 ["INT_ADD", "register:40f0:8", ["const:c15d10:8", "const:4:8"]]
+ 00c15d10 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c14d1c bytes a5240194
+ 00c15d10 bytes 9c240194
- 00c14cd8 ["INT_ADD", "register:40f0:8", ["const:c14cd8:8", "const:4:8"]]
- 00c14cd8 ["CALL", null, ["callee:00c59310:8"]]
+ 00c15ccc ["INT_ADD", "register:40f0:8", ["const:c15ccc:8", "const:4:8"]]
+ 00c15ccc ["CALL", null, ["callee:00c59310:8"]]
- 00c14cd8 bytes 9a0d0194
+ 00c15ccc bytes 910d0194
- 00c14cdc ["COPY", "register:40e0:8", ["const:c9b000:8"]]
+ 00c15cd0 ["COPY", "register:40e0:8", ["const:c9c000:8"]]
- 00c14cdc bytes 3c0400f0
+ 00c15cd0 bytes 3c0400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16a921080b74b024c8f3ed764ccfde38"></a>

### [`00c1518c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1518c.md) → [`00c16180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16180.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e700.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5f6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f6d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1619c",
      "incomplete_value": true,
      "site": "00c161a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c151a8",
      "incomplete_value": true,
      "site": "00c151b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9b8:8"
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
      "definition_site": "00c1619c",
      "incomplete_value": true,
      "site": "00c161a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c151a8",
      "incomplete_value": true,
      "site": "00c151b4",
      "value": [
        "LOAD",
        "16",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1619c",
      "READ",
      [
        "storage",
        "002e19b8",
        null,
        null
      ]
    ],
    [
      "00c1619c",
      "READ",
      [
        "storage",
        "002e19c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1619c",
      "READ",
      [
        "storage",
        "002e19f8",
        null,
        null
      ]
    ],
    [
      "00c1619c",
      "READ",
      [
        "storage",
        "002e1a08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c151a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1518c.md#insn-00c151a0) · [`00c151b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1518c.md#insn-00c151b8)
- 新版 [`00c16194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16180.md#insn-00c16194) · [`00c161ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16180.md#insn-00c161ac)

~~~diff
- 00c151a0 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00c151a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c151a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c151a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c16194 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00c16194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c16194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c16194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c151a0 bytes 08e12691
+ 00c16194 bytes 08e12791
- 00c151b8 ["INT_ADD", "register:40f0:8", ["const:c151b8:8", "const:4:8"]]
- 00c151b8 ["CALL", null, ["callee:00c5f6d0:8"]]
+ 00c161ac ["INT_ADD", "register:40f0:8", ["const:c161ac:8", "const:4:8"]]
+ 00c161ac ["CALL", null, ["callee:00c5f6d0:8"]]
- 00c151b8 bytes 52250194
+ 00c161ac bytes 49250194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a25d2efad3f7a2c3db1b7877788de3f7"></a>

### [`00c1525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1525c.md) → [`00c16250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16250.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c0c080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16290",
      "incomplete_value": true,
      "site": "00c16298",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c1529c",
      "incomplete_value": true,
      "site": "00c152a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c162a0",
      "incomplete_value": true,
      "site": "00c162a4",
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
      "definition_site": "00c152ac",
      "incomplete_value": true,
      "site": "00c152b0",
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
      "definition_site": "00c162c0",
      "incomplete_value": true,
      "site": "00c162c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c152cc",
      "incomplete_value": true,
      "site": "00c152d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00c16290",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c16298",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1629c",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c16290",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c16298",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1629c",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c152d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1525c.md#insn-00c152d4) · [`00c15294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1525c.md#insn-00c15294) · [`00c15298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c1525c.md#insn-00c15298)
- 新版 [`00c162c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16250.md#insn-00c162c8) · [`00c16288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16250.md#insn-00c16288) · [`00c1628c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16250.md#insn-00c1628c)

~~~diff
- 00c152d4 ["INT_ADD", "register:40f0:8", ["const:c152d4:8", "const:4:8"]]
- 00c152d4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c162c8 ["INT_ADD", "register:40f0:8", ["const:c162c8:8", "const:4:8"]]
+ 00c162c8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c152d4 bytes 37230194
+ 00c162c8 bytes 2e230194
- 00c15294 ["INT_ADD", "register:40f0:8", ["const:c15294:8", "const:4:8"]]
- 00c15294 ["CALL", null, ["callee:00c59310:8"]]
+ 00c16288 ["INT_ADD", "register:40f0:8", ["const:c16288:8", "const:4:8"]]
+ 00c16288 ["CALL", null, ["callee:00c59310:8"]]
- 00c15294 bytes 2b0c0194
+ 00c16288 bytes 220c0194
- 00c15298 ["COPY", "register:40c0:8", ["const:c9b000:8"]]
+ 00c1628c ["COPY", "register:40c0:8", ["const:c9c000:8"]]
- 00c15298 bytes 380400d0
+ 00c1628c bytes 380400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6edd3591c388b4109abb0b7b4b96dc3c"></a>

### [`00c15470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15470.md) → [`00c16464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16464.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c0c080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c164a4",
      "incomplete_value": true,
      "site": "00c164ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c154b0",
      "incomplete_value": true,
      "site": "00c154b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c164b4",
      "incomplete_value": true,
      "site": "00c164b8",
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
      "definition_site": "00c154c0",
      "incomplete_value": true,
      "site": "00c154c4",
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
      "definition_site": "00c164d4",
      "incomplete_value": true,
      "site": "00c164dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c154e0",
      "incomplete_value": true,
      "site": "00c154e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00c164a4",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c164ac",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c164b0",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c164a4",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c164ac",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c164b0",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c154e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15470.md#insn-00c154e8) · [`00c154a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15470.md#insn-00c154a8) · [`00c154ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15470.md#insn-00c154ac)
- 新版 [`00c164dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16464.md#insn-00c164dc) · [`00c1649c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16464.md#insn-00c1649c) · [`00c164a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16464.md#insn-00c164a0)

~~~diff
- 00c154e8 ["INT_ADD", "register:40f0:8", ["const:c154e8:8", "const:4:8"]]
- 00c154e8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c164dc ["INT_ADD", "register:40f0:8", ["const:c164dc:8", "const:4:8"]]
+ 00c164dc ["CALL", null, ["callee:00c5ef80:8"]]
- 00c154e8 bytes b2220194
+ 00c164dc bytes a9220194
- 00c154a8 ["INT_ADD", "register:40f0:8", ["const:c154a8:8", "const:4:8"]]
- 00c154a8 ["CALL", null, ["callee:00c59310:8"]]
+ 00c1649c ["INT_ADD", "register:40f0:8", ["const:c1649c:8", "const:4:8"]]
+ 00c1649c ["CALL", null, ["callee:00c59310:8"]]
- 00c154a8 bytes a60b0194
+ 00c1649c bytes 9d0b0194
- 00c154ac ["COPY", "register:40c0:8", ["const:c9b000:8"]]
+ 00c164a0 ["COPY", "register:40c0:8", ["const:c9c000:8"]]
- 00c154ac bytes 380400d0
+ 00c164a0 bytes 380400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e2de23ad551a69eb3f99004b3550414"></a>

### [`00c15674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15674.md) → [`00c16668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16668.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c17680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c17680.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c166a4",
      "incomplete_value": true,
      "site": "00c166ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c156b0",
      "incomplete_value": true,
      "site": "00c156b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c166b4",
      "incomplete_value": true,
      "site": "00c166b8",
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
      "definition_site": "00c156c0",
      "incomplete_value": true,
      "site": "00c156c4",
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
      "definition_site": "00c166d8",
      "incomplete_value": true,
      "site": "00c166e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c156e4",
      "incomplete_value": true,
      "site": "00c156ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00c166a4",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c166ac",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c166b0",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c166a4",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c166ac",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c166b0",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c156ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15674.md#insn-00c156ec) · [`00c156a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15674.md#insn-00c156a8) · [`00c156ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c15674.md#insn-00c156ac)
- 新版 [`00c166e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16668.md#insn-00c166e0) · [`00c1669c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16668.md#insn-00c1669c) · [`00c166a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c16668.md#insn-00c166a0)

~~~diff
- 00c156ec ["INT_ADD", "register:40f0:8", ["const:c156ec:8", "const:4:8"]]
- 00c156ec ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c166e0 ["INT_ADD", "register:40f0:8", ["const:c166e0:8", "const:4:8"]]
+ 00c166e0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c156ec bytes 31220194
+ 00c166e0 bytes 28220194
- 00c156a8 ["INT_ADD", "register:40f0:8", ["const:c156a8:8", "const:4:8"]]
- 00c156a8 ["CALL", null, ["callee:00c59310:8"]]
+ 00c1669c ["INT_ADD", "register:40f0:8", ["const:c1669c:8", "const:4:8"]]
+ 00c1669c ["CALL", null, ["callee:00c59310:8"]]
- 00c156a8 bytes 260b0194
+ 00c1669c bytes 1d0b0194
- 00c156ac ["COPY", "register:40b8:8", ["const:c9b000:8"]]
+ 00c166a0 ["COPY", "register:40b8:8", ["const:c9c000:8"]]
- 00c156ac bytes 370400d0
+ 00c166a0 bytes 370400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03a1b34c90d991f56c91b63620893080"></a>

### [`00c157f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c157f8.md) → [`00c167ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c167ec.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c0b08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b08c.md) [`00c1668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c1668c.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c0c080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c080.md) [`00c17680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c17680.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.07% / 新版 96.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16844",
      "incomplete_value": true,
      "site": "00c16844",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c15850",
      "incomplete_value": true,
      "site": "00c15850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c16a34",
      "incomplete_value": true,
      "site": "00c16a48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f4c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c15a40",
      "incomplete_value": true,
      "site": "00c15a54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f0c:8"
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
      "definition_site": "00c16a34",
      "incomplete_value": true,
      "site": "00c16a48",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c15a40",
      "incomplete_value": true,
      "site": "00c15a54",
      "value": [
        "LOAD",
        "16",
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
      "00c1683c",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c16844",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c16848",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1683c",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c16844",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c16848",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c15884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c157f8.md#insn-00c15884) · [`00c15840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c157f8.md#insn-00c15840) · [`00c15844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c15/00c157f8.md#insn-00c15844)
- 新版 [`00c16878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c167ec.md#insn-00c16878) · [`00c16834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c167ec.md#insn-00c16834) · [`00c16838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c16/00c167ec.md#insn-00c16838)

~~~diff
- 00c15884 ["INT_ADD", "register:40f0:8", ["const:c15884:8", "const:4:8"]]
- 00c15884 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c16878 ["INT_ADD", "register:40f0:8", ["const:c16878:8", "const:4:8"]]
+ 00c16878 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c15884 bytes cb210194
+ 00c16878 bytes c2210194
- 00c15840 ["INT_ADD", "register:40f0:8", ["const:c15840:8", "const:4:8"]]
- 00c15840 ["CALL", null, ["callee:00c59310:8"]]
+ 00c16834 ["INT_ADD", "register:40f0:8", ["const:c16834:8", "const:4:8"]]
+ 00c16834 ["CALL", null, ["callee:00c59310:8"]]
- 00c15840 bytes c00a0194
+ 00c16834 bytes b70a0194
- 00c15844 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
+ 00c16838 ["COPY", "register:40d0:8", ["const:c9c000:8"]]
- 00c15844 bytes 3a0400d0
+ 00c16838 bytes 3a0400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d91c3933d72219c9b7e27270824f188e"></a>

### [`00c169e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c169e8.md) → [`00c179dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c179dc.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE3putES4_RNS_8ios_baseEcPK2tmPKcSC_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a850.md) · 呼出先 5件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 1件 [`00c5b820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b820.md) · 呼出先 5件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.39% / 新版 99.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17a2c",
      "incomplete_value": true,
      "site": "00c17a34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16a38",
      "incomplete_value": true,
      "site": "00c16a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c17a3c",
      "incomplete_value": true,
      "site": "00c17a40",
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
      "definition_site": "00c16a48",
      "incomplete_value": true,
      "site": "00c16a4c",
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
      "definition_site": "00c17a5c",
      "incomplete_value": true,
      "site": "00c17a64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16a68",
      "incomplete_value": true,
      "site": "00c16a70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "00c17a2c",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c17a34",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c17a38",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c17a2c",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c17a34",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c17a38",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c16a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c169e8.md#insn-00c16a70) · [`00c16a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c169e8.md#insn-00c16a30) · [`00c16a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c169e8.md#insn-00c16a34)
- 新版 [`00c17a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c179dc.md#insn-00c17a64) · [`00c17a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c179dc.md#insn-00c17a24) · [`00c17a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c179dc.md#insn-00c17a28)

~~~diff
- 00c16a70 ["INT_ADD", "register:40f0:8", ["const:c16a70:8", "const:4:8"]]
- 00c16a70 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c17a64 ["INT_ADD", "register:40f0:8", ["const:c17a64:8", "const:4:8"]]
+ 00c17a64 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c16a70 bytes 501d0194
+ 00c17a64 bytes 471d0194
- 00c16a30 ["INT_ADD", "register:40f0:8", ["const:c16a30:8", "const:4:8"]]
- 00c16a30 ["CALL", null, ["callee:00c59310:8"]]
+ 00c17a24 ["INT_ADD", "register:40f0:8", ["const:c17a24:8", "const:4:8"]]
+ 00c17a24 ["CALL", null, ["callee:00c59310:8"]]
- 00c16a30 bytes 44060194
+ 00c17a24 bytes 3b060194
- 00c16a34 ["COPY", "register:40d8:8", ["const:c9a000:8"]]
+ 00c17a28 ["COPY", "register:40d8:8", ["const:c9b000:8"]]
- 00c16a34 bytes 3b040090
+ 00c17a28 bytes 3b040090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbfd3d545932741cc270501d277565bd"></a>

### [`00c16dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16dc8.md) → [`00c17dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c17dbc.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE3putES4_RNS_8ios_baseEwPK2tmPKwSC_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17e0c",
      "incomplete_value": true,
      "site": "00c17e14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c16e18",
      "incomplete_value": true,
      "site": "00c16e20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c17e1c",
      "incomplete_value": true,
      "site": "00c17e20",
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
      "definition_site": "00c16e28",
      "incomplete_value": true,
      "site": "00c16e2c",
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
      "definition_site": "00c17e3c",
      "incomplete_value": true,
      "site": "00c17e44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c16e48",
      "incomplete_value": true,
      "site": "00c16e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00c17e0c",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c17e14",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c17e18",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c17e0c",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c17e14",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c17e18",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c16e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16dc8.md#insn-00c16e50) · [`00c16e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16dc8.md#insn-00c16e10) · [`00c16e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c16/00c16dc8.md#insn-00c16e14)
- 新版 [`00c17e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c17dbc.md#insn-00c17e44) · [`00c17e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c17dbc.md#insn-00c17e04) · [`00c17e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c17/00c17dbc.md#insn-00c17e08)

~~~diff
- 00c16e50 ["INT_ADD", "register:40f0:8", ["const:c16e50:8", "const:4:8"]]
- 00c16e50 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c17e44 ["INT_ADD", "register:40f0:8", ["const:c17e44:8", "const:4:8"]]
+ 00c17e44 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c16e50 bytes 581c0194
+ 00c17e44 bytes 4f1c0194
- 00c16e10 ["INT_ADD", "register:40f0:8", ["const:c16e10:8", "const:4:8"]]
- 00c16e10 ["CALL", null, ["callee:00c59310:8"]]
+ 00c17e04 ["INT_ADD", "register:40f0:8", ["const:c17e04:8", "const:4:8"]]
+ 00c17e04 ["CALL", null, ["callee:00c59310:8"]]
- 00c16e10 bytes 4c050194
+ 00c17e04 bytes 43050194
- 00c16e14 ["COPY", "register:40d8:8", ["const:c9b000:8"]]
+ 00c17e08 ["COPY", "register:40d8:8", ["const:c9c000:8"]]
- 00c16e14 bytes 3b0400b0
+ 00c17e08 bytes 3b0400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06d66b69e79c606a3b418be31182bd2a"></a>

### [`00c17134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17134.md) → [`00c18128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18128.md) _ZNKSt6__ndk110__time_put8__do_putEPwRS1_PK2tmcc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e740.md) · 呼出先 5件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md) [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md) [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md) [`00c5e750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e750.md)
- 新版 呼出元 1件 [`00c5f710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f710.md) · 呼出先 5件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md) [`00c5f610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f610.md) [`00c5f700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f700.md) [`00c5f720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c18200",
      "incomplete_value": false,
      "site": "00c18204",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1720c",
      "incomplete_value": false,
      "site": "00c17210",
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
            "const:d98:8"
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
      "00c18200",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c18200",
      "PARAM",
      [
        "storage",
        "0029fdd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c17210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17134.md#insn-00c17210) · [`00c17194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17134.md#insn-00c17194) · [`00c171ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17134.md#insn-00c171ac)
- 新版 [`00c18204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18128.md#insn-00c18204) · [`00c18188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18128.md#insn-00c18188) · [`00c181a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18128.md#insn-00c181a0)

~~~diff
- 00c17210 ["INT_ADD", "register:40f0:8", ["const:c17210:8", "const:4:8"]]
- 00c17210 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c18204 ["INT_ADD", "register:40f0:8", ["const:c18204:8", "const:4:8"]]
+ 00c18204 ["CALL", null, ["callee:00c5f050:8"]]
- 00c17210 bytes 9c1b0194
+ 00c18204 bytes 931b0194
- 00c17194 ["INT_ADD", "register:40f0:8", ["const:c17194:8", "const:4:8"]]
- 00c17194 ["CALL", null, ["callee:00c5f700:8"]]
+ 00c18188 ["INT_ADD", "register:40f0:8", ["const:c18188:8", "const:4:8"]]
+ 00c18188 ["CALL", null, ["callee:00c5f700:8"]]
- 00c17194 bytes 671d0194
+ 00c18188 bytes 5e1d0194
- 00c171ac ["INT_ADD", "register:40f0:8", ["const:c171ac:8", "const:4:8"]]
- 00c171ac ["CALL", null, ["callee:00c5f610:8"]]
+ 00c181a0 ["INT_ADD", "register:40f0:8", ["const:c181a0:8", "const:4:8"]]
+ 00c181a0 ["CALL", null, ["callee:00c5f610:8"]]
- 00c171ac bytes 251d0194
+ 00c181a0 bytes 1c1d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa0642b88ddca72ae94145796e0ad99b"></a>

### [`00c17384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17384.md) → [`00c18378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18378.md) _ZNKSt6__ndk110moneypunctIwLb0EE16do_negative_signEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18384",
      "incomplete_value": true,
      "site": "00c1838c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17390",
      "incomplete_value": true,
      "site": "00c17398",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:2c4000:8"
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
      "00c18384",
      "READ",
      [
        "storage",
        "002c4000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c18384",
      "READ",
      [
        "storage",
        "002c4050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c17390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17384.md#insn-00c17390)
- 新版 [`00c18384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18378.md#insn-00c18384)

~~~diff
- 00c17390 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00c17390 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c17390 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c17390 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c18384 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:50:8"]]
+ 00c18384 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c18384 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c18384 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c17390 bytes 200140fd
+ 00c18384 bytes 202940fd
~~~


<a id="compare-5449a955d0b85523a030304e0da35d96"></a>

### [`00c17414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17414.md) → [`00c18408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18408.md) _ZNKSt6__ndk110moneypunctIwLb1EE16do_negative_signEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18414",
      "incomplete_value": true,
      "site": "00c1841c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17420",
      "incomplete_value": true,
      "site": "00c17428",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:2c4000:8"
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
      "00c18414",
      "READ",
      [
        "storage",
        "002c4000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c18414",
      "READ",
      [
        "storage",
        "002c4050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c17420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17414.md#insn-00c17420)
- 新版 [`00c18414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18408.md#insn-00c18414)

~~~diff
- 00c17420 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00c17420 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c17420 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c17420 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c18414 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:50:8"]]
+ 00c18414 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c18414 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c18414 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c17420 bytes 200140fd
+ 00c18414 bytes 202940fd
~~~


<a id="compare-f780e623b7afb21d751cec72a0154d4c"></a>

### [`00c1784c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c1784c.md) → [`00c18840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18840.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c17b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b90.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c18b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b84.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1889c",
      "incomplete_value": true,
      "site": "00c188a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c178a8",
      "incomplete_value": true,
      "site": "00c178b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c18948",
      "incomplete_value": true,
      "site": "00c18954",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d7f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17954",
      "incomplete_value": true,
      "site": "00c17960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3f:8"
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
      "definition_site": "00c188d0",
      "incomplete_value": true,
      "site": "00c188d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c178dc",
      "incomplete_value": true,
      "site": "00c178e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "00c18870",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c18888",
      "DATA",
      [
        "storage",
        "00c17b90",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1889c",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c18870",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ],
    [
      "00c18888",
      "DATA",
      [
        "storage",
        "00c18b84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1889c",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c178e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c1784c.md#insn-00c178e4) · [`00c17a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c1784c.md#insn-00c17a10) · [`00c17b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c1784c.md#insn-00c17b28)
- 新版 [`00c188d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18840.md#insn-00c188d8) · [`00c18a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18840.md#insn-00c18a04) · [`00c18b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18840.md#insn-00c18b1c)

~~~diff
- 00c178e4 ["INT_ADD", "register:40f0:8", ["const:c178e4:8", "const:4:8"]]
- 00c178e4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c188d8 ["INT_ADD", "register:40f0:8", ["const:c188d8:8", "const:4:8"]]
+ 00c188d8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c178e4 bytes b3190194
+ 00c188d8 bytes aa190194
- 00c17a10 ["INT_ADD", "register:40f0:8", ["const:c17a10:8", "const:4:8"]]
- 00c17a10 ["CALL", null, ["callee:00c5f740:8"]]
+ 00c18a04 ["INT_ADD", "register:40f0:8", ["const:c18a04:8", "const:4:8"]]
+ 00c18a04 ["CALL", null, ["callee:00c5f740:8"]]
- 00c17a10 bytes 581b0194
+ 00c18a04 bytes 4f1b0194
- 00c17b28 ["INT_ADD", "register:40f0:8", ["const:c17b28:8", "const:4:8"]]
- 00c17b28 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c18b1c ["INT_ADD", "register:40f0:8", ["const:c18b1c:8", "const:4:8"]]
+ 00c18b1c ["CALL", null, ["callee:00c5f050:8"]]
- 00c17b28 bytes 56190194
+ 00c18b1c bytes 4d190194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3782916da46d744352e141d99a436b8e"></a>

### [`00c17b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b98.md) → [`00c18b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b8c.md) _ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIcEERNS_10unique_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e760.md) · 呼出先 11件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c17b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)
- 新版 呼出元 1件 [`00c5f730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f730.md) · 呼出先 11件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c18b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b84.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c596a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596a0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18cf8",
      "incomplete_value": true,
      "site": "00c18d00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c17d04",
      "incomplete_value": true,
      "site": "00c17d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
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
      "definition_site": "00c18fd4",
      "incomplete_value": true,
      "site": "00c18fd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17fe0",
      "incomplete_value": true,
      "site": "00c17fe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
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
      "definition_site": "00c1900c",
      "incomplete_value": true,
      "site": "00c19010",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c18018",
      "incomplete_value": true,
      "site": "00c1801c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:df8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c18cf8",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c18d00",
      "DATA",
      [
        "storage",
        "00c17b90",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c18f1c",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c18cf8",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ],
    [
      "00c18d00",
      "DATA",
      [
        "storage",
        "00c18b84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c18f1c",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c17c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b98.md#insn-00c17c0c) · [`00c17ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b98.md#insn-00c17ca8) · [`00c17cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b98.md#insn-00c17cf8)
- 新版 [`00c18c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b8c.md#insn-00c18c00) · [`00c18c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b8c.md#insn-00c18c9c) · [`00c18cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b8c.md#insn-00c18cec)

~~~diff
- 00c17c0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c17c0c ["INT_ADD", "register:40f0:8", ["const:c17c0c:8", "const:4:8"]]
- 00c17c0c ["CALLIND", null, ["register:0:8"]]
+ 00c18c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c18c00 ["INT_ADD", "register:40f0:8", ["const:c18c00:8", "const:4:8"]]
+ 00c18c00 ["CALLIND", null, ["register:0:8"]]
- 00c17c0c bytes 00013fd6
+ 00c18c00 bytes 00013fd6
- 00c17ca8 ["INT_ADD", "register:40f0:8", ["const:c17ca8:8", "const:4:8"]]
- 00c17ca8 ["CALL", null, ["callee:00c5f750:8"]]
+ 00c18c9c ["INT_ADD", "register:40f0:8", ["const:c18c9c:8", "const:4:8"]]
+ 00c18c9c ["CALL", null, ["callee:00c5f750:8"]]
- 00c17ca8 bytes b61a0194
+ 00c18c9c bytes ad1a0194
- 00c17cf8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00c18cec ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00c17cf8 bytes 29040090
+ 00c18cec bytes 29040090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb8517276e9dbf4a134611a4cffb3e4"></a>

### [`00c18da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c18/00c18da0.md) → [`00c19d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c19/00c19d94.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIcS3_NS_9allocato

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c17b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b90.md) [`00c19060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19060.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c18b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b84.md) [`00c1a054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1a054.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19ddc",
      "incomplete_value": true,
      "site": "00c19ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c18de8",
      "incomplete_value": true,
      "site": "00c18de8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
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
      "definition_site": "00c19df8",
      "incomplete_value": true,
      "site": "00c19df8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c18e04",
      "incomplete_value": true,
      "site": "00c18e04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c19e00",
      "incomplete_value": true,
      "site": "00c19e04",
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
      "definition_site": "00c18e0c",
      "incomplete_value": true,
      "site": "00c18e10",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c19dc4",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c19ddc",
      "DATA",
      [
        "storage",
        "00c17b90",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c19df0",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c19dc4",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ],
    [
      "00c19ddc",
      "DATA",
      [
        "storage",
        "00c18b84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c19df0",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c18e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c18/00c18da0.md#insn-00c18e38) · [`00c18dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c18/00c18da0.md#insn-00c18dc8) · [`00c18dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c18/00c18da0.md#insn-00c18dd0)
- 新版 [`00c19e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c19/00c19d94.md#insn-00c19e2c) · [`00c19dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c19/00c19d94.md#insn-00c19dbc) · [`00c19dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c19/00c19d94.md#insn-00c19dc4)

~~~diff
- 00c18e38 ["INT_ADD", "register:40f0:8", ["const:c18e38:8", "const:4:8"]]
- 00c18e38 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c19e2c ["INT_ADD", "register:40f0:8", ["const:c19e2c:8", "const:4:8"]]
+ 00c19e2c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c18e38 bytes 5e140194
+ 00c19e2c bytes 55140194
- 00c18dc8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c19dbc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c18dc8 bytes 080400f0
+ 00c19dbc bytes 080400f0
- 00c18dd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca0:8"]]
- 00c18dd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c19dc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
+ 00c19dc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c18dd0 bytes 085146f9
+ 00c19dc4 bytes 083946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a3edbd3ccfda3ae3a083db3da5b2fee"></a>

### [`00c196e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c196e8.md) → [`00c1a6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1a6dc.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c17b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b90.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c18b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b84.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.94% / 新版 95.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1a724",
      "incomplete_value": true,
      "site": "00c1a724",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c19730",
      "incomplete_value": true,
      "site": "00c19730",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
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
      "definition_site": "00c1a738",
      "incomplete_value": true,
      "site": "00c1a740",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c19744",
      "incomplete_value": true,
      "site": "00c1974c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c1a7e4",
      "incomplete_value": true,
      "site": "00c1a7f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d7f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c197f0",
      "incomplete_value": true,
      "site": "00c197fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3f:8"
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
      "00c1a70c",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c1a724",
      "DATA",
      [
        "storage",
        "00c17b90",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1a738",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c1a70c",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ],
    [
      "00c1a724",
      "DATA",
      [
        "storage",
        "00c18b84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1a738",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c19780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c196e8.md#insn-00c19780) · [`00c198b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c196e8.md#insn-00c198b4) · [`00c199c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c196e8.md#insn-00c199c8)
- 新版 [`00c1a774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1a6dc.md#insn-00c1a774) · [`00c1a8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1a6dc.md#insn-00c1a8a8) · [`00c1a9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1a6dc.md#insn-00c1a9bc)

~~~diff
- 00c19780 ["INT_ADD", "register:40f0:8", ["const:c19780:8", "const:4:8"]]
- 00c19780 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c1a774 ["INT_ADD", "register:40f0:8", ["const:c1a774:8", "const:4:8"]]
+ 00c1a774 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c19780 bytes 0c120194
+ 00c1a774 bytes 03120194
- 00c198b4 ["INT_ADD", "register:40f0:8", ["const:c198b4:8", "const:4:8"]]
- 00c198b4 ["CALL", null, ["callee:00c5f740:8"]]
+ 00c1a8a8 ["INT_ADD", "register:40f0:8", ["const:c1a8a8:8", "const:4:8"]]
+ 00c1a8a8 ["CALL", null, ["callee:00c5f740:8"]]
- 00c198b4 bytes af130194
+ 00c1a8a8 bytes a6130194
- 00c199c8 ["INT_ADD", "register:40f0:8", ["const:c199c8:8", "const:4:8"]]
- 00c199c8 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c1a9bc ["INT_ADD", "register:40f0:8", ["const:c1a9bc:8", "const:4:8"]]
+ 00c1a9bc ["CALL", null, ["callee:00c5f050:8"]]
- 00c199c8 bytes ae110194
+ 00c1a9bc bytes a5110194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3abadbfcbfc87578dc4e35d1b09f6738"></a>

### [`00c19a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19a30.md) → [`00c1aa24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1aa24.md) _ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIwEERNS_10unique_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e790.md) · 呼出先 11件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c17b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c17/00c17b90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c5f760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f760.md) · 呼出先 11件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c18b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c18/00c18b84.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1abb4",
      "incomplete_value": true,
      "site": "00c1abbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c19bc0",
      "incomplete_value": true,
      "site": "00c19bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
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
      "definition_site": "00c1ae78",
      "incomplete_value": true,
      "site": "00c1ae80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c19e84",
      "incomplete_value": true,
      "site": "00c19e8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
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
      "definition_site": "00c1aecc",
      "incomplete_value": true,
      "site": "00c1aed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c19ed8",
      "incomplete_value": true,
      "site": "00c19edc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1abb4",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c1abbc",
      "DATA",
      [
        "storage",
        "00c17b90",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1adc0",
      "READ",
      [
        "storage",
        "00c9bca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c1abb4",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ],
    [
      "00c1abbc",
      "DATA",
      [
        "storage",
        "00c18b84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1adc0",
      "READ",
      [
        "storage",
        "00c9cc70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c19ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19a30.md#insn-00c19ab8) · [`00c19af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19a30.md#insn-00c19af0) · [`00c19b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c19/00c19a30.md#insn-00c19b6c)
- 新版 [`00c1aaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1aa24.md#insn-00c1aaac) · [`00c1aae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1aa24.md#insn-00c1aae4) · [`00c1ab60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1a/00c1aa24.md#insn-00c1ab60)

~~~diff
- 00c19ab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c19ab8 ["INT_ADD", "register:40f0:8", ["const:c19ab8:8", "const:4:8"]]
- 00c19ab8 ["CALLIND", null, ["register:0:8"]]
+ 00c1aaac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1aaac ["INT_ADD", "register:40f0:8", ["const:c1aaac:8", "const:4:8"]]
+ 00c1aaac ["CALLIND", null, ["register:0:8"]]
- 00c19ab8 bytes 00013fd6
+ 00c1aaac bytes 00013fd6
- 00c19af0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c19af0 ["INT_ADD", "register:40f0:8", ["const:c19af0:8", "const:4:8"]]
- 00c19af0 ["CALLIND", null, ["register:0:8"]]
+ 00c1aae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c1aae4 ["INT_ADD", "register:40f0:8", ["const:c1aae4:8", "const:4:8"]]
+ 00c1aae4 ["CALLIND", null, ["register:0:8"]]
- 00c19af0 bytes 00013fd6
+ 00c1aae4 bytes 00013fd6
- 00c19b6c ["INT_ADD", "register:40f0:8", ["const:c19b6c:8", "const:4:8"]]
- 00c19b6c ["CALL", null, ["callee:00c5f770:8"]]
+ 00c1ab60 ["INT_ADD", "register:40f0:8", ["const:c1ab60:8", "const:4:8"]]
+ 00c1ab60 ["CALL", null, ["callee:00c5f770:8"]]
- 00c19b6c bytes 0d130194
+ 00c1ab60 bytes 04130194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-095d1c70fd96b7aa3bd6796ea1336454"></a>

### [`00c1b5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b5d0.md) → [`00c1c5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1c5c4.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEce

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`004596a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004596a8.md) [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c1ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 0件  · 呼出先 19件 [`004599c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/004599c8.md) [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c1ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1ca70.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1c69c",
      "incomplete_value": true,
      "site": "00c1c6a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1b6a8",
      "incomplete_value": true,
      "site": "00c1b6b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c1c964",
      "incomplete_value": true,
      "site": "00c1c964",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1b970",
      "incomplete_value": true,
      "site": "00c1b970",
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
            "const:d98:8"
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
      "definition_site": "00c1c6ac",
      "incomplete_value": true,
      "site": "00c1c6b0",
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
      "definition_site": "00c1b6b8",
      "incomplete_value": true,
      "site": "00c1b6bc",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1c5f8",
      "PARAM",
      [
        "storage",
        "002b1754",
        null,
        "string"
      ]
    ],
    [
      "00c1c62c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1c634",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1c5f8",
      "PARAM",
      [
        "storage",
        "002b182b",
        null,
        "string"
      ]
    ],
    [
      "00c1c62c",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1c634",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1b6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b5d0.md#insn-00c1b6e4) · [`00c1b954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b5d0.md#insn-00c1b954) · [`00c1b96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1b5d0.md#insn-00c1b96c)
- 新版 [`00c1c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1c5c4.md#insn-00c1c6d8) · [`00c1c948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1c5c4.md#insn-00c1c948) · [`00c1c960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1c5c4.md#insn-00c1c960)

~~~diff
- 00c1b6e4 ["INT_ADD", "register:40f0:8", ["const:c1b6e4:8", "const:4:8"]]
- 00c1b6e4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c1c6d8 ["INT_ADD", "register:40f0:8", ["const:c1c6d8:8", "const:4:8"]]
+ 00c1c6d8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1b6e4 bytes 330a0194
+ 00c1c6d8 bytes 2a0a0194
- 00c1b954 ["INT_ADD", "register:40f0:8", ["const:c1b954:8", "const:4:8"]]
- 00c1b954 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c1c948 ["INT_ADD", "register:40f0:8", ["const:c1c948:8", "const:4:8"]]
+ 00c1c948 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c1b954 bytes 73f10094
+ 00c1c948 bytes 6af10094
- 00c1b96c ["INT_ADD", "register:40f0:8", ["const:c1b96c:8", "const:4:8"]]
- 00c1b96c ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c1c960 ["INT_ADD", "register:40f0:8", ["const:c1c960:8", "const:4:8"]]
+ 00c1c960 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c1b96c bytes 61060194
+ 00c1c960 bytes 58060194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c151fc392043e374ac6b129c8e545279"></a>

### [`00c1c1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c1c8.md) → [`00c1d1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d1bc.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEcRKNS_12basic_stringIcS3_NS_9allocatorIc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`004596a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004596a8.md) [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004599c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/004599c8.md) [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.47% / 新版 99.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d20c",
      "incomplete_value": true,
      "site": "00c1d20c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c218",
      "incomplete_value": true,
      "site": "00c1c218",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c1d214",
      "incomplete_value": true,
      "site": "00c1d218",
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
      "definition_site": "00c1c220",
      "incomplete_value": true,
      "site": "00c1c224",
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
      "definition_site": "00c1d238",
      "incomplete_value": true,
      "site": "00c1d240",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c244",
      "incomplete_value": true,
      "site": "00c1c24c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d00:8"
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
      "00c1d204",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d20c",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1d210",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1d204",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d20c",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1d210",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c1c8.md#insn-00c1c24c) · [`00c1c208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c1c8.md#insn-00c1c208) · [`00c1c20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c1c8.md#insn-00c1c20c)
- 新版 [`00c1d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d1bc.md#insn-00c1d240) · [`00c1d1fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d1bc.md#insn-00c1d1fc) · [`00c1d200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d1bc.md#insn-00c1d200)

~~~diff
- 00c1c24c ["INT_ADD", "register:40f0:8", ["const:c1c24c:8", "const:4:8"]]
- 00c1c24c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c1d240 ["INT_ADD", "register:40f0:8", ["const:c1d240:8", "const:4:8"]]
+ 00c1d240 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1c24c bytes 59070194
+ 00c1d240 bytes 50070194
- 00c1c208 ["INT_ADD", "register:40f0:8", ["const:c1c208:8", "const:4:8"]]
- 00c1c208 ["CALL", null, ["callee:00c59310:8"]]
+ 00c1d1fc ["INT_ADD", "register:40f0:8", ["const:c1d1fc:8", "const:4:8"]]
+ 00c1d1fc ["CALL", null, ["callee:00c59310:8"]]
- 00c1c208 bytes 4ef00094
+ 00c1d1fc bytes 45f00094
- 00c1c20c ["COPY", "register:40b8:8", ["const:c9a000:8"]]
+ 00c1d200 ["COPY", "register:40b8:8", ["const:c9b000:8"]]
- 00c1c20c bytes f70300d0
+ 00c1d200 bytes f70300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-793270b0b78ed6f5d3f312a62ffb2d25"></a>

### [`00c1c54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c54c.md) → [`00c1d540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d540.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwe

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c1ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1ba7c.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c1ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1c/00c1ca70.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d618",
      "incomplete_value": true,
      "site": "00c1d620",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c1c624",
      "incomplete_value": true,
      "site": "00c1c62c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c1d8ec",
      "incomplete_value": true,
      "site": "00c1d8ec",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c8f8",
      "incomplete_value": true,
      "site": "00c1c8f8",
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
            "const:d98:8"
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
      "definition_site": "00c1d628",
      "incomplete_value": true,
      "site": "00c1d62c",
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
      "definition_site": "00c1c634",
      "incomplete_value": true,
      "site": "00c1c638",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1d574",
      "PARAM",
      [
        "storage",
        "002b1754",
        null,
        "string"
      ]
    ],
    [
      "00c1d5a8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1d5b0",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1d574",
      "PARAM",
      [
        "storage",
        "002b182b",
        null,
        "string"
      ]
    ],
    [
      "00c1d5a8",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1d5b0",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1c59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c54c.md#insn-00c1c59c) · [`00c1c5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c54c.md#insn-00c1c5d4) · [`00c1c660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1c/00c1c54c.md#insn-00c1c660)
- 新版 [`00c1d590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d540.md#insn-00c1d590) · [`00c1d5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d540.md#insn-00c1d5c8) · [`00c1d654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1d/00c1d540.md#insn-00c1d654)

~~~diff
- 00c1c59c ["INT_ADD", "register:40f0:8", ["const:c1c59c:8", "const:4:8"]]
- 00c1c59c ["CALL", null, ["callee:00c5f1a0:8"]]
+ 00c1d590 ["INT_ADD", "register:40f0:8", ["const:c1d590:8", "const:4:8"]]
+ 00c1d590 ["CALL", null, ["callee:00c5f1a0:8"]]
- 00c1c59c bytes 0d070194
+ 00c1d590 bytes 04070194
- 00c1c5d4 ["INT_ADD", "register:40f0:8", ["const:c1c5d4:8", "const:4:8"]]
- 00c1c5d4 ["CALL", null, ["callee:00c1ca70:8"]]
+ 00c1d5c8 ["INT_ADD", "register:40f0:8", ["const:c1d5c8:8", "const:4:8"]]
+ 00c1d5c8 ["CALL", null, ["callee:00c1ca70:8"]]
- 00c1c5d4 bytes 2afdff97
+ 00c1d5c8 bytes 2afdff97
- 00c1c660 ["INT_ADD", "register:40f0:8", ["const:c1c660:8", "const:4:8"]]
- 00c1c660 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c1d654 ["INT_ADD", "register:40f0:8", ["const:c1d654:8", "const:4:8"]]
+ 00c1d654 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1c660 bytes 54060194
+ 00c1d654 bytes 4b060194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdb506b3bc52672cfc5c8380a1b81ccb"></a>

### [`00c1d0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d0b0.md) → [`00c1e0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e0a4.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c11980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c11/00c11980.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c12974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c12/00c12974.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1e0f4",
      "incomplete_value": true,
      "site": "00c1e0f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c1d100",
      "incomplete_value": true,
      "site": "00c1d100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c1e120",
      "incomplete_value": true,
      "site": "00c1e128",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d12c",
      "incomplete_value": true,
      "site": "00c1d134",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c10:8"
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
      "definition_site": "00c1e11c",
      "incomplete_value": false,
      "site": "00c1e128",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c1d128",
      "incomplete_value": false,
      "site": "00c1d134",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c1e0ec",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c1e0f4",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1e0f8",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1e0ec",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c1e0f4",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1e0f8",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1d134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d0b0.md#insn-00c1d134) · [`00c1d0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d0b0.md#insn-00c1d0f0) · [`00c1d0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d0b0.md#insn-00c1d0f4)
- 新版 [`00c1e128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e0a4.md#insn-00c1e128) · [`00c1e0e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e0a4.md#insn-00c1e0e4) · [`00c1e0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e0a4.md#insn-00c1e0e8)

~~~diff
- 00c1d134 ["INT_ADD", "register:40f0:8", ["const:c1d134:8", "const:4:8"]]
- 00c1d134 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c1e128 ["INT_ADD", "register:40f0:8", ["const:c1e128:8", "const:4:8"]]
+ 00c1e128 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1d134 bytes 9f030194
+ 00c1e128 bytes 96030194
- 00c1d0f0 ["INT_ADD", "register:40f0:8", ["const:c1d0f0:8", "const:4:8"]]
- 00c1d0f0 ["CALL", null, ["callee:00c59310:8"]]
+ 00c1e0e4 ["INT_ADD", "register:40f0:8", ["const:c1e0e4:8", "const:4:8"]]
+ 00c1e0e4 ["CALL", null, ["callee:00c59310:8"]]
- 00c1d0f0 bytes 94ec0094
+ 00c1e0e4 bytes 8bec0094
- 00c1d0f4 ["COPY", "register:40b8:8", ["const:c9b000:8"]]
+ 00c1e0e8 ["COPY", "register:40b8:8", ["const:c9c000:8"]]
- 00c1d0f4 bytes f70300d0
+ 00c1e0e8 bytes f70300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3cb4e9a0bfa3a697517c5a49e29d142"></a>

### [`00c1d738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md) → [`00c1e72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e72c.md) FUN_00c1e72c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c1fbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fbe0.md) · 呼出先 12件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c20bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20bd4.md) · 呼出先 12件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 35.74% / 新版 35.74%

CFGの説明率　旧版 20.85% / 新版 20.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `store_condition` 6件, `store_value` 1件, `unresolved_branch_alignment` 128件, `unresolved_call_alignment` 103件, `unresolved_store_alignment` 155件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 23件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1e768",
      "incomplete_value": false,
      "site": "00c1e768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c94000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d774",
      "incomplete_value": false,
      "site": "00c1d774",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00c1d7e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00c1d7e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1e768",
      "DATA",
      [
        "storage",
        "00c93790",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1e7d8",
      "READ",
      [
        "storage",
        "00c9bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00c1d7ec",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c1e768",
      "DATA",
      [
        "storage",
        "00c94760",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1e7d8",
      "READ",
      [
        "storage",
        "00c9cc98",
        null,
        "pointer"
      ]
    ],
    [
      "00c1e7e0",
      "READ",
      [
        "storage",
        "00c9c418",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1d7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md#insn-00c1d7e8) · [`00c1d7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md#insn-00c1d7f4) · [`00c1d7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md#insn-00c1d7f8)

~~~diff
- 00c1d7e8 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00c1d7e8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00c1d7e8 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00c1d7e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00c1d7e8 bytes 19a001a9
- 00c1d7f4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00c1d7f4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00c1d7f4 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00c1d7f4 ["COPY", "tmp:3:8", ["register:40b0:8"]]
- 00c1d7f4 bytes c87e00a9
- 00c1d7f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00c1d7f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00c1d7f8 bytes f50700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc3d4d119c68436c80fca0fe8c7a584d"></a>

### [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) → [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) FUN_00c2051c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c24f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f98.md) [`00c250d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c250d0.md) · 呼出先 43件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c1d738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md) [`00c1fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md) [`00c1fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md) [`00c1fec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md)
- 新版 呼出元 2件 [`00c25f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f8c.md) [`00c260c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c260c4.md) · 呼出先 43件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c1e72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e72c.md) [`00c20c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md) [`00c20d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md) [`00c20eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.68% / 新版 87.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2054c",
      "incomplete_value": false,
      "site": "00c2054c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c94000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f558",
      "incomplete_value": false,
      "site": "00c1f558",
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
            "const:790:8"
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
      "definition_site": "00c206f8",
      "incomplete_value": true,
      "site": "00c206f8",
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
      "definition_site": "00c1f704",
      "incomplete_value": true,
      "site": "00c1f704",
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
      "definition_site": "00c20734",
      "incomplete_value": true,
      "site": "00c20738",
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
      "definition_site": "00c1f740",
      "incomplete_value": true,
      "site": "00c1f744",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2054c",
      "DATA",
      [
        "storage",
        "00c93790",
        null,
        "undefined *"
      ]
    ],
    [
      "00c205dc",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c205e4",
      "READ",
      [
        "storage",
        "01127ee0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2054c",
      "DATA",
      [
        "storage",
        "00c94760",
        null,
        "undefined *"
      ]
    ],
    [
      "00c205dc",
      "READ",
      [
        "storage",
        "01128ea8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c205e4",
      "READ",
      [
        "storage",
        "01128ea0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md#insn-00c1fa84) · [`00c1fa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md#insn-00c1fa90) · [`00c1fa94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md#insn-00c1fa94)
- 新版 [`00c20a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md#insn-00c20a78) · [`00c20a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md#insn-00c20a84) · [`00c20a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md#insn-00c20a88)

~~~diff
- 00c1fa84 ["INT_ADD", "register:40f0:8", ["const:c1fa84:8", "const:4:8"]]
- 00c1fa84 ["CALL", null, ["callee:00c1e72c:8"]]
+ 00c20a78 ["INT_ADD", "register:40f0:8", ["const:c20a78:8", "const:4:8"]]
+ 00c20a78 ["CALL", null, ["callee:00c1e72c:8"]]
- 00c1fa84 bytes 2df7ff97
+ 00c20a78 bytes 2df7ff97
- 00c1fa90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ee0:8"]]
- 00c1fa90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00c20a84 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ea0:8"]]
+ 00c20a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00c1fa90 bytes d57207f9
+ 00c20a84 bytes d55207f9
- 00c1fa94 ["INT_ADD", "register:40f0:8", ["const:c1fa94:8", "const:4:8"]]
- 00c1fa94 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c20a88 ["INT_ADD", "register:40f0:8", ["const:c20a88:8", "const:4:8"]]
+ 00c20a88 ["CALL", null, ["callee:00c58f10:8"]]
- 00c1fa94 bytes 2be10094
+ 00c20a88 bytes 22e10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38bd7881b92b68971da6d18ffc41d28b"></a>

### [`00c1fbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fbe0.md) → [`00c20bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20bd4.md) _ZNSt6__ndk16locale7classicEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5e990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e990.md) · 呼出先 3件 [`00c1d738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d738.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5f960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f960.md) · 呼出先 3件 [`00c1e72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e72c.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c20c3c",
      "incomplete_value": true,
      "site": "00c20c3c",
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
      "definition_site": "00c1fc48",
      "incomplete_value": true,
      "site": "00c1fc48",
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
            "const:ee0:8"
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
      "definition_site": "00c20c10",
      "incomplete_value": false,
      "site": "00c20c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fc1c",
      "incomplete_value": false,
      "site": "00c1fc20",
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
            "const:ee8:8"
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
      "definition_site": "00c20c28",
      "incomplete_value": false,
      "site": "00c20c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fc34",
      "incomplete_value": false,
      "site": "00c1fc38",
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
            "const:da8:8"
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
      "00c20bec",
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c20bf8",
      "DATA",
      [
        "storage",
        "01127ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c20c10",
      "PARAM",
      [
        "storage",
        "01127ee8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c20bec",
      "READ",
      [
        "storage",
        "01128ea8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c20bf8",
      "DATA",
      [
        "storage",
        "01128ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c20c10",
      "PARAM",
      [
        "storage",
        "01128ea8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fbe0.md#insn-00c1fc20) · [`00c1fc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fbe0.md#insn-00c1fc38) · [`00c1fc48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fbe0.md#insn-00c1fc48)
- 新版 [`00c20c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20bd4.md#insn-00c20c14) · [`00c20c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20bd4.md#insn-00c20c2c) · [`00c20c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20bd4.md#insn-00c20c3c)

~~~diff
- 00c1fc20 ["INT_ADD", "register:40f0:8", ["const:c1fc20:8", "const:4:8"]]
- 00c1fc20 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c20c14 ["INT_ADD", "register:40f0:8", ["const:c20c14:8", "const:4:8"]]
+ 00c20c14 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c1fc20 bytes c0e00094
+ 00c20c14 bytes b7e00094
- 00c1fc38 ["INT_ADD", "register:40f0:8", ["const:c1fc38:8", "const:4:8"]]
- 00c1fc38 ["CALL", null, ["callee:00c1e72c:8"]]
+ 00c20c2c ["INT_ADD", "register:40f0:8", ["const:c20c2c:8", "const:4:8"]]
+ 00c20c2c ["CALL", null, ["callee:00c1e72c:8"]]
- 00c1fc38 bytes c0f6ff97
+ 00c20c2c bytes c0f6ff97
- 00c1fc48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 00c1fc48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00c20c3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00c20c3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00c1fc48 bytes 137107f9
+ 00c20c3c bytes 135107f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cf5ca665d80b09afa4b90cb0b00469f"></a>

### [`00c1fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md) → [`00c20c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md) FUN_00c20c60

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20c84",
      "incomplete_value": true,
      "site": "00c20c88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c1fc90",
      "incomplete_value": true,
      "site": "00c1fc94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:448:8"
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
      "definition_site": "00c20c90",
      "incomplete_value": true,
      "site": "00c20c94",
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
      "definition_site": "00c1fc9c",
      "incomplete_value": true,
      "site": "00c1fca0",
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
      "definition_site": "00c20cb8",
      "incomplete_value": true,
      "site": "00c20cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c1fcc4",
      "incomplete_value": true,
      "site": "00c1fcc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:448:8"
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
      "00c20c84",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c20c88",
      "DATA",
      [
        "storage",
        "01127c58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20c8c",
      "READ",
      [
        "storage",
        "01127c58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20c84",
      "READ",
      [
        "storage",
        "00c9c418",
        null,
        "pointer"
      ]
    ],
    [
      "00c20c88",
      "DATA",
      [
        "storage",
        "01128c18",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20c8c",
      "READ",
      [
        "storage",
        "01128c18",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md#insn-00c1fcc8) · [`00c1fc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md#insn-00c1fc84) · [`00c1fc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md#insn-00c1fc90)
- 新版 [`00c20cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md#insn-00c20cbc) · [`00c20c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md#insn-00c20c78) · [`00c20c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md#insn-00c20c84)

~~~diff
- 00c1fcc8 ["INT_ADD", "register:40f0:8", ["const:c1fcc8:8", "const:4:8"]]
- 00c1fcc8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c20cbc ["INT_ADD", "register:40f0:8", ["const:c20cbc:8", "const:4:8"]]
+ 00c20cbc ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1fcc8 bytes baf80094
+ 00c20cbc bytes b1f80094
- 00c1fc84 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c20c78 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c1fc84 bytes f4030090
+ 00c20c78 bytes f4030090
- 00c1fc90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:448:8"]]
- 00c1fc90 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20c84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00c20c84 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fc90 bytes 942642f9
+ 00c20c84 bytes 940e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d612317b548794dabc84b62ee35f519b"></a>

### [`00c1fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md) → [`00c20d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md) FUN_00c20d8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20db0",
      "incomplete_value": true,
      "site": "00c20db4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c1fdbc",
      "incomplete_value": true,
      "site": "00c1fdc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "definition_site": "00c20dbc",
      "incomplete_value": true,
      "site": "00c20dc0",
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
      "definition_site": "00c1fdc8",
      "incomplete_value": true,
      "site": "00c1fdcc",
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
      "definition_site": "00c20de4",
      "incomplete_value": true,
      "site": "00c20de8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c1fdf0",
      "incomplete_value": true,
      "site": "00c1fdf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "00c20db0",
      "READ",
      [
        "storage",
        "00c9bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20db4",
      "DATA",
      [
        "storage",
        "01127c68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20db8",
      "READ",
      [
        "storage",
        "01127c68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20db0",
      "READ",
      [
        "storage",
        "00c9cca8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20db4",
      "DATA",
      [
        "storage",
        "01128c28",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20db8",
      "READ",
      [
        "storage",
        "01128c28",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md#insn-00c1fdf4) · [`00c1fdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md#insn-00c1fdb0) · [`00c1fdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md#insn-00c1fdbc)
- 新版 [`00c20de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md#insn-00c20de8) · [`00c20da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md#insn-00c20da4) · [`00c20db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md#insn-00c20db0)

~~~diff
- 00c1fdf4 ["INT_ADD", "register:40f0:8", ["const:c1fdf4:8", "const:4:8"]]
- 00c1fdf4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c20de8 ["INT_ADD", "register:40f0:8", ["const:c20de8:8", "const:4:8"]]
+ 00c20de8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1fdf4 bytes 6ff80094
+ 00c20de8 bytes 66f80094
- 00c1fdb0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c20da4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c1fdb0 bytes f4030090
+ 00c20da4 bytes f4030090
- 00c1fdbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
- 00c1fdbc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20db0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00c20db0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fdbc bytes 946e46f9
+ 00c20db0 bytes 945646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514c6d12a764de0a1b5ff74eaa12c563"></a>

### [`00c1fec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md) → [`00c20eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md) FUN_00c20eb8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20edc",
      "incomplete_value": true,
      "site": "00c20ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fee8",
      "incomplete_value": true,
      "site": "00c1feec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c20ee8",
      "incomplete_value": true,
      "site": "00c20eec",
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
      "definition_site": "00c1fef4",
      "incomplete_value": true,
      "site": "00c1fef8",
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
      "definition_site": "00c20f10",
      "incomplete_value": true,
      "site": "00c20f14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1ff1c",
      "incomplete_value": true,
      "site": "00c1ff20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "00c20edc",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c20ee0",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20ee4",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20edc",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20ee0",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20ee4",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1ff20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md#insn-00c1ff20) · [`00c1fedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md#insn-00c1fedc) · [`00c1fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md#insn-00c1fee8)
- 新版 [`00c20f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md#insn-00c20f14) · [`00c20ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md#insn-00c20ed0) · [`00c20edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md#insn-00c20edc)

~~~diff
- 00c1ff20 ["INT_ADD", "register:40f0:8", ["const:c1ff20:8", "const:4:8"]]
- 00c1ff20 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c20f14 ["INT_ADD", "register:40f0:8", ["const:c20f14:8", "const:4:8"]]
+ 00c20f14 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c1ff20 bytes 24f80094
+ 00c20f14 bytes 1bf80094
- 00c1fedc ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c20ed0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c1fedc bytes d40300f0
+ 00c20ed0 bytes d40300f0
- 00c1fee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00c1fee8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20edc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00c20edc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fee8 bytes 948246f9
+ 00c20edc bytes 946a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ec025c0c6e2cb1d7816a805c25a2592"></a>

### [`00c1fff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md) → [`00c20fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20fe4.md) FUN_00c20fe4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21008",
      "incomplete_value": true,
      "site": "00c2100c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c20014",
      "incomplete_value": true,
      "site": "00c20018",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c21014",
      "incomplete_value": true,
      "site": "00c21018",
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
      "definition_site": "00c20020",
      "incomplete_value": true,
      "site": "00c20024",
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
      "definition_site": "00c2103c",
      "incomplete_value": true,
      "site": "00c21040",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20048",
      "incomplete_value": true,
      "site": "00c2004c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c10:8"
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
      "00c21008",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c2100c",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21010",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21008",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2100c",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21010",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2004c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md#insn-00c2004c) · [`00c20008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md#insn-00c20008) · [`00c20014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md#insn-00c20014)
- 新版 [`00c21040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20fe4.md#insn-00c21040) · [`00c20ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20fe4.md#insn-00c20ffc) · [`00c21008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20fe4.md#insn-00c21008)

~~~diff
- 00c2004c ["INT_ADD", "register:40f0:8", ["const:c2004c:8", "const:4:8"]]
- 00c2004c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21040 ["INT_ADD", "register:40f0:8", ["const:c21040:8", "const:4:8"]]
+ 00c21040 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c2004c bytes d9f70094
+ 00c21040 bytes d0f70094
- 00c20008 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c20ffc ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20008 bytes d40300f0
+ 00c20ffc bytes f4030090
- 00c20014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00c20014 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21008 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00c21008 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20014 bytes 940a46f9
+ 00c21008 bytes 94f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f34952ca79f316767b9921e3b87ce5d"></a>

### [`00c2011c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c2011c.md) → [`00c21110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21110.md) FUN_00c21110

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21134",
      "incomplete_value": true,
      "site": "00c21138",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20140",
      "incomplete_value": true,
      "site": "00c20144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "definition_site": "00c21140",
      "incomplete_value": true,
      "site": "00c21144",
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
      "definition_site": "00c2014c",
      "incomplete_value": true,
      "site": "00c20150",
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
      "definition_site": "00c21168",
      "incomplete_value": true,
      "site": "00c2116c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20174",
      "incomplete_value": true,
      "site": "00c20178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "00c21134",
      "READ",
      [
        "storage",
        "00c9b988",
        null,
        "pointer"
      ]
    ],
    [
      "00c21138",
      "DATA",
      [
        "storage",
        "01127f28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2113c",
      "READ",
      [
        "storage",
        "01127f28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21134",
      "READ",
      [
        "storage",
        "00c9c958",
        null,
        "pointer"
      ]
    ],
    [
      "00c21138",
      "DATA",
      [
        "storage",
        "01128ee8",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2113c",
      "READ",
      [
        "storage",
        "01128ee8",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c2011c.md#insn-00c20178) · [`00c20134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c2011c.md#insn-00c20134) · [`00c20140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c2011c.md#insn-00c20140)
- 新版 [`00c2116c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21110.md#insn-00c2116c) · [`00c21128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21110.md#insn-00c21128) · [`00c21134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21110.md#insn-00c21134)

~~~diff
- 00c20178 ["INT_ADD", "register:40f0:8", ["const:c20178:8", "const:4:8"]]
- 00c20178 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2116c ["INT_ADD", "register:40f0:8", ["const:c2116c:8", "const:4:8"]]
+ 00c2116c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20178 bytes 8ef70094
+ 00c2116c bytes 85f70094
- 00c20134 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21128 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20134 bytes d40300f0
+ 00c21128 bytes d40300f0
- 00c20140 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00c20140 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21134 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:958:8"]]
+ 00c21134 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20140 bytes 94c644f9
+ 00c21134 bytes 94ae44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-056fcea796a54832b734cd4daea70faf"></a>

### [`00c20248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20248.md) → [`00c2123c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c2123c.md) FUN_00c2123c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21260",
      "incomplete_value": true,
      "site": "00c21264",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c2026c",
      "incomplete_value": true,
      "site": "00c20270",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "definition_site": "00c2126c",
      "incomplete_value": true,
      "site": "00c21270",
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
      "definition_site": "00c20278",
      "incomplete_value": true,
      "site": "00c2027c",
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
      "definition_site": "00c21294",
      "incomplete_value": true,
      "site": "00c21298",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c202a0",
      "incomplete_value": true,
      "site": "00c202a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "00c21260",
      "READ",
      [
        "storage",
        "00c9bc78",
        null,
        "pointer"
      ]
    ],
    [
      "00c21264",
      "DATA",
      [
        "storage",
        "01127f38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21268",
      "READ",
      [
        "storage",
        "01127f38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21260",
      "READ",
      [
        "storage",
        "00c9cc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c21264",
      "DATA",
      [
        "storage",
        "01128ef8",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21268",
      "READ",
      [
        "storage",
        "01128ef8",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c202a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20248.md#insn-00c202a4) · [`00c20260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20248.md#insn-00c20260) · [`00c2026c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20248.md#insn-00c2026c)
- 新版 [`00c21298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c2123c.md#insn-00c21298) · [`00c21254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c2123c.md#insn-00c21254) · [`00c21260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c2123c.md#insn-00c21260)

~~~diff
- 00c202a4 ["INT_ADD", "register:40f0:8", ["const:c202a4:8", "const:4:8"]]
- 00c202a4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21298 ["INT_ADD", "register:40f0:8", ["const:c21298:8", "const:4:8"]]
+ 00c21298 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c202a4 bytes 43f70094
+ 00c21298 bytes 3af70094
- 00c20260 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21254 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20260 bytes d40300f0
+ 00c21254 bytes d40300f0
- 00c2026c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
- 00c2026c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21260 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c48:8"]]
+ 00c21260 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2026c bytes 943e46f9
+ 00c21260 bytes 942646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-158f1cd0ff233d84195b4c475aa331a0"></a>

### [`00c20374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20374.md) → [`00c21368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21368.md) FUN_00c21368

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2138c",
      "incomplete_value": true,
      "site": "00c21390",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20398",
      "incomplete_value": true,
      "site": "00c2039c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c21398",
      "incomplete_value": true,
      "site": "00c2139c",
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
      "definition_site": "00c203a4",
      "incomplete_value": true,
      "site": "00c203a8",
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
      "definition_site": "00c213c0",
      "incomplete_value": true,
      "site": "00c213c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c203cc",
      "incomplete_value": true,
      "site": "00c203d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c2138c",
      "READ",
      [
        "storage",
        "00c9bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21390",
      "DATA",
      [
        "storage",
        "01127f48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21394",
      "READ",
      [
        "storage",
        "01127f48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2138c",
      "READ",
      [
        "storage",
        "00c9ccc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21390",
      "DATA",
      [
        "storage",
        "01128f08",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21394",
      "READ",
      [
        "storage",
        "01128f08",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c203d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20374.md#insn-00c203d0) · [`00c2038c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20374.md#insn-00c2038c) · [`00c20398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20374.md#insn-00c20398)
- 新版 [`00c213c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21368.md#insn-00c213c4) · [`00c21380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21368.md#insn-00c21380) · [`00c2138c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21368.md#insn-00c2138c)

~~~diff
- 00c203d0 ["INT_ADD", "register:40f0:8", ["const:c203d0:8", "const:4:8"]]
- 00c203d0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c213c4 ["INT_ADD", "register:40f0:8", ["const:c213c4:8", "const:4:8"]]
+ 00c213c4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c203d0 bytes f8f60094
+ 00c213c4 bytes eff60094
- 00c2038c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21380 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c2038c bytes d40300f0
+ 00c21380 bytes d40300f0
- 00c20398 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
- 00c20398 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2138c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc8:8"]]
+ 00c2138c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20398 bytes 947e46f9
+ 00c2138c bytes 946646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbf12ae83f96f67bdd5dc13a816cd295"></a>

### [`00c204a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c204a0.md) → [`00c21494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21494.md) FUN_00c21494

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c214b8",
      "incomplete_value": true,
      "site": "00c214bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c204c4",
      "incomplete_value": true,
      "site": "00c204c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "definition_site": "00c214c4",
      "incomplete_value": true,
      "site": "00c214c8",
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
      "definition_site": "00c204d0",
      "incomplete_value": true,
      "site": "00c204d4",
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
      "definition_site": "00c214ec",
      "incomplete_value": true,
      "site": "00c214f0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "00c204f8",
      "incomplete_value": true,
      "site": "00c204fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d08:8"
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
      "00c214b8",
      "READ",
      [
        "storage",
        "00c9bd08",
        null,
        "pointer"
      ]
    ],
    [
      "00c214bc",
      "DATA",
      [
        "storage",
        "01127f68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c214c0",
      "READ",
      [
        "storage",
        "01127f68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c214b8",
      "READ",
      [
        "storage",
        "00c9ccd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c214bc",
      "DATA",
      [
        "storage",
        "01128f28",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c214c0",
      "READ",
      [
        "storage",
        "01128f28",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c204fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c204a0.md#insn-00c204fc) · [`00c204b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c204a0.md#insn-00c204b8) · [`00c204c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c204a0.md#insn-00c204c4)
- 新版 [`00c214f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21494.md#insn-00c214f0) · [`00c214ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21494.md#insn-00c214ac) · [`00c214b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21494.md#insn-00c214b8)

~~~diff
- 00c204fc ["INT_ADD", "register:40f0:8", ["const:c204fc:8", "const:4:8"]]
- 00c204fc ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c214f0 ["INT_ADD", "register:40f0:8", ["const:c214f0:8", "const:4:8"]]
+ 00c214f0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c204fc bytes adf60094
+ 00c214f0 bytes a4f60094
- 00c204b8 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c214ac ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c204b8 bytes d40300f0
+ 00c214ac bytes d40300f0
- 00c204c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
- 00c204c4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c214b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
+ 00c214b8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c204c4 bytes 948646f9
+ 00c214b8 bytes 946e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ccace24229b3911e2b8e88b925680d3"></a>

### [`00c205cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c205cc.md) → [`00c215c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c215c0.md) FUN_00c215c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c215e4",
      "incomplete_value": true,
      "site": "00c215e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c205f0",
      "incomplete_value": true,
      "site": "00c205f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "definition_site": "00c215f0",
      "incomplete_value": true,
      "site": "00c215f4",
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
      "definition_site": "00c205fc",
      "incomplete_value": true,
      "site": "00c20600",
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
      "definition_site": "00c21618",
      "incomplete_value": true,
      "site": "00c2161c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c20624",
      "incomplete_value": true,
      "site": "00c20628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "00c215e4",
      "READ",
      [
        "storage",
        "00c9bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c215e8",
      "DATA",
      [
        "storage",
        "01127f58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c215ec",
      "READ",
      [
        "storage",
        "01127f58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c215e4",
      "READ",
      [
        "storage",
        "00c9cce8",
        null,
        "pointer"
      ]
    ],
    [
      "00c215e8",
      "DATA",
      [
        "storage",
        "01128f18",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c215ec",
      "READ",
      [
        "storage",
        "01128f18",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c205cc.md#insn-00c20628) · [`00c205e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c205cc.md#insn-00c205e4) · [`00c205f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c205cc.md#insn-00c205f0)
- 新版 [`00c2161c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c215c0.md#insn-00c2161c) · [`00c215d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c215c0.md#insn-00c215d8) · [`00c215e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c215c0.md#insn-00c215e4)

~~~diff
- 00c20628 ["INT_ADD", "register:40f0:8", ["const:c20628:8", "const:4:8"]]
- 00c20628 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2161c ["INT_ADD", "register:40f0:8", ["const:c2161c:8", "const:4:8"]]
+ 00c2161c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20628 bytes 62f60094
+ 00c2161c bytes 59f60094
- 00c205e4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c215d8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c205e4 bytes d40300f0
+ 00c215d8 bytes d40300f0
- 00c205f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d18:8"]]
- 00c205f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c215e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce8:8"]]
+ 00c215e4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c205f0 bytes 948e46f9
+ 00c215e4 bytes 947646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f6c2f90b98b5237c18c460ac6b31625"></a>

### [`00c206f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c206f8.md) → [`00c216ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c216ec.md) FUN_00c216ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21710",
      "incomplete_value": true,
      "site": "00c21714",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c2071c",
      "incomplete_value": true,
      "site": "00c20720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "definition_site": "00c2171c",
      "incomplete_value": true,
      "site": "00c21720",
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
      "definition_site": "00c20728",
      "incomplete_value": true,
      "site": "00c2072c",
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
      "definition_site": "00c21744",
      "incomplete_value": true,
      "site": "00c21748",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c20750",
      "incomplete_value": true,
      "site": "00c20754",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "00c21710",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c21714",
      "DATA",
      [
        "storage",
        "01127f78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21718",
      "READ",
      [
        "storage",
        "01127f78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21710",
      "READ",
      [
        "storage",
        "00c9ccf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21714",
      "DATA",
      [
        "storage",
        "01128f38",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21718",
      "READ",
      [
        "storage",
        "01128f38",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c206f8.md#insn-00c20754) · [`00c20710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c206f8.md#insn-00c20710) · [`00c2071c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c206f8.md#insn-00c2071c)
- 新版 [`00c21748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c216ec.md#insn-00c21748) · [`00c21704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c216ec.md#insn-00c21704) · [`00c21710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c216ec.md#insn-00c21710)

~~~diff
- 00c20754 ["INT_ADD", "register:40f0:8", ["const:c20754:8", "const:4:8"]]
- 00c20754 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21748 ["INT_ADD", "register:40f0:8", ["const:c21748:8", "const:4:8"]]
+ 00c21748 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20754 bytes 17f60094
+ 00c21748 bytes 0ef60094
- 00c20710 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21704 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20710 bytes d40300f0
+ 00c21704 bytes d40300f0
- 00c2071c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00c2071c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21710 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00c21710 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2071c bytes 949646f9
+ 00c21710 bytes 947e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f69a114881d3066dfea1360aef52558"></a>

### [`00c20824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20824.md) → [`00c21818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21818.md) FUN_00c21818

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2183c",
      "incomplete_value": true,
      "site": "00c21840",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c20848",
      "incomplete_value": true,
      "site": "00c2084c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00c21848",
      "incomplete_value": true,
      "site": "00c2184c",
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
      "definition_site": "00c20854",
      "incomplete_value": true,
      "site": "00c20858",
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
      "definition_site": "00c21870",
      "incomplete_value": true,
      "site": "00c21874",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c2087c",
      "incomplete_value": true,
      "site": "00c20880",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "00c2183c",
      "READ",
      [
        "storage",
        "00c9bc88",
        null,
        "pointer"
      ]
    ],
    [
      "00c21840",
      "DATA",
      [
        "storage",
        "01127f88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21844",
      "READ",
      [
        "storage",
        "01127f88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2183c",
      "READ",
      [
        "storage",
        "00c9cc58",
        null,
        "pointer"
      ]
    ],
    [
      "00c21840",
      "DATA",
      [
        "storage",
        "01128f48",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21844",
      "READ",
      [
        "storage",
        "01128f48",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20824.md#insn-00c20880) · [`00c2083c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20824.md#insn-00c2083c) · [`00c20848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20824.md#insn-00c20848)
- 新版 [`00c21874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21818.md#insn-00c21874) · [`00c21830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21818.md#insn-00c21830) · [`00c2183c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21818.md#insn-00c2183c)

~~~diff
- 00c20880 ["INT_ADD", "register:40f0:8", ["const:c20880:8", "const:4:8"]]
- 00c20880 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21874 ["INT_ADD", "register:40f0:8", ["const:c21874:8", "const:4:8"]]
+ 00c21874 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20880 bytes ccf50094
+ 00c21874 bytes c3f50094
- 00c2083c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21830 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c2083c bytes d40300f0
+ 00c21830 bytes d40300f0
- 00c20848 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00c20848 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2183c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00c2183c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20848 bytes 944646f9
+ 00c2183c bytes 942e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87bc2378651a14a1720f265b2cd55881"></a>

### [`00c20950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20950.md) → [`00c21944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21944.md) FUN_00c21944

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21968",
      "incomplete_value": true,
      "site": "00c2196c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20974",
      "incomplete_value": true,
      "site": "00c20978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00c21974",
      "incomplete_value": true,
      "site": "00c21978",
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
      "definition_site": "00c20980",
      "incomplete_value": true,
      "site": "00c20984",
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
      "definition_site": "00c2199c",
      "incomplete_value": true,
      "site": "00c219a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c209a8",
      "incomplete_value": true,
      "site": "00c209ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "00c21968",
      "READ",
      [
        "storage",
        "00c9bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00c2196c",
      "DATA",
      [
        "storage",
        "01127f98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21970",
      "READ",
      [
        "storage",
        "01127f98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21968",
      "READ",
      [
        "storage",
        "00c9cc68",
        null,
        "pointer"
      ]
    ],
    [
      "00c2196c",
      "DATA",
      [
        "storage",
        "01128f58",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21970",
      "READ",
      [
        "storage",
        "01128f58",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c209ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20950.md#insn-00c209ac) · [`00c20968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20950.md#insn-00c20968) · [`00c20974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20950.md#insn-00c20974)
- 新版 [`00c219a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21944.md#insn-00c219a0) · [`00c2195c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21944.md#insn-00c2195c) · [`00c21968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21944.md#insn-00c21968)

~~~diff
- 00c209ac ["INT_ADD", "register:40f0:8", ["const:c209ac:8", "const:4:8"]]
- 00c209ac ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c219a0 ["INT_ADD", "register:40f0:8", ["const:c219a0:8", "const:4:8"]]
+ 00c219a0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c209ac bytes 81f50094
+ 00c219a0 bytes 78f50094
- 00c20968 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c2195c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20968 bytes d40300f0
+ 00c2195c bytes d40300f0
- 00c20974 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00c20974 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21968 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00c21968 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20974 bytes 944e46f9
+ 00c21968 bytes 943646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46829395642c969dc6c3612df351470f"></a>

### [`00c20a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20a7c.md) → [`00c21a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21a70.md) FUN_00c21a70

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21a94",
      "incomplete_value": true,
      "site": "00c21a98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20aa0",
      "incomplete_value": true,
      "site": "00c20aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "definition_site": "00c21aa0",
      "incomplete_value": true,
      "site": "00c21aa4",
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
      "definition_site": "00c20aac",
      "incomplete_value": true,
      "site": "00c20ab0",
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
      "definition_site": "00c21ac8",
      "incomplete_value": true,
      "site": "00c21acc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20ad4",
      "incomplete_value": true,
      "site": "00c20ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "00c21a94",
      "READ",
      [
        "storage",
        "00c9bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c21a98",
      "DATA",
      [
        "storage",
        "01127cf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21a9c",
      "READ",
      [
        "storage",
        "01127cf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21a94",
      "READ",
      [
        "storage",
        "00c9cc80",
        null,
        "pointer"
      ]
    ],
    [
      "00c21a98",
      "DATA",
      [
        "storage",
        "01128cb8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21a9c",
      "READ",
      [
        "storage",
        "01128cb8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20a7c.md#insn-00c20ad8) · [`00c20a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20a7c.md#insn-00c20a94) · [`00c20aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20a7c.md#insn-00c20aa0)
- 新版 [`00c21acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21a70.md#insn-00c21acc) · [`00c21a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21a70.md#insn-00c21a88) · [`00c21a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21a70.md#insn-00c21a94)

~~~diff
- 00c20ad8 ["INT_ADD", "register:40f0:8", ["const:c20ad8:8", "const:4:8"]]
- 00c20ad8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21acc ["INT_ADD", "register:40f0:8", ["const:c21acc:8", "const:4:8"]]
+ 00c21acc ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20ad8 bytes 36f50094
+ 00c21acc bytes 2df50094
- 00c20a94 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21a88 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20a94 bytes d40300f0
+ 00c21a88 bytes d40300f0
- 00c20aa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
- 00c20aa0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c80:8"]]
+ 00c21a94 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20aa0 bytes 945a46f9
+ 00c21a94 bytes 944246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f66608071ec8b8b92c2c5ca4ca33b03"></a>

### [`00c20ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20ba8.md) → [`00c21b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21b9c.md) FUN_00c21b9c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9a0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 1件 [`00c5f970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f970.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21bcc",
      "incomplete_value": true,
      "site": "00c21bcc",
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
      "definition_site": "00c20bd8",
      "incomplete_value": true,
      "site": "00c20bd8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c21bbc",
      "READ",
      [
        "storage",
        "00c9be68",
        null,
        "pointer"
      ]
    ],
    [
      "00c21bcc",
      "DATA",
      [
        "storage",
        "00c954d0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c21bbc",
      "READ",
      [
        "storage",
        "00c9ce38",
        null,
        "pointer"
      ]
    ],
    [
      "00c21bcc",
      "DATA",
      [
        "storage",
        "00c964a0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20ba8.md#insn-00c20bbc) · [`00c20bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20ba8.md#insn-00c20bc8) · [`00c20bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20ba8.md#insn-00c20bcc)
- 新版 [`00c21bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21b9c.md#insn-00c21bb0) · [`00c21bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21b9c.md#insn-00c21bbc)

~~~diff
- 00c20bbc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c21bb0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c20bbc bytes c80300f0
+ 00c21bb0 bytes c80300f0
- 00c20bc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
- 00c20bc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21bbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
+ 00c21bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20bc8 bytes 083547f9
+ 00c21bbc bytes 081d47f9
- 00c20bcc ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20bcc bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdc16f94c42d8c561cedfb55acd514f7"></a>

### [`00c20c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20c8c.md) → [`00c21c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21c80.md) FUN_00c21c80

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21ca4",
      "incomplete_value": true,
      "site": "00c21ca8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20cb0",
      "incomplete_value": true,
      "site": "00c20cb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "definition_site": "00c21cb0",
      "incomplete_value": true,
      "site": "00c21cb4",
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
      "definition_site": "00c20cbc",
      "incomplete_value": true,
      "site": "00c20cc0",
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
      "definition_site": "00c21cd8",
      "incomplete_value": true,
      "site": "00c21cdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20ce4",
      "incomplete_value": true,
      "site": "00c20ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "00c21ca4",
      "READ",
      [
        "storage",
        "00c9bca8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21ca8",
      "DATA",
      [
        "storage",
        "01127d08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21cac",
      "READ",
      [
        "storage",
        "01127d08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21ca4",
      "READ",
      [
        "storage",
        "00c9cc78",
        null,
        "pointer"
      ]
    ],
    [
      "00c21ca8",
      "DATA",
      [
        "storage",
        "01128cc8",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21cac",
      "READ",
      [
        "storage",
        "01128cc8",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20c8c.md#insn-00c20ce8) · [`00c20ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20c8c.md#insn-00c20ca4) · [`00c20cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20c8c.md#insn-00c20cb0)
- 新版 [`00c21cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21c80.md#insn-00c21cdc) · [`00c21c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21c80.md#insn-00c21c98) · [`00c21ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21c80.md#insn-00c21ca4)

~~~diff
- 00c20ce8 ["INT_ADD", "register:40f0:8", ["const:c20ce8:8", "const:4:8"]]
- 00c20ce8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21cdc ["INT_ADD", "register:40f0:8", ["const:c21cdc:8", "const:4:8"]]
+ 00c21cdc ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20ce8 bytes b2f40094
+ 00c21cdc bytes a9f40094
- 00c20ca4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21c98 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20ca4 bytes d40300f0
+ 00c21c98 bytes d40300f0
- 00c20cb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00c20cb0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21ca4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00c21ca4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20cb0 bytes 945646f9
+ 00c21ca4 bytes 943e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2539d4db6849137bd9c470676b6f5cf5"></a>

### [`00c20db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20db8.md) → [`00c21dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21dac.md) FUN_00c21dac

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 1件 [`00c5e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9b0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 1件 [`00c5f980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f980.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21ddc",
      "incomplete_value": true,
      "site": "00c21ddc",
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
      "definition_site": "00c20de8",
      "incomplete_value": true,
      "site": "00c20de8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c21dcc",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00c21ddc",
      "DATA",
      [
        "storage",
        "00c95558",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c21dcc",
      "READ",
      [
        "storage",
        "00c9ce40",
        null,
        "pointer"
      ]
    ],
    [
      "00c21ddc",
      "DATA",
      [
        "storage",
        "00c96528",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20db8.md#insn-00c20dcc) · [`00c20dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20db8.md#insn-00c20dd8) · [`00c20ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20db8.md#insn-00c20ddc)
- 新版 [`00c21dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21dac.md#insn-00c21dc0) · [`00c21dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21dac.md#insn-00c21dcc)

~~~diff
- 00c20dcc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c21dc0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c20dcc bytes c80300f0
+ 00c21dc0 bytes c80300f0
- 00c20dd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00c20dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21dcc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e40:8"]]
+ 00c21dcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20dd8 bytes 083947f9
+ 00c21dcc bytes 082147f9
- 00c20ddc ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20ddc bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1e54bea4f9b2c8af06353fc1bc2ed0f"></a>

### [`00c20e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20e9c.md) → [`00c21e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21e90.md) FUN_00c21e90

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21eb4",
      "incomplete_value": true,
      "site": "00c21eb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20ec0",
      "incomplete_value": true,
      "site": "00c20ec4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00c21ee8",
      "incomplete_value": true,
      "site": "00c21eec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20ef4",
      "incomplete_value": true,
      "site": "00c20ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00c21edc",
      "incomplete_value": false,
      "site": "00c21eec",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c20ee8",
      "incomplete_value": false,
      "site": "00c20ef8",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c21eb4",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c21eb8",
      "DATA",
      [
        "storage",
        "01127d18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21ebc",
      "READ",
      [
        "storage",
        "01127d18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21eb4",
      "READ",
      [
        "storage",
        "00c9cc90",
        null,
        "pointer"
      ]
    ],
    [
      "00c21eb8",
      "DATA",
      [
        "storage",
        "01128cd8",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21ebc",
      "READ",
      [
        "storage",
        "01128cd8",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20e9c.md#insn-00c20ef8) · [`00c20eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20e9c.md#insn-00c20eb4) · [`00c20ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20e9c.md#insn-00c20ec0)
- 新版 [`00c21eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21e90.md#insn-00c21eec) · [`00c21ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21e90.md#insn-00c21ea8) · [`00c21eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21e90.md#insn-00c21eb4)

~~~diff
- 00c20ef8 ["INT_ADD", "register:40f0:8", ["const:c20ef8:8", "const:4:8"]]
- 00c20ef8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c21eec ["INT_ADD", "register:40f0:8", ["const:c21eec:8", "const:4:8"]]
+ 00c21eec ["CALL", null, ["callee:00c5ef80:8"]]
- 00c20ef8 bytes 2ef40094
+ 00c21eec bytes 25f40094
- 00c20eb4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c21ea8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c20eb4 bytes d40300f0
+ 00c21ea8 bytes d40300f0
- 00c20ec0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00c20ec0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21eb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
+ 00c21eb4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20ec0 bytes 946246f9
+ 00c21eb4 bytes 944a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-803a91c0c469a010c573799cc20e5c98"></a>

### [`00c20fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20fc8.md) → [`00c21fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21fbc.md) FUN_00c21fbc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 1件 [`00c5e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9c0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 1件 [`00c5f990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f990.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21fec",
      "incomplete_value": true,
      "site": "00c21fec",
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
      "definition_site": "00c20ff8",
      "incomplete_value": true,
      "site": "00c20ff8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c21fdc",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c21fec",
      "DATA",
      [
        "storage",
        "00c955e0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c21fdc",
      "READ",
      [
        "storage",
        "00c9ce48",
        null,
        "pointer"
      ]
    ],
    [
      "00c21fec",
      "DATA",
      [
        "storage",
        "00c965b0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20fc8.md#insn-00c20fdc) · [`00c20fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20fc8.md#insn-00c20fe8) · [`00c20fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c20/00c20fc8.md#insn-00c20fec)
- 新版 [`00c21fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21fbc.md#insn-00c21fd0) · [`00c21fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c21/00c21fbc.md#insn-00c21fdc)

~~~diff
- 00c20fdc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c21fd0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c20fdc bytes c80300f0
+ 00c21fd0 bytes c80300f0
- 00c20fe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
- 00c20fe8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21fdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
+ 00c21fdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20fe8 bytes 083d47f9
+ 00c21fdc bytes 082547f9
- 00c20fec ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20fec bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-591b3f041b52359ae333215aa53b9a1c"></a>

### [`00c210ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c210ac.md) → [`00c220a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c220a0.md) FUN_00c220a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c220c4",
      "incomplete_value": true,
      "site": "00c220c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c210d0",
      "incomplete_value": true,
      "site": "00c210d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "definition_site": "00c220d0",
      "incomplete_value": true,
      "site": "00c220d4",
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
      "definition_site": "00c210dc",
      "incomplete_value": true,
      "site": "00c210e0",
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
      "definition_site": "00c220f8",
      "incomplete_value": true,
      "site": "00c220fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21104",
      "incomplete_value": true,
      "site": "00c21108",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "00c220c4",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c220c8",
      "DATA",
      [
        "storage",
        "01127d28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c220cc",
      "READ",
      [
        "storage",
        "01127d28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c220c4",
      "READ",
      [
        "storage",
        "00c9cc88",
        null,
        "pointer"
      ]
    ],
    [
      "00c220c8",
      "DATA",
      [
        "storage",
        "01128ce8",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c220cc",
      "READ",
      [
        "storage",
        "01128ce8",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c210ac.md#insn-00c21108) · [`00c210c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c210ac.md#insn-00c210c4) · [`00c210d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c210ac.md#insn-00c210d0)
- 新版 [`00c220fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c220a0.md#insn-00c220fc) · [`00c220b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c220a0.md#insn-00c220b8) · [`00c220c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c220a0.md#insn-00c220c4)

~~~diff
- 00c21108 ["INT_ADD", "register:40f0:8", ["const:c21108:8", "const:4:8"]]
- 00c21108 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c220fc ["INT_ADD", "register:40f0:8", ["const:c220fc:8", "const:4:8"]]
+ 00c220fc ["CALL", null, ["callee:00c5ef80:8"]]
- 00c21108 bytes aaf30094
+ 00c220fc bytes a1f30094
- 00c210c4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c220b8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c210c4 bytes d40300d0
+ 00c220b8 bytes d40300d0
- 00c210d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00c210d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c220c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00c220c4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c210d0 bytes 945e46f9
+ 00c220c4 bytes 944646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef0f1f2ca3156baec177538eaccb0dd2"></a>

### [`00c211d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c211d8.md) → [`00c221cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c221cc.md) FUN_00c221cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 1件 [`00c5e9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9d0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 1件 [`00c5f9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f9a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c221fc",
      "incomplete_value": true,
      "site": "00c221fc",
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
      "definition_site": "00c21208",
      "incomplete_value": true,
      "site": "00c21208",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c221ec",
      "READ",
      [
        "storage",
        "00c9be80",
        null,
        "pointer"
      ]
    ],
    [
      "00c221fc",
      "DATA",
      [
        "storage",
        "00c95668",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c221ec",
      "READ",
      [
        "storage",
        "00c9ce50",
        null,
        "pointer"
      ]
    ],
    [
      "00c221fc",
      "DATA",
      [
        "storage",
        "00c96638",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c211ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c211d8.md#insn-00c211ec) · [`00c211f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c211d8.md#insn-00c211f8) · [`00c211fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c211d8.md#insn-00c211fc)
- 新版 [`00c221e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c221cc.md#insn-00c221e0) · [`00c221ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c221cc.md#insn-00c221ec)

~~~diff
- 00c211ec ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c221e0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c211ec bytes c80300d0
+ 00c221e0 bytes c80300d0
- 00c211f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
- 00c211f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c221ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
+ 00c221ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c211f8 bytes 084147f9
+ 00c221ec bytes 082947f9
- 00c211fc ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c211fc bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d63845136fa6b562840e2e737eb5dd"></a>

### [`00c212bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c212bc.md) → [`00c222b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c222b0.md) FUN_00c222b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c222d4",
      "incomplete_value": true,
      "site": "00c222d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c212e0",
      "incomplete_value": true,
      "site": "00c212e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
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
      "definition_site": "00c222e0",
      "incomplete_value": true,
      "site": "00c222e4",
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
      "definition_site": "00c212ec",
      "incomplete_value": true,
      "site": "00c212f0",
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
      "definition_site": "00c22308",
      "incomplete_value": true,
      "site": "00c2230c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c21314",
      "incomplete_value": true,
      "site": "00c21318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
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
      "00c222d4",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c222d8",
      "DATA",
      [
        "storage",
        "01127cb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c222dc",
      "READ",
      [
        "storage",
        "01127cb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c222d4",
      "READ",
      [
        "storage",
        "00c9c390",
        null,
        "pointer"
      ]
    ],
    [
      "00c222d8",
      "DATA",
      [
        "storage",
        "01128c78",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c222dc",
      "READ",
      [
        "storage",
        "01128c78",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c212bc.md#insn-00c21318) · [`00c212d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c212bc.md#insn-00c212d4) · [`00c212e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c212bc.md#insn-00c212e0)
- 新版 [`00c2230c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c222b0.md#insn-00c2230c) · [`00c222c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c222b0.md#insn-00c222c8) · [`00c222d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c222b0.md#insn-00c222d4)

~~~diff
- 00c21318 ["INT_ADD", "register:40f0:8", ["const:c21318:8", "const:4:8"]]
- 00c21318 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2230c ["INT_ADD", "register:40f0:8", ["const:c2230c:8", "const:4:8"]]
+ 00c2230c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c21318 bytes 26f30094
+ 00c2230c bytes 1df30094
- 00c212d4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c222c8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c212d4 bytes d40300d0
+ 00c222c8 bytes d40300d0
- 00c212e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c0:8"]]
- 00c212e0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c222d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00c222d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c212e0 bytes 94e241f9
+ 00c222d4 bytes 94ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3863a7ed2b26934476164a18c379cde"></a>

### [`00c213e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c213e8.md) → [`00c223dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c223dc.md) FUN_00c223dc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c22434",
      "incomplete_value": true,
      "site": "00c22438",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21440",
      "incomplete_value": true,
      "site": "00c21444",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "definition_site": "00c22428",
      "incomplete_value": false,
      "site": "00c22438",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c21434",
      "incomplete_value": false,
      "site": "00c21444",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c22400",
      "READ",
      [
        "storage",
        "00c9bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c22404",
      "DATA",
      [
        "storage",
        "01127cc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22408",
      "READ",
      [
        "storage",
        "01127cc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22400",
      "READ",
      [
        "storage",
        "00c9cd90",
        null,
        "pointer"
      ]
    ],
    [
      "00c22404",
      "DATA",
      [
        "storage",
        "01128c88",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22408",
      "READ",
      [
        "storage",
        "01128c88",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c213e8.md#insn-00c21444) · [`00c21400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c213e8.md#insn-00c21400) · [`00c2140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c213e8.md#insn-00c2140c)
- 新版 [`00c22438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c223dc.md#insn-00c22438) · [`00c223f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c223dc.md#insn-00c223f4) · [`00c22400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c223dc.md#insn-00c22400)

~~~diff
- 00c21444 ["INT_ADD", "register:40f0:8", ["const:c21444:8", "const:4:8"]]
- 00c21444 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c22438 ["INT_ADD", "register:40f0:8", ["const:c22438:8", "const:4:8"]]
+ 00c22438 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c21444 bytes dbf20094
+ 00c22438 bytes d2f20094
- 00c21400 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c223f4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c21400 bytes d40300d0
+ 00c223f4 bytes d40300d0
- 00c2140c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00c2140c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22400 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00c22400 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2140c bytes 94e246f9
+ 00c22400 bytes 94ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535872e24fe642dca95d656760bd9096"></a>

### [`00c21514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21514.md) → [`00c22508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22508.md) FUN_00c22508

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2252c",
      "incomplete_value": true,
      "site": "00c22530",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:398:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21538",
      "incomplete_value": true,
      "site": "00c2153c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
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
      "definition_site": "00c22538",
      "incomplete_value": true,
      "site": "00c2253c",
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
      "definition_site": "00c21544",
      "incomplete_value": true,
      "site": "00c21548",
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
      "definition_site": "00c22560",
      "incomplete_value": true,
      "site": "00c22564",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:398:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2156c",
      "incomplete_value": true,
      "site": "00c21570",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
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
      "00c2252c",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c22530",
      "DATA",
      [
        "storage",
        "01127cd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22534",
      "READ",
      [
        "storage",
        "01127cd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2252c",
      "READ",
      [
        "storage",
        "00c9c398",
        null,
        "pointer"
      ]
    ],
    [
      "00c22530",
      "DATA",
      [
        "storage",
        "01128c98",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22534",
      "READ",
      [
        "storage",
        "01128c98",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21514.md#insn-00c21570) · [`00c2152c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21514.md#insn-00c2152c) · [`00c21538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21514.md#insn-00c21538)
- 新版 [`00c22564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22508.md#insn-00c22564) · [`00c22520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22508.md#insn-00c22520) · [`00c2252c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22508.md#insn-00c2252c)

~~~diff
- 00c21570 ["INT_ADD", "register:40f0:8", ["const:c21570:8", "const:4:8"]]
- 00c21570 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c22564 ["INT_ADD", "register:40f0:8", ["const:c22564:8", "const:4:8"]]
+ 00c22564 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c21570 bytes 90f20094
+ 00c22564 bytes 87f20094
- 00c2152c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c22520 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c2152c bytes d40300d0
+ 00c22520 bytes d40300d0
- 00c21538 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00c21538 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2252c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:398:8"]]
+ 00c2252c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c21538 bytes 94e641f9
+ 00c2252c bytes 94ce41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb36fd6cc0bba975aabf354b16e54bb"></a>

### [`00c21640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21640.md) → [`00c22634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22634.md) FUN_00c22634

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22658",
      "incomplete_value": true,
      "site": "00c2265c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21664",
      "incomplete_value": true,
      "site": "00c21668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "definition_site": "00c22664",
      "incomplete_value": true,
      "site": "00c22668",
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
      "definition_site": "00c21670",
      "incomplete_value": true,
      "site": "00c21674",
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
      "definition_site": "00c2268c",
      "incomplete_value": true,
      "site": "00c22690",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21698",
      "incomplete_value": true,
      "site": "00c2169c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "00c22658",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2265c",
      "DATA",
      [
        "storage",
        "01127ce8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22660",
      "READ",
      [
        "storage",
        "01127ce8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22658",
      "READ",
      [
        "storage",
        "00c9cdb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2265c",
      "DATA",
      [
        "storage",
        "01128ca8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22660",
      "READ",
      [
        "storage",
        "01128ca8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2169c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21640.md#insn-00c2169c) · [`00c21658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21640.md#insn-00c21658) · [`00c21664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21640.md#insn-00c21664)
- 新版 [`00c22690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22634.md#insn-00c22690) · [`00c2264c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22634.md#insn-00c2264c) · [`00c22658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22634.md#insn-00c22658)

~~~diff
- 00c2169c ["INT_ADD", "register:40f0:8", ["const:c2169c:8", "const:4:8"]]
- 00c2169c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c22690 ["INT_ADD", "register:40f0:8", ["const:c22690:8", "const:4:8"]]
+ 00c22690 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c2169c bytes 45f20094
+ 00c22690 bytes 3cf20094
- 00c21658 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c2264c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c21658 bytes d40300d0
+ 00c2264c bytes d40300d0
- 00c21664 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:de0:8"]]
- 00c21664 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22658 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00c22658 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c21664 bytes 94f246f9
+ 00c22658 bytes 94da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f41ad74ac058ef272b9350c798b0af3"></a>

### [`00c2176c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c2176c.md) → [`00c22760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22760.md) FUN_00c22760

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22784",
      "incomplete_value": true,
      "site": "00c22788",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21790",
      "incomplete_value": true,
      "site": "00c21794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "definition_site": "00c227b8",
      "incomplete_value": true,
      "site": "00c227bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c217c4",
      "incomplete_value": true,
      "site": "00c217c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "definition_site": "00c227ac",
      "incomplete_value": false,
      "site": "00c227bc",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c217b8",
      "incomplete_value": false,
      "site": "00c217c8",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c22784",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c22788",
      "DATA",
      [
        "storage",
        "01127d78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2278c",
      "READ",
      [
        "storage",
        "01127d78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22784",
      "READ",
      [
        "storage",
        "00c9cdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c22788",
      "DATA",
      [
        "storage",
        "01128d38",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2278c",
      "READ",
      [
        "storage",
        "01128d38",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c217c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c2176c.md#insn-00c217c8) · [`00c21784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c2176c.md#insn-00c21784) · [`00c21790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c2176c.md#insn-00c21790)
- 新版 [`00c227bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22760.md#insn-00c227bc) · [`00c22778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22760.md#insn-00c22778) · [`00c22784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c22760.md#insn-00c22784)

~~~diff
- 00c217c8 ["INT_ADD", "register:40f0:8", ["const:c217c8:8", "const:4:8"]]
- 00c217c8 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c227bc ["INT_ADD", "register:40f0:8", ["const:c227bc:8", "const:4:8"]]
+ 00c227bc ["CALL", null, ["callee:00c5ef80:8"]]
- 00c217c8 bytes faf10094
+ 00c227bc bytes f1f10094
- 00c21784 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c22778 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c21784 bytes d40300d0
+ 00c22778 bytes d40300d0
- 00c21790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00c21790 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22784 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
+ 00c22784 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c21790 bytes 94fa46f9
+ 00c22784 bytes 94e246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c27efd15a38a4c9f47006d64c6861f7e"></a>

### [`00c21898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21898.md) → [`00c2288c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c2288c.md) FUN_00c2288c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) · 呼出先 5件 [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md)
- 新版 呼出元 2件 [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) · 呼出先 5件 [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c228b0",
      "incomplete_value": true,
      "site": "00c228b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c218bc",
      "incomplete_value": true,
      "site": "00c218c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "definition_site": "00c228bc",
      "incomplete_value": true,
      "site": "00c228c0",
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
      "definition_site": "00c218c8",
      "incomplete_value": true,
      "site": "00c218cc",
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
      "definition_site": "00c228e4",
      "incomplete_value": true,
      "site": "00c228e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c218f0",
      "incomplete_value": true,
      "site": "00c218f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "00c228b0",
      "READ",
      [
        "storage",
        "00c9be00",
        null,
        "pointer"
      ]
    ],
    [
      "00c228b4",
      "DATA",
      [
        "storage",
        "01127d88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c228b8",
      "READ",
      [
        "storage",
        "01127d88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c228b0",
      "READ",
      [
        "storage",
        "00c9cdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c228b4",
      "DATA",
      [
        "storage",
        "01128d48",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c228b8",
      "READ",
      [
        "storage",
        "01128d48",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c218f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21898.md#insn-00c218f4) · [`00c218b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21898.md#insn-00c218b0) · [`00c218bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c21898.md#insn-00c218bc)
- 新版 [`00c228e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c2288c.md#insn-00c228e8) · [`00c228a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c2288c.md#insn-00c228a4) · [`00c228b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c2288c.md#insn-00c228b0)

~~~diff
- 00c218f4 ["INT_ADD", "register:40f0:8", ["const:c218f4:8", "const:4:8"]]
- 00c218f4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c228e8 ["INT_ADD", "register:40f0:8", ["const:c228e8:8", "const:4:8"]]
+ 00c228e8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c218f4 bytes aff10094
+ 00c228e8 bytes a6f10094
- 00c218b0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c228a4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c218b0 bytes d40300d0
+ 00c228a4 bytes d40300d0
- 00c218bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00c218bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c228b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00c228b0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c218bc bytes 940247f9
+ 00c228b0 bytes 94ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f410005df88a1984c594d8df540ba64c"></a>

### [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) → [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) FUN_00c229b8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c2513c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2513c.md) [`00c2528c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2528c.md) · 呼出先 40件 [`00c1d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d5fc.md) [`00c1fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fc6c.md) [`00c1fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md) [`00c1fec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fec4.md) [`00c1fff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fff0.md)
- 新版 呼出元 2件 [`00c26130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26130.md) [`00c26280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26280.md) · 呼出先 40件 [`00c1e5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e5f0.md) [`00c20c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20c60.md) [`00c20d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20d8c.md) [`00c20eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20eb8.md) [`00c20fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c20fe4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.29% / 新版 88.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c229ec",
      "incomplete_value": false,
      "site": "00c229ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c94000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c219f8",
      "incomplete_value": false,
      "site": "00c219f8",
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
            "const:790:8"
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
      "definition_site": "00c22b7c",
      "incomplete_value": true,
      "site": "00c22b7c",
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
      "definition_site": "00c21b88",
      "incomplete_value": true,
      "site": "00c21b88",
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
      "definition_site": "00c22bb4",
      "incomplete_value": true,
      "site": "00c22bb8",
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
      "definition_site": "00c21bc0",
      "incomplete_value": true,
      "site": "00c21bc4",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c229ec",
      "DATA",
      [
        "storage",
        "00c93790",
        null,
        "undefined *"
      ]
    ],
    [
      "00c22b74",
      "READ",
      [
        "storage",
        "00c9be08",
        null,
        "pointer"
      ]
    ],
    [
      "00c22b7c",
      "DATA",
      [
        "storage",
        "00c95aa0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00c229ec",
      "DATA",
      [
        "storage",
        "00c94760",
        null,
        "undefined *"
      ]
    ],
    [
      "00c22b74",
      "READ",
      [
        "storage",
        "00c9cdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c22b7c",
      "DATA",
      [
        "storage",
        "00c96a70",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c219e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md#insn-00c219e8) · [`00c219ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md#insn-00c219ec) · [`00c21a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md#insn-00c21a6c)
- 新版 [`00c229dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md#insn-00c229dc) · [`00c229e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md#insn-00c229e0) · [`00c22a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md#insn-00c22a60)

~~~diff
- 00c219e8 ["COPY", "register:4048:8", ["const:c93000:8"]]
+ 00c229dc ["COPY", "register:4048:8", ["const:c94000:8"]]
- 00c219e8 bytes 890300d0
+ 00c229dc bytes 890300d0
- 00c219ec ["COPY", "tmp:0:8", ["const:790:8"]]
- 00c219ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c219ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c219ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c229e0 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00c229e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c229e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c229e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c219ec bytes 29411e91
+ 00c229e0 bytes 29811d91
- 00c21a6c ["INT_ADD", "register:40f0:8", ["const:c21a6c:8", "const:4:8"]]
- 00c21a6c ["CALL", null, ["callee:00c1e5f0:8"]]
+ 00c22a60 ["INT_ADD", "register:40f0:8", ["const:c22a60:8", "const:4:8"]]
+ 00c22a60 ["CALL", null, ["callee:00c1e5f0:8"]]
- 00c21a6c bytes e4eeff97
+ 00c22a60 bytes e4eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed029e6f8698f41e419be3e954438742"></a>

### [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) → [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) FUN_00c23008

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c25304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25304.md) · 呼出先 33件 [`00c1d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1d/00c1d5fc.md) [`00c22378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22378.md) [`00c224bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c224bc.md) [`00c22600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22600.md) [`00c22744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22744.md)
- 新版 呼出元 1件 [`00c262f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c262f8.md) · 呼出先 33件 [`00c1e5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c1e/00c1e5f0.md) [`00c2336c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2336c.md) [`00c234b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c234b0.md) [`00c235f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c235f4.md) [`00c23738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23738.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23038",
      "incomplete_value": false,
      "site": "00c23038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c94000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22044",
      "incomplete_value": false,
      "site": "00c22044",
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
            "const:790:8"
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
      "00c23038",
      "DATA",
      [
        "storage",
        "00c93790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c23038",
      "DATA",
      [
        "storage",
        "00c94760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md#insn-00c22034) · [`00c22038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md#insn-00c22038) · [`00c220b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md#insn-00c220b8)
- 新版 [`00c23028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md#insn-00c23028) · [`00c2302c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md#insn-00c2302c) · [`00c230ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md#insn-00c230ac)

~~~diff
- 00c22034 ["COPY", "register:4048:8", ["const:c93000:8"]]
+ 00c23028 ["COPY", "register:4048:8", ["const:c94000:8"]]
- 00c22034 bytes 890300b0
+ 00c23028 bytes 890300b0
- 00c22038 ["COPY", "tmp:0:8", ["const:790:8"]]
- 00c22038 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c22038 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c22038 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c2302c ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00c2302c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2302c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c2302c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c22038 bytes 29411e91
+ 00c2302c bytes 29811d91
- 00c220b8 ["INT_ADD", "register:40f0:8", ["const:c220b8:8", "const:4:8"]]
- 00c220b8 ["CALL", null, ["callee:00c1e5f0:8"]]
+ 00c230ac ["INT_ADD", "register:40f0:8", ["const:c230ac:8", "const:4:8"]]
+ 00c230ac ["CALL", null, ["callee:00c1e5f0:8"]]
- 00c220b8 bytes 51edff97
+ 00c230ac bytes 51edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6eccaf0adfe59fa80c60e074ccaf04"></a>

### [`00c22378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22378.md) → [`00c2336c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2336c.md) FUN_00c2336c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23390",
      "incomplete_value": true,
      "site": "00c23394",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c2239c",
      "incomplete_value": true,
      "site": "00c223a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:448:8"
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
      "definition_site": "00c2339c",
      "incomplete_value": true,
      "site": "00c233a0",
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
      "definition_site": "00c223a8",
      "incomplete_value": true,
      "site": "00c223ac",
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
      "definition_site": "00c233c4",
      "incomplete_value": true,
      "site": "00c233c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c223d0",
      "incomplete_value": true,
      "site": "00c223d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:448:8"
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
      "00c23390",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c23394",
      "DATA",
      [
        "storage",
        "01127c58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23398",
      "READ",
      [
        "storage",
        "01127c58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23390",
      "READ",
      [
        "storage",
        "00c9c418",
        null,
        "pointer"
      ]
    ],
    [
      "00c23394",
      "DATA",
      [
        "storage",
        "01128c18",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23398",
      "READ",
      [
        "storage",
        "01128c18",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c223d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22378.md#insn-00c223d4) · [`00c22390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22378.md#insn-00c22390) · [`00c2239c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22378.md#insn-00c2239c)
- 新版 [`00c233c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2336c.md#insn-00c233c8) · [`00c23384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2336c.md#insn-00c23384) · [`00c23390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2336c.md#insn-00c23390)

~~~diff
- 00c223d4 ["INT_ADD", "register:40f0:8", ["const:c223d4:8", "const:4:8"]]
- 00c223d4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c233c8 ["INT_ADD", "register:40f0:8", ["const:c233c8:8", "const:4:8"]]
+ 00c233c8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c223d4 bytes f7ee0094
+ 00c233c8 bytes eeee0094
- 00c22390 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23384 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c22390 bytes d40300b0
+ 00c23384 bytes d40300b0
- 00c2239c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:448:8"]]
- 00c2239c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00c23390 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2239c bytes 942642f9
+ 00c23390 bytes 940e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4e35e616e068b4e38fdd0de5a13479"></a>

### [`00c224bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c224bc.md) → [`00c234b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c234b0.md) FUN_00c234b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c234d4",
      "incomplete_value": true,
      "site": "00c234d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
    "old": {
      "definition_site": "00c224e0",
      "incomplete_value": true,
      "site": "00c224e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c234e0",
      "incomplete_value": true,
      "site": "00c234e4",
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
      "definition_site": "00c224ec",
      "incomplete_value": true,
      "site": "00c224f0",
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
      "definition_site": "00c23508",
      "incomplete_value": true,
      "site": "00c2350c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c22514",
      "incomplete_value": true,
      "site": "00c22518",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
      "00c234d4",
      "READ",
      [
        "storage",
        "00c9bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c234d8",
      "DATA",
      [
        "storage",
        "01127c68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c234dc",
      "READ",
      [
        "storage",
        "01127c68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c234d4",
      "READ",
      [
        "storage",
        "00c9cca8",
        null,
        "pointer"
      ]
    ],
    [
      "00c234d8",
      "DATA",
      [
        "storage",
        "01128c28",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c234dc",
      "READ",
      [
        "storage",
        "01128c28",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c224bc.md#insn-00c22518) · [`00c224d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c224bc.md#insn-00c224d4) · [`00c224e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c224bc.md#insn-00c224e0)
- 新版 [`00c2350c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c234b0.md#insn-00c2350c) · [`00c234c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c234b0.md#insn-00c234c8) · [`00c234d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c234b0.md#insn-00c234d4)

~~~diff
- 00c22518 ["INT_ADD", "register:40f0:8", ["const:c22518:8", "const:4:8"]]
- 00c22518 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2350c ["INT_ADD", "register:40f0:8", ["const:c2350c:8", "const:4:8"]]
+ 00c2350c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c22518 bytes a6ee0094
+ 00c2350c bytes 9dee0094
- 00c224d4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c234c8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c224d4 bytes d40300b0
+ 00c234c8 bytes d40300b0
- 00c224e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
- 00c224e0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c234d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00c234d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c224e0 bytes 946e46f9
+ 00c234d4 bytes 945646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4334d5610e28bb5c36ef667e945fae0"></a>

### [`00c22600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22600.md) → [`00c235f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c235f4.md) FUN_00c235f4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23618",
      "incomplete_value": true,
      "site": "00c2361c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22624",
      "incomplete_value": true,
      "site": "00c22628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
      "definition_site": "00c23624",
      "incomplete_value": true,
      "site": "00c23628",
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
      "definition_site": "00c22630",
      "incomplete_value": true,
      "site": "00c22634",
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
      "definition_site": "00c2364c",
      "incomplete_value": true,
      "site": "00c23650",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22658",
      "incomplete_value": true,
      "site": "00c2265c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d00:8"
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
      "00c23618",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00c2361c",
      "DATA",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23620",
      "READ",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23618",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2361c",
      "DATA",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23620",
      "READ",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2265c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22600.md#insn-00c2265c) · [`00c22618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22600.md#insn-00c22618) · [`00c22624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22600.md#insn-00c22624)
- 新版 [`00c23650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c235f4.md#insn-00c23650) · [`00c2360c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c235f4.md#insn-00c2360c) · [`00c23618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c235f4.md#insn-00c23618)

~~~diff
- 00c2265c ["INT_ADD", "register:40f0:8", ["const:c2265c:8", "const:4:8"]]
- 00c2265c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23650 ["INT_ADD", "register:40f0:8", ["const:c23650:8", "const:4:8"]]
+ 00c23650 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c2265c bytes 55ee0094
+ 00c23650 bytes 4cee0094
- 00c22618 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c2360c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c22618 bytes d4030090
+ 00c2360c bytes d4030090
- 00c22624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
- 00c22624 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23618 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00c23618 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22624 bytes 948246f9
+ 00c23618 bytes 946a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1e52f37339ea7a8f1e197f613a61614"></a>

### [`00c22744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22744.md) → [`00c23738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23738.md) FUN_00c23738

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2375c",
      "incomplete_value": true,
      "site": "00c23760",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22768",
      "incomplete_value": true,
      "site": "00c2276c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "definition_site": "00c23768",
      "incomplete_value": true,
      "site": "00c2376c",
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
      "definition_site": "00c22774",
      "incomplete_value": true,
      "site": "00c22778",
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
      "definition_site": "00c23790",
      "incomplete_value": true,
      "site": "00c23794",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c2279c",
      "incomplete_value": true,
      "site": "00c227a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00c2375c",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00c23760",
      "DATA",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23764",
      "READ",
      [
        "storage",
        "01127f08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2375c",
      "READ",
      [
        "storage",
        "00c9cbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c23760",
      "DATA",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23764",
      "READ",
      [
        "storage",
        "01128ec8",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c227a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22744.md#insn-00c227a0) · [`00c2275c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22744.md#insn-00c2275c) · [`00c22768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22744.md#insn-00c22768)
- 新版 [`00c23794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23738.md#insn-00c23794) · [`00c23750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23738.md#insn-00c23750) · [`00c2375c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23738.md#insn-00c2375c)

~~~diff
- 00c227a0 ["INT_ADD", "register:40f0:8", ["const:c227a0:8", "const:4:8"]]
- 00c227a0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23794 ["INT_ADD", "register:40f0:8", ["const:c23794:8", "const:4:8"]]
+ 00c23794 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c227a0 bytes 04ee0094
+ 00c23794 bytes fbed0094
- 00c2275c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23750 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c2275c bytes d40300b0
+ 00c23750 bytes d40300b0
- 00c22768 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00c22768 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2375c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00c2375c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22768 bytes 940a46f9
+ 00c2375c bytes 94f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff26f08adfeaa27bd96ef959f486c10"></a>

### [`00c22888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22888.md) → [`00c2387c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2387c.md) FUN_00c2387c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c238a0",
      "incomplete_value": true,
      "site": "00c238a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c228ac",
      "incomplete_value": true,
      "site": "00c228b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "definition_site": "00c238ac",
      "incomplete_value": true,
      "site": "00c238b0",
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
      "definition_site": "00c228b8",
      "incomplete_value": true,
      "site": "00c228bc",
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
      "definition_site": "00c238d4",
      "incomplete_value": true,
      "site": "00c238d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c228e0",
      "incomplete_value": true,
      "site": "00c228e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "00c238a0",
      "READ",
      [
        "storage",
        "00c9b988",
        null,
        "pointer"
      ]
    ],
    [
      "00c238a4",
      "DATA",
      [
        "storage",
        "01127f28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c238a8",
      "READ",
      [
        "storage",
        "01127f28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c238a0",
      "READ",
      [
        "storage",
        "00c9c958",
        null,
        "pointer"
      ]
    ],
    [
      "00c238a4",
      "DATA",
      [
        "storage",
        "01128ee8",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c238a8",
      "READ",
      [
        "storage",
        "01128ee8",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c228e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22888.md#insn-00c228e4) · [`00c228a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22888.md#insn-00c228a0) · [`00c228ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22888.md#insn-00c228ac)
- 新版 [`00c238d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2387c.md#insn-00c238d8) · [`00c23894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2387c.md#insn-00c23894) · [`00c238a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c2387c.md#insn-00c238a0)

~~~diff
- 00c228e4 ["INT_ADD", "register:40f0:8", ["const:c228e4:8", "const:4:8"]]
- 00c228e4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c238d8 ["INT_ADD", "register:40f0:8", ["const:c238d8:8", "const:4:8"]]
+ 00c238d8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c228e4 bytes b3ed0094
+ 00c238d8 bytes aaed0094
- 00c228a0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23894 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c228a0 bytes d40300b0
+ 00c23894 bytes d40300b0
- 00c228ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00c228ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c238a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:958:8"]]
+ 00c238a0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c228ac bytes 94c644f9
+ 00c238a0 bytes 94ae44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41af04a58b6bced2ff638808d10cd3cc"></a>

### [`00c229cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c229cc.md) → [`00c239c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c239c0.md) FUN_00c239c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c239e4",
      "incomplete_value": true,
      "site": "00c239e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c229f0",
      "incomplete_value": true,
      "site": "00c229f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c239f0",
      "incomplete_value": true,
      "site": "00c239f4",
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
      "definition_site": "00c229fc",
      "incomplete_value": true,
      "site": "00c22a00",
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
      "definition_site": "00c23a18",
      "incomplete_value": true,
      "site": "00c23a1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22a24",
      "incomplete_value": true,
      "site": "00c22a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c239e4",
      "READ",
      [
        "storage",
        "00c9bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c239e8",
      "DATA",
      [
        "storage",
        "01127f48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c239ec",
      "READ",
      [
        "storage",
        "01127f48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c239e4",
      "READ",
      [
        "storage",
        "00c9ccc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c239e8",
      "DATA",
      [
        "storage",
        "01128f08",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c239ec",
      "READ",
      [
        "storage",
        "01128f08",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c229cc.md#insn-00c22a28) · [`00c229e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c229cc.md#insn-00c229e4) · [`00c229f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c229cc.md#insn-00c229f0)
- 新版 [`00c23a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c239c0.md#insn-00c23a1c) · [`00c239d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c239c0.md#insn-00c239d8) · [`00c239e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c239c0.md#insn-00c239e4)

~~~diff
- 00c22a28 ["INT_ADD", "register:40f0:8", ["const:c22a28:8", "const:4:8"]]
- 00c22a28 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23a1c ["INT_ADD", "register:40f0:8", ["const:c23a1c:8", "const:4:8"]]
+ 00c23a1c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c22a28 bytes 62ed0094
+ 00c23a1c bytes 59ed0094
- 00c229e4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c239d8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c229e4 bytes d40300b0
+ 00c239d8 bytes d40300b0
- 00c229f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
- 00c229f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c239e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc8:8"]]
+ 00c239e4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c229f0 bytes 947e46f9
+ 00c239e4 bytes 946646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b5b1acd0c83d9c3c573740b9e63067"></a>

### [`00c22b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22b10.md) → [`00c23b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23b04.md) FUN_00c23b04

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23b28",
      "incomplete_value": true,
      "site": "00c23b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c22b34",
      "incomplete_value": true,
      "site": "00c22b38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "definition_site": "00c23b34",
      "incomplete_value": true,
      "site": "00c23b38",
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
      "definition_site": "00c22b40",
      "incomplete_value": true,
      "site": "00c22b44",
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
      "definition_site": "00c23b5c",
      "incomplete_value": true,
      "site": "00c23b60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
    "old": {
      "definition_site": "00c22b68",
      "incomplete_value": true,
      "site": "00c22b6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "00c23b28",
      "READ",
      [
        "storage",
        "00c9bd08",
        null,
        "pointer"
      ]
    ],
    [
      "00c23b2c",
      "DATA",
      [
        "storage",
        "01127f68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23b30",
      "READ",
      [
        "storage",
        "01127f68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23b28",
      "READ",
      [
        "storage",
        "00c9ccd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23b2c",
      "DATA",
      [
        "storage",
        "01128f28",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23b30",
      "READ",
      [
        "storage",
        "01128f28",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22b10.md#insn-00c22b6c) · [`00c22b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22b10.md#insn-00c22b28) · [`00c22b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22b10.md#insn-00c22b34)
- 新版 [`00c23b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23b04.md#insn-00c23b60) · [`00c23b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23b04.md#insn-00c23b1c) · [`00c23b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23b04.md#insn-00c23b28)

~~~diff
- 00c22b6c ["INT_ADD", "register:40f0:8", ["const:c22b6c:8", "const:4:8"]]
- 00c22b6c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23b60 ["INT_ADD", "register:40f0:8", ["const:c23b60:8", "const:4:8"]]
+ 00c23b60 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c22b6c bytes 11ed0094
+ 00c23b60 bytes 08ed0094
- 00c22b28 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23b1c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c22b28 bytes d40300b0
+ 00c23b1c bytes d40300b0
- 00c22b34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d08:8"]]
- 00c22b34 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
+ 00c23b28 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22b34 bytes 948646f9
+ 00c23b28 bytes 946e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-759c5ec4dd75c6a52b50d16eea053767"></a>

### [`00c22c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22c54.md) → [`00c23c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23c48.md) FUN_00c23c48

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23c6c",
      "incomplete_value": true,
      "site": "00c23c70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22c78",
      "incomplete_value": true,
      "site": "00c22c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "definition_site": "00c23c78",
      "incomplete_value": true,
      "site": "00c23c7c",
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
      "definition_site": "00c22c84",
      "incomplete_value": true,
      "site": "00c22c88",
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
      "definition_site": "00c23ca0",
      "incomplete_value": true,
      "site": "00c23ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22cac",
      "incomplete_value": true,
      "site": "00c22cb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "00c23c6c",
      "READ",
      [
        "storage",
        "00c9bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c23c70",
      "DATA",
      [
        "storage",
        "01127f58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23c74",
      "READ",
      [
        "storage",
        "01127f58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23c6c",
      "READ",
      [
        "storage",
        "00c9cce8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23c70",
      "DATA",
      [
        "storage",
        "01128f18",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23c74",
      "READ",
      [
        "storage",
        "01128f18",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22c54.md#insn-00c22cb0) · [`00c22c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22c54.md#insn-00c22c6c) · [`00c22c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22c54.md#insn-00c22c78)
- 新版 [`00c23ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23c48.md#insn-00c23ca4) · [`00c23c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23c48.md#insn-00c23c60) · [`00c23c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23c48.md#insn-00c23c6c)

~~~diff
- 00c22cb0 ["INT_ADD", "register:40f0:8", ["const:c22cb0:8", "const:4:8"]]
- 00c22cb0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23ca4 ["INT_ADD", "register:40f0:8", ["const:c23ca4:8", "const:4:8"]]
+ 00c23ca4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c22cb0 bytes c0ec0094
+ 00c23ca4 bytes b7ec0094
- 00c22c6c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23c60 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c22c6c bytes d40300b0
+ 00c23c60 bytes d40300b0
- 00c22c78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d18:8"]]
- 00c22c78 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23c6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce8:8"]]
+ 00c23c6c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22c78 bytes 948e46f9
+ 00c23c6c bytes 947646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bdc07eea5495f848ebfadc5e41f478c"></a>

### [`00c22d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22d98.md) → [`00c23d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23d8c.md) FUN_00c23d8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23db0",
      "incomplete_value": true,
      "site": "00c23db4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22dbc",
      "incomplete_value": true,
      "site": "00c22dc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "definition_site": "00c23dbc",
      "incomplete_value": true,
      "site": "00c23dc0",
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
      "definition_site": "00c22dc8",
      "incomplete_value": true,
      "site": "00c22dcc",
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
      "definition_site": "00c23de4",
      "incomplete_value": true,
      "site": "00c23de8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22df0",
      "incomplete_value": true,
      "site": "00c22df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "00c23db0",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c23db4",
      "DATA",
      [
        "storage",
        "01127f78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23db8",
      "READ",
      [
        "storage",
        "01127f78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23db0",
      "READ",
      [
        "storage",
        "00c9ccf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23db4",
      "DATA",
      [
        "storage",
        "01128f38",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23db8",
      "READ",
      [
        "storage",
        "01128f38",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22d98.md#insn-00c22df4) · [`00c22db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22d98.md#insn-00c22db0) · [`00c22dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22d98.md#insn-00c22dbc)
- 新版 [`00c23de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23d8c.md#insn-00c23de8) · [`00c23da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23d8c.md#insn-00c23da4) · [`00c23db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23d8c.md#insn-00c23db0)

~~~diff
- 00c22df4 ["INT_ADD", "register:40f0:8", ["const:c22df4:8", "const:4:8"]]
- 00c22df4 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23de8 ["INT_ADD", "register:40f0:8", ["const:c23de8:8", "const:4:8"]]
+ 00c23de8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c22df4 bytes 6fec0094
+ 00c23de8 bytes 66ec0094
- 00c22db0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23da4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c22db0 bytes d40300b0
+ 00c23da4 bytes d40300b0
- 00c22dbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00c22dbc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23db0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00c23db0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22dbc bytes 949646f9
+ 00c23db0 bytes 947e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97203926ecc3787f799c519baf176a74"></a>

### [`00c22edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22edc.md) → [`00c23ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23ed0.md) FUN_00c23ed0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23ef4",
      "incomplete_value": true,
      "site": "00c23ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22f00",
      "incomplete_value": true,
      "site": "00c22f04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "definition_site": "00c23f00",
      "incomplete_value": true,
      "site": "00c23f04",
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
      "definition_site": "00c22f0c",
      "incomplete_value": true,
      "site": "00c22f10",
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
      "definition_site": "00c23f28",
      "incomplete_value": true,
      "site": "00c23f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c22f34",
      "incomplete_value": true,
      "site": "00c22f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
      "00c23ef4",
      "READ",
      [
        "storage",
        "00c9bc78",
        null,
        "pointer"
      ]
    ],
    [
      "00c23ef8",
      "DATA",
      [
        "storage",
        "01127f38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23efc",
      "READ",
      [
        "storage",
        "01127f38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23ef4",
      "READ",
      [
        "storage",
        "00c9cc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c23ef8",
      "DATA",
      [
        "storage",
        "01128ef8",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23efc",
      "READ",
      [
        "storage",
        "01128ef8",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22edc.md#insn-00c22f38) · [`00c22ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22edc.md#insn-00c22ef4) · [`00c22f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22edc.md#insn-00c22f00)
- 新版 [`00c23f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23ed0.md#insn-00c23f2c) · [`00c23ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23ed0.md#insn-00c23ee8) · [`00c23ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23ed0.md#insn-00c23ef4)

~~~diff
- 00c22f38 ["INT_ADD", "register:40f0:8", ["const:c22f38:8", "const:4:8"]]
- 00c22f38 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c23f2c ["INT_ADD", "register:40f0:8", ["const:c23f2c:8", "const:4:8"]]
+ 00c23f2c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c22f38 bytes 1eec0094
+ 00c23f2c bytes 15ec0094
- 00c22ef4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c23ee8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c22ef4 bytes d40300b0
+ 00c23ee8 bytes d40300b0
- 00c22f00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
- 00c22f00 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23ef4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c48:8"]]
+ 00c23ef4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22f00 bytes 943e46f9
+ 00c23ef4 bytes 942646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe28e5aab18bd4c588347109bc1328db"></a>

### [`00c23020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23020.md) → [`00c24014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24014.md) FUN_00c24014

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24038",
      "incomplete_value": true,
      "site": "00c2403c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23044",
      "incomplete_value": true,
      "site": "00c23048",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "definition_site": "00c24044",
      "incomplete_value": true,
      "site": "00c24048",
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
      "definition_site": "00c23050",
      "incomplete_value": true,
      "site": "00c23054",
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
      "definition_site": "00c2406c",
      "incomplete_value": true,
      "site": "00c24070",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23078",
      "incomplete_value": true,
      "site": "00c2307c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "00c24038",
      "READ",
      [
        "storage",
        "00c9bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2403c",
      "DATA",
      [
        "storage",
        "01127cf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24040",
      "READ",
      [
        "storage",
        "01127cf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24038",
      "READ",
      [
        "storage",
        "00c9cc80",
        null,
        "pointer"
      ]
    ],
    [
      "00c2403c",
      "DATA",
      [
        "storage",
        "01128cb8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24040",
      "READ",
      [
        "storage",
        "01128cb8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2307c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23020.md#insn-00c2307c) · [`00c23038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23020.md#insn-00c23038) · [`00c23044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23020.md#insn-00c23044)
- 新版 [`00c24070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24014.md#insn-00c24070) · [`00c2402c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24014.md#insn-00c2402c) · [`00c24038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24014.md#insn-00c24038)

~~~diff
- 00c2307c ["INT_ADD", "register:40f0:8", ["const:c2307c:8", "const:4:8"]]
- 00c2307c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24070 ["INT_ADD", "register:40f0:8", ["const:c24070:8", "const:4:8"]]
+ 00c24070 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c2307c bytes cdeb0094
+ 00c24070 bytes c4eb0094
- 00c23038 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c2402c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23038 bytes d4030090
+ 00c2402c bytes d4030090
- 00c23044 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb0:8"]]
- 00c23044 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c80:8"]]
+ 00c24038 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23044 bytes 945a46f9
+ 00c24038 bytes 944246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace189cc8fbe4d00a43b168798625977"></a>

### [`00c23164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23164.md) → [`00c24158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24158.md) FUN_00c24158

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2417c",
      "incomplete_value": true,
      "site": "00c24180",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23188",
      "incomplete_value": true,
      "site": "00c2318c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "definition_site": "00c24188",
      "incomplete_value": true,
      "site": "00c2418c",
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
      "definition_site": "00c23194",
      "incomplete_value": true,
      "site": "00c23198",
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
      "definition_site": "00c241b0",
      "incomplete_value": true,
      "site": "00c241b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c231bc",
      "incomplete_value": true,
      "site": "00c231c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "00c2417c",
      "READ",
      [
        "storage",
        "00c9bca8",
        null,
        "pointer"
      ]
    ],
    [
      "00c24180",
      "DATA",
      [
        "storage",
        "01127d08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24184",
      "READ",
      [
        "storage",
        "01127d08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2417c",
      "READ",
      [
        "storage",
        "00c9cc78",
        null,
        "pointer"
      ]
    ],
    [
      "00c24180",
      "DATA",
      [
        "storage",
        "01128cc8",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24184",
      "READ",
      [
        "storage",
        "01128cc8",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c231c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23164.md#insn-00c231c0) · [`00c2317c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23164.md#insn-00c2317c) · [`00c23188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23164.md#insn-00c23188)
- 新版 [`00c241b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24158.md#insn-00c241b4) · [`00c24170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24158.md#insn-00c24170) · [`00c2417c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24158.md#insn-00c2417c)

~~~diff
- 00c231c0 ["INT_ADD", "register:40f0:8", ["const:c231c0:8", "const:4:8"]]
- 00c231c0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c241b4 ["INT_ADD", "register:40f0:8", ["const:c241b4:8", "const:4:8"]]
+ 00c241b4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c231c0 bytes 7ceb0094
+ 00c241b4 bytes 73eb0094
- 00c2317c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24170 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c2317c bytes d4030090
+ 00c24170 bytes d4030090
- 00c23188 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
- 00c23188 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2417c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00c2417c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23188 bytes 945646f9
+ 00c2417c bytes 943e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e025507dd57c25cc58216f44b9be847"></a>

### [`00c232a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c232a8.md) → [`00c2429c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c2429c.md) FUN_00c2429c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c242c0",
      "incomplete_value": true,
      "site": "00c242c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c232cc",
      "incomplete_value": true,
      "site": "00c232d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00c242cc",
      "incomplete_value": true,
      "site": "00c242d0",
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
      "definition_site": "00c232d8",
      "incomplete_value": true,
      "site": "00c232dc",
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
      "definition_site": "00c242f4",
      "incomplete_value": true,
      "site": "00c242f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23300",
      "incomplete_value": true,
      "site": "00c23304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "00c242c0",
      "READ",
      [
        "storage",
        "00c9bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c242c4",
      "DATA",
      [
        "storage",
        "01127d18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c242c8",
      "READ",
      [
        "storage",
        "01127d18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c242c0",
      "READ",
      [
        "storage",
        "00c9cc90",
        null,
        "pointer"
      ]
    ],
    [
      "00c242c4",
      "DATA",
      [
        "storage",
        "01128cd8",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c242c8",
      "READ",
      [
        "storage",
        "01128cd8",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c232a8.md#insn-00c23304) · [`00c232c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c232a8.md#insn-00c232c0) · [`00c232cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c232a8.md#insn-00c232cc)
- 新版 [`00c242f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c2429c.md#insn-00c242f8) · [`00c242b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c2429c.md#insn-00c242b4) · [`00c242c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c2429c.md#insn-00c242c0)

~~~diff
- 00c23304 ["INT_ADD", "register:40f0:8", ["const:c23304:8", "const:4:8"]]
- 00c23304 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c242f8 ["INT_ADD", "register:40f0:8", ["const:c242f8:8", "const:4:8"]]
+ 00c242f8 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23304 bytes 2beb0094
+ 00c242f8 bytes 22eb0094
- 00c232c0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c242b4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c232c0 bytes d4030090
+ 00c242b4 bytes d4030090
- 00c232cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00c232cc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c242c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
+ 00c242c0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c232cc bytes 946246f9
+ 00c242c0 bytes 944a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cea74f8492f63f25ff01d9ff7a4e3abf"></a>

### [`00c233ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c233ec.md) → [`00c243e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c243e0.md) FUN_00c243e0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24404",
      "incomplete_value": true,
      "site": "00c24408",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23410",
      "incomplete_value": true,
      "site": "00c23414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "definition_site": "00c24410",
      "incomplete_value": true,
      "site": "00c24414",
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
      "definition_site": "00c2341c",
      "incomplete_value": true,
      "site": "00c23420",
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
      "definition_site": "00c24438",
      "incomplete_value": true,
      "site": "00c2443c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23444",
      "incomplete_value": true,
      "site": "00c23448",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "00c24404",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c24408",
      "DATA",
      [
        "storage",
        "01127d28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2440c",
      "READ",
      [
        "storage",
        "01127d28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24404",
      "READ",
      [
        "storage",
        "00c9cc88",
        null,
        "pointer"
      ]
    ],
    [
      "00c24408",
      "DATA",
      [
        "storage",
        "01128ce8",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2440c",
      "READ",
      [
        "storage",
        "01128ce8",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c233ec.md#insn-00c23448) · [`00c23404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c233ec.md#insn-00c23404) · [`00c23410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c233ec.md#insn-00c23410)
- 新版 [`00c2443c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c243e0.md#insn-00c2443c) · [`00c243f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c243e0.md#insn-00c243f8) · [`00c24404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c243e0.md#insn-00c24404)

~~~diff
- 00c23448 ["INT_ADD", "register:40f0:8", ["const:c23448:8", "const:4:8"]]
- 00c23448 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2443c ["INT_ADD", "register:40f0:8", ["const:c2443c:8", "const:4:8"]]
+ 00c2443c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23448 bytes daea0094
+ 00c2443c bytes d1ea0094
- 00c23404 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c243f8 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23404 bytes d4030090
+ 00c243f8 bytes d4030090
- 00c23410 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00c23410 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00c24404 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23410 bytes 945e46f9
+ 00c24404 bytes 944646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-169ad552a923fac4447a785a523cb8aa"></a>

### [`00c23530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23530.md) → [`00c24524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24524.md) FUN_00c24524

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24548",
      "incomplete_value": true,
      "site": "00c2454c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23554",
      "incomplete_value": true,
      "site": "00c23558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
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
      "definition_site": "00c24554",
      "incomplete_value": true,
      "site": "00c24558",
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
      "definition_site": "00c23560",
      "incomplete_value": true,
      "site": "00c23564",
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
      "definition_site": "00c2457c",
      "incomplete_value": true,
      "site": "00c24580",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23588",
      "incomplete_value": true,
      "site": "00c2358c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
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
      "00c24548",
      "READ",
      [
        "storage",
        "00c9bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00c2454c",
      "DATA",
      [
        "storage",
        "01127d38",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24550",
      "READ",
      [
        "storage",
        "01127d38",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24548",
      "READ",
      [
        "storage",
        "00c9cd48",
        null,
        "pointer"
      ]
    ],
    [
      "00c2454c",
      "DATA",
      [
        "storage",
        "01128cf8",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24550",
      "READ",
      [
        "storage",
        "01128cf8",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2358c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23530.md#insn-00c2358c) · [`00c23548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23530.md#insn-00c23548) · [`00c23554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23530.md#insn-00c23554)
- 新版 [`00c24580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24524.md#insn-00c24580) · [`00c2453c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24524.md#insn-00c2453c) · [`00c24548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24524.md#insn-00c24548)

~~~diff
- 00c2358c ["INT_ADD", "register:40f0:8", ["const:c2358c:8", "const:4:8"]]
- 00c2358c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24580 ["INT_ADD", "register:40f0:8", ["const:c24580:8", "const:4:8"]]
+ 00c24580 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c2358c bytes 89ea0094
+ 00c24580 bytes 80ea0094
- 00c23548 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c2453c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23548 bytes d4030090
+ 00c2453c bytes d4030090
- 00c23554 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
- 00c23554 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24548 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
+ 00c24548 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23554 bytes 94be46f9
+ 00c24548 bytes 94a646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ad9c07db9f0115125dedf3f87453f5e"></a>

### [`00c23674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23674.md) → [`00c24668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24668.md) FUN_00c24668

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2468c",
      "incomplete_value": true,
      "site": "00c24690",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23698",
      "incomplete_value": true,
      "site": "00c2369c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "definition_site": "00c24698",
      "incomplete_value": true,
      "site": "00c2469c",
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
      "definition_site": "00c236a4",
      "incomplete_value": true,
      "site": "00c236a8",
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
      "definition_site": "00c246c0",
      "incomplete_value": true,
      "site": "00c246c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c236cc",
      "incomplete_value": true,
      "site": "00c236d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "00c2468c",
      "READ",
      [
        "storage",
        "00c9bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00c24690",
      "DATA",
      [
        "storage",
        "01127d48",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24694",
      "READ",
      [
        "storage",
        "01127d48",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2468c",
      "READ",
      [
        "storage",
        "00c9cd58",
        null,
        "pointer"
      ]
    ],
    [
      "00c24690",
      "DATA",
      [
        "storage",
        "01128d08",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24694",
      "READ",
      [
        "storage",
        "01128d08",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c236d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23674.md#insn-00c236d0) · [`00c2368c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23674.md#insn-00c2368c) · [`00c23698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23674.md#insn-00c23698)
- 新版 [`00c246c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24668.md#insn-00c246c4) · [`00c24680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24668.md#insn-00c24680) · [`00c2468c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24668.md#insn-00c2468c)

~~~diff
- 00c236d0 ["INT_ADD", "register:40f0:8", ["const:c236d0:8", "const:4:8"]]
- 00c236d0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c246c4 ["INT_ADD", "register:40f0:8", ["const:c246c4:8", "const:4:8"]]
+ 00c246c4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c236d0 bytes 38ea0094
+ 00c246c4 bytes 2fea0094
- 00c2368c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24680 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c2368c bytes d4030090
+ 00c24680 bytes d4030090
- 00c23698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
- 00c23698 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2468c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00c2468c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23698 bytes 94c646f9
+ 00c2468c bytes 94ae46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c53a45568ffcc038777d17ac25cd871"></a>

### [`00c237b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c237b8.md) → [`00c247ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c247ac.md) FUN_00c247ac

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c247d0",
      "incomplete_value": true,
      "site": "00c247d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c237dc",
      "incomplete_value": true,
      "site": "00c237e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "definition_site": "00c247dc",
      "incomplete_value": true,
      "site": "00c247e0",
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
      "definition_site": "00c237e8",
      "incomplete_value": true,
      "site": "00c237ec",
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
      "definition_site": "00c24804",
      "incomplete_value": true,
      "site": "00c24808",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23810",
      "incomplete_value": true,
      "site": "00c23814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "00c247d0",
      "READ",
      [
        "storage",
        "00c9bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00c247d4",
      "DATA",
      [
        "storage",
        "01127d58",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c247d8",
      "READ",
      [
        "storage",
        "01127d58",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c247d0",
      "READ",
      [
        "storage",
        "00c9cd68",
        null,
        "pointer"
      ]
    ],
    [
      "00c247d4",
      "DATA",
      [
        "storage",
        "01128d18",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c247d8",
      "READ",
      [
        "storage",
        "01128d18",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c237b8.md#insn-00c23814) · [`00c237d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c237b8.md#insn-00c237d0) · [`00c237dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c237b8.md#insn-00c237dc)
- 新版 [`00c24808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c247ac.md#insn-00c24808) · [`00c247c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c247ac.md#insn-00c247c4) · [`00c247d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c247ac.md#insn-00c247d0)

~~~diff
- 00c23814 ["INT_ADD", "register:40f0:8", ["const:c23814:8", "const:4:8"]]
- 00c23814 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24808 ["INT_ADD", "register:40f0:8", ["const:c24808:8", "const:4:8"]]
+ 00c24808 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23814 bytes e7e90094
+ 00c24808 bytes dee90094
- 00c237d0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c247c4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c237d0 bytes d4030090
+ 00c247c4 bytes d4030090
- 00c237dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00c237dc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c247d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00c247d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c237dc bytes 94ce46f9
+ 00c247d0 bytes 94b646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65eb8c8967c812c146eaaba7863768b1"></a>

### [`00c238fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c238fc.md) → [`00c248f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c248f0.md) FUN_00c248f0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24914",
      "incomplete_value": true,
      "site": "00c24918",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23920",
      "incomplete_value": true,
      "site": "00c23924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24920",
      "incomplete_value": true,
      "site": "00c24924",
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
      "definition_site": "00c2392c",
      "incomplete_value": true,
      "site": "00c23930",
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
      "definition_site": "00c24948",
      "incomplete_value": true,
      "site": "00c2494c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23954",
      "incomplete_value": true,
      "site": "00c23958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c24914",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00c24918",
      "DATA",
      [
        "storage",
        "01127d68",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2491c",
      "READ",
      [
        "storage",
        "01127d68",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24914",
      "READ",
      [
        "storage",
        "00c9cd78",
        null,
        "pointer"
      ]
    ],
    [
      "00c24918",
      "DATA",
      [
        "storage",
        "01128d28",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2491c",
      "READ",
      [
        "storage",
        "01128d28",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c238fc.md#insn-00c23958) · [`00c23914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c238fc.md#insn-00c23914) · [`00c23920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c238fc.md#insn-00c23920)
- 新版 [`00c2494c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c248f0.md#insn-00c2494c) · [`00c24908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c248f0.md#insn-00c24908) · [`00c24914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c248f0.md#insn-00c24914)

~~~diff
- 00c23958 ["INT_ADD", "register:40f0:8", ["const:c23958:8", "const:4:8"]]
- 00c23958 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2494c ["INT_ADD", "register:40f0:8", ["const:c2494c:8", "const:4:8"]]
+ 00c2494c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23958 bytes 96e90094
+ 00c2494c bytes 8de90094
- 00c23914 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24908 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23914 bytes d4030090
+ 00c24908 bytes d4030090
- 00c23920 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
- 00c23920 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24914 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
+ 00c24914 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23920 bytes 94d646f9
+ 00c24914 bytes 94be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a235f682682a30476202fd70db04b7a9"></a>

### [`00c23a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23a40.md) → [`00c24a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24a34.md) FUN_00c24a34

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24a58",
      "incomplete_value": true,
      "site": "00c24a5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c23a64",
      "incomplete_value": true,
      "site": "00c23a68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00c24a8c",
      "incomplete_value": true,
      "site": "00c24a90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c23a98",
      "incomplete_value": true,
      "site": "00c23a9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "definition_site": "00c24a80",
      "incomplete_value": false,
      "site": "00c24a90",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c23a8c",
      "incomplete_value": false,
      "site": "00c23a9c",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c24a58",
      "READ",
      [
        "storage",
        "00c9bc88",
        null,
        "pointer"
      ]
    ],
    [
      "00c24a5c",
      "DATA",
      [
        "storage",
        "01127f88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24a60",
      "READ",
      [
        "storage",
        "01127f88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24a58",
      "READ",
      [
        "storage",
        "00c9cc58",
        null,
        "pointer"
      ]
    ],
    [
      "00c24a5c",
      "DATA",
      [
        "storage",
        "01128f48",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24a60",
      "READ",
      [
        "storage",
        "01128f48",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23a40.md#insn-00c23a9c) · [`00c23a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23a40.md#insn-00c23a58) · [`00c23a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23a40.md#insn-00c23a64)
- 新版 [`00c24a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24a34.md#insn-00c24a90) · [`00c24a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24a34.md#insn-00c24a4c) · [`00c24a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24a34.md#insn-00c24a58)

~~~diff
- 00c23a9c ["INT_ADD", "register:40f0:8", ["const:c23a9c:8", "const:4:8"]]
- 00c23a9c ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24a90 ["INT_ADD", "register:40f0:8", ["const:c24a90:8", "const:4:8"]]
+ 00c24a90 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23a9c bytes 45e90094
+ 00c24a90 bytes 3ce90094
- 00c23a58 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24a4c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23a58 bytes d4030090
+ 00c24a4c bytes d4030090
- 00c23a64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00c23a64 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00c24a58 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23a64 bytes 944646f9
+ 00c24a58 bytes 942e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83237a456753ba7da709f5f8d9ab8612"></a>

### [`00c23b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23b84.md) → [`00c24b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24b78.md) FUN_00c24b78

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24b9c",
      "incomplete_value": true,
      "site": "00c24ba0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23ba8",
      "incomplete_value": true,
      "site": "00c23bac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "definition_site": "00c24ba8",
      "incomplete_value": true,
      "site": "00c24bac",
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
      "definition_site": "00c23bb4",
      "incomplete_value": true,
      "site": "00c23bb8",
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
      "definition_site": "00c24bd0",
      "incomplete_value": true,
      "site": "00c24bd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23bdc",
      "incomplete_value": true,
      "site": "00c23be0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c98:8"
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
      "00c24b9c",
      "READ",
      [
        "storage",
        "00c9bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00c24ba0",
      "DATA",
      [
        "storage",
        "01127f98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24ba4",
      "READ",
      [
        "storage",
        "01127f98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24b9c",
      "READ",
      [
        "storage",
        "00c9cc68",
        null,
        "pointer"
      ]
    ],
    [
      "00c24ba0",
      "DATA",
      [
        "storage",
        "01128f58",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24ba4",
      "READ",
      [
        "storage",
        "01128f58",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23b84.md#insn-00c23be0) · [`00c23b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23b84.md#insn-00c23b9c) · [`00c23ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23b84.md#insn-00c23ba8)
- 新版 [`00c24bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24b78.md#insn-00c24bd4) · [`00c24b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24b78.md#insn-00c24b90) · [`00c24b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24b78.md#insn-00c24b9c)

~~~diff
- 00c23be0 ["INT_ADD", "register:40f0:8", ["const:c23be0:8", "const:4:8"]]
- 00c23be0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24bd4 ["INT_ADD", "register:40f0:8", ["const:c24bd4:8", "const:4:8"]]
+ 00c24bd4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23be0 bytes f4e80094
+ 00c24bd4 bytes ebe80094
- 00c23b9c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24b90 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23b9c bytes d4030090
+ 00c24b90 bytes d4030090
- 00c23ba8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00c23ba8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24b9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00c24b9c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23ba8 bytes 944e46f9
+ 00c24b9c bytes 943646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-069b7aa0ffa3e09a61c5b77410dd7707"></a>

### [`00c23cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23cc8.md) → [`00c24cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24cbc.md) FUN_00c24cbc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24ce0",
      "incomplete_value": true,
      "site": "00c24ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23cec",
      "incomplete_value": true,
      "site": "00c23cf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c24d14",
      "incomplete_value": true,
      "site": "00c24d18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23d20",
      "incomplete_value": true,
      "site": "00c23d24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c24d08",
      "incomplete_value": false,
      "site": "00c24d18",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c23d14",
      "incomplete_value": false,
      "site": "00c23d24",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c24ce0",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c24ce4",
      "DATA",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24ce8",
      "READ",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24ce0",
      "READ",
      [
        "storage",
        "00c9cbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c24ce4",
      "DATA",
      [
        "storage",
        "01128c38",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24ce8",
      "READ",
      [
        "storage",
        "01128c38",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23cc8.md#insn-00c23d24) · [`00c23ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23cc8.md#insn-00c23ce0) · [`00c23cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23cc8.md#insn-00c23cec)
- 新版 [`00c24d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24cbc.md#insn-00c24d18) · [`00c24cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24cbc.md#insn-00c24cd4) · [`00c24ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24cbc.md#insn-00c24ce0)

~~~diff
- 00c23d24 ["INT_ADD", "register:40f0:8", ["const:c23d24:8", "const:4:8"]]
- 00c23d24 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24d18 ["INT_ADD", "register:40f0:8", ["const:c24d18:8", "const:4:8"]]
+ 00c24d18 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23d24 bytes a3e80094
+ 00c24d18 bytes 9ae80094
- 00c23ce0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24cd4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23ce0 bytes d4030090
+ 00c24cd4 bytes d4030090
- 00c23cec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00c23cec ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24ce0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb0:8"]]
+ 00c24ce0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23cec bytes 94f245f9
+ 00c24ce0 bytes 94da45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4944ae2bb5558ab33d88b1ccef38a6"></a>

### [`00c23e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23e0c.md) → [`00c24e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24e00.md) FUN_00c24e00

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24e24",
      "incomplete_value": true,
      "site": "00c24e28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c23e30",
      "incomplete_value": true,
      "site": "00c23e34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "definition_site": "00c24e30",
      "incomplete_value": true,
      "site": "00c24e34",
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
      "definition_site": "00c23e3c",
      "incomplete_value": true,
      "site": "00c23e40",
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
      "definition_site": "00c24e58",
      "incomplete_value": true,
      "site": "00c24e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c23e64",
      "incomplete_value": true,
      "site": "00c23e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
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
      "00c24e24",
      "READ",
      [
        "storage",
        "00c9bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c24e28",
      "DATA",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24e2c",
      "READ",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24e24",
      "READ",
      [
        "storage",
        "00c9cbe8",
        null,
        "pointer"
      ]
    ],
    [
      "00c24e28",
      "DATA",
      [
        "storage",
        "01128c48",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24e2c",
      "READ",
      [
        "storage",
        "01128c48",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23e0c.md#insn-00c23e68) · [`00c23e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23e0c.md#insn-00c23e24) · [`00c23e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23e0c.md#insn-00c23e30)
- 新版 [`00c24e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24e00.md#insn-00c24e5c) · [`00c24e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24e00.md#insn-00c24e18) · [`00c24e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24e00.md#insn-00c24e24)

~~~diff
- 00c23e68 ["INT_ADD", "register:40f0:8", ["const:c23e68:8", "const:4:8"]]
- 00c23e68 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24e5c ["INT_ADD", "register:40f0:8", ["const:c24e5c:8", "const:4:8"]]
+ 00c24e5c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23e68 bytes 52e80094
+ 00c24e5c bytes 49e80094
- 00c23e24 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24e18 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23e24 bytes d4030090
+ 00c24e18 bytes d4030090
- 00c23e30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
- 00c23e30 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24e24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00c24e24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23e30 bytes 940e46f9
+ 00c24e24 bytes 94f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236ca1cf07b8512b0a54f56c78cfb512"></a>

### [`00c23f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23f50.md) → [`00c24f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24f44.md) FUN_00c24f44

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24f68",
      "incomplete_value": true,
      "site": "00c24f6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:8d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23f74",
      "incomplete_value": true,
      "site": "00c23f78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "definition_site": "00c24f74",
      "incomplete_value": true,
      "site": "00c24f78",
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
      "definition_site": "00c23f80",
      "incomplete_value": true,
      "site": "00c23f84",
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
      "definition_site": "00c24f9c",
      "incomplete_value": true,
      "site": "00c24fa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:8d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23fa8",
      "incomplete_value": true,
      "site": "00c23fac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "00c24f68",
      "READ",
      [
        "storage",
        "00c9b908",
        null,
        "pointer"
      ]
    ],
    [
      "00c24f6c",
      "DATA",
      [
        "storage",
        "01127c98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24f70",
      "READ",
      [
        "storage",
        "01127c98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24f68",
      "READ",
      [
        "storage",
        "00c9c8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c24f6c",
      "DATA",
      [
        "storage",
        "01128c58",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24f70",
      "READ",
      [
        "storage",
        "01128c58",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23f50.md#insn-00c23fac) · [`00c23f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23f50.md#insn-00c23f68) · [`00c23f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c23/00c23f50.md#insn-00c23f74)
- 新版 [`00c24fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24f44.md#insn-00c24fa0) · [`00c24f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24f44.md#insn-00c24f5c) · [`00c24f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c24/00c24f44.md#insn-00c24f68)

~~~diff
- 00c23fac ["INT_ADD", "register:40f0:8", ["const:c23fac:8", "const:4:8"]]
- 00c23fac ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c24fa0 ["INT_ADD", "register:40f0:8", ["const:c24fa0:8", "const:4:8"]]
+ 00c24fa0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c23fac bytes 01e80094
+ 00c24fa0 bytes f8e70094
- 00c23f68 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c24f5c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c23f68 bytes d4030090
+ 00c24f5c bytes d4030090
- 00c23f74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
- 00c23f74 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00c24f68 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23f74 bytes 948644f9
+ 00c24f68 bytes 946e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70b57e63758451af5e0227cc6f9a4144"></a>

### [`00c24094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24094.md) → [`00c25088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25088.md) FUN_00c25088

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c250ac",
      "incomplete_value": true,
      "site": "00c250b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c240b8",
      "incomplete_value": true,
      "site": "00c240bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c250b8",
      "incomplete_value": true,
      "site": "00c250bc",
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
      "definition_site": "00c240c4",
      "incomplete_value": true,
      "site": "00c240c8",
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
      "definition_site": "00c250e0",
      "incomplete_value": true,
      "site": "00c250e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c240ec",
      "incomplete_value": true,
      "site": "00c240f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c250ac",
      "READ",
      [
        "storage",
        "00c9bc28",
        null,
        "pointer"
      ]
    ],
    [
      "00c250b0",
      "DATA",
      [
        "storage",
        "01127ca8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c250b4",
      "READ",
      [
        "storage",
        "01127ca8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c250ac",
      "READ",
      [
        "storage",
        "00c9cbf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c250b0",
      "DATA",
      [
        "storage",
        "01128c68",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c250b4",
      "READ",
      [
        "storage",
        "01128c68",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c240f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24094.md#insn-00c240f0) · [`00c240ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24094.md#insn-00c240ac) · [`00c240b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24094.md#insn-00c240b8)
- 新版 [`00c250e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25088.md#insn-00c250e4) · [`00c250a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25088.md#insn-00c250a0) · [`00c250ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25088.md#insn-00c250ac)

~~~diff
- 00c240f0 ["INT_ADD", "register:40f0:8", ["const:c240f0:8", "const:4:8"]]
- 00c240f0 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c250e4 ["INT_ADD", "register:40f0:8", ["const:c250e4:8", "const:4:8"]]
+ 00c250e4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c240f0 bytes b0e70094
+ 00c250e4 bytes a7e70094
- 00c240ac ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c250a0 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c240ac bytes b40300f0
+ 00c250a0 bytes b40300f0
- 00c240b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
- 00c240b8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c250ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf8:8"]]
+ 00c250ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c240b8 bytes 941646f9
+ 00c250ac bytes 94fe45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-148528fdedcd2afe1426a98788dd137f"></a>

### [`00c241d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c241d8.md) → [`00c251cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c251cc.md) FUN_00c251cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c251f0",
      "incomplete_value": true,
      "site": "00c251f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c241fc",
      "incomplete_value": true,
      "site": "00c24200",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
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
      "definition_site": "00c251fc",
      "incomplete_value": true,
      "site": "00c25200",
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
      "definition_site": "00c24208",
      "incomplete_value": true,
      "site": "00c2420c",
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
      "definition_site": "00c25224",
      "incomplete_value": true,
      "site": "00c25228",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "00c24230",
      "incomplete_value": true,
      "site": "00c24234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
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
      "00c251f0",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c251f4",
      "DATA",
      [
        "storage",
        "01127cb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c251f8",
      "READ",
      [
        "storage",
        "01127cb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c251f0",
      "READ",
      [
        "storage",
        "00c9c390",
        null,
        "pointer"
      ]
    ],
    [
      "00c251f4",
      "DATA",
      [
        "storage",
        "01128c78",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c251f8",
      "READ",
      [
        "storage",
        "01128c78",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c241d8.md#insn-00c24234) · [`00c241f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c241d8.md#insn-00c241f0) · [`00c241fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c241d8.md#insn-00c241fc)
- 新版 [`00c25228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c251cc.md#insn-00c25228) · [`00c251e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c251cc.md#insn-00c251e4) · [`00c251f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c251cc.md#insn-00c251f0)

~~~diff
- 00c24234 ["INT_ADD", "register:40f0:8", ["const:c24234:8", "const:4:8"]]
- 00c24234 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c25228 ["INT_ADD", "register:40f0:8", ["const:c25228:8", "const:4:8"]]
+ 00c25228 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c24234 bytes 5fe70094
+ 00c25228 bytes 56e70094
- 00c241f0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c251e4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c241f0 bytes b40300f0
+ 00c251e4 bytes b40300f0
- 00c241fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c0:8"]]
- 00c241fc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c251f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00c251f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c241fc bytes 94e241f9
+ 00c251f0 bytes 94ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a92636066d25a4a886827c21ee18156e"></a>

### [`00c2431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2431c.md) → [`00c25310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25310.md) FUN_00c25310

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25334",
      "incomplete_value": true,
      "site": "00c25338",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24340",
      "incomplete_value": true,
      "site": "00c24344",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "definition_site": "00c25340",
      "incomplete_value": true,
      "site": "00c25344",
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
      "definition_site": "00c2434c",
      "incomplete_value": true,
      "site": "00c24350",
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
      "definition_site": "00c25368",
      "incomplete_value": true,
      "site": "00c2536c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24374",
      "incomplete_value": true,
      "site": "00c24378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
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
      "00c25334",
      "READ",
      [
        "storage",
        "00c9bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25338",
      "DATA",
      [
        "storage",
        "01127cc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2533c",
      "READ",
      [
        "storage",
        "01127cc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c25334",
      "READ",
      [
        "storage",
        "00c9cd90",
        null,
        "pointer"
      ]
    ],
    [
      "00c25338",
      "DATA",
      [
        "storage",
        "01128c88",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2533c",
      "READ",
      [
        "storage",
        "01128c88",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2431c.md#insn-00c24378) · [`00c24334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2431c.md#insn-00c24334) · [`00c24340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2431c.md#insn-00c24340)
- 新版 [`00c2536c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25310.md#insn-00c2536c) · [`00c25328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25310.md#insn-00c25328) · [`00c25334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25310.md#insn-00c25334)

~~~diff
- 00c24378 ["INT_ADD", "register:40f0:8", ["const:c24378:8", "const:4:8"]]
- 00c24378 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2536c ["INT_ADD", "register:40f0:8", ["const:c2536c:8", "const:4:8"]]
+ 00c2536c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c24378 bytes 0ee70094
+ 00c2536c bytes 05e70094
- 00c24334 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c25328 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c24334 bytes b40300f0
+ 00c25328 bytes b40300f0
- 00c24340 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00c24340 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25334 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00c25334 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c24340 bytes 94e246f9
+ 00c25334 bytes 94ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0f8dce492a887c50450235fc5bf8355"></a>

### [`00c24460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24460.md) → [`00c25454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25454.md) FUN_00c25454

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25478",
      "incomplete_value": true,
      "site": "00c2547c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:398:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24484",
      "incomplete_value": true,
      "site": "00c24488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
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
      "definition_site": "00c25484",
      "incomplete_value": true,
      "site": "00c25488",
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
      "definition_site": "00c24490",
      "incomplete_value": true,
      "site": "00c24494",
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
      "definition_site": "00c254ac",
      "incomplete_value": true,
      "site": "00c254b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:398:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c244b8",
      "incomplete_value": true,
      "site": "00c244bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
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
      "00c25478",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2547c",
      "DATA",
      [
        "storage",
        "01127cd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c25480",
      "READ",
      [
        "storage",
        "01127cd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c25478",
      "READ",
      [
        "storage",
        "00c9c398",
        null,
        "pointer"
      ]
    ],
    [
      "00c2547c",
      "DATA",
      [
        "storage",
        "01128c98",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c25480",
      "READ",
      [
        "storage",
        "01128c98",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c244bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24460.md#insn-00c244bc) · [`00c24478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24460.md#insn-00c24478) · [`00c24484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24460.md#insn-00c24484)
- 新版 [`00c254b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25454.md#insn-00c254b0) · [`00c2546c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25454.md#insn-00c2546c) · [`00c25478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25454.md#insn-00c25478)

~~~diff
- 00c244bc ["INT_ADD", "register:40f0:8", ["const:c244bc:8", "const:4:8"]]
- 00c244bc ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c254b0 ["INT_ADD", "register:40f0:8", ["const:c254b0:8", "const:4:8"]]
+ 00c254b0 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c244bc bytes bde60094
+ 00c254b0 bytes b4e60094
- 00c24478 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c2546c ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c24478 bytes b40300f0
+ 00c2546c bytes b40300f0
- 00c24484 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c8:8"]]
- 00c24484 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25478 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:398:8"]]
+ 00c25478 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c24484 bytes 94e641f9
+ 00c25478 bytes 94ce41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faef9ccc1e476da282e68753da465ff0"></a>

### [`00c245a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c245a4.md) → [`00c25598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25598.md) FUN_00c25598

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c255bc",
      "incomplete_value": true,
      "site": "00c255c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c245c8",
      "incomplete_value": true,
      "site": "00c245cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "definition_site": "00c255c8",
      "incomplete_value": true,
      "site": "00c255cc",
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
      "definition_site": "00c245d4",
      "incomplete_value": true,
      "site": "00c245d8",
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
      "definition_site": "00c255f0",
      "incomplete_value": true,
      "site": "00c255f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c245fc",
      "incomplete_value": true,
      "site": "00c24600",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "00c255bc",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00c255c0",
      "DATA",
      [
        "storage",
        "01127ce8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c255c4",
      "READ",
      [
        "storage",
        "01127ce8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c255bc",
      "READ",
      [
        "storage",
        "00c9cdb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c255c0",
      "DATA",
      [
        "storage",
        "01128ca8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c255c4",
      "READ",
      [
        "storage",
        "01128ca8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c245a4.md#insn-00c24600) · [`00c245bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c245a4.md#insn-00c245bc) · [`00c245c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c245a4.md#insn-00c245c8)
- 新版 [`00c255f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25598.md#insn-00c255f4) · [`00c255b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25598.md#insn-00c255b0) · [`00c255bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25598.md#insn-00c255bc)

~~~diff
- 00c24600 ["INT_ADD", "register:40f0:8", ["const:c24600:8", "const:4:8"]]
- 00c24600 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c255f4 ["INT_ADD", "register:40f0:8", ["const:c255f4:8", "const:4:8"]]
+ 00c255f4 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c24600 bytes 6ce60094
+ 00c255f4 bytes 63e60094
- 00c245bc ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c255b0 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c245bc bytes b40300f0
+ 00c255b0 bytes b40300f0
- 00c245c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:de0:8"]]
- 00c245c8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c255bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00c255bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c245c8 bytes 94f246f9
+ 00c255bc bytes 94da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2edc5df6423fe9338b2ef3ff56f09f6b"></a>

### [`00c246e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c246e8.md) → [`00c256dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c256dc.md) FUN_00c256dc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25700",
      "incomplete_value": true,
      "site": "00c25704",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2470c",
      "incomplete_value": true,
      "site": "00c24710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "definition_site": "00c2570c",
      "incomplete_value": true,
      "site": "00c25710",
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
      "definition_site": "00c24718",
      "incomplete_value": true,
      "site": "00c2471c",
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
      "definition_site": "00c25734",
      "incomplete_value": true,
      "site": "00c25738",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24740",
      "incomplete_value": true,
      "site": "00c24744",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "00c25700",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25704",
      "DATA",
      [
        "storage",
        "01127d78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c25708",
      "READ",
      [
        "storage",
        "01127d78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c25700",
      "READ",
      [
        "storage",
        "00c9cdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25704",
      "DATA",
      [
        "storage",
        "01128d38",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c25708",
      "READ",
      [
        "storage",
        "01128d38",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c246e8.md#insn-00c24744) · [`00c24700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c246e8.md#insn-00c24700) · [`00c2470c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c246e8.md#insn-00c2470c)
- 新版 [`00c25738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c256dc.md#insn-00c25738) · [`00c256f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c256dc.md#insn-00c256f4) · [`00c25700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c256dc.md#insn-00c25700)

~~~diff
- 00c24744 ["INT_ADD", "register:40f0:8", ["const:c24744:8", "const:4:8"]]
- 00c24744 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c25738 ["INT_ADD", "register:40f0:8", ["const:c25738:8", "const:4:8"]]
+ 00c25738 ["CALL", null, ["callee:00c5ef80:8"]]
- 00c24744 bytes 1be60094
+ 00c25738 bytes 12e60094
- 00c24700 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c256f4 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c24700 bytes b40300f0
+ 00c256f4 bytes b40300f0
- 00c2470c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00c2470c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25700 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
+ 00c25700 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2470c bytes 94fa46f9
+ 00c25700 bytes 94e246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de378225123d362fae3d70cd6b8cd3f5"></a>

### [`00c2482c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2482c.md) → [`00c25820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25820.md) FUN_00c25820

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c22014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c22/00c22014.md) · 呼出先 6件 [`00c05ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05ff4.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c23008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c23/00c23008.md) · 呼出先 6件 [`00c06fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06fe8.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25844",
      "incomplete_value": true,
      "site": "00c25848",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24850",
      "incomplete_value": true,
      "site": "00c24854",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:e00:8"
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
      "definition_site": "00c25878",
      "incomplete_value": true,
      "site": "00c2587c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24884",
      "incomplete_value": true,
      "site": "00c24888",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "definition_site": "00c2586c",
      "incomplete_value": false,
      "site": "00c2587c",
      "value": [
        "leaf",
        "const:c37048:8"
      ]
    },
    "old": {
      "definition_site": "00c24878",
      "incomplete_value": false,
      "site": "00c24888",
      "value": [
        "leaf",
        "const:c36054:8"
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
      "00c25844",
      "READ",
      [
        "storage",
        "00c9be00",
        null,
        "pointer"
      ]
    ],
    [
      "00c25848",
      "DATA",
      [
        "storage",
        "01127d88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2584c",
      "READ",
      [
        "storage",
        "01127d88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c25844",
      "READ",
      [
        "storage",
        "00c9cdd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25848",
      "DATA",
      [
        "storage",
        "01128d48",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2584c",
      "READ",
      [
        "storage",
        "01128d48",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2482c.md#insn-00c24888) · [`00c24844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2482c.md#insn-00c24844) · [`00c24850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c2482c.md#insn-00c24850)
- 新版 [`00c2587c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25820.md#insn-00c2587c) · [`00c25838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25820.md#insn-00c25838) · [`00c25844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25820.md#insn-00c25844)

~~~diff
- 00c24888 ["INT_ADD", "register:40f0:8", ["const:c24888:8", "const:4:8"]]
- 00c24888 ["CALL", null, ["callee:00c5ef80:8"]]
+ 00c2587c ["INT_ADD", "register:40f0:8", ["const:c2587c:8", "const:4:8"]]
+ 00c2587c ["CALL", null, ["callee:00c5ef80:8"]]
- 00c24888 bytes cae50094
+ 00c2587c bytes c1e50094
- 00c24844 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c25838 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c24844 bytes b40300f0
+ 00c25838 bytes b40300f0
- 00c24850 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
- 00c24850 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25844 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd0:8"]]
+ 00c25844 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c24850 bytes 940247f9
+ 00c25844 bytes 94ea46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864fe2ea6faad8e78cb010fb8877b9de"></a>

### [`00c24970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md) → [`00c25964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25964.md) FUN_00c25964

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c253ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c253ac.md) · 呼出先 10件 [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) [`00c35984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c263a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c263a0.md) · 呼出先 10件 [`00c36960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md) [`00c36978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36978.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25994",
      "incomplete_value": false,
      "site": "00c25994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c94000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c249a0",
      "incomplete_value": false,
      "site": "00c249a0",
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
            "const:790:8"
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
      "00c25994",
      "DATA",
      [
        "storage",
        "00c93790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c25994",
      "DATA",
      [
        "storage",
        "00c94760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md#insn-00c24994) · [`00c24998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md#insn-00c24998) · [`00c2499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md#insn-00c2499c)
- 新版 [`00c25988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25964.md#insn-00c25988) · [`00c2598c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25964.md#insn-00c2598c)

~~~diff
- 00c24994 ["COPY", "register:4058:8", ["const:c93000:8"]]
+ 00c25988 ["COPY", "register:4058:8", ["const:c94000:8"]]
- 00c24994 bytes 6b0300f0
+ 00c25988 bytes 6b0300f0
- 00c24998 ["COPY", "tmp:0:8", ["const:790:8"]]
- 00c24998 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00c24998 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00c24998 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00c2598c ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00c2598c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00c2598c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00c2598c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00c24998 bytes 6b411e91
+ 00c2598c bytes 6b811d91
- 00c2499c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00c2499c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

