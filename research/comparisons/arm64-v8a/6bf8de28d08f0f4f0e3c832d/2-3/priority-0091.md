# v16.0.2 → v16.0.3 · 最優先の変更候補 (91)

[一覧の目次](README.md)

<a id="compare-67cb30a921a1fdfca2e99e3a614a86ec"></a>

### [`00c4c014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md) → [`00c4d008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d008.md) FUN_00c4d008

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4d06c",
      "incomplete_value": true,
      "site": "00c4d07c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:71f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00c4d06c",
      "READ",
      [
        "storage",
        "002bd641",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d06c",
      "READ",
      [
        "storage",
        "002bd71f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md#insn-00c4c058) · [`00c4c070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md#insn-00c4c070) · [`00c4c0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md#insn-00c4c0a8)
- 新版 [`00c4d04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d008.md#insn-00c4d04c) · [`00c4d064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d008.md#insn-00c4d064) · [`00c4d09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d008.md#insn-00c4d09c)

~~~diff
- 00c4c058 ["INT_ADD", "register:40f0:8", ["const:c4c058:8", "const:4:8"]]
- 00c4c058 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d04c ["INT_ADD", "register:40f0:8", ["const:c4d04c:8", "const:4:8"]]
+ 00c4d04c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c058 bytes 46380094
+ 00c4d04c bytes 3d380094
- 00c4c070 ["COPY", "tmp:0:8", ["const:641:8"]]
- 00c4c070 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4c070 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4c070 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4d064 ["COPY", "tmp:0:8", ["const:71f:8"]]
+ 00c4d064 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d064 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d064 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4c070 bytes 4a051991
+ 00c4d064 bytes 4a7d1c91
- 00c4c0a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c0a8 ["INT_ADD", "register:40f0:8", ["const:c4c0a8:8", "const:4:8"]]
- 00c4c0a8 ["CALLIND", null, ["register:0:8"]]
+ 00c4d09c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d09c ["INT_ADD", "register:40f0:8", ["const:c4d09c:8", "const:4:8"]]
+ 00c4d09c ["CALLIND", null, ["register:0:8"]]
- 00c4c0a8 bytes 00013fd6
+ 00c4d09c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0453a0e02d4a0a3136d131e130414fda"></a>

### [`00c4c0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md) → [`00c4d0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d0ec.md) FUN_00c4d0ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4d150",
      "incomplete_value": true,
      "site": "00c4d160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:397:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00c4d150",
      "READ",
      [
        "storage",
        "002bc2b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d150",
      "READ",
      [
        "storage",
        "002bc397",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md#insn-00c4c13c) · [`00c4c154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md#insn-00c4c154) · [`00c4c190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md#insn-00c4c190)
- 新版 [`00c4d130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d0ec.md#insn-00c4d130) · [`00c4d148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d0ec.md#insn-00c4d148) · [`00c4d184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d0ec.md#insn-00c4d184)

~~~diff
- 00c4c13c ["INT_ADD", "register:40f0:8", ["const:c4c13c:8", "const:4:8"]]
- 00c4c13c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d130 ["INT_ADD", "register:40f0:8", ["const:c4d130:8", "const:4:8"]]
+ 00c4d130 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c13c bytes 0d380094
+ 00c4d130 bytes 04380094
- 00c4c154 ["COPY", "tmp:0:8", ["const:2b9:8"]]
- 00c4c154 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4c154 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4c154 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4d148 ["COPY", "tmp:0:8", ["const:397:8"]]
+ 00c4d148 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d148 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d148 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4c154 bytes 4ae50a91
+ 00c4d148 bytes 4a5d0e91
- 00c4c190 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c190 ["INT_ADD", "register:40f0:8", ["const:c4c190:8", "const:4:8"]]
- 00c4c190 ["CALLIND", null, ["register:0:8"]]
+ 00c4d184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d184 ["INT_ADD", "register:40f0:8", ["const:c4d184:8", "const:4:8"]]
+ 00c4d184 ["CALLIND", null, ["register:0:8"]]
- 00c4c190 bytes 00013fd6
+ 00c4d184 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268c4f025566db2fd0491f0799671f13"></a>

### [`00c4c3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md) → [`00c4d3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d3c8.md) FUN_00c4d3c8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4d55c",
      "incomplete_value": false,
      "site": "00c4d574",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4d564",
      "incomplete_value": false,
      "site": "00c4d574",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4d56c",
      "incomplete_value": false,
      "site": "00c4d574",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4d4cc",
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      "00c4d4cc",
      "READ",
      [
        "storage",
        "002bd64b",
        null,
        "string"
      ]
    ],
    [
      "00c4d4cc",
      "READ",
      [
        "storage",
        "002b8d44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d4cc",
      "READ",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ],
    [
      "00c4d4cc",
      "READ",
      [
        "storage",
        "002bd729",
        null,
        "string"
      ]
    ],
    [
      "00c4d4cc",
      "READ",
      [
        "storage",
        "002b8e13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md#insn-00c4c580) · [`00c4c41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md#insn-00c4c41c) · [`00c4c470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md#insn-00c4c470)
- 新版 [`00c4d574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d3c8.md#insn-00c4d574) · [`00c4d410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d3c8.md#insn-00c4d410) · [`00c4d464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d3c8.md#insn-00c4d464)

~~~diff
- 00c4c580 ["INT_ADD", "register:40f0:8", ["const:c4c580:8", "const:4:8"]]
- 00c4c580 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c4d574 ["INT_ADD", "register:40f0:8", ["const:c4d574:8", "const:4:8"]]
+ 00c4d574 ["CALL", null, ["callee:00c3909c:8"]]
- 00c4c580 bytes caaeff97
+ 00c4d574 bytes caaeff97
- 00c4c41c ["INT_ADD", "register:40f0:8", ["const:c4c41c:8", "const:4:8"]]
- 00c4c41c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d410 ["INT_ADD", "register:40f0:8", ["const:c4d410:8", "const:4:8"]]
+ 00c4d410 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c41c bytes 55370094
+ 00c4d410 bytes 4c370094
- 00c4c470 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00c4c470 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c4c470 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c4c470 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c4d464 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 00c4d464 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c4d464 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c4d464 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c4c470 bytes b53e3b91
+ 00c4d464 bytes b5b63e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df473f77288a59d1876d2a1f5d6a7094"></a>

### [`00c4c58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md) → [`00c4d580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d580.md) FUN_00c4d580

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md)

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
      "definition_site": "00c4d640",
      "incomplete_value": false,
      "site": "00c4d658",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4d648",
      "incomplete_value": false,
      "site": "00c4d658",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4d650",
      "incomplete_value": false,
      "site": "00c4d658",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4d5a0",
      "DATA",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      "00c4d5d0",
      "DATA",
      [
        "storage",
        "002b7ef0",
        null,
        "string"
      ]
    ],
    [
      "00c4d608",
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d5a0",
      "DATA",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ],
    [
      "00c4d5d0",
      "DATA",
      [
        "storage",
        "002b7fbf",
        null,
        "string"
      ]
    ],
    [
      "00c4d608",
      "READ",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md#insn-00c4c664) · [`00c4c5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md#insn-00c4c5ac) · [`00c4c5cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md#insn-00c4c5cc)
- 新版 [`00c4d658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d580.md#insn-00c4d658) · [`00c4d5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d580.md#insn-00c4d5a0) · [`00c4d5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d580.md#insn-00c4d5c0)

~~~diff
- 00c4c664 ["INT_ADD", "register:40f0:8", ["const:c4c664:8", "const:4:8"]]
- 00c4c664 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c4d658 ["INT_ADD", "register:40f0:8", ["const:c4d658:8", "const:4:8"]]
+ 00c4d658 ["CALL", null, ["callee:00c3909c:8"]]
- 00c4c664 bytes 91aeff97
+ 00c4d658 bytes 91aeff97
- 00c4c5ac ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00c4c5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c4c5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c4c5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c4d5a0 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 00c4d5a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4d5a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4d5a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c4c5ac bytes 003c3b91
+ 00c4d5a0 bytes 00b43e91
- 00c4c5cc ["COPY", "tmp:0:8", ["const:64b:8"]]
- 00c4c5cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4c5cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4c5cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4d5c0 ["COPY", "tmp:0:8", ["const:729:8"]]
+ 00c4d5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4d5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4d5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4c5cc bytes 082d1991
+ 00c4d5c0 bytes 08a51c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5861d48af7b7b82bc0d03d3e65273ffa"></a>

### [`00c4c670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md) → [`00c4d664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d664.md) FUN_00c4d664

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4d7a4",
      "incomplete_value": true,
      "site": "00c4d7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bbf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d7a8",
      "incomplete_value": true,
      "site": "00c4d7b0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d810",
      "incomplete_value": true,
      "site": "00c4d818",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:220:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00c4d7a4",
      "READ",
      [
        "storage",
        "002b4ae1",
        null,
        "string"
      ]
    ],
    [
      "00c4d7a8",
      "READ",
      [
        "storage",
        "002b4aee",
        null,
        "string"
      ]
    ],
    [
      "00c4d810",
      "READ",
      [
        "storage",
        "002bb142",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d7a4",
      "READ",
      [
        "storage",
        "002b4bbf",
        null,
        "string"
      ]
    ],
    [
      "00c4d7a8",
      "READ",
      [
        "storage",
        "002b4bcc",
        null,
        "string"
      ]
    ],
    [
      "00c4d810",
      "READ",
      [
        "storage",
        "002bb220",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md#insn-00c4c6b8) · [`00c4c6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md#insn-00c4c6fc) · [`00c4c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md#insn-00c4c734)
- 新版 [`00c4d6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d664.md#insn-00c4d6ac) · [`00c4d6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d664.md#insn-00c4d6f0) · [`00c4d728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d664.md#insn-00c4d728)

~~~diff
- 00c4c6b8 ["INT_ADD", "register:40f0:8", ["const:c4c6b8:8", "const:4:8"]]
- 00c4c6b8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d6ac ["INT_ADD", "register:40f0:8", ["const:c4d6ac:8", "const:4:8"]]
+ 00c4d6ac ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c6b8 bytes ae360094
+ 00c4d6ac bytes a5360094
- 00c4c6fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4c6fc ["INT_ADD", "register:40f0:8", ["const:c4c6fc:8", "const:4:8"]]
- 00c4c6fc ["CALLIND", null, ["register:0:8"]]
+ 00c4d6f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d6f0 ["INT_ADD", "register:40f0:8", ["const:c4d6f0:8", "const:4:8"]]
+ 00c4d6f0 ["CALLIND", null, ["register:0:8"]]
- 00c4c6fc bytes 00013fd6
+ 00c4d6f0 bytes 00013fd6
- 00c4c734 ["INT_ADD", "register:40f0:8", ["const:c4c734:8", "const:4:8"]]
- 00c4c734 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4d728 ["INT_ADD", "register:40f0:8", ["const:c4d728:8", "const:4:8"]]
+ 00c4d728 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4c734 bytes 8f360094
+ 00c4d728 bytes 86360094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27350bbde07277d0ecd2b9c60cac5d45"></a>

### [`00c4c8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md) → [`00c4d8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d8a0.md) FUN_00c4d8a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00c4d8c0",
      "incomplete_value": true,
      "site": "00c4d8c4",
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
                "const:e08:8"
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
      "00c4d8b0",
      "DATA",
      [
        "storage",
        "00313d98",
        null,
        null
      ]
    ],
    [
      "00c4d8bc",
      "DATA",
      [
        "storage",
        "00313dc8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4d8b0",
      "DATA",
      [
        "storage",
        "00313dd8",
        null,
        null
      ]
    ],
    [
      "00c4d8bc",
      "DATA",
      [
        "storage",
        "00313e08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4c8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md#insn-00c4c8b8) · [`00c4c8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md#insn-00c4c8c0) · [`00c4c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md#insn-00c4c8c4)
- 新版 [`00c4d8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d8a0.md#insn-00c4d8ac) · [`00c4d8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d8a0.md#insn-00c4d8b8)

~~~diff
- 00c4c8b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00c4c8b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c8b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c8b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4d8ac ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00c4d8ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d8ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d8ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c8b8 bytes 29613691
+ 00c4d8ac bytes 29613791
- 00c4c8c0 ["COPY", "register:4048:8", ["const:313000:8"]]
- 00c4c8c0 bytes 29b6fff0
- 00c4c8c4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00c4c8c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c8c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4c8c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4d8b8 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00c4d8b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d8b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4d8b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4c8c4 bytes 29213791
+ 00c4d8b8 bytes 29213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e0e47fb655c0e695e15212115a6a2c"></a>

### [`00c4cba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md) → [`00c4db94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4db94.md) FUN_00c4db94

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4dc04",
      "incomplete_value": false,
      "site": "00c4dc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4dc04",
      "DATA",
      [
        "storage",
        "00c99300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4dc04",
      "DATA",
      [
        "storage",
        "00c9a2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4cbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md#insn-00c4cbe0) · [`00c4cc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md#insn-00c4cc08) · [`00c4cc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md#insn-00c4cc0c)
- 新版 [`00c4dbd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4db94.md#insn-00c4dbd4) · [`00c4dbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4db94.md#insn-00c4dbfc) · [`00c4dc00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4db94.md#insn-00c4dc00)

~~~diff
- 00c4cbe0 ["INT_ADD", "register:40f0:8", ["const:c4cbe0:8", "const:4:8"]]
- 00c4cbe0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4dbd4 ["INT_ADD", "register:40f0:8", ["const:c4dbd4:8", "const:4:8"]]
+ 00c4dbd4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4cbe0 bytes 44350094
+ 00c4dbd4 bytes 3b350094
- 00c4cc08 ["COPY", "register:4048:8", ["const:c99000:8"]]
+ 00c4dbfc ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00c4cc08 bytes 690200b0
+ 00c4dbfc bytes 690200b0
- 00c4cc0c ["COPY", "tmp:0:8", ["const:300:8"]]
- 00c4cc0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4cc0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4cc0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4dc00 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 00c4dc00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4dc00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4dc00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4cc0c bytes 29010c91
+ 00c4dc00 bytes 29410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d42d1de2c8a5796e09e2ddb5640dea8c"></a>

### [`00c4ce88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md) → [`00c4de7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4de7c.md) FUN_00c4de7c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4df14",
      "incomplete_value": true,
      "site": "00c4df24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:303:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00c4df14",
      "READ",
      [
        "storage",
        "002a5238",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4df14",
      "READ",
      [
        "storage",
        "002a5303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ceb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md#insn-00c4ceb4) · [`00c4ced8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md#insn-00c4ced8) · [`00c4cf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md#insn-00c4cf04)
- 新版 [`00c4dea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4de7c.md#insn-00c4dea8) · [`00c4decc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4de7c.md#insn-00c4decc) · [`00c4def8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4de7c.md#insn-00c4def8)

~~~diff
- 00c4ceb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ceb4 ["INT_ADD", "register:40f0:8", ["const:c4ceb4:8", "const:4:8"]]
- 00c4ceb4 ["CALLIND", null, ["register:0:8"]]
+ 00c4dea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4dea8 ["INT_ADD", "register:40f0:8", ["const:c4dea8:8", "const:4:8"]]
+ 00c4dea8 ["CALLIND", null, ["register:0:8"]]
- 00c4ceb4 bytes 00013fd6
+ 00c4dea8 bytes 00013fd6
- 00c4ced8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ced8 ["INT_ADD", "register:40f0:8", ["const:c4ced8:8", "const:4:8"]]
- 00c4ced8 ["CALLIND", null, ["register:0:8"]]
+ 00c4decc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4decc ["INT_ADD", "register:40f0:8", ["const:c4decc:8", "const:4:8"]]
+ 00c4decc ["CALLIND", null, ["register:0:8"]]
- 00c4ced8 bytes 00013fd6
+ 00c4decc bytes 00013fd6
- 00c4cf04 ["INT_ADD", "register:40f0:8", ["const:c4cf04:8", "const:4:8"]]
- 00c4cf04 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4def8 ["INT_ADD", "register:40f0:8", ["const:c4def8:8", "const:4:8"]]
+ 00c4def8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4cf04 bytes 9b340094
+ 00c4def8 bytes 92340094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10d672c3043b2a20797d68574efd7ea6"></a>

### [`00c4d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md) → [`00c4e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e180.md) FUN_00c4e180

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4e1ec",
      "incomplete_value": false,
      "site": "00c4e1ec",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4e1ec",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e1ec",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md#insn-00c4d1c0) · [`00c4d1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md#insn-00c4d1e8) · [`00c4d1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md#insn-00c4d1ec)
- 新版 [`00c4e1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e180.md#insn-00c4e1b4) · [`00c4e1dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e180.md#insn-00c4e1dc) · [`00c4e1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e180.md#insn-00c4e1e0)

~~~diff
- 00c4d1c0 ["INT_ADD", "register:40f0:8", ["const:c4d1c0:8", "const:4:8"]]
- 00c4d1c0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4e1b4 ["INT_ADD", "register:40f0:8", ["const:c4e1b4:8", "const:4:8"]]
+ 00c4e1b4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4d1c0 bytes cc330094
+ 00c4e1b4 bytes c3330094
- 00c4d1e8 ["INT_ADD", "register:40f0:8", ["const:c4d1e8:8", "const:4:8"]]
- 00c4d1e8 ["CALL", null, ["callee:00c59080:8"]]
+ 00c4e1dc ["INT_ADD", "register:40f0:8", ["const:c4e1dc:8", "const:4:8"]]
+ 00c4e1dc ["CALL", null, ["callee:00c59080:8"]]
- 00c4d1e8 bytes b22b0094
+ 00c4e1dc bytes a92b0094
- 00c4d1ec ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c4e1e0 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c4d1ec bytes 490200d0
+ 00c4e1e0 bytes 490200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e376428130f8c0261fe7a7a94ba622b2"></a>

### [`00c4d238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md) → [`00c4e22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e22c.md) FUN_00c4e22c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4e294",
      "incomplete_value": false,
      "site": "00c4e294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4e294",
      "DATA",
      [
        "storage",
        "00c994c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e294",
      "DATA",
      [
        "storage",
        "00c9a490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md#insn-00c4d270) · [`00c4d290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md#insn-00c4d290) · [`00c4d294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md#insn-00c4d294)
- 新版 [`00c4e264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e22c.md#insn-00c4e264) · [`00c4e284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e22c.md#insn-00c4e284) · [`00c4e288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e22c.md#insn-00c4e288)

~~~diff
- 00c4d270 ["INT_ADD", "register:40f0:8", ["const:c4d270:8", "const:4:8"]]
- 00c4d270 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4e264 ["INT_ADD", "register:40f0:8", ["const:c4e264:8", "const:4:8"]]
+ 00c4e264 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4d270 bytes a0330094
+ 00c4e264 bytes 97330094
- 00c4d290 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4e284 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4d290 bytes 68020090
+ 00c4e284 bytes 68020090
- 00c4d294 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00c4d294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4d294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4d294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4e288 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00c4e288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4e288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4e288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4d294 bytes 08011391
+ 00c4e288 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8172de1d90a03c6b57727d7c17fe83dc"></a>

### [`00c4d868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md) → [`00c4e85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e85c.md) FUN_00c4e85c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4e8c0",
      "incomplete_value": true,
      "site": "00c4e8d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:efa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00c4e8c0",
      "READ",
      [
        "storage",
        "002a3e2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4e8c0",
      "READ",
      [
        "storage",
        "002a3efa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4d8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md#insn-00c4d8ac) · [`00c4d8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md#insn-00c4d8c4) · [`00c4d8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md#insn-00c4d8f4)
- 新版 [`00c4e8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e85c.md#insn-00c4e8a0) · [`00c4e8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e85c.md#insn-00c4e8b8) · [`00c4e8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e85c.md#insn-00c4e8e8)

~~~diff
- 00c4d8ac ["INT_ADD", "register:40f0:8", ["const:c4d8ac:8", "const:4:8"]]
- 00c4d8ac ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4e8a0 ["INT_ADD", "register:40f0:8", ["const:c4e8a0:8", "const:4:8"]]
+ 00c4e8a0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4d8ac bytes 31320094
+ 00c4e8a0 bytes 28320094
- 00c4d8c4 ["COPY", "tmp:0:8", ["const:e2f:8"]]
- 00c4d8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4d8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4d8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4e8b8 ["COPY", "tmp:0:8", ["const:efa:8"]]
+ 00c4e8b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4e8b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4e8b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4d8c4 bytes 4abd3891
+ 00c4e8b8 bytes 4ae93b91
- 00c4d8f4 ["INT_ADD", "register:40f0:8", ["const:c4d8f4:8", "const:4:8"]]
- 00c4d8f4 ["CALL", null, ["callee:00c461d4:8"]]
+ 00c4e8e8 ["INT_ADD", "register:40f0:8", ["const:c4e8e8:8", "const:4:8"]]
+ 00c4e8e8 ["CALL", null, ["callee:00c461d4:8"]]
- 00c4d8f4 bytes 3bdeff97
+ 00c4e8e8 bytes 3bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d807b0add75d967facf4b6e072690fe2"></a>

### [`00c4db64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md) → [`00c4eb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4eb58.md) FUN_00c4eb58

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4ecf0",
      "incomplete_value": true,
      "site": "00c4ecfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:737:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ed58",
      "incomplete_value": true,
      "site": "00c4ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eeb8",
      "incomplete_value": true,
      "site": "00c4eec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00c4ecf0",
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      "00c4ed58",
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ],
    [
      "00c4eeb8",
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ecf0",
      "READ",
      [
        "storage",
        "002bd737",
        null,
        "string"
      ]
    ],
    [
      "00c4ed58",
      "READ",
      [
        "storage",
        "002beb8d",
        null,
        "string"
      ]
    ],
    [
      "00c4eeb8",
      "READ",
      [
        "storage",
        "002c0eda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md#insn-00c4dbb4) · [`00c4dbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md#insn-00c4dbdc) · [`00c4dc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md#insn-00c4dc14)
- 新版 [`00c4eba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4eb58.md#insn-00c4eba8) · [`00c4ebd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4eb58.md#insn-00c4ebd0) · [`00c4ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4eb58.md#insn-00c4ec08)

~~~diff
- 00c4dbb4 ["INT_ADD", "register:40f0:8", ["const:c4dbb4:8", "const:4:8"]]
- 00c4dbb4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4eba8 ["INT_ADD", "register:40f0:8", ["const:c4eba8:8", "const:4:8"]]
+ 00c4eba8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4dbb4 bytes 6f310094
+ 00c4eba8 bytes 66310094
- 00c4dbdc ["INT_ADD", "register:40f0:8", ["const:c4dbdc:8", "const:4:8"]]
- 00c4dbdc ["CALL", null, ["callee:00c461d4:8"]]
+ 00c4ebd0 ["INT_ADD", "register:40f0:8", ["const:c4ebd0:8", "const:4:8"]]
+ 00c4ebd0 ["CALL", null, ["callee:00c461d4:8"]]
- 00c4dbdc bytes 81ddff97
+ 00c4ebd0 bytes 81ddff97
- 00c4dc14 ["INT_ADD", "register:40f0:8", ["const:c4dc14:8", "const:4:8"]]
- 00c4dc14 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4ec08 ["INT_ADD", "register:40f0:8", ["const:c4ec08:8", "const:4:8"]]
+ 00c4ec08 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4dc14 bytes 57310094
+ 00c4ec08 bytes 4e310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c11c1409f0bb13da05a7203d24d82d4"></a>

### [`00c4e0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md) → [`00c4f0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f0d0.md) FUN_00c4f0d0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 8件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 8件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

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
      "definition_site": "00c4f2c8",
      "incomplete_value": false,
      "site": "00c4f2c8",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f2ec",
      "incomplete_value": false,
      "site": "00c4f2ec",
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
            "const:aeb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f378",
      "incomplete_value": false,
      "site": "00c4f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4f2c8",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f2ec",
      "DATA",
      [
        "storage",
        "002a8993",
        null,
        "string"
      ]
    ],
    [
      "00c4f378",
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f2c8",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f2ec",
      "DATA",
      [
        "storage",
        "002a8aeb",
        null,
        "string"
      ]
    ],
    [
      "00c4f378",
      "DATA",
      [
        "storage",
        "00c9a8f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md#insn-00c4e1e0) · [`00c4e228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md#insn-00c4e228) · [`00c4e258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md#insn-00c4e258)
- 新版 [`00c4f1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f0d0.md#insn-00c4f1d4) · [`00c4f21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f0d0.md#insn-00c4f21c) · [`00c4f24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f0d0.md#insn-00c4f24c)

~~~diff
- 00c4e1e0 ["INT_ADD", "register:40f0:8", ["const:c4e1e0:8", "const:4:8"]]
- 00c4e1e0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4f1d4 ["INT_ADD", "register:40f0:8", ["const:c4f1d4:8", "const:4:8"]]
+ 00c4f1d4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4e1e0 bytes e42f0094
+ 00c4f1d4 bytes db2f0094
- 00c4e228 ["INT_ADD", "register:40f0:8", ["const:c4e228:8", "const:4:8"]]
- 00c4e228 ["CALL", null, ["callee:00c3bd5c:8"]]
+ 00c4f21c ["INT_ADD", "register:40f0:8", ["const:c4f21c:8", "const:4:8"]]
+ 00c4f21c ["CALL", null, ["callee:00c3bd5c:8"]]
- 00c4e228 bytes d0b2ff97
+ 00c4f21c bytes d0b2ff97
- 00c4e258 ["INT_ADD", "register:40f0:8", ["const:c4e258:8", "const:4:8"]]
- 00c4e258 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4f24c ["INT_ADD", "register:40f0:8", ["const:c4f24c:8", "const:4:8"]]
+ 00c4f24c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4e258 bytes a62f0094
+ 00c4f24c bytes 9d2f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfaad633f30a4edcd9a04fa9ff78001f"></a>

### [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) → [`00c4f678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) FUN_00c4f678

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 5件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c4f678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) · 呼出先 5件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c4f678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4f870",
      "incomplete_value": false,
      "site": "00c4f870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f8f8",
      "incomplete_value": false,
      "site": "00c4f8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fa08",
      "incomplete_value": false,
      "site": "00c4fa08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4f870",
      "DATA",
      [
        "storage",
        "00c99b50",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f8f8",
      "DATA",
      [
        "storage",
        "00c99ae0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4fa08",
      "DATA",
      [
        "storage",
        "00c99a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f870",
      "DATA",
      [
        "storage",
        "00c9ab20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f8f8",
      "DATA",
      [
        "storage",
        "00c9aab0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4fa08",
      "DATA",
      [
        "storage",
        "00c9aa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4e7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md#insn-00c4e7a0) · [`00c4e81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md#insn-00c4e81c) · [`00c4e844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md#insn-00c4e844)
- 新版 [`00c4f794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md#insn-00c4f794) · [`00c4f810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md#insn-00c4f810) · [`00c4f838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md#insn-00c4f838)

~~~diff
- 00c4e7a0 ["INT_ADD", "register:40f0:8", ["const:c4e7a0:8", "const:4:8"]]
- 00c4e7a0 ["CALL", null, ["callee:00c3f654:8"]]
+ 00c4f794 ["INT_ADD", "register:40f0:8", ["const:c4f794:8", "const:4:8"]]
+ 00c4f794 ["CALL", null, ["callee:00c3f654:8"]]
- 00c4e7a0 bytes b0bfff97
+ 00c4f794 bytes b0bfff97
- 00c4e81c ["INT_ADD", "register:40f0:8", ["const:c4e81c:8", "const:4:8"]]
- 00c4e81c ["CALL", null, ["callee:00c3bd5c:8"]]
+ 00c4f810 ["INT_ADD", "register:40f0:8", ["const:c4f810:8", "const:4:8"]]
+ 00c4f810 ["CALL", null, ["callee:00c3bd5c:8"]]
- 00c4e81c bytes 53b1ff97
+ 00c4f810 bytes 53b1ff97
- 00c4e844 ["INT_ADD", "register:40f0:8", ["const:c4e844:8", "const:4:8"]]
- 00c4e844 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4f838 ["INT_ADD", "register:40f0:8", ["const:c4f838:8", "const:4:8"]]
+ 00c4f838 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4e844 bytes 2b2e0094
+ 00c4f838 bytes 222e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0106b9bc253586d9e8ca3ec5ac910a9"></a>

### [`00c4ea5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md) → [`00c4fa50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fa50.md) FUN_00c4fa50

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4fabc",
      "incomplete_value": false,
      "site": "00c4fabc",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4fabc",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fabc",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md#insn-00c4ea90) · [`00c4eab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md#insn-00c4eab8) · [`00c4eabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md#insn-00c4eabc)
- 新版 [`00c4fa84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fa50.md#insn-00c4fa84) · [`00c4faac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fa50.md#insn-00c4faac) · [`00c4fab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fa50.md#insn-00c4fab0)

~~~diff
- 00c4ea90 ["INT_ADD", "register:40f0:8", ["const:c4ea90:8", "const:4:8"]]
- 00c4ea90 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fa84 ["INT_ADD", "register:40f0:8", ["const:c4fa84:8", "const:4:8"]]
+ 00c4fa84 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4ea90 bytes 982d0094
+ 00c4fa84 bytes 8f2d0094
- 00c4eab8 ["INT_ADD", "register:40f0:8", ["const:c4eab8:8", "const:4:8"]]
- 00c4eab8 ["CALL", null, ["callee:00c59080:8"]]
+ 00c4faac ["INT_ADD", "register:40f0:8", ["const:c4faac:8", "const:4:8"]]
+ 00c4faac ["CALL", null, ["callee:00c59080:8"]]
- 00c4eab8 bytes 7e250094
+ 00c4faac bytes 75250094
- 00c4eabc ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c4fab0 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c4eabc bytes 490200b0
+ 00c4fab0 bytes 490200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1500e7031725aab889419ee893f3c739"></a>

### [`00c4eb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md) → [`00c4fafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fafc.md) FUN_00c4fafc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4fb68",
      "incomplete_value": false,
      "site": "00c4fb68",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00c4fb68",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fb68",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4eb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md#insn-00c4eb3c) · [`00c4eb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md#insn-00c4eb64) · [`00c4eb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md#insn-00c4eb68)
- 新版 [`00c4fb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fafc.md#insn-00c4fb30) · [`00c4fb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fafc.md#insn-00c4fb58) · [`00c4fb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fafc.md#insn-00c4fb5c)

~~~diff
- 00c4eb3c ["INT_ADD", "register:40f0:8", ["const:c4eb3c:8", "const:4:8"]]
- 00c4eb3c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fb30 ["INT_ADD", "register:40f0:8", ["const:c4fb30:8", "const:4:8"]]
+ 00c4fb30 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4eb3c bytes 6d2d0094
+ 00c4fb30 bytes 642d0094
- 00c4eb64 ["INT_ADD", "register:40f0:8", ["const:c4eb64:8", "const:4:8"]]
- 00c4eb64 ["CALL", null, ["callee:00c59080:8"]]
+ 00c4fb58 ["INT_ADD", "register:40f0:8", ["const:c4fb58:8", "const:4:8"]]
+ 00c4fb58 ["CALL", null, ["callee:00c59080:8"]]
- 00c4eb64 bytes 53250094
+ 00c4fb58 bytes 4a250094
- 00c4eb68 ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c4fb5c ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c4eb68 bytes 490200b0
+ 00c4fb5c bytes 490200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02a94a9d75e76d21edab4854d3fa4e2"></a>

### [`00c4ebb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md) → [`00c4fba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fba8.md) FUN_00c4fba8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4fc14",
      "incomplete_value": false,
      "site": "00c4fc14",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ec20",
      "incomplete_value": false,
      "site": "00c4ec20",
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
      "00c4fc14",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fc14",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ebe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md#insn-00c4ebe8) · [`00c4ec10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md#insn-00c4ec10) · [`00c4ec14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md#insn-00c4ec14)
- 新版 [`00c4fbdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fba8.md#insn-00c4fbdc) · [`00c4fc04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fba8.md#insn-00c4fc04) · [`00c4fc08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fba8.md#insn-00c4fc08)

~~~diff
- 00c4ebe8 ["INT_ADD", "register:40f0:8", ["const:c4ebe8:8", "const:4:8"]]
- 00c4ebe8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fbdc ["INT_ADD", "register:40f0:8", ["const:c4fbdc:8", "const:4:8"]]
+ 00c4fbdc ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4ebe8 bytes 422d0094
+ 00c4fbdc bytes 392d0094
- 00c4ec10 ["INT_ADD", "register:40f0:8", ["const:c4ec10:8", "const:4:8"]]
- 00c4ec10 ["CALL", null, ["callee:00c59080:8"]]
+ 00c4fc04 ["INT_ADD", "register:40f0:8", ["const:c4fc04:8", "const:4:8"]]
+ 00c4fc04 ["CALL", null, ["callee:00c59080:8"]]
- 00c4ec10 bytes 28250094
+ 00c4fc04 bytes 1f250094
- 00c4ec14 ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c4fc08 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c4ec14 bytes 490200b0
+ 00c4fc08 bytes 490200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dda08409f1985b957ae3318a8d81483"></a>

### [`00c4ec60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md) → [`00c4fc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fc54.md) FUN_00c4fc54

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4fcbc",
      "incomplete_value": false,
      "site": "00c4fcbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ecc8",
      "incomplete_value": false,
      "site": "00c4ecc8",
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
            "const:bc0:8"
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
      "00c4fcbc",
      "DATA",
      [
        "storage",
        "00c99bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fcbc",
      "DATA",
      [
        "storage",
        "00c9ab90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ec98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md#insn-00c4ec98) · [`00c4ecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md#insn-00c4ecb8) · [`00c4ecbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md#insn-00c4ecbc)
- 新版 [`00c4fc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fc54.md#insn-00c4fc8c) · [`00c4fcac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fc54.md#insn-00c4fcac) · [`00c4fcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fc54.md#insn-00c4fcb0)

~~~diff
- 00c4ec98 ["INT_ADD", "register:40f0:8", ["const:c4ec98:8", "const:4:8"]]
- 00c4ec98 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fc8c ["INT_ADD", "register:40f0:8", ["const:c4fc8c:8", "const:4:8"]]
+ 00c4fc8c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4ec98 bytes 162d0094
+ 00c4fc8c bytes 0d2d0094
- 00c4ecb8 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4fcac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4ecb8 bytes 480200f0
+ 00c4fcac bytes 480200f0
- 00c4ecbc ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00c4ecbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ecbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ecbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4fcb0 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00c4fcb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fcb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fcb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ecbc bytes 08012f91
+ 00c4fcb0 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636ebf972931c47b3b19a30dc98d0778"></a>

### [`00c4ed0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md) → [`00c4fd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fd00.md) FUN_00c4fd00

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4fd64",
      "incomplete_value": false,
      "site": "00c4fd64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ed70",
      "incomplete_value": false,
      "site": "00c4ed70",
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
            "const:c30:8"
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
      "00c4fd64",
      "DATA",
      [
        "storage",
        "00c99c30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fd64",
      "DATA",
      [
        "storage",
        "00c9ac00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ed40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md#insn-00c4ed40) · [`00c4ed60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md#insn-00c4ed60) · [`00c4ed64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md#insn-00c4ed64)
- 新版 [`00c4fd34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fd00.md#insn-00c4fd34) · [`00c4fd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fd00.md#insn-00c4fd54) · [`00c4fd58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fd00.md#insn-00c4fd58)

~~~diff
- 00c4ed40 ["INT_ADD", "register:40f0:8", ["const:c4ed40:8", "const:4:8"]]
- 00c4ed40 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fd34 ["INT_ADD", "register:40f0:8", ["const:c4fd34:8", "const:4:8"]]
+ 00c4fd34 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4ed40 bytes ec2c0094
+ 00c4fd34 bytes e32c0094
- 00c4ed60 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4fd54 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4ed60 bytes 480200f0
+ 00c4fd54 bytes 480200f0
- 00c4ed64 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 00c4ed64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ed64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ed64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4fd58 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00c4fd58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fd58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fd58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ed64 bytes 08c13091
+ 00c4fd58 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ab761e441c7e1c4479373da2018d0e"></a>

### [`00c4edac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md) → [`00c4fda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fda0.md) FUN_00c4fda0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4fe08",
      "incomplete_value": false,
      "site": "00c4fe08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ee14",
      "incomplete_value": false,
      "site": "00c4ee14",
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
            "const:ca0:8"
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
      "00c4fe08",
      "DATA",
      [
        "storage",
        "00c99ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fe08",
      "DATA",
      [
        "storage",
        "00c9ac70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ede4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md#insn-00c4ede4) · [`00c4ee04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md#insn-00c4ee04) · [`00c4ee08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md#insn-00c4ee08)
- 新版 [`00c4fdd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fda0.md#insn-00c4fdd8) · [`00c4fdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fda0.md#insn-00c4fdf8) · [`00c4fdfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fda0.md#insn-00c4fdfc)

~~~diff
- 00c4ede4 ["INT_ADD", "register:40f0:8", ["const:c4ede4:8", "const:4:8"]]
- 00c4ede4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fdd8 ["INT_ADD", "register:40f0:8", ["const:c4fdd8:8", "const:4:8"]]
+ 00c4fdd8 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4ede4 bytes c32c0094
+ 00c4fdd8 bytes ba2c0094
- 00c4ee04 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4fdf8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4ee04 bytes 480200f0
+ 00c4fdf8 bytes 480200f0
- 00c4ee08 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c4ee08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ee08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ee08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4fdfc ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00c4fdfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fdfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fdfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ee08 bytes 08813291
+ 00c4fdfc bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184166833d7080bc6bc3382da55c9971"></a>

### [`00c4ee58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md) → [`00c4fe4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fe4c.md) FUN_00c4fe4c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4feb4",
      "incomplete_value": false,
      "site": "00c4feb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eec0",
      "incomplete_value": false,
      "site": "00c4eec0",
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
            "const:d10:8"
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
      "00c4feb4",
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4feb4",
      "DATA",
      [
        "storage",
        "00c9ace0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md#insn-00c4ee90) · [`00c4eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md#insn-00c4eeb0) · [`00c4eeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md#insn-00c4eeb4)
- 新版 [`00c4fe84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fe4c.md#insn-00c4fe84) · [`00c4fea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fe4c.md#insn-00c4fea4) · [`00c4fea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fe4c.md#insn-00c4fea8)

~~~diff
- 00c4ee90 ["INT_ADD", "register:40f0:8", ["const:c4ee90:8", "const:4:8"]]
- 00c4ee90 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4fe84 ["INT_ADD", "register:40f0:8", ["const:c4fe84:8", "const:4:8"]]
+ 00c4fe84 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4ee90 bytes 982c0094
+ 00c4fe84 bytes 8f2c0094
- 00c4eeb0 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4fea4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4eeb0 bytes 480200f0
+ 00c4fea4 bytes 480200f0
- 00c4eeb4 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00c4eeb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4eeb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4eeb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4fea8 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00c4fea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4eeb4 bytes 08413491
+ 00c4fea8 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0dbea357d16af6abecaa4009cfb5fe5"></a>

### [`00c4ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) → [`00c4fef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md) FUN_00c4fef8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 6件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c508cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md) [`00c5096c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 6件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c518c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c518c0.md) [`00c51960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51960.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fff4",
      "incomplete_value": false,
      "site": "00c4fff4",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f000",
      "incomplete_value": false,
      "site": "00c4f000",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c500d0",
      "incomplete_value": false,
      "site": "00c500d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
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
            "const:df0:8"
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
      "definition_site": "00c5016c",
      "incomplete_value": false,
      "site": "00c5016c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f178",
      "incomplete_value": false,
      "site": "00c4f178",
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
            "const:df0:8"
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
      "00c4fff4",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c500d0",
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c5016c",
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4fff4",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c500d0",
      "DATA",
      [
        "storage",
        "00c9adc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c5016c",
      "DATA",
      [
        "storage",
        "00c9adc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4efc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md#insn-00c4efc8) · [`00c4eff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md#insn-00c4eff8) · [`00c4effc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md#insn-00c4effc)
- 新版 [`00c4ffbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md#insn-00c4ffbc) · [`00c4ffec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md#insn-00c4ffec) · [`00c4fff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md#insn-00c4fff0)

~~~diff
- 00c4efc8 ["INT_ADD", "register:40f0:8", ["const:c4efc8:8", "const:4:8"]]
- 00c4efc8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4ffbc ["INT_ADD", "register:40f0:8", ["const:c4ffbc:8", "const:4:8"]]
+ 00c4ffbc ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4efc8 bytes 4a2c0094
+ 00c4ffbc bytes 412c0094
- 00c4eff8 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c4ffec ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c4eff8 bytes 480200b0
+ 00c4ffec bytes 480200b0
- 00c4effc ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c4effc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4effc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4effc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4fff0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00c4fff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4fff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4effc bytes 08411c91
+ 00c4fff0 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e862a52f091016a95f34497c3f8c92d1"></a>

### [`00c4f1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md) → [`00c501b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c501b4.md) FUN_00c501b4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.05% / 新版 94.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c502c0",
      "incomplete_value": false,
      "site": "00c502c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f2cc",
      "incomplete_value": false,
      "site": "00c4f2cc",
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
            "const:f40:8"
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
      "00c502c0",
      "DATA",
      [
        "storage",
        "00c99f40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c502e0",
      "DATA",
      [
        "storage",
        "002b367d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c502c0",
      "DATA",
      [
        "storage",
        "00c9af10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c502e0",
      "DATA",
      [
        "storage",
        "002b36c7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md#insn-00c4f238) · [`00c4f248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md#insn-00c4f248) · [`00c4f258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md#insn-00c4f258)
- 新版 [`00c5022c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c501b4.md#insn-00c5022c) · [`00c5023c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c501b4.md#insn-00c5023c) · [`00c5024c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c501b4.md#insn-00c5024c)

~~~diff
- 00c4f238 ["COPY", "tmp:0:8", ["const:67d:8"]]
- 00c4f238 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f238 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f238 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c5022c ["COPY", "tmp:0:8", ["const:6c7:8"]]
+ 00c5022c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c5022c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c5022c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4f238 bytes 73f61991
+ 00c5022c bytes 731e1b91
- 00c4f248 ["COPY", "tmp:0:8", ["const:c5e:8"]]
- 00c4f248 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f248 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f248 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c5023c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00c5023c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c5023c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c5023c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4f248 bytes 737a3191
+ 00c5023c bytes 73a23291
- 00c4f258 ["COPY", "tmp:0:8", ["const:7eb:8"]]
- 00c4f258 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f258 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f258 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c5024c ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00c5024c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c5024c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c5024c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4f258 bytes 73ae1f91
+ 00c5024c bytes 73e22291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b0bc1c779b3fe837f119d7fe5bcf1f8"></a>

### [`00c4f310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md) → [`00c50304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50304.md) FUN_00c50304

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c5036c",
      "incomplete_value": false,
      "site": "00c5036c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f378",
      "incomplete_value": false,
      "site": "00c4f378",
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
            "const:fb0:8"
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
      "00c5036c",
      "DATA",
      [
        "storage",
        "00c99fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c5036c",
      "DATA",
      [
        "storage",
        "00c9af80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md#insn-00c4f344) · [`00c4f36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md#insn-00c4f36c) · [`00c4f370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md#insn-00c4f370)
- 新版 [`00c50338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50304.md#insn-00c50338) · [`00c50360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50304.md#insn-00c50360) · [`00c50364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50304.md#insn-00c50364)

~~~diff
- 00c4f344 ["INT_ADD", "register:40f0:8", ["const:c4f344:8", "const:4:8"]]
- 00c4f344 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c50338 ["INT_ADD", "register:40f0:8", ["const:c50338:8", "const:4:8"]]
+ 00c50338 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4f344 bytes 6b2b0094
+ 00c50338 bytes 622b0094
- 00c4f36c ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c50360 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4f36c bytes 480200d0
+ 00c50360 bytes 480200d0
- 00c4f370 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00c4f370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50364 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00c50364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f370 bytes 08c13e91
+ 00c50364 bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0f7896834590320af9ebb36f00a76a"></a>

### [`00c4f3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md) → [`00c503b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c503b0.md) FUN_00c503b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c50424",
      "incomplete_value": false,
      "site": "00c50424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f430",
      "incomplete_value": false,
      "site": "00c4f430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "00c50424",
      "DATA",
      [
        "storage",
        "00c9a020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50424",
      "DATA",
      [
        "storage",
        "00c9aff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md#insn-00c4f3f4) · [`00c4f420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md#insn-00c4f420) · [`00c4f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md#insn-00c4f474)
- 新版 [`00c503e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c503b0.md#insn-00c503e8) · [`00c50414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c503b0.md#insn-00c50414) · [`00c50468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c503b0.md#insn-00c50468)

~~~diff
- 00c4f3f4 ["INT_ADD", "register:40f0:8", ["const:c4f3f4:8", "const:4:8"]]
- 00c4f3f4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c503e8 ["INT_ADD", "register:40f0:8", ["const:c503e8:8", "const:4:8"]]
+ 00c503e8 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4f3f4 bytes 3f2b0094
+ 00c503e8 bytes 362b0094
- 00c4f420 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00c4f420 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4f420 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4f420 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c50414 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00c50414 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c50414 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c50414 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4f420 bytes 4a810091
+ 00c50414 bytes 4ac13f91
- 00c4f474 ["INT_ADD", "register:40f0:8", ["const:c4f474:8", "const:4:8"]]
- 00c4f474 ["CALL", null, ["callee:00c590c0:8"]]
+ 00c50468 ["INT_ADD", "register:40f0:8", ["const:c50468:8", "const:4:8"]]
+ 00c50468 ["CALL", null, ["callee:00c590c0:8"]]
- 00c4f474 bytes 1f230094
+ 00c50468 bytes 16230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fde8133705946b7ec8ce5b8245f6000a"></a>

### [`00c4f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md) → [`00c5046c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5046c.md) FUN_00c5046c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c504d0",
      "incomplete_value": false,
      "site": "00c504d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f4dc",
      "incomplete_value": false,
      "site": "00c4f4dc",
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
            "const:d10:8"
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
      "definition_site": "00c504f0",
      "incomplete_value": false,
      "site": "00c504f0",
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
            "const:667:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f4fc",
      "incomplete_value": false,
      "site": "00c4f4fc",
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
            "const:50f:8"
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
      "00c504d0",
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c504f0",
      "DATA",
      [
        "storage",
        "002a750f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c504d0",
      "DATA",
      [
        "storage",
        "00c9ace0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c504f0",
      "DATA",
      [
        "storage",
        "002a7667",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md#insn-00c4f4ac) · [`00c4f4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md#insn-00c4f4cc) · [`00c4f4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md#insn-00c4f4d0)
- 新版 [`00c504a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5046c.md#insn-00c504a0) · [`00c504c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5046c.md#insn-00c504c0) · [`00c504c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5046c.md#insn-00c504c4)

~~~diff
- 00c4f4ac ["INT_ADD", "register:40f0:8", ["const:c4f4ac:8", "const:4:8"]]
- 00c4f4ac ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c504a0 ["INT_ADD", "register:40f0:8", ["const:c504a0:8", "const:4:8"]]
+ 00c504a0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4f4ac bytes 112b0094
+ 00c504a0 bytes 082b0094
- 00c4f4cc ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c504c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4f4cc bytes 480200d0
+ 00c504c0 bytes 480200d0
- 00c4f4d0 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00c4f4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c504c4 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00c504c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c504c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c504c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f4d0 bytes 08413491
+ 00c504c4 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6c4b3ac6bbd59f2547e448d1990edfa"></a>

### [`00c4f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md) → [`00c5051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5051c.md) FUN_00c5051c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c50580",
      "incomplete_value": false,
      "site": "00c50580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f58c",
      "incomplete_value": false,
      "site": "00c4f58c",
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
            "const:d10:8"
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
      "definition_site": "00c505a0",
      "incomplete_value": false,
      "site": "00c505a0",
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
            "const:ef9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f5ac",
      "incomplete_value": false,
      "site": "00c4f5ac",
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
            "const:eb9:8"
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
      "00c50580",
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c505a0",
      "DATA",
      [
        "storage",
        "002a0eb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c50580",
      "DATA",
      [
        "storage",
        "00c9ace0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c505a0",
      "DATA",
      [
        "storage",
        "002a0ef9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md#insn-00c4f55c) · [`00c4f57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md#insn-00c4f57c) · [`00c4f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md#insn-00c4f580)
- 新版 [`00c50550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5051c.md#insn-00c50550) · [`00c50570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5051c.md#insn-00c50570) · [`00c50574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5051c.md#insn-00c50574)

~~~diff
- 00c4f55c ["INT_ADD", "register:40f0:8", ["const:c4f55c:8", "const:4:8"]]
- 00c4f55c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c50550 ["INT_ADD", "register:40f0:8", ["const:c50550:8", "const:4:8"]]
+ 00c50550 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4f55c bytes e52a0094
+ 00c50550 bytes dc2a0094
- 00c4f57c ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c50570 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c4f57c bytes 480200d0
+ 00c50570 bytes 480200d0
- 00c4f580 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00c4f580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50574 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00c50574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f580 bytes 08413491
+ 00c50574 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3113c47d66042803c15559aa57ea5b2b"></a>

### [`00c4fa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md) → [`00c50a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50a30.md) FUN_00c50a30

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50bc0",
      "incomplete_value": true,
      "site": "00c50bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:737:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4fbcc",
      "incomplete_value": true,
      "site": "00c4fbd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50c28",
      "incomplete_value": true,
      "site": "00c50c34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4fc34",
      "incomplete_value": true,
      "site": "00c4fc40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c50bc0",
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      "00c50c28",
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c50bc0",
      "READ",
      [
        "storage",
        "002bd737",
        null,
        "string"
      ]
    ],
    [
      "00c50c28",
      "READ",
      [
        "storage",
        "002beb8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md#insn-00c4fa88) · [`00c4fab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md#insn-00c4fab0) · [`00c4fae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md#insn-00c4fae8)
- 新版 [`00c50a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50a30.md#insn-00c50a7c) · [`00c50aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50a30.md#insn-00c50aa4) · [`00c50adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50a30.md#insn-00c50adc)

~~~diff
- 00c4fa88 ["INT_ADD", "register:40f0:8", ["const:c4fa88:8", "const:4:8"]]
- 00c4fa88 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50a7c ["INT_ADD", "register:40f0:8", ["const:c50a7c:8", "const:4:8"]]
+ 00c50a7c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4fa88 bytes ba290094
+ 00c50a7c bytes b1290094
- 00c4fab0 ["INT_ADD", "register:40f0:8", ["const:c4fab0:8", "const:4:8"]]
- 00c4fab0 ["CALL", null, ["callee:00c461d4:8"]]
+ 00c50aa4 ["INT_ADD", "register:40f0:8", ["const:c50aa4:8", "const:4:8"]]
+ 00c50aa4 ["CALL", null, ["callee:00c461d4:8"]]
- 00c4fab0 bytes ccd5ff97
+ 00c50aa4 bytes ccd5ff97
- 00c4fae8 ["INT_ADD", "register:40f0:8", ["const:c4fae8:8", "const:4:8"]]
- 00c4fae8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c50adc ["INT_ADD", "register:40f0:8", ["const:c50adc:8", "const:4:8"]]
+ 00c50adc ["CALL", null, ["callee:00c5b140:8"]]
- 00c4fae8 bytes a2290094
+ 00c50adc bytes 99290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dea4ca10a31e61f101d164e849f7944"></a>

### [`00c50150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md) → [`00c51144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51144.md) FUN_00c51144

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c5121c",
      "incomplete_value": true,
      "site": "00c51228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:737:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50228",
      "incomplete_value": true,
      "site": "00c50234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c51284",
      "incomplete_value": true,
      "site": "00c51290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50290",
      "incomplete_value": true,
      "site": "00c5029c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c5121c",
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      "00c51284",
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c5121c",
      "READ",
      [
        "storage",
        "002bd737",
        null,
        "string"
      ]
    ],
    [
      "00c51284",
      "READ",
      [
        "storage",
        "002beb8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md#insn-00c50174) · [`00c501a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md#insn-00c501a8) · [`00c5020c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md#insn-00c5020c)
- 新版 [`00c51168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51144.md#insn-00c51168) · [`00c5119c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51144.md#insn-00c5119c) · [`00c51200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51144.md#insn-00c51200)

~~~diff
- 00c50174 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50174 ["INT_ADD", "register:40f0:8", ["const:c50174:8", "const:4:8"]]
- 00c50174 ["CALLIND", null, ["register:0:8"]]
+ 00c51168 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51168 ["INT_ADD", "register:40f0:8", ["const:c51168:8", "const:4:8"]]
+ 00c51168 ["CALLIND", null, ["register:0:8"]]
- 00c50174 bytes 00013fd6
+ 00c51168 bytes 00013fd6
- 00c501a8 ["INT_ADD", "register:40f0:8", ["const:c501a8:8", "const:4:8"]]
- 00c501a8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c5119c ["INT_ADD", "register:40f0:8", ["const:c5119c:8", "const:4:8"]]
+ 00c5119c ["CALL", null, ["callee:00c5b140:8"]]
- 00c501a8 bytes f2270094
+ 00c5119c bytes e9270094
- 00c5020c ["INT_ADD", "register:40f0:8", ["const:c5020c:8", "const:4:8"]]
- 00c5020c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51200 ["INT_ADD", "register:40f0:8", ["const:c51200:8", "const:4:8"]]
+ 00c51200 ["CALL", null, ["callee:00c5b140:8"]]
- 00c5020c bytes d9270094
+ 00c51200 bytes d0270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5727ffc9cc5a93d8ffbdd43a85ef00"></a>

### [`00c50538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md) → [`00c5152c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5152c.md) FUN_00c5152c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c51594",
      "incomplete_value": true,
      "site": "00c515a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:670:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c505a0",
      "incomplete_value": true,
      "site": "00c505ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
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
      "00c51594",
      "READ",
      [
        "storage",
        "002a7518",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c51594",
      "READ",
      [
        "storage",
        "002a7670",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md#insn-00c50584) · [`00c50598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md#insn-00c50598) · [`00c505e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md#insn-00c505e4)
- 新版 [`00c51578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5152c.md#insn-00c51578) · [`00c5158c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5152c.md#insn-00c5158c) · [`00c515d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c5152c.md#insn-00c515d8)

~~~diff
- 00c50584 ["INT_ADD", "register:40f0:8", ["const:c50584:8", "const:4:8"]]
- 00c50584 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51578 ["INT_ADD", "register:40f0:8", ["const:c51578:8", "const:4:8"]]
+ 00c51578 ["CALL", null, ["callee:00c5b140:8"]]
- 00c50584 bytes fb260094
+ 00c51578 bytes f2260094
- 00c50598 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00c50598 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c50598 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c50598 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c5158c ["COPY", "tmp:0:8", ["const:670:8"]]
+ 00c5158c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c5158c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c5158c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c50598 bytes 29611491
+ 00c5158c bytes 29c11991
- 00c505e4 ["INT_ADD", "register:40f0:8", ["const:c505e4:8", "const:4:8"]]
- 00c505e4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c515d8 ["INT_ADD", "register:40f0:8", ["const:c515d8:8", "const:4:8"]]
+ 00c515d8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c505e4 bytes e3260094
+ 00c515d8 bytes da260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a5e129f01cd890fa670298d05d19811"></a>

### [`00c508cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md) → [`00c518c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c518c0.md) FUN_00c518c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c4fef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c51924",
      "incomplete_value": false,
      "site": "00c51924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50930",
      "incomplete_value": false,
      "site": "00c50930",
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
            "const:d80:8"
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
      "00c51924",
      "DATA",
      [
        "storage",
        "00c99d80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c51924",
      "DATA",
      [
        "storage",
        "00c9ad50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md#insn-00c50900) · [`00c50920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md#insn-00c50920) · [`00c50924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md#insn-00c50924)
- 新版 [`00c518f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c518c0.md#insn-00c518f4) · [`00c51914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c518c0.md#insn-00c51914) · [`00c51918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c518c0.md#insn-00c51918)

~~~diff
- 00c50900 ["INT_ADD", "register:40f0:8", ["const:c50900:8", "const:4:8"]]
- 00c50900 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c518f4 ["INT_ADD", "register:40f0:8", ["const:c518f4:8", "const:4:8"]]
+ 00c518f4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c50900 bytes fc250094
+ 00c518f4 bytes f3250094
- 00c50920 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c51914 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c50920 bytes 480200b0
+ 00c51914 bytes 480200b0
- 00c50924 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00c50924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c51918 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00c51918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c51918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c51918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50924 bytes 08013691
+ 00c51918 bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6512b84ec69a54a2f9dbb74cef884b3c"></a>

### [`00c5096c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md) → [`00c51960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51960.md) FUN_00c51960

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c4fef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c519c8",
      "incomplete_value": false,
      "site": "00c519c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c509d4",
      "incomplete_value": false,
      "site": "00c509d4",
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
            "const:df0:8"
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
      "00c519c8",
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c519c8",
      "DATA",
      [
        "storage",
        "00c9adc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c509a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md#insn-00c509a4) · [`00c509c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md#insn-00c509c4) · [`00c509c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md#insn-00c509c8)
- 新版 [`00c51998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51960.md#insn-00c51998) · [`00c519b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51960.md#insn-00c519b8) · [`00c519bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51960.md#insn-00c519bc)

~~~diff
- 00c509a4 ["INT_ADD", "register:40f0:8", ["const:c509a4:8", "const:4:8"]]
- 00c509a4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c51998 ["INT_ADD", "register:40f0:8", ["const:c51998:8", "const:4:8"]]
+ 00c51998 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c509a4 bytes d3250094
+ 00c51998 bytes ca250094
- 00c509c4 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c519b8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c509c4 bytes 480200b0
+ 00c519b8 bytes 480200b0
- 00c509c8 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 00c509c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c509c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c509c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c519bc ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00c519bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c519bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c519bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c509c8 bytes 08c13791
+ 00c519bc bytes 08013791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d44a5a43a985d47977e12cc92a83c539"></a>

### [`00c50a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md) → [`00c51a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51a08.md) FUN_00c51a08

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c51a6c",
      "incomplete_value": true,
      "site": "00c51a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50a78",
      "incomplete_value": true,
      "site": "00c50a84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b14:8"
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
      "definition_site": "00c51a7c",
      "incomplete_value": true,
      "site": "00c51a7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c50a88",
      "incomplete_value": true,
      "site": "00c50a88",
      "value": [
        "LOAD",
        "8",
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
      "00c51a6c",
      "READ",
      [
        "storage",
        "002bfb14",
        null,
        "string"
      ]
    ],
    [
      "00c51a70",
      "READ",
      [
        "storage",
        "002bfb19",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c51a6c",
      "READ",
      [
        "storage",
        "002bfbf2",
        null,
        "string"
      ]
    ],
    [
      "00c51a70",
      "READ",
      [
        "storage",
        "002bfbf7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md#insn-00c50a58) · [`00c50a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md#insn-00c50a70) · [`00c50aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md#insn-00c50aa8)
- 新版 [`00c51a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51a08.md#insn-00c51a4c) · [`00c51a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51a08.md#insn-00c51a64) · [`00c51a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51a08.md#insn-00c51a9c)

~~~diff
- 00c50a58 ["INT_ADD", "register:40f0:8", ["const:c50a58:8", "const:4:8"]]
- 00c50a58 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51a4c ["INT_ADD", "register:40f0:8", ["const:c51a4c:8", "const:4:8"]]
+ 00c51a4c ["CALL", null, ["callee:00c5b140:8"]]
- 00c50a58 bytes c6250094
+ 00c51a4c bytes bd250094
- 00c50a70 ["COPY", "tmp:0:8", ["const:b14:8"]]
- 00c50a70 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c50a70 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c50a70 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c51a64 ["COPY", "tmp:0:8", ["const:bf2:8"]]
+ 00c51a64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c51a64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c51a64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c50a70 bytes 4a512c91
+ 00c51a64 bytes 4ac92f91
- 00c50aa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50aa8 ["INT_ADD", "register:40f0:8", ["const:c50aa8:8", "const:4:8"]]
- 00c50aa8 ["CALLIND", null, ["register:0:8"]]
+ 00c51a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51a9c ["INT_ADD", "register:40f0:8", ["const:c51a9c:8", "const:4:8"]]
+ 00c51a9c ["CALLIND", null, ["register:0:8"]]
- 00c50aa8 bytes 00013fd6
+ 00c51a9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a5abe40688b3aff8c55871377c8676"></a>

### [`00c50c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md) → [`00c51c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51c8c.md) FUN_00c51c8c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c51cf4",
      "incomplete_value": false,
      "site": "00c51cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50d00",
      "incomplete_value": false,
      "site": "00c50d00",
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
            "const:e60:8"
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
      "00c51cf4",
      "DATA",
      [
        "storage",
        "00c99e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c51cf4",
      "DATA",
      [
        "storage",
        "00c9ae30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md#insn-00c50cd0) · [`00c50cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md#insn-00c50cf0) · [`00c50cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md#insn-00c50cf4)
- 新版 [`00c51cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51c8c.md#insn-00c51cc4) · [`00c51ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51c8c.md#insn-00c51ce4) · [`00c51ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51c8c.md#insn-00c51ce8)

~~~diff
- 00c50cd0 ["INT_ADD", "register:40f0:8", ["const:c50cd0:8", "const:4:8"]]
- 00c50cd0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c51cc4 ["INT_ADD", "register:40f0:8", ["const:c51cc4:8", "const:4:8"]]
+ 00c51cc4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c50cd0 bytes 08250094
+ 00c51cc4 bytes ff240094
- 00c50cf0 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c51ce4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c50cf0 bytes 480200b0
+ 00c51ce4 bytes 480200b0
- 00c50cf4 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 00c50cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c51ce8 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00c51ce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c51ce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c51ce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50cf4 bytes 08813991
+ 00c51ce8 bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54bf2f0fee7b45da47e3e29b24bf7914"></a>

### [`00c50d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md) → [`00c51d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51d5c.md) FUN_00c51d5c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51ed8",
      "incomplete_value": false,
      "site": "00c51ef0",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50ee4",
      "incomplete_value": false,
      "site": "00c50efc",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51ee0",
      "incomplete_value": false,
      "site": "00c51ef0",
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
            "const:5fb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50eec",
      "incomplete_value": false,
      "site": "00c50efc",
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
            "const:52e:8"
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
      "definition_site": "00c51ee8",
      "incomplete_value": false,
      "site": "00c51ef0",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50ef4",
      "incomplete_value": false,
      "site": "00c50efc",
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
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c51ed8",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c51ee0",
      "PARAM",
      [
        "storage",
        "002ac52e",
        null,
        "string"
      ]
    ],
    [
      "00c51ee8",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c51ed8",
      "PARAM",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ],
    [
      "00c51ee0",
      "PARAM",
      [
        "storage",
        "002ac5fb",
        null,
        "string"
      ]
    ],
    [
      "00c51ee8",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md#insn-00c50efc) · [`00c50dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md#insn-00c50dc4) · [`00c50e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md#insn-00c50e0c)
- 新版 [`00c51ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51d5c.md#insn-00c51ef0) · [`00c51db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51d5c.md#insn-00c51db8) · [`00c51e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51d5c.md#insn-00c51e00)

~~~diff
- 00c50efc ["INT_ADD", "register:40f0:8", ["const:c50efc:8", "const:4:8"]]
- 00c50efc ["CALL", null, ["callee:00c3909c:8"]]
+ 00c51ef0 ["INT_ADD", "register:40f0:8", ["const:c51ef0:8", "const:4:8"]]
+ 00c51ef0 ["CALL", null, ["callee:00c3909c:8"]]
- 00c50efc bytes 6b9cff97
+ 00c51ef0 bytes 6b9cff97
- 00c50dc4 ["INT_ADD", "register:40f0:8", ["const:c50dc4:8", "const:4:8"]]
- 00c50dc4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51db8 ["INT_ADD", "register:40f0:8", ["const:c51db8:8", "const:4:8"]]
+ 00c51db8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c50dc4 bytes eb240094
+ 00c51db8 bytes e2240094
- 00c50e0c ["INT_ADD", "register:40f0:8", ["const:c50e0c:8", "const:4:8"]]
- 00c50e0c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c51e00 ["INT_ADD", "register:40f0:8", ["const:c51e00:8", "const:4:8"]]
+ 00c51e00 ["CALL", null, ["callee:00c5b140:8"]]
- 00c50e0c bytes d9240094
+ 00c51e00 bytes d0240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d22a7380a06112967cbe0c9e5f405cf"></a>

### [`00c50f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md) → [`00c51f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51f08.md) FUN_00c51f08

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c51f74",
      "incomplete_value": false,
      "site": "00c51f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50f80",
      "incomplete_value": false,
      "site": "00c50f80",
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
            "const:ed0:8"
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
      "00c51f74",
      "DATA",
      [
        "storage",
        "00c99ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c51f74",
      "DATA",
      [
        "storage",
        "00c9aea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md#insn-00c50f4c) · [`00c50f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md#insn-00c50f74) · [`00c50f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md#insn-00c50f78)
- 新版 [`00c51f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51f08.md#insn-00c51f40) · [`00c51f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51f08.md#insn-00c51f68) · [`00c51f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51f08.md#insn-00c51f6c)

~~~diff
- 00c50f4c ["INT_ADD", "register:40f0:8", ["const:c50f4c:8", "const:4:8"]]
- 00c50f4c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c51f40 ["INT_ADD", "register:40f0:8", ["const:c51f40:8", "const:4:8"]]
+ 00c51f40 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c50f4c bytes 69240094
+ 00c51f40 bytes 60240094
- 00c50f74 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c51f68 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c50f74 bytes 480200b0
+ 00c51f68 bytes 480200b0
- 00c50f78 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00c50f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c51f6c ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00c51f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c51f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c51f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50f78 bytes 08413b91
+ 00c51f6c bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57fdcffe2c2fc5e3e64b0137db7840cb"></a>

### [`00c51c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md) → [`00c52c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52c04.md) FUN_00c52c04

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c518d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md) [`00c51ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md) · 呼出先 6件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)
- 新版 呼出元 2件 [`00c528cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c528cc.md) [`00c52adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52adc.md) · 呼出先 6件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c52d6c",
      "incomplete_value": false,
      "site": "00c52d84",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c51d78",
      "incomplete_value": false,
      "site": "00c51d90",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c52d74",
      "incomplete_value": false,
      "site": "00c52d84",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c51d80",
      "incomplete_value": false,
      "site": "00c51d90",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c52d7c",
      "incomplete_value": false,
      "site": "00c52d84",
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
            "const:aad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c51d88",
      "incomplete_value": false,
      "site": "00c51d90",
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
            "const:955:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c52d6c",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c52d74",
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      "00c52d7c",
      "PARAM",
      [
        "storage",
        "002a8955",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c52d6c",
      "PARAM",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ],
    [
      "00c52d74",
      "PARAM",
      [
        "storage",
        "002b2911",
        null,
        "string"
      ]
    ],
    [
      "00c52d7c",
      "PARAM",
      [
        "storage",
        "002a8aad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md#insn-00c51d90) · [`00c51c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md#insn-00c51c68) · [`00c51ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md#insn-00c51ca8)
- 新版 [`00c52d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52c04.md#insn-00c52d84) · [`00c52c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52c04.md#insn-00c52c5c) · [`00c52c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52c04.md#insn-00c52c9c)

~~~diff
- 00c51d90 ["INT_ADD", "register:40f0:8", ["const:c51d90:8", "const:4:8"]]
- 00c51d90 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c52d84 ["INT_ADD", "register:40f0:8", ["const:c52d84:8", "const:4:8"]]
+ 00c52d84 ["CALL", null, ["callee:00c3909c:8"]]
- 00c51d90 bytes c698ff97
+ 00c52d84 bytes c698ff97
- 00c51c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51c68 ["INT_ADD", "register:40f0:8", ["const:c51c68:8", "const:4:8"]]
- 00c51c68 ["CALLIND", null, ["register:0:8"]]
+ 00c52c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52c5c ["INT_ADD", "register:40f0:8", ["const:c52c5c:8", "const:4:8"]]
+ 00c52c5c ["CALLIND", null, ["register:0:8"]]
- 00c51c68 bytes 00013fd6
+ 00c52c5c bytes 00013fd6
- 00c51ca8 ["INT_ADD", "register:40f0:8", ["const:c51ca8:8", "const:4:8"]]
- 00c51ca8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c52c9c ["INT_ADD", "register:40f0:8", ["const:c52c9c:8", "const:4:8"]]
+ 00c52c9c ["CALL", null, ["callee:00c5b140:8"]]
- 00c51ca8 bytes 32210094
+ 00c52c9c bytes 29210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0e01a1c3d9b0750c8d4a8a9a8631940"></a>

### [`00c52000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52000.md) → [`00c52ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ff4.md) __cxa_free_exception

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57ff0.md) · 呼出先 1件 [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md)
- 新版 呼出元 1件 [`00c58fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fc0.md) · 呼出先 1件 [`00c538a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c538a8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "00c53004",
      "value": [
        "leaf",
        "ram:c538a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c52010",
      "value": [
        "leaf",
        "ram:c528b4:8"
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
      "00c53004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ],
  "added": [
    [
      "00c53004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c52010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52000.md#insn-00c52010)
- 新版 [`00c53004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ff4.md#insn-00c53004)

~~~diff
- 00c52010 ["INT_ADD", "register:40f0:8", ["const:c52010:8", "const:4:8"]]
- 00c52010 ["CALL", null, ["ram:c528b4:8"]]
+ 00c53004 ["INT_ADD", "register:40f0:8", ["const:c53004:8", "const:4:8"]]
+ 00c53004 ["CALL", null, ["ram:c538a8:8"]]
- 00c52010 bytes 29020094
+ 00c53004 bytes 29020094
~~~


<a id="compare-62963412d80a1de15d89ab3fcec0eb6c"></a>

### [`00c52094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md) → [`00c53088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53088.md) FUN_00c53088

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c52024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52024.md) · 呼出先 4件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c53018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53018.md) · 呼出先 4件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) [`00c538a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c538a8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "00c530cc",
      "value": [
        "leaf",
        "ram:c538a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c520d8",
      "value": [
        "leaf",
        "ram:c528b4:8"
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
      "00c530cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ],
  "added": [
    [
      "00c530cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c520d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md#insn-00c520d8) · [`00c520b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md#insn-00c520b8) · [`00c520d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md#insn-00c520d0)
- 新版 [`00c530cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53088.md#insn-00c530cc) · [`00c530ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53088.md#insn-00c530ac) · [`00c530c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53088.md#insn-00c530c4)

~~~diff
- 00c520d8 ["INT_ADD", "register:40f0:8", ["const:c520d8:8", "const:4:8"]]
- 00c520d8 ["CALL", null, ["ram:c528b4:8"]]
+ 00c530cc ["INT_ADD", "register:40f0:8", ["const:c530cc:8", "const:4:8"]]
+ 00c530cc ["CALL", null, ["ram:c538a8:8"]]
- 00c520d8 bytes f7010094
+ 00c530cc bytes f7010094
- 00c520b8 ["INT_ADD", "register:40f0:8", ["const:c520b8:8", "const:4:8"]]
- 00c520b8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00c530ac ["INT_ADD", "register:40f0:8", ["const:c530ac:8", "const:4:8"]]
+ 00c530ac ["CALL", null, ["callee:00c54d90:8"]]
- 00c520b8 bytes 3a070094
+ 00c530ac bytes 39070094
- 00c520d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c520d0 ["INT_ADD", "register:40f0:8", ["const:c520d0:8", "const:4:8"]]
- 00c520d0 ["CALLIND", null, ["register:0:8"]]
+ 00c530c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c530c4 ["INT_ADD", "register:40f0:8", ["const:c530c4:8", "const:4:8"]]
+ 00c530c4 ["CALLIND", null, ["register:0:8"]]
- 00c520d0 bytes 00013fd6
+ 00c530c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfd507cb1b345e298898b5fa0eca6ea6"></a>

### [`00c521cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md) → [`00c531c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c531c0.md) __cxa_end_catch

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c583a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583a0.md) · 呼出先 4件 [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c541dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c541dc.md) [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)
- 新版 呼出元 1件 [`00c59370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59370.md) · 呼出先 4件 [`00c538a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c538a8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c551cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c551cc.md) [`00c5fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

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
      "site": "00c53230",
      "value": [
        "leaf",
        "ram:c538a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c5223c",
      "value": [
        "leaf",
        "ram:c528b4:8"
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
      "site": "00c53260",
      "value": [
        "leaf",
        "ram:c538a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c5226c",
      "value": [
        "leaf",
        "ram:c528b4:8"
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
      "00c53230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ],
    [
      "00c53260",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ],
  "added": [
    [
      "00c53230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ],
    [
      "00c53260",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5223c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md#insn-00c5223c) · [`00c5226c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md#insn-00c5226c) · [`00c521dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md#insn-00c521dc)
- 新版 [`00c53230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c531c0.md#insn-00c53230) · [`00c53260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c531c0.md#insn-00c53260) · [`00c531d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c531c0.md#insn-00c531d0)

~~~diff
- 00c5223c ["INT_ADD", "register:40f0:8", ["const:c5223c:8", "const:4:8"]]
- 00c5223c ["CALL", null, ["ram:c528b4:8"]]
+ 00c53230 ["INT_ADD", "register:40f0:8", ["const:c53230:8", "const:4:8"]]
+ 00c53230 ["CALL", null, ["ram:c538a8:8"]]
- 00c5223c bytes 9e010094
+ 00c53230 bytes 9e010094
- 00c5226c ["INT_ADD", "register:40f0:8", ["const:c5226c:8", "const:4:8"]]
- 00c5226c ["CALL", null, ["ram:c528b4:8"]]
+ 00c53260 ["INT_ADD", "register:40f0:8", ["const:c53260:8", "const:4:8"]]
+ 00c53260 ["CALL", null, ["ram:c538a8:8"]]
- 00c5226c bytes 92010094
+ 00c53260 bytes 92010094
- 00c521dc ["INT_ADD", "register:40f0:8", ["const:c521dc:8", "const:4:8"]]
- 00c521dc ["CALL", null, ["callee:00c5fe40:8"]]
+ 00c531d0 ["INT_ADD", "register:40f0:8", ["const:c531d0:8", "const:4:8"]]
+ 00c531d0 ["CALL", null, ["callee:00c5fe40:8"]]
- 00c521dc bytes 25330094
+ 00c531d0 bytes 1c330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d9d9a41a5aa1d1a082b18dff909062d"></a>

### [`00c522b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md) → [`00c532ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c532ac.md) __cxa_decrement_exception_refcount

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfe0.md) · 呼出先 2件 [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c5efb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efb0.md) · 呼出先 2件 [`00c538a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c538a8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

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
      "site": "00c532ec",
      "value": [
        "leaf",
        "ram:c538a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c522f8",
      "value": [
        "leaf",
        "ram:c528b4:8"
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
      "00c532ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ],
  "added": [
    [
      "00c532ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c522f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md#insn-00c522f8) · [`00c522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md#insn-00c522d8) · [`00c522f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md#insn-00c522f0)
- 新版 [`00c532ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c532ac.md#insn-00c532ec) · [`00c532cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c532ac.md#insn-00c532cc) · [`00c532e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c532ac.md#insn-00c532e4)

~~~diff
- 00c522f8 ["INT_ADD", "register:40f0:8", ["const:c522f8:8", "const:4:8"]]
- 00c522f8 ["CALL", null, ["ram:c528b4:8"]]
+ 00c532ec ["INT_ADD", "register:40f0:8", ["const:c532ec:8", "const:4:8"]]
+ 00c532ec ["CALL", null, ["ram:c538a8:8"]]
- 00c522f8 bytes 6f010094
+ 00c532ec bytes 6f010094
- 00c522d8 ["INT_ADD", "register:40f0:8", ["const:c522d8:8", "const:4:8"]]
- 00c522d8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00c532cc ["INT_ADD", "register:40f0:8", ["const:c532cc:8", "const:4:8"]]
+ 00c532cc ["CALL", null, ["callee:00c54d90:8"]]
- 00c522d8 bytes b2060094
+ 00c532cc bytes b1060094
- 00c522f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c522f0 ["INT_ADD", "register:40f0:8", ["const:c522f0:8", "const:4:8"]]
- 00c522f0 ["CALLIND", null, ["register:0:8"]]
+ 00c532e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c532e4 ["INT_ADD", "register:40f0:8", ["const:c532e4:8", "const:4:8"]]
+ 00c532e4 ["CALLIND", null, ["register:0:8"]]
- 00c522f0 bytes 00013fd6
+ 00c532e4 bytes 00013fd6
~~~


<a id="compare-f5626b1be674256e0ef66ab8a1824170"></a>

### [`00c52614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md) → [`00c53608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53608.md) FUN_00c53608

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c524f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c524f4.md) · 呼出先 4件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c534e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c534e8.md) · 呼出先 4件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) [`00c538a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c538a8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "00c53654",
      "value": [
        "leaf",
        "ram:c538a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c52660",
      "value": [
        "leaf",
        "ram:c528b4:8"
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
      "00c53654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ],
    [
      "00c53668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ],
  "added": [
    [
      "00c53654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ],
    [
      "00c53668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c538a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c52660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md#insn-00c52660) · [`00c52640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md#insn-00c52640) · [`00c52658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md#insn-00c52658)
- 新版 [`00c53654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53608.md#insn-00c53654) · [`00c53634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53608.md#insn-00c53634) · [`00c5364c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53608.md#insn-00c5364c)

~~~diff
- 00c52660 ["INT_ADD", "register:40f0:8", ["const:c52660:8", "const:4:8"]]
- 00c52660 ["CALL", null, ["ram:c528b4:8"]]
+ 00c53654 ["INT_ADD", "register:40f0:8", ["const:c53654:8", "const:4:8"]]
+ 00c53654 ["CALL", null, ["ram:c538a8:8"]]
- 00c52660 bytes 95000094
+ 00c53654 bytes 95000094
- 00c52640 ["INT_ADD", "register:40f0:8", ["const:c52640:8", "const:4:8"]]
- 00c52640 ["CALL", null, ["callee:00c54d90:8"]]
+ 00c53634 ["INT_ADD", "register:40f0:8", ["const:c53634:8", "const:4:8"]]
+ 00c53634 ["CALL", null, ["callee:00c54d90:8"]]
- 00c52640 bytes d8050094
+ 00c53634 bytes d7050094
- 00c52658 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c52658 ["INT_ADD", "register:40f0:8", ["const:c52658:8", "const:4:8"]]
- 00c52658 ["CALLIND", null, ["register:0:8"]]
+ 00c5364c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5364c ["INT_ADD", "register:40f0:8", ["const:c5364c:8", "const:4:8"]]
+ 00c5364c ["CALLIND", null, ["register:0:8"]]
- 00c52658 bytes 00013fd6
+ 00c5364c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbb79c83e634c160fff1863954bdc83"></a>

### [`00c5272c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md) → [`00c53720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53720.md) FUN_00c53720

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) · 呼出先 3件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 1件 [`00c536d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c536d4.md) · 呼出先 3件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.02% / 新版 82.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c53770",
      "incomplete_value": true,
      "site": "00c53770",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5277c",
      "incomplete_value": true,
      "site": "00c5277c",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c53768",
      "incomplete_value": false,
      "site": "00c53770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:b6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52774",
      "incomplete_value": false,
      "site": "00c5277c",
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
            "const:bac:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c53774",
      "incomplete_value": false,
      "site": "00c53774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:b6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52780",
      "incomplete_value": false,
      "site": "00c52780",
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
            "const:bac:8"
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
      "00c53738",
      "PARAM",
      [
        "storage",
        "01128b68",
        null,
        null
      ]
    ],
    [
      "00c53744",
      "READ",
      [
        "storage",
        "01128b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00c53770",
      "WRITE",
      [
        "storage",
        "01128b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c53738",
      "PARAM",
      [
        "storage",
        "01129b28",
        null,
        null
      ]
    ],
    [
      "00c53744",
      "READ",
      [
        "storage",
        "01129b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00c53770",
      "WRITE",
      [
        "storage",
        "01129b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c52748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md#insn-00c52748) · [`00c5277c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md#insn-00c5277c) · [`00c5282c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md#insn-00c5282c)
- 新版 [`00c5373c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53720.md#insn-00c5373c) · [`00c53770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53720.md#insn-00c53770) · [`00c53820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53720.md#insn-00c53820)

~~~diff
- 00c52748 ["INT_ADD", "register:40f0:8", ["const:c52748:8", "const:4:8"]]
- 00c52748 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c5373c ["INT_ADD", "register:40f0:8", ["const:c5373c:8", "const:4:8"]]
+ 00c5373c ["CALL", null, ["callee:00c5c740:8"]]
- 00c52748 bytes 0a240094
+ 00c5373c bytes 01240094
- 00c5277c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b90:8"]]
- 00c5277c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
+ 00c53770 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b50:8"]]
+ 00c53770 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
- 00c5277c bytes 0ec905f9
+ 00c53770 bytes 0ea905f9
- 00c5282c ["INT_ADD", "register:40f0:8", ["const:c5282c:8", "const:4:8"]]
- 00c5282c ["CALL", null, ["callee:00c3909c:8"]]
+ 00c53820 ["INT_ADD", "register:40f0:8", ["const:c53820:8", "const:4:8"]]
+ 00c53820 ["CALL", null, ["callee:00c3909c:8"]]
- 00c5282c bytes 1f96ff97
+ 00c53820 bytes 1f96ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109c514a51bf266571ab3d0c028186e5"></a>

### [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) → [`00c539d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md) __gxx_personality_v0

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c51ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ee4.md) [`00c5319c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md) [`00c53344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53344.md) [`00c54174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54174.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) [`00c52ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ed8.md) [`00c54190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54190.md) [`00c54338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54338.md) [`00c55164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55164.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c53d2c",
      "incomplete_value": true,
      "site": "00c53d2c",
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
            "INT_MULT",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52d38",
      "incomplete_value": true,
      "site": "00c52d38",
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
            "INT_MULT",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40d0:8"
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
      "00c53d1c",
      "DATA",
      [
        "storage",
        "00313de8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c53d1c",
      "DATA",
      [
        "storage",
        "00313e28",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c52a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md#insn-00c52a64) · [`00c52a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md#insn-00c52a74) · [`00c52a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md#insn-00c52a80)
- 新版 [`00c53a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md#insn-00c53a58) · [`00c53a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md#insn-00c53a68) · [`00c53a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c539d8.md#insn-00c53a74)

~~~diff
- 00c52a64 ["INT_ADD", "register:40f0:8", ["const:c52a64:8", "const:4:8"]]
- 00c52a64 ["CALL", null, ["callee:00c551e8:8"]]
+ 00c53a58 ["INT_ADD", "register:40f0:8", ["const:c53a58:8", "const:4:8"]]
+ 00c53a58 ["CALL", null, ["callee:00c551e8:8"]]
- 00c52a64 bytes e5050094
+ 00c53a58 bytes e4050094
- 00c52a74 ["INT_ADD", "register:40f0:8", ["const:c52a74:8", "const:4:8"]]
- 00c52a74 ["CALL", null, ["callee:00c551e8:8"]]
+ 00c53a68 ["INT_ADD", "register:40f0:8", ["const:c53a68:8", "const:4:8"]]
+ 00c53a68 ["CALL", null, ["callee:00c551e8:8"]]
- 00c52a74 bytes e1050094
+ 00c53a68 bytes e0050094
- 00c52a80 ["INT_ADD", "register:40f0:8", ["const:c52a80:8", "const:4:8"]]
- 00c52a80 ["CALL", null, ["callee:00c55220:8"]]
+ 00c53a74 ["INT_ADD", "register:40f0:8", ["const:c53a74:8", "const:4:8"]]
+ 00c53a74 ["CALL", null, ["callee:00c55220:8"]]
- 00c52a80 bytes ec050094
+ 00c53a74 bytes eb050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941460300bb049605641b8533edf7dbd"></a>

### [`00c52f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md) → [`00c53f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53f74.md) __cxa_call_unexpected

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00c37930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c51ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ee4.md) [`00c51ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ef0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00c38924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38924.md) [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c52ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ed8.md) [`00c52ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ee4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c540c8",
      "incomplete_value": true,
      "site": "00c540cc",
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
      "definition_site": "00c530d4",
      "incomplete_value": true,
      "site": "00c530d8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c540dc",
      "incomplete_value": true,
      "site": "00c540f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c530e8",
      "incomplete_value": true,
      "site": "00c530fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:f30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54128",
      "incomplete_value": true,
      "site": "00c54130",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53134",
      "incomplete_value": true,
      "site": "00c5313c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:f30:8"
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
      "00c540c4",
      "READ",
      [
        "storage",
        "00c9bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00c540cc",
      "DATA",
      [
        "storage",
        "00c96738",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c540dc",
      "READ",
      [
        "storage",
        "00c9bf30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c540c4",
      "READ",
      [
        "storage",
        "00c9cef8",
        null,
        "pointer"
      ]
    ],
    [
      "00c540cc",
      "DATA",
      [
        "storage",
        "00c97708",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c540dc",
      "READ",
      [
        "storage",
        "00c9cf00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c530fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md#insn-00c530fc) · [`00c5313c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md#insn-00c5313c) · [`00c52fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md#insn-00c52fa8)
- 新版 [`00c540f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53f74.md#insn-00c540f0) · [`00c54130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53f74.md#insn-00c54130) · [`00c53f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53f74.md#insn-00c53f9c)

~~~diff
- 00c530fc ["INT_ADD", "register:40f0:8", ["const:c530fc:8", "const:4:8"]]
- 00c530fc ["CALL", null, ["callee:00c54338:8"]]
+ 00c540f0 ["INT_ADD", "register:40f0:8", ["const:c540f0:8", "const:4:8"]]
+ 00c540f0 ["CALL", null, ["callee:00c54338:8"]]
- 00c530fc bytes 92000094
+ 00c540f0 bytes 92000094
- 00c5313c ["INT_ADD", "register:40f0:8", ["const:c5313c:8", "const:4:8"]]
- 00c5313c ["CALL", null, ["callee:00c58fb0:8"]]
+ 00c54130 ["INT_ADD", "register:40f0:8", ["const:c54130:8", "const:4:8"]]
+ 00c54130 ["CALL", null, ["callee:00c58fb0:8"]]
- 00c5313c bytes a9130094
+ 00c54130 bytes a0130094
- 00c52fa8 ["INT_ADD", "register:40f0:8", ["const:c52fa8:8", "const:4:8"]]
- 00c52fa8 ["CALL", null, ["callee:00c590b0:8"]]
+ 00c53f9c ["INT_ADD", "register:40f0:8", ["const:c53f9c:8", "const:4:8"]]
+ 00c53f9c ["CALL", null, ["callee:00c590b0:8"]]
- 00c52fa8 bytes 4e140094
+ 00c53f9c bytes 45140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15121a7f6382d0df6306126ae9fc88a3"></a>

### [`00c535a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md) → [`00c54594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54594.md) __emutls_get_address

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md) · 呼出先 11件 [`00c537c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c5b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b390.md) · 呼出先 11件 [`00c547bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c547bc.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c591e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591e0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c54650",
      "incomplete_value": false,
      "site": "00c54650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5365c",
      "incomplete_value": false,
      "site": "00c5365c",
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
            "const:db0:8"
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
      "definition_site": "00c54648",
      "incomplete_value": true,
      "site": "00c54650",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53654",
      "incomplete_value": true,
      "site": "00c5365c",
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
            "const:1:8"
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
      "definition_site": "00c54648",
      "incomplete_value": true,
      "site": "00c54654",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53654",
      "incomplete_value": true,
      "site": "00c53660",
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
            "const:1:8"
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
      "00c545bc",
      "READ",
      [
        "storage",
        "01128da4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c54624",
      "PARAM",
      [
        "storage",
        "00c537c8",
        null,
        null
      ]
    ],
    [
      "00c54628",
      "PARAM",
      [
        "storage",
        "01128da8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c545bc",
      "READ",
      [
        "storage",
        "01129d64",
        null,
        "undefined4"
      ]
    ],
    [
      "00c54624",
      "PARAM",
      [
        "storage",
        "00c547bc",
        null,
        null
      ]
    ],
    [
      "00c54628",
      "PARAM",
      [
        "storage",
        "01129d68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c535cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md#insn-00c535cc) · [`00c53638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md#insn-00c53638) · [`00c5365c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md#insn-00c5365c)
- 新版 [`00c545c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54594.md#insn-00c545c0) · [`00c5462c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54594.md#insn-00c5462c) · [`00c54650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54594.md#insn-00c54650)

~~~diff
- 00c535cc ["INT_ADD", "register:40f0:8", ["const:c535cc:8", "const:4:8"]]
- 00c535cc ["CALL", null, ["callee:00c5f290:8"]]
+ 00c545c0 ["INT_ADD", "register:40f0:8", ["const:c545c0:8", "const:4:8"]]
+ 00c545c0 ["CALL", null, ["callee:00c5f290:8"]]
- 00c535cc bytes 3d2b0094
+ 00c545c0 bytes 342b0094
- 00c53638 ["INT_ADD", "register:40f0:8", ["const:c53638:8", "const:4:8"]]
- 00c53638 ["CALL", null, ["callee:00c5c760:8"]]
+ 00c5462c ["INT_ADD", "register:40f0:8", ["const:c5462c:8", "const:4:8"]]
+ 00c5462c ["CALL", null, ["callee:00c5c760:8"]]
- 00c53638 bytes 56200094
+ 00c5462c bytes 4d200094
- 00c5365c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
- 00c5365c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00c54650 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00c54650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00c5365c bytes 16d906f9
+ 00c54650 bytes 16b906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a64c96ed7f65b7f551c4cf6568284b"></a>

### [`00c5378c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md) → [`00c54780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54780.md) FUN_00c54780

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043ae68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043ae68.md) · 呼出先 1件 [`00c5efe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5efe0.md)
- 新版 呼出元 1件 [`0043b188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b188.md) · 呼出先 1件 [`00c5ffb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c547a4",
      "incomplete_value": true,
      "site": "00c547a8",
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
      "definition_site": "00c537b0",
      "incomplete_value": true,
      "site": "00c537b4",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c54788",
      "READ",
      [
        "storage",
        "01128da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c547a4",
      "READ",
      [
        "storage",
        "01128da4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c547ac",
      "WRITE",
      [
        "storage",
        "01128da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c54788",
      "READ",
      [
        "storage",
        "01129d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c547a4",
      "READ",
      [
        "storage",
        "01129d64",
        null,
        "undefined4"
      ]
    ],
    [
      "00c547ac",
      "WRITE",
      [
        "storage",
        "01129d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c537b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md#insn-00c537b4) · [`00c53790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md#insn-00c53790) · [`00c53794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md#insn-00c53794)
- 新版 [`00c547a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54780.md#insn-00c547a8) · [`00c54784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54780.md#insn-00c54784) · [`00c54788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54780.md#insn-00c54788)

~~~diff
- 00c537b4 ["INT_ADD", "register:40f0:8", ["const:c537b4:8", "const:4:8"]]
- 00c537b4 ["CALL", null, ["callee:00c5ffb0:8"]]
+ 00c547a8 ["INT_ADD", "register:40f0:8", ["const:c547a8:8", "const:4:8"]]
+ 00c547a8 ["CALL", null, ["callee:00c5ffb0:8"]]
- 00c537b4 bytes 0b2e0094
+ 00c547a8 bytes 022e0094
- 00c53790 ["COPY", "register:4040:8", ["const:1128000:8"]]
+ 00c54784 ["COPY", "register:4040:8", ["const:1129000:8"]]
- 00c53790 bytes a82600b0
+ 00c54784 bytes a82600b0
- 00c53794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00c53794 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00c53794 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00c54788 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
+ 00c54788 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c54788 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00c53794 bytes 08817639
+ 00c54788 bytes 08817539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3f24b040075b97dbceae60e963e5ea9"></a>

### [`00c537c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md) → [`00c547bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c547bc.md) FUN_00c547bc

採用 · 移動量 `+0xff4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c535a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md) · 呼出先 3件 [`00c53804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53804.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c54594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54594.md) · 呼出先 3件 [`00c547f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c547f8.md) [`00c5b3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b3a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

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
      "definition_site": "00c547e4",
      "incomplete_value": false,
      "site": "00c547e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c537f0",
      "incomplete_value": false,
      "site": "00c537f0",
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
            "const:da0:8"
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
      "definition_site": "00c547c8",
      "incomplete_value": false,
      "site": "00c547d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:d64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c537d4",
      "incomplete_value": false,
      "site": "00c537e0",
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
            "const:da4:8"
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
      "definition_site": "00c547d0",
      "incomplete_value": false,
      "site": "00c547d4",
      "value": [
        "leaf",
        "const:c547f8:8"
      ]
    },
    "old": {
      "definition_site": "00c537dc",
      "incomplete_value": false,
      "site": "00c537e0",
      "value": [
        "leaf",
        "const:c53804:8"
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
      "00c547c8",
      "PARAM",
      [
        "storage",
        "01128da4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c547d0",
      "PARAM",
      [
        "storage",
        "00c53804",
        null,
        null
      ]
    ],
    [
      "00c547e4",
      "WRITE",
      [
        "storage",
        "01128da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c547c8",
      "PARAM",
      [
        "storage",
        "01129d64",
        null,
        "undefined4"
      ]
    ],
    [
      "00c547d0",
      "PARAM",
      [
        "storage",
        "00c547f8",
        null,
        null
      ]
    ],
    [
      "00c547e4",
      "WRITE",
      [
        "storage",
        "01129d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c537e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md#insn-00c537e0) · [`00c537f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md#insn-00c537f0) · [`00c537d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md#insn-00c537d0)
- 新版 [`00c547d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c547bc.md#insn-00c547d4) · [`00c547e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c547bc.md#insn-00c547e4) · [`00c547c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c547bc.md#insn-00c547c4)

~~~diff
- 00c537e0 ["INT_ADD", "register:40f0:8", ["const:c537e0:8", "const:4:8"]]
- 00c537e0 ["CALL", null, ["callee:00c5b3a0:8"]]
+ 00c547d4 ["INT_ADD", "register:40f0:8", ["const:c547d4:8", "const:4:8"]]
+ 00c547d4 ["CALL", null, ["callee:00c5b3a0:8"]]
- 00c537e0 bytes fc1a0094
+ 00c547d4 bytes f31a0094
- 00c537f0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00c537f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:da0:8"]]
- 00c537f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c547e4 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00c547e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:d60:8"]]
+ 00c547e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00c537f0 bytes 09813639
+ 00c547e4 bytes 09813539
- 00c537d0 ["COPY", "register:4000:8", ["const:1128000:8"]]
+ 00c547c4 ["COPY", "register:4000:8", ["const:1129000:8"]]
- 00c537d0 bytes a02600b0
+ 00c547c4 bytes a02600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d2538edb2177b8a819f4dee8cfac076"></a>

### [`00c538c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md) → [`00c548b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c548b4.md) _INIT_0

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md) [`00c5eff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eff0.md) [`00c5f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5e1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1d0.md) [`00c5ffc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffc0.md) [`00c5ffd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c548d4",
      "incomplete_value": false,
      "site": "00c548d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c538e4",
      "incomplete_value": false,
      "site": "00c538e4",
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
            "const:de0:8"
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
      "definition_site": "00c54920",
      "incomplete_value": false,
      "site": "00c54920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53930",
      "incomplete_value": false,
      "site": "00c53930",
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
            "const:de0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c5493c",
      "incomplete_value": false,
      "site": "00c5493c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5394c",
      "incomplete_value": false,
      "site": "00c5394c",
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
            "const:de0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c548d4",
      "WRITE",
      [
        "storage",
        "01128de0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c548e8",
      "PARAM",
      [
        "storage",
        "002a6375",
        null,
        "string"
      ]
    ],
    [
      "00c54900",
      "PARAM",
      [
        "storage",
        "002a9a14",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c548d4",
      "WRITE",
      [
        "storage",
        "01129da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c548e8",
      "PARAM",
      [
        "storage",
        "002a64cd",
        null,
        "string"
      ]
    ],
    [
      "00c54900",
      "PARAM",
      [
        "storage",
        "002a9ae1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c538e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md#insn-00c538e4) · [`00c53900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md#insn-00c53900) · [`00c5391c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md#insn-00c5391c)
- 新版 [`00c548d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c548b4.md#insn-00c548d4) · [`00c548f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c548b4.md#insn-00c548f0) · [`00c5490c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c548b4.md#insn-00c5490c)

~~~diff
- 00c538e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00c538e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00c538e4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:de0:8"]]
- 00c538e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00c548d4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00c548d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00c548d4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:da0:8"]]
+ 00c548d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00c538e4 bytes 3f813739
+ 00c548d4 bytes 3f813639
- 00c53900 ["INT_ADD", "register:40f0:8", ["const:c53900:8", "const:4:8"]]
- 00c53900 ["CALL", null, ["callee:00c5ffd0:8"]]
+ 00c548f0 ["INT_ADD", "register:40f0:8", ["const:c548f0:8", "const:4:8"]]
+ 00c548f0 ["CALL", null, ["callee:00c5ffd0:8"]]
- 00c53900 bytes c02d0094
+ 00c548f0 bytes b82d0094
- 00c5391c ["INT_ADD", "register:40f0:8", ["const:c5391c:8", "const:4:8"]]
- 00c5391c ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00c5490c ["INT_ADD", "register:40f0:8", ["const:c5490c:8", "const:4:8"]]
+ 00c5490c ["CALL", null, ["callee:00c5e1d0:8"]]
- 00c5391c bytes 39260094
+ 00c5490c bytes 31260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce2142418c830d64e6c5342cc642e81"></a>

### [`00c53c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md) → [`00c54bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54bf8.md) _INIT_1

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5395c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5395c.md) [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md) [`00c5eff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eff0.md) [`00c5f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5494c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c5494c.md) [`00c5e1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1d0.md) [`00c5ffc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffc0.md) [`00c5ffd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffd0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c54c04",
      "incomplete_value": true,
      "site": "00c54c04",
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
      "definition_site": "00c53c14",
      "incomplete_value": true,
      "site": "00c53c14",
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
      "definition_site": "00c54c1c",
      "incomplete_value": false,
      "site": "00c54c24",
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
            "const:4cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53c2c",
      "incomplete_value": false,
      "site": "00c53c34",
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
            "const:375:8"
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
      "definition_site": "00c54c34",
      "incomplete_value": false,
      "site": "00c54c40",
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
            "const:ae1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53c44",
      "incomplete_value": false,
      "site": "00c53c50",
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
            "const:a14:8"
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
      "00c54c00",
      "READ",
      [
        "storage",
        "01128de8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c54c1c",
      "PARAM",
      [
        "storage",
        "002a6375",
        null,
        "string"
      ]
    ],
    [
      "00c54c34",
      "PARAM",
      [
        "storage",
        "002a9a14",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54c00",
      "READ",
      [
        "storage",
        "01129da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c54c1c",
      "PARAM",
      [
        "storage",
        "002a64cd",
        null,
        "string"
      ]
    ],
    [
      "00c54c34",
      "PARAM",
      [
        "storage",
        "002a9ae1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md#insn-00c53c34) · [`00c53c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md#insn-00c53c50) · [`00c53c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md#insn-00c53c80)
- 新版 [`00c54c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54bf8.md#insn-00c54c24) · [`00c54c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54bf8.md#insn-00c54c40) · [`00c54c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54bf8.md#insn-00c54c70)

~~~diff
- 00c53c34 ["INT_ADD", "register:40f0:8", ["const:c53c34:8", "const:4:8"]]
- 00c53c34 ["CALL", null, ["callee:00c5ffd0:8"]]
+ 00c54c24 ["INT_ADD", "register:40f0:8", ["const:c54c24:8", "const:4:8"]]
+ 00c54c24 ["CALL", null, ["callee:00c5ffd0:8"]]
- 00c53c34 bytes f32c0094
+ 00c54c24 bytes eb2c0094
- 00c53c50 ["INT_ADD", "register:40f0:8", ["const:c53c50:8", "const:4:8"]]
- 00c53c50 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00c54c40 ["INT_ADD", "register:40f0:8", ["const:c54c40:8", "const:4:8"]]
+ 00c54c40 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00c53c50 bytes 6c250094
+ 00c54c40 bytes 64250094
- 00c53c80 ["INT_ADD", "register:40f0:8", ["const:c53c80:8", "const:4:8"]]
- 00c53c80 ["CALL", null, ["ram:c5395c:8"]]
+ 00c54c70 ["INT_ADD", "register:40f0:8", ["const:c54c70:8", "const:4:8"]]
+ 00c54c70 ["CALL", null, ["ram:c5494c:8"]]
- 00c53c80 bytes 37ffff97
+ 00c54c70 bytes 37ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d14da8ee294c9031500b0f36b12f43"></a>

### [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) → [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) FUN_00c54eb8

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) · 呼出先 9件 [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) [`00c542e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md) [`00c54464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54464.md) [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md) [`00c544b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544b8.md)
- 新版 呼出元 2件 [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) · 呼出先 9件 [`00c55230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md) [`00c552d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c552d8.md) [`00c55454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55454.md) [`00c55468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55468.md) [`00c554a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54f90",
      "incomplete_value": true,
      "site": "00c54f94",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53fa0",
      "incomplete_value": true,
      "site": "00c53fa4",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54f78",
      "incomplete_value": false,
      "site": "00c54f94",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53f88",
      "incomplete_value": false,
      "site": "00c53fa4",
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
            "const:ec4:8"
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
      "definition_site": "00c54f84",
      "incomplete_value": false,
      "site": "00c54f94",
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
            "const:5ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53f94",
      "incomplete_value": false,
      "site": "00c53fa4",
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
            "const:522:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c54f78",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c54f7c",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c54f84",
      "PARAM",
      [
        "storage",
        "002ad522",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54f78",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c54f7c",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c54f84",
      "PARAM",
      [
        "storage",
        "002ad5ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md#insn-00c53fa4) · [`00c53ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md#insn-00c53ef0) · [`00c53ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md#insn-00c53ef8)
- 新版 [`00c54f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md#insn-00c54f94) · [`00c54ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md#insn-00c54ee0) · [`00c54ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md#insn-00c54ee8)

~~~diff
- 00c53fa4 ["INT_ADD", "register:40f0:8", ["const:c53fa4:8", "const:4:8"]]
- 00c53fa4 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c54f94 ["INT_ADD", "register:40f0:8", ["const:c54f94:8", "const:4:8"]]
+ 00c54f94 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c53fa4 bytes 1b2c0094
+ 00c54f94 bytes 132c0094
- 00c53ef0 ["INT_ADD", "register:40f0:8", ["const:c53ef0:8", "const:4:8"]]
- 00c53ef0 ["CALL", null, ["callee:00c55230:8"]]
+ 00c54ee0 ["INT_ADD", "register:40f0:8", ["const:c54ee0:8", "const:4:8"]]
+ 00c54ee0 ["CALL", null, ["callee:00c55230:8"]]
- 00c53ef0 bytes d4000094
+ 00c54ee0 bytes d4000094
- 00c53ef8 ["INT_ADD", "register:40f0:8", ["const:c53ef8:8", "const:4:8"]]
- 00c53ef8 ["CALL", null, ["callee:00c55454:8"]]
+ 00c54ee8 ["INT_ADD", "register:40f0:8", ["const:c54ee8:8", "const:4:8"]]
+ 00c54ee8 ["CALL", null, ["callee:00c55454:8"]]
- 00c53ef8 bytes 5b010094
+ 00c54ee8 bytes 5b010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e570bec6c1a7c51f7a37e6a43eebb747"></a>

### [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) → [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) FUN_00c54fec

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 256件 [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md) [`0046803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/0046803c.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00478188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478188.md) · 呼出先 7件 [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) [`00c57ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57ce8.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 257件 [`00461810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461810.md) [`00461b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461b78.md) [`0046835c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/0046835c.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`004784a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00478/004784a8.md) · 呼出先 7件 [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) [`00c55070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md) [`00c58cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58cd8.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5505c",
      "incomplete_value": true,
      "site": "00c55060",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5406c",
      "incomplete_value": true,
      "site": "00c54070",
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
            "const:130:8"
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
      "definition_site": "00c55044",
      "incomplete_value": false,
      "site": "00c55060",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54054",
      "incomplete_value": false,
      "site": "00c54070",
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
            "const:ec4:8"
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
      "definition_site": "00c55050",
      "incomplete_value": false,
      "site": "00c55060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:747:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54060",
      "incomplete_value": false,
      "site": "00c54070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:669:8"
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
      "00c55044",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c55048",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c55050",
      "PARAM",
      [
        "storage",
        "002bd669",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c55044",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c55048",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c55050",
      "PARAM",
      [
        "storage",
        "002bd747",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md#insn-00c54070) · [`00c54018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md#insn-00c54018) · [`00c54030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md#insn-00c54030)
- 新版 [`00c55060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md#insn-00c55060) · [`00c55008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md#insn-00c55008) · [`00c55020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md#insn-00c55020)

~~~diff
- 00c54070 ["INT_ADD", "register:40f0:8", ["const:c54070:8", "const:4:8"]]
- 00c54070 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c55060 ["INT_ADD", "register:40f0:8", ["const:c55060:8", "const:4:8"]]
+ 00c55060 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c54070 bytes e82b0094
+ 00c55060 bytes e02b0094
- 00c54018 ["INT_ADD", "register:40f0:8", ["const:c54018:8", "const:4:8"]]
- 00c54018 ["CALL", null, ["callee:00c58cd8:8"]]
+ 00c55008 ["INT_ADD", "register:40f0:8", ["const:c55008:8", "const:4:8"]]
+ 00c55008 ["CALL", null, ["callee:00c58cd8:8"]]
- 00c54018 bytes 340f0094
+ 00c55008 bytes 340f0094
- 00c54030 ["INT_ADD", "register:40f0:8", ["const:c54030:8", "const:4:8"]]
- 00c54030 ["CALL", null, ["callee:00c54eb8:8"]]
+ 00c55020 ["INT_ADD", "register:40f0:8", ["const:c55020:8", "const:4:8"]]
+ 00c55020 ["CALL", null, ["callee:00c54eb8:8"]]
- 00c54030 bytes a6ffff97
+ 00c55020 bytes a6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc4c18087e679fee5bbc32f5772b195"></a>

### [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) → [`00c55230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md) FUN_00c55230

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) · 呼出先 2件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 3件 [`00c54dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54dc0.md) [`00c54eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54eb8.md) [`00c55070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55070.md) · 呼出先 2件 [`00c55cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c5525c",
      "incomplete_value": false,
      "site": "00c5525c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9b000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5426c",
      "incomplete_value": false,
      "site": "00c5426c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "definition_site": "00c5525c",
      "incomplete_value": false,
      "site": "00c5525c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5426c",
      "incomplete_value": false,
      "site": "00c5426c",
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
            "const:df0:8"
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
      "00c5525c",
      "DATA",
      [
        "storage",
        "00c9a090",
        null,
        "undefined *"
      ]
    ],
    [
      "00c5525c",
      "DATA",
      [
        "storage",
        "01128df0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c5525c",
      "DATA",
      [
        "storage",
        "00c9b060",
        null,
        "undefined *"
      ]
    ],
    [
      "00c5525c",
      "DATA",
      [
        "storage",
        "01129db0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md#insn-00c54250) · [`00c54254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md#insn-00c54254) · [`00c54258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md#insn-00c54258)
- 新版 [`00c55240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md#insn-00c55240) · [`00c55244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md#insn-00c55244)

~~~diff
- 00c54250 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c55240 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00c54250 bytes 280200d0
+ 00c55240 bytes 280200d0
- 00c54254 ["COPY", "tmp:0:8", ["const:90:8"]]
- 00c54254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c54254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c54254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c55244 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 00c55244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c55244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c55244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c54254 bytes 08410291
+ 00c55244 bytes 08810191
- 00c54258 ["COPY", "register:4048:8", ["const:1128000:8"]]
- 00c54258 bytes a9260090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67553225144606a9135dc9100dd8e6cc"></a>

### [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) → [`00c55660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md) FUN_00c55660

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) · 呼出先 6件 [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md)
- 新版 呼出元 2件 [`00c554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554d0.md) [`00c587ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md) · 呼出先 6件 [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) [`00c5773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.07% / 新版 96.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55914",
      "incomplete_value": true,
      "site": "00c55918",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54924",
      "incomplete_value": true,
      "site": "00c54928",
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
            "const:130:8"
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
      "definition_site": "00c558fc",
      "incomplete_value": false,
      "site": "00c55918",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5490c",
      "incomplete_value": false,
      "site": "00c54928",
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
            "const:ec4:8"
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
      "definition_site": "00c55908",
      "incomplete_value": false,
      "site": "00c55918",
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
            "const:8da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54918",
      "incomplete_value": false,
      "site": "00c54928",
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
            "const:890:8"
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
      "00c556c4",
      "DATA",
      [
        "storage",
        "002bd6bc",
        null,
        "string"
      ]
    ],
    [
      "00c557a0",
      "DATA",
      [
        "storage",
        "002a3ea2",
        null,
        "string"
      ]
    ],
    [
      "00c558fc",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c556c4",
      "DATA",
      [
        "storage",
        "002bd79a",
        null,
        "string"
      ]
    ],
    [
      "00c557a0",
      "DATA",
      [
        "storage",
        "002a3f6d",
        null,
        "string"
      ]
    ],
    [
      "00c558fc",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md#insn-00c54928) · [`00c546d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md#insn-00c546d4) · [`00c54720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md#insn-00c54720)
- 新版 [`00c55918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md#insn-00c55918) · [`00c556c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md#insn-00c556c4) · [`00c55710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md#insn-00c55710)

~~~diff
- 00c54928 ["INT_ADD", "register:40f0:8", ["const:c54928:8", "const:4:8"]]
- 00c54928 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c55918 ["INT_ADD", "register:40f0:8", ["const:c55918:8", "const:4:8"]]
+ 00c55918 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c54928 bytes ba290094
+ 00c55918 bytes b2290094
- 00c546d4 ["COPY", "tmp:0:8", ["const:6bc:8"]]
- 00c546d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c546d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c546d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c556c4 ["COPY", "tmp:0:8", ["const:79a:8"]]
+ 00c556c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c556c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c556c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c546d4 bytes 00f01a91
+ 00c556c4 bytes 00681e91
- 00c54720 ["INT_ADD", "register:40f0:8", ["const:c54720:8", "const:4:8"]]
- 00c54720 ["CALL", null, ["callee:00c5773c:8"]]
+ 00c55710 ["INT_ADD", "register:40f0:8", ["const:c55710:8", "const:4:8"]]
+ 00c55710 ["CALL", null, ["callee:00c5773c:8"]]
- 00c54720 bytes 0b080094
+ 00c55710 bytes 0b080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40df12c968d0fda4cb0a281b7bef5962"></a>

### [`00c5498c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md) → [`00c5597c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c5597c.md) FUN_00c5597c

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55a50",
      "incomplete_value": true,
      "site": "00c55a54",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54a60",
      "incomplete_value": true,
      "site": "00c54a64",
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
            "const:130:8"
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
      "definition_site": "00c55a38",
      "incomplete_value": false,
      "site": "00c55a54",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54a48",
      "incomplete_value": false,
      "site": "00c54a64",
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
            "const:ec4:8"
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
      "definition_site": "00c55a44",
      "incomplete_value": false,
      "site": "00c55a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:805:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54a54",
      "incomplete_value": false,
      "site": "00c54a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:72e:8"
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
      "00c55a38",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c55a3c",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c55a44",
      "PARAM",
      [
        "storage",
        "002af72e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c55a38",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c55a3c",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c55a44",
      "PARAM",
      [
        "storage",
        "002af805",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md#insn-00c54a64) · [`00c54a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md#insn-00c54a40) · [`00c54a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md#insn-00c54a48)
- 新版 [`00c55a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c5597c.md#insn-00c55a54) · [`00c55a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c5597c.md#insn-00c55a30) · [`00c55a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c5597c.md#insn-00c55a38)

~~~diff
- 00c54a64 ["INT_ADD", "register:40f0:8", ["const:c54a64:8", "const:4:8"]]
- 00c54a64 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c55a54 ["INT_ADD", "register:40f0:8", ["const:c55a54:8", "const:4:8"]]
+ 00c55a54 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c54a64 bytes 6b290094
+ 00c55a54 bytes 63290094
- 00c54a40 ["COPY", "register:4098:8", ["const:c9b000:8"]]
+ 00c55a30 ["COPY", "register:4098:8", ["const:c9c000:8"]]
- 00c54a40 bytes 330200f0
+ 00c55a30 bytes 330200f0
- 00c54a48 ["COPY", "tmp:0:8", ["const:ec4:8"]]
- 00c54a48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c54a48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c54a48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c55a38 ["COPY", "tmp:0:8", ["const:f04:8"]]
+ 00c55a38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c55a38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c55a38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c54a48 bytes 21103b91
+ 00c55a38 bytes 21103c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d04fa959c340ea792542dec11cd2a4b"></a>

### [`00c54a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md) → [`00c55a64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55a64.md) FUN_00c55a64

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55b38",
      "incomplete_value": true,
      "site": "00c55b3c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54b48",
      "incomplete_value": true,
      "site": "00c54b4c",
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
            "const:130:8"
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
      "definition_site": "00c55b20",
      "incomplete_value": false,
      "site": "00c55b3c",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54b30",
      "incomplete_value": false,
      "site": "00c54b4c",
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
            "const:ec4:8"
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
      "definition_site": "00c55b2c",
      "incomplete_value": false,
      "site": "00c55b3c",
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
            "const:ee6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54b3c",
      "incomplete_value": false,
      "site": "00c54b4c",
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
            "const:e17:8"
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
      "00c55b20",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c55b24",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c55b2c",
      "PARAM",
      [
        "storage",
        "002b5e17",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c55b20",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c55b24",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c55b2c",
      "PARAM",
      [
        "storage",
        "002b5ee6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md#insn-00c54b4c) · [`00c54b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md#insn-00c54b28) · [`00c54b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md#insn-00c54b30)
- 新版 [`00c55b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55a64.md#insn-00c55b3c) · [`00c55b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55a64.md#insn-00c55b18) · [`00c55b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55a64.md#insn-00c55b20)

~~~diff
- 00c54b4c ["INT_ADD", "register:40f0:8", ["const:c54b4c:8", "const:4:8"]]
- 00c54b4c ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c55b3c ["INT_ADD", "register:40f0:8", ["const:c55b3c:8", "const:4:8"]]
+ 00c55b3c ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c54b4c bytes 31290094
+ 00c55b3c bytes 29290094
- 00c54b28 ["COPY", "register:4098:8", ["const:c9b000:8"]]
+ 00c55b18 ["COPY", "register:4098:8", ["const:c9c000:8"]]
- 00c54b28 bytes 330200f0
+ 00c55b18 bytes 330200f0
- 00c54b30 ["COPY", "tmp:0:8", ["const:ec4:8"]]
- 00c54b30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c54b30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c54b30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c55b20 ["COPY", "tmp:0:8", ["const:f04:8"]]
+ 00c55b20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c55b20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c55b20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c54b30 bytes 21103b91
+ 00c55b20 bytes 21103c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ce699a0be452601df48d4d819943b6"></a>

### [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) → [`00c55cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md) FUN_00c55cf8

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) · 呼出先 10件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) [`00c575ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c575ac.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c55230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55230.md) · 呼出先 10件 [`00c554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554d0.md) [`00c564f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md) [`00c582c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md) [`00c5859c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c5859c.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55d48",
      "incomplete_value": false,
      "site": "00c55d58",
      "value": [
        "leaf",
        "const:c5859c:8"
      ]
    },
    "old": {
      "definition_site": "00c54d58",
      "incomplete_value": false,
      "site": "00c54d68",
      "value": [
        "leaf",
        "const:c575ac:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55d84",
      "incomplete_value": false,
      "site": "00c55d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:db4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54d94",
      "incomplete_value": false,
      "site": "00c54d98",
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
            "const:df4:8"
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
      "definition_site": "00c55dcc",
      "incomplete_value": false,
      "site": "00c55dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:db4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54ddc",
      "incomplete_value": false,
      "site": "00c54de0",
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
            "const:df4:8"
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
      "00c55d48",
      "PARAM",
      [
        "storage",
        "00c575ac",
        null,
        null
      ]
    ],
    [
      "00c55d84",
      "PARAM",
      [
        "storage",
        "01128df4",
        null,
        null
      ]
    ],
    [
      "00c55d94",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c55d48",
      "PARAM",
      [
        "storage",
        "00c5859c",
        null,
        null
      ]
    ],
    [
      "00c55d84",
      "PARAM",
      [
        "storage",
        "01129db4",
        null,
        null
      ]
    ],
    [
      "00c55d94",
      "READ",
      [
        "storage",
        "00ca5948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md#insn-00c54d68) · [`00c54d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md#insn-00c54d98) · [`00c54de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md#insn-00c54de0)
- 新版 [`00c55d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md#insn-00c55d58) · [`00c55d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md#insn-00c55d88) · [`00c55dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md#insn-00c55dd0)

~~~diff
- 00c54d68 ["INT_ADD", "register:40f0:8", ["const:c54d68:8", "const:4:8"]]
- 00c54d68 ["CALL", null, ["callee:00c60010:8"]]
+ 00c55d58 ["INT_ADD", "register:40f0:8", ["const:c55d58:8", "const:4:8"]]
+ 00c55d58 ["CALL", null, ["callee:00c60010:8"]]
- 00c54d68 bytes b6280094
+ 00c55d58 bytes ae280094
- 00c54d98 ["INT_ADD", "register:40f0:8", ["const:c54d98:8", "const:4:8"]]
- 00c54d98 ["CALL", null, ["callee:00c60020:8"]]
+ 00c55d88 ["INT_ADD", "register:40f0:8", ["const:c55d88:8", "const:4:8"]]
+ 00c55d88 ["CALL", null, ["callee:00c60020:8"]]
- 00c54d98 bytes ae280094
+ 00c55d88 bytes a6280094
- 00c54de0 ["INT_ADD", "register:40f0:8", ["const:c54de0:8", "const:4:8"]]
- 00c54de0 ["CALL", null, ["callee:00c60000:8"]]
+ 00c55dd0 ["INT_ADD", "register:40f0:8", ["const:c55dd0:8", "const:4:8"]]
+ 00c55dd0 ["CALL", null, ["callee:00c60000:8"]]
- 00c54de0 bytes 94280094
+ 00c55dd0 bytes 8c280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2970cb78743b561cc88376529fad53d5"></a>

### [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) → [`00c56060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md) FUN_00c56060

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54b90.md) · 呼出先 11件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c5607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md) [`00c561b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md) [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md)
- 新版 呼出元 1件 [`00c55b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55b80.md) · 呼出先 11件 [`00c554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554d0.md) [`00c564f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md) [`00c5706c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5706c.md) [`00c571a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c571a0.md) [`00c57904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c56478",
      "incomplete_value": true,
      "site": "00c5647c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55488",
      "incomplete_value": true,
      "site": "00c5548c",
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
            "const:130:8"
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
      "definition_site": "00c56460",
      "incomplete_value": false,
      "site": "00c5647c",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55470",
      "incomplete_value": false,
      "site": "00c5548c",
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
            "const:ec4:8"
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
      "definition_site": "00c5646c",
      "incomplete_value": false,
      "site": "00c5647c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5547c",
      "incomplete_value": false,
      "site": "00c5548c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d5b:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c56460",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c56464",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c5646c",
      "PARAM",
      [
        "storage",
        "002a1d5b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c56460",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c56464",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c5646c",
      "PARAM",
      [
        "storage",
        "002a1d9b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md#insn-00c5548c) · [`00c554c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md#insn-00c554c0) · [`00c554f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md#insn-00c554f4)
- 新版 [`00c5647c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md#insn-00c5647c) · [`00c564b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md#insn-00c564b0) · [`00c564e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md#insn-00c564e4)

~~~diff
- 00c5548c ["INT_ADD", "register:40f0:8", ["const:c5548c:8", "const:4:8"]]
- 00c5548c ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c5647c ["INT_ADD", "register:40f0:8", ["const:c5647c:8", "const:4:8"]]
+ 00c5647c ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c5548c bytes e1260094
+ 00c5647c bytes d9260094
- 00c554c0 ["INT_ADD", "register:40f0:8", ["const:c554c0:8", "const:4:8"]]
- 00c554c0 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c564b0 ["INT_ADD", "register:40f0:8", ["const:c564b0:8", "const:4:8"]]
+ 00c564b0 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c554c0 bytes d4260094
+ 00c564b0 bytes cc260094
- 00c554f4 ["INT_ADD", "register:40f0:8", ["const:c554f4:8", "const:4:8"]]
- 00c554f4 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c564e4 ["INT_ADD", "register:40f0:8", ["const:c564e4:8", "const:4:8"]]
+ 00c564e4 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c554f4 bytes c7260094
+ 00c564e4 bytes bf260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ae06434f77f470411e16c4bc297bab"></a>

### [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) → [`00c564f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md) FUN_00c564f4

採用 · 移動量 `+0xff0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) · 呼出先 8件 [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 3件 [`00c55cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md) [`00c56060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md) [`00c582c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md) · 呼出先 8件 [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) [`00c5773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.10% / 新版 92.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c56ed4",
      "incomplete_value": true,
      "site": "00c56ed8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55ee4",
      "incomplete_value": true,
      "site": "00c55ee8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c56ec8",
      "incomplete_value": false,
      "site": "00c56ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55ed8",
      "incomplete_value": false,
      "site": "00c55ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:e3c:8"
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
      "definition_site": "00c56f6c",
      "incomplete_value": true,
      "site": "00c56f70",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55f7c",
      "incomplete_value": true,
      "site": "00c55f80",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c565cc",
      "DATA",
      [
        "storage",
        "00313e50",
        "switchD_00c555e4::switchdataD_00313e50",
        "ushort"
      ]
    ],
    [
      "00c56df0",
      "PARAM",
      [
        "storage",
        "002bc305",
        null,
        "string"
      ]
    ],
    [
      "00c56e00",
      "PARAM",
      [
        "storage",
        "002b7f07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c565cc",
      "DATA",
      [
        "storage",
        "00313e90",
        "switchD_00c565d4::switchdataD_00313e90",
        "ushort"
      ]
    ],
    [
      "00c56df0",
      "PARAM",
      [
        "storage",
        "002bc3e3",
        null,
        "string"
      ]
    ],
    [
      "00c56e00",
      "PARAM",
      [
        "storage",
        "002b7fd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c55ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md#insn-00c55ee8) · [`00c55f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md#insn-00c55f80) · [`00c55fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md#insn-00c55fd0)
- 新版 [`00c56ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md#insn-00c56ed8) · [`00c56f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md#insn-00c56f70) · [`00c56fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md#insn-00c56fc0)

~~~diff
- 00c55ee8 ["INT_ADD", "register:40f0:8", ["const:c55ee8:8", "const:4:8"]]
- 00c55ee8 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c56ed8 ["INT_ADD", "register:40f0:8", ["const:c56ed8:8", "const:4:8"]]
+ 00c56ed8 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c55ee8 bytes 4a240094
+ 00c56ed8 bytes 42240094
- 00c55f80 ["INT_ADD", "register:40f0:8", ["const:c55f80:8", "const:4:8"]]
- 00c55f80 ["CALL", null, ["callee:00c5b250:8"]]
+ 00c56f70 ["INT_ADD", "register:40f0:8", ["const:c56f70:8", "const:4:8"]]
+ 00c56f70 ["CALL", null, ["callee:00c5b250:8"]]
- 00c55f80 bytes c0100094
+ 00c56f70 bytes b8100094
- 00c55fd0 ["INT_ADD", "register:40f0:8", ["const:c55fd0:8", "const:4:8"]]
- 00c55fd0 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c56fc0 ["INT_ADD", "register:40f0:8", ["const:c56fc0:8", "const:4:8"]]
+ 00c56fc0 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c55fd0 bytes 10240094
+ 00c56fc0 bytes 08240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b7df964b5c981d38c5af10e33c80b6f"></a>

### [`00c5607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md) → [`00c5706c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5706c.md) FUN_00c5706c

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) · 呼出先 5件 [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c56060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md) · 呼出先 5件 [`00c57904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5718c",
      "incomplete_value": true,
      "site": "00c57190",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5619c",
      "incomplete_value": true,
      "site": "00c561a0",
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
            "const:130:8"
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
      "definition_site": "00c57174",
      "incomplete_value": false,
      "site": "00c57190",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56184",
      "incomplete_value": false,
      "site": "00c561a0",
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
            "const:ec4:8"
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
      "definition_site": "00c57180",
      "incomplete_value": false,
      "site": "00c57190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:805:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56190",
      "incomplete_value": false,
      "site": "00c561a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:72e:8"
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
      "00c57174",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c57178",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c57180",
      "PARAM",
      [
        "storage",
        "002af72e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c57174",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c57178",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c57180",
      "PARAM",
      [
        "storage",
        "002af805",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c561a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md#insn-00c561a0) · [`00c5617c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md#insn-00c5617c) · [`00c56184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md#insn-00c56184)
- 新版 [`00c57190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5706c.md#insn-00c57190) · [`00c5716c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5706c.md#insn-00c5716c) · [`00c57174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5706c.md#insn-00c57174)

~~~diff
- 00c561a0 ["INT_ADD", "register:40f0:8", ["const:c561a0:8", "const:4:8"]]
- 00c561a0 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c57190 ["INT_ADD", "register:40f0:8", ["const:c57190:8", "const:4:8"]]
+ 00c57190 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c561a0 bytes 9c230094
+ 00c57190 bytes 94230094
- 00c5617c ["COPY", "register:4098:8", ["const:c9b000:8"]]
+ 00c5716c ["COPY", "register:4098:8", ["const:c9c000:8"]]
- 00c5617c bytes 330200b0
+ 00c5716c bytes 330200b0
- 00c56184 ["COPY", "tmp:0:8", ["const:ec4:8"]]
- 00c56184 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c56184 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c56184 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c57174 ["COPY", "tmp:0:8", ["const:f04:8"]]
+ 00c57174 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57174 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57174 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c56184 bytes 21103b91
+ 00c57174 bytes 21103c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-902328d09204e34b6ae2f79323f00318"></a>

### [`00c561b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md) → [`00c571a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c571a0.md) FUN_00c571a0

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) · 呼出先 5件 [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c56060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md) · 呼出先 5件 [`00c57904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57368",
      "incomplete_value": true,
      "site": "00c5736c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56378",
      "incomplete_value": true,
      "site": "00c5637c",
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
            "const:130:8"
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
      "definition_site": "00c57350",
      "incomplete_value": false,
      "site": "00c5736c",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56360",
      "incomplete_value": false,
      "site": "00c5637c",
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
            "const:ec4:8"
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
      "definition_site": "00c5735c",
      "incomplete_value": false,
      "site": "00c5736c",
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
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5636c",
      "incomplete_value": false,
      "site": "00c5637c",
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
            "const:5eb:8"
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
      "00c57350",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c57354",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c5735c",
      "PARAM",
      [
        "storage",
        "002ae5eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c57350",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c57354",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c5735c",
      "PARAM",
      [
        "storage",
        "002ae6b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md#insn-00c5637c) · [`00c563b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md#insn-00c563b0) · [`00c56240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md#insn-00c56240)
- 新版 [`00c5736c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c571a0.md#insn-00c5736c) · [`00c573a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c571a0.md#insn-00c573a0) · [`00c57230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c571a0.md#insn-00c57230)

~~~diff
- 00c5637c ["INT_ADD", "register:40f0:8", ["const:c5637c:8", "const:4:8"]]
- 00c5637c ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c5736c ["INT_ADD", "register:40f0:8", ["const:c5736c:8", "const:4:8"]]
+ 00c5736c ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c5637c bytes 25230094
+ 00c5736c bytes 1d230094
- 00c563b0 ["INT_ADD", "register:40f0:8", ["const:c563b0:8", "const:4:8"]]
- 00c563b0 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c573a0 ["INT_ADD", "register:40f0:8", ["const:c573a0:8", "const:4:8"]]
+ 00c573a0 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c563b0 bytes 18230094
+ 00c573a0 bytes 10230094
- 00c56240 ["INT_ADD", "register:40f0:8", ["const:c56240:8", "const:4:8"]]
- 00c56240 ["CALL", null, ["callee:00c57904:8"]]
+ 00c57230 ["INT_ADD", "register:40f0:8", ["const:c57230:8", "const:4:8"]]
+ 00c57230 ["CALL", null, ["callee:00c57904:8"]]
- 00c56240 bytes b5010094
+ 00c57230 bytes b5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d27e6c07904ea975225e0f305efb9679"></a>

### [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) → [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) FUN_00c573b0

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c576dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md) [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) · 呼出先 5件 [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 6件 [`00c554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554d0.md) [`00c55660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md) [`00c564f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md) [`00c586cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md) [`00c587ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md) · 呼出先 5件 [`00c5773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.58% / 新版 84.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c575d8",
      "incomplete_value": true,
      "site": "00c575dc",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c565e8",
      "incomplete_value": true,
      "site": "00c565ec",
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
            "const:130:8"
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
      "definition_site": "00c575c0",
      "incomplete_value": false,
      "site": "00c575dc",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c565d0",
      "incomplete_value": false,
      "site": "00c565ec",
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
            "const:ec4:8"
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
      "definition_site": "00c575cc",
      "incomplete_value": false,
      "site": "00c575dc",
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
            "const:8da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c565dc",
      "incomplete_value": false,
      "site": "00c565ec",
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
            "const:890:8"
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
      "00c575c0",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c575c4",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c575cc",
      "PARAM",
      [
        "storage",
        "002b3890",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c575c0",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c575c4",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c575cc",
      "PARAM",
      [
        "storage",
        "002b38da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c565ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md#insn-00c565ec) · [`00c56630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md#insn-00c56630) · [`00c5666c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md#insn-00c5666c)
- 新版 [`00c575dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md#insn-00c575dc) · [`00c57620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md#insn-00c57620) · [`00c5765c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md#insn-00c5765c)

~~~diff
- 00c565ec ["INT_ADD", "register:40f0:8", ["const:c565ec:8", "const:4:8"]]
- 00c565ec ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c575dc ["INT_ADD", "register:40f0:8", ["const:c575dc:8", "const:4:8"]]
+ 00c575dc ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c565ec bytes 89220094
+ 00c575dc bytes 81220094
- 00c56630 ["INT_ADD", "register:40f0:8", ["const:c56630:8", "const:4:8"]]
- 00c56630 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c57620 ["INT_ADD", "register:40f0:8", ["const:c57620:8", "const:4:8"]]
+ 00c57620 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c56630 bytes 78220094
+ 00c57620 bytes 70220094
- 00c5666c ["INT_ADD", "register:40f0:8", ["const:c5666c:8", "const:4:8"]]
- 00c5666c ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c5765c ["INT_ADD", "register:40f0:8", ["const:c5765c:8", "const:4:8"]]
+ 00c5765c ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c5666c bytes 69220094
+ 00c5765c bytes 61220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-265f638774782cba9f31136af58443c7"></a>

### [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) → [`00c5773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md) FUN_00c5773c

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 6件 [`00c554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c554d0.md) [`00c55660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55660.md) [`00c564f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md) [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) [`00c57904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md) · 呼出先 4件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c578bc",
      "incomplete_value": true,
      "site": "00c578c0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c568cc",
      "incomplete_value": true,
      "site": "00c568d0",
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
            "const:130:8"
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
      "definition_site": "00c578a4",
      "incomplete_value": false,
      "site": "00c578c0",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c568b4",
      "incomplete_value": false,
      "site": "00c568d0",
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
            "const:ec4:8"
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
      "definition_site": "00c578b0",
      "incomplete_value": false,
      "site": "00c578c0",
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
            "const:4d5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c568c0",
      "incomplete_value": false,
      "site": "00c568d0",
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
            "const:37d:8"
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
      "00c578a4",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c578a8",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c578b0",
      "PARAM",
      [
        "storage",
        "002a637d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c578a4",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c578a8",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c578b0",
      "PARAM",
      [
        "storage",
        "002a64d5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c568d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md#insn-00c568d0) · [`00c56904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md#insn-00c56904) · [`00c568ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md#insn-00c568ac)
- 新版 [`00c578c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md#insn-00c578c0) · [`00c578f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md#insn-00c578f4) · [`00c5789c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md#insn-00c5789c)

~~~diff
- 00c568d0 ["INT_ADD", "register:40f0:8", ["const:c568d0:8", "const:4:8"]]
- 00c568d0 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c578c0 ["INT_ADD", "register:40f0:8", ["const:c578c0:8", "const:4:8"]]
+ 00c578c0 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c568d0 bytes d0210094
+ 00c578c0 bytes c8210094
- 00c56904 ["INT_ADD", "register:40f0:8", ["const:c56904:8", "const:4:8"]]
- 00c56904 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c578f4 ["INT_ADD", "register:40f0:8", ["const:c578f4:8", "const:4:8"]]
+ 00c578f4 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c56904 bytes c3210094
+ 00c578f4 bytes bb210094
- 00c568ac ["COPY", "register:4098:8", ["const:c9b000:8"]]
+ 00c5789c ["COPY", "register:4098:8", ["const:c9c000:8"]]
- 00c568ac bytes 330200b0
+ 00c5789c bytes 330200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cd0b8e95b54239f052f740c8cc03f38"></a>

### [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) → [`00c57904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md) FUN_00c57904

採用 · 移動量 `+0xff0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) [`00c5607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md) [`00c561b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md) · 呼出先 5件 [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 3件 [`00c56060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c56060.md) [`00c5706c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5706c.md) [`00c571a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c571a0.md) · 呼出先 5件 [`00c5773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c5773c.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 40件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c580d4",
      "incomplete_value": true,
      "site": "00c580d8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c570e4",
      "incomplete_value": true,
      "site": "00c570e8",
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
            "const:130:8"
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
      "definition_site": "00c580bc",
      "incomplete_value": false,
      "site": "00c580d8",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c570cc",
      "incomplete_value": false,
      "site": "00c570e8",
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
            "const:ec4:8"
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
      "definition_site": "00c580c8",
      "incomplete_value": false,
      "site": "00c580d8",
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
            "const:8da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c570d8",
      "incomplete_value": false,
      "site": "00c570e8",
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
            "const:890:8"
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
      "00c579b0",
      "DATA",
      [
        "storage",
        "00313eb0",
        "switchD_00c569c8::switchdataD_00313eb0",
        "ushort"
      ]
    ],
    [
      "00c580bc",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c580c0",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c579b0",
      "DATA",
      [
        "storage",
        "00313ef0",
        "switchD_00c579b8::switchdataD_00313ef0",
        "ushort"
      ]
    ],
    [
      "00c580bc",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c580c0",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c570e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md#insn-00c570e8) · [`00c5711c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md#insn-00c5711c) · [`00c57150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md#insn-00c57150)
- 新版 [`00c580d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md#insn-00c580d8) · [`00c5810c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md#insn-00c5810c) · [`00c58140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c57904.md#insn-00c58140)

~~~diff
- 00c570e8 ["INT_ADD", "register:40f0:8", ["const:c570e8:8", "const:4:8"]]
- 00c570e8 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c580d8 ["INT_ADD", "register:40f0:8", ["const:c580d8:8", "const:4:8"]]
+ 00c580d8 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c570e8 bytes ca1f0094
+ 00c580d8 bytes c21f0094
- 00c5711c ["INT_ADD", "register:40f0:8", ["const:c5711c:8", "const:4:8"]]
- 00c5711c ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c5810c ["INT_ADD", "register:40f0:8", ["const:c5810c:8", "const:4:8"]]
+ 00c5810c ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c5711c bytes bd1f0094
+ 00c5810c bytes b51f0094
- 00c57150 ["INT_ADD", "register:40f0:8", ["const:c57150:8", "const:4:8"]]
- 00c57150 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c58140 ["INT_ADD", "register:40f0:8", ["const:c58140:8", "const:4:8"]]
+ 00c58140 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c57150 bytes b01f0094
+ 00c58140 bytes a81f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43e4589c386a0b5f979f7e5f6912f7c8"></a>

### [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) → [`00c582c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md) FUN_00c582c8

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) · 呼出先 10件 [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c55cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c55/00c55cf8.md) · 呼出先 10件 [`00c564f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c56/00c564f4.md) [`00c587ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c587ec.md) [`00c589b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.50% / 新版 89.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 5件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c58540",
      "incomplete_value": true,
      "site": "00c58540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57550",
      "incomplete_value": true,
      "site": "00c57550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "definition_site": "00c58544",
      "incomplete_value": true,
      "site": "00c58544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57554",
      "incomplete_value": true,
      "site": "00c57554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00c58564",
      "incomplete_value": true,
      "site": "00c58564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57574",
      "incomplete_value": true,
      "site": "00c57574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c5834c",
      "PARAM",
      [
        "storage",
        "01128df4",
        null,
        null
      ]
    ],
    [
      "00c5835c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "pointer"
      ]
    ],
    [
      "00c58360",
      "READ",
      [
        "storage",
        "00ca4980",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c5834c",
      "PARAM",
      [
        "storage",
        "01129db4",
        null,
        null
      ]
    ],
    [
      "00c5835c",
      "READ",
      [
        "storage",
        "00ca5948",
        null,
        "pointer"
      ]
    ],
    [
      "00c58360",
      "READ",
      [
        "storage",
        "00ca5950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md#insn-00c57360) · [`00c573ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md#insn-00c573ec) · [`00c57424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md#insn-00c57424)
- 新版 [`00c58350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md#insn-00c58350) · [`00c583dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md#insn-00c583dc) · [`00c58414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c582c8.md#insn-00c58414)

~~~diff
- 00c57360 ["INT_ADD", "register:40f0:8", ["const:c57360:8", "const:4:8"]]
- 00c57360 ["CALL", null, ["callee:00c60020:8"]]
+ 00c58350 ["INT_ADD", "register:40f0:8", ["const:c58350:8", "const:4:8"]]
+ 00c58350 ["CALL", null, ["callee:00c60020:8"]]
- 00c57360 bytes 3c1f0094
+ 00c58350 bytes 341f0094
- 00c573ec ["INT_ADD", "register:40f0:8", ["const:c573ec:8", "const:4:8"]]
- 00c573ec ["CALL", null, ["callee:00c60000:8"]]
+ 00c583dc ["INT_ADD", "register:40f0:8", ["const:c583dc:8", "const:4:8"]]
+ 00c583dc ["CALL", null, ["callee:00c60000:8"]]
- 00c573ec bytes 111f0094
+ 00c583dc bytes 091f0094
- 00c57424 ["INT_ADD", "register:40f0:8", ["const:c57424:8", "const:4:8"]]
- 00c57424 ["CALL", null, ["callee:00c60000:8"]]
+ 00c58414 ["INT_ADD", "register:40f0:8", ["const:c58414:8", "const:4:8"]]
+ 00c58414 ["CALL", null, ["callee:00c60000:8"]]
- 00c57424 bytes 031f0094
+ 00c58414 bytes fb1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0beda29f56c44416435cc0480ad8458f"></a>

### [`00c576dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md) → [`00c586cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md) FUN_00c586cc

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c575ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c575ac.md) [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) · 呼出先 4件 [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 2件 [`00c5859c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c5859c.md) [`00c589b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md) · 呼出先 4件 [`00c573b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c57/00c573b0.md) [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c58714",
      "incomplete_value": true,
      "site": "00c58718",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57724",
      "incomplete_value": true,
      "site": "00c57728",
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
            "const:130:8"
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
      "definition_site": "00c58708",
      "incomplete_value": false,
      "site": "00c58718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57718",
      "incomplete_value": false,
      "site": "00c57728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:b62:8"
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
      "definition_site": "00c58798",
      "incomplete_value": true,
      "site": "00c5879c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c577a8",
      "incomplete_value": true,
      "site": "00c577ac",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c58708",
      "PARAM",
      [
        "storage",
        "002b4b62",
        null,
        "string"
      ]
    ],
    [
      "00c5870c",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c58714",
      "PARAM",
      [
        "storage",
        "0112a8f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c58708",
      "PARAM",
      [
        "storage",
        "002b4c40",
        null,
        "string"
      ]
    ],
    [
      "00c5870c",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c58714",
      "PARAM",
      [
        "storage",
        "0112b8f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md#insn-00c57728) · [`00c577ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md#insn-00c577ac) · [`00c57710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md#insn-00c57710)
- 新版 [`00c58718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md#insn-00c58718) · [`00c5879c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md#insn-00c5879c) · [`00c58700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c586cc.md#insn-00c58700)

~~~diff
- 00c57728 ["INT_ADD", "register:40f0:8", ["const:c57728:8", "const:4:8"]]
- 00c57728 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c58718 ["INT_ADD", "register:40f0:8", ["const:c58718:8", "const:4:8"]]
+ 00c58718 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c57728 bytes 3a1e0094
+ 00c58718 bytes 321e0094
- 00c577ac ["INT_ADD", "register:40f0:8", ["const:c577ac:8", "const:4:8"]]
- 00c577ac ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c5879c ["INT_ADD", "register:40f0:8", ["const:c5879c:8", "const:4:8"]]
+ 00c5879c ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c577ac bytes 191e0094
+ 00c5879c bytes 111e0094
- 00c57710 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00c58700 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00c57710 bytes 34020090
+ 00c58700 bytes 34020090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e9717942af227b4315012d68f512aa"></a>

### [`00c57b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md) → [`00c58b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58b1c.md) FUN_00c58b1c

採用 · 移動量 `+0xff0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c589b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c589b4.md) · 呼出先 4件 [`00c5b250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b250.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ffe0.md) [`0112b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.13% / 新版 84.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c58bc4",
      "incomplete_value": true,
      "site": "00c58bc8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57bd4",
      "incomplete_value": true,
      "site": "00c57bd8",
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
            "const:130:8"
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
      "definition_site": "00c58bac",
      "incomplete_value": false,
      "site": "00c58bc8",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57bbc",
      "incomplete_value": false,
      "site": "00c57bd8",
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
            "const:ec4:8"
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
      "definition_site": "00c58bb8",
      "incomplete_value": false,
      "site": "00c58bc8",
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
            "const:b31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57bc8",
      "incomplete_value": false,
      "site": "00c57bd8",
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
            "const:a64:8"
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
      "00c58bac",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c58bb0",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c58bb8",
      "PARAM",
      [
        "storage",
        "002a9a64",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c58bac",
      "PARAM",
      [
        "storage",
        "002a0f04",
        null,
        "string"
      ]
    ],
    [
      "00c58bb0",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c58bb8",
      "PARAM",
      [
        "storage",
        "002a9b31",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md#insn-00c57bd8) · [`00c57c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md#insn-00c57c18) · [`00c57bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md#insn-00c57bb4)
- 新版 [`00c58bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58b1c.md#insn-00c58bc8) · [`00c58c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58b1c.md#insn-00c58c08) · [`00c58ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58b1c.md#insn-00c58ba4)

~~~diff
- 00c57bd8 ["INT_ADD", "register:40f0:8", ["const:c57bd8:8", "const:4:8"]]
- 00c57bd8 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c58bc8 ["INT_ADD", "register:40f0:8", ["const:c58bc8:8", "const:4:8"]]
+ 00c58bc8 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c57bd8 bytes 0e1d0094
+ 00c58bc8 bytes 061d0094
- 00c57c18 ["INT_ADD", "register:40f0:8", ["const:c57c18:8", "const:4:8"]]
- 00c57c18 ["CALL", null, ["callee:00c5ffe0:8"]]
+ 00c58c08 ["INT_ADD", "register:40f0:8", ["const:c58c08:8", "const:4:8"]]
+ 00c58c08 ["CALL", null, ["callee:00c5ffe0:8"]]
- 00c57c18 bytes fe1c0094
+ 00c58c08 bytes f61c0094
- 00c57bb4 ["COPY", "register:4098:8", ["const:c9b000:8"]]
+ 00c58ba4 ["COPY", "register:4098:8", ["const:c9c000:8"]]
- 00c57bb4 bytes 33020090
+ 00c58ba4 bytes 33020090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e3031d5993c4cd7868b2134e128210"></a>

### [`00c57dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md) → [`00c58d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58d8c.md) _Znwm

採用 · 移動量 `+0xfd0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) · 呼出先 6件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b10.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) · 呼出先 6件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ae0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c58dec",
      "incomplete_value": true,
      "site": "00c58df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "old": {
      "definition_site": "00c57e1c",
      "incomplete_value": true,
      "site": "00c57e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
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
      "definition_site": "00c58df0",
      "incomplete_value": true,
      "site": "00c58df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c57e20",
      "incomplete_value": true,
      "site": "00c57e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
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
      "00c58dec",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c58dec",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c58df0",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c58dec",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c58dec",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c58df0",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md#insn-00c57e24) · [`00c57dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md#insn-00c57dd8) · [`00c57de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md#insn-00c57de0)
- 新版 [`00c58df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58d8c.md#insn-00c58df4) · [`00c58da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58d8c.md#insn-00c58da8) · [`00c58db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58d8c.md#insn-00c58db0)

~~~diff
- 00c57e24 ["INT_ADD", "register:40f0:8", ["const:c57e24:8", "const:4:8"]]
- 00c57e24 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00c58df4 ["INT_ADD", "register:40f0:8", ["const:c58df4:8", "const:4:8"]]
+ 00c58df4 ["CALL", null, ["callee:00c58fb0:8"]]
- 00c57e24 bytes 6f000094
+ 00c58df4 bytes 6f000094
- 00c57dd8 ["INT_ADD", "register:40f0:8", ["const:c57dd8:8", "const:4:8"]]
- 00c57dd8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c58da8 ["INT_ADD", "register:40f0:8", ["const:c58da8:8", "const:4:8"]]
+ 00c58da8 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c57dd8 bytes c6080094
+ 00c58da8 bytes c6080094
- 00c57de0 ["INT_ADD", "register:40f0:8", ["const:c57de0:8", "const:4:8"]]
- 00c57de0 ["CALL", null, ["callee:00c5fe80:8"]]
+ 00c58db0 ["INT_ADD", "register:40f0:8", ["const:c58db0:8", "const:4:8"]]
+ 00c58db0 ["CALL", null, ["callee:00c5fe80:8"]]
- 00c57de0 bytes 341c0094
+ 00c58db0 bytes 341c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5642ef2dbeb3a61512d7473acefe6dc9"></a>

### [`00c57e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md) → [`00c58e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58e00.md) _ZnwmSt11align_val_t

採用 · 移動量 `+0xfd0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef90.md) · 呼出先 6件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b10.md) [`00c5eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eeb0.md)
- 新版 呼出元 1件 [`00c5ff60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ff60.md) · 呼出先 6件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ae0.md) [`00c5fe80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c58e84",
      "incomplete_value": true,
      "site": "00c58e8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "old": {
      "definition_site": "00c57eb4",
      "incomplete_value": true,
      "site": "00c57ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
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
      "definition_site": "00c58e88",
      "incomplete_value": true,
      "site": "00c58e8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00c57eb8",
      "incomplete_value": true,
      "site": "00c57ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
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
      "00c58e84",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c58e84",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c58e88",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c58e84",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c58e84",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c58e88",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md#insn-00c57ebc) · [`00c57e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md#insn-00c57e68) · [`00c57e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md#insn-00c57e74)
- 新版 [`00c58e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58e00.md#insn-00c58e8c) · [`00c58e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58e00.md#insn-00c58e38) · [`00c58e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58e00.md#insn-00c58e44)

~~~diff
- 00c57ebc ["INT_ADD", "register:40f0:8", ["const:c57ebc:8", "const:4:8"]]
- 00c57ebc ["CALL", null, ["callee:00c58fb0:8"]]
+ 00c58e8c ["INT_ADD", "register:40f0:8", ["const:c58e8c:8", "const:4:8"]]
+ 00c58e8c ["CALL", null, ["callee:00c58fb0:8"]]
- 00c57ebc bytes 49000094
+ 00c58e8c bytes 49000094
- 00c57e68 ["INT_ADD", "register:40f0:8", ["const:c57e68:8", "const:4:8"]]
- 00c57e68 ["CALL", null, ["callee:00c5ff70:8"]]
+ 00c58e38 ["INT_ADD", "register:40f0:8", ["const:c58e38:8", "const:4:8"]]
+ 00c58e38 ["CALL", null, ["callee:00c5ff70:8"]]
- 00c57e68 bytes 4e1c0094
+ 00c58e38 bytes 4e1c0094
- 00c57e74 ["INT_ADD", "register:40f0:8", ["const:c57e74:8", "const:4:8"]]
- 00c57e74 ["CALL", null, ["callee:00c5fe80:8"]]
+ 00c58e44 ["INT_ADD", "register:40f0:8", ["const:c58e44:8", "const:4:8"]]
+ 00c58e44 ["CALL", null, ["callee:00c5fe80:8"]]
- 00c57e74 bytes 0f1c0094
+ 00c58e44 bytes 0f1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

