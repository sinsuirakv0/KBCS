# v16.0.2 → v16.0.3 · 最優先の変更候補 (1)

[一覧の目次](README.md)

<a id="compare-cee5dff085cf3ee0bc2340facd4d9fee"></a>

### [`0043aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb8.md) → [`0043b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d8.md) _INIT_3

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bfa1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1ac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bfb1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1a0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b1f4",
      "incomplete_value": false,
      "site": "0043b1f8",
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
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043aed4",
      "incomplete_value": false,
      "site": "0043aed8",
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
            "const:a00:8"
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
      "definition_site": "0043b20c",
      "incomplete_value": true,
      "site": "0043b218",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:c00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043aeec",
      "incomplete_value": true,
      "site": "0043aef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b208",
      "incomplete_value": false,
      "site": "0043b218",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043aee8",
      "incomplete_value": false,
      "site": "0043aef8",
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
            "const:9d8:8"
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
      "0043b1e8",
      "READ",
      [
        "storage",
        "00ca4a00",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b1f4",
      "PARAM",
      [
        "storage",
        "00ca4a00",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b208",
      "PARAM",
      [
        "storage",
        "00ca49d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043b1e8",
      "READ",
      [
        "storage",
        "00ca59c0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b1f4",
      "PARAM",
      [
        "storage",
        "00ca59c0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b208",
      "PARAM",
      [
        "storage",
        "00ca5998",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043aed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb8.md#insn-0043aed8) · [`0043aef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb8.md#insn-0043aef8) · [`0043aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb8.md#insn-0043aec0)
- 新版 [`0043b1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d8.md#insn-0043b1f8) · [`0043b218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d8.md#insn-0043b218) · [`0043b1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d8.md#insn-0043b1e0)

~~~diff
- 0043aed8 ["INT_ADD", "register:40f0:8", ["const:43aed8:8", "const:4:8"]]
- 0043aed8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 0043b1f8 ["INT_ADD", "register:40f0:8", ["const:43b1f8:8", "const:4:8"]]
+ 0043b1f8 ["CALL", null, ["callee:00c58ef0:8"]]
- 0043aed8 bytes 12742094
+ 0043b1f8 bytes 3e772094
- 0043aef8 ["INT_ADD", "register:40f0:8", ["const:43aef8:8", "const:4:8"]]
- 0043aef8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043b218 ["INT_ADD", "register:40f0:8", ["const:43b218:8", "const:4:8"]]
+ 0043b218 ["CALL", null, ["callee:00c58ed0:8"]]
- 0043aef8 bytes 02742094
+ 0043b218 bytes 2e772094
- 0043aec0 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b1e0 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043aec0 bytes 484300d0
+ 0043b1e0 bytes 484300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aedb864e8b69e4ecc9b2ed0d4d338950"></a>

### [`0043af6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md) → [`0043b28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b28c.md) Java_jp_co_ponos_battlecats_MyActivity_appInit

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0055f500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f500.md) [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) [`00b2b988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b988.md) [`00b2c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md) [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0055f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f820.md) [`0056aec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md) [`00b2c97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2c/00b2c97c.md) [`00b2d290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2d290.md) [`00b2ded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2ded8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043b2d0",
      "incomplete_value": false,
      "site": "0043b2dc",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afb0",
      "incomplete_value": false,
      "site": "0043afbc",
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
            "const:78:8"
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
      "definition_site": "0043b2f4",
      "incomplete_value": false,
      "site": "0043b2f4",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afd4",
      "incomplete_value": false,
      "site": "0043afd4",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b2f4",
      "incomplete_value": false,
      "site": "0043b2f4",
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
                "const:9d0:8"
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
      "definition_site": "0043afd4",
      "incomplete_value": false,
      "site": "0043afd4",
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
                "const:a10:8"
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
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b2a0",
      "READ",
      [
        "storage",
        "00ca4a10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b2dc",
      "DATA",
      [
        "storage",
        "00c63078",
        null,
        "undefined *"
      ]
    ],
    [
      "0043b2f0",
      "READ",
      [
        "storage",
        "00ca4a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b2a0",
      "READ",
      [
        "storage",
        "00ca59d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b2dc",
      "DATA",
      [
        "storage",
        "00c64048",
        null,
        "undefined *"
      ]
    ],
    [
      "0043b2f0",
      "READ",
      [
        "storage",
        "00ca59d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md#insn-0043b008) · [`0043af7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md#insn-0043af7c) · [`0043af80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md#insn-0043af80)
- 新版 [`0043b328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b28c.md#insn-0043b328) · [`0043b29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b28c.md#insn-0043b29c) · [`0043b2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b28c.md#insn-0043b2a0)

~~~diff
- 0043b008 ["INT_ADD", "register:40f0:8", ["const:43b008:8", "const:4:8"]]
- 0043b008 ["CALL", null, ["callee:00b2ded8:8"]]
+ 0043b328 ["INT_ADD", "register:40f0:8", ["const:43b328:8", "const:4:8"]]
+ 0043b328 ["CALL", null, ["callee:00b2ded8:8"]]
- 0043b008 bytes b7c71b94
+ 0043b328 bytes ecca1b94
- 0043af7c ["COPY", "register:40b0:8", ["const:ca4000:8"]]
+ 0043b29c ["COPY", "register:40b0:8", ["const:ca5000:8"]]
- 0043af7c bytes 564300d0
+ 0043b29c bytes 564300d0
- 0043af80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a10:8"]]
- 0043af80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043b2a0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9d0:8"]]
+ 0043b2a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043af80 bytes c80a45f9
+ 0043b2a0 bytes c8ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baa377c33b33da186111fab0733082d9"></a>

### [`0043b03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md) → [`0043b35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b35c.md) Java_jp_co_ponos_battlecats_MyActivity_appUpdateDraw

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00555494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555494.md) [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) [`00b2b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b990.md) [`00b2d3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d3d0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005557b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005557b4.md) [`0058fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md) [`00b2c984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2c/00b2c984.md) [`00b2e3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e3c4.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3c8",
      "incomplete_value": true,
      "site": "0043b3c8",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b0a8",
      "incomplete_value": true,
      "site": "0043b0a8",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b428",
      "incomplete_value": true,
      "site": "0043b428",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b108",
      "incomplete_value": true,
      "site": "0043b108",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b3a4",
      "incomplete_value": true,
      "site": "0043b3bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b084",
      "incomplete_value": true,
      "site": "0043b09c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
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
      "0043b388",
      "READ",
      [
        "storage",
        "00ca4a28",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b394",
      "READ",
      [
        "storage",
        "00ca4a20",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b3a4",
      "READ",
      [
        "storage",
        "00ca4a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b388",
      "READ",
      [
        "storage",
        "00ca59e8",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b394",
      "READ",
      [
        "storage",
        "00ca59e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b3a4",
      "READ",
      [
        "storage",
        "00ca59d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md#insn-0043b09c) · [`0043b0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md#insn-0043b0a8) · [`0043b0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md#insn-0043b0cc)
- 新版 [`0043b3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b35c.md#insn-0043b3bc) · [`0043b3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b35c.md#insn-0043b3c8) · [`0043b3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b35c.md#insn-0043b3ec)

~~~diff
- 0043b09c ["INT_ADD", "register:40f0:8", ["const:43b09c:8", "const:4:8"]]
- 0043b09c ["CALL", null, ["callee:00b2e3c4:8"]]
+ 0043b3bc ["INT_ADD", "register:40f0:8", ["const:43b3bc:8", "const:4:8"]]
+ 0043b3bc ["CALL", null, ["callee:00b2e3c4:8"]]
- 0043b09c bytes cdc81b94
+ 0043b3bc bytes 02cc1b94
- 0043b0a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a20:8"]]
- 0043b0a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b3c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9e0:8"]]
+ 0043b3c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b0a8 bytes b31205f9
+ 0043b3c8 bytes b3f204f9
- 0043b0cc ["INT_ADD", "register:40f0:8", ["const:43b0cc:8", "const:4:8"]]
- 0043b0cc ["CALL", null, ["callee:00b2c984:8"]]
+ 0043b3ec ["INT_ADD", "register:40f0:8", ["const:43b3ec:8", "const:4:8"]]
+ 0043b3ec ["CALL", null, ["callee:00b2c984:8"]]
- 0043b0cc bytes 31c21b94
+ 0043b3ec bytes 66c51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6695959d8620bcb3863e5819f0021785"></a>

### [`0043b128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md) → [`0043b448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b448.md) Java_jp_co_ponos_battlecats_MyActivity_gfxInit

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043b23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b23c.md) [`0058f7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7bc.md) [`005923f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b55c.md) [`0058fadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fadc.md) [`00592710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592710.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b490",
      "incomplete_value": false,
      "site": "0043b490",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b170",
      "incomplete_value": false,
      "site": "0043b170",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0043b494",
      "incomplete_value": true,
      "site": "0043b494",
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
      "definition_site": "0043b174",
      "incomplete_value": true,
      "site": "0043b174",
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
      "definition_site": "0043b4f4",
      "incomplete_value": true,
      "site": "0043b4f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b1d4",
      "incomplete_value": true,
      "site": "0043b1d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b46c",
      "READ",
      [
        "storage",
        "00ca4a40",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b488",
      "READ",
      [
        "storage",
        "00ca4a38",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b490",
      "WRITE",
      [
        "storage",
        "00ca4a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b46c",
      "READ",
      [
        "storage",
        "00ca5a00",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b488",
      "READ",
      [
        "storage",
        "00ca59f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b490",
      "WRITE",
      [
        "storage",
        "00ca59f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md#insn-0043b1d8) · [`0043b204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md#insn-0043b204) · [`0043b224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md#insn-0043b224)
- 新版 [`0043b4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b448.md#insn-0043b4f8) · [`0043b524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b448.md#insn-0043b524) · [`0043b544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b448.md#insn-0043b544)

~~~diff
- 0043b1d8 ["INT_ADD", "register:40f0:8", ["const:43b1d8:8", "const:4:8"]]
- 0043b1d8 ["CALL", null, ["callee:0058fadc:8"]]
+ 0043b4f8 ["INT_ADD", "register:40f0:8", ["const:43b4f8:8", "const:4:8"]]
+ 0043b4f8 ["CALL", null, ["callee:0058fadc:8"]]
- 0043b1d8 bytes 79510594
+ 0043b4f8 bytes 79510594
- 0043b204 ["INT_ADD", "register:40f0:8", ["const:43b204:8", "const:4:8"]]
- 0043b204 ["CALL", null, ["callee:00c58ef0:8"]]
+ 0043b524 ["INT_ADD", "register:40f0:8", ["const:43b524:8", "const:4:8"]]
+ 0043b524 ["CALL", null, ["callee:00c58ef0:8"]]
- 0043b204 bytes 47732094
+ 0043b524 bytes 73762094
- 0043b224 ["INT_ADD", "register:40f0:8", ["const:43b224:8", "const:4:8"]]
- 0043b224 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043b544 ["INT_ADD", "register:40f0:8", ["const:43b544:8", "const:4:8"]]
+ 0043b544 ["CALL", null, ["callee:00c58ed0:8"]]
- 0043b224 bytes 37732094
+ 0043b544 bytes 63762094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52450a573294d47f1f33ffcd0112efa7"></a>

### [`0043b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b28c.md) → [`0043b5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5ac.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableWidth

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b5b4",
      "incomplete_value": true,
      "site": "0043b5b8",
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
      "definition_site": "0043b294",
      "incomplete_value": true,
      "site": "0043b298",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b5b4",
      "READ",
      [
        "storage",
        "00ca4d88",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b5b4",
      "READ",
      [
        "storage",
        "00ca5d48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b28c.md#insn-0043b28c) · [`0043b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b28c.md#insn-0043b290)
- 新版 [`0043b5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5ac.md#insn-0043b5ac) · [`0043b5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5ac.md#insn-0043b5b0)

~~~diff
- 0043b28c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b5ac ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043b28c bytes 484300b0
+ 0043b5ac bytes 484300d0
- 0043b290 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0043b290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0043b5b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b290 bytes 08c13591
+ 0043b5b0 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4a674f9876c75ebe162715dc1066af2"></a>

### [`0043b29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b29c.md) → [`0043b5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5bc.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableHeight

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b5c4",
      "incomplete_value": true,
      "site": "0043b5c8",
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
      "definition_site": "0043b2a4",
      "incomplete_value": true,
      "site": "0043b2a8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b5c4",
      "READ",
      [
        "storage",
        "00ca4d8c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b5c4",
      "READ",
      [
        "storage",
        "00ca5d4c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b29c.md#insn-0043b29c) · [`0043b2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b29c.md#insn-0043b2a0)
- 新版 [`0043b5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5bc.md#insn-0043b5bc) · [`0043b5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5bc.md#insn-0043b5c0)

~~~diff
- 0043b29c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b5bc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043b29c bytes 484300b0
+ 0043b5bc bytes 484300d0
- 0043b2a0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0043b2a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5c0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0043b5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b2a0 bytes 08c13591
+ 0043b5c0 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5357847c3a929462fef2c7afb5a710ce"></a>

### [`0043b2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ac.md) → [`0043b5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5cc.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowWidth

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b5d4",
      "incomplete_value": true,
      "site": "0043b5d8",
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
      "definition_site": "0043b2b4",
      "incomplete_value": true,
      "site": "0043b2b8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b5d4",
      "READ",
      [
        "storage",
        "00ca4d78",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b5d4",
      "READ",
      [
        "storage",
        "00ca5d38",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ac.md#insn-0043b2ac) · [`0043b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ac.md#insn-0043b2b0)
- 新版 [`0043b5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5cc.md#insn-0043b5cc) · [`0043b5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5cc.md#insn-0043b5d0)

~~~diff
- 0043b2ac ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b5cc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043b2ac bytes 484300b0
+ 0043b5cc bytes 484300d0
- 0043b2b0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0043b2b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5d0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0043b5d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b2b0 bytes 08c13591
+ 0043b5d0 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652e0c00706b648b7f0d1663b6a4dbba"></a>

### [`0043b2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2bc.md) → [`0043b5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5dc.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowHeight

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b5e4",
      "incomplete_value": true,
      "site": "0043b5e8",
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
      "definition_site": "0043b2c4",
      "incomplete_value": true,
      "site": "0043b2c8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b5e4",
      "READ",
      [
        "storage",
        "00ca4d7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b5e4",
      "READ",
      [
        "storage",
        "00ca5d3c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2bc.md#insn-0043b2bc) · [`0043b2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2bc.md#insn-0043b2c0)
- 新版 [`0043b5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5dc.md#insn-0043b5dc) · [`0043b5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5dc.md#insn-0043b5e0)

~~~diff
- 0043b2bc ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b5dc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043b2bc bytes 484300b0
+ 0043b5dc bytes 484300d0
- 0043b2c0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0043b2c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5e0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0043b5e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b2c0 bytes 08c13591
+ 0043b5e0 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-540e874a4c989f8242efb37e1e8c9e91"></a>

### [`0043b2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2cc.md) → [`0043b5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5ec.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeWidth

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b5f4",
      "incomplete_value": true,
      "site": "0043b5f8",
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
      "definition_site": "0043b2d4",
      "incomplete_value": true,
      "site": "0043b2d8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b5f4",
      "READ",
      [
        "storage",
        "00ca4d80",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b5f4",
      "READ",
      [
        "storage",
        "00ca5d40",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2cc.md#insn-0043b2cc) · [`0043b2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2cc.md#insn-0043b2d0)
- 新版 [`0043b5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5ec.md#insn-0043b5ec) · [`0043b5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5ec.md#insn-0043b5f0)

~~~diff
- 0043b2cc ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b5ec ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043b2cc bytes 484300b0
+ 0043b5ec bytes 484300d0
- 0043b2d0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0043b2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5f0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0043b5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b2d0 bytes 08c13591
+ 0043b5f0 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e43cff25741126add728fc1971efbdf2"></a>

### [`0043b2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2dc.md) → [`0043b5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5fc.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeHeight

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b604",
      "incomplete_value": true,
      "site": "0043b608",
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
      "definition_site": "0043b2e4",
      "incomplete_value": true,
      "site": "0043b2e8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b604",
      "READ",
      [
        "storage",
        "00ca4d84",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b604",
      "READ",
      [
        "storage",
        "00ca5d44",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2dc.md#insn-0043b2dc) · [`0043b2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2dc.md#insn-0043b2e0)
- 新版 [`0043b5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5fc.md#insn-0043b5fc) · [`0043b600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b5fc.md#insn-0043b600)

~~~diff
- 0043b2dc ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043b5fc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043b2dc bytes 484300b0
+ 0043b5fc bytes 484300d0
- 0043b2e0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0043b2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b600 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0043b600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b2e0 bytes 08c13591
+ 0043b600 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec1dd9c88d8267b8ad5d34191409b99e"></a>

### [`0043b2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md) → [`0043b60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b60c.md) Java_jp_co_ponos_battlecats_MyActivity_gfxResize

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md) [`00b2ded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2ded8.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 74.47% / 新版 74.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b668",
      "incomplete_value": true,
      "site": "0043b668",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b348",
      "incomplete_value": true,
      "site": "0043b348",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b668",
      "incomplete_value": true,
      "site": "0043b668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b348",
      "incomplete_value": true,
      "site": "0043b348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b694",
      "incomplete_value": true,
      "site": "0043b694",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b374",
      "incomplete_value": true,
      "site": "0043b374",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b624",
      "READ",
      [
        "storage",
        "00c9ac40",
        null,
        "pointer"
      ]
    ],
    [
      "0043b628",
      "READ",
      [
        "storage",
        "00c9ac48",
        null,
        "pointer"
      ]
    ],
    [
      "0043b634",
      "READ",
      [
        "storage",
        "00ca655c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b624",
      "READ",
      [
        "storage",
        "00c9bc10",
        null,
        "pointer"
      ]
    ],
    [
      "0043b628",
      "READ",
      [
        "storage",
        "00c9bc18",
        null,
        "pointer"
      ]
    ],
    [
      "0043b634",
      "READ",
      [
        "storage",
        "00ca751c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md#insn-0043b2f8) · [`0043b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md#insn-0043b2fc) · [`0043b300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md#insn-0043b300)
- 新版 [`0043b618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b60c.md#insn-0043b618) · [`0043b61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b60c.md#insn-0043b61c) · [`0043b620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b60c.md#insn-0043b620)

~~~diff
- 0043b2f8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0043b618 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0043b2f8 bytes e84200f0
+ 0043b618 bytes 08430090
- 0043b2fc ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0043b61c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0043b2fc bytes e94200f0
+ 0043b61c bytes 09430090
- 0043b300 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 0043b620 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 0043b300 bytes ea4200f0
+ 0043b620 bytes 0a430090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5baa25f1efefe90efeb0434a7c58ea55"></a>

### [`0043b3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md) → [`0043b6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b6c8.md) Java_jp_co_ponos_battlecats_MyActivity_appTouch

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b2d2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d2f8.md) [`00b2d340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d340.md) [`00b2d388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d388.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b2e2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e2ec.md) [`00b2e334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e334.md) [`00b2e37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2e/00b2e37c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b770",
      "incomplete_value": true,
      "site": "0043b770",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b450",
      "incomplete_value": true,
      "site": "0043b450",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b774",
      "incomplete_value": true,
      "site": "0043b774",
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
            "const:a0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b454",
      "incomplete_value": true,
      "site": "0043b454",
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
            "const:a4c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b714",
      "incomplete_value": true,
      "site": "0043b71c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b3f4",
      "incomplete_value": true,
      "site": "0043b3fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
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
      "0043b714",
      "READ",
      [
        "storage",
        "00ca4a10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b738",
      "READ",
      [
        "storage",
        "00ca4a10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b748",
      "READ",
      [
        "storage",
        "00ca4a48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b714",
      "READ",
      [
        "storage",
        "00ca59d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b738",
      "READ",
      [
        "storage",
        "00ca59d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b748",
      "READ",
      [
        "storage",
        "00ca5a08",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md#insn-0043b3fc) · [`0043b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md#insn-0043b420) · [`0043b44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b3a8.md#insn-0043b44c)
- 新版 [`0043b71c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b6c8.md#insn-0043b71c) · [`0043b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b6c8.md#insn-0043b740) · [`0043b76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b6c8.md#insn-0043b76c)

~~~diff
- 0043b3fc ["INT_ADD", "register:40f0:8", ["const:43b3fc:8", "const:4:8"]]
- 0043b3fc ["CALL", null, ["callee:00b2e334:8"]]
+ 0043b71c ["INT_ADD", "register:40f0:8", ["const:43b71c:8", "const:4:8"]]
+ 0043b71c ["CALL", null, ["callee:00b2e334:8"]]
- 0043b3fc bytes d1c71b94
+ 0043b71c bytes 06cb1b94
- 0043b420 ["INT_ADD", "register:40f0:8", ["const:43b420:8", "const:4:8"]]
- 0043b420 ["CALL", null, ["callee:00b2e37c:8"]]
+ 0043b740 ["INT_ADD", "register:40f0:8", ["const:43b740:8", "const:4:8"]]
+ 0043b740 ["CALL", null, ["callee:00b2e37c:8"]]
- 0043b420 bytes dac71b94
+ 0043b740 bytes 0fcb1b94
- 0043b44c ["INT_ADD", "register:40f0:8", ["const:43b44c:8", "const:4:8"]]
- 0043b44c ["CALL", null, ["callee:00b2e2ec:8"]]
+ 0043b76c ["INT_ADD", "register:40f0:8", ["const:43b76c:8", "const:4:8"]]
+ 0043b76c ["CALL", null, ["callee:00b2e2ec:8"]]
- 0043b44c bytes abc71b94
+ 0043b76c bytes e0ca1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b258c472d766bef99a7daffa1d10d58"></a>

### [`0043b698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b698.md) → [`0043b9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b9b8.md) Java_jp_co_ponos_battlecats_MyActivity_kill

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b2bc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bc68.md) [`00b2c4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b2cc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2c/00b2cc5c.md) [`00b2d4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2d4b4.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b9d0",
      "incomplete_value": true,
      "site": "0043b9d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6b0",
      "incomplete_value": true,
      "site": "0043b6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
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
      "0043b9d0",
      "READ",
      [
        "storage",
        "00ca4a10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b9d8",
      "READ",
      [
        "storage",
        "00ca4a10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b9e0",
      "READ",
      [
        "storage",
        "00ca4a18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b9d0",
      "READ",
      [
        "storage",
        "00ca59d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b9d8",
      "READ",
      [
        "storage",
        "00ca59d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b9e0",
      "READ",
      [
        "storage",
        "00ca59d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b698.md#insn-0043b6b4) · [`0043b6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b698.md#insn-0043b6a4) · [`0043b6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b698.md#insn-0043b6a8)
- 新版 [`0043b9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b9b8.md#insn-0043b9d4) · [`0043b9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b9b8.md#insn-0043b9c4) · [`0043b9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b9b8.md#insn-0043b9c8)

~~~diff
- 0043b6b4 ["INT_ADD", "register:40f0:8", ["const:43b6b4:8", "const:4:8"]]
- 0043b6b4 ["CALL", null, ["callee:00b2cc5c:8"]]
+ 0043b9d4 ["INT_ADD", "register:40f0:8", ["const:43b9d4:8", "const:4:8"]]
+ 0043b9d4 ["CALL", null, ["callee:00b2cc5c:8"]]
- 0043b6b4 bytes 6dc11b94
+ 0043b9d4 bytes a2c41b94
- 0043b6a4 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 0043b9c4 ["COPY", "register:40a0:8", ["const:ca5000:8"]]
- 0043b6a4 bytes 544300b0
+ 0043b9c4 bytes 544300d0
- 0043b6a8 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 0043b6a8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0043b6a8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0043b6a8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0043b9c8 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 0043b9c8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0043b9c8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0043b9c8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0043b6a8 bytes 94422891
+ 0043b9c8 bytes 94422791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df9a257133780a7e1f4607e21038f005"></a>

### [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) → [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) FUN_0043bac4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 272件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c8c.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 272件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043dadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440fac.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0043bad0",
      "incomplete_value": false,
      "site": "0043bad4",
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
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b7b0",
      "incomplete_value": false,
      "site": "0043b7b4",
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
            "const:ecf:8"
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
      "0043bad0",
      "PARAM",
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
      "0043bad0",
      "PARAM",
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

- 旧版 [`0043b7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md#insn-0043b7b4) · [`0043b7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md#insn-0043b7b0)
- 新版 [`0043bad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md#insn-0043bad4) · [`0043bad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md#insn-0043bad0)

~~~diff
- 0043b7b4 ["INT_ADD", "register:40f0:8", ["const:43b7b4:8", "const:4:8"]]
- 0043b7b4 ["CALL", null, ["callee:0043bad8:8"]]
+ 0043bad4 ["INT_ADD", "register:40f0:8", ["const:43bad4:8", "const:4:8"]]
+ 0043bad4 ["CALL", null, ["callee:0043bad8:8"]]
- 0043b7b4 bytes 01000094
+ 0043bad4 bytes 01000094
- 0043b7b0 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 0043b7b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043b7b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043b7b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043bad0 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 0043bad0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043bad0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043bad0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043b7b0 bytes 003c3b91
+ 0043bad0 bytes 00b43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61082e8d887188aaf59de5e693b07e68"></a>

### [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md) → [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md) FUN_0043bad8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 234件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00443758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443758.md) [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`0045cdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md) · 呼出先 4件 [`0043b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b808.md) [`00c37d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 235件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00443a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a78.md) [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) [`0045d0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d0ec.md) · 呼出先 4件 [`0043bb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb28.md) [`00c38d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043bb08",
      "incomplete_value": true,
      "site": "0043bb10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "0043b7e8",
      "incomplete_value": true,
      "site": "0043b7f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c60:8"
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
      "definition_site": "0043bb0c",
      "incomplete_value": true,
      "site": "0043bb10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "0043b7ec",
      "incomplete_value": true,
      "site": "0043b7f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c68:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043bb08",
      "READ",
      [
        "storage",
        "00c9ac60",
        null,
        "pointer"
      ]
    ],
    [
      "0043bb08",
      "PARAM",
      [
        "storage",
        "00c968a8",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043bb0c",
      "READ",
      [
        "storage",
        "00c9ac68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043bb08",
      "READ",
      [
        "storage",
        "00c9bc30",
        null,
        "pointer"
      ]
    ],
    [
      "0043bb08",
      "PARAM",
      [
        "storage",
        "00c97878",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043bb0c",
      "READ",
      [
        "storage",
        "00c9bc38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md#insn-0043b7f0) · [`0043b7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md#insn-0043b7cc) · [`0043b7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md#insn-0043b7d8)
- 新版 [`0043bb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md#insn-0043bb10) · [`0043baec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md#insn-0043baec) · [`0043baf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md#insn-0043baf8)

~~~diff
- 0043b7f0 ["INT_ADD", "register:40f0:8", ["const:43b7f0:8", "const:4:8"]]
- 0043b7f0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0043bb10 ["INT_ADD", "register:40f0:8", ["const:43bb10:8", "const:4:8"]]
+ 0043bb10 ["CALL", null, ["callee:00c58fb0:8"]]
- 0043b7f0 bytes fc712094
+ 0043bb10 bytes 28752094
- 0043b7cc ["INT_ADD", "register:40f0:8", ["const:43b7cc:8", "const:4:8"]]
- 0043b7cc ["CALL", null, ["callee:00c58f90:8"]]
+ 0043baec ["INT_ADD", "register:40f0:8", ["const:43baec:8", "const:4:8"]]
+ 0043baec ["CALL", null, ["callee:00c58f90:8"]]
- 0043b7cc bytes fd712094
+ 0043baec bytes 29752094
- 0043b7d8 ["INT_ADD", "register:40f0:8", ["const:43b7d8:8", "const:4:8"]]
- 0043b7d8 ["CALL", null, ["callee:0043bb28:8"]]
+ 0043baf8 ["INT_ADD", "register:40f0:8", ["const:43baf8:8", "const:4:8"]]
+ 0043baf8 ["CALL", null, ["callee:0043bb28:8"]]
- 0043b7d8 bytes 0c000094
+ 0043baf8 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eb73bc80a485676444ab224386e115f"></a>

### [`0043bdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdc8.md) → [`0043c0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0e8.md) FUN_0043c0e8

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
      "definition_site": "0043c0ec",
      "incomplete_value": false,
      "site": "0043c0f0",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bdcc",
      "incomplete_value": false,
      "site": "0043bdd0",
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
            "const:78:8"
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
      "0043c0f0",
      "DATA",
      [
        "storage",
        "00c63078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c0f0",
      "DATA",
      [
        "storage",
        "00c64048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdc8.md#insn-0043bdc8) · [`0043bdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdc8.md#insn-0043bdcc)
- 新版 [`0043c0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0e8.md#insn-0043c0e8) · [`0043c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0e8.md#insn-0043c0ec)

~~~diff
- 0043bdc8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0043c0e8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043bdc8 bytes 48410090
+ 0043c0e8 bytes 48410090
- 0043bdcc ["COPY", "tmp:0:8", ["const:78:8"]]
- 0043bdcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043bdcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043bdcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c0ec ["COPY", "tmp:0:8", ["const:48:8"]]
+ 0043c0ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c0ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c0ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043bdcc bytes 08e10191
+ 0043c0ec bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68d5b42c1edc81f5365021fff73a0874"></a>

### [`0043bdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdd8.md) → [`0043c0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0f8.md) FUN_0043c0f8

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
      "definition_site": "0043c108",
      "incomplete_value": false,
      "site": "0043c110",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bde8",
      "incomplete_value": false,
      "site": "0043bdf0",
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
            "const:78:8"
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
      "0043c110",
      "DATA",
      [
        "storage",
        "00c63078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c110",
      "DATA",
      [
        "storage",
        "00c64048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bde4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdd8.md#insn-0043bde4) · [`0043bde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdd8.md#insn-0043bde8) · [`0043bdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bdd8.md#insn-0043bdf4)
- 新版 [`0043c104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0f8.md#insn-0043c104) · [`0043c108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0f8.md#insn-0043c108) · [`0043c114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c0f8.md#insn-0043c114)

~~~diff
- 0043bde4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0043c104 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043bde4 bytes 48410090
+ 0043c104 bytes 48410090
- 0043bde8 ["COPY", "tmp:0:8", ["const:78:8"]]
- 0043bde8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043bde8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043bde8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c108 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 0043c108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043bde8 bytes 08e10191
+ 0043c108 bytes 08210191
- 0043bdf4 ["INT_ADD", "register:40f0:8", ["const:43bdf4:8", "const:4:8"]]
- 0043bdf4 ["CALL", null, ["callee:00c58f40:8"]]
+ 0043c114 ["INT_ADD", "register:40f0:8", ["const:43c114:8", "const:4:8"]]
+ 0043c114 ["CALL", null, ["callee:00c58f40:8"]]
- 0043bdf4 bytes 5f702094
+ 0043c114 bytes 8b732094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa2f563f7113a2a68c6e40dfbfac4c5"></a>

### [`0043be14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043be14.md) → [`0043c134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c134.md) _INIT_4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043af14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af14.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043b234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b234.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c170",
      "incomplete_value": true,
      "site": "0043c18c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043be50",
      "incomplete_value": true,
      "site": "0043be6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043c194",
      "incomplete_value": true,
      "site": "0043c1b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043be74",
      "incomplete_value": true,
      "site": "0043be90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043c1b4",
      "incomplete_value": true,
      "site": "0043c1d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043be94",
      "incomplete_value": true,
      "site": "0043beb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0043c170",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0043c194",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0043c1b4",
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
      "0043c170",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0043c194",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0043c1b4",
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

- 旧版 [`0043bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043be14.md#insn-0043bf74) · [`0043c04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043be14.md#insn-0043c04c) · [`0043c064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043be14.md#insn-0043c064)
- 新版 [`0043c294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c134.md#insn-0043c294) · [`0043c36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c134.md#insn-0043c36c) · [`0043c384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c134.md#insn-0043c384)

~~~diff
- 0043bf74 ["INT_ADD", "register:40f0:8", ["const:43bf74:8", "const:4:8"]]
- 0043bf74 ["CALL", null, ["callee:0043bb58:8"]]
+ 0043c294 ["INT_ADD", "register:40f0:8", ["const:43c294:8", "const:4:8"]]
+ 0043c294 ["CALL", null, ["callee:0043bb58:8"]]
- 0043bf74 bytes 31feff97
+ 0043c294 bytes 31feff97
- 0043c04c ["INT_ADD", "register:40f0:8", ["const:43c04c:8", "const:4:8"]]
- 0043c04c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043c36c ["INT_ADD", "register:40f0:8", ["const:43c36c:8", "const:4:8"]]
+ 0043c36c ["CALL", null, ["callee:00c58ed0:8"]]
- 0043c04c bytes ad6f2094
+ 0043c36c bytes d9722094
- 0043c064 ["INT_ADD", "register:40f0:8", ["const:43c064:8", "const:4:8"]]
- 0043c064 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043c384 ["INT_ADD", "register:40f0:8", ["const:43c384:8", "const:4:8"]]
+ 0043c384 ["CALL", null, ["callee:00c58ed0:8"]]
- 0043c064 bytes a76f2094
+ 0043c384 bytes d3722094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1b2a573cbf20c5773db761ec95cd87"></a>

### [`0043c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c1c0.md) → [`0043c4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c4e0.md) _INIT_5

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043c21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c21c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c53c.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.57% / 新版 69.57%

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
      "definition_site": "0043c4fc",
      "incomplete_value": false,
      "site": "0043c500",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c1dc",
      "incomplete_value": false,
      "site": "0043c1e0",
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
            "const:a70:8"
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
      "definition_site": "0043c50c",
      "incomplete_value": false,
      "site": "0043c520",
      "value": [
        "leaf",
        "const:43c53c:8"
      ]
    },
    "old": {
      "definition_site": "0043c1ec",
      "incomplete_value": false,
      "site": "0043c200",
      "value": [
        "leaf",
        "const:43c21c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c514",
      "incomplete_value": false,
      "site": "0043c520",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c1f4",
      "incomplete_value": false,
      "site": "0043c200",
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
      "0043c4f0",
      "READ",
      [
        "storage",
        "00ca4a70",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c4fc",
      "PARAM",
      [
        "storage",
        "00ca4a70",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c50c",
      "PARAM",
      [
        "storage",
        "0043c21c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043c4f0",
      "READ",
      [
        "storage",
        "00ca5a30",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c4fc",
      "PARAM",
      [
        "storage",
        "00ca5a30",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c50c",
      "PARAM",
      [
        "storage",
        "0043c53c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c1c0.md#insn-0043c1e0) · [`0043c200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c1c0.md#insn-0043c200) · [`0043c1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c1c0.md#insn-0043c1c8)
- 新版 [`0043c500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c4e0.md#insn-0043c500) · [`0043c520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c4e0.md#insn-0043c520) · [`0043c4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c4e0.md#insn-0043c4e8)

~~~diff
- 0043c1e0 ["INT_ADD", "register:40f0:8", ["const:43c1e0:8", "const:4:8"]]
- 0043c1e0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 0043c500 ["INT_ADD", "register:40f0:8", ["const:43c500:8", "const:4:8"]]
+ 0043c500 ["CALL", null, ["callee:00c58ef0:8"]]
- 0043c1e0 bytes 506f2094
+ 0043c500 bytes 7c722094
- 0043c200 ["INT_ADD", "register:40f0:8", ["const:43c200:8", "const:4:8"]]
- 0043c200 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043c520 ["INT_ADD", "register:40f0:8", ["const:43c520:8", "const:4:8"]]
+ 0043c520 ["CALL", null, ["callee:00c58ed0:8"]]
- 0043c200 bytes 406f2094
+ 0043c520 bytes 6c722094
- 0043c1c8 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043c4e8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043c1c8 bytes 48430090
+ 0043c4e8 bytes 484300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f7adc5dae1fef757963c7a8c1473eb1"></a>

### [`0043c23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c23c.md) → [`0043c55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c55c.md) _INIT_6

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043c21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c21c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c53c.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.57% / 新版 69.57%

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
      "definition_site": "0043c578",
      "incomplete_value": false,
      "site": "0043c57c",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c258",
      "incomplete_value": false,
      "site": "0043c25c",
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
            "const:a80:8"
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
      "definition_site": "0043c588",
      "incomplete_value": false,
      "site": "0043c59c",
      "value": [
        "leaf",
        "const:43c53c:8"
      ]
    },
    "old": {
      "definition_site": "0043c268",
      "incomplete_value": false,
      "site": "0043c27c",
      "value": [
        "leaf",
        "const:43c21c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c590",
      "incomplete_value": false,
      "site": "0043c59c",
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
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c270",
      "incomplete_value": false,
      "site": "0043c27c",
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
      "0043c56c",
      "READ",
      [
        "storage",
        "00ca4a80",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c578",
      "PARAM",
      [
        "storage",
        "00ca4a80",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c588",
      "PARAM",
      [
        "storage",
        "0043c21c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043c56c",
      "READ",
      [
        "storage",
        "00ca5a40",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c578",
      "PARAM",
      [
        "storage",
        "00ca5a40",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c588",
      "PARAM",
      [
        "storage",
        "0043c53c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c23c.md#insn-0043c25c) · [`0043c27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c23c.md#insn-0043c27c) · [`0043c244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c23c.md#insn-0043c244)
- 新版 [`0043c57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c55c.md#insn-0043c57c) · [`0043c59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c55c.md#insn-0043c59c) · [`0043c564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c55c.md#insn-0043c564)

~~~diff
- 0043c25c ["INT_ADD", "register:40f0:8", ["const:43c25c:8", "const:4:8"]]
- 0043c25c ["CALL", null, ["callee:00c58ef0:8"]]
+ 0043c57c ["INT_ADD", "register:40f0:8", ["const:43c57c:8", "const:4:8"]]
+ 0043c57c ["CALL", null, ["callee:00c58ef0:8"]]
- 0043c25c bytes 316f2094
+ 0043c57c bytes 5d722094
- 0043c27c ["INT_ADD", "register:40f0:8", ["const:43c27c:8", "const:4:8"]]
- 0043c27c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043c59c ["INT_ADD", "register:40f0:8", ["const:43c59c:8", "const:4:8"]]
+ 0043c59c ["CALL", null, ["callee:00c58ed0:8"]]
- 0043c27c bytes 216f2094
+ 0043c59c bytes 4d722094
- 0043c244 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0043c564 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0043c244 bytes 48430090
+ 0043c564 bytes 484300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-128ae58e1d3bd9a227823fd755a40e09"></a>

### [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) → [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) FUN_0043c5b8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00443100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443100.md) [`004433d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004433d8.md) · 呼出先 49件 [`0043d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d5f4.md) [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0043e5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md)
- 新版 呼出元 2件 [`00443420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443420.md) [`004436f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436f8.md) · 呼出先 49件 [`0043d914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043d914.md) [`0043dadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md) [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) [`0043e8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e8d8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.32% / 新版 95.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 2件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c740",
      "incomplete_value": true,
      "site": "0043c740",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c420",
      "incomplete_value": true,
      "site": "0043c420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c824",
      "incomplete_value": false,
      "site": "0043c824",
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
                "const:c66000:8"
              ],
              [
                "leaf",
                "const:5d0:8"
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
      "definition_site": "0043c504",
      "incomplete_value": false,
      "site": "0043c504",
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
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:600:8"
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c960",
      "incomplete_value": true,
      "site": "0043c960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c640",
      "incomplete_value": true,
      "site": "0043c640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6cf:8"
              ]
            ]
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
      "0043c64c",
      "PARAM",
      [
        "storage",
        "002c0f22",
        null,
        "string"
      ]
    ],
    [
      "0043c684",
      "PARAM",
      [
        "storage",
        "002b9edc",
        null,
        null
      ]
    ],
    [
      "0043c730",
      "READ",
      [
        "storage",
        "002a7580",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043c64c",
      "PARAM",
      [
        "storage",
        "002c0f6c",
        null,
        "string"
      ]
    ],
    [
      "0043c684",
      "PARAM",
      [
        "storage",
        "002b9fba",
        null,
        null
      ]
    ],
    [
      "0043c730",
      "READ",
      [
        "storage",
        "002a76d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md#insn-0043c338) · [`0043c36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md#insn-0043c36c) · [`0043c68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md#insn-0043c68c)
- 新版 [`0043c658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md#insn-0043c658) · [`0043c68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md#insn-0043c68c) · [`0043c9ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md#insn-0043c9ac)

~~~diff
- 0043c338 ["INT_ADD", "register:40f0:8", ["const:43c338:8", "const:4:8"]]
- 0043c338 ["CALL", null, ["callee:00c59000:8"]]
+ 0043c658 ["INT_ADD", "register:40f0:8", ["const:43c658:8", "const:4:8"]]
+ 0043c658 ["CALL", null, ["callee:00c59000:8"]]
- 0043c338 bytes 3e6f2094
+ 0043c658 bytes 6a722094
- 0043c36c ["INT_ADD", "register:40f0:8", ["const:43c36c:8", "const:4:8"]]
- 0043c36c ["CALL", null, ["callee:00c59010:8"]]
+ 0043c68c ["INT_ADD", "register:40f0:8", ["const:43c68c:8", "const:4:8"]]
+ 0043c68c ["CALL", null, ["callee:00c59010:8"]]
- 0043c36c bytes 356f2094
+ 0043c68c bytes 61722094
- 0043c68c ["INT_ADD", "register:40f0:8", ["const:43c68c:8", "const:4:8"]]
- 0043c68c ["CALL", null, ["callee:00c54d60:8"]]
+ 0043c9ac ["INT_ADD", "register:40f0:8", ["const:43c9ac:8", "const:4:8"]]
+ 0043c9ac ["CALL", null, ["callee:00c54d60:8"]]
- 0043c68c bytes b95d2094
+ 0043c9ac bytes ed602094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a017cc42129b63fe0bb10a9e0b2c6a9"></a>

### [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) → [`0043dadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md) FUN_0043dadc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) · 呼出先 13件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c8c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488094.md) [`004881b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004881b8.md)
- 新版 呼出元 2件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) · 呼出先 13件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00440fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440fac.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004883b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004883b4.md) [`004884d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004884d8.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.81% / 新版 95.81%

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
      "definition_site": "0043dd78",
      "incomplete_value": true,
      "site": "0043dd7c",
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
      "definition_site": "0043da58",
      "incomplete_value": true,
      "site": "0043da5c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0043dd74",
      "incomplete_value": true,
      "site": "0043dd80",
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
      "definition_site": "0043da54",
      "incomplete_value": true,
      "site": "0043da60",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043dd8c",
      "incomplete_value": true,
      "site": "0043dd8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
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
      "definition_site": "0043da6c",
      "incomplete_value": true,
      "site": "0043da6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
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
    "ordinal": 37,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043dd68",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "0043dd6c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0043dd74",
      "READ",
      [
        "storage",
        "00c932d0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0043dd68",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ],
    [
      "0043dd6c",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "0043dd74",
      "READ",
      [
        "storage",
        "00c942a0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md#insn-0043d7ec) · [`0043d7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md#insn-0043d7f8) · [`0043d824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md#insn-0043d824)
- 新版 [`0043db0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md#insn-0043db0c) · [`0043db18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md#insn-0043db18) · [`0043db44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md#insn-0043db44)

~~~diff
- 0043d7ec ["INT_ADD", "register:40f0:8", ["const:43d7ec:8", "const:4:8"]]
- 0043d7ec ["CALL", null, ["callee:00488180:8"]]
+ 0043db0c ["INT_ADD", "register:40f0:8", ["const:43db0c:8", "const:4:8"]]
+ 0043db0c ["CALL", null, ["callee:00488180:8"]]
- 0043d7ec bytes 9d290194
+ 0043db0c bytes 9d290194
- 0043d7f8 ["INT_ADD", "register:40f0:8", ["const:43d7f8:8", "const:4:8"]]
- 0043d7f8 ["CALL", null, ["callee:004883b4:8"]]
+ 0043db18 ["INT_ADD", "register:40f0:8", ["const:43db18:8", "const:4:8"]]
+ 0043db18 ["CALL", null, ["callee:004883b4:8"]]
- 0043d7f8 bytes 272a0194
+ 0043db18 bytes 272a0194
- 0043d824 ["INT_ADD", "register:40f0:8", ["const:43d824:8", "const:4:8"]]
- 0043d824 ["CALL", null, ["callee:004884d8:8"]]
+ 0043db44 ["INT_ADD", "register:40f0:8", ["const:43db44:8", "const:4:8"]]
+ 0043db44 ["CALL", null, ["callee:004884d8:8"]]
- 0043d824 bytes 652a0194
+ 0043db44 bytes 652a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb8c1084f31694951c27da03b451072"></a>

### [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) → [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) FUN_0043df04

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 39件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`004446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 39件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) [`0043fc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md) [`004449e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043e0b4",
      "incomplete_value": false,
      "site": "0043e0bc",
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
            "const:3c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043dd94",
      "incomplete_value": false,
      "site": "0043dd9c",
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
            "const:2f6:8"
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
      "0043e0b4",
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043e0b4",
      "PARAM",
      [
        "storage",
        "002a53c1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043dd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md#insn-0043dd9c) · [`0043dc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md#insn-0043dc7c) · [`0043dccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md#insn-0043dccc)
- 新版 [`0043e0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md#insn-0043e0bc) · [`0043df9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md#insn-0043df9c) · [`0043dfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md#insn-0043dfec)

~~~diff
- 0043dd9c ["INT_ADD", "register:40f0:8", ["const:43dd9c:8", "const:4:8"]]
- 0043dd9c ["CALL", null, ["callee:00c59010:8"]]
+ 0043e0bc ["INT_ADD", "register:40f0:8", ["const:43e0bc:8", "const:4:8"]]
+ 0043e0bc ["CALL", null, ["callee:00c59010:8"]]
- 0043dd9c bytes a9682094
+ 0043e0bc bytes d56b2094
- 0043dc7c ["INT_ADD", "register:40f0:8", ["const:43dc7c:8", "const:4:8"]]
- 0043dc7c ["CALL", null, ["callee:0043be80:8"]]
+ 0043df9c ["INT_ADD", "register:40f0:8", ["const:43df9c:8", "const:4:8"]]
+ 0043df9c ["CALL", null, ["callee:0043be80:8"]]
- 0043dc7c bytes b9f7ff97
+ 0043df9c bytes b9f7ff97
- 0043dccc ["INT_ADD", "register:40f0:8", ["const:43dccc:8", "const:4:8"]]
- 0043dccc ["CALL", null, ["callee:00c59070:8"]]
+ 0043dfec ["INT_ADD", "register:40f0:8", ["const:43dfec:8", "const:4:8"]]
+ 0043dfec ["CALL", null, ["callee:00c59070:8"]]
- 0043dccc bytes f5682094
+ 0043dfec bytes 216c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2626d24089e05fa4ad9a2b55ab4954f"></a>

### [`0043deb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043deb8.md) → [`0043e1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e1d8.md) FUN_0043e1d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00482e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/00482e6c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e1f4",
      "incomplete_value": true,
      "site": "0043e1f8",
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
      "definition_site": "0043ded4",
      "incomplete_value": true,
      "site": "0043ded8",
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
      "0043e1ec",
      "READ",
      [
        "storage",
        "00c9ac78",
        null,
        "pointer"
      ]
    ],
    [
      "0043e1f8",
      "DATA",
      [
        "storage",
        "00c65610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043e1ec",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "0043e1f8",
      "DATA",
      [
        "storage",
        "00c665e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043deb8.md#insn-0043dec4) · [`0043decc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043deb8.md#insn-0043decc) · [`0043dee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043deb8.md#insn-0043dee8)
- 新版 [`0043e1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e1d8.md#insn-0043e1e4) · [`0043e1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e1d8.md#insn-0043e1ec) · [`0043e208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e1d8.md#insn-0043e208)

~~~diff
- 0043dec4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0043e1e4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0043dec4 bytes e84200b0
+ 0043e1e4 bytes e84200b0
- 0043decc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c78:8"]]
- 0043decc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043e1ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
+ 0043e1ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043decc bytes 083d46f9
+ 0043e1ec bytes 082546f9
- 0043dee8 ["INT_ADD", "register:40f0:8", ["const:43dee8:8", "const:4:8"]]
- 0043dee8 ["CALL", null, ["callee:00c54d90:8"]]
+ 0043e208 ["INT_ADD", "register:40f0:8", ["const:43e208:8", "const:4:8"]]
+ 0043e208 ["CALL", null, ["callee:00c54d90:8"]]
- 0043dee8 bytes ae572094
+ 0043e208 bytes e25a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad32b2cdb6d4eb29da4d219623bb63c8"></a>

### [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) → [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) FUN_0043e310

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) · 呼出先 20件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`004431f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431f4.md) [`004431f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431f8.md) [`00443284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443284.md) [`00443288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443288.md)
- 新版 呼出元 2件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) · 呼出先 20件 [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00443514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443514.md) [`00443518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443518.md) [`004435a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004435a4.md) [`004435a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004435a8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.31% / 新版 96.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e504",
      "incomplete_value": false,
      "site": "0043e504",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e1e4",
      "incomplete_value": false,
      "site": "0043e1e4",
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
            "const:308:8"
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
      "definition_site": "0043e528",
      "incomplete_value": false,
      "site": "0043e528",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e208",
      "incomplete_value": false,
      "site": "0043e208",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e53c",
      "incomplete_value": false,
      "site": "0043e53c",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e21c",
      "incomplete_value": false,
      "site": "0043e21c",
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
            "const:408:8"
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
      "0043e360",
      "PARAM",
      [
        "storage",
        "002a52f8",
        null,
        "undefined4"
      ]
    ],
    [
      "0043e390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ],
    [
      "0043e468",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043e360",
      "PARAM",
      [
        "storage",
        "002a53c3",
        null,
        "undefined4"
      ]
    ],
    [
      "0043e390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00765314"
      ]
    ],
    [
      "0043e468",
      "READ",
      [
        "storage",
        "00c9bc68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043e048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md#insn-0043e048) · [`0043e070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md#insn-0043e070) · [`0043e150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md#insn-0043e150)
- 新版 [`0043e368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md#insn-0043e368) · [`0043e390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md#insn-0043e390) · [`0043e470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md#insn-0043e470)

~~~diff
- 0043e048 ["INT_ADD", "register:40f0:8", ["const:43e048:8", "const:4:8"]]
- 0043e048 ["CALL", null, ["callee:00c59010:8"]]
+ 0043e368 ["INT_ADD", "register:40f0:8", ["const:43e368:8", "const:4:8"]]
+ 0043e368 ["CALL", null, ["callee:00c59010:8"]]
- 0043e048 bytes fe672094
+ 0043e368 bytes 2a6b2094
- 0043e070 ["INT_ADD", "register:40f0:8", ["const:43e070:8", "const:4:8"]]
- 0043e070 ["CALL", null, ["ram:764f38:8"]]
+ 0043e390 ["INT_ADD", "register:40f0:8", ["const:43e390:8", "const:4:8"]]
+ 0043e390 ["CALL", null, ["ram:765314:8"]]
- 0043e070 bytes b29b0c94
+ 0043e390 bytes e19b0c94
- 0043e150 ["INT_ADD", "register:40f0:8", ["const:43e150:8", "const:4:8"]]
- 0043e150 ["CALL", null, ["callee:00562094:8"]]
+ 0043e470 ["INT_ADD", "register:40f0:8", ["const:43e470:8", "const:4:8"]]
+ 0043e470 ["CALL", null, ["callee:00562094:8"]]
- 0043e150 bytes 098f0494
+ 0043e470 bytes 098f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf04ae57e920e2cc60c5fc7d03a68f07"></a>

### [`0043e5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md) → [`0043e8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e8d8.md) FUN_0043e8d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) · 呼出先 11件 [`00442f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f24.md) [`00442f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f28.md) [`00442fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442fb0.md) [`00442fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442fb4.md) [`004430f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430f8.md)
- 新版 呼出元 1件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) · 呼出先 11件 [`00443244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443244.md) [`00443248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443248.md) [`004432d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004432d0.md) [`004432d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004432d4.md) [`00443418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443418.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.40% / 新版 94.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e990",
      "incomplete_value": false,
      "site": "0043e990",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e670",
      "incomplete_value": false,
      "site": "0043e670",
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
            "const:158:8"
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
      "definition_site": "0043e9b4",
      "incomplete_value": false,
      "site": "0043e9b4",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e694",
      "incomplete_value": false,
      "site": "0043e694",
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
            "const:1e8:8"
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
      "definition_site": "0043e9c8",
      "incomplete_value": false,
      "site": "0043e9c8",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e6a8",
      "incomplete_value": false,
      "site": "0043e6a8",
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
            "const:278:8"
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
      "0043e908",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ],
    [
      "0043e908",
      "PARAM",
      [
        "storage",
        "00ca5dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043e990",
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043e908",
      "READ",
      [
        "storage",
        "00c9bc68",
        null,
        "pointer"
      ]
    ],
    [
      "0043e908",
      "PARAM",
      [
        "storage",
        "00ca6d90",
        null,
        "undefined1"
      ]
    ],
    [
      "0043e990",
      "DATA",
      [
        "storage",
        "00c64128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043e5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md#insn-0043e5ec) · [`0043e5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md#insn-0043e5d4) · [`0043e5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md#insn-0043e5e8)
- 新版 [`0043e90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e8d8.md#insn-0043e90c) · [`0043e8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e8d8.md#insn-0043e8f4) · [`0043e908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e8d8.md#insn-0043e908)

~~~diff
- 0043e5ec ["INT_ADD", "register:40f0:8", ["const:43e5ec:8", "const:4:8"]]
- 0043e5ec ["CALL", null, ["callee:00562094:8"]]
+ 0043e90c ["INT_ADD", "register:40f0:8", ["const:43e90c:8", "const:4:8"]]
+ 0043e90c ["CALL", null, ["callee:00562094:8"]]
- 0043e5ec bytes e28d0494
+ 0043e90c bytes e28d0494
- 0043e5d4 ["COPY", "register:4000:8", ["const:c9a000:8"]]
+ 0043e8f4 ["COPY", "register:4000:8", ["const:c9b000:8"]]
- 0043e5d4 bytes e0420090
+ 0043e8f4 bytes e04200b0
- 0043e5e8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c98:8"]]
- 0043e5e8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043e908 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c68:8"]]
+ 0043e908 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043e5e8 bytes 004c46f9
+ 0043e908 bytes 003446f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e70a0877474a12021408fe6abbf0d0e"></a>

### [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) → [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) FUN_0043ecac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 38件 [`0062a204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062a/0062a204.md) [`00677a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00677/00677a80.md) [`0067e838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e838.md) [`006b3864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3864.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 5件 [`0043ea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ea1c.md) [`0043eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eaa0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 38件 [`0062a5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062a/0062a5b4.md) [`00677e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00677/00677e30.md) [`0067ebe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067ebe8.md) [`006b3c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3c14.md) [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 5件 [`0043ed3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ed3c.md) [`0043edc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043edc0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043ece0",
      "incomplete_value": false,
      "site": "0043ece4",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e9c0",
      "incomplete_value": false,
      "site": "0043e9c4",
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
            "const:ae0:8"
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
      "definition_site": "0043ecf0",
      "incomplete_value": false,
      "site": "0043ecf4",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043e9d0",
      "incomplete_value": false,
      "site": "0043e9d4",
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
            "const:a88:8"
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
      "definition_site": "0043ecfc",
      "incomplete_value": false,
      "site": "0043ed10",
      "value": [
        "leaf",
        "const:43ed3c:8"
      ]
    },
    "old": {
      "definition_site": "0043e9dc",
      "incomplete_value": false,
      "site": "0043e9f0",
      "value": [
        "leaf",
        "const:43ea1c:8"
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
      "0043ecc0",
      "READ",
      [
        "storage",
        "00ca4ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043eccc",
      "DATA",
      [
        "storage",
        "00ca4a88",
        null,
        null
      ]
    ],
    [
      "0043ece0",
      "PARAM",
      [
        "storage",
        "00ca4ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0043ecc0",
      "READ",
      [
        "storage",
        "00ca5aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043eccc",
      "DATA",
      [
        "storage",
        "00ca5a48",
        null,
        null
      ]
    ],
    [
      "0043ece0",
      "PARAM",
      [
        "storage",
        "00ca5aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043e9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md#insn-0043e9c4) · [`0043e9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md#insn-0043e9d4) · [`0043e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md#insn-0043e9f0)
- 新版 [`0043ece4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md#insn-0043ece4) · [`0043ecf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md#insn-0043ecf4) · [`0043ed10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md#insn-0043ed10)

~~~diff
- 0043e9c4 ["INT_ADD", "register:40f0:8", ["const:43e9c4:8", "const:4:8"]]
- 0043e9c4 ["CALL", null, ["callee:00c58ef0:8"]]
+ 0043ece4 ["INT_ADD", "register:40f0:8", ["const:43ece4:8", "const:4:8"]]
+ 0043ece4 ["CALL", null, ["callee:00c58ef0:8"]]
- 0043e9c4 bytes 57652094
+ 0043ece4 bytes 83682094
- 0043e9d4 ["INT_ADD", "register:40f0:8", ["const:43e9d4:8", "const:4:8"]]
- 0043e9d4 ["CALL", null, ["callee:0043edc0:8"]]
+ 0043ecf4 ["INT_ADD", "register:40f0:8", ["const:43ecf4:8", "const:4:8"]]
+ 0043ecf4 ["CALL", null, ["callee:0043edc0:8"]]
- 0043e9d4 bytes 33000094
+ 0043ecf4 bytes 33000094
- 0043e9f0 ["INT_ADD", "register:40f0:8", ["const:43e9f0:8", "const:4:8"]]
- 0043e9f0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0043ed10 ["INT_ADD", "register:40f0:8", ["const:43ed10:8", "const:4:8"]]
+ 0043ed10 ["CALL", null, ["callee:00c58ed0:8"]]
- 0043e9f0 bytes 44652094
+ 0043ed10 bytes 70682094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1c9497c06e38c4a6b5e628de435f6d"></a>

### [`0043eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eaa0.md) → [`0043edc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043edc0.md) FUN_0043edc0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`004434c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434c0.md) · 呼出先 4件 [`00b33b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b33/00b33b74.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`004437e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437e0.md) · 呼出先 4件 [`00b34b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b34/00b34b68.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043ee2c",
      "incomplete_value": true,
      "site": "0043ee38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0043eb0c",
      "incomplete_value": true,
      "site": "0043eb18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c0:8"
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
      "definition_site": "0043ee28",
      "incomplete_value": true,
      "site": "0043ee3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043eb08",
      "incomplete_value": true,
      "site": "0043eb1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:610:8"
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
      "definition_site": "0043ee28",
      "incomplete_value": true,
      "site": "0043ee3c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0043eb08",
      "incomplete_value": true,
      "site": "0043eb1c",
      "value": [
        "LOAD",
        "16",
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
      "0043ee28",
      "READ",
      [
        "storage",
        "002ae610",
        null,
        "string"
      ]
    ],
    [
      "0043ee28",
      "READ",
      [
        "storage",
        "002ae620",
        null,
        "string"
      ]
    ],
    [
      "0043ee2c",
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
      "0043ee28",
      "READ",
      [
        "storage",
        "002ae6dd",
        null,
        "string"
      ]
    ],
    [
      "0043ee28",
      "READ",
      [
        "storage",
        "002ae6ed",
        null,
        "string"
      ]
    ],
    [
      "0043ee2c",
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

- 旧版 [`0043eaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eaa0.md#insn-0043eaf8) · [`0043eb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eaa0.md#insn-0043eb00) · [`0043eb04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eaa0.md#insn-0043eb04)
- 新版 [`0043ee18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043edc0.md#insn-0043ee18) · [`0043ee20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043edc0.md#insn-0043ee20)

~~~diff
- 0043eaf8 ["INT_ADD", "register:40f0:8", ["const:43eaf8:8", "const:4:8"]]
- 0043eaf8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0043ee18 ["INT_ADD", "register:40f0:8", ["const:43ee18:8", "const:4:8"]]
+ 0043ee18 ["CALL", null, ["callee:00c58f30:8"]]
- 0043eaf8 bytes 1a652094
+ 0043ee18 bytes 46682094
- 0043eb00 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0043eb00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043eb00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043eb00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ee20 ["COPY", "tmp:0:8", ["const:6dd:8"]]
+ 0043ee20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ee20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ee20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043eb00 bytes 08411891
+ 0043ee20 bytes 08751b91
- 0043eb04 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0043eb04 bytes 29f4ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9182f7075033a569c804a3e5377f4ae"></a>

### [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) → [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) FUN_0043efc0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00853360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853360.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`0088238c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088238c.md) · 呼出先 24件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0044b8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b8d8.md) [`00481470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481470.md)
- 新版 呼出元 9件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`0085430c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00854/0085430c.md) [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) [`00883338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883338.md) · 呼出先 24件 [`0043dadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043dadc.md) [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) [`0044bbf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bbf8.md) [`00481790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481790.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.04% / 新版 97.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f26c",
      "incomplete_value": true,
      "site": "0043f274",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ef4c",
      "incomplete_value": true,
      "site": "0043ef54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043f4d4",
      "incomplete_value": false,
      "site": "0043f4dc",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f1b4",
      "incomplete_value": false,
      "site": "0043f1bc",
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
            "const:589:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043f108",
      "READ",
      [
        "storage",
        "00c9ac78",
        null,
        "pointer"
      ]
    ],
    [
      "0043f144",
      "PARAM",
      [
        "storage",
        "002c0f22",
        null,
        "string"
      ]
    ],
    [
      "0043f174",
      "PARAM",
      [
        "storage",
        "002b9edc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043f108",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "0043f144",
      "PARAM",
      [
        "storage",
        "002c0f6c",
        null,
        "string"
      ]
    ],
    [
      "0043f174",
      "PARAM",
      [
        "storage",
        "002b9fba",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md#insn-0043f1bc) · [`0043ecdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md#insn-0043ecdc) · [`0043ecf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md#insn-0043ecf0)
- 新版 [`0043f4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md#insn-0043f4dc) · [`0043effc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md#insn-0043effc) · [`0043f010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md#insn-0043f010)

~~~diff
- 0043f1bc ["INT_ADD", "register:40f0:8", ["const:43f1bc:8", "const:4:8"]]
- 0043f1bc ["CALL", null, ["callee:00c59010:8"]]
+ 0043f4dc ["INT_ADD", "register:40f0:8", ["const:43f4dc:8", "const:4:8"]]
+ 0043f4dc ["CALL", null, ["callee:00c59010:8"]]
- 0043f1bc bytes a1632094
+ 0043f4dc bytes cd662094
- 0043ecdc ["INT_ADD", "register:40f0:8", ["const:43ecdc:8", "const:4:8"]]
- 0043ecdc ["CALL", null, ["callee:0048d1b0:8"]]
+ 0043effc ["INT_ADD", "register:40f0:8", ["const:43effc:8", "const:4:8"]]
+ 0043effc ["CALL", null, ["callee:0048d1b0:8"]]
- 0043ecdc bytes 6d380194
+ 0043effc bytes 6d380194
- 0043ecf0 ["INT_ADD", "register:40f0:8", ["const:43ecf0:8", "const:4:8"]]
- 0043ecf0 ["CALL", null, ["callee:0059821c:8"]]
+ 0043f010 ["INT_ADD", "register:40f0:8", ["const:43f010:8", "const:4:8"]]
+ 0043f010 ["CALL", null, ["callee:0059821c:8"]]
- 0043ecf0 bytes 83640594
+ 0043f010 bytes 83640594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0922c70d81f12b1459be812a5025f0b9"></a>

### [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) → [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md) FUN_0043f798

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 25件 [`0062a204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062a/0062a204.md) [`00677a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00677/00677a80.md) [`0067e838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e838.md) [`006b3864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3864.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 4件 [`00443718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443718.md) [`0044371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044371c.md) [`00b33e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b33/00b33e14.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 25件 [`0062a5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062a/0062a5b4.md) [`00677e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00677/00677e30.md) [`0067ebe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067ebe8.md) [`006b3c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3c14.md) [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 4件 [`00443a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a38.md) [`00443a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a3c.md) [`00b34e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b34/00b34e08.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "definition_site": "0043f7c4",
      "incomplete_value": false,
      "site": "0043f7cc",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f4a4",
      "incomplete_value": false,
      "site": "0043f4ac",
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
            "const:5a8:8"
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
      "0043f7cc",
      "DATA",
      [
        "storage",
        "00c635a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f800",
      "READ",
      [
        "storage",
        "00c635c8",
        null,
        "pointer"
      ]
    ],
    [
      "0043f800",
      "READ",
      [
        "storage",
        "00c635d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f7cc",
      "DATA",
      [
        "storage",
        "00c64578",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f800",
      "READ",
      [
        "storage",
        "00c64598",
        null,
        "pointer"
      ]
    ],
    [
      "0043f800",
      "READ",
      [
        "storage",
        "00c645a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md#insn-0043f4a0) · [`0043f4a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md#insn-0043f4a4) · [`0043f4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md#insn-0043f4b8)
- 新版 [`0043f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md#insn-0043f7c0) · [`0043f7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md#insn-0043f7c4) · [`0043f7d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md#insn-0043f7d8)

~~~diff
- 0043f4a0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0043f7c0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0043f4a0 bytes 28410090
+ 0043f7c0 bytes 284100b0
- 0043f4a4 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 0043f4a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f4a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f4a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f7c4 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 0043f7c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f7c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f7c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f4a4 bytes 08a11691
+ 0043f7c4 bytes 08e11591
- 0043f4b8 ["INT_ADD", "register:40f0:8", ["const:43f4b8:8", "const:4:8"]]
- 0043f4b8 ["CALL", null, ["callee:00b34e08:8"]]
+ 0043f7d8 ["INT_ADD", "register:40f0:8", ["const:43f7d8:8", "const:4:8"]]
+ 0043f7d8 ["CALL", null, ["callee:00b34e08:8"]]
- 0043f4b8 bytes 57d21b94
+ 0043f7d8 bytes 8cd51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5706831c67ea4e22d63d8c8dfba250"></a>

### [`0043f574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f574.md) → [`0043f894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f894.md) FUN_0043f894

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2c4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md) · 呼出先 4件 [`00443718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443718.md) [`0044371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044371c.md) [`00b33e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b33/00b33e14.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00b2d4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2d/00b2d4b4.md) · 呼出先 4件 [`00443a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a38.md) [`00443a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a3c.md) [`00b34e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b34/00b34e08.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f8b4",
      "incomplete_value": false,
      "site": "0043f8c4",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f594",
      "incomplete_value": false,
      "site": "0043f5a4",
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
            "const:5a8:8"
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
      "0043f8c4",
      "DATA",
      [
        "storage",
        "00c635a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f8f8",
      "READ",
      [
        "storage",
        "00c635c8",
        null,
        "pointer"
      ]
    ],
    [
      "0043f8f8",
      "READ",
      [
        "storage",
        "00c635d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f8c4",
      "DATA",
      [
        "storage",
        "00c64578",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f8f8",
      "READ",
      [
        "storage",
        "00c64598",
        null,
        "pointer"
      ]
    ],
    [
      "0043f8f8",
      "READ",
      [
        "storage",
        "00c645a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f574.md#insn-0043f590) · [`0043f594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f574.md#insn-0043f594) · [`0043f5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f574.md#insn-0043f5b0)
- 新版 [`0043f8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f894.md#insn-0043f8b0) · [`0043f8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f894.md#insn-0043f8b4) · [`0043f8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f894.md#insn-0043f8d0)

~~~diff
- 0043f590 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0043f8b0 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0043f590 bytes 29410090
+ 0043f8b0 bytes 294100b0
- 0043f594 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 0043f594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f8b4 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 0043f8b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f8b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f8b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f594 bytes 29a11691
+ 0043f8b4 bytes 29e11591
- 0043f5b0 ["INT_ADD", "register:40f0:8", ["const:43f5b0:8", "const:4:8"]]
- 0043f5b0 ["CALL", null, ["callee:00b34e08:8"]]
+ 0043f8d0 ["INT_ADD", "register:40f0:8", ["const:43f8d0:8", "const:4:8"]]
+ 0043f8d0 ["CALL", null, ["callee:00b34e08:8"]]
- 0043f5b0 bytes 19d21b94
+ 0043f8d0 bytes 4ed51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5568d441daea09b14dbbb359dd3363"></a>

### [`0043f658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f658.md) → [`0043f978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f978.md) FUN_0043f978

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f46c.md) · 呼出先 6件 [`004434b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434b8.md) [`004434bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434bc.md) [`00443698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443698.md) [`0044369c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044369c.md) [`00b33b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b33/00b33b78.md)
- 新版 呼出元 1件 [`0043f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f78c.md) · 呼出先 6件 [`004437d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437d8.md) [`004437dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437dc.md) [`004439b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439b8.md) [`004439bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439bc.md) [`00b34b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b34/00b34b6c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f998",
      "incomplete_value": false,
      "site": "0043f9bc",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f678",
      "incomplete_value": false,
      "site": "0043f69c",
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
            "const:488:8"
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
      "definition_site": "0043f9b4",
      "incomplete_value": false,
      "site": "0043f9c0",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f694",
      "incomplete_value": false,
      "site": "0043f6a0",
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
            "const:518:8"
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
      "definition_site": "0043f9cc",
      "incomplete_value": false,
      "site": "0043f9e0",
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
            "const:6dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f6ac",
      "incomplete_value": false,
      "site": "0043f6c0",
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
            "const:610:8"
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
      "0043f9bc",
      "DATA",
      [
        "storage",
        "00c63488",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f9c0",
      "DATA",
      [
        "storage",
        "00c63518",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f9cc",
      "PARAM",
      [
        "storage",
        "002ae610",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043f9bc",
      "DATA",
      [
        "storage",
        "00c64458",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f9c0",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f9cc",
      "PARAM",
      [
        "storage",
        "002ae6dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f658.md#insn-0043f6c0) · [`0043f674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f658.md#insn-0043f674) · [`0043f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f658.md#insn-0043f678)
- 新版 [`0043f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f978.md#insn-0043f9e0) · [`0043f994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f978.md#insn-0043f994) · [`0043f998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f978.md#insn-0043f998)

~~~diff
- 0043f6c0 ["INT_ADD", "register:40f0:8", ["const:43f6c0:8", "const:4:8"]]
- 0043f6c0 ["CALL", null, ["callee:00b34b6c:8"]]
+ 0043f9e0 ["INT_ADD", "register:40f0:8", ["const:43f9e0:8", "const:4:8"]]
+ 0043f9e0 ["CALL", null, ["callee:00b34b6c:8"]]
- 0043f6c0 bytes 2ed11b94
+ 0043f9e0 bytes 63d41b94
- 0043f674 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0043f994 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0043f674 bytes 29410090
+ 0043f994 bytes 294100b0
- 0043f678 ["COPY", "tmp:0:8", ["const:488:8"]]
- 0043f678 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f678 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f678 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f998 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0043f998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f678 bytes 29211291
+ 0043f998 bytes 29611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44ea2cf8081210090dd8660989bd9e74"></a>

### [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) → [`0043fc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md) FUN_0043fc7c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a89b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a89/00a89b40.md) [`00b11d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11d1c.md) · 呼出先 23件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00443758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443758.md) [`00481470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481470.md)
- 新版 呼出元 2件 [`00a8ab34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8a/00a8ab34.md) [`00b12d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b12d10.md) · 呼出先 23件 [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00443a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a78.md) [`00481790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481790.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fe00",
      "incomplete_value": true,
      "site": "0043fe00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fae0",
      "incomplete_value": true,
      "site": "0043fae0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00440154",
      "incomplete_value": true,
      "site": "00440160",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
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
    "old": {
      "definition_site": "0043fe34",
      "incomplete_value": true,
      "site": "0043fe40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
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
    "ordinal": 71,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00440268",
      "incomplete_value": true,
      "site": "00440274",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ff48",
      "incomplete_value": true,
      "site": "0043ff54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043fce8",
      "PARAM",
      [
        "storage",
        "002b9edc",
        null,
        null
      ]
    ],
    [
      "0043fdf0",
      "READ",
      [
        "storage",
        "002a7580",
        null,
        "string"
      ]
    ],
    [
      "0043ff34",
      "READ",
      [
        "storage",
        "002a3ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043fce8",
      "PARAM",
      [
        "storage",
        "002b9fba",
        null,
        null
      ]
    ],
    [
      "0043fdf0",
      "READ",
      [
        "storage",
        "002a76d8",
        null,
        "string"
      ]
    ],
    [
      "0043ff34",
      "READ",
      [
        "storage",
        "002a3f9a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md#insn-0043f9d0) · [`0043fb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md#insn-0043fb20) · [`0043fc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md#insn-0043fc34)
- 新版 [`0043fcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md#insn-0043fcf0) · [`0043fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md#insn-0043fe40) · [`0043ff54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md#insn-0043ff54)

~~~diff
- 0043f9d0 ["INT_ADD", "register:40f0:8", ["const:43f9d0:8", "const:4:8"]]
- 0043f9d0 ["CALL", null, ["callee:00c59010:8"]]
+ 0043fcf0 ["INT_ADD", "register:40f0:8", ["const:43fcf0:8", "const:4:8"]]
+ 0043fcf0 ["CALL", null, ["callee:00c59010:8"]]
- 0043f9d0 bytes 9c612094
+ 0043fcf0 bytes c8642094
- 0043fb20 ["INT_ADD", "register:40f0:8", ["const:43fb20:8", "const:4:8"]]
- 0043fb20 ["CALL", null, ["callee:00597070:8"]]
+ 0043fe40 ["INT_ADD", "register:40f0:8", ["const:43fe40:8", "const:4:8"]]
+ 0043fe40 ["CALL", null, ["callee:00597070:8"]]
- 0043fb20 bytes 8c5c0594
+ 0043fe40 bytes 8c5c0594
- 0043fc34 ["INT_ADD", "register:40f0:8", ["const:43fc34:8", "const:4:8"]]
- 0043fc34 ["CALL", null, ["callee:004413ec:8"]]
+ 0043ff54 ["INT_ADD", "register:40f0:8", ["const:43ff54:8", "const:4:8"]]
+ 0043ff54 ["CALL", null, ["callee:004413ec:8"]]
- 0043fc34 bytes 26050094
+ 0043ff54 bytes 26050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5eafc20abf1b35aa0b186aa5f146699"></a>

### [`00440bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440bbc.md) → [`00440edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440edc.md) FUN_00440edc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006b8610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8610.md) [`0080f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080f/0080f180.md) [`0081a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081a/0081a86c.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)
- 新版 呼出元 4件 [`006b89c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b8/006b89c0.md) [`008100e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00810/008100e4.md) [`0081b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0081b/0081b818.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md) [`00c59050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59050.md) [`00c59060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "definition_site": "00440f0c",
      "incomplete_value": true,
      "site": "00440f14",
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
      "definition_site": "00440bec",
      "incomplete_value": true,
      "site": "00440bf4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00440f18",
      "incomplete_value": true,
      "site": "00440f18",
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
      "definition_site": "00440bf8",
      "incomplete_value": true,
      "site": "00440bf8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00440f28",
      "incomplete_value": true,
      "site": "00440f28",
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
                "register:4000:8"
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
      "definition_site": "00440c08",
      "incomplete_value": true,
      "site": "00440c08",
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
                "register:4000:8"
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
      "00440ef8",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "00440efc",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00440f08",
      "READ",
      [
        "storage",
        "00c932d0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00440ef8",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ],
    [
      "00440efc",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00440f08",
      "READ",
      [
        "storage",
        "00c942a0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440bbc.md#insn-00440bcc) · [`00440bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440bbc.md#insn-00440bd0) · [`00440bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440bbc.md#insn-00440bd8)
- 新版 [`00440eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440edc.md#insn-00440eec) · [`00440ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440edc.md#insn-00440ef0) · [`00440ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440edc.md#insn-00440ef8)

~~~diff
- 00440bcc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00440eec ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00440bcc bytes c84200d0
+ 00440eec bytes c84200f0
- 00440bd0 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
+ 00440ef0 ["COPY", "register:40b0:8", ["const:c9b000:8"]]
- 00440bd0 bytes d64200d0
+ 00440ef0 bytes d64200f0
- 00440bd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
- 00440bd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00440ef8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 00440ef8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00440bd8 bytes 084146f9
+ 00440ef8 bytes 082946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876be07486c10886db8f60028f6d96e7"></a>

### [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) → [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) FUN_00441220

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 575件 [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00440c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c8c.md) [`0045cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cad8.md) [`0045dbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dbb8.md) [`00461b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461b78.md) · 呼出先 4件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58100.md)
- 新版 呼出元 578件 [`0043fc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md) [`00440fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440fac.md) [`0045cdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cdf8.md) [`0045ded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045ded8.md) [`00461e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461e98.md) · 呼出先 4件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c590d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00441248",
      "incomplete_value": true,
      "site": "00441250",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "00440f28",
      "incomplete_value": true,
      "site": "00440f30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
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
      "definition_site": "0044124c",
      "incomplete_value": true,
      "site": "00441250",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "old": {
      "definition_site": "00440f2c",
      "incomplete_value": true,
      "site": "00440f30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00441248",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "00441248",
      "PARAM",
      [
        "storage",
        "00c96780",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0044124c",
      "READ",
      [
        "storage",
        "00c9aca8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00441248",
      "READ",
      [
        "storage",
        "00c9bc70",
        null,
        "pointer"
      ]
    ],
    [
      "00441248",
      "PARAM",
      [
        "storage",
        "00c97750",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0044124c",
      "READ",
      [
        "storage",
        "00c9bc78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00440f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md#insn-00440f30) · [`00440f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md#insn-00440f10) · [`00440f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md#insn-00440f18)
- 新版 [`00441250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md#insn-00441250) · [`00441230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md#insn-00441230) · [`00441238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md#insn-00441238)

~~~diff
- 00440f30 ["INT_ADD", "register:40f0:8", ["const:440f30:8", "const:4:8"]]
- 00440f30 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00441250 ["INT_ADD", "register:40f0:8", ["const:441250:8", "const:4:8"]]
+ 00441250 ["CALL", null, ["callee:00c58fb0:8"]]
- 00440f30 bytes 2c5c2094
+ 00441250 bytes 585f2094
- 00440f10 ["INT_ADD", "register:40f0:8", ["const:440f10:8", "const:4:8"]]
- 00440f10 ["CALL", null, ["callee:00c58f90:8"]]
+ 00441230 ["INT_ADD", "register:40f0:8", ["const:441230:8", "const:4:8"]]
+ 00441230 ["CALL", null, ["callee:00c58f90:8"]]
- 00440f10 bytes 2c5c2094
+ 00441230 bytes 585f2094
- 00440f18 ["INT_ADD", "register:40f0:8", ["const:440f18:8", "const:4:8"]]
- 00440f18 ["CALL", null, ["callee:00c590d0:8"]]
+ 00441238 ["INT_ADD", "register:40f0:8", ["const:441238:8", "const:4:8"]]
+ 00441238 ["CALL", null, ["callee:00c590d0:8"]]
- 00440f18 bytes 7a5c2094
+ 00441238 bytes a65f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6027a44815a887d8f97182c73086f81"></a>

### [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) → [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) FUN_004412bc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 43件 [`00440c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c8c.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004858ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004858ec.md) [`004b3f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3f24.md) [`004be464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 43件 [`00440fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440fac.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`00485c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00485/00485c0c.md) [`004b4244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b4/004b4244.md) [`004be784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be784.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "004412c8",
      "incomplete_value": false,
      "site": "004412cc",
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
      "definition_site": "00440fa8",
      "incomplete_value": false,
      "site": "00440fac",
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
      "004412c8",
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
      "004412c8",
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

- 旧版 [`00440fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md#insn-00440fac) · [`00440fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md#insn-00440fa4) · [`00440fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md#insn-00440fa8)
- 新版 [`004412cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md#insn-004412cc) · [`004412c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md#insn-004412c4) · [`004412c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md#insn-004412c8)

~~~diff
- 00440fac ["INT_ADD", "register:40f0:8", ["const:440fac:8", "const:4:8"]]
- 00440fac ["CALL", null, ["callee:0043bad8:8"]]
+ 004412cc ["INT_ADD", "register:40f0:8", ["const:4412cc:8", "const:4:8"]]
+ 004412cc ["CALL", null, ["callee:0043bad8:8"]]
- 00440fac bytes 03eaff97
+ 004412cc bytes 03eaff97
- 00440fa4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 004412c4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00440fa4 bytes a0f3fff0
+ 004412c4 bytes a0f3fff0
- 00440fa8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00440fa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00440fa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00440fa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004412c8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 004412c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004412c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004412c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00440fa8 bytes 00303e91
+ 004412c8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a2e47328c0da93f126dce4c2f4f6167"></a>

### [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) → [`00441618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md) FUN_00441618

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004411d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004411d0.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`006173b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006173b0.md) [`0061af38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md)
- 新版 呼出元 4件 [`004414f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004414f0.md) [`00441618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md) [`00617760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00617/00617760.md) [`0061b2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0061b/0061b2e8.md) · 呼出先 21件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`00441618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00441788",
      "incomplete_value": false,
      "site": "00441790",
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
      "definition_site": "00441468",
      "incomplete_value": false,
      "site": "00441470",
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
      "definition_site": "00441840",
      "incomplete_value": false,
      "site": "00441848",
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
      "definition_site": "00441520",
      "incomplete_value": false,
      "site": "00441528",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044185c",
      "incomplete_value": false,
      "site": "00441868",
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
      "definition_site": "0044153c",
      "incomplete_value": false,
      "site": "00441548",
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
      "00441788",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00441840",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0044185c",
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
      "00441788",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00441840",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "0044185c",
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

- 旧版 [`00441470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md#insn-00441470) · [`00441528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md#insn-00441528) · [`0044153c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md#insn-0044153c)
- 新版 [`00441790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md#insn-00441790) · [`00441848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md#insn-00441848) · [`0044185c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md#insn-0044185c)

~~~diff
- 00441470 ["INT_ADD", "register:40f0:8", ["const:441470:8", "const:4:8"]]
- 00441470 ["CALL", null, ["callee:004421f4:8"]]
+ 00441790 ["INT_ADD", "register:40f0:8", ["const:441790:8", "const:4:8"]]
+ 00441790 ["CALL", null, ["callee:004421f4:8"]]
- 00441470 bytes 99020094
+ 00441790 bytes 99020094
- 00441528 ["INT_ADD", "register:40f0:8", ["const:441528:8", "const:4:8"]]
- 00441528 ["CALL", null, ["callee:004421f4:8"]]
+ 00441848 ["INT_ADD", "register:40f0:8", ["const:441848:8", "const:4:8"]]
+ 00441848 ["CALL", null, ["callee:004421f4:8"]]
- 00441528 bytes 6b020094
+ 00441848 bytes 6b020094
- 0044153c ["COPY", "tmp:0:8", ["const:f29:8"]]
- 0044153c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044153c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044153c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044185c ["COPY", "tmp:0:8", ["const:f73:8"]]
+ 0044185c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044185c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044185c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044153c bytes 21a43c91
+ 0044185c bytes 21cc3d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7ffd792f27ed92c78938f34639cce8"></a>

### [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) → [`00442274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md) FUN_00442274

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`0047d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d8a0.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`0073a3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a3ac.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 7件 [`00441618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md) [`00442274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md) [`0047dbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047dbc0.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md) [`0073a75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073a/0073a75c.md) · 呼出先 21件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004423dc",
      "incomplete_value": false,
      "site": "004423e4",
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
      "definition_site": "004420bc",
      "incomplete_value": false,
      "site": "004420c4",
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
      "definition_site": "00442494",
      "incomplete_value": false,
      "site": "0044249c",
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
      "definition_site": "00442174",
      "incomplete_value": false,
      "site": "0044217c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004424b0",
      "incomplete_value": false,
      "site": "004424bc",
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
      "definition_site": "00442190",
      "incomplete_value": false,
      "site": "0044219c",
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
      "004423dc",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00442494",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "004424b0",
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
      "004423dc",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00442494",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "004424b0",
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

- 旧版 [`004420c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md#insn-004420c4) · [`0044217c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md#insn-0044217c) · [`0044219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md#insn-0044219c)
- 新版 [`004423e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md#insn-004423e4) · [`0044249c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md#insn-0044249c) · [`004424bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md#insn-004424bc)

~~~diff
- 004420c4 ["INT_ADD", "register:40f0:8", ["const:4420c4:8", "const:4:8"]]
- 004420c4 ["CALL", null, ["callee:004421f4:8"]]
+ 004423e4 ["INT_ADD", "register:40f0:8", ["const:4423e4:8", "const:4:8"]]
+ 004423e4 ["CALL", null, ["callee:004421f4:8"]]
- 004420c4 bytes 84ffff97
+ 004423e4 bytes 84ffff97
- 0044217c ["INT_ADD", "register:40f0:8", ["const:44217c:8", "const:4:8"]]
- 0044217c ["CALL", null, ["callee:004421f4:8"]]
+ 0044249c ["INT_ADD", "register:40f0:8", ["const:44249c:8", "const:4:8"]]
+ 0044249c ["CALL", null, ["callee:004421f4:8"]]
- 0044217c bytes 56ffff97
+ 0044249c bytes 56ffff97
- 0044219c ["INT_ADD", "register:40f0:8", ["const:44219c:8", "const:4:8"]]
- 0044219c ["CALL", null, ["callee:00442b54:8"]]
+ 004424bc ["INT_ADD", "register:40f0:8", ["const:4424bc:8", "const:4:8"]]
+ 004424bc ["CALL", null, ["callee:00442b54:8"]]
- 0044219c bytes a6010094
+ 004424bc bytes a6010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234b82cccd335f20595f6855993b92d0"></a>

### [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) → [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) FUN_00442c7c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 129件 [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md) [`00441e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441e00.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00441f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441f54.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 129件 [`00441618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441618.md) [`00442120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442120.md) [`004421f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/004421f4.md) [`00442274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442274.md) [`00447120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "00442c88",
      "incomplete_value": false,
      "site": "00442c8c",
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
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442968",
      "incomplete_value": false,
      "site": "0044296c",
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
            "const:ecf:8"
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
      "00442c88",
      "PARAM",
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
      "00442c88",
      "PARAM",
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

- 旧版 [`0044296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md#insn-0044296c) · [`00442968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md#insn-00442968)
- 新版 [`00442c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md#insn-00442c8c) · [`00442c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md#insn-00442c88)

~~~diff
- 0044296c ["INT_ADD", "register:40f0:8", ["const:44296c:8", "const:4:8"]]
- 0044296c ["CALL", null, ["callee:00442c90:8"]]
+ 00442c8c ["INT_ADD", "register:40f0:8", ["const:442c8c:8", "const:4:8"]]
+ 00442c8c ["CALL", null, ["callee:00442c90:8"]]
- 0044296c bytes 01000094
+ 00442c8c bytes 01000094
- 00442968 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00442968 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00442968 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00442968 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00442c88 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 00442c88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00442c88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00442c88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00442968 bytes 003c3b91
+ 00442c88 bytes 00b43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f93f15352fa095a5b92bee3b0ccf13"></a>

### [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) → [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) FUN_00442c90

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 225件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00486db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486db8.md) [`0049f430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f430.md) [`0049f444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f444.md) [`0049f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f458.md) · 呼出先 4件 [`004429c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/004429c0.md) [`00c37d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 225件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`004870d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/004870d8.md) [`0049f750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f750.md) [`0049f764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f764.md) [`0049f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f778.md) · 呼出先 4件 [`00442ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442ce0.md) [`00c38d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00442cc0",
      "incomplete_value": true,
      "site": "00442cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "definition_site": "004429a0",
      "incomplete_value": true,
      "site": "004429a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb0:8"
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
      "definition_site": "00442cc4",
      "incomplete_value": true,
      "site": "00442cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "old": {
      "definition_site": "004429a4",
      "incomplete_value": true,
      "site": "004429a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00442cc0",
      "READ",
      [
        "storage",
        "00c9acb0",
        null,
        "pointer"
      ]
    ],
    [
      "00442cc0",
      "PARAM",
      [
        "storage",
        "00c968e8",
        "_ZTISt12out_of_range",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00442cc4",
      "READ",
      [
        "storage",
        "00c9acb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00442cc0",
      "READ",
      [
        "storage",
        "00c9bc80",
        null,
        "pointer"
      ]
    ],
    [
      "00442cc0",
      "PARAM",
      [
        "storage",
        "00c978b8",
        "_ZTISt12out_of_range",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00442cc4",
      "READ",
      [
        "storage",
        "00c9bc88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004429a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md#insn-004429a8) · [`00442984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md#insn-00442984) · [`00442990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md#insn-00442990)
- 新版 [`00442cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md#insn-00442cc8) · [`00442ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md#insn-00442ca4) · [`00442cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md#insn-00442cb0)

~~~diff
- 004429a8 ["INT_ADD", "register:40f0:8", ["const:4429a8:8", "const:4:8"]]
- 004429a8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00442cc8 ["INT_ADD", "register:40f0:8", ["const:442cc8:8", "const:4:8"]]
+ 00442cc8 ["CALL", null, ["callee:00c58fb0:8"]]
- 004429a8 bytes 8e552094
+ 00442cc8 bytes ba582094
- 00442984 ["INT_ADD", "register:40f0:8", ["const:442984:8", "const:4:8"]]
- 00442984 ["CALL", null, ["callee:00c58f90:8"]]
+ 00442ca4 ["INT_ADD", "register:40f0:8", ["const:442ca4:8", "const:4:8"]]
+ 00442ca4 ["CALL", null, ["callee:00c58f90:8"]]
- 00442984 bytes 8f552094
+ 00442ca4 bytes bb582094
- 00442990 ["INT_ADD", "register:40f0:8", ["const:442990:8", "const:4:8"]]
- 00442990 ["CALL", null, ["callee:00442ce0:8"]]
+ 00442cb0 ["INT_ADD", "register:40f0:8", ["const:442cb0:8", "const:4:8"]]
+ 00442cb0 ["CALL", null, ["callee:00442ce0:8"]]
- 00442990 bytes 0c000094
+ 00442cb0 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f494eafd2866bdc10931355541ac993"></a>

### [`00442db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442db4.md) → [`004430d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430d4.md) FUN_004430d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004430e8",
      "incomplete_value": false,
      "site": "004430ec",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442dc8",
      "incomplete_value": false,
      "site": "00442dcc",
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
            "const:c8:8"
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
      "004430ec",
      "DATA",
      [
        "storage",
        "00c630c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004430ec",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442db4.md#insn-00442dc0) · [`00442dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442db4.md#insn-00442dc4) · [`00442dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442db4.md#insn-00442dc8)
- 新版 [`004430e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430d4.md#insn-004430e0) · [`004430e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430d4.md#insn-004430e4) · [`004430e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430d4.md#insn-004430e8)

~~~diff
- 00442dc0 ["INT_ADD", "register:40f0:8", ["const:442dc0:8", "const:4:8"]]
- 00442dc0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004430e0 ["INT_ADD", "register:40f0:8", ["const:4430e0:8", "const:4:8"]]
+ 004430e0 ["CALL", null, ["callee:00c58f30:8"]]
- 00442dc0 bytes 68542094
+ 004430e0 bytes 94572094
- 00442dc4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004430e4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442dc4 bytes 084100b0
+ 004430e4 bytes 084100b0
- 00442dc8 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00442dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004430e8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 004430e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004430e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004430e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442dc8 bytes 08210391
+ 004430e8 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e838fa72351f2816a72b48c364a94d2e"></a>

### [`00442dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442dd8.md) → [`004430f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430f8.md) FUN_004430f8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004430fc",
      "incomplete_value": false,
      "site": "00443100",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442ddc",
      "incomplete_value": false,
      "site": "00442de0",
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
            "const:c8:8"
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
      "00443100",
      "DATA",
      [
        "storage",
        "00c630c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443100",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442dd8.md#insn-00442dd8) · [`00442ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442dd8.md#insn-00442ddc)
- 新版 [`004430f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430f8.md#insn-004430f8) · [`004430fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004430f8.md#insn-004430fc)

~~~diff
- 00442dd8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004430f8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442dd8 bytes 084100b0
+ 004430f8 bytes 084100b0
- 00442ddc ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00442ddc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442ddc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442ddc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004430fc ["COPY", "tmp:0:8", ["const:98:8"]]
+ 004430fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004430fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004430fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442ddc bytes 08210391
+ 004430fc bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f996bec6cfb819305d14bf5b67bff81d"></a>

### [`00442edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442edc.md) → [`004431fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004431fc.md) FUN_004431fc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00443220",
      "incomplete_value": false,
      "site": "00443220",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442f00",
      "incomplete_value": false,
      "site": "00442f00",
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
            "const:158:8"
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
      "00443220",
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443220",
      "DATA",
      [
        "storage",
        "00c64128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442edc.md#insn-00442ef0) · [`00442ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442edc.md#insn-00442ef8) · [`00442efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442edc.md#insn-00442efc)
- 新版 [`00443210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004431fc.md#insn-00443210) · [`00443218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004431fc.md#insn-00443218) · [`0044321c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004431fc.md#insn-0044321c)

~~~diff
- 00442ef0 ["INT_ADD", "register:40f0:8", ["const:442ef0:8", "const:4:8"]]
- 00442ef0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00443210 ["INT_ADD", "register:40f0:8", ["const:443210:8", "const:4:8"]]
+ 00443210 ["CALL", null, ["callee:00c58f30:8"]]
- 00442ef0 bytes 1c542094
+ 00443210 bytes 48572094
- 00442ef8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00443218 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442ef8 bytes 084100b0
+ 00443218 bytes 084100b0
- 00442efc ["COPY", "tmp:0:8", ["const:158:8"]]
- 00442efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044321c ["COPY", "tmp:0:8", ["const:128:8"]]
+ 0044321c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044321c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044321c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442efc bytes 08610591
+ 0044321c bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6eeb8f06f7bab4f0f5392b0c60fc96b"></a>

### [`00442f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f10.md) → [`00443230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443230.md) FUN_00443230

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044323c",
      "incomplete_value": false,
      "site": "0044323c",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442f1c",
      "incomplete_value": false,
      "site": "00442f1c",
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
            "const:158:8"
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
      "0044323c",
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044323c",
      "DATA",
      [
        "storage",
        "00c64128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f10.md#insn-00442f14) · [`00442f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f10.md#insn-00442f18)
- 新版 [`00443234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443230.md#insn-00443234) · [`00443238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443230.md#insn-00443238)

~~~diff
- 00442f14 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 00443234 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00442f14 bytes 094100b0
+ 00443234 bytes 094100b0
- 00442f18 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00442f18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00442f18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00442f18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00443238 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 00443238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00443238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00443238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00442f18 bytes 29610591
+ 00443238 bytes 29a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50ed6fcb56885f3d5ee5fe6db44c74cb"></a>

### [`00442f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f68.md) → [`00443288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443288.md) FUN_00443288

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004432ac",
      "incomplete_value": false,
      "site": "004432ac",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442f8c",
      "incomplete_value": false,
      "site": "00442f8c",
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
      "004432ac",
      "DATA",
      [
        "storage",
        "00c631e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004432ac",
      "DATA",
      [
        "storage",
        "00c641b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f68.md#insn-00442f7c) · [`00442f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f68.md#insn-00442f84) · [`00442f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f68.md#insn-00442f88)
- 新版 [`0044329c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443288.md#insn-0044329c) · [`004432a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443288.md#insn-004432a4) · [`004432a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443288.md#insn-004432a8)

~~~diff
- 00442f7c ["INT_ADD", "register:40f0:8", ["const:442f7c:8", "const:4:8"]]
- 00442f7c ["CALL", null, ["callee:00c58f30:8"]]
+ 0044329c ["INT_ADD", "register:40f0:8", ["const:44329c:8", "const:4:8"]]
+ 0044329c ["CALL", null, ["callee:00c58f30:8"]]
- 00442f7c bytes f9532094
+ 0044329c bytes 25572094
- 00442f84 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004432a4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00442f84 bytes 084100b0
+ 004432a4 bytes 084100b0
- 00442f88 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00442f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00442f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00442f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004432a8 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 004432a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004432a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004432a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00442f88 bytes 08a10791
+ 004432a8 bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f18f449e262cd394cabb91ddaa22f3"></a>

### [`00442f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f9c.md) → [`004432bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004432bc.md) FUN_004432bc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004432c8",
      "incomplete_value": false,
      "site": "004432c8",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00442fa8",
      "incomplete_value": false,
      "site": "00442fa8",
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
      "004432c8",
      "DATA",
      [
        "storage",
        "00c631e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004432c8",
      "DATA",
      [
        "storage",
        "00c641b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00442fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f9c.md#insn-00442fa0) · [`00442fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442f9c.md#insn-00442fa4)
- 新版 [`004432c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004432bc.md#insn-004432c0) · [`004432c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004432bc.md#insn-004432c4)

~~~diff
- 00442fa0 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 004432c0 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00442fa0 bytes 094100b0
+ 004432c0 bytes 094100b0
- 00442fa4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00442fa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00442fa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00442fa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004432c4 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 004432c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004432c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004432c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00442fa4 bytes 29a10791
+ 004432c4 bytes 29e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d21a76604d072305e4046fab29c2d3a"></a>

### [`004430b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430b0.md) → [`004433d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004433d0.md) FUN_004433d0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004433f4",
      "incomplete_value": false,
      "site": "004433f4",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004430d4",
      "incomplete_value": false,
      "site": "004430d4",
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
            "const:278:8"
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
      "004433f4",
      "DATA",
      [
        "storage",
        "00c63278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004433f4",
      "DATA",
      [
        "storage",
        "00c64248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004430c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430b0.md#insn-004430c4) · [`004430cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430b0.md#insn-004430cc) · [`004430d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430b0.md#insn-004430d0)
- 新版 [`004433e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004433d0.md#insn-004433e4) · [`004433ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004433d0.md#insn-004433ec) · [`004433f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004433d0.md#insn-004433f0)

~~~diff
- 004430c4 ["INT_ADD", "register:40f0:8", ["const:4430c4:8", "const:4:8"]]
- 004430c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 004433e4 ["INT_ADD", "register:40f0:8", ["const:4433e4:8", "const:4:8"]]
+ 004433e4 ["CALL", null, ["callee:00c58f30:8"]]
- 004430c4 bytes a7532094
+ 004433e4 bytes d3562094
- 004430cc ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004433ec ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004430cc bytes 08410090
+ 004433ec bytes 084100b0
- 004430d0 ["COPY", "tmp:0:8", ["const:278:8"]]
- 004430d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004430d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004430d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004433f0 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 004433f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004433f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004433f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004430d0 bytes 08e10991
+ 004433f0 bytes 08210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b41d9c43d5acb6e6d3b380c97fb551d7"></a>

### [`004430e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430e4.md) → [`00443404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443404.md) FUN_00443404

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443410",
      "incomplete_value": false,
      "site": "00443410",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004430f0",
      "incomplete_value": false,
      "site": "004430f0",
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
            "const:278:8"
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
      "00443410",
      "DATA",
      [
        "storage",
        "00c63278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443410",
      "DATA",
      [
        "storage",
        "00c64248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004430e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430e4.md#insn-004430e8) · [`004430ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004430e4.md#insn-004430ec)
- 新版 [`00443408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443404.md#insn-00443408) · [`0044340c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443404.md#insn-0044340c)

~~~diff
- 004430e8 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 00443408 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004430e8 bytes 09410090
+ 00443408 bytes 094100b0
- 004430ec ["COPY", "tmp:0:8", ["const:278:8"]]
- 004430ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004430ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004430ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0044340c ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0044340c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0044340c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0044340c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004430ec bytes 29e10991
+ 0044340c bytes 29210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b62352189c4bfba8eb5c802d49ec1d"></a>

### [`004431ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431ac.md) → [`004434cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004434cc.md) FUN_004434cc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004434f0",
      "incomplete_value": false,
      "site": "004434f0",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004431d0",
      "incomplete_value": false,
      "site": "004431d0",
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
            "const:308:8"
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
      "004434f0",
      "DATA",
      [
        "storage",
        "00c63308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004434f0",
      "DATA",
      [
        "storage",
        "00c642d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004431c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431ac.md#insn-004431c0) · [`004431c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431ac.md#insn-004431c8) · [`004431cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431ac.md#insn-004431cc)
- 新版 [`004434e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004434cc.md#insn-004434e0) · [`004434e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004434cc.md#insn-004434e8) · [`004434ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004434cc.md#insn-004434ec)

~~~diff
- 004431c0 ["INT_ADD", "register:40f0:8", ["const:4431c0:8", "const:4:8"]]
- 004431c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004434e0 ["INT_ADD", "register:40f0:8", ["const:4434e0:8", "const:4:8"]]
+ 004434e0 ["CALL", null, ["callee:00c58f30:8"]]
- 004431c0 bytes 68532094
+ 004434e0 bytes 94562094
- 004431c8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004434e8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004431c8 bytes 08410090
+ 004434e8 bytes 084100b0
- 004431cc ["COPY", "tmp:0:8", ["const:308:8"]]
- 004431cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004431cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004431cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004434ec ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 004434ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004434ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004434ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004431cc bytes 08210c91
+ 004434ec bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e313e0aa061e08a931e417dd454fec79"></a>

### [`004431e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431e0.md) → [`00443500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443500.md) FUN_00443500

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044350c",
      "incomplete_value": false,
      "site": "0044350c",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004431ec",
      "incomplete_value": false,
      "site": "004431ec",
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
            "const:308:8"
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
      "0044350c",
      "DATA",
      [
        "storage",
        "00c63308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044350c",
      "DATA",
      [
        "storage",
        "00c642d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004431e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431e0.md#insn-004431e4) · [`004431e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004431e0.md#insn-004431e8)
- 新版 [`00443504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443500.md#insn-00443504) · [`00443508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443500.md#insn-00443508)

~~~diff
- 004431e4 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 00443504 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004431e4 bytes 09410090
+ 00443504 bytes 094100b0
- 004431e8 ["COPY", "tmp:0:8", ["const:308:8"]]
- 004431e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004431e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004431e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00443508 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00443508 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00443508 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00443508 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004431e8 bytes 29210c91
+ 00443508 bytes 29610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-955450079e3652ecf38e900e187812dc"></a>

### [`0044323c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044323c.md) → [`0044355c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/0044355c.md) FUN_0044355c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00443580",
      "incomplete_value": false,
      "site": "00443580",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443260",
      "incomplete_value": false,
      "site": "00443260",
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
            "const:388:8"
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
      "00443580",
      "DATA",
      [
        "storage",
        "00c63388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443580",
      "DATA",
      [
        "storage",
        "00c64358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044323c.md#insn-00443250) · [`00443258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044323c.md#insn-00443258) · [`0044325c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044323c.md#insn-0044325c)
- 新版 [`00443570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/0044355c.md#insn-00443570) · [`00443578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/0044355c.md#insn-00443578) · [`0044357c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/0044355c.md#insn-0044357c)

~~~diff
- 00443250 ["INT_ADD", "register:40f0:8", ["const:443250:8", "const:4:8"]]
- 00443250 ["CALL", null, ["callee:00c58f30:8"]]
+ 00443570 ["INT_ADD", "register:40f0:8", ["const:443570:8", "const:4:8"]]
+ 00443570 ["CALL", null, ["callee:00c58f30:8"]]
- 00443250 bytes 44532094
+ 00443570 bytes 70562094
- 00443258 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00443578 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443258 bytes 08410090
+ 00443578 bytes 084100b0
- 0044325c ["COPY", "tmp:0:8", ["const:388:8"]]
- 0044325c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044325c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044325c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044357c ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0044357c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044357c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044357c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044325c bytes 08210e91
+ 0044357c bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3958a0d006cac8726c58cd3518e1c3ad"></a>

### [`00443270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443270.md) → [`00443590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443590.md) FUN_00443590

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044359c",
      "incomplete_value": false,
      "site": "0044359c",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044327c",
      "incomplete_value": false,
      "site": "0044327c",
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
            "const:388:8"
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
      "0044359c",
      "DATA",
      [
        "storage",
        "00c63388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044359c",
      "DATA",
      [
        "storage",
        "00c64358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443270.md#insn-00443274) · [`00443278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443270.md#insn-00443278)
- 新版 [`00443594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443590.md#insn-00443594) · [`00443598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443590.md#insn-00443598)

~~~diff
- 00443274 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 00443594 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00443274 bytes 09410090
+ 00443594 bytes 094100b0
- 00443278 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00443278 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00443278 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00443278 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00443598 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00443598 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00443598 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00443598 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00443278 bytes 29210e91
+ 00443598 bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f748f12157568a2d0d9e3214c4be1e8"></a>

### [`00443388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443388.md) → [`004436a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436a8.md) FUN_004436a8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004436cc",
      "incomplete_value": false,
      "site": "004436cc",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004433ac",
      "incomplete_value": false,
      "site": "004433ac",
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
            "const:408:8"
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
      "004436cc",
      "DATA",
      [
        "storage",
        "00c63408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004436cc",
      "DATA",
      [
        "storage",
        "00c643d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044339c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443388.md#insn-0044339c) · [`004433a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443388.md#insn-004433a4) · [`004433a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443388.md#insn-004433a8)
- 新版 [`004436bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436a8.md#insn-004436bc) · [`004436c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436a8.md#insn-004436c4) · [`004436c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436a8.md#insn-004436c8)

~~~diff
- 0044339c ["INT_ADD", "register:40f0:8", ["const:44339c:8", "const:4:8"]]
- 0044339c ["CALL", null, ["callee:00c58f30:8"]]
+ 004436bc ["INT_ADD", "register:40f0:8", ["const:4436bc:8", "const:4:8"]]
+ 004436bc ["CALL", null, ["callee:00c58f30:8"]]
- 0044339c bytes f1522094
+ 004436bc bytes 1d562094
- 004433a4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004436c4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004433a4 bytes 08410090
+ 004436c4 bytes 084100b0
- 004433a8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 004433a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004433a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004433a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004436c8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 004436c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004436c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004436c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004433a8 bytes 08211091
+ 004436c8 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96c4f70cfb9e0050806f8cba1cad0e4"></a>

### [`004433bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004433bc.md) → [`004436dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436dc.md) FUN_004436dc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004436e8",
      "incomplete_value": false,
      "site": "004436e8",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004433c8",
      "incomplete_value": false,
      "site": "004433c8",
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
            "const:408:8"
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
      "004436e8",
      "DATA",
      [
        "storage",
        "00c63408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004436e8",
      "DATA",
      [
        "storage",
        "00c643d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004433c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004433bc.md#insn-004433c0) · [`004433c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004433bc.md#insn-004433c4)
- 新版 [`004436e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436dc.md#insn-004436e0) · [`004436e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004436dc.md#insn-004436e4)

~~~diff
- 004433c0 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 004436e0 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004433c0 bytes 09410090
+ 004436e0 bytes 094100b0
- 004433c4 ["COPY", "tmp:0:8", ["const:408:8"]]
- 004433c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004433c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004433c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004436e4 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 004436e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004436e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004436e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004433c4 bytes 29211091
+ 004436e4 bytes 29610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbc9f4a1b6b3a49828b6cf2be7c16afb"></a>

### [`00443484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443484.md) → [`004437a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437a4.md) FUN_004437a4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004437b8",
      "incomplete_value": false,
      "site": "004437bc",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443498",
      "incomplete_value": false,
      "site": "0044349c",
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
            "const:488:8"
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
      "004437bc",
      "DATA",
      [
        "storage",
        "00c63488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004437bc",
      "DATA",
      [
        "storage",
        "00c64458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443484.md#insn-00443490) · [`00443494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443484.md#insn-00443494) · [`00443498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443484.md#insn-00443498)
- 新版 [`004437b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437a4.md#insn-004437b0) · [`004437b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437a4.md#insn-004437b4) · [`004437b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437a4.md#insn-004437b8)

~~~diff
- 00443490 ["INT_ADD", "register:40f0:8", ["const:443490:8", "const:4:8"]]
- 00443490 ["CALL", null, ["callee:00c58f30:8"]]
+ 004437b0 ["INT_ADD", "register:40f0:8", ["const:4437b0:8", "const:4:8"]]
+ 004437b0 ["CALL", null, ["callee:00c58f30:8"]]
- 00443490 bytes b4522094
+ 004437b0 bytes e0552094
- 00443494 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004437b4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443494 bytes 08410090
+ 004437b4 bytes 084100b0
- 00443498 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00443498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004437b8 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 004437b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004437b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004437b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443498 bytes 08211291
+ 004437b8 bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4965e9dae12e0d58aa220eab4f32823a"></a>

### [`004434a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434a8.md) → [`004437c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437c8.md) FUN_004437c8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004437cc",
      "incomplete_value": false,
      "site": "004437d0",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004434ac",
      "incomplete_value": false,
      "site": "004434b0",
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
            "const:488:8"
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
      "004437d0",
      "DATA",
      [
        "storage",
        "00c63488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004437d0",
      "DATA",
      [
        "storage",
        "00c64458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004434a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434a8.md#insn-004434a8) · [`004434ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434a8.md#insn-004434ac)
- 新版 [`004437c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437c8.md#insn-004437c8) · [`004437cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437c8.md#insn-004437cc)

~~~diff
- 004434a8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004437c8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004434a8 bytes 08410090
+ 004437c8 bytes 084100b0
- 004434ac ["COPY", "tmp:0:8", ["const:488:8"]]
- 004434ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004434ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004434ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004437cc ["COPY", "tmp:0:8", ["const:458:8"]]
+ 004437cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004437cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004437cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004434ac bytes 08211291
+ 004437cc bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d27ce7767e6c0b0d44181aa968b10087"></a>

### [`004434c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434c0.md) → [`004437e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437e0.md) FUN_004437e0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043ea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043ea1c.md) [`0043eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eaa0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043ed3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ed3c.md) [`0043edc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043edc0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 78.31% / 新版 78.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443874",
      "incomplete_value": false,
      "site": "00443874",
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
            "const:a7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443554",
      "incomplete_value": false,
      "site": "00443554",
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
            "const:abc:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044389c",
      "incomplete_value": false,
      "site": "004438a0",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044357c",
      "incomplete_value": false,
      "site": "00443580",
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
            "const:ae0:8"
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
      "definition_site": "004438ac",
      "incomplete_value": false,
      "site": "004438b0",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044358c",
      "incomplete_value": false,
      "site": "00443590",
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
            "const:a88:8"
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
      "00443830",
      "READ",
      [
        "storage",
        "00ca4ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00443864",
      "READ",
      [
        "storage",
        "00ca4ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00443874",
      "WRITE",
      [
        "storage",
        "00ca4abc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00443830",
      "READ",
      [
        "storage",
        "00ca5aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00443864",
      "READ",
      [
        "storage",
        "00ca5aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00443874",
      "WRITE",
      [
        "storage",
        "00ca5a7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434c0.md#insn-00443554) · [`00443580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434c0.md#insn-00443580) · [`00443590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004434c0.md#insn-00443590)
- 新版 [`00443874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437e0.md#insn-00443874) · [`004438a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437e0.md#insn-004438a0) · [`004438b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004437e0.md#insn-004438b0)

~~~diff
- 00443554 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:abc:8"]]
- 00443554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00443874 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a7c:8"]]
+ 00443874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00443554 bytes 28bd0ab9
+ 00443874 bytes 287d0ab9
- 00443580 ["INT_ADD", "register:40f0:8", ["const:443580:8", "const:4:8"]]
- 00443580 ["CALL", null, ["callee:00c58ef0:8"]]
+ 004438a0 ["INT_ADD", "register:40f0:8", ["const:4438a0:8", "const:4:8"]]
+ 004438a0 ["CALL", null, ["callee:00c58ef0:8"]]
- 00443580 bytes 68522094
+ 004438a0 bytes 94552094
- 00443590 ["INT_ADD", "register:40f0:8", ["const:443590:8", "const:4:8"]]
- 00443590 ["CALL", null, ["callee:0043edc0:8"]]
+ 004438b0 ["INT_ADD", "register:40f0:8", ["const:4438b0:8", "const:4:8"]]
+ 004438b0 ["CALL", null, ["callee:0043edc0:8"]]
- 00443590 bytes 44edff97
+ 004438b0 bytes 44edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09886c14b9e100438063062addd2ad1d"></a>

### [`00443664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443664.md) → [`00443984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443984.md) FUN_00443984

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00443998",
      "incomplete_value": false,
      "site": "0044399c",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443678",
      "incomplete_value": false,
      "site": "0044367c",
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
            "const:518:8"
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
      "0044399c",
      "DATA",
      [
        "storage",
        "00c63518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044399c",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443664.md#insn-00443670) · [`00443674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443664.md#insn-00443674) · [`00443678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443664.md#insn-00443678)
- 新版 [`00443990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443984.md#insn-00443990) · [`00443994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443984.md#insn-00443994) · [`00443998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443984.md#insn-00443998)

~~~diff
- 00443670 ["INT_ADD", "register:40f0:8", ["const:443670:8", "const:4:8"]]
- 00443670 ["CALL", null, ["callee:00c58f30:8"]]
+ 00443990 ["INT_ADD", "register:40f0:8", ["const:443990:8", "const:4:8"]]
+ 00443990 ["CALL", null, ["callee:00c58f30:8"]]
- 00443670 bytes 3c522094
+ 00443990 bytes 68552094
- 00443674 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00443994 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443674 bytes 08410090
+ 00443994 bytes 084100b0
- 00443678 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00443678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443998 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 00443998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443678 bytes 08611491
+ 00443998 bytes 08a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82f15f2dab5cbc802d9684cd4d745681"></a>

### [`00443688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443688.md) → [`004439a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439a8.md) FUN_004439a8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004439ac",
      "incomplete_value": false,
      "site": "004439b0",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044368c",
      "incomplete_value": false,
      "site": "00443690",
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
      "004439b0",
      "DATA",
      [
        "storage",
        "00c63518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004439b0",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443688.md#insn-00443688) · [`0044368c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443688.md#insn-0044368c)
- 新版 [`004439a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439a8.md#insn-004439a8) · [`004439ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439a8.md#insn-004439ac)

~~~diff
- 00443688 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 004439a8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443688 bytes 08410090
+ 004439a8 bytes 084100b0
- 0044368c ["COPY", "tmp:0:8", ["const:518:8"]]
- 0044368c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044368c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044368c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004439ac ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 004439ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004439ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004439ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044368c bytes 08611491
+ 004439ac bytes 08a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b6b4abf193920b4774a586485b0781"></a>

### [`004436a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436a0.md) → [`004439c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439c0.md) FUN_004439c0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004439cc",
      "incomplete_value": true,
      "site": "004439cc",
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
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004436ac",
      "incomplete_value": true,
      "site": "004436ac",
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
            "const:44:8"
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
      "004439c8",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "004439cc",
      "WRITE",
      [
        "storage",
        "00ca4db4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004439c8",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      "004439cc",
      "WRITE",
      [
        "storage",
        "00ca5d74",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004436a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436a0.md#insn-004436a0) · [`004436a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436a0.md#insn-004436a8)
- 新版 [`004439c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439c0.md#insn-004439c0) · [`004439c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/004439c0.md#insn-004439c8)

~~~diff
- 004436a0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004439c0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004436a0 bytes a84200f0
+ 004439c0 bytes c8420090
- 004436a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c38:8"]]
- 004436a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004439c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 004439c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004436a8 bytes 081d46f9
+ 004439c8 bytes 080546f9
~~~


<a id="compare-d270969be224723b29906d6d0582963a"></a>

### [`004436e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436e4.md) → [`00443a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a04.md) FUN_00443a04

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00443a18",
      "incomplete_value": false,
      "site": "00443a1c",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004436f8",
      "incomplete_value": false,
      "site": "004436fc",
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
            "const:5a8:8"
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
      "00443a1c",
      "DATA",
      [
        "storage",
        "00c635a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443a1c",
      "DATA",
      [
        "storage",
        "00c64578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004436f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436e4.md#insn-004436f0) · [`004436f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436e4.md#insn-004436f4) · [`004436f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/004436e4.md#insn-004436f8)
- 新版 [`00443a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a04.md#insn-00443a10) · [`00443a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a04.md#insn-00443a14) · [`00443a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a04.md#insn-00443a18)

~~~diff
- 004436f0 ["INT_ADD", "register:40f0:8", ["const:4436f0:8", "const:4:8"]]
- 004436f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00443a10 ["INT_ADD", "register:40f0:8", ["const:443a10:8", "const:4:8"]]
+ 00443a10 ["CALL", null, ["callee:00c58f30:8"]]
- 004436f0 bytes 1c522094
+ 00443a10 bytes 48552094
- 004436f4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00443a14 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004436f4 bytes 08410090
+ 00443a14 bytes 084100b0
- 004436f8 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 004436f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004436f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004436f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443a18 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00443a18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443a18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443a18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004436f8 bytes 08a11691
+ 00443a18 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3527e5e862f74011ca574026459ca7"></a>

### [`00443708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443708.md) → [`00443a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a28.md) FUN_00443a28

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443a2c",
      "incomplete_value": false,
      "site": "00443a30",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044370c",
      "incomplete_value": false,
      "site": "00443710",
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
            "const:5a8:8"
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
      "00443a30",
      "DATA",
      [
        "storage",
        "00c635a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443a30",
      "DATA",
      [
        "storage",
        "00c64578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443708.md#insn-00443708) · [`0044370c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443708.md#insn-0044370c)
- 新版 [`00443a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a28.md#insn-00443a28) · [`00443a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a28.md#insn-00443a2c)

~~~diff
- 00443708 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00443a28 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00443708 bytes 08410090
+ 00443a28 bytes 084100b0
- 0044370c ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 0044370c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044370c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044370c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443a2c ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00443a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044370c bytes 08a11691
+ 00443a2c bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893d1b886df44dd0de9715bf5c840aa2"></a>

### [`00443720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443720.md) → [`00443a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a40.md) FUN_00443a40

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443a48",
      "incomplete_value": false,
      "site": "00443a48",
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
                "const:d30:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443728",
      "incomplete_value": false,
      "site": "00443728",
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
                "const:d70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
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
      "00443a48",
      "WRITE",
      [
        "storage",
        "00ca4db4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00443a48",
      "WRITE",
      [
        "storage",
        "00ca5d74",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443720.md#insn-00443720) · [`00443724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443720.md#insn-00443724)
- 新版 [`00443a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a40.md#insn-00443a40) · [`00443a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a40.md#insn-00443a44)

~~~diff
- 00443720 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 00443a40 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00443720 bytes 084300b0
+ 00443a40 bytes 084300d0
- 00443724 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 00443724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00443724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00443724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443a44 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00443a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00443724 bytes 08c13591
+ 00443a44 bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a7f8e5538441da1de15cad3b687ef0a"></a>

### [`00443758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443758.md) → [`00443a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a78.md) FUN_00443a78

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0043fc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00443a84",
      "incomplete_value": false,
      "site": "00443a88",
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
      "definition_site": "00443764",
      "incomplete_value": false,
      "site": "00443768",
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
      "00443a84",
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
      "00443a84",
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

- 旧版 [`00443768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443758.md#insn-00443768) · [`00443760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443758.md#insn-00443760) · [`00443764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443758.md#insn-00443764)
- 新版 [`00443a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a78.md#insn-00443a88) · [`00443a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a78.md#insn-00443a80) · [`00443a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a78.md#insn-00443a84)

~~~diff
- 00443768 ["INT_ADD", "register:40f0:8", ["const:443768:8", "const:4:8"]]
- 00443768 ["CALL", null, ["callee:0043bad8:8"]]
+ 00443a88 ["INT_ADD", "register:40f0:8", ["const:443a88:8", "const:4:8"]]
+ 00443a88 ["CALL", null, ["callee:0043bad8:8"]]
- 00443768 bytes 14e0ff97
+ 00443a88 bytes 14e0ff97
- 00443760 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00443a80 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00443760 bytes a0f3ff90
+ 00443a80 bytes a0f3ffb0
- 00443764 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00443764 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00443764 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00443764 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00443a84 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00443a84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00443a84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00443a84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00443764 bytes 00303e91
+ 00443a84 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b40beb3ccecbd0145066fce51ca94d98"></a>

### [`0044376c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044376c.md) → [`00443a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a8c.md) _INIT_7

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
      "definition_site": "00443ac8",
      "incomplete_value": true,
      "site": "00443ae4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004437a8",
      "incomplete_value": true,
      "site": "004437c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443aec",
      "incomplete_value": true,
      "site": "00443b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004437cc",
      "incomplete_value": true,
      "site": "004437e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443b0c",
      "incomplete_value": true,
      "site": "00443b28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004437ec",
      "incomplete_value": true,
      "site": "00443808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00443ac8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00443aec",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00443b0c",
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
      "00443ac8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00443aec",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00443b0c",
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

- 旧版 [`004438cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044376c.md#insn-004438cc) · [`004439a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044376c.md#insn-004439a0) · [`00443794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/0044376c.md#insn-00443794)
- 新版 [`00443bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a8c.md#insn-00443bec) · [`00443cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a8c.md#insn-00443cc0) · [`00443ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443a8c.md#insn-00443ab4)

~~~diff
- 004438cc ["INT_ADD", "register:40f0:8", ["const:4438cc:8", "const:4:8"]]
- 004438cc ["CALL", null, ["callee:0043bb58:8"]]
+ 00443bec ["INT_ADD", "register:40f0:8", ["const:443bec:8", "const:4:8"]]
+ 00443bec ["CALL", null, ["callee:0043bb58:8"]]
- 004438cc bytes dbdfff97
+ 00443bec bytes dbdfff97
- 004439a0 ["INT_ADD", "register:40f0:8", ["const:4439a0:8", "const:4:8"]]
- 004439a0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00443cc0 ["INT_ADD", "register:40f0:8", ["const:443cc0:8", "const:4:8"]]
+ 00443cc0 ["CALL", null, ["callee:00c58ed0:8"]]
- 004439a0 bytes 58512094
+ 00443cc0 bytes 84542094
- 00443794 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 00443ab4 ["COPY", "register:4098:8", ["const:ca5000:8"]]
- 00443794 bytes 134300b0
+ 00443ab4 bytes 134300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1322fcba1dae9b13d1d013b658c0705"></a>

### [`00443afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443afc.md) → [`00443e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443e1c.md) _INIT_8

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
      "definition_site": "00443e58",
      "incomplete_value": true,
      "site": "00443e74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443b38",
      "incomplete_value": true,
      "site": "00443b54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443e7c",
      "incomplete_value": true,
      "site": "00443e98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443b5c",
      "incomplete_value": true,
      "site": "00443b78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443e9c",
      "incomplete_value": true,
      "site": "00443eb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443b7c",
      "incomplete_value": true,
      "site": "00443b98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00443e58",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00443e7c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00443e9c",
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
      "00443e58",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00443e7c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00443e9c",
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

- 旧版 [`00443c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443afc.md#insn-00443c5c) · [`00443d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443afc.md#insn-00443d30) · [`00443b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443afc.md#insn-00443b24)
- 新版 [`00443f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443e1c.md#insn-00443f7c) · [`00444050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443e1c.md#insn-00444050) · [`00443e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00443/00443e1c.md#insn-00443e44)

~~~diff
- 00443c5c ["INT_ADD", "register:40f0:8", ["const:443c5c:8", "const:4:8"]]
- 00443c5c ["CALL", null, ["callee:0043bb58:8"]]
+ 00443f7c ["INT_ADD", "register:40f0:8", ["const:443f7c:8", "const:4:8"]]
+ 00443f7c ["CALL", null, ["callee:0043bb58:8"]]
- 00443c5c bytes f7deff97
+ 00443f7c bytes f7deff97
- 00443d30 ["INT_ADD", "register:40f0:8", ["const:443d30:8", "const:4:8"]]
- 00443d30 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00444050 ["INT_ADD", "register:40f0:8", ["const:444050:8", "const:4:8"]]
+ 00444050 ["CALL", null, ["callee:00c58ed0:8"]]
- 00443d30 bytes 74502094
+ 00444050 bytes a0532094
- 00443b24 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 00443e44 ["COPY", "register:4098:8", ["const:ca5000:8"]]
- 00443b24 bytes 134300b0
+ 00443e44 bytes 134300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd94d7af2d0c0015960abd997fecf073"></a>

### [`00443e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443e8c.md) → [`004441ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004441ac.md) FUN_004441ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab90.md) · 呼出先 8件 [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 1件 [`0044aeb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044aeb0.md) · 呼出先 8件 [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.64% / 新版 75.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 22件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444270",
      "incomplete_value": false,
      "site": "00444270",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443f50",
      "incomplete_value": false,
      "site": "00443f50",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004442a8",
      "incomplete_value": false,
      "site": "004442a8",
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
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443f88",
      "incomplete_value": false,
      "site": "00443f88",
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
            "const:b34:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004442fc",
      "incomplete_value": false,
      "site": "004442fc",
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
                "const:ad8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00443fdc",
      "incomplete_value": false,
      "site": "00443fdc",
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
                "const:b18:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004441dc",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "004441e8",
      "READ",
      [
        "storage",
        "00ca4b20",
        null,
        "undefined8"
      ]
    ],
    [
      "004441f0",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004441dc",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "004441e8",
      "READ",
      [
        "storage",
        "00ca5ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "004441f0",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00443f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443e8c.md#insn-00443f50) · [`00443f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443e8c.md#insn-00443f88) · [`00443fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00443/00443e8c.md#insn-00443fbc)
- 新版 [`00444270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004441ac.md#insn-00444270) · [`004442a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004441ac.md#insn-004442a8) · [`004442dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004441ac.md#insn-004442dc)

~~~diff
- 00443f50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
- 00443f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00444270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:af0:8"]]
+ 00444270 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00443f50 bytes 09310bb9
+ 00444270 bytes 09f10ab9
- 00443f88 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00443f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:b34:8"]]
- 00443f88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 004442a8 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 004442a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:af4:8"]]
+ 004442a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00443f88 bytes 09d12c39
+ 004442a8 bytes 09d12b39
- 00443fbc ["INT_ADD", "register:40f0:8", ["const:443fbc:8", "const:4:8"]]
- 00443fbc ["CALL", null, ["callee:00c58ef0:8"]]
+ 004442dc ["INT_ADD", "register:40f0:8", ["const:4442dc:8", "const:4:8"]]
+ 004442dc ["CALL", null, ["callee:00c58ef0:8"]]
- 00443fbc bytes d94f2094
+ 004442dc bytes 05532094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af06255c39d8b4440bb86066dc2ea346"></a>

### [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) → [`00444440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md) FUN_00444440

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`008723d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md) [`00872a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md) [`00872f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872f04.md) [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 4件 [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 6件 [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) [`0087337c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/0087337c.md) [`00873a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873a14.md) [`00873eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873eb0.md) [`00877f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md) · 呼出先 4件 [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444490",
      "incomplete_value": false,
      "site": "00444490",
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
                "const:ad8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444170",
      "incomplete_value": false,
      "site": "00444170",
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
                "const:b18:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "00444494",
      "incomplete_value": false,
      "site": "00444494",
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
                "const:ad8:8"
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
      "definition_site": "00444174",
      "incomplete_value": false,
      "site": "00444174",
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
                "const:b18:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444494",
      "incomplete_value": false,
      "site": "00444494",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444174",
      "incomplete_value": false,
      "site": "00444174",
      "value": [
        "INT_ADD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00444450",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "0044445c",
      "DATA",
      [
        "storage",
        "00ca4b18",
        null,
        "undefined8"
      ]
    ],
    [
      "0044446c",
      "PARAM",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00444450",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "0044445c",
      "DATA",
      [
        "storage",
        "00ca5ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "0044446c",
      "PARAM",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md#insn-00444150) · [`00444180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md#insn-00444180) · [`0044418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md#insn-0044418c)
- 新版 [`00444470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md#insn-00444470) · [`004444a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md#insn-004444a0) · [`004444ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md#insn-004444ac)

~~~diff
- 00444150 ["INT_ADD", "register:40f0:8", ["const:444150:8", "const:4:8"]]
- 00444150 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00444470 ["INT_ADD", "register:40f0:8", ["const:444470:8", "const:4:8"]]
+ 00444470 ["CALL", null, ["callee:00c58ef0:8"]]
- 00444150 bytes 744f2094
+ 00444470 bytes a0522094
- 00444180 ["INT_ADD", "register:40f0:8", ["const:444180:8", "const:4:8"]]
- 00444180 ["CALL", null, ["callee:00c58ed0:8"]]
+ 004444a0 ["INT_ADD", "register:40f0:8", ["const:4444a0:8", "const:4:8"]]
+ 004444a0 ["CALL", null, ["callee:00c58ed0:8"]]
- 00444180 bytes 604f2094
+ 004444a0 bytes 8c522094
- 0044418c ["INT_ADD", "register:40f0:8", ["const:44418c:8", "const:4:8"]]
- 0044418c ["CALL", null, ["callee:00c58f10:8"]]
+ 004444ac ["INT_ADD", "register:40f0:8", ["const:4444ac:8", "const:4:8"]]
+ 004444ac ["CALL", null, ["callee:00c58f10:8"]]
- 0044418c bytes 6d4f2094
+ 004444ac bytes 99522094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c67cd068a2e3c15380fea22339ee50e8"></a>

### [`00444194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444194.md) → [`004444b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004444b4.md) FUN_004444b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0044ac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ac00.md) · 呼出先 6件 [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`0044af20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044af20.md) · 呼出先 6件 [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 29件, `call_target` 1件, `store_destination` 38件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444508",
      "incomplete_value": false,
      "site": "00444508",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004441e8",
      "incomplete_value": false,
      "site": "004441e8",
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
            "const:b20:8"
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
      "definition_site": "00444508",
      "incomplete_value": false,
      "site": "00444508",
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
                "const:ae0:8"
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
      "definition_site": "004441e8",
      "incomplete_value": false,
      "site": "004441e8",
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
                "const:b20:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0044458c",
      "incomplete_value": true,
      "site": "0044458c",
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
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044426c",
      "incomplete_value": true,
      "site": "0044426c",
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
            "const:b34:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004444c8",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "004444d4",
      "READ",
      [
        "storage",
        "00ca4b20",
        null,
        "undefined8"
      ]
    ],
    [
      "004444dc",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004444c8",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "004444d4",
      "READ",
      [
        "storage",
        "00ca5ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "004444dc",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044426c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444194.md#insn-0044426c) · [`004441a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444194.md#insn-004441a0) · [`004441a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444194.md#insn-004441a4)
- 新版 [`0044458c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004444b4.md#insn-0044458c) · [`004444c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004444b4.md#insn-004444c0) · [`004444c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004444b4.md#insn-004444c4)

~~~diff
- 0044426c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0044426c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0044426c ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:b34:8"]]
- 0044426c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0044458c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0044458c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0044458c ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:af4:8"]]
+ 0044458c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0044426c bytes 7fd22c39
+ 0044458c bytes 7fd22b39
- 004441a0 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 004444c0 ["COPY", "register:40a0:8", ["const:ca5000:8"]]
- 004441a0 bytes 14430090
+ 004444c0 bytes 144300b0
- 004441a4 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 004441a4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 004441a4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 004441a4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 004444c4 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 004444c4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 004444c4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 004444c4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 004441a4 bytes 94222d91
+ 004444c4 bytes 94222c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b41fe4dfda3bc40fba7b6df18361dfb"></a>

### [`004444a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md) → [`004447c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md) FUN_004447c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0044612c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md) [`0044ac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ac00.md) · 呼出先 10件 [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00446318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md) [`00446654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446654.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 2件 [`0044644c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/0044644c.md) [`0044af20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044af20.md) · 呼出先 10件 [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00446638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md) [`00446974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446974.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.69% / 新版 89.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444920",
      "incomplete_value": false,
      "site": "00444920",
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
                "const:ad8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444600",
      "incomplete_value": false,
      "site": "00444600",
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
                "const:b18:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444924",
      "incomplete_value": false,
      "site": "00444924",
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
                "const:ad8:8"
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
      "definition_site": "00444604",
      "incomplete_value": false,
      "site": "00444604",
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
                "const:b18:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444924",
      "incomplete_value": false,
      "site": "00444924",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444604",
      "incomplete_value": false,
      "site": "00444604",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00444894",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "004448fc",
      "PARAM",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "0044490c",
      "PARAM",
      [
        "storage",
        "00ca4b18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00444894",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "004448fc",
      "PARAM",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "0044490c",
      "PARAM",
      [
        "storage",
        "00ca5ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004445e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md#insn-004445e0) · [`00444610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md#insn-00444610) · [`0044461c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md#insn-0044461c)
- 新版 [`00444900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md#insn-00444900) · [`00444930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md#insn-00444930) · [`0044493c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md#insn-0044493c)

~~~diff
- 004445e0 ["INT_ADD", "register:40f0:8", ["const:4445e0:8", "const:4:8"]]
- 004445e0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00444900 ["INT_ADD", "register:40f0:8", ["const:444900:8", "const:4:8"]]
+ 00444900 ["CALL", null, ["callee:00c58ef0:8"]]
- 004445e0 bytes 504e2094
+ 00444900 bytes 7c512094
- 00444610 ["INT_ADD", "register:40f0:8", ["const:444610:8", "const:4:8"]]
- 00444610 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00444930 ["INT_ADD", "register:40f0:8", ["const:444930:8", "const:4:8"]]
+ 00444930 ["CALL", null, ["callee:00c58ed0:8"]]
- 00444610 bytes 3c4e2094
+ 00444930 bytes 68512094
- 0044461c ["INT_ADD", "register:40f0:8", ["const:44461c:8", "const:4:8"]]
- 0044461c ["CALL", null, ["callee:00c58f10:8"]]
+ 0044493c ["INT_ADD", "register:40f0:8", ["const:44493c:8", "const:4:8"]]
+ 0044493c ["CALL", null, ["callee:00c58f10:8"]]
- 0044461c bytes 494e2094
+ 0044493c bytes 75512094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe893c451f9c0ef9ac765f1cfe537162"></a>

### [`004446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md) → [`004449e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md) FUN_004449e0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008723d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md) [`00550c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c5c.md)
- 新版 呼出元 1件 [`0087337c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/0087337c.md) · 呼出先 13件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00444f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444f38.md) [`004470d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/004470d0.md) [`00550f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.64% / 新版 99.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00444c6c",
      "incomplete_value": false,
      "site": "00444c70",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044494c",
      "incomplete_value": false,
      "site": "00444950",
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
            "const:ee1:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00444c6c",
      "PARAM",
      [
        "storage",
        "002b9ee1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00444c6c",
      "PARAM",
      [
        "storage",
        "002b9fbf",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md#insn-00444950) · [`00444714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md#insn-00444714) · [`00444720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md#insn-00444720)
- 新版 [`00444c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md#insn-00444c70) · [`00444a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md#insn-00444a34) · [`00444a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md#insn-00444a40)

~~~diff
- 00444950 ["INT_ADD", "register:40f0:8", ["const:444950:8", "const:4:8"]]
- 00444950 ["CALL", null, ["callee:00c59150:8"]]
+ 00444c70 ["INT_ADD", "register:40f0:8", ["const:444c70:8", "const:4:8"]]
+ 00444c70 ["CALL", null, ["callee:00c59150:8"]]
- 00444950 bytes 0c4e2094
+ 00444c70 bytes 38512094
- 00444714 ["INT_ADD", "register:40f0:8", ["const:444714:8", "const:4:8"]]
- 00444714 ["CALL", null, ["callee:00444f38:8"]]
+ 00444a34 ["INT_ADD", "register:40f0:8", ["const:444a34:8", "const:4:8"]]
+ 00444a34 ["CALL", null, ["callee:00444f38:8"]]
- 00444714 bytes 41010094
+ 00444a34 bytes 41010094
- 00444720 ["INT_ADD", "register:40f0:8", ["const:444720:8", "const:4:8"]]
- 00444720 ["CALL", null, ["callee:00550f88:8"]]
+ 00444a40 ["INT_ADD", "register:40f0:8", ["const:444a40:8", "const:4:8"]]
+ 00444a40 ["CALL", null, ["callee:00550f88:8"]]
- 00444720 bytes 52310494
+ 00444a40 bytes 52310494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772560ddd1fd0166d7ad862d03666a0b"></a>

### [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) → [`00444f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444f38.md) FUN_00444f38

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0044ad0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ad0c.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md)
- 新版 呼出元 1件 [`004449e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md) · 呼出先 14件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0044b02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b02c.md) [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.47% / 新版 91.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00444f78",
      "incomplete_value": false,
      "site": "00444f7c",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00444c58",
      "incomplete_value": false,
      "site": "00444c5c",
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
            "const:628:8"
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
      "definition_site": "00445094",
      "incomplete_value": true,
      "site": "00445098",
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
      "definition_site": "00444d74",
      "incomplete_value": true,
      "site": "00444d78",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00445090",
      "incomplete_value": true,
      "site": "0044509c",
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
      "definition_site": "00444d70",
      "incomplete_value": true,
      "site": "00444d7c",
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
      "00444f7c",
      "DATA",
      [
        "storage",
        "00c63628",
        null,
        "undefined *"
      ]
    ],
    [
      "00445084",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "00445088",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00444f7c",
      "DATA",
      [
        "storage",
        "00c645f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00445084",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ],
    [
      "00445088",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00444c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md#insn-00444c50) · [`00444c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md#insn-00444c54) · [`00444c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md#insn-00444c58)
- 新版 [`00444f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444f38.md#insn-00444f70) · [`00444f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444f38.md#insn-00444f74) · [`00444f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444f38.md#insn-00444f78)

~~~diff
- 00444c50 ["INT_ADD", "register:40f0:8", ["const:444c50:8", "const:4:8"]]
- 00444c50 ["CALL", null, ["callee:00488180:8"]]
+ 00444f70 ["INT_ADD", "register:40f0:8", ["const:444f70:8", "const:4:8"]]
+ 00444f70 ["CALL", null, ["callee:00488180:8"]]
- 00444c50 bytes 840c0194
+ 00444f70 bytes 840c0194
- 00444c54 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 00444f74 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00444c54 bytes e84000f0
+ 00444f74 bytes 08410090
- 00444c58 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00444c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00444c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00444c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00444f78 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00444f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00444f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00444f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00444c58 bytes 08a11891
+ 00444f78 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257329bad34e6404bc191f1545681bfc"></a>

### [`0044612c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md) → [`0044644c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/0044644c.md) FUN_0044644c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) · 呼出先 11件 [`004444a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md) [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00446318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md) [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) · 呼出先 11件 [`004447c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md) [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00446638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md) [`00550f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f04.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.09% / 新版 90.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446508",
      "incomplete_value": false,
      "site": "00446508",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004461e8",
      "incomplete_value": false,
      "site": "004461e8",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004465dc",
      "incomplete_value": false,
      "site": "004465dc",
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
                "const:ad8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004462bc",
      "incomplete_value": false,
      "site": "004462bc",
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
                "const:b18:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004465e0",
      "incomplete_value": false,
      "site": "004465e0",
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
                "const:ad8:8"
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
      "definition_site": "004462c0",
      "incomplete_value": false,
      "site": "004462c0",
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
                "const:b18:8"
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
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004464f8",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00446508",
      "WRITE",
      [
        "storage",
        "00ca4b30",
        null,
        "undefined4"
      ]
    ],
    [
      "004465b0",
      "PARAM",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004464f8",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "00446508",
      "WRITE",
      [
        "storage",
        "00ca5af0",
        null,
        "undefined4"
      ]
    ],
    [
      "004465b0",
      "PARAM",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004461e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md#insn-004461e8) · [`00446294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md#insn-00446294) · [`004462cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md#insn-004462cc)
- 新版 [`00446508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/0044644c.md#insn-00446508) · [`004465b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/0044644c.md#insn-004465b4) · [`004465ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/0044644c.md#insn-004465ec)

~~~diff
- 004461e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
- 004461e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 00446508 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:af0:8"]]
+ 00446508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 004461e8 bytes 20310bb9
+ 00446508 bytes 20f10ab9
- 00446294 ["INT_ADD", "register:40f0:8", ["const:446294:8", "const:4:8"]]
- 00446294 ["CALL", null, ["callee:00c58ef0:8"]]
+ 004465b4 ["INT_ADD", "register:40f0:8", ["const:4465b4:8", "const:4:8"]]
+ 004465b4 ["CALL", null, ["callee:00c58ef0:8"]]
- 00446294 bytes 23472094
+ 004465b4 bytes 4f4a2094
- 004462cc ["INT_ADD", "register:40f0:8", ["const:4462cc:8", "const:4:8"]]
- 004462cc ["CALL", null, ["callee:00c58ed0:8"]]
+ 004465ec ["INT_ADD", "register:40f0:8", ["const:4465ec:8", "const:4:8"]]
+ 004465ec ["CALL", null, ["callee:00c58ed0:8"]]
- 004462cc bytes 0d472094
+ 004465ec bytes 394a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d17fed8a8d9d7ce87c88952ceaa60892"></a>

### [`00446318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md) → [`00446638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md) FUN_00446638

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004444a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0044612c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044612c.md) [`0044673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044673c.md) · 呼出先 4件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00550c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c74.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 4件 [`004447c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md) [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`0044644c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/0044644c.md) [`00446a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446a5c.md) · 呼出先 4件 [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00550f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f94.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00446680",
      "incomplete_value": true,
      "site": "00446680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00446360",
      "incomplete_value": true,
      "site": "00446360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a02:8"
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
      "0044666c",
      "READ",
      [
        "storage",
        "002a8a02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044666c",
      "READ",
      [
        "storage",
        "002a8b5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044633c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md#insn-0044633c) · [`00446344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md#insn-00446344) · [`00446374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md#insn-00446374)
- 新版 [`0044665c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md#insn-0044665c) · [`00446664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md#insn-00446664) · [`00446694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md#insn-00446694)

~~~diff
- 0044633c ["INT_ADD", "register:40f0:8", ["const:44633c:8", "const:4:8"]]
- 0044633c ["CALL", null, ["callee:00550f94:8"]]
+ 0044665c ["INT_ADD", "register:40f0:8", ["const:44665c:8", "const:4:8"]]
+ 0044665c ["CALL", null, ["callee:00550f94:8"]]
- 0044633c bytes 4e2a0494
+ 0044665c bytes 4e2a0494
- 00446344 ["COPY", "tmp:0:8", ["const:a02:8"]]
- 00446344 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00446344 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00446344 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00446664 ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 00446664 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00446664 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00446664 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00446344 bytes 29092891
+ 00446664 bytes 29692d91
- 00446374 ["INT_ADD", "register:40f0:8", ["const:446374:8", "const:4:8"]]
- 00446374 ["CALL", null, ["callee:0043df04:8"]]
+ 00446694 ["INT_ADD", "register:40f0:8", ["const:446694:8", "const:4:8"]]
+ 00446694 ["CALL", null, ["callee:0043df04:8"]]
- 00446374 bytes 1cdeff97
+ 00446694 bytes 1cdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171baac562d59c5b7ed45927a0de0073"></a>

### [`0044673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044673c.md) → [`00446a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446a5c.md) FUN_00446a5c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00446b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446b64.md) · 呼出先 16件 [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00446318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446318.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00550c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c5c.md) [`00550c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c60.md)
- 新版 呼出元 1件 [`00446e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446e84.md) · 呼出先 16件 [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00446638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446638.md) [`0049b51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049b/0049b51c.md) [`00550f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f7c.md) [`00550f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 20件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446c20",
      "incomplete_value": false,
      "site": "00446c20",
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
                "const:ad8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00446900",
      "incomplete_value": false,
      "site": "00446900",
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
                "const:b18:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "00446c24",
      "incomplete_value": false,
      "site": "00446c24",
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
                "const:ad8:8"
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
      "definition_site": "00446904",
      "incomplete_value": false,
      "site": "00446904",
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
                "const:b18:8"
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
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446c24",
      "incomplete_value": false,
      "site": "00446c24",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00446904",
      "incomplete_value": false,
      "site": "00446904",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00446a90",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00446aa0",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00446ad8",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00446a90",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "00446aa0",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "00446ad8",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004468e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044673c.md#insn-004468e0) · [`00446910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044673c.md#insn-00446910) · [`0044691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/0044673c.md#insn-0044691c)
- 新版 [`00446c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446a5c.md#insn-00446c00) · [`00446c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446a5c.md#insn-00446c30) · [`00446c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446a5c.md#insn-00446c3c)

~~~diff
- 004468e0 ["INT_ADD", "register:40f0:8", ["const:4468e0:8", "const:4:8"]]
- 004468e0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00446c00 ["INT_ADD", "register:40f0:8", ["const:446c00:8", "const:4:8"]]
+ 00446c00 ["CALL", null, ["callee:00c58ef0:8"]]
- 004468e0 bytes 90452094
+ 00446c00 bytes bc482094
- 00446910 ["INT_ADD", "register:40f0:8", ["const:446910:8", "const:4:8"]]
- 00446910 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00446c30 ["INT_ADD", "register:40f0:8", ["const:446c30:8", "const:4:8"]]
+ 00446c30 ["CALL", null, ["callee:00c58ed0:8"]]
- 00446910 bytes 7c452094
+ 00446c30 bytes a8482094
- 0044691c ["INT_ADD", "register:40f0:8", ["const:44691c:8", "const:4:8"]]
- 0044691c ["CALL", null, ["callee:00c58f10:8"]]
+ 00446c3c ["INT_ADD", "register:40f0:8", ["const:446c3c:8", "const:4:8"]]
+ 00446c3c ["CALL", null, ["callee:00c58f10:8"]]
- 0044691c bytes 89452094
+ 00446c3c bytes b5482094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ae9a83e0fe99abd83bb16d2c621d0ba"></a>

### [`00446aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446aac.md) → [`00446dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446dcc.md) FUN_00446dcc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md) [`00c59050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59050.md) [`00c59060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.91% / 新版 73.91%

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
      "definition_site": "00446dfc",
      "incomplete_value": true,
      "site": "00446e04",
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
      "definition_site": "00446adc",
      "incomplete_value": true,
      "site": "00446ae4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00446e08",
      "incomplete_value": true,
      "site": "00446e08",
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
      "definition_site": "00446ae8",
      "incomplete_value": true,
      "site": "00446ae8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446e18",
      "incomplete_value": true,
      "site": "00446e18",
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
                "register:4000:8"
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
      "definition_site": "00446af8",
      "incomplete_value": true,
      "site": "00446af8",
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
                "register:4000:8"
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
      "00446de8",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "00446dec",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00446df8",
      "READ",
      [
        "storage",
        "00c932d0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00446de8",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ],
    [
      "00446dec",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00446df8",
      "READ",
      [
        "storage",
        "00c942a0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00446abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446aac.md#insn-00446abc) · [`00446ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446aac.md#insn-00446ac0) · [`00446ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446aac.md#insn-00446ac8)
- 新版 [`00446ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446dcc.md#insn-00446ddc) · [`00446de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446dcc.md#insn-00446de0) · [`00446de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446dcc.md#insn-00446de8)

~~~diff
- 00446abc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00446ddc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00446abc bytes a8420090
+ 00446ddc bytes a84200b0
- 00446ac0 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
+ 00446de0 ["COPY", "register:40b0:8", ["const:c9b000:8"]]
- 00446ac0 bytes b6420090
+ 00446de0 bytes b64200b0
- 00446ac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
- 00446ac8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00446de8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 00446de8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00446ac8 bytes 084146f9
+ 00446de8 bytes 082946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea1dc3aac0572d83ad41e03991f93da"></a>

### [`00446b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446b68.md) → [`00446e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446e88.md) FUN_00446e88

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00446654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446654.md) · 呼出先 6件 [`00446c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446c6c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) [`00c581e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581e0.md)
- 新版 呼出元 1件 [`00446974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446974.md) · 呼出先 6件 [`00446f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446f8c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c591a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591a0.md) [`00c591b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

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
      "definition_site": "00446eec",
      "incomplete_value": false,
      "site": "00446ef8",
      "value": [
        "leaf",
        "const:446f8c:8"
      ]
    },
    "old": {
      "definition_site": "00446bcc",
      "incomplete_value": false,
      "site": "00446bd8",
      "value": [
        "leaf",
        "const:446c6c:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446f3c",
      "incomplete_value": false,
      "site": "00446f40",
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
            "const:fa5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00446c1c",
      "incomplete_value": false,
      "site": "00446c20",
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
            "const:eda:8"
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
      "00446eec",
      "PARAM",
      [
        "storage",
        "00446c6c",
        null,
        null
      ]
    ],
    [
      "00446f3c",
      "PARAM",
      [
        "storage",
        "002a3eda",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00446eec",
      "PARAM",
      [
        "storage",
        "00446f8c",
        null,
        null
      ]
    ],
    [
      "00446f3c",
      "PARAM",
      [
        "storage",
        "002a3fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00446bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446b68.md#insn-00446bd8) · [`00446c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446b68.md#insn-00446c20) · [`00446b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446b68.md#insn-00446b9c)
- 新版 [`00446ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446e88.md#insn-00446ef8) · [`00446f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446e88.md#insn-00446f40) · [`00446ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446e88.md#insn-00446ebc)

~~~diff
- 00446bd8 ["INT_ADD", "register:40f0:8", ["const:446bd8:8", "const:4:8"]]
- 00446bd8 ["CALL", null, ["callee:00c591b0:8"]]
+ 00446ef8 ["INT_ADD", "register:40f0:8", ["const:446ef8:8", "const:4:8"]]
+ 00446ef8 ["CALL", null, ["callee:00c591b0:8"]]
- 00446bd8 bytes 82452094
+ 00446ef8 bytes ae482094
- 00446c20 ["INT_ADD", "register:40f0:8", ["const:446c20:8", "const:4:8"]]
- 00446c20 ["CALL", null, ["callee:00c591c0:8"]]
+ 00446f40 ["INT_ADD", "register:40f0:8", ["const:446f40:8", "const:4:8"]]
+ 00446f40 ["CALL", null, ["callee:00c591c0:8"]]
- 00446c20 bytes 74452094
+ 00446f40 bytes a0482094
- 00446b9c ["INT_ADD", "register:40f0:8", ["const:446b9c:8", "const:4:8"]]
- 00446b9c ["CALL", null, ["callee:00c58f30:8"]]
+ 00446ebc ["INT_ADD", "register:40f0:8", ["const:446ebc:8", "const:4:8"]]
+ 00446ebc ["CALL", null, ["callee:00c58f30:8"]]
- 00446b9c bytes f1442094
+ 00446ebc bytes 1d482094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ceb967bb389402d03af9c0f77ebd4e3"></a>

### [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) → [`00447120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md) FUN_00447120

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`00447120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md) · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

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
      "definition_site": "00447274",
      "incomplete_value": false,
      "site": "0044727c",
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
      "definition_site": "00446f54",
      "incomplete_value": false,
      "site": "00446f5c",
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
      "definition_site": "00447330",
      "incomplete_value": false,
      "site": "00447338",
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
      "definition_site": "00447010",
      "incomplete_value": false,
      "site": "00447018",
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
      "definition_site": "00447348",
      "incomplete_value": false,
      "site": "00447354",
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
      "definition_site": "00447028",
      "incomplete_value": false,
      "site": "00447034",
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
      "00447274",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00447330",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00447348",
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
      "00447274",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00447330",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "00447348",
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

- 旧版 [`00446f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md#insn-00446f5c) · [`00447018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md#insn-00447018) · [`00447034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md#insn-00447034)
- 新版 [`0044727c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md#insn-0044727c) · [`00447338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md#insn-00447338) · [`00447354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md#insn-00447354)

~~~diff
- 00446f5c ["INT_ADD", "register:40f0:8", ["const:446f5c:8", "const:4:8"]]
- 00446f5c ["CALL", null, ["callee:004421f4:8"]]
+ 0044727c ["INT_ADD", "register:40f0:8", ["const:44727c:8", "const:4:8"]]
+ 0044727c ["CALL", null, ["callee:004421f4:8"]]
- 00446f5c bytes deebff97
+ 0044727c bytes deebff97
- 00447018 ["INT_ADD", "register:40f0:8", ["const:447018:8", "const:4:8"]]
- 00447018 ["CALL", null, ["callee:004421f4:8"]]
+ 00447338 ["INT_ADD", "register:40f0:8", ["const:447338:8", "const:4:8"]]
+ 00447338 ["CALL", null, ["callee:004421f4:8"]]
- 00447018 bytes afebff97
+ 00447338 bytes afebff97
- 00447034 ["INT_ADD", "register:40f0:8", ["const:447034:8", "const:4:8"]]
- 00447034 ["CALL", null, ["callee:00442b54:8"]]
+ 00447354 ["INT_ADD", "register:40f0:8", ["const:447354:8", "const:4:8"]]
+ 00447354 ["CALL", null, ["callee:00442b54:8"]]
- 00447034 bytes 00eeff97
+ 00447354 bytes 00eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54503f1c01e82668c4c727ac16801f06"></a>

### [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) → [`00447a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md) FUN_00447a54

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 27件 [`00446e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446e00.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00449068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449068.md) [`00449a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 27件 [`00447120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447120.md) [`00447a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md) [`00449388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449388.md) [`00449d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md) [`005e3504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e3/005e3504.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00447ba8",
      "incomplete_value": false,
      "site": "00447bb0",
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
      "definition_site": "00447888",
      "incomplete_value": false,
      "site": "00447890",
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
      "definition_site": "00447bcc",
      "incomplete_value": false,
      "site": "00447bd8",
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
      "definition_site": "004478ac",
      "incomplete_value": false,
      "site": "004478b8",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00447d00",
      "incomplete_value": false,
      "site": "00447d08",
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
      "definition_site": "004479e0",
      "incomplete_value": false,
      "site": "004479e8",
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
      "00447ba8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00447bcc",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00447d00",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00447ba8",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00447bcc",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "00447d00",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00447890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md#insn-00447890) · [`004478b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md#insn-004478b8) · [`004479e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md#insn-004479e8)
- 新版 [`00447bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md#insn-00447bb0) · [`00447bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md#insn-00447bd8) · [`00447d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md#insn-00447d08)

~~~diff
- 00447890 ["INT_ADD", "register:40f0:8", ["const:447890:8", "const:4:8"]]
- 00447890 ["CALL", null, ["callee:004421f4:8"]]
+ 00447bb0 ["INT_ADD", "register:40f0:8", ["const:447bb0:8", "const:4:8"]]
+ 00447bb0 ["CALL", null, ["callee:004421f4:8"]]
- 00447890 bytes 91e9ff97
+ 00447bb0 bytes 91e9ff97
- 004478b8 ["INT_ADD", "register:40f0:8", ["const:4478b8:8", "const:4:8"]]
- 004478b8 ["CALL", null, ["callee:00442b54:8"]]
+ 00447bd8 ["INT_ADD", "register:40f0:8", ["const:447bd8:8", "const:4:8"]]
+ 00447bd8 ["CALL", null, ["callee:00442b54:8"]]
- 004478b8 bytes dfebff97
+ 00447bd8 bytes dfebff97
- 004479e8 ["INT_ADD", "register:40f0:8", ["const:4479e8:8", "const:4:8"]]
- 004479e8 ["CALL", null, ["callee:004421f4:8"]]
+ 00447d08 ["INT_ADD", "register:40f0:8", ["const:447d08:8", "const:4:8"]]
+ 00447d08 ["CALL", null, ["callee:004421f4:8"]]
- 004479e8 bytes 3be9ff97
+ 00447d08 bytes 3be9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2a079faaa529c5d62f083588f03652"></a>

### [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) → [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) FUN_00448254

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 178件 [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047b88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b88c.md) [`005c429c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 178件 [`00447a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047bbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047bbac.md) [`005c464c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c464c.md) [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004483a4",
      "incomplete_value": false,
      "site": "004483ac",
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
      "definition_site": "00448084",
      "incomplete_value": false,
      "site": "0044808c",
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
      "definition_site": "004483c8",
      "incomplete_value": false,
      "site": "004483d4",
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
      "definition_site": "004480a8",
      "incomplete_value": false,
      "site": "004480b4",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004484fc",
      "incomplete_value": false,
      "site": "00448504",
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
      "definition_site": "004481dc",
      "incomplete_value": false,
      "site": "004481e4",
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
      "004483a4",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "004483c8",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "004484fc",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004483a4",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "004483c8",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "004484fc",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044808c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md#insn-0044808c) · [`004480b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md#insn-004480b4) · [`004481e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md#insn-004481e4)
- 新版 [`004483ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md#insn-004483ac) · [`004483d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md#insn-004483d4) · [`00448504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md#insn-00448504)

~~~diff
- 0044808c ["INT_ADD", "register:40f0:8", ["const:44808c:8", "const:4:8"]]
- 0044808c ["CALL", null, ["callee:004421f4:8"]]
+ 004483ac ["INT_ADD", "register:40f0:8", ["const:4483ac:8", "const:4:8"]]
+ 004483ac ["CALL", null, ["callee:004421f4:8"]]
- 0044808c bytes 92e7ff97
+ 004483ac bytes 92e7ff97
- 004480b4 ["INT_ADD", "register:40f0:8", ["const:4480b4:8", "const:4:8"]]
- 004480b4 ["CALL", null, ["callee:00442b54:8"]]
+ 004483d4 ["INT_ADD", "register:40f0:8", ["const:4483d4:8", "const:4:8"]]
+ 004483d4 ["CALL", null, ["callee:00442b54:8"]]
- 004480b4 bytes e0e9ff97
+ 004483d4 bytes e0e9ff97
- 004481e4 ["INT_ADD", "register:40f0:8", ["const:4481e4:8", "const:4:8"]]
- 004481e4 ["CALL", null, ["callee:004421f4:8"]]
+ 00448504 ["INT_ADD", "register:40f0:8", ["const:448504:8", "const:4:8"]]
+ 00448504 ["CALL", null, ["callee:004421f4:8"]]
- 004481e4 bytes 3ce7ff97
+ 00448504 bytes 3ce7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5820614c81644a0bb494244712e0db5f"></a>

### [`00448720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00448/00448720.md) → [`00448a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448a40.md) FUN_00448a40

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00448720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00448/00448720.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`00448a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448a40.md) · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00448b98",
      "incomplete_value": false,
      "site": "00448ba0",
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
      "definition_site": "00448878",
      "incomplete_value": false,
      "site": "00448880",
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
      "definition_site": "00448c54",
      "incomplete_value": false,
      "site": "00448c5c",
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
      "definition_site": "00448934",
      "incomplete_value": false,
      "site": "0044893c",
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
      "definition_site": "00448c6c",
      "incomplete_value": false,
      "site": "00448c78",
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
      "definition_site": "0044894c",
      "incomplete_value": false,
      "site": "00448958",
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
      "00448b98",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00448c54",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00448c6c",
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
      "00448b98",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00448c54",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "00448c6c",
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

- 旧版 [`00448880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00448/00448720.md#insn-00448880) · [`0044893c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00448/00448720.md#insn-0044893c) · [`00448958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00448/00448720.md#insn-00448958)
- 新版 [`00448ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448a40.md#insn-00448ba0) · [`00448c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448a40.md#insn-00448c5c) · [`00448c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448a40.md#insn-00448c78)

~~~diff
- 00448880 ["INT_ADD", "register:40f0:8", ["const:448880:8", "const:4:8"]]
- 00448880 ["CALL", null, ["callee:004421f4:8"]]
+ 00448ba0 ["INT_ADD", "register:40f0:8", ["const:448ba0:8", "const:4:8"]]
+ 00448ba0 ["CALL", null, ["callee:004421f4:8"]]
- 00448880 bytes 95e5ff97
+ 00448ba0 bytes 95e5ff97
- 0044893c ["INT_ADD", "register:40f0:8", ["const:44893c:8", "const:4:8"]]
- 0044893c ["CALL", null, ["callee:004421f4:8"]]
+ 00448c5c ["INT_ADD", "register:40f0:8", ["const:448c5c:8", "const:4:8"]]
+ 00448c5c ["CALL", null, ["callee:004421f4:8"]]
- 0044893c bytes 66e5ff97
+ 00448c5c bytes 66e5ff97
- 00448958 ["INT_ADD", "register:40f0:8", ["const:448958:8", "const:4:8"]]
- 00448958 ["CALL", null, ["callee:00442b54:8"]]
+ 00448c78 ["INT_ADD", "register:40f0:8", ["const:448c78:8", "const:4:8"]]
+ 00448c78 ["CALL", null, ["callee:00442b54:8"]]
- 00448958 bytes b7e7ff97
+ 00448c78 bytes b7e7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed71f975d598a9946938c78813482765"></a>

### [`00449068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449068.md) → [`00449388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449388.md) FUN_00449388

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00448720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00448/00448720.md) [`00449068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449068.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`00620470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620470.md) [`00622ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/00622ea0.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 10件 [`00448a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448a40.md) [`00449388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449388.md) [`005e3504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e3/005e3504.md) [`00620820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00620/00620820.md) [`00623250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00623/00623250.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004494e0",
      "incomplete_value": false,
      "site": "004494e8",
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
      "definition_site": "004491c0",
      "incomplete_value": false,
      "site": "004491c8",
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
      "definition_site": "00449504",
      "incomplete_value": false,
      "site": "00449510",
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
      "definition_site": "004491e4",
      "incomplete_value": false,
      "site": "004491f0",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449638",
      "incomplete_value": false,
      "site": "00449640",
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
      "definition_site": "00449318",
      "incomplete_value": false,
      "site": "00449320",
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
      "004494e0",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00449504",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00449638",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004494e0",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00449504",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "00449638",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004491c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449068.md#insn-004491c8) · [`004491f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449068.md#insn-004491f0) · [`00449320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449068.md#insn-00449320)
- 新版 [`004494e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449388.md#insn-004494e8) · [`00449510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449388.md#insn-00449510) · [`00449640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449388.md#insn-00449640)

~~~diff
- 004491c8 ["INT_ADD", "register:40f0:8", ["const:4491c8:8", "const:4:8"]]
- 004491c8 ["CALL", null, ["callee:004421f4:8"]]
+ 004494e8 ["INT_ADD", "register:40f0:8", ["const:4494e8:8", "const:4:8"]]
+ 004494e8 ["CALL", null, ["callee:004421f4:8"]]
- 004491c8 bytes 43e3ff97
+ 004494e8 bytes 43e3ff97
- 004491f0 ["INT_ADD", "register:40f0:8", ["const:4491f0:8", "const:4:8"]]
- 004491f0 ["CALL", null, ["callee:00442b54:8"]]
+ 00449510 ["INT_ADD", "register:40f0:8", ["const:449510:8", "const:4:8"]]
+ 00449510 ["CALL", null, ["callee:00442b54:8"]]
- 004491f0 bytes 91e5ff97
+ 00449510 bytes 91e5ff97
- 00449320 ["INT_ADD", "register:40f0:8", ["const:449320:8", "const:4:8"]]
- 00449320 ["CALL", null, ["callee:004421f4:8"]]
+ 00449640 ["INT_ADD", "register:40f0:8", ["const:449640:8", "const:4:8"]]
+ 00449640 ["CALL", null, ["callee:004421f4:8"]]
- 00449320 bytes ede2ff97
+ 00449640 bytes ede2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae6654b7fc7975a75c14921a2cbd97ad"></a>

### [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) → [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) FUN_00449d18

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0044986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/0044986c.md) [`004e5ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e5/004e5ea0.md) [`005d17e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d17e4.md) [`005d455c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d455c.md) [`00768dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768dbc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 8件 [`00449b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449b8c.md) [`004e61c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004e6/004e61c0.md) [`005d1b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1b94.md) [`005d490c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d490c.md) [`00769198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769198.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00449d24",
      "incomplete_value": false,
      "site": "00449d28",
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
      "definition_site": "00449a04",
      "incomplete_value": false,
      "site": "00449a08",
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
      "00449d24",
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
      "00449d24",
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

- 旧版 [`00449a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md#insn-00449a08) · [`00449a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md#insn-00449a00) · [`00449a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md#insn-00449a04)
- 新版 [`00449d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md#insn-00449d28) · [`00449d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md#insn-00449d20) · [`00449d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md#insn-00449d24)

~~~diff
- 00449a08 ["INT_ADD", "register:40f0:8", ["const:449a08:8", "const:4:8"]]
- 00449a08 ["CALL", null, ["callee:0043bad8:8"]]
+ 00449d28 ["INT_ADD", "register:40f0:8", ["const:449d28:8", "const:4:8"]]
+ 00449d28 ["CALL", null, ["callee:0043bad8:8"]]
- 00449a08 bytes 6cc7ff97
+ 00449d28 bytes 6cc7ff97
- 00449a00 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00449d20 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00449a00 bytes 60f3ffd0
+ 00449d20 bytes 60f3fff0
- 00449a04 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00449a04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00449a04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00449a04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00449d24 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00449d24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00449d24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00449d24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00449a04 bytes 00303e91
+ 00449d24 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fd51e703ac704c2244b5bc06617e36a"></a>

### [`00449a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md) → [`00449d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md) FUN_00449d2c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00449a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md) [`0048f4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f4a0.md) [`005dbd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005db/005dbd54.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 4件 [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`00449d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md) [`0048f7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f7c0.md) [`005dc104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005dc/005dc104.md) · 呼出先 21件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449e98",
      "incomplete_value": false,
      "site": "00449ea0",
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
      "definition_site": "00449b78",
      "incomplete_value": false,
      "site": "00449b80",
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
      "definition_site": "00449f58",
      "incomplete_value": false,
      "site": "00449f60",
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
      "definition_site": "00449c38",
      "incomplete_value": false,
      "site": "00449c40",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449f74",
      "incomplete_value": false,
      "site": "00449f80",
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
      "definition_site": "00449c54",
      "incomplete_value": false,
      "site": "00449c60",
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
      "00449e98",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00449f58",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00449f74",
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
      "00449e98",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "00449f58",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "00449f74",
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

- 旧版 [`00449b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md#insn-00449b80) · [`00449c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md#insn-00449c40) · [`00449c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/00449a0c.md#insn-00449c60)
- 新版 [`00449ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md#insn-00449ea0) · [`00449f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md#insn-00449f60) · [`00449f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d2c.md#insn-00449f80)

~~~diff
- 00449b80 ["INT_ADD", "register:40f0:8", ["const:449b80:8", "const:4:8"]]
- 00449b80 ["CALL", null, ["callee:004421f4:8"]]
+ 00449ea0 ["INT_ADD", "register:40f0:8", ["const:449ea0:8", "const:4:8"]]
+ 00449ea0 ["CALL", null, ["callee:004421f4:8"]]
- 00449b80 bytes d5e0ff97
+ 00449ea0 bytes d5e0ff97
- 00449c40 ["INT_ADD", "register:40f0:8", ["const:449c40:8", "const:4:8"]]
- 00449c40 ["CALL", null, ["callee:004421f4:8"]]
+ 00449f60 ["INT_ADD", "register:40f0:8", ["const:449f60:8", "const:4:8"]]
+ 00449f60 ["CALL", null, ["callee:004421f4:8"]]
- 00449c40 bytes a5e0ff97
+ 00449f60 bytes a5e0ff97
- 00449c60 ["INT_ADD", "register:40f0:8", ["const:449c60:8", "const:4:8"]]
- 00449c60 ["CALL", null, ["callee:00442b54:8"]]
+ 00449f80 ["INT_ADD", "register:40f0:8", ["const:449f80:8", "const:4:8"]]
+ 00449f80 ["CALL", null, ["callee:00442b54:8"]]
- 00449c60 bytes f5e2ff97
+ 00449f80 bytes f5e2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3cd82a12293efcde82d7786a32a6a9b"></a>

### [`0044a2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044a2f8.md) → [`0044a618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044a618.md) FUN_0044a618

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0044a2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044a2f8.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`0044a618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044a618.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044a768",
      "incomplete_value": false,
      "site": "0044a770",
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
      "definition_site": "0044a448",
      "incomplete_value": false,
      "site": "0044a450",
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
      "definition_site": "0044a78c",
      "incomplete_value": false,
      "site": "0044a798",
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
      "definition_site": "0044a46c",
      "incomplete_value": false,
      "site": "0044a478",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044a8c0",
      "incomplete_value": false,
      "site": "0044a8c8",
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
      "definition_site": "0044a5a0",
      "incomplete_value": false,
      "site": "0044a5a8",
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
      "0044a768",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0044a78c",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "0044a8c0",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044a768",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "0044a78c",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "0044a8c0",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044a450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044a2f8.md#insn-0044a450) · [`0044a478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044a2f8.md#insn-0044a478) · [`0044a5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044a2f8.md#insn-0044a5a8)
- 新版 [`0044a770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044a618.md#insn-0044a770) · [`0044a798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044a618.md#insn-0044a798) · [`0044a8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044a618.md#insn-0044a8c8)

~~~diff
- 0044a450 ["INT_ADD", "register:40f0:8", ["const:44a450:8", "const:4:8"]]
- 0044a450 ["CALL", null, ["callee:004421f4:8"]]
+ 0044a770 ["INT_ADD", "register:40f0:8", ["const:44a770:8", "const:4:8"]]
+ 0044a770 ["CALL", null, ["callee:004421f4:8"]]
- 0044a450 bytes a1deff97
+ 0044a770 bytes a1deff97
- 0044a478 ["INT_ADD", "register:40f0:8", ["const:44a478:8", "const:4:8"]]
- 0044a478 ["CALL", null, ["callee:00442b54:8"]]
+ 0044a798 ["INT_ADD", "register:40f0:8", ["const:44a798:8", "const:4:8"]]
+ 0044a798 ["CALL", null, ["callee:00442b54:8"]]
- 0044a478 bytes efe0ff97
+ 0044a798 bytes efe0ff97
- 0044a5a8 ["INT_ADD", "register:40f0:8", ["const:44a5a8:8", "const:4:8"]]
- 0044a5a8 ["CALL", null, ["callee:004421f4:8"]]
+ 0044a8c8 ["INT_ADD", "register:40f0:8", ["const:44a8c8:8", "const:4:8"]]
+ 0044a8c8 ["CALL", null, ["callee:004421f4:8"]]
- 0044a5a8 bytes 4bdeff97
+ 0044a8c8 bytes 4bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b74fabbad58af95eabc1b40db0f4b0"></a>

### [`0044aae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044aae8.md) → [`0044ae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae08.md) FUN_0044ae08

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0044ae1c",
      "incomplete_value": false,
      "site": "0044ae20",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044aafc",
      "incomplete_value": false,
      "site": "0044ab00",
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
            "const:6a0:8"
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
      "0044ae20",
      "DATA",
      [
        "storage",
        "00c636a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044ae20",
      "DATA",
      [
        "storage",
        "00c64670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044aaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044aae8.md#insn-0044aaf4) · [`0044aaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044aae8.md#insn-0044aaf8) · [`0044aafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044aae8.md#insn-0044aafc)
- 新版 [`0044ae14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae08.md#insn-0044ae14) · [`0044ae18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae08.md#insn-0044ae18) · [`0044ae1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae08.md#insn-0044ae1c)

~~~diff
- 0044aaf4 ["INT_ADD", "register:40f0:8", ["const:44aaf4:8", "const:4:8"]]
- 0044aaf4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044ae14 ["INT_ADD", "register:40f0:8", ["const:44ae14:8", "const:4:8"]]
+ 0044ae14 ["CALL", null, ["callee:00c58f30:8"]]
- 0044aaf4 bytes 1b352094
+ 0044ae14 bytes 47382094
- 0044aaf8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044ae18 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044aaf8 bytes c84000b0
+ 0044ae18 bytes c84000d0
- 0044aafc ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0044aafc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044aafc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044aafc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044ae1c ["COPY", "tmp:0:8", ["const:670:8"]]
+ 0044ae1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ae1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ae1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044aafc bytes 08811a91
+ 0044ae1c bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7137a1be74fc5010548bfe7c27e6546b"></a>

### [`0044ab54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab54.md) → [`0044ae74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae74.md) FUN_0044ae74

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0044ae88",
      "incomplete_value": false,
      "site": "0044ae8c",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ab68",
      "incomplete_value": false,
      "site": "0044ab6c",
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
            "const:720:8"
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
      "0044ae8c",
      "DATA",
      [
        "storage",
        "00c63720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044ae8c",
      "DATA",
      [
        "storage",
        "00c646f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab54.md#insn-0044ab60) · [`0044ab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab54.md#insn-0044ab64) · [`0044ab68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab54.md#insn-0044ab68)
- 新版 [`0044ae80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae74.md#insn-0044ae80) · [`0044ae84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae74.md#insn-0044ae84) · [`0044ae88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044ae74.md#insn-0044ae88)

~~~diff
- 0044ab60 ["INT_ADD", "register:40f0:8", ["const:44ab60:8", "const:4:8"]]
- 0044ab60 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044ae80 ["INT_ADD", "register:40f0:8", ["const:44ae80:8", "const:4:8"]]
+ 0044ae80 ["CALL", null, ["callee:00c58f30:8"]]
- 0044ab60 bytes 00352094
+ 0044ae80 bytes 2c382094
- 0044ab64 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044ae84 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044ab64 bytes c84000b0
+ 0044ae84 bytes c84000d0
- 0044ab68 ["COPY", "tmp:0:8", ["const:720:8"]]
- 0044ab68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044ab68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044ab68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044ae88 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 0044ae88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ae88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ae88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044ab68 bytes 08811c91
+ 0044ae88 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad46dc9667e9506a6bf4c9a002fcc5e"></a>

### [`0044abc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044abc4.md) → [`0044aee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044aee4.md) FUN_0044aee4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0044aef8",
      "incomplete_value": false,
      "site": "0044aefc",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044abd8",
      "incomplete_value": false,
      "site": "0044abdc",
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
            "const:7a0:8"
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
      "0044aefc",
      "DATA",
      [
        "storage",
        "00c637a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044aefc",
      "DATA",
      [
        "storage",
        "00c64770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044abc4.md#insn-0044abd0) · [`0044abd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044abc4.md#insn-0044abd4) · [`0044abd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044abc4.md#insn-0044abd8)
- 新版 [`0044aef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044aee4.md#insn-0044aef0) · [`0044aef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044aee4.md#insn-0044aef4) · [`0044aef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044aee4.md#insn-0044aef8)

~~~diff
- 0044abd0 ["INT_ADD", "register:40f0:8", ["const:44abd0:8", "const:4:8"]]
- 0044abd0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044aef0 ["INT_ADD", "register:40f0:8", ["const:44aef0:8", "const:4:8"]]
+ 0044aef0 ["CALL", null, ["callee:00c58f30:8"]]
- 0044abd0 bytes e4342094
+ 0044aef0 bytes 10382094
- 0044abd4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0044aef4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0044abd4 bytes c84000b0
+ 0044aef4 bytes c84000d0
- 0044abd8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 0044abd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044abd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044abd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044aef8 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 0044aef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044abd8 bytes 08811e91
+ 0044aef8 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34b4b30211f7f93888dc0e68be2af657"></a>

### [`0044ac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ac00.md) → [`0044af20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044af20.md) FUN_0044af20

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00444194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444194.md) [`004444a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004444a4.md) [`00444654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444654.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004444b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004444b4.md) [`004447c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004447c4.md) [`00444974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444974.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044af7c",
      "incomplete_value": false,
      "site": "0044af7c",
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
                "const:ad8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ac5c",
      "incomplete_value": false,
      "site": "0044ac5c",
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
                "const:b18:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "0044af80",
      "incomplete_value": false,
      "site": "0044af80",
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
                "const:ad8:8"
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
      "definition_site": "0044ac60",
      "incomplete_value": false,
      "site": "0044ac60",
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
                "const:b18:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044af80",
      "incomplete_value": false,
      "site": "0044af80",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ac60",
      "incomplete_value": false,
      "site": "0044ac60",
      "value": [
        "INT_ADD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044af3c",
      "READ",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ],
    [
      "0044af48",
      "PARAM",
      [
        "storage",
        "00ca4b18",
        null,
        "undefined8"
      ]
    ],
    [
      "0044af58",
      "PARAM",
      [
        "storage",
        "00ca4b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044af3c",
      "READ",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ],
    [
      "0044af48",
      "PARAM",
      [
        "storage",
        "00ca5ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "0044af58",
      "PARAM",
      [
        "storage",
        "00ca5b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ac3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ac00.md#insn-0044ac3c) · [`0044ac6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ac00.md#insn-0044ac6c) · [`0044ac78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ac00.md#insn-0044ac78)
- 新版 [`0044af5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044af20.md#insn-0044af5c) · [`0044af8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044af20.md#insn-0044af8c) · [`0044af98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044a/0044af20.md#insn-0044af98)

~~~diff
- 0044ac3c ["INT_ADD", "register:40f0:8", ["const:44ac3c:8", "const:4:8"]]
- 0044ac3c ["CALL", null, ["callee:00c58ef0:8"]]
+ 0044af5c ["INT_ADD", "register:40f0:8", ["const:44af5c:8", "const:4:8"]]
+ 0044af5c ["CALL", null, ["callee:00c58ef0:8"]]
- 0044ac3c bytes b9342094
+ 0044af5c bytes e5372094
- 0044ac6c ["INT_ADD", "register:40f0:8", ["const:44ac6c:8", "const:4:8"]]
- 0044ac6c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0044af8c ["INT_ADD", "register:40f0:8", ["const:44af8c:8", "const:4:8"]]
+ 0044af8c ["CALL", null, ["callee:00c58ed0:8"]]
- 0044ac6c bytes a5342094
+ 0044af8c bytes d1372094
- 0044ac78 ["INT_ADD", "register:40f0:8", ["const:44ac78:8", "const:4:8"]]
- 0044ac78 ["CALL", null, ["callee:00c58f10:8"]]
+ 0044af98 ["INT_ADD", "register:40f0:8", ["const:44af98:8", "const:4:8"]]
+ 0044af98 ["CALL", null, ["callee:00c58f10:8"]]
- 0044ac78 bytes b2342094
+ 0044af98 bytes de372094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f5d72560a28ad0c92a9babf531fcce"></a>

### [`0044ae10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ae10.md) → [`0044b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b130.md) _INIT_9

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
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
      "definition_site": "0044b16c",
      "incomplete_value": true,
      "site": "0044b188",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044ae4c",
      "incomplete_value": true,
      "site": "0044ae68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044b190",
      "incomplete_value": true,
      "site": "0044b1ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044ae70",
      "incomplete_value": true,
      "site": "0044ae8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044b1b0",
      "incomplete_value": true,
      "site": "0044b1cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044ae90",
      "incomplete_value": true,
      "site": "0044aeac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0044b16c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0044b190",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0044b1b0",
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
      "0044b16c",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0044b190",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0044b1b0",
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

- 旧版 [`0044af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ae10.md#insn-0044af70) · [`0044b044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ae10.md#insn-0044b044) · [`0044ae38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ae10.md#insn-0044ae38)
- 新版 [`0044b290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b130.md#insn-0044b290) · [`0044b364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b130.md#insn-0044b364) · [`0044b158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b130.md#insn-0044b158)

~~~diff
- 0044af70 ["INT_ADD", "register:40f0:8", ["const:44af70:8", "const:4:8"]]
- 0044af70 ["CALL", null, ["callee:0043bb58:8"]]
+ 0044b290 ["INT_ADD", "register:40f0:8", ["const:44b290:8", "const:4:8"]]
+ 0044b290 ["CALL", null, ["callee:0043bb58:8"]]
- 0044af70 bytes 32c2ff97
+ 0044b290 bytes 32c2ff97
- 0044b044 ["INT_ADD", "register:40f0:8", ["const:44b044:8", "const:4:8"]]
- 0044b044 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0044b364 ["INT_ADD", "register:40f0:8", ["const:44b364:8", "const:4:8"]]
+ 0044b364 ["CALL", null, ["callee:00c58ed0:8"]]
- 0044b044 bytes af332094
+ 0044b364 bytes db362094
- 0044ae38 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 0044b158 ["COPY", "register:4098:8", ["const:ca5000:8"]]
- 0044ae38 bytes d34200d0
+ 0044b158 bytes d34200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602bff4a9b16bd7fdc01cc0f62a195d7"></a>

### [`0044b1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1a0.md) → [`0044b4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b4c0.md) FUN_0044b4c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`004504e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/004504e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b4cc",
      "incomplete_value": true,
      "site": "0044b4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b1ac",
      "incomplete_value": true,
      "site": "0044b1bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d9:8"
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
      "definition_site": "0044b4e0",
      "incomplete_value": true,
      "site": "0044b4e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044b1c0",
      "incomplete_value": true,
      "site": "0044b1c0",
      "value": [
        "LOAD",
        "8",
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
      "0044b4cc",
      "READ",
      [
        "storage",
        "002bd6d9",
        null,
        "string"
      ]
    ],
    [
      "0044b4d4",
      "READ",
      [
        "storage",
        "002bd6e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b4cc",
      "READ",
      [
        "storage",
        "002bd7b7",
        null,
        "string"
      ]
    ],
    [
      "0044b4d4",
      "READ",
      [
        "storage",
        "002bd7c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1a0.md#insn-0044b1a8)
- 新版 [`0044b4c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b4c0.md#insn-0044b4c8)

~~~diff
- 0044b1a8 ["COPY", "tmp:0:8", ["const:6d9:8"]]
- 0044b1a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0044b1a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0044b1a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0044b4c8 ["COPY", "tmp:0:8", ["const:7b7:8"]]
+ 0044b4c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0044b4c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0044b4c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0044b1a8 bytes 4a651b91
+ 0044b4c8 bytes 4add1e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6029c46a8597bbbd1de310943dc50956"></a>

### [`0044b1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1c8.md) → [`0044b4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b4e8.md) FUN_0044b4e8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0062b754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062b/0062b754.md) [`0062ed3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062e/0062ed3c.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 5件 [`0062bb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062b/0062bb04.md) [`0062f0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062f/0062f0ec.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b510",
      "incomplete_value": true,
      "site": "0044b520",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c24:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b1f0",
      "incomplete_value": true,
      "site": "0044b200",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b46:8"
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
      "definition_site": "0044b524",
      "incomplete_value": true,
      "site": "0044b524",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044b204",
      "incomplete_value": true,
      "site": "0044b204",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b530",
      "incomplete_value": false,
      "site": "0044b538",
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
            "const:dc9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b210",
      "incomplete_value": false,
      "site": "0044b218",
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
            "const:d89:8"
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
      "0044b510",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044b518",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044b530",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b510",
      "READ",
      [
        "storage",
        "002bfc24",
        null,
        "string"
      ]
    ],
    [
      "0044b518",
      "READ",
      [
        "storage",
        "002bfc32",
        null,
        "string"
      ]
    ],
    [
      "0044b530",
      "PARAM",
      [
        "storage",
        "002a1dc9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1c8.md#insn-0044b218) · [`0044b1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1c8.md#insn-0044b1e4) · [`0044b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1c8.md#insn-0044b210)
- 新版 [`0044b538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b4e8.md#insn-0044b538) · [`0044b504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b4e8.md#insn-0044b504) · [`0044b530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b4e8.md#insn-0044b530)

~~~diff
- 0044b218 ["INT_ADD", "register:40f0:8", ["const:44b218:8", "const:4:8"]]
- 0044b218 ["CALL", null, ["callee:00c59010:8"]]
+ 0044b538 ["INT_ADD", "register:40f0:8", ["const:44b538:8", "const:4:8"]]
+ 0044b538 ["CALL", null, ["callee:00c59010:8"]]
- 0044b218 bytes 8a332094
+ 0044b538 bytes b6362094
- 0044b1e4 ["COPY", "tmp:0:8", ["const:b46:8"]]
- 0044b1e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0044b1e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0044b1e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0044b504 ["COPY", "tmp:0:8", ["const:c24:8"]]
+ 0044b504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0044b1e4 bytes 29192d91
+ 0044b504 bytes 29913091
- 0044b210 ["COPY", "tmp:0:8", ["const:d89:8"]]
- 0044b210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044b210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044b210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044b530 ["COPY", "tmp:0:8", ["const:dc9:8"]]
+ 0044b530 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044b530 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044b530 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044b210 bytes 21243691
+ 0044b530 bytes 21243791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebeb8a9ff6e9f4851ebf6a97b401b206"></a>

### [`0044b294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b294.md) → [`0044b5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b5b4.md) FUN_0044b5b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0044c814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0089b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b2e4.md) · 呼出先 5件 [`0059765c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059765c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`0044cb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044c/0044cb34.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`0089c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c290.md) · 呼出先 5件 [`0059797c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059797c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b5e0",
      "incomplete_value": true,
      "site": "0044b5f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c24:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b2c0",
      "incomplete_value": true,
      "site": "0044b2d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b46:8"
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
      "definition_site": "0044b5f4",
      "incomplete_value": true,
      "site": "0044b5f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0044b2d4",
      "incomplete_value": true,
      "site": "0044b2d4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b600",
      "incomplete_value": false,
      "site": "0044b608",
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
            "const:65:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b2e0",
      "incomplete_value": false,
      "site": "0044b2e8",
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
            "const:f96:8"
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
      "0044b5e0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044b5e8",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044b600",
      "PARAM",
      [
        "storage",
        "002b7f96",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b5e0",
      "READ",
      [
        "storage",
        "002bfc24",
        null,
        "string"
      ]
    ],
    [
      "0044b5e8",
      "READ",
      [
        "storage",
        "002bfc32",
        null,
        "string"
      ]
    ],
    [
      "0044b600",
      "PARAM",
      [
        "storage",
        "002b8065",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b294.md#insn-0044b2e8) · [`0044b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b294.md#insn-0044b2b4) · [`0044b2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b294.md#insn-0044b2dc)
- 新版 [`0044b608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b5b4.md#insn-0044b608) · [`0044b5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b5b4.md#insn-0044b5d4) · [`0044b5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b5b4.md#insn-0044b5fc)

~~~diff
- 0044b2e8 ["INT_ADD", "register:40f0:8", ["const:44b2e8:8", "const:4:8"]]
- 0044b2e8 ["CALL", null, ["callee:00c59010:8"]]
+ 0044b608 ["INT_ADD", "register:40f0:8", ["const:44b608:8", "const:4:8"]]
+ 0044b608 ["CALL", null, ["callee:00c59010:8"]]
- 0044b2e8 bytes 56332094
+ 0044b608 bytes 82362094
- 0044b2b4 ["COPY", "tmp:0:8", ["const:b46:8"]]
- 0044b2b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0044b2b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0044b2b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0044b5d4 ["COPY", "tmp:0:8", ["const:c24:8"]]
+ 0044b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0044b2b4 bytes 29192d91
+ 0044b5d4 bytes 29913091
- 0044b2dc ["COPY", "register:4008:8", ["const:2b7000:8"]]
+ 0044b5fc ["COPY", "register:4008:8", ["const:2b8000:8"]]
- 0044b2dc bytes 61f3ff90
+ 0044b5fc bytes 61f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-698efd94221ff1a978d83d6b66d65e1f"></a>

### [`0044b434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md) → [`0044b754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b754.md) FUN_0044b754

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) [`00455d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 10件 [`00452238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452238.md) [`00452848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452848.md) [`00452fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452fb4.md) [`00455b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00455/00455b3c.md) [`004560b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00456/004560b8.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b778",
      "incomplete_value": true,
      "site": "0044b78c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b458",
      "incomplete_value": true,
      "site": "0044b46c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b784",
      "incomplete_value": true,
      "site": "0044b790",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b464",
      "incomplete_value": true,
      "site": "0044b470",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8fc:8"
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
      "definition_site": "0044b784",
      "incomplete_value": true,
      "site": "0044b790",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b464",
      "incomplete_value": true,
      "site": "0044b470",
      "value": [
        "LOAD",
        "16",
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
      "0044b778",
      "READ",
      [
        "storage",
        "002c32e0",
        null,
        null
      ]
    ],
    [
      "0044b784",
      "READ",
      [
        "storage",
        "002b18fc",
        null,
        "string"
      ]
    ],
    [
      "0044b784",
      "READ",
      [
        "storage",
        "002b190c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b778",
      "READ",
      [
        "storage",
        "002c3330",
        null,
        null
      ]
    ],
    [
      "0044b784",
      "READ",
      [
        "storage",
        "002b19d3",
        null,
        "string"
      ]
    ],
    [
      "0044b784",
      "READ",
      [
        "storage",
        "002b19e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md#insn-0044b448) · [`0044b458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md#insn-0044b458) · [`0044b45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md#insn-0044b45c)
- 新版 [`0044b768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b754.md#insn-0044b768) · [`0044b778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b754.md#insn-0044b778)

~~~diff
- 0044b448 ["INT_ADD", "register:40f0:8", ["const:44b448:8", "const:4:8"]]
- 0044b448 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044b768 ["INT_ADD", "register:40f0:8", ["const:44b768:8", "const:4:8"]]
+ 0044b768 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b448 bytes c6322094
+ 0044b768 bytes f2352094
- 0044b458 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 0044b458 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b458 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b458 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b778 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 0044b778 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b778 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b778 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b458 bytes 00b9c03d
+ 0044b778 bytes 00cdc03d
- 0044b45c ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 0044b45c bytes 28f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b632140b2fa185bb91a33c6e0662e609"></a>

### [`0044b524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md) → [`0044b844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b844.md) FUN_0044b844

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`00456364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md) [`00456f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md) [`00457440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md) [`004578b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md) [`00458270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458270.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 7件 [`00456684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00456/00456684.md) [`0045725c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00457/0045725c.md) [`00457760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00457/00457760.md) [`00457bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00457/00457bd8.md) [`00458590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00458/00458590.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b868",
      "incomplete_value": true,
      "site": "0044b87c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b548",
      "incomplete_value": true,
      "site": "0044b55c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b874",
      "incomplete_value": true,
      "site": "0044b880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b554",
      "incomplete_value": true,
      "site": "0044b560",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b1:8"
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
      "definition_site": "0044b874",
      "incomplete_value": true,
      "site": "0044b880",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b554",
      "incomplete_value": true,
      "site": "0044b560",
      "value": [
        "LOAD",
        "16",
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
      "0044b868",
      "READ",
      [
        "storage",
        "002c32e0",
        null,
        null
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b71b1",
        null,
        "string"
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b71c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b868",
      "READ",
      [
        "storage",
        "002c3330",
        null,
        null
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b7280",
        null,
        "string"
      ]
    ],
    [
      "0044b874",
      "READ",
      [
        "storage",
        "002b7290",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md#insn-0044b538) · [`0044b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md#insn-0044b548) · [`0044b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md#insn-0044b54c)
- 新版 [`0044b858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b844.md#insn-0044b858) · [`0044b868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b844.md#insn-0044b868)

~~~diff
- 0044b538 ["INT_ADD", "register:40f0:8", ["const:44b538:8", "const:4:8"]]
- 0044b538 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044b858 ["INT_ADD", "register:40f0:8", ["const:44b858:8", "const:4:8"]]
+ 0044b858 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b538 bytes 8a322094
+ 0044b858 bytes b6352094
- 0044b548 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 0044b548 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b548 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b548 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 0044b868 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b868 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b868 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b548 bytes 00b9c03d
+ 0044b868 bytes 00cdc03d
- 0044b54c ["COPY", "register:4040:8", ["const:2b7000:8"]]
- 0044b54c bytes 68f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33c455135bbd31703a7b76368e267503"></a>

### [`0044b574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md) → [`0044b894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b894.md) FUN_0044b894

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) [`0044fd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md) [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00a84f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a84/00a84f18.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 5件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0044fca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fca8.md) [`0045006c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/0045006c.md) [`0045476c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00454/0045476c.md) [`00a85f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a85/00a85f0c.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b8bc",
      "incomplete_value": true,
      "site": "0044b8c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0044b59c",
      "incomplete_value": true,
      "site": "0044b5a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b8b8",
      "incomplete_value": true,
      "site": "0044b8cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b598",
      "incomplete_value": true,
      "site": "0044b5ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a0f:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b8b8",
      "incomplete_value": true,
      "site": "0044b8cc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b598",
      "incomplete_value": true,
      "site": "0044b5ac",
      "value": [
        "LOAD",
        "16",
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
      "0044b8b8",
      "READ",
      [
        "storage",
        "002a8a0f",
        null,
        "string"
      ]
    ],
    [
      "0044b8b8",
      "READ",
      [
        "storage",
        "002a8a1f",
        null,
        "string"
      ]
    ],
    [
      "0044b8bc",
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
      "0044b8b8",
      "READ",
      [
        "storage",
        "002a8b67",
        null,
        "string"
      ]
    ],
    [
      "0044b8b8",
      "READ",
      [
        "storage",
        "002a8b77",
        null,
        "string"
      ]
    ],
    [
      "0044b8bc",
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

- 旧版 [`0044b588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md#insn-0044b588) · [`0044b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md#insn-0044b590) · [`0044b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md#insn-0044b594)
- 新版 [`0044b8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b894.md#insn-0044b8a8) · [`0044b8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b894.md#insn-0044b8b0)

~~~diff
- 0044b588 ["INT_ADD", "register:40f0:8", ["const:44b588:8", "const:4:8"]]
- 0044b588 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044b8a8 ["INT_ADD", "register:40f0:8", ["const:44b8a8:8", "const:4:8"]]
+ 0044b8a8 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b588 bytes 76322094
+ 0044b8a8 bytes a2352094
- 0044b590 ["COPY", "tmp:0:8", ["const:a0f:8"]]
- 0044b590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044b590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044b590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044b8b0 ["COPY", "tmp:0:8", ["const:b67:8"]]
+ 0044b8b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b8b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b8b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044b590 bytes 083d2891
+ 0044b8b0 bytes 089d2d91
- 0044b594 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0044b594 bytes a9f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9e0a062ab1d7780ddd5e2a56a7cc33"></a>

### [`0044b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b5c4.md) → [`0044b8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b8e4.md) FUN_0044b8e4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) [`00477e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477e4c.md) · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 2件 [`00473adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/00473adc.md) [`0047816c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00478/0047816c.md) · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ff0.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.64% / 新版 83.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b924",
      "incomplete_value": true,
      "site": "0044b930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b604",
      "incomplete_value": true,
      "site": "0044b610",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:590:8"
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
      "definition_site": "0044b920",
      "incomplete_value": true,
      "site": "0044b934",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b600",
      "incomplete_value": true,
      "site": "0044b614",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f34:8"
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
      "definition_site": "0044b920",
      "incomplete_value": true,
      "site": "0044b934",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b600",
      "incomplete_value": true,
      "site": "0044b614",
      "value": [
        "LOAD",
        "16",
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
      "0044b920",
      "READ",
      [
        "storage",
        "002c0f34",
        null,
        "string"
      ]
    ],
    [
      "0044b920",
      "READ",
      [
        "storage",
        "002c0f44",
        null,
        "string"
      ]
    ],
    [
      "0044b924",
      "READ",
      [
        "storage",
        "002c2590",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044b920",
      "READ",
      [
        "storage",
        "002c0f7e",
        null,
        "string"
      ]
    ],
    [
      "0044b920",
      "READ",
      [
        "storage",
        "002c0f8e",
        null,
        "string"
      ]
    ],
    [
      "0044b924",
      "READ",
      [
        "storage",
        "002c25e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b5c4.md#insn-0044b634) · [`0044b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b5c4.md#insn-0044b5f0) · [`0044b5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b5c4.md#insn-0044b5f8)
- 新版 [`0044b954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b8e4.md#insn-0044b954) · [`0044b910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b8e4.md#insn-0044b910) · [`0044b918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044b8e4.md#insn-0044b918)

~~~diff
- 0044b634 ["INT_ADD", "register:40f0:8", ["const:44b634:8", "const:4:8"]]
- 0044b634 ["CALL", null, ["callee:00c59010:8"]]
+ 0044b954 ["INT_ADD", "register:40f0:8", ["const:44b954:8", "const:4:8"]]
+ 0044b954 ["CALL", null, ["callee:00c59010:8"]]
- 0044b634 bytes 83322094
+ 0044b954 bytes af352094
- 0044b5f0 ["INT_ADD", "register:40f0:8", ["const:44b5f0:8", "const:4:8"]]
- 0044b5f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044b910 ["INT_ADD", "register:40f0:8", ["const:44b910:8", "const:4:8"]]
+ 0044b910 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b5f0 bytes 5c322094
+ 0044b910 bytes 88352094
- 0044b5f8 ["COPY", "tmp:0:8", ["const:f34:8"]]
- 0044b5f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044b5f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044b5f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044b918 ["COPY", "tmp:0:8", ["const:f7e:8"]]
+ 0044b918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044b5f8 bytes 08d13c91
+ 0044b918 bytes 08f93d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6410eac0381649b4763201c33a92f23"></a>

### [`0044b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md) → [`0044ba60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044ba60.md) FUN_0044ba60

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00454884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md) [`00454d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md) [`00455338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`00454ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00454/00454ba4.md) [`00455088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00455/00455088.md) [`00455658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00455/00455658.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ba84",
      "incomplete_value": true,
      "site": "0044ba9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b764",
      "incomplete_value": true,
      "site": "0044b77c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6a0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044ba90",
      "incomplete_value": true,
      "site": "0044baa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b770",
      "incomplete_value": true,
      "site": "0044b780",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f10:8"
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
      "definition_site": "0044ba90",
      "incomplete_value": true,
      "site": "0044baa0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b770",
      "incomplete_value": true,
      "site": "0044b780",
      "value": [
        "LOAD",
        "16",
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
      "0044ba84",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ],
    [
      "0044ba90",
      "READ",
      [
        "storage",
        "002b9f10",
        null,
        "string"
      ]
    ],
    [
      "0044ba90",
      "READ",
      [
        "storage",
        "002b9f20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ba84",
      "READ",
      [
        "storage",
        "002c26f0",
        null,
        null
      ]
    ],
    [
      "0044ba90",
      "READ",
      [
        "storage",
        "002b9fee",
        null,
        "string"
      ]
    ],
    [
      "0044ba90",
      "READ",
      [
        "storage",
        "002b9ffe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md#insn-0044b754) · [`0044b764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md#insn-0044b764) · [`0044b768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md#insn-0044b768)
- 新版 [`0044ba74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044ba60.md#insn-0044ba74) · [`0044ba84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044ba60.md#insn-0044ba84)

~~~diff
- 0044b754 ["INT_ADD", "register:40f0:8", ["const:44b754:8", "const:4:8"]]
- 0044b754 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044ba74 ["INT_ADD", "register:40f0:8", ["const:44ba74:8", "const:4:8"]]
+ 0044ba74 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b754 bytes 03322094
+ 0044ba74 bytes 2f352094
- 0044b764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6a0:8"]]
- 0044b764 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b764 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b764 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044ba84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6f0:8"]]
+ 0044ba84 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044ba84 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044ba84 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b764 bytes 00a9c13d
+ 0044ba84 bytes 00bdc13d
- 0044b768 ["COPY", "register:4040:8", ["const:2b9000:8"]]
- 0044b768 bytes 68f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce2c74da9ef884902299ce4747fffb73"></a>

### [`0044b794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b794.md) → [`0044bab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bab4.md) FUN_0044bab4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`005a75a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a75a8.md) [`005a85b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a85b8.md) [`005a97f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a97f8.md) [`005aaf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aaf20.md) [`005ac090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac090.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 7件 [`005a7958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a7/005a7958.md) [`005a8968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a8/005a8968.md) [`005a9ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a9/005a9ba8.md) [`005ab2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ab/005ab2d0.md) [`005ac440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ac/005ac440.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044badc",
      "incomplete_value": true,
      "site": "0044bae8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b7bc",
      "incomplete_value": true,
      "site": "0044b7c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e40:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044bad8",
      "incomplete_value": true,
      "site": "0044baec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:862:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b7b8",
      "incomplete_value": true,
      "site": "0044b7cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:78b:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044bad8",
      "incomplete_value": true,
      "site": "0044baec",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b7b8",
      "incomplete_value": true,
      "site": "0044b7cc",
      "value": [
        "LOAD",
        "16",
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
      "0044bad8",
      "READ",
      [
        "storage",
        "002af78b",
        null,
        "string"
      ]
    ],
    [
      "0044bad8",
      "READ",
      [
        "storage",
        "002af79b",
        null,
        "string"
      ]
    ],
    [
      "0044badc",
      "READ",
      [
        "storage",
        "002c2e40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044bad8",
      "READ",
      [
        "storage",
        "002af862",
        null,
        "string"
      ]
    ],
    [
      "0044bad8",
      "READ",
      [
        "storage",
        "002af872",
        null,
        "string"
      ]
    ],
    [
      "0044badc",
      "READ",
      [
        "storage",
        "002c2e90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b794.md#insn-0044b7a8) · [`0044b7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b794.md#insn-0044b7b0) · [`0044b7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b794.md#insn-0044b7b4)
- 新版 [`0044bac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bab4.md#insn-0044bac8) · [`0044bad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bab4.md#insn-0044bad0)

~~~diff
- 0044b7a8 ["INT_ADD", "register:40f0:8", ["const:44b7a8:8", "const:4:8"]]
- 0044b7a8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044bac8 ["INT_ADD", "register:40f0:8", ["const:44bac8:8", "const:4:8"]]
+ 0044bac8 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b7a8 bytes ee312094
+ 0044bac8 bytes 1a352094
- 0044b7b0 ["COPY", "tmp:0:8", ["const:78b:8"]]
- 0044b7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044b7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044b7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044bad0 ["COPY", "tmp:0:8", ["const:862:8"]]
+ 0044bad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044bad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044bad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044b7b0 bytes 082d1e91
+ 0044bad0 bytes 08892191
- 0044b7b4 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0044b7b4 bytes a9f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-459b045a4c69b6d32c726470cf9ae00e"></a>

### [`0044b7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b7e4.md) → [`0044bb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bb04.md) FUN_0044bb04

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`008d648c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d6/008d648c.md) [`008d7ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7ce0.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bb28",
      "incomplete_value": true,
      "site": "0044bb3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b808",
      "incomplete_value": true,
      "site": "0044b81c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044bb34",
      "incomplete_value": true,
      "site": "0044bb40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:913:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b814",
      "incomplete_value": true,
      "site": "0044b820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8c9:8"
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
      "definition_site": "0044bb34",
      "incomplete_value": true,
      "site": "0044bb40",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0044b814",
      "incomplete_value": true,
      "site": "0044b820",
      "value": [
        "LOAD",
        "16",
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
      "0044bb28",
      "READ",
      [
        "storage",
        "002c32e0",
        null,
        null
      ]
    ],
    [
      "0044bb34",
      "READ",
      [
        "storage",
        "002b38c9",
        null,
        "string"
      ]
    ],
    [
      "0044bb34",
      "READ",
      [
        "storage",
        "002b38d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bb28",
      "READ",
      [
        "storage",
        "002c3330",
        null,
        null
      ]
    ],
    [
      "0044bb34",
      "READ",
      [
        "storage",
        "002b3913",
        null,
        "string"
      ]
    ],
    [
      "0044bb34",
      "READ",
      [
        "storage",
        "002b3923",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b7e4.md#insn-0044b7f8) · [`0044b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b7e4.md#insn-0044b808) · [`0044b80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b7e4.md#insn-0044b80c)
- 新版 [`0044bb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bb04.md#insn-0044bb18) · [`0044bb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bb04.md#insn-0044bb28)

~~~diff
- 0044b7f8 ["INT_ADD", "register:40f0:8", ["const:44b7f8:8", "const:4:8"]]
- 0044b7f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0044bb18 ["INT_ADD", "register:40f0:8", ["const:44bb18:8", "const:4:8"]]
+ 0044bb18 ["CALL", null, ["callee:00c58f30:8"]]
- 0044b7f8 bytes da312094
+ 0044bb18 bytes 06352094
- 0044b808 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 0044b808 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b808 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b808 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044bb28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 0044bb28 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044bb28 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044bb28 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b808 bytes 00b9c03d
+ 0044bb28 bytes 00cdc03d
- 0044b80c ["COPY", "register:4040:8", ["const:2b3000:8"]]
- 0044b80c bytes 48f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

