# v16.0.2 → v16.0.3 · 最優先の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-bba416db618f5c2bce3c0134297af150"></a>

### [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) → [`00579884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579884.md) FUN_00579884

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) · 呼出先 11件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md)
- 新版 呼出元 1件 [`0057921c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/0057921c.md) · 呼出先 11件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`005979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979bc.md) [`00597a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597a48.md) [`00597dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597dec.md) [`00597df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597df4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005799c0",
      "incomplete_value": false,
      "site": "005799c8",
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
      "definition_site": "005796a0",
      "incomplete_value": false,
      "site": "005796a8",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00579a24",
      "incomplete_value": false,
      "site": "00579a2c",
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
      "definition_site": "00579704",
      "incomplete_value": false,
      "site": "0057970c",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00579a88",
      "incomplete_value": false,
      "site": "00579a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:653:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579768",
      "incomplete_value": false,
      "site": "00579770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:586:8"
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
      "005799c0",
      "PARAM",
      [
        "storage",
        "002a019e",
        null,
        "string"
      ]
    ],
    [
      "00579a24",
      "PARAM",
      [
        "storage",
        "002b0d12",
        null,
        "string"
      ]
    ],
    [
      "00579a88",
      "PARAM",
      [
        "storage",
        "002ab586",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005799c0",
      "PARAM",
      [
        "storage",
        "002a01de",
        null,
        "string"
      ]
    ],
    [
      "00579a24",
      "PARAM",
      [
        "storage",
        "002b0de9",
        null,
        "string"
      ]
    ],
    [
      "00579a88",
      "PARAM",
      [
        "storage",
        "002ab653",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005796a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md#insn-005796a8) · [`0057970c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md#insn-0057970c) · [`00579770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md#insn-00579770)
- 新版 [`005799c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579884.md#insn-005799c8) · [`00579a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579884.md#insn-00579a2c) · [`00579a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579884.md#insn-00579a90)

~~~diff
- 005796a8 ["INT_ADD", "register:40f0:8", ["const:5796a8:8", "const:4:8"]]
- 005796a8 ["CALL", null, ["callee:00c59010:8"]]
+ 005799c8 ["INT_ADD", "register:40f0:8", ["const:5799c8:8", "const:4:8"]]
+ 005799c8 ["CALL", null, ["callee:00c59010:8"]]
- 005796a8 bytes 667a1b94
+ 005799c8 bytes 927d1b94
- 0057970c ["INT_ADD", "register:40f0:8", ["const:57970c:8", "const:4:8"]]
- 0057970c ["CALL", null, ["callee:00c59010:8"]]
+ 00579a2c ["INT_ADD", "register:40f0:8", ["const:579a2c:8", "const:4:8"]]
+ 00579a2c ["CALL", null, ["callee:00c59010:8"]]
- 0057970c bytes 4d7a1b94
+ 00579a2c bytes 797d1b94
- 00579770 ["INT_ADD", "register:40f0:8", ["const:579770:8", "const:4:8"]]
- 00579770 ["CALL", null, ["callee:00c59010:8"]]
+ 00579a90 ["INT_ADD", "register:40f0:8", ["const:579a90:8", "const:4:8"]]
+ 00579a90 ["CALL", null, ["callee:00c59010:8"]]
- 00579770 bytes 347a1b94
+ 00579a90 bytes 607d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8559a96ae9622f125c70d5850f6f590a"></a>

### [`00579b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579b0c.md) → [`00579e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579e2c.md) FUN_00579e2c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00579f88",
      "incomplete_value": true,
      "site": "00579f88",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579c68",
      "incomplete_value": true,
      "site": "00579c68",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a128",
      "incomplete_value": true,
      "site": "0057a128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:933:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579e08",
      "incomplete_value": true,
      "site": "00579e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:866:8"
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
      "definition_site": "0057a130",
      "incomplete_value": true,
      "site": "0057a130",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00579e10",
      "incomplete_value": true,
      "site": "00579e10",
      "value": [
        "LOAD",
        "8",
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
      "00579f04",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00579f68",
      "DATA",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00579f78",
      "WRITE",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00579f04",
      "READ",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ],
    [
      "00579f68",
      "DATA",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ],
    [
      "00579f78",
      "WRITE",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579b0c.md#insn-00579c68) · [`00579b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579b0c.md#insn-00579b64) · [`00579b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579b0c.md#insn-00579b90)
- 新版 [`00579f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579e2c.md#insn-00579f88) · [`00579e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579e2c.md#insn-00579e84) · [`00579eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579e2c.md#insn-00579eb0)

~~~diff
- 00579c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 00579c68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00579f88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f8:8"]]
+ 00579f88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00579c68 bytes 099d01f9
+ 00579f88 bytes 097d01f9
- 00579b64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00579b64 ["INT_ADD", "register:40f0:8", ["const:579b64:8", "const:4:8"]]
- 00579b64 ["CALLIND", null, ["register:0:8"]]
+ 00579e84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00579e84 ["INT_ADD", "register:40f0:8", ["const:579e84:8", "const:4:8"]]
+ 00579e84 ["CALLIND", null, ["register:0:8"]]
- 00579b64 bytes 20013fd6
+ 00579e84 bytes 20013fd6
- 00579b90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00579b90 ["INT_ADD", "register:40f0:8", ["const:579b90:8", "const:4:8"]]
- 00579b90 ["CALLIND", null, ["register:0:8"]]
+ 00579eb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00579eb0 ["INT_ADD", "register:40f0:8", ["const:579eb0:8", "const:4:8"]]
+ 00579eb0 ["CALLIND", null, ["register:0:8"]]
- 00579b90 bytes 00013fd6
+ 00579eb0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d2f6505da678082622735f9316e5257"></a>

### [`0057a17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a17c.md) → [`0057a49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a49c.md) FUN_0057a49c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a500",
      "incomplete_value": true,
      "site": "0057a500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dfb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a1e0",
      "incomplete_value": true,
      "site": "0057a1e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d1d:8"
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
      "definition_site": "0057a504",
      "incomplete_value": true,
      "site": "0057a504",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a1e4",
      "incomplete_value": true,
      "site": "0057a1e4",
      "value": [
        "LOAD",
        "8",
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
      "0057a4f0",
      "READ",
      [
        "storage",
        "002b3d1d",
        null,
        "string"
      ]
    ],
    [
      "0057a4f8",
      "READ",
      [
        "storage",
        "002b3d22",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a4f0",
      "READ",
      [
        "storage",
        "002b3dfb",
        null,
        "string"
      ]
    ],
    [
      "0057a4f8",
      "READ",
      [
        "storage",
        "002b3e00",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a17c.md#insn-0057a1b8) · [`0057a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a17c.md#insn-0057a1c0) · [`0057a1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a17c.md#insn-0057a1cc)
- 新版 [`0057a4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a49c.md#insn-0057a4d8) · [`0057a4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a49c.md#insn-0057a4e0) · [`0057a4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a49c.md#insn-0057a4ec)

~~~diff
- 0057a1b8 ["INT_ADD", "register:40f0:8", ["const:57a1b8:8", "const:4:8"]]
- 0057a1b8 ["CALL", null, ["callee:005891cc:8"]]
+ 0057a4d8 ["INT_ADD", "register:40f0:8", ["const:57a4d8:8", "const:4:8"]]
+ 0057a4d8 ["CALL", null, ["callee:005891cc:8"]]
- 0057a1b8 bytes 3d3b0094
+ 0057a4d8 bytes 3d3b0094
- 0057a1c0 ["INT_ADD", "register:40f0:8", ["const:57a1c0:8", "const:4:8"]]
- 0057a1c0 ["CALL", null, ["callee:005894bc:8"]]
+ 0057a4e0 ["INT_ADD", "register:40f0:8", ["const:57a4e0:8", "const:4:8"]]
+ 0057a4e0 ["CALL", null, ["callee:005894bc:8"]]
- 0057a1c0 bytes f73b0094
+ 0057a4e0 bytes f73b0094
- 0057a1cc ["COPY", "tmp:0:8", ["const:d1d:8"]]
- 0057a1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a4ec ["COPY", "tmp:0:8", ["const:dfb:8"]]
+ 0057a4ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a4ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a4ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a1cc bytes 29753491
+ 0057a4ec bytes 29ed3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2072068eb806a4594ffbe26abf4eefe6"></a>

### [`0057a3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a3cc.md) → [`0057a6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6ec.md) FUN_0057a6ec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a740",
      "incomplete_value": true,
      "site": "0057a740",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4cb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a420",
      "incomplete_value": true,
      "site": "0057a420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ed:8"
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
      "definition_site": "0057a744",
      "incomplete_value": true,
      "site": "0057a744",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a424",
      "incomplete_value": true,
      "site": "0057a424",
      "value": [
        "LOAD",
        "8",
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
      "0057a730",
      "READ",
      [
        "storage",
        "002ba3ed",
        null,
        "string"
      ]
    ],
    [
      "0057a738",
      "READ",
      [
        "storage",
        "002ba3f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a730",
      "READ",
      [
        "storage",
        "002ba4cb",
        null,
        "string"
      ]
    ],
    [
      "0057a738",
      "READ",
      [
        "storage",
        "002ba4d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a3cc.md#insn-0057a3f8) · [`0057a400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a3cc.md#insn-0057a400) · [`0057a40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a3cc.md#insn-0057a40c)
- 新版 [`0057a718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6ec.md#insn-0057a718) · [`0057a720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6ec.md#insn-0057a720) · [`0057a72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6ec.md#insn-0057a72c)

~~~diff
- 0057a3f8 ["INT_ADD", "register:40f0:8", ["const:57a3f8:8", "const:4:8"]]
- 0057a3f8 ["CALL", null, ["callee:005891cc:8"]]
+ 0057a718 ["INT_ADD", "register:40f0:8", ["const:57a718:8", "const:4:8"]]
+ 0057a718 ["CALL", null, ["callee:005891cc:8"]]
- 0057a3f8 bytes ad3a0094
+ 0057a718 bytes ad3a0094
- 0057a400 ["INT_ADD", "register:40f0:8", ["const:57a400:8", "const:4:8"]]
- 0057a400 ["CALL", null, ["callee:005894bc:8"]]
+ 0057a720 ["INT_ADD", "register:40f0:8", ["const:57a720:8", "const:4:8"]]
+ 0057a720 ["CALL", null, ["callee:005894bc:8"]]
- 0057a400 bytes 673b0094
+ 0057a720 bytes 673b0094
- 0057a40c ["COPY", "tmp:0:8", ["const:3ed:8"]]
- 0057a40c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a40c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a40c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a72c ["COPY", "tmp:0:8", ["const:4cb:8"]]
+ 0057a72c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a72c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a72c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a40c bytes 29b50f91
+ 0057a72c bytes 292d1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76ebcdf33f77440ab5696a1888d7c3a"></a>

### [`0057a504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a504.md) → [`0057a824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a824.md) FUN_0057a824

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a878",
      "incomplete_value": true,
      "site": "0057a878",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:56a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a558",
      "incomplete_value": true,
      "site": "0057a558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49b:8"
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
      "definition_site": "0057a87c",
      "incomplete_value": true,
      "site": "0057a87c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a55c",
      "incomplete_value": true,
      "site": "0057a55c",
      "value": [
        "LOAD",
        "8",
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
      "0057a868",
      "READ",
      [
        "storage",
        "002b749b",
        null,
        "string"
      ]
    ],
    [
      "0057a870",
      "READ",
      [
        "storage",
        "002b74a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a868",
      "READ",
      [
        "storage",
        "002b756a",
        null,
        "string"
      ]
    ],
    [
      "0057a870",
      "READ",
      [
        "storage",
        "002b7570",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a504.md#insn-0057a530) · [`0057a538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a504.md#insn-0057a538) · [`0057a544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a504.md#insn-0057a544)
- 新版 [`0057a850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a824.md#insn-0057a850) · [`0057a858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a824.md#insn-0057a858) · [`0057a864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a824.md#insn-0057a864)

~~~diff
- 0057a530 ["INT_ADD", "register:40f0:8", ["const:57a530:8", "const:4:8"]]
- 0057a530 ["CALL", null, ["callee:005891cc:8"]]
+ 0057a850 ["INT_ADD", "register:40f0:8", ["const:57a850:8", "const:4:8"]]
+ 0057a850 ["CALL", null, ["callee:005891cc:8"]]
- 0057a530 bytes 5f3a0094
+ 0057a850 bytes 5f3a0094
- 0057a538 ["INT_ADD", "register:40f0:8", ["const:57a538:8", "const:4:8"]]
- 0057a538 ["CALL", null, ["callee:005894bc:8"]]
+ 0057a858 ["INT_ADD", "register:40f0:8", ["const:57a858:8", "const:4:8"]]
+ 0057a858 ["CALL", null, ["callee:005894bc:8"]]
- 0057a538 bytes 193b0094
+ 0057a858 bytes 193b0094
- 0057a544 ["COPY", "tmp:0:8", ["const:49b:8"]]
- 0057a544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a864 ["COPY", "tmp:0:8", ["const:56a:8"]]
+ 0057a864 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a864 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a864 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a544 bytes 296d1291
+ 0057a864 bytes 29a91591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f83769b49cc1b2e8122bc83880bb2b47"></a>

### [`0057a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md) → [`0057a95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a95c.md) FUN_0057a95c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0057c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0057c690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c690.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057a994",
      "incomplete_value": false,
      "site": "0057a9a8",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a674",
      "incomplete_value": false,
      "site": "0057a688",
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
      "definition_site": "0057a99c",
      "incomplete_value": false,
      "site": "0057a9a8",
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
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a67c",
      "incomplete_value": false,
      "site": "0057a688",
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
            "const:e70:8"
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
      "0057a994",
      "PARAM",
      [
        "storage",
        "00c6be58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a99c",
      "PARAM",
      [
        "storage",
        "00c6be70",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0057a994",
      "PARAM",
      [
        "storage",
        "00c6ce28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a99c",
      "PARAM",
      [
        "storage",
        "00c6ce40",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md#insn-0057a688) · [`0057a670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md#insn-0057a670) · [`0057a674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md#insn-0057a674)
- 新版 [`0057a9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a95c.md#insn-0057a9a8) · [`0057a990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a95c.md#insn-0057a990) · [`0057a994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a95c.md#insn-0057a994)

~~~diff
- 0057a688 ["INT_ADD", "register:40f0:8", ["const:57a688:8", "const:4:8"]]
- 0057a688 ["CALL", null, ["callee:00c596b0:8"]]
+ 0057a9a8 ["INT_ADD", "register:40f0:8", ["const:57a9a8:8", "const:4:8"]]
+ 0057a9a8 ["CALL", null, ["callee:00c596b0:8"]]
- 0057a688 bytes 16781b94
+ 0057a9a8 bytes 427b1b94
- 0057a670 ["COPY", "register:4008:8", ["const:c6b000:8"]]
+ 0057a990 ["COPY", "register:4008:8", ["const:c6c000:8"]]
- 0057a670 bytes 813700b0
+ 0057a990 bytes 813700d0
- 0057a674 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0057a674 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057a674 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057a674 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057a994 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 0057a994 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a994 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a994 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057a674 bytes 21603991
+ 0057a994 bytes 21a03891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d58b5a41a39c6ce9943dbaafdc67a964"></a>

### [`0057a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md) → [`0057aa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057aa9c.md) FUN_0057aa9c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a4c.md) · 呼出先 8件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00550d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d6c.md) · 呼出先 8件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ab18",
      "incomplete_value": true,
      "site": "0057ab18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a7f8",
      "incomplete_value": true,
      "site": "0057a7f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4d0:8"
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
      "definition_site": "0057ab3c",
      "incomplete_value": true,
      "site": "0057ab3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e73:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a81c",
      "incomplete_value": true,
      "site": "0057a81c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e29:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057abfc",
      "incomplete_value": false,
      "site": "0057ac04",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a8dc",
      "incomplete_value": false,
      "site": "0057a8e4",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057ab0c",
      "READ",
      [
        "storage",
        "002bb4d0",
        null,
        "string"
      ]
    ],
    [
      "0057ab38",
      "READ",
      [
        "storage",
        "002b1e29",
        null,
        "string"
      ]
    ],
    [
      "0057ac04",
      "DATA",
      [
        "storage",
        "00c6bff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057ab0c",
      "READ",
      [
        "storage",
        "002bb5ae",
        null,
        "string"
      ]
    ],
    [
      "0057ab38",
      "READ",
      [
        "storage",
        "002b1e73",
        null,
        "string"
      ]
    ],
    [
      "0057ac04",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md#insn-0057a7c8) · [`0057a7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md#insn-0057a7d0) · [`0057a7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md#insn-0057a7e8)
- 新版 [`0057aae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057aa9c.md#insn-0057aae8) · [`0057aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057aa9c.md#insn-0057aaf0) · [`0057ab08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057aa9c.md#insn-0057ab08)

~~~diff
- 0057a7c8 ["INT_ADD", "register:40f0:8", ["const:57a7c8:8", "const:4:8"]]
- 0057a7c8 ["CALL", null, ["callee:005891cc:8"]]
+ 0057aae8 ["INT_ADD", "register:40f0:8", ["const:57aae8:8", "const:4:8"]]
+ 0057aae8 ["CALL", null, ["callee:005891cc:8"]]
- 0057a7c8 bytes b9390094
+ 0057aae8 bytes b9390094
- 0057a7d0 ["INT_ADD", "register:40f0:8", ["const:57a7d0:8", "const:4:8"]]
- 0057a7d0 ["CALL", null, ["callee:005894bc:8"]]
+ 0057aaf0 ["INT_ADD", "register:40f0:8", ["const:57aaf0:8", "const:4:8"]]
+ 0057aaf0 ["CALL", null, ["callee:005894bc:8"]]
- 0057a7d0 bytes 733a0094
+ 0057aaf0 bytes 733a0094
- 0057a7e8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0057a7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ab08 ["COPY", "tmp:0:8", ["const:5ae:8"]]
+ 0057ab08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ab08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ab08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a7e8 bytes 08411391
+ 0057ab08 bytes 08b91691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-645d626af6815283fd64bafeec1283ce"></a>

### [`0057a9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9a8.md) → [`0057acc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acc8.md) FUN_0057acc8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ace4",
      "incomplete_value": false,
      "site": "0057acec",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a9c4",
      "incomplete_value": false,
      "site": "0057a9cc",
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
            "const:40:8"
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
      "definition_site": "0057ad00",
      "incomplete_value": false,
      "site": "0057ad00",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a9e0",
      "incomplete_value": false,
      "site": "0057a9e0",
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
            "const:da8:8"
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
      "0057acec",
      "DATA",
      [
        "storage",
        "00c6c040",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ad00",
      "DATA",
      [
        "storage",
        "00c6bda8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057acec",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ad00",
      "DATA",
      [
        "storage",
        "00c6cd78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9a8.md#insn-0057a9bc) · [`0057a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9a8.md#insn-0057a9c0) · [`0057a9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9a8.md#insn-0057a9c4)
- 新版 [`0057acdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acc8.md#insn-0057acdc) · [`0057ace0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acc8.md#insn-0057ace0) · [`0057ace4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acc8.md#insn-0057ace4)

~~~diff
- 0057a9bc ["INT_ADD", "register:40f0:8", ["const:57a9bc:8", "const:4:8"]]
- 0057a9bc ["CALL", null, ["callee:00c58f30:8"]]
+ 0057acdc ["INT_ADD", "register:40f0:8", ["const:57acdc:8", "const:4:8"]]
+ 0057acdc ["CALL", null, ["callee:00c58f30:8"]]
- 0057a9bc bytes 69751b94
+ 0057acdc bytes 95781b94
- 0057a9c0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057ace0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057a9c0 bytes 883700d0
+ 0057ace0 bytes 883700f0
- 0057a9c4 ["COPY", "tmp:0:8", ["const:40:8"]]
- 0057a9c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a9c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a9c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ace4 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0057ace4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ace4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ace4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a9c4 bytes 08010191
+ 0057ace4 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c93b3f27667a0e2b3a727b604a7320b"></a>

### [`0057a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md) → [`0057ad14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057ad14.md) FUN_0057ad14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ad88",
      "incomplete_value": true,
      "site": "0057ad88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057aa68",
      "incomplete_value": true,
      "site": "0057aa68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
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
      "definition_site": "0057ad90",
      "incomplete_value": true,
      "site": "0057ad90",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057aa70",
      "incomplete_value": true,
      "site": "0057aa70",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ad8c",
      "incomplete_value": true,
      "site": "0057ada0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8bf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057aa6c",
      "incomplete_value": true,
      "site": "0057aa80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:767:8"
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
      "0057ad70",
      "READ",
      [
        "storage",
        "002bffa0",
        null,
        "string"
      ]
    ],
    [
      "0057ad78",
      "READ",
      [
        "storage",
        "002bffa6",
        null,
        "string"
      ]
    ],
    [
      "0057ad8c",
      "READ",
      [
        "storage",
        "002a6767",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ad70",
      "READ",
      [
        "storage",
        "002bffea",
        null,
        "string"
      ]
    ],
    [
      "0057ad78",
      "READ",
      [
        "storage",
        "002bfff0",
        null,
        "string"
      ]
    ],
    [
      "0057ad8c",
      "READ",
      [
        "storage",
        "002a68bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md#insn-0057ab78) · [`0057aa28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md#insn-0057aa28) · [`0057aa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md#insn-0057aa3c)
- 新版 [`0057ae98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057ad14.md#insn-0057ae98) · [`0057ad48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057ad14.md#insn-0057ad48) · [`0057ad5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057ad14.md#insn-0057ad5c)

~~~diff
- 0057ab78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
- 0057ab78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057ae98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
+ 0057ae98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057ab78 bytes 09d101f9
+ 0057ae98 bytes 09b101f9
- 0057aa28 ["INT_ADD", "register:40f0:8", ["const:57aa28:8", "const:4:8"]]
- 0057aa28 ["CALL", null, ["callee:005891cc:8"]]
+ 0057ad48 ["INT_ADD", "register:40f0:8", ["const:57ad48:8", "const:4:8"]]
+ 0057ad48 ["CALL", null, ["callee:005891cc:8"]]
- 0057aa28 bytes 21390094
+ 0057ad48 bytes 21390094
- 0057aa3c ["INT_ADD", "register:40f0:8", ["const:57aa3c:8", "const:4:8"]]
- 0057aa3c ["CALL", null, ["callee:00589c30:8"]]
+ 0057ad5c ["INT_ADD", "register:40f0:8", ["const:57ad5c:8", "const:4:8"]]
+ 0057ad5c ["CALL", null, ["callee:00589c30:8"]]
- 0057aa3c bytes b53b0094
+ 0057ad5c bytes b53b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeba2b04e94a070201d875b0dca2240e"></a>

### [`0057aca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057aca4.md) → [`0057afc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057afc4.md) FUN_0057afc4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b024",
      "incomplete_value": true,
      "site": "0057b024",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ad04",
      "incomplete_value": true,
      "site": "0057ad04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:91a:8"
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
      "definition_site": "0057b0a0",
      "incomplete_value": true,
      "site": "0057b0a0",
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
      "definition_site": "0057ad80",
      "incomplete_value": true,
      "site": "0057ad80",
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
      "0057b014",
      "READ",
      [
        "storage",
        "002a791a",
        null,
        "string"
      ]
    ],
    [
      "0057b09c",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b0f8",
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
      "0057b014",
      "READ",
      [
        "storage",
        "002a7a72",
        null,
        "string"
      ]
    ],
    [
      "0057b09c",
      "READ",
      [
        "storage",
        "00ca7350",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b0f8",
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

- 旧版 [`0057acd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057aca4.md#insn-0057acd4) · [`0057acdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057aca4.md#insn-0057acdc) · [`0057ace8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057aca4.md#insn-0057ace8)
- 新版 [`0057aff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057afc4.md#insn-0057aff4) · [`0057affc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057afc4.md#insn-0057affc) · [`0057b008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057afc4.md#insn-0057b008)

~~~diff
- 0057acd4 ["INT_ADD", "register:40f0:8", ["const:57acd4:8", "const:4:8"]]
- 0057acd4 ["CALL", null, ["callee:005891cc:8"]]
+ 0057aff4 ["INT_ADD", "register:40f0:8", ["const:57aff4:8", "const:4:8"]]
+ 0057aff4 ["CALL", null, ["callee:005891cc:8"]]
- 0057acd4 bytes 76380094
+ 0057aff4 bytes 76380094
- 0057acdc ["INT_ADD", "register:40f0:8", ["const:57acdc:8", "const:4:8"]]
- 0057acdc ["CALL", null, ["callee:005894bc:8"]]
+ 0057affc ["INT_ADD", "register:40f0:8", ["const:57affc:8", "const:4:8"]]
+ 0057affc ["CALL", null, ["callee:005894bc:8"]]
- 0057acdc bytes 30390094
+ 0057affc bytes 30390094
- 0057ace8 ["COPY", "tmp:0:8", ["const:91a:8"]]
- 0057ace8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b008 ["COPY", "tmp:0:8", ["const:a72:8"]]
+ 0057b008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057ace8 bytes 29692491
+ 0057b008 bytes 29c92991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00eb6cc50faf771cfbbbdeed03e167ec"></a>

### [`0057ae9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057ae9c.md) → [`0057b1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b1bc.md) FUN_0057b1bc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b218",
      "incomplete_value": true,
      "site": "0057b218",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:579:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057aef8",
      "incomplete_value": true,
      "site": "0057aef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4aa:8"
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
      "0057b200",
      "READ",
      [
        "storage",
        "002b74aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057b200",
      "READ",
      [
        "storage",
        "002b7579",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057ae9c.md#insn-0057aec0) · [`0057aec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057ae9c.md#insn-0057aec8) · [`0057aed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057ae9c.md#insn-0057aed4)
- 新版 [`0057b1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b1bc.md#insn-0057b1e0) · [`0057b1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b1bc.md#insn-0057b1e8) · [`0057b1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b1bc.md#insn-0057b1f4)

~~~diff
- 0057aec0 ["INT_ADD", "register:40f0:8", ["const:57aec0:8", "const:4:8"]]
- 0057aec0 ["CALL", null, ["callee:005891cc:8"]]
+ 0057b1e0 ["INT_ADD", "register:40f0:8", ["const:57b1e0:8", "const:4:8"]]
+ 0057b1e0 ["CALL", null, ["callee:005891cc:8"]]
- 0057aec0 bytes fb370094
+ 0057b1e0 bytes fb370094
- 0057aec8 ["INT_ADD", "register:40f0:8", ["const:57aec8:8", "const:4:8"]]
- 0057aec8 ["CALL", null, ["callee:005894bc:8"]]
+ 0057b1e8 ["INT_ADD", "register:40f0:8", ["const:57b1e8:8", "const:4:8"]]
+ 0057b1e8 ["CALL", null, ["callee:005894bc:8"]]
- 0057aec8 bytes b5380094
+ 0057b1e8 bytes b5380094
- 0057aed4 ["COPY", "tmp:0:8", ["const:4aa:8"]]
- 0057aed4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057aed4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057aed4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b1f4 ["COPY", "tmp:0:8", ["const:579:8"]]
+ 0057b1f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b1f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b1f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057aed4 bytes 29a91291
+ 0057b1f4 bytes 29e51591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5154db06f29b7373c884a3ea3b8c5f6"></a>

### [`0057afbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057afbc.md) → [`0057b2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b2dc.md) FUN_0057b2dc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a54.md) · 呼出先 11件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00550d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d74.md) · 呼出先 11件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b348",
      "incomplete_value": true,
      "site": "0057b350",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:19f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b028",
      "incomplete_value": true,
      "site": "0057b030",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d4:8"
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
      "definition_site": "0057b354",
      "incomplete_value": true,
      "site": "0057b354",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057b034",
      "incomplete_value": true,
      "site": "0057b034",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b414",
      "incomplete_value": false,
      "site": "0057b41c",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b0f4",
      "incomplete_value": false,
      "site": "0057b0fc",
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
            "const:90:8"
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
      "0057b348",
      "READ",
      [
        "storage",
        "002a20d4",
        null,
        "string"
      ]
    ],
    [
      "0057b34c",
      "READ",
      [
        "storage",
        "002a20e1",
        null,
        "string"
      ]
    ],
    [
      "0057b41c",
      "DATA",
      [
        "storage",
        "00c6c090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b348",
      "READ",
      [
        "storage",
        "002a219f",
        null,
        "string"
      ]
    ],
    [
      "0057b34c",
      "READ",
      [
        "storage",
        "002a21ac",
        null,
        "string"
      ]
    ],
    [
      "0057b41c",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057afe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057afbc.md#insn-0057afe8) · [`0057aff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057afbc.md#insn-0057aff0) · [`0057b024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057afbc.md#insn-0057b024)
- 新版 [`0057b308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b2dc.md#insn-0057b308) · [`0057b310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b2dc.md#insn-0057b310) · [`0057b344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b2dc.md#insn-0057b344)

~~~diff
- 0057afe8 ["INT_ADD", "register:40f0:8", ["const:57afe8:8", "const:4:8"]]
- 0057afe8 ["CALL", null, ["callee:005891cc:8"]]
+ 0057b308 ["INT_ADD", "register:40f0:8", ["const:57b308:8", "const:4:8"]]
+ 0057b308 ["CALL", null, ["callee:005891cc:8"]]
- 0057afe8 bytes b1370094
+ 0057b308 bytes b1370094
- 0057aff0 ["INT_ADD", "register:40f0:8", ["const:57aff0:8", "const:4:8"]]
- 0057aff0 ["CALL", null, ["callee:005894bc:8"]]
+ 0057b310 ["INT_ADD", "register:40f0:8", ["const:57b310:8", "const:4:8"]]
+ 0057b310 ["CALL", null, ["callee:005894bc:8"]]
- 0057aff0 bytes 6b380094
+ 0057b310 bytes 6b380094
- 0057b024 ["COPY", "tmp:0:8", ["const:d4:8"]]
- 0057b024 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b024 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b024 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b344 ["COPY", "tmp:0:8", ["const:19f:8"]]
+ 0057b344 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b344 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b344 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b024 bytes 29510391
+ 0057b344 bytes 297d0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7511b6d7d6775a4cc6fe60d8f883eda8"></a>

### [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) → [`0057b4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b4c4.md) FUN_0057b4c4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a50.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`0057c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`00550d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d70.md) · 呼出先 15件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`0057c9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c9b4.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.90% / 新版 91.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057b6ec",
      "incomplete_value": true,
      "site": "0057b6ec",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b3cc",
      "incomplete_value": true,
      "site": "0057b3cc",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b7a8",
      "incomplete_value": false,
      "site": "0057b7b0",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b488",
      "incomplete_value": false,
      "site": "0057b490",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b7c0",
      "incomplete_value": false,
      "site": "0057b7c0",
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
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b4a0",
      "incomplete_value": false,
      "site": "0057b4a0",
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
            "const:df0:8"
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
      "0057b544",
      "READ",
      [
        "storage",
        "002a9d35",
        null,
        "string"
      ]
    ],
    [
      "0057b544",
      "READ",
      [
        "storage",
        "002a9d45",
        null,
        "string"
      ]
    ],
    [
      "0057b548",
      "READ",
      [
        "storage",
        "002c2f00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057b544",
      "READ",
      [
        "storage",
        "002a9e02",
        null,
        "string"
      ]
    ],
    [
      "0057b544",
      "READ",
      [
        "storage",
        "002a9e12",
        null,
        "string"
      ]
    ],
    [
      "0057b548",
      "READ",
      [
        "storage",
        "002c2f50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md#insn-0057b3cc) · [`0057b1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md#insn-0057b1e0) · [`0057b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md#insn-0057b1e8)
- 新版 [`0057b6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b4c4.md#insn-0057b6ec) · [`0057b500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b4c4.md#insn-0057b500) · [`0057b508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b4c4.md#insn-0057b508)

~~~diff
- 0057b3cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
- 0057b3cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057b6ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:348:8"]]
+ 0057b6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057b3cc bytes 09c501f9
+ 0057b6ec bytes 09a501f9
- 0057b1e0 ["INT_ADD", "register:40f0:8", ["const:57b1e0:8", "const:4:8"]]
- 0057b1e0 ["CALL", null, ["callee:005891cc:8"]]
+ 0057b500 ["INT_ADD", "register:40f0:8", ["const:57b500:8", "const:4:8"]]
+ 0057b500 ["CALL", null, ["callee:005891cc:8"]]
- 0057b1e0 bytes 33370094
+ 0057b500 bytes 33370094
- 0057b1e8 ["INT_ADD", "register:40f0:8", ["const:57b1e8:8", "const:4:8"]]
- 0057b1e8 ["CALL", null, ["callee:005894bc:8"]]
+ 0057b508 ["INT_ADD", "register:40f0:8", ["const:57b508:8", "const:4:8"]]
+ 0057b508 ["CALL", null, ["callee:005894bc:8"]]
- 0057b1e8 bytes ed370094
+ 0057b508 bytes ed370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36955e29adebb6c04a4eedd2615b67da"></a>

### [`0057b558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b558.md) → [`0057b878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b878.md) Java_jp_co_ponos_battlecats_MyActivity_onAlertClick

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.56% / 新版 92.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057b9e8",
      "incomplete_value": true,
      "site": "0057b9e8",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b6c8",
      "incomplete_value": true,
      "site": "0057b6c8",
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
            "const:3a0:8"
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
      "definition_site": "0057b8a4",
      "incomplete_value": true,
      "site": "0057b8a4",
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
      "definition_site": "0057b584",
      "incomplete_value": true,
      "site": "0057b584",
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
      "definition_site": "0057b9e4",
      "incomplete_value": true,
      "site": "0057b9e4",
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
      "definition_site": "0057b6c4",
      "incomplete_value": true,
      "site": "0057b6c4",
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
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057b8a0",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b8e8",
      "READ",
      [
        "storage",
        "00ca63e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b91c",
      "READ",
      [
        "storage",
        "00ca63a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b8a0",
      "READ",
      [
        "storage",
        "00ca7350",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b8e8",
      "READ",
      [
        "storage",
        "00ca73a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b91c",
      "READ",
      [
        "storage",
        "00ca7368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b558.md#insn-0057b6c8) · [`0057b578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b558.md#insn-0057b578) · [`0057b57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b558.md#insn-0057b57c)
- 新版 [`0057b9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b878.md#insn-0057b9e8) · [`0057b898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b878.md#insn-0057b898) · [`0057b89c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057b878.md#insn-0057b89c)

~~~diff
- 0057b6c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3a0:8"]]
- 0057b6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0057b9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
+ 0057b9e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057b6c8 bytes 28d101f9
+ 0057b9e8 bytes 28b101f9
- 0057b578 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0057b898 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0057b578 bytes 483900f0
+ 0057b898 bytes 68390090
- 0057b57c ["COPY", "tmp:0:8", ["const:390:8"]]
- 0057b57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b89c ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0057b89c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b89c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b89c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b57c bytes 08410e91
+ 0057b89c bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8350a826f4738eee23d462f4f28e8251"></a>

### [`0057b73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b73c.md) → [`0057ba5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057ba5c.md) Java_jp_co_ponos_battlecats_MyActivity_onButtonClick

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057ba68",
      "incomplete_value": true,
      "site": "0057ba68",
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
      "definition_site": "0057b748",
      "incomplete_value": true,
      "site": "0057b748",
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
      "0057ba64",
      "READ",
      [
        "storage",
        "00ca6378",
        null,
        "undefined8"
      ]
    ],
    [
      "0057babc",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057ba64",
      "READ",
      [
        "storage",
        "00ca7338",
        null,
        "undefined8"
      ]
    ],
    [
      "0057babc",
      "READ",
      [
        "storage",
        "00ca7360",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b73c.md#insn-0057b73c) · [`0057b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b73c.md#insn-0057b740) · [`0057b74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b73c.md#insn-0057b74c)
- 新版 [`0057ba5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057ba5c.md#insn-0057ba5c) · [`0057ba60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057ba5c.md#insn-0057ba60) · [`0057ba6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057ba5c.md#insn-0057ba6c)

~~~diff
- 0057b73c ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0057ba5c ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0057b73c bytes 483900f0
+ 0057ba5c bytes 68390090
- 0057b740 ["COPY", "tmp:0:8", ["const:378:8"]]
- 0057b740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba60 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0057ba60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b740 bytes 08e10d91
+ 0057ba60 bytes 08e10c91
- 0057b74c ["COPY", "register:4048:8", ["const:ca6000:8"]]
+ 0057ba6c ["COPY", "register:4048:8", ["const:ca7000:8"]]
- 0057b74c bytes 493900f0
+ 0057ba6c bytes 69390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52453e61116b9144303a3786a6555140"></a>

### [`0057b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b7b8.md) → [`0057bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bad8.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewFilter

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00589cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589cb4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057bb00",
      "incomplete_value": true,
      "site": "0057bb00",
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
      "definition_site": "0057b7e0",
      "incomplete_value": true,
      "site": "0057b7e0",
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
      "0057bafc",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057bb54",
      "READ",
      [
        "storage",
        "00ca63c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057bafc",
      "READ",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ],
    [
      "0057bb54",
      "READ",
      [
        "storage",
        "00ca7380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b7b8.md#insn-0057b7d4) · [`0057b7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b7b8.md#insn-0057b7d8) · [`0057b7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b7b8.md#insn-0057b7e4)
- 新版 [`0057baf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bad8.md#insn-0057baf4) · [`0057baf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bad8.md#insn-0057baf8) · [`0057bb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bad8.md#insn-0057bb04)

~~~diff
- 0057b7d4 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0057baf4 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0057b7d4 bytes 483900f0
+ 0057baf4 bytes 68390090
- 0057b7d8 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0057b7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057baf8 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0057baf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057baf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057baf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b7d8 bytes 08010d91
+ 0057baf8 bytes 08010c91
- 0057b7e4 ["COPY", "register:4098:8", ["const:ca6000:8"]]
+ 0057bb04 ["COPY", "register:4098:8", ["const:ca7000:8"]]
- 0057b7e4 bytes 533900f0
+ 0057bb04 bytes 73390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc386129a3cf90e141f499e5f7bb2a5f"></a>

### [`0057b8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b8f0.md) → [`0057bc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bc10.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewResult

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00589cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589cb4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057bc40",
      "incomplete_value": true,
      "site": "0057bc40",
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
      "definition_site": "0057b920",
      "incomplete_value": true,
      "site": "0057b920",
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
      "0057bc3c",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057bc94",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057bc3c",
      "READ",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ],
    [
      "0057bc94",
      "READ",
      [
        "storage",
        "00ca7350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b8f0.md#insn-0057b914) · [`0057b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b8f0.md#insn-0057b918) · [`0057b924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b8f0.md#insn-0057b924)
- 新版 [`0057bc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bc10.md#insn-0057bc34) · [`0057bc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bc10.md#insn-0057bc38) · [`0057bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bc10.md#insn-0057bc44)

~~~diff
- 0057b914 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0057bc34 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0057b914 bytes 483900f0
+ 0057bc34 bytes 68390090
- 0057b918 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0057b918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057bc38 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0057bc38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057bc38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057bc38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b918 bytes 08010d91
+ 0057bc38 bytes 08010c91
- 0057b924 ["COPY", "register:40a8:8", ["const:ca6000:8"]]
+ 0057bc44 ["COPY", "register:40a8:8", ["const:ca7000:8"]]
- 0057b924 bytes 553900f0
+ 0057bc44 bytes 75390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72a3cc568ace4fee7ff71fcc0022dbb1"></a>

### [`0057ba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057ba28.md) → [`0057bd48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bd48.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewEvalResult

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00589cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589cb4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057bd78",
      "incomplete_value": true,
      "site": "0057bd78",
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
      "definition_site": "0057ba58",
      "incomplete_value": true,
      "site": "0057ba58",
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
      "0057bd74",
      "READ",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ],
    [
      "0057be10",
      "READ",
      [
        "storage",
        "00ca63a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057bd74",
      "READ",
      [
        "storage",
        "00ca7318",
        null,
        "undefined8"
      ]
    ],
    [
      "0057be10",
      "READ",
      [
        "storage",
        "00ca7368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057ba28.md#insn-0057ba4c) · [`0057ba50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057ba28.md#insn-0057ba50) · [`0057ba5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057ba28.md#insn-0057ba5c)
- 新版 [`0057bd6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bd48.md#insn-0057bd6c) · [`0057bd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bd48.md#insn-0057bd70) · [`0057bd7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bd48.md#insn-0057bd7c)

~~~diff
- 0057ba4c ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0057bd6c ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0057ba4c bytes 483900f0
+ 0057bd6c bytes 68390090
- 0057ba50 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0057ba50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057bd70 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0057bd70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057bd70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057bd70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ba50 bytes 08610d91
+ 0057bd70 bytes 08610c91
- 0057ba5c ["COPY", "register:40a8:8", ["const:ca6000:8"]]
+ 0057bd7c ["COPY", "register:40a8:8", ["const:ca7000:8"]]
- 0057ba5c bytes 553900f0
+ 0057bd7c bytes 75390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f806c8f0c62b6e6e2dfd8e04d4ba2914"></a>

### [`0057bbbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bbbc.md) → [`0057bedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bedc.md) FUN_0057bedc

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
      "definition_site": "0057bef4",
      "incomplete_value": false,
      "site": "0057bef8",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057bbd4",
      "incomplete_value": false,
      "site": "0057bbd8",
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
            "const:cb8:8"
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
      "0057bef8",
      "DATA",
      [
        "storage",
        "00c6bcb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057bef8",
      "DATA",
      [
        "storage",
        "00c6cc88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bbbc.md#insn-0057bbd0) · [`0057bbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bbbc.md#insn-0057bbd4) · [`0057bc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bbbc.md#insn-0057bc08)
- 新版 [`0057bef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bedc.md#insn-0057bef0) · [`0057bef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bedc.md#insn-0057bef4) · [`0057bf28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057b/0057bedc.md#insn-0057bf28)

~~~diff
- 0057bbd0 ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 0057bef0 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0057bbd0 bytes 89370090
+ 0057bef0 bytes 893700b0
- 0057bbd4 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 0057bbd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057bbd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057bbd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057bef4 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 0057bef4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bef4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bef4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057bbd4 bytes 29e13291
+ 0057bef4 bytes 29213291
- 0057bc08 ["INT_ADD", "register:40f0:8", ["const:57bc08:8", "const:4:8"]]
- 0057bc08 ["CALL", null, ["callee:00c58f50:8"]]
+ 0057bf28 ["INT_ADD", "register:40f0:8", ["const:57bf28:8", "const:4:8"]]
+ 0057bf28 ["CALL", null, ["callee:00c58f50:8"]]
- 0057bc08 bytes de701b94
+ 0057bf28 bytes 0a741b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52251d9ca72a8d2f3dd03208b9955006"></a>

### [`0057c050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c050.md) → [`0057c370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c370.md) FUN_0057c370

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
      "definition_site": "0057c374",
      "incomplete_value": false,
      "site": "0057c378",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c054",
      "incomplete_value": false,
      "site": "0057c058",
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
            "const:f50:8"
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
      "0057c378",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c378",
      "DATA",
      [
        "storage",
        "00c6cf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c050.md#insn-0057c050) · [`0057c054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c050.md#insn-0057c054)
- 新版 [`0057c370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c370.md#insn-0057c370) · [`0057c374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c370.md#insn-0057c374)

~~~diff
- 0057c050 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c370 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c050 bytes 683700f0
+ 0057c370 bytes 88370090
- 0057c054 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0057c054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c374 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0057c374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c054 bytes 08413d91
+ 0057c374 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c943e145b6b6ff28215bd5ac73e0db8"></a>

### [`0057c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c060.md) → [`0057c380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c380.md) FUN_0057c380

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
      "definition_site": "0057c390",
      "incomplete_value": false,
      "site": "0057c398",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c070",
      "incomplete_value": false,
      "site": "0057c078",
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
            "const:f50:8"
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
      "0057c398",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c398",
      "DATA",
      [
        "storage",
        "00c6cf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c060.md#insn-0057c06c) · [`0057c070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c060.md#insn-0057c070) · [`0057c07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c060.md#insn-0057c07c)
- 新版 [`0057c38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c380.md#insn-0057c38c) · [`0057c390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c380.md#insn-0057c390) · [`0057c39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c380.md#insn-0057c39c)

~~~diff
- 0057c06c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c38c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c06c bytes 683700f0
+ 0057c38c bytes 88370090
- 0057c070 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0057c070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c390 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0057c390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c070 bytes 08413d91
+ 0057c390 bytes 08813c91
- 0057c07c ["INT_ADD", "register:40f0:8", ["const:57c07c:8", "const:4:8"]]
- 0057c07c ["CALL", null, ["callee:00c58f40:8"]]
+ 0057c39c ["INT_ADD", "register:40f0:8", ["const:57c39c:8", "const:4:8"]]
+ 0057c39c ["CALL", null, ["callee:00c58f40:8"]]
- 0057c07c bytes bd6f1b94
+ 0057c39c bytes e9721b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f766d3e5924483a9a20060d9d33fbfee"></a>

### [`0057c0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0a0.md) → [`0057c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3c0.md) FUN_0057c3c0

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
      "definition_site": "0057c3c4",
      "incomplete_value": false,
      "site": "0057c3c8",
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
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c0a4",
      "incomplete_value": false,
      "site": "0057c0a8",
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
            "const:fa0:8"
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
      "0057c3c8",
      "DATA",
      [
        "storage",
        "00c6bfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c3c8",
      "DATA",
      [
        "storage",
        "00c6cf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0a0.md#insn-0057c0a0) · [`0057c0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0a0.md#insn-0057c0a4)
- 新版 [`0057c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3c0.md#insn-0057c3c0) · [`0057c3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3c0.md#insn-0057c3c4)

~~~diff
- 0057c0a0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c3c0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c0a0 bytes 683700f0
+ 0057c3c0 bytes 88370090
- 0057c0a4 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 0057c0a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c0a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c0a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c3c4 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 0057c3c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c3c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c3c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c0a4 bytes 08813e91
+ 0057c3c4 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33d83b8c563fdac68c4cbd338e073fdb"></a>

### [`0057c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0b0.md) → [`0057c3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3d0.md) FUN_0057c3d0

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
      "definition_site": "0057c3e0",
      "incomplete_value": false,
      "site": "0057c3e8",
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
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c0c0",
      "incomplete_value": false,
      "site": "0057c0c8",
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
            "const:fa0:8"
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
      "0057c3e8",
      "DATA",
      [
        "storage",
        "00c6bfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c3e8",
      "DATA",
      [
        "storage",
        "00c6cf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0b0.md#insn-0057c0bc) · [`0057c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0b0.md#insn-0057c0c0) · [`0057c0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0b0.md#insn-0057c0cc)
- 新版 [`0057c3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3d0.md#insn-0057c3dc) · [`0057c3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3d0.md#insn-0057c3e0) · [`0057c3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c3d0.md#insn-0057c3ec)

~~~diff
- 0057c0bc ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c3dc ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c0bc bytes 683700f0
+ 0057c3dc bytes 88370090
- 0057c0c0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 0057c0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c3e0 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 0057c3e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c3e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c3e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c0c0 bytes 08813e91
+ 0057c3e0 bytes 08c13d91
- 0057c0cc ["INT_ADD", "register:40f0:8", ["const:57c0cc:8", "const:4:8"]]
- 0057c0cc ["CALL", null, ["callee:00c58f40:8"]]
+ 0057c3ec ["INT_ADD", "register:40f0:8", ["const:57c3ec:8", "const:4:8"]]
+ 0057c3ec ["CALL", null, ["callee:00c58f40:8"]]
- 0057c0cc bytes a96f1b94
+ 0057c3ec bytes d5721b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09d2dbcfad8d7488371b66fdef7bb17"></a>

### [`0057c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md) → [`0057c56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c56c.md) FUN_0057c56c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0057c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md) [`0057c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`0057c410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c410.md) [`0057c690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c690.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0057c578",
      "incomplete_value": false,
      "site": "0057c57c",
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
      "definition_site": "0057c258",
      "incomplete_value": false,
      "site": "0057c25c",
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
      "0057c578",
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
      "0057c578",
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

- 旧版 [`0057c25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md#insn-0057c25c) · [`0057c254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md#insn-0057c254) · [`0057c258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md#insn-0057c258)
- 新版 [`0057c57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c56c.md#insn-0057c57c) · [`0057c574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c56c.md#insn-0057c574) · [`0057c578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c56c.md#insn-0057c578)

~~~diff
- 0057c25c ["INT_ADD", "register:40f0:8", ["const:57c25c:8", "const:4:8"]]
- 0057c25c ["CALL", null, ["callee:0043bad8:8"]]
+ 0057c57c ["INT_ADD", "register:40f0:8", ["const:57c57c:8", "const:4:8"]]
+ 0057c57c ["CALL", null, ["callee:0043bad8:8"]]
- 0057c25c bytes 57fdfa97
+ 0057c57c bytes 57fdfa97
- 0057c254 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0057c574 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0057c254 bytes c0e9fff0
+ 0057c574 bytes e0e9ff90
- 0057c258 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0057c258 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057c258 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057c258 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c578 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0057c578 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c578 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c578 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057c258 bytes 00303e91
+ 0057c578 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5b7536ec74cd94ba9e3382ff62bc388"></a>

### [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md) → [`0057c67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md) FUN_0057c67c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0057a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a2e4.md) [`0057a33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a33c.md) [`0057a384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a384.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 3件 [`0057a604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a604.md) [`0057a65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a65c.md) [`0057a6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057a6a4.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "0057c688",
      "incomplete_value": false,
      "site": "0057c68c",
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
      "definition_site": "0057c368",
      "incomplete_value": false,
      "site": "0057c36c",
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
      "0057c688",
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
      "0057c688",
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

- 旧版 [`0057c36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md#insn-0057c36c) · [`0057c364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md#insn-0057c364) · [`0057c368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md#insn-0057c368)
- 新版 [`0057c68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md#insn-0057c68c) · [`0057c684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md#insn-0057c684) · [`0057c688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c67c.md#insn-0057c688)

~~~diff
- 0057c36c ["INT_ADD", "register:40f0:8", ["const:57c36c:8", "const:4:8"]]
- 0057c36c ["CALL", null, ["callee:00442c90:8"]]
+ 0057c68c ["INT_ADD", "register:40f0:8", ["const:57c68c:8", "const:4:8"]]
+ 0057c68c ["CALL", null, ["callee:00442c90:8"]]
- 0057c36c bytes 8119fb97
+ 0057c68c bytes 8119fb97
- 0057c364 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0057c684 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0057c364 bytes c0e9fff0
+ 0057c684 bytes e0e9ff90
- 0057c368 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0057c368 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057c368 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057c368 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c688 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0057c688 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c688 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c688 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057c368 bytes 00303e91
+ 0057c688 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68fc6228dfe942ea097f6cd4be703de5"></a>

### [`0057c4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4cc.md) → [`0057c7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7ec.md) FUN_0057c7ec

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
      "definition_site": "0057c7f0",
      "incomplete_value": false,
      "site": "0057c7f4",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4d0",
      "incomplete_value": false,
      "site": "0057c4d4",
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
            "const:ff0:8"
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
      "0057c7f4",
      "DATA",
      [
        "storage",
        "00c6bff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c7f4",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4cc.md#insn-0057c4cc) · [`0057c4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4cc.md#insn-0057c4d0)
- 新版 [`0057c7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7ec.md#insn-0057c7ec) · [`0057c7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7ec.md#insn-0057c7f0)

~~~diff
- 0057c4cc ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c7ec ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c4cc bytes 683700f0
+ 0057c7ec bytes 88370090
- 0057c4d0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 0057c4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c7f0 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0057c7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4d0 bytes 08c13f91
+ 0057c7f0 bytes 08013f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95271f9479c08042ae253e2f9c7cc66a"></a>

### [`0057c4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4dc.md) → [`0057c7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7fc.md) FUN_0057c7fc

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
      "definition_site": "0057c80c",
      "incomplete_value": false,
      "site": "0057c814",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4ec",
      "incomplete_value": false,
      "site": "0057c4f4",
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
            "const:ff0:8"
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
      "0057c814",
      "DATA",
      [
        "storage",
        "00c6bff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c814",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4dc.md#insn-0057c4e8) · [`0057c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4dc.md#insn-0057c4ec) · [`0057c4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4dc.md#insn-0057c4f8)
- 新版 [`0057c808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7fc.md#insn-0057c808) · [`0057c80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7fc.md#insn-0057c80c) · [`0057c818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c7fc.md#insn-0057c818)

~~~diff
- 0057c4e8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c808 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c4e8 bytes 683700f0
+ 0057c808 bytes 88370090
- 0057c4ec ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 0057c4ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c80c ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0057c80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4ec bytes 08c13f91
+ 0057c80c bytes 08013f91
- 0057c4f8 ["INT_ADD", "register:40f0:8", ["const:57c4f8:8", "const:4:8"]]
- 0057c4f8 ["CALL", null, ["callee:00c58f40:8"]]
+ 0057c818 ["INT_ADD", "register:40f0:8", ["const:57c818:8", "const:4:8"]]
+ 0057c818 ["CALL", null, ["callee:00c58f40:8"]]
- 0057c4f8 bytes 9e6e1b94
+ 0057c818 bytes ca711b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc6d0b8f4165a5fbeaef3754146f145"></a>

### [`0057c51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c51c.md) → [`0057c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c83c.md) FUN_0057c83c

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
      "definition_site": "0057c840",
      "incomplete_value": false,
      "site": "0057c844",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c520",
      "incomplete_value": false,
      "site": "0057c524",
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
            "const:40:8"
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
      "0057c844",
      "DATA",
      [
        "storage",
        "00c6c040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c844",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c51c.md#insn-0057c51c) · [`0057c520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c51c.md#insn-0057c520)
- 新版 [`0057c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c83c.md#insn-0057c83c) · [`0057c840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c83c.md#insn-0057c840)

~~~diff
- 0057c51c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057c83c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057c51c bytes 88370090
+ 0057c83c bytes 883700b0
- 0057c520 ["COPY", "tmp:0:8", ["const:40:8"]]
- 0057c520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c840 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0057c840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c520 bytes 08010191
+ 0057c840 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55961162904832a70f299a5209083444"></a>

### [`0057c52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c52c.md) → [`0057c84c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c84c.md) FUN_0057c84c

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
      "definition_site": "0057c85c",
      "incomplete_value": false,
      "site": "0057c864",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c53c",
      "incomplete_value": false,
      "site": "0057c544",
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
            "const:40:8"
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
      "0057c864",
      "DATA",
      [
        "storage",
        "00c6c040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c864",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c52c.md#insn-0057c538) · [`0057c53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c52c.md#insn-0057c53c) · [`0057c548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c52c.md#insn-0057c548)
- 新版 [`0057c858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c84c.md#insn-0057c858) · [`0057c85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c84c.md#insn-0057c85c) · [`0057c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c84c.md#insn-0057c868)

~~~diff
- 0057c538 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057c858 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057c538 bytes 88370090
+ 0057c858 bytes 883700b0
- 0057c53c ["COPY", "tmp:0:8", ["const:40:8"]]
- 0057c53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c85c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0057c85c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c85c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c85c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c53c bytes 08010191
+ 0057c85c bytes 08410091
- 0057c548 ["INT_ADD", "register:40f0:8", ["const:57c548:8", "const:4:8"]]
- 0057c548 ["CALL", null, ["callee:00c58f40:8"]]
+ 0057c868 ["INT_ADD", "register:40f0:8", ["const:57c868:8", "const:4:8"]]
+ 0057c868 ["CALL", null, ["callee:00c58f40:8"]]
- 0057c548 bytes 8a6e1b94
+ 0057c868 bytes b6711b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7d8f27a097a63ae9b741c493af0ee2"></a>

### [`0057c64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c64c.md) → [`0057c96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c96c.md) FUN_0057c96c

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
      "definition_site": "0057c970",
      "incomplete_value": false,
      "site": "0057c974",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c650",
      "incomplete_value": false,
      "site": "0057c654",
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
            "const:90:8"
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
      "0057c974",
      "DATA",
      [
        "storage",
        "00c6c090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c974",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c64c.md#insn-0057c64c) · [`0057c650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c64c.md#insn-0057c650)
- 新版 [`0057c96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c96c.md#insn-0057c96c) · [`0057c970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c96c.md#insn-0057c970)

~~~diff
- 0057c64c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057c96c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057c64c bytes 88370090
+ 0057c96c bytes 883700b0
- 0057c650 ["COPY", "tmp:0:8", ["const:90:8"]]
- 0057c650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c970 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0057c970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c650 bytes 08410291
+ 0057c970 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b9e10a99491f56819c9c7887093a29"></a>

### [`0057c65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c65c.md) → [`0057c97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c97c.md) FUN_0057c97c

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
      "definition_site": "0057c98c",
      "incomplete_value": false,
      "site": "0057c994",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c66c",
      "incomplete_value": false,
      "site": "0057c674",
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
            "const:90:8"
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
      "0057c994",
      "DATA",
      [
        "storage",
        "00c6c090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c994",
      "DATA",
      [
        "storage",
        "00c6d060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c65c.md#insn-0057c668) · [`0057c66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c65c.md#insn-0057c66c) · [`0057c678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c65c.md#insn-0057c678)
- 新版 [`0057c988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c97c.md#insn-0057c988) · [`0057c98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c97c.md#insn-0057c98c) · [`0057c998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c97c.md#insn-0057c998)

~~~diff
- 0057c668 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057c988 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057c668 bytes 88370090
+ 0057c988 bytes 883700b0
- 0057c66c ["COPY", "tmp:0:8", ["const:90:8"]]
- 0057c66c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c66c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c66c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c98c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0057c98c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c98c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c98c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c66c bytes 08410291
+ 0057c98c bytes 08810191
- 0057c678 ["INT_ADD", "register:40f0:8", ["const:57c678:8", "const:4:8"]]
- 0057c678 ["CALL", null, ["callee:00c58f40:8"]]
+ 0057c998 ["INT_ADD", "register:40f0:8", ["const:57c998:8", "const:4:8"]]
+ 0057c998 ["CALL", null, ["callee:00c58f40:8"]]
- 0057c678 bytes 3e6e1b94
+ 0057c998 bytes 6a711b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d721c8d00a731a1798dd810055b0bd3"></a>

### [`0057c7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c7fc.md) → [`0057cb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cb1c.md) _INIT_31

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`005765ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765ec.md) [`005765f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765f4.md) [`00576738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576738.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`0057690c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057690c.md) [`00576914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576914.md) [`00576a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a58.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 12件, `store_value` 7件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cb58",
      "incomplete_value": true,
      "site": "0057cb74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c838",
      "incomplete_value": true,
      "site": "0057c854",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057cb7c",
      "incomplete_value": true,
      "site": "0057cb98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c85c",
      "incomplete_value": true,
      "site": "0057c878",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057cb9c",
      "incomplete_value": true,
      "site": "0057cbb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c87c",
      "incomplete_value": true,
      "site": "0057c898",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057cb58",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0057cb7c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0057cb9c",
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
      "0057cb58",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0057cb7c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0057cb9c",
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

- 旧版 [`0057ca34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c7fc.md#insn-0057ca34) · [`0057ca5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c7fc.md#insn-0057ca5c) · [`0057caac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c7fc.md#insn-0057caac)
- 新版 [`0057cd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cb1c.md#insn-0057cd54) · [`0057cd7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cb1c.md#insn-0057cd7c)

~~~diff
- 0057ca34 ["INT_ADD", "register:40f0:8", ["const:57ca34:8", "const:4:8"]]
- 0057ca34 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0057cd54 ["INT_ADD", "register:40f0:8", ["const:57cd54:8", "const:4:8"]]
+ 0057cd54 ["CALL", null, ["callee:00c58ed0:8"]]
- 0057ca34 bytes 336d1b94
+ 0057cd54 bytes 5f701b94
- 0057ca5c ["INT_ADD", "register:40f0:8", ["const:57ca5c:8", "const:4:8"]]
- 0057ca5c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0057cd7c ["INT_ADD", "register:40f0:8", ["const:57cd7c:8", "const:4:8"]]
+ 0057cd7c ["CALL", null, ["callee:00c58ed0:8"]]
- 0057ca5c bytes 296d1b94
+ 0057cd7c bytes 55701b94
- 0057caac ["INT_ADD", "register:40f0:8", ["const:57caac:8", "const:4:8"]]
- 0057caac ["CALL", null, ["callee:00c58ed0:8"]]
- 0057caac bytes 156d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55426f644c78b1cc9015402ee5108154"></a>

### [`0057cc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cc58.md) → [`0057cf78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cf78.md) FUN_0057cf78

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cf98",
      "incomplete_value": false,
      "site": "0057cf98",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc78",
      "incomplete_value": false,
      "site": "0057cc78",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cf98",
      "incomplete_value": false,
      "site": "0057cf98",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc78",
      "incomplete_value": false,
      "site": "0057cc78",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057cf98",
      "DATA",
      [
        "storage",
        "00c6c0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cf98",
      "DATA",
      [
        "storage",
        "00c6c1a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cf98",
      "DATA",
      [
        "storage",
        "00c6d0b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cf98",
      "DATA",
      [
        "storage",
        "00c6d178",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cc58.md#insn-0057cc68) · [`0057cc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cc58.md#insn-0057cc6c) · [`0057cc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cc58.md#insn-0057cc80)
- 新版 [`0057cf88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cf78.md#insn-0057cf88) · [`0057cf8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cf78.md#insn-0057cf8c) · [`0057cfa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cf78.md#insn-0057cfa0)

~~~diff
- 0057cc68 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057cf88 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057cc68 bytes 88370090
+ 0057cf88 bytes 883700b0
- 0057cc6c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0057cc6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cf8c ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 0057cf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cc6c bytes 08810391
+ 0057cf8c bytes 08c10291
- 0057cc80 ["INT_ADD", "register:40f0:8", ["const:57cc80:8", "const:4:8"]]
- 0057cc80 ["CALL", null, ["callee:00c5b1e0:8"]]
+ 0057cfa0 ["INT_ADD", "register:40f0:8", ["const:57cfa0:8", "const:4:8"]]
+ 0057cfa0 ["CALL", null, ["callee:00c5b1e0:8"]]
- 0057cc80 bytes 64751b94
+ 0057cfa0 bytes 90781b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb77397b1dec2ff09ec7d9c3ad51a01f"></a>

### [`0057ccb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057ccb8.md) → [`0057cfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cfd8.md) FUN_0057cfd8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cff8",
      "incomplete_value": false,
      "site": "0057cff8",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ccd8",
      "incomplete_value": false,
      "site": "0057ccd8",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cff8",
      "incomplete_value": false,
      "site": "0057cff8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ccd8",
      "incomplete_value": false,
      "site": "0057ccd8",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057cff8",
      "DATA",
      [
        "storage",
        "00c6c0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cff8",
      "DATA",
      [
        "storage",
        "00c6c1a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cff8",
      "DATA",
      [
        "storage",
        "00c6d0b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cff8",
      "DATA",
      [
        "storage",
        "00c6d178",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ccc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057ccb8.md#insn-0057ccc8) · [`0057cccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057ccb8.md#insn-0057cccc) · [`0057cce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057ccb8.md#insn-0057cce0)
- 新版 [`0057cfe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cfd8.md#insn-0057cfe8) · [`0057cfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cfd8.md#insn-0057cfec) · [`0057d000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057cfd8.md#insn-0057d000)

~~~diff
- 0057ccc8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057cfe8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057ccc8 bytes 88370090
+ 0057cfe8 bytes 883700b0
- 0057cccc ["COPY", "tmp:0:8", ["const:e0:8"]]
- 0057cccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cfec ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 0057cfec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cfec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cfec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cccc bytes 08810391
+ 0057cfec bytes 08c10291
- 0057cce0 ["INT_ADD", "register:40f0:8", ["const:57cce0:8", "const:4:8"]]
- 0057cce0 ["CALL", null, ["callee:00c5b1e0:8"]]
+ 0057d000 ["INT_ADD", "register:40f0:8", ["const:57d000:8", "const:4:8"]]
+ 0057d000 ["CALL", null, ["callee:00c5b1e0:8"]]
- 0057cce0 bytes 4c751b94
+ 0057d000 bytes 78781b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-768bac99db368fdd48a45595c5c5ffdf"></a>

### [`0057cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md) → [`0057d218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d218.md) FUN_0057d218

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0058af84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d388",
      "incomplete_value": false,
      "site": "0057d394",
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
      "definition_site": "0057d068",
      "incomplete_value": false,
      "site": "0057d074",
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
      "0057d394",
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
      "0057d394",
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

- 旧版 [`0057cf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md#insn-0057cf44) · [`0057cf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md#insn-0057cf60) · [`0057cf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md#insn-0057cf98)
- 新版 [`0057d264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d218.md#insn-0057d264) · [`0057d280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d218.md#insn-0057d280) · [`0057d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d218.md#insn-0057d2b8)

~~~diff
- 0057cf44 ["INT_ADD", "register:40f0:8", ["const:57cf44:8", "const:4:8"]]
- 0057cf44 ["CALL", null, ["callee:00c58f30:8"]]
+ 0057d264 ["INT_ADD", "register:40f0:8", ["const:57d264:8", "const:4:8"]]
+ 0057d264 ["CALL", null, ["callee:00c58f30:8"]]
- 0057cf44 bytes 076c1b94
+ 0057d264 bytes 336f1b94
- 0057cf60 ["INT_ADD", "register:40f0:8", ["const:57cf60:8", "const:4:8"]]
- 0057cf60 ["CALL", null, ["callee:00c59130:8"]]
+ 0057d280 ["INT_ADD", "register:40f0:8", ["const:57d280:8", "const:4:8"]]
+ 0057d280 ["CALL", null, ["callee:00c59130:8"]]
- 0057cf60 bytes 806c1b94
+ 0057d280 bytes ac6f1b94
- 0057cf98 ["INT_ADD", "register:40f0:8", ["const:57cf98:8", "const:4:8"]]
- 0057cf98 ["CALL", null, ["callee:00c5b220:8"]]
+ 0057d2b8 ["INT_ADD", "register:40f0:8", ["const:57d2b8:8", "const:4:8"]]
+ 0057d2b8 ["CALL", null, ["callee:00c5b220:8"]]
- 0057cf98 bytes ae741b94
+ 0057d2b8 bytes da771b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d80d8eb557c44b54f1b551d53ea617a"></a>

### [`0057d4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md) → [`0057d7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d7f4.md) FUN_0057d7f4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0058af84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d96c",
      "incomplete_value": false,
      "site": "0057d978",
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
      "definition_site": "0057d64c",
      "incomplete_value": false,
      "site": "0057d658",
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
      "0057d978",
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
      "0057d978",
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

- 旧版 [`0057d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md#insn-0057d520) · [`0057d53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md#insn-0057d53c) · [`0057d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md#insn-0057d578)
- 新版 [`0057d840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d7f4.md#insn-0057d840) · [`0057d85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d7f4.md#insn-0057d85c) · [`0057d898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057d7f4.md#insn-0057d898)

~~~diff
- 0057d520 ["INT_ADD", "register:40f0:8", ["const:57d520:8", "const:4:8"]]
- 0057d520 ["CALL", null, ["callee:00c58f30:8"]]
+ 0057d840 ["INT_ADD", "register:40f0:8", ["const:57d840:8", "const:4:8"]]
+ 0057d840 ["CALL", null, ["callee:00c58f30:8"]]
- 0057d520 bytes 906a1b94
+ 0057d840 bytes bc6d1b94
- 0057d53c ["INT_ADD", "register:40f0:8", ["const:57d53c:8", "const:4:8"]]
- 0057d53c ["CALL", null, ["callee:00c59130:8"]]
+ 0057d85c ["INT_ADD", "register:40f0:8", ["const:57d85c:8", "const:4:8"]]
+ 0057d85c ["CALL", null, ["callee:00c59130:8"]]
- 0057d53c bytes 096b1b94
+ 0057d85c bytes 356e1b94
- 0057d578 ["INT_ADD", "register:40f0:8", ["const:57d578:8", "const:4:8"]]
- 0057d578 ["CALL", null, ["callee:00c5b120:8"]]
+ 0057d898 ["INT_ADD", "register:40f0:8", ["const:57d898:8", "const:4:8"]]
+ 0057d898 ["CALL", null, ["callee:00c5b120:8"]]
- 0057d578 bytes f6721b94
+ 0057d898 bytes 22761b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0beaf5e729dcceff034c13380626eba"></a>

### [`0057d9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d9e8.md) → [`0057dd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dd08.md) FUN_0057dd08

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md) [`00c5a230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a230.md)
- 新版 呼出元 1件 [`00550f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f04.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md) [`00c5b200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b200.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dd60",
      "incomplete_value": false,
      "site": "0057dd6c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057da40",
      "incomplete_value": false,
      "site": "0057da4c",
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
            "const:380:8"
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
      "definition_site": "0057dd80",
      "incomplete_value": false,
      "site": "0057dd80",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057da60",
      "incomplete_value": false,
      "site": "0057da60",
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
            "const:e0:8"
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
      "definition_site": "0057dd84",
      "incomplete_value": false,
      "site": "0057dd88",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057da64",
      "incomplete_value": false,
      "site": "0057da68",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057dd28",
      "READ",
      [
        "storage",
        "00c9b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0057dd3c",
      "READ",
      [
        "storage",
        "00ca63b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057dd6c",
      "DATA",
      [
        "storage",
        "00c6c380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dd28",
      "READ",
      [
        "storage",
        "00c9c370",
        null,
        "pointer"
      ]
    ],
    [
      "0057dd3c",
      "READ",
      [
        "storage",
        "00ca7378",
        null,
        "undefined8"
      ]
    ],
    [
      "0057dd6c",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d9e8.md#insn-0057da00) · [`0057da08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d9e8.md#insn-0057da08) · [`0057da28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d9e8.md#insn-0057da28)
- 新版 [`0057dd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dd08.md#insn-0057dd20) · [`0057dd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dd08.md#insn-0057dd28) · [`0057dd48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dd08.md#insn-0057dd48)

~~~diff
- 0057da00 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0057dd20 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0057da00 bytes e83800d0
+ 0057dd20 bytes e83800f0
- 0057da08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
- 0057da08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057dd28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 0057dd28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057da08 bytes 08d141f9
+ 0057dd28 bytes 08b941f9
- 0057da28 ["INT_ADD", "register:40f0:8", ["const:57da28:8", "const:4:8"]]
- 0057da28 ["CALL", null, ["callee:00c5b200:8"]]
+ 0057dd48 ["INT_ADD", "register:40f0:8", ["const:57dd48:8", "const:4:8"]]
+ 0057dd48 ["CALL", null, ["callee:00c5b200:8"]]
- 0057da28 bytes 02721b94
+ 0057dd48 bytes 2e751b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e86b6dc093bf3d68a7fd63e6730dd2f6"></a>

### [`0057db80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057db80.md) → [`0057dea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dea0.md) FUN_0057dea0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057deb0",
      "incomplete_value": false,
      "site": "0057deb0",
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
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db90",
      "incomplete_value": false,
      "site": "0057db90",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057deb0",
      "incomplete_value": false,
      "site": "0057deb0",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:190:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db90",
      "incomplete_value": false,
      "site": "0057db90",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057deb0",
      "DATA",
      [
        "storage",
        "00c6c1c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057deb0",
      "DATA",
      [
        "storage",
        "00c6c288",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057deb0",
      "DATA",
      [
        "storage",
        "00c6d190",
        null,
        "undefined *"
      ]
    ],
    [
      "0057deb0",
      "DATA",
      [
        "storage",
        "00c6d258",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057db80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057db80.md#insn-0057db80) · [`0057db84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057db80.md#insn-0057db84)
- 新版 [`0057dea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dea0.md#insn-0057dea0) · [`0057dea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dea0.md#insn-0057dea4)

~~~diff
- 0057db80 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057dea0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057db80 bytes 683700f0
+ 0057dea0 bytes 88370090
- 0057db84 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 0057db84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057db84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057db84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dea4 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 0057dea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057db84 bytes 08010791
+ 0057dea4 bytes 08410691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b171c581178658bfd4e0709adb6c5ef0"></a>

### [`0057dba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dba4.md) → [`0057dec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dec4.md) FUN_0057dec4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ded4",
      "incomplete_value": true,
      "site": "0057ded4",
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
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbb4",
      "incomplete_value": true,
      "site": "0057dbb4",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ded4",
      "incomplete_value": true,
      "site": "0057ded4",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:190:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbb4",
      "incomplete_value": true,
      "site": "0057dbb4",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057ded4",
      "DATA",
      [
        "storage",
        "00c6c1c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ded4",
      "DATA",
      [
        "storage",
        "00c6c288",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057ded4",
      "DATA",
      [
        "storage",
        "00c6d190",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ded4",
      "DATA",
      [
        "storage",
        "00c6d258",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dba4.md#insn-0057dba4) · [`0057dba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dba4.md#insn-0057dba8) · [`0057dbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dba4.md#insn-0057dbd4)
- 新版 [`0057dec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dec4.md#insn-0057dec4) · [`0057dec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dec4.md#insn-0057dec8) · [`0057def4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dec4.md#insn-0057def4)

~~~diff
- 0057dba4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057dec4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057dba4 bytes 683700f0
+ 0057dec4 bytes 88370090
- 0057dba8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 0057dba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dec8 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 0057dec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dba8 bytes 08010791
+ 0057dec8 bytes 08410691
- 0057dbd4 ["INT_ADD", "register:40f0:8", ["const:57dbd4:8", "const:4:8"]]
- 0057dbd4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0057def4 ["INT_ADD", "register:40f0:8", ["const:57def4:8", "const:4:8"]]
+ 0057def4 ["CALL", null, ["callee:00c58f50:8"]]
- 0057dbd4 bytes eb681b94
+ 0057def4 bytes 176c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88e0d1e0fc2f6ec5d8c995021777dbc"></a>

### [`0057dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dbe8.md) → [`0057df08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057df08.md) FUN_0057df08

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
      "definition_site": "0057df0c",
      "incomplete_value": false,
      "site": "0057df10",
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
      "definition_site": "0057dbec",
      "incomplete_value": false,
      "site": "0057dbf0",
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
      "0057df10",
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
      "0057df10",
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

- 旧版 [`0057dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dbe8.md#insn-0057dbe8) · [`0057dbec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dbe8.md#insn-0057dbec)
- 新版 [`0057df08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057df08.md#insn-0057df08) · [`0057df0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057df08.md#insn-0057df0c)

~~~diff
- 0057dbe8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057df08 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057dbe8 bytes 683700f0
+ 0057df08 bytes 88370090
- 0057dbec ["COPY", "tmp:0:8", ["const:330:8"]]
- 0057dbec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057df0c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0057df0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dbec bytes 08c10c91
+ 0057df0c bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-283f0812d7f61b0b9d5d0bd96510cd0a"></a>

### [`0057dc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc38.md) → [`0057df58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057df58.md) FUN_0057df58

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
      "definition_site": "0057df5c",
      "incomplete_value": false,
      "site": "0057df60",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dc3c",
      "incomplete_value": false,
      "site": "0057dc40",
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
            "const:380:8"
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
      "0057df60",
      "DATA",
      [
        "storage",
        "00c6c380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057df60",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc38.md#insn-0057dc38) · [`0057dc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc38.md#insn-0057dc3c)
- 新版 [`0057df58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057df58.md#insn-0057df58) · [`0057df5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057df58.md#insn-0057df5c)

~~~diff
- 0057dc38 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057df58 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057dc38 bytes 683700f0
+ 0057df58 bytes 88370090
- 0057dc3c ["COPY", "tmp:0:8", ["const:380:8"]]
- 0057dc3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057df5c ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0057df5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057df5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dc3c bytes 08010e91
+ 0057df5c bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9144d1fc3d8724bf81a2015b6e1a9140"></a>

### [`0057dc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc88.md) → [`0057dfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfa8.md) FUN_0057dfa8

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
      "definition_site": "0057dfac",
      "incomplete_value": false,
      "site": "0057dfb0",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dc8c",
      "incomplete_value": false,
      "site": "0057dc90",
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
            "const:3d0:8"
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
      "0057dfb0",
      "DATA",
      [
        "storage",
        "00c6c3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dfb0",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc88.md#insn-0057dc88) · [`0057dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc88.md#insn-0057dc8c)
- 新版 [`0057dfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfa8.md#insn-0057dfa8) · [`0057dfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfa8.md#insn-0057dfac)

~~~diff
- 0057dc88 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057dfa8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057dc88 bytes 683700f0
+ 0057dfa8 bytes 88370090
- 0057dc8c ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 0057dc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dfac ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 0057dfac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dfac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dfac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dc8c bytes 08410f91
+ 0057dfac bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0238fc523f7f8e419c461f5baa7ce50a"></a>

### [`0057dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc98.md) → [`0057dfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfb8.md) FUN_0057dfb8

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
      "definition_site": "0057dfc8",
      "incomplete_value": false,
      "site": "0057dfd0",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dca8",
      "incomplete_value": false,
      "site": "0057dcb0",
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
            "const:3d0:8"
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
      "0057dfd0",
      "DATA",
      [
        "storage",
        "00c6c3d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dfd0",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc98.md#insn-0057dca4) · [`0057dca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc98.md#insn-0057dca8) · [`0057dcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc98.md#insn-0057dcb4)
- 新版 [`0057dfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfb8.md#insn-0057dfc4) · [`0057dfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfb8.md#insn-0057dfc8) · [`0057dfd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057d/0057dfb8.md#insn-0057dfd4)

~~~diff
- 0057dca4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057dfc4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057dca4 bytes 683700f0
+ 0057dfc4 bytes 88370090
- 0057dca8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 0057dca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dfc8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 0057dfc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dfc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dfc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dca8 bytes 08410f91
+ 0057dfc8 bytes 08810e91
- 0057dcb4 ["INT_ADD", "register:40f0:8", ["const:57dcb4:8", "const:4:8"]]
- 0057dcb4 ["CALL", null, ["callee:00c58f40:8"]]
+ 0057dfd4 ["INT_ADD", "register:40f0:8", ["const:57dfd4:8", "const:4:8"]]
+ 0057dfd4 ["CALL", null, ["callee:00c58f40:8"]]
- 0057dcb4 bytes af681b94
+ 0057dfd4 bytes db6b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84a96d1c1a7a52019de92e602279ac52"></a>

### [`0057e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md) → [`0057e3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3f0.md) FUN_0057e3f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00550c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c48.md) [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`00586324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`00550f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f68.md) [`00585a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md) [`00586644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00586/00586644.md) · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e424",
      "incomplete_value": false,
      "site": "0057e42c",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e104",
      "incomplete_value": false,
      "site": "0057e10c",
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
            "const:498:8"
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
      "0057e42c",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e444",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e42c",
      "DATA",
      [
        "storage",
        "00c6d468",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e444",
      "DATA",
      [
        "storage",
        "00c6d3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md#insn-0057e0fc) · [`0057e100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md#insn-0057e100) · [`0057e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md#insn-0057e104)
- 新版 [`0057e41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3f0.md#insn-0057e41c) · [`0057e420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3f0.md#insn-0057e420) · [`0057e424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e3f0.md#insn-0057e424)

~~~diff
- 0057e0fc ["INT_ADD", "register:40f0:8", ["const:57e0fc:8", "const:4:8"]]
- 0057e0fc ["CALL", null, ["callee:00c58f30:8"]]
+ 0057e41c ["INT_ADD", "register:40f0:8", ["const:57e41c:8", "const:4:8"]]
+ 0057e41c ["CALL", null, ["callee:00c58f30:8"]]
- 0057e0fc bytes 99671b94
+ 0057e41c bytes c56a1b94
- 0057e100 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057e420 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057e100 bytes 683700d0
+ 0057e420 bytes 683700f0
- 0057e104 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0057e104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e424 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0057e424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e104 bytes 08611291
+ 0057e424 bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cad850f5722d8c00cba69c8e54d203ee"></a>

### [`0057e1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e1a4.md) → [`0057e4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e4c4.md) FUN_0057e4c4

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e4dc",
      "incomplete_value": true,
      "site": "0057e4e0",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e1bc",
      "incomplete_value": true,
      "site": "0057e1c0",
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
            "const:420:8"
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
      "0057e4e0",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e4e0",
      "DATA",
      [
        "storage",
        "00c6d3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e1a4.md#insn-0057e1b8) · [`0057e1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e1a4.md#insn-0057e1bc) · [`0057e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e1a4.md#insn-0057e1d0)
- 新版 [`0057e4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e4c4.md#insn-0057e4d8) · [`0057e4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e4c4.md#insn-0057e4dc) · [`0057e4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e4c4.md#insn-0057e4f0)

~~~diff
- 0057e1b8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057e4d8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057e1b8 bytes 683700d0
+ 0057e4d8 bytes 683700f0
- 0057e1bc ["COPY", "tmp:0:8", ["const:420:8"]]
- 0057e1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e4dc ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0057e4dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e4dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e4dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e1bc bytes 08811091
+ 0057e4dc bytes 08c10f91
- 0057e1d0 ["INT_ADD", "register:40f0:8", ["const:57e1d0:8", "const:4:8"]]
- 0057e1d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057e4f0 ["INT_ADD", "register:40f0:8", ["const:57e4f0:8", "const:4:8"]]
+ 0057e4f0 ["CALL", null, ["callee:00c54d90:8"]]
- 0057e1d0 bytes f4561b94
+ 0057e4f0 bytes 285a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed983e01a6e9b8b2f9a0f78664403b3"></a>

### [`0057e21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e21c.md) → [`0057e53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e53c.md) FUN_0057e53c

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
      "definition_site": "0057e554",
      "incomplete_value": false,
      "site": "0057e558",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e234",
      "incomplete_value": false,
      "site": "0057e238",
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
            "const:420:8"
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
      "0057e558",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e558",
      "DATA",
      [
        "storage",
        "00c6d3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e21c.md#insn-0057e230) · [`0057e234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e21c.md#insn-0057e234) · [`0057e248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e21c.md#insn-0057e248)
- 新版 [`0057e550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e53c.md#insn-0057e550) · [`0057e554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e53c.md#insn-0057e554) · [`0057e568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e53c.md#insn-0057e568)

~~~diff
- 0057e230 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057e550 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057e230 bytes 683700d0
+ 0057e550 bytes 683700f0
- 0057e234 ["COPY", "tmp:0:8", ["const:420:8"]]
- 0057e234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e554 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0057e554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e234 bytes 08811091
+ 0057e554 bytes 08c10f91
- 0057e248 ["INT_ADD", "register:40f0:8", ["const:57e248:8", "const:4:8"]]
- 0057e248 ["CALL", null, ["callee:00c54d90:8"]]
+ 0057e568 ["INT_ADD", "register:40f0:8", ["const:57e568:8", "const:4:8"]]
+ 0057e568 ["CALL", null, ["callee:00c54d90:8"]]
- 0057e248 bytes d6561b94
+ 0057e568 bytes 0a5a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42c39a815dc78985e81344cfaa86c1f2"></a>

### [`0057e294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e294.md) → [`0057e5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e5b4.md) FUN_0057e5b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de50.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0057e170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e170.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e5e0",
      "incomplete_value": false,
      "site": "0057e5e4",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e2c0",
      "incomplete_value": false,
      "site": "0057e2c4",
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
            "const:498:8"
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
      "definition_site": "0057e5ec",
      "incomplete_value": false,
      "site": "0057e5fc",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e2cc",
      "incomplete_value": false,
      "site": "0057e2dc",
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
            "const:420:8"
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
      "0057e5e4",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e5fc",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e5e4",
      "DATA",
      [
        "storage",
        "00c6d468",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e5fc",
      "DATA",
      [
        "storage",
        "00c6d3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e294.md#insn-0057e2bc) · [`0057e2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e294.md#insn-0057e2c0) · [`0057e2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e294.md#insn-0057e2c8)
- 新版 [`0057e5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e5b4.md#insn-0057e5dc) · [`0057e5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e5b4.md#insn-0057e5e0)

~~~diff
- 0057e2bc ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057e5dc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057e2bc bytes 683700d0
+ 0057e5dc bytes 683700f0
- 0057e2c0 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0057e2c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e2c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e2c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e5e0 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0057e5e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e5e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e5e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e2c0 bytes 08611291
+ 0057e5e0 bytes 08a11191
- 0057e2c8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e2c8 bytes 683700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c5dcc7762ff393d513d10d0a4ad69fb"></a>

### [`0057e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3bc.md) → [`0057e6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6dc.md) FUN_0057e6dc

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
      "definition_site": "0057e6e0",
      "incomplete_value": false,
      "site": "0057e6e4",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e3c0",
      "incomplete_value": false,
      "site": "0057e3c4",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057e6e4",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e6e4",
      "DATA",
      [
        "storage",
        "00c6d468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3bc.md#insn-0057e3bc) · [`0057e3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3bc.md#insn-0057e3c0)
- 新版 [`0057e6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6dc.md#insn-0057e6dc) · [`0057e6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6dc.md#insn-0057e6e0)

~~~diff
- 0057e3bc ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057e6dc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057e3bc bytes 683700d0
+ 0057e6dc bytes 683700f0
- 0057e3c0 ["COPY", "tmp:0:8", ["const:498:8"]]
- 0057e3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e6e0 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0057e6e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e6e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e6e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e3c0 bytes 08611291
+ 0057e6e0 bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-627c0f8472587a181373324f40a7f483"></a>

### [`0057e3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3cc.md) → [`0057e6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6ec.md) FUN_0057e6ec

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
      "definition_site": "0057e6fc",
      "incomplete_value": false,
      "site": "0057e704",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e3dc",
      "incomplete_value": false,
      "site": "0057e3e4",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057e704",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e704",
      "DATA",
      [
        "storage",
        "00c6d468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3cc.md#insn-0057e3d8) · [`0057e3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3cc.md#insn-0057e3dc) · [`0057e3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3cc.md#insn-0057e3e8)
- 新版 [`0057e6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6ec.md#insn-0057e6f8) · [`0057e6fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6ec.md#insn-0057e6fc) · [`0057e708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e6ec.md#insn-0057e708)

~~~diff
- 0057e3d8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0057e6f8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0057e3d8 bytes 683700d0
+ 0057e6f8 bytes 683700f0
- 0057e3dc ["COPY", "tmp:0:8", ["const:498:8"]]
- 0057e3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e6fc ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0057e6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e3dc bytes 08611291
+ 0057e6fc bytes 08a11191
- 0057e3e8 ["INT_ADD", "register:40f0:8", ["const:57e3e8:8", "const:4:8"]]
- 0057e3e8 ["CALL", null, ["callee:00c58f40:8"]]
+ 0057e708 ["INT_ADD", "register:40f0:8", ["const:57e708:8", "const:4:8"]]
+ 0057e708 ["CALL", null, ["callee:00c58f40:8"]]
- 0057e3e8 bytes e2661b94
+ 0057e708 bytes 0e6a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-549cd7fc8f0b4c09a0131f128509f46b"></a>

### [`0057e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md) → [`0057e83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e83c.md) FUN_0057e83c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00550c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c6c.md) [`0057ec30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec30.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589194.md)
- 新版 呼出元 2件 [`00550f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f8c.md) [`0057ef50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057ef50.md) · 呼出先 15件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894b4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e89c",
      "incomplete_value": true,
      "site": "0057e89c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e57c",
      "incomplete_value": true,
      "site": "0057e57c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:77e:8"
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
      "definition_site": "0057e8a8",
      "incomplete_value": true,
      "site": "0057e8b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b4f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e588",
      "incomplete_value": true,
      "site": "0057e594",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a71:8"
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
      "definition_site": "0057e954",
      "incomplete_value": true,
      "site": "0057e954",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e634",
      "incomplete_value": true,
      "site": "0057e634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:246:8"
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
      "0057e88c",
      "READ",
      [
        "storage",
        "002a677e",
        null,
        "string"
      ]
    ],
    [
      "0057e8a8",
      "READ",
      [
        "storage",
        "002bda71",
        null,
        "string"
      ]
    ],
    [
      "0057e93c",
      "READ",
      [
        "storage",
        "002b6246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e88c",
      "READ",
      [
        "storage",
        "002a68d6",
        null,
        "string"
      ]
    ],
    [
      "0057e8a8",
      "READ",
      [
        "storage",
        "002bdb4f",
        null,
        "string"
      ]
    ],
    [
      "0057e93c",
      "READ",
      [
        "storage",
        "002b6315",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md#insn-0057e548) · [`0057e550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md#insn-0057e550) · [`0057e568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md#insn-0057e568)
- 新版 [`0057e868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e83c.md#insn-0057e868) · [`0057e870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e83c.md#insn-0057e870) · [`0057e888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e83c.md#insn-0057e888)

~~~diff
- 0057e548 ["INT_ADD", "register:40f0:8", ["const:57e548:8", "const:4:8"]]
- 0057e548 ["CALL", null, ["callee:005891cc:8"]]
+ 0057e868 ["INT_ADD", "register:40f0:8", ["const:57e868:8", "const:4:8"]]
+ 0057e868 ["CALL", null, ["callee:005891cc:8"]]
- 0057e548 bytes 592a0094
+ 0057e868 bytes 592a0094
- 0057e550 ["INT_ADD", "register:40f0:8", ["const:57e550:8", "const:4:8"]]
- 0057e550 ["CALL", null, ["callee:005894bc:8"]]
+ 0057e870 ["INT_ADD", "register:40f0:8", ["const:57e870:8", "const:4:8"]]
+ 0057e870 ["CALL", null, ["callee:005894bc:8"]]
- 0057e550 bytes 132b0094
+ 0057e870 bytes 132b0094
- 0057e568 ["COPY", "tmp:0:8", ["const:77e:8"]]
- 0057e568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e888 ["COPY", "tmp:0:8", ["const:8d6:8"]]
+ 0057e888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e568 bytes 08f91d91
+ 0057e888 bytes 08592391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3fcc168468f3661048c84f70a43422"></a>

### [`0057e874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md) → [`0057eb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eb94.md) FUN_0057eb94

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589194.md)
- 新版 呼出元 1件 [`00550f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f88.md) · 呼出先 15件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894b4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ec00",
      "incomplete_value": true,
      "site": "0057ec0c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b4f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e8e0",
      "incomplete_value": true,
      "site": "0057e8ec",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a71:8"
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
      "definition_site": "0057ecac",
      "incomplete_value": true,
      "site": "0057ecac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e98c",
      "incomplete_value": true,
      "site": "0057e98c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:246:8"
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
      "definition_site": "0057ecb4",
      "incomplete_value": true,
      "site": "0057ecb4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057e994",
      "incomplete_value": true,
      "site": "0057e994",
      "value": [
        "LOAD",
        "8",
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
      "0057ebe4",
      "READ",
      [
        "storage",
        "002a01a7",
        null,
        "string"
      ]
    ],
    [
      "0057ec00",
      "READ",
      [
        "storage",
        "002bda71",
        null,
        "string"
      ]
    ],
    [
      "0057ec94",
      "READ",
      [
        "storage",
        "002b6246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ebe4",
      "READ",
      [
        "storage",
        "002a01e7",
        null,
        "string"
      ]
    ],
    [
      "0057ec00",
      "READ",
      [
        "storage",
        "002bdb4f",
        null,
        "string"
      ]
    ],
    [
      "0057ec94",
      "READ",
      [
        "storage",
        "002b6315",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md#insn-0057e8a0) · [`0057e8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md#insn-0057e8a8) · [`0057e8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md#insn-0057e8c0)
- 新版 [`0057ebc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eb94.md#insn-0057ebc0) · [`0057ebc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eb94.md#insn-0057ebc8) · [`0057ebe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057eb94.md#insn-0057ebe0)

~~~diff
- 0057e8a0 ["INT_ADD", "register:40f0:8", ["const:57e8a0:8", "const:4:8"]]
- 0057e8a0 ["CALL", null, ["callee:005891cc:8"]]
+ 0057ebc0 ["INT_ADD", "register:40f0:8", ["const:57ebc0:8", "const:4:8"]]
+ 0057ebc0 ["CALL", null, ["callee:005891cc:8"]]
- 0057e8a0 bytes 83290094
+ 0057ebc0 bytes 83290094
- 0057e8a8 ["INT_ADD", "register:40f0:8", ["const:57e8a8:8", "const:4:8"]]
- 0057e8a8 ["CALL", null, ["callee:005894bc:8"]]
+ 0057ebc8 ["INT_ADD", "register:40f0:8", ["const:57ebc8:8", "const:4:8"]]
+ 0057ebc8 ["CALL", null, ["callee:005894bc:8"]]
- 0057e8a8 bytes 3d2a0094
+ 0057ebc8 bytes 3d2a0094
- 0057e8c0 ["COPY", "tmp:0:8", ["const:1a7:8"]]
- 0057e8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ebe0 ["COPY", "tmp:0:8", ["const:1e7:8"]]
+ 0057ebe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ebe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ebe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e8c0 bytes 089d0691
+ 0057ebe0 bytes 089d0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-010d9d9c098e258b7a4ca01a248ceb90"></a>

### [`0057eea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md) → [`0057f1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f1c8.md) FUN_0057f1c8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f208",
      "incomplete_value": true,
      "site": "0057f218",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057eee8",
      "incomplete_value": true,
      "site": "0057eef8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b3:8"
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
      "definition_site": "0057f21c",
      "incomplete_value": true,
      "site": "0057f21c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057eefc",
      "incomplete_value": true,
      "site": "0057eefc",
      "value": [
        "LOAD",
        "8",
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
      "0057f208",
      "READ",
      [
        "storage",
        "002a01b3",
        null,
        "string"
      ]
    ],
    [
      "0057f210",
      "READ",
      [
        "storage",
        "002a01c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f208",
      "READ",
      [
        "storage",
        "002a01f3",
        null,
        "string"
      ]
    ],
    [
      "0057f210",
      "READ",
      [
        "storage",
        "002a0200",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md#insn-0057eed0) · [`0057eed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md#insn-0057eed8) · [`0057eee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md#insn-0057eee4)
- 新版 [`0057f1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f1c8.md#insn-0057f1f0) · [`0057f1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f1c8.md#insn-0057f1f8) · [`0057f204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f1c8.md#insn-0057f204)

~~~diff
- 0057eed0 ["INT_ADD", "register:40f0:8", ["const:57eed0:8", "const:4:8"]]
- 0057eed0 ["CALL", null, ["callee:005891cc:8"]]
+ 0057f1f0 ["INT_ADD", "register:40f0:8", ["const:57f1f0:8", "const:4:8"]]
+ 0057f1f0 ["CALL", null, ["callee:005891cc:8"]]
- 0057eed0 bytes f7270094
+ 0057f1f0 bytes f7270094
- 0057eed8 ["INT_ADD", "register:40f0:8", ["const:57eed8:8", "const:4:8"]]
- 0057eed8 ["CALL", null, ["callee:005894bc:8"]]
+ 0057f1f8 ["INT_ADD", "register:40f0:8", ["const:57f1f8:8", "const:4:8"]]
+ 0057f1f8 ["CALL", null, ["callee:005894bc:8"]]
- 0057eed8 bytes b1280094
+ 0057f1f8 bytes b1280094
- 0057eee4 ["COPY", "tmp:0:8", ["const:1b3:8"]]
- 0057eee4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057eee4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057eee4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f204 ["COPY", "tmp:0:8", ["const:1f3:8"]]
+ 0057f204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057eee4 bytes 29cd0691
+ 0057f204 bytes 29cd0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee2bb94d64d910ac1e75aeadcb7ae45"></a>

### [`0057f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md) → [`0057f33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f33c.md) FUN_0057f33c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

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
      "definition_site": "0057f388",
      "incomplete_value": true,
      "site": "0057f3a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f068",
      "incomplete_value": true,
      "site": "0057f084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:658:8"
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
      "0057f388",
      "READ",
      [
        "storage",
        "002a5658",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f388",
      "READ",
      [
        "storage",
        "002a57b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md#insn-0057f044) · [`0057f04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md#insn-0057f04c) · [`0057f058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md#insn-0057f058)
- 新版 [`0057f364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f33c.md#insn-0057f364) · [`0057f36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f33c.md#insn-0057f36c) · [`0057f378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f33c.md#insn-0057f378)

~~~diff
- 0057f044 ["INT_ADD", "register:40f0:8", ["const:57f044:8", "const:4:8"]]
- 0057f044 ["CALL", null, ["callee:005891cc:8"]]
+ 0057f364 ["INT_ADD", "register:40f0:8", ["const:57f364:8", "const:4:8"]]
+ 0057f364 ["CALL", null, ["callee:005891cc:8"]]
- 0057f044 bytes 9a270094
+ 0057f364 bytes 9a270094
- 0057f04c ["INT_ADD", "register:40f0:8", ["const:57f04c:8", "const:4:8"]]
- 0057f04c ["CALL", null, ["callee:005894bc:8"]]
+ 0057f36c ["INT_ADD", "register:40f0:8", ["const:57f36c:8", "const:4:8"]]
+ 0057f36c ["CALL", null, ["callee:005894bc:8"]]
- 0057f04c bytes 54280094
+ 0057f36c bytes 54280094
- 0057f058 ["COPY", "tmp:0:8", ["const:658:8"]]
- 0057f058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f378 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 0057f378 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f378 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f378 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f058 bytes 29611991
+ 0057f378 bytes 29c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d356ce4c18f1ad2bbf56d2be30608d8a"></a>

### [`0057f19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md) → [`0057f4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f4bc.md) FUN_0057f4bc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

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
      "definition_site": "0057f508",
      "incomplete_value": true,
      "site": "0057f524",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f1e8",
      "incomplete_value": true,
      "site": "0057f204",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:179:8"
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
      "0057f508",
      "READ",
      [
        "storage",
        "0029f179",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f508",
      "READ",
      [
        "storage",
        "0029f1b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md#insn-0057f1c4) · [`0057f1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md#insn-0057f1cc) · [`0057f1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md#insn-0057f1d8)
- 新版 [`0057f4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f4bc.md#insn-0057f4e4) · [`0057f4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f4bc.md#insn-0057f4ec) · [`0057f4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f4bc.md#insn-0057f4f8)

~~~diff
- 0057f1c4 ["INT_ADD", "register:40f0:8", ["const:57f1c4:8", "const:4:8"]]
- 0057f1c4 ["CALL", null, ["callee:005891cc:8"]]
+ 0057f4e4 ["INT_ADD", "register:40f0:8", ["const:57f4e4:8", "const:4:8"]]
+ 0057f4e4 ["CALL", null, ["callee:005891cc:8"]]
- 0057f1c4 bytes 3a270094
+ 0057f4e4 bytes 3a270094
- 0057f1cc ["INT_ADD", "register:40f0:8", ["const:57f1cc:8", "const:4:8"]]
- 0057f1cc ["CALL", null, ["callee:005894bc:8"]]
+ 0057f4ec ["INT_ADD", "register:40f0:8", ["const:57f4ec:8", "const:4:8"]]
+ 0057f4ec ["CALL", null, ["callee:005894bc:8"]]
- 0057f1cc bytes f4270094
+ 0057f4ec bytes f4270094
- 0057f1d8 ["COPY", "tmp:0:8", ["const:179:8"]]
- 0057f1d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f1d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f1d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f4f8 ["COPY", "tmp:0:8", ["const:1b9:8"]]
+ 0057f4f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f4f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f4f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f1d8 bytes 29e50591
+ 0057f4f8 bytes 29e50691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccdf4f7871fdf6619002cc615b31fa99"></a>

### [`0057f314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f314.md) → [`0057f634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f634.md) FUN_0057f634

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f680",
      "incomplete_value": true,
      "site": "0057f690",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f360",
      "incomplete_value": true,
      "site": "0057f370",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8c2:8"
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
      "definition_site": "0057f698",
      "incomplete_value": true,
      "site": "0057f698",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f378",
      "incomplete_value": true,
      "site": "0057f378",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f694",
      "incomplete_value": true,
      "site": "0057f6ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f374",
      "incomplete_value": true,
      "site": "0057f38c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057f680",
      "READ",
      [
        "storage",
        "002ac8c2",
        null,
        "string"
      ]
    ],
    [
      "0057f684",
      "READ",
      [
        "storage",
        "002ac8d1",
        null,
        "string"
      ]
    ],
    [
      "0057f694",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057f680",
      "READ",
      [
        "storage",
        "002ac98f",
        null,
        "string"
      ]
    ],
    [
      "0057f684",
      "READ",
      [
        "storage",
        "002ac99e",
        null,
        "string"
      ]
    ],
    [
      "0057f694",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f314.md#insn-0057f33c) · [`0057f344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f314.md#insn-0057f344) · [`0057f350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f314.md#insn-0057f350)
- 新版 [`0057f65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f634.md#insn-0057f65c) · [`0057f664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f634.md#insn-0057f664) · [`0057f670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f634.md#insn-0057f670)

~~~diff
- 0057f33c ["INT_ADD", "register:40f0:8", ["const:57f33c:8", "const:4:8"]]
- 0057f33c ["CALL", null, ["callee:005891cc:8"]]
+ 0057f65c ["INT_ADD", "register:40f0:8", ["const:57f65c:8", "const:4:8"]]
+ 0057f65c ["CALL", null, ["callee:005891cc:8"]]
- 0057f33c bytes dc260094
+ 0057f65c bytes dc260094
- 0057f344 ["INT_ADD", "register:40f0:8", ["const:57f344:8", "const:4:8"]]
- 0057f344 ["CALL", null, ["callee:005894bc:8"]]
+ 0057f664 ["INT_ADD", "register:40f0:8", ["const:57f664:8", "const:4:8"]]
+ 0057f664 ["CALL", null, ["callee:005894bc:8"]]
- 0057f344 bytes 96270094
+ 0057f664 bytes 96270094
- 0057f350 ["INT_ADD", "register:40f0:8", ["const:57f350:8", "const:4:8"]]
- 0057f350 ["CALL", null, ["callee:00c58f30:8"]]
+ 0057f670 ["INT_ADD", "register:40f0:8", ["const:57f670:8", "const:4:8"]]
+ 0057f670 ["CALL", null, ["callee:00c58f30:8"]]
- 0057f350 bytes 04631b94
+ 0057f670 bytes 30661b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b989022b30de30ee7a55a901dc8b6bcf"></a>

### [`0057f4a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f4a4.md) → [`0057f7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f7c4.md) FUN_0057f7c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f814",
      "incomplete_value": true,
      "site": "0057f82c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f4f4",
      "incomplete_value": true,
      "site": "0057f50c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e33:8"
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
      "definition_site": "0057f830",
      "incomplete_value": true,
      "site": "0057f83c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f510",
      "incomplete_value": true,
      "site": "0057f51c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f4e:8"
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
      "definition_site": "0057f840",
      "incomplete_value": true,
      "site": "0057f840",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f520",
      "incomplete_value": true,
      "site": "0057f520",
      "value": [
        "LOAD",
        "8",
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
      "0057f814",
      "READ",
      [
        "storage",
        "002bee33",
        null,
        "string"
      ]
    ],
    [
      "0057f830",
      "READ",
      [
        "storage",
        "002b4f4e",
        null,
        "string"
      ]
    ],
    [
      "0057f834",
      "READ",
      [
        "storage",
        "002b4f5c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f814",
      "READ",
      [
        "storage",
        "002bef11",
        null,
        "string"
      ]
    ],
    [
      "0057f830",
      "READ",
      [
        "storage",
        "002b502c",
        null,
        "string"
      ]
    ],
    [
      "0057f834",
      "READ",
      [
        "storage",
        "002b503a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f4a4.md#insn-0057f4d4) · [`0057f4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f4a4.md#insn-0057f4dc) · [`0057f4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f4a4.md#insn-0057f4e8)
- 新版 [`0057f7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f7c4.md#insn-0057f7f4) · [`0057f7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f7c4.md#insn-0057f7fc) · [`0057f808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f7c4.md#insn-0057f808)

~~~diff
- 0057f4d4 ["INT_ADD", "register:40f0:8", ["const:57f4d4:8", "const:4:8"]]
- 0057f4d4 ["CALL", null, ["callee:005891cc:8"]]
+ 0057f7f4 ["INT_ADD", "register:40f0:8", ["const:57f7f4:8", "const:4:8"]]
+ 0057f7f4 ["CALL", null, ["callee:005891cc:8"]]
- 0057f4d4 bytes 76260094
+ 0057f7f4 bytes 76260094
- 0057f4dc ["INT_ADD", "register:40f0:8", ["const:57f4dc:8", "const:4:8"]]
- 0057f4dc ["CALL", null, ["callee:005894bc:8"]]
+ 0057f7fc ["INT_ADD", "register:40f0:8", ["const:57f7fc:8", "const:4:8"]]
+ 0057f7fc ["CALL", null, ["callee:005894bc:8"]]
- 0057f4dc bytes 30270094
+ 0057f7fc bytes 30270094
- 0057f4e8 ["COPY", "tmp:0:8", ["const:e33:8"]]
- 0057f4e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f4e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f4e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f808 ["COPY", "tmp:0:8", ["const:f11:8"]]
+ 0057f808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f4e8 bytes 29cd3891
+ 0057f808 bytes 29453c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58354384fd829efb28092544cb0feca8"></a>

### [`0057f66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md) → [`0057f98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f98c.md) FUN_0057f98c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589194.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894b4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f9d4",
      "incomplete_value": true,
      "site": "0057f9e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:325:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f6b4",
      "incomplete_value": true,
      "site": "0057f6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:256:8"
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
      "definition_site": "0057fa00",
      "incomplete_value": true,
      "site": "0057fa10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ff9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f6e0",
      "incomplete_value": true,
      "site": "0057f6f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:faf:8"
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
      "definition_site": "0057fa04",
      "incomplete_value": true,
      "site": "0057fa14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f6e4",
      "incomplete_value": true,
      "site": "0057f6f4",
      "value": [
        "LOAD",
        "8",
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
      "0057f9d4",
      "READ",
      [
        "storage",
        "002b6256",
        null,
        "string"
      ]
    ],
    [
      "0057fa00",
      "READ",
      [
        "storage",
        "002bffaf",
        null,
        "string"
      ]
    ],
    [
      "0057fa04",
      "READ",
      [
        "storage",
        "002bffbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f9d4",
      "READ",
      [
        "storage",
        "002b6325",
        null,
        "string"
      ]
    ],
    [
      "0057fa00",
      "READ",
      [
        "storage",
        "002bfff9",
        null,
        "string"
      ]
    ],
    [
      "0057fa04",
      "READ",
      [
        "storage",
        "002c0009",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md#insn-0057f69c) · [`0057f6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md#insn-0057f6a4) · [`0057f6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md#insn-0057f6ac)
- 新版 [`0057f9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f98c.md#insn-0057f9bc) · [`0057f9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f98c.md#insn-0057f9c4) · [`0057f9cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057f98c.md#insn-0057f9cc)

~~~diff
- 0057f69c ["INT_ADD", "register:40f0:8", ["const:57f69c:8", "const:4:8"]]
- 0057f69c ["CALL", null, ["callee:005891cc:8"]]
+ 0057f9bc ["INT_ADD", "register:40f0:8", ["const:57f9bc:8", "const:4:8"]]
+ 0057f9bc ["CALL", null, ["callee:005891cc:8"]]
- 0057f69c bytes 04260094
+ 0057f9bc bytes 04260094
- 0057f6a4 ["INT_ADD", "register:40f0:8", ["const:57f6a4:8", "const:4:8"]]
- 0057f6a4 ["CALL", null, ["callee:005894bc:8"]]
+ 0057f9c4 ["INT_ADD", "register:40f0:8", ["const:57f9c4:8", "const:4:8"]]
+ 0057f9c4 ["CALL", null, ["callee:005894bc:8"]]
- 0057f6a4 bytes be260094
+ 0057f9c4 bytes be260094
- 0057f6ac ["COPY", "tmp:0:8", ["const:256:8"]]
- 0057f6ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f6ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f6ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f9cc ["COPY", "tmp:0:8", ["const:325:8"]]
+ 0057f9cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f9cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f9cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f6ac bytes 29590991
+ 0057f9cc bytes 29950c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f57413704b8d02ab538eb2886407a9"></a>

### [`0057f8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f8ac.md) → [`0057fbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fbcc.md) FUN_0057fbcc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0055c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0055cb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055c/0055cb24.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fc3c",
      "incomplete_value": true,
      "site": "0057fc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e2b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f91c",
      "incomplete_value": true,
      "site": "0057f91c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d5e:8"
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
      "definition_site": "0057fc58",
      "incomplete_value": true,
      "site": "0057fc68",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f938",
      "incomplete_value": true,
      "site": "0057f948",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:8a0:8"
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
      "0057fc28",
      "READ",
      [
        "storage",
        "002a9d5e",
        null,
        "string"
      ]
    ],
    [
      "0057fc30",
      "READ",
      [
        "storage",
        "002a9d63",
        null,
        "string"
      ]
    ],
    [
      "0057fc58",
      "READ",
      [
        "storage",
        "002c28a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057fc28",
      "READ",
      [
        "storage",
        "002a9e2b",
        null,
        "string"
      ]
    ],
    [
      "0057fc30",
      "READ",
      [
        "storage",
        "002a9e30",
        null,
        "string"
      ]
    ],
    [
      "0057fc58",
      "READ",
      [
        "storage",
        "002c28f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f8ac.md#insn-0057f8f0) · [`0057f8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f8ac.md#insn-0057f8f8) · [`0057f904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f8ac.md#insn-0057f904)
- 新版 [`0057fc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fbcc.md#insn-0057fc10) · [`0057fc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fbcc.md#insn-0057fc18) · [`0057fc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fbcc.md#insn-0057fc24)

~~~diff
- 0057f8f0 ["INT_ADD", "register:40f0:8", ["const:57f8f0:8", "const:4:8"]]
- 0057f8f0 ["CALL", null, ["callee:005891cc:8"]]
+ 0057fc10 ["INT_ADD", "register:40f0:8", ["const:57fc10:8", "const:4:8"]]
+ 0057fc10 ["CALL", null, ["callee:005891cc:8"]]
- 0057f8f0 bytes 6f250094
+ 0057fc10 bytes 6f250094
- 0057f8f8 ["INT_ADD", "register:40f0:8", ["const:57f8f8:8", "const:4:8"]]
- 0057f8f8 ["CALL", null, ["callee:005894bc:8"]]
+ 0057fc18 ["INT_ADD", "register:40f0:8", ["const:57fc18:8", "const:4:8"]]
+ 0057fc18 ["CALL", null, ["callee:005894bc:8"]]
- 0057f8f8 bytes 29260094
+ 0057fc18 bytes 29260094
- 0057f904 ["COPY", "tmp:0:8", ["const:d5e:8"]]
- 0057f904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057fc24 ["COPY", "tmp:0:8", ["const:e2b:8"]]
+ 0057fc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057fc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057fc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f904 bytes 29793591
+ 0057fc24 bytes 29ad3891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937c570abfdb2a28946d3cc35abbae6d"></a>

### [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) → [`0057fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md) FUN_0057fe6c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005552d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552d8.md) [`0057fd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md) [`0057fde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md) [`0057fe94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md) [`0057ff3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md) · 呼出先 11件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 6件 [`005555f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555f8.md) [`00580080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580080.md) [`00580108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580108.md) [`005801b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005801b4.md) [`0058025c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/0058025c.md) · 呼出先 11件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fed0",
      "incomplete_value": true,
      "site": "0057fed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fbb0",
      "incomplete_value": true,
      "site": "0057fbb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0f:8"
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
      "definition_site": "0057fed8",
      "incomplete_value": true,
      "site": "0057fed8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057fbb8",
      "incomplete_value": true,
      "site": "0057fbb8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fed4",
      "incomplete_value": true,
      "site": "0057fee8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fbb4",
      "incomplete_value": true,
      "site": "0057fbc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:275:8"
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
      "0057feb8",
      "READ",
      [
        "storage",
        "002b2d0f",
        null,
        "string"
      ]
    ],
    [
      "0057fec0",
      "READ",
      [
        "storage",
        "002b2d14",
        null,
        "string"
      ]
    ],
    [
      "0057fed4",
      "READ",
      [
        "storage",
        "002a1275",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057feb8",
      "READ",
      [
        "storage",
        "002b2d59",
        null,
        "string"
      ]
    ],
    [
      "0057fec0",
      "READ",
      [
        "storage",
        "002b2d5e",
        null,
        "string"
      ]
    ],
    [
      "0057fed4",
      "READ",
      [
        "storage",
        "002a12b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md#insn-0057fb80) · [`0057fb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md#insn-0057fb88) · [`0057fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md#insn-0057fb94)
- 新版 [`0057fea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md#insn-0057fea0) · [`0057fea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md#insn-0057fea8) · [`0057feb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md#insn-0057feb4)

~~~diff
- 0057fb80 ["INT_ADD", "register:40f0:8", ["const:57fb80:8", "const:4:8"]]
- 0057fb80 ["CALL", null, ["callee:005891cc:8"]]
+ 0057fea0 ["INT_ADD", "register:40f0:8", ["const:57fea0:8", "const:4:8"]]
+ 0057fea0 ["CALL", null, ["callee:005891cc:8"]]
- 0057fb80 bytes cb240094
+ 0057fea0 bytes cb240094
- 0057fb88 ["INT_ADD", "register:40f0:8", ["const:57fb88:8", "const:4:8"]]
- 0057fb88 ["CALL", null, ["callee:005894bc:8"]]
+ 0057fea8 ["INT_ADD", "register:40f0:8", ["const:57fea8:8", "const:4:8"]]
+ 0057fea8 ["CALL", null, ["callee:005894bc:8"]]
- 0057fb88 bytes 85250094
+ 0057fea8 bytes 85250094
- 0057fb94 ["COPY", "tmp:0:8", ["const:d0f:8"]]
- 0057fb94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057fb94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057fb94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057feb4 ["COPY", "tmp:0:8", ["const:d59:8"]]
+ 0057feb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057feb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057feb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057fb94 bytes 293d3491
+ 0057feb4 bytes 29653591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6af4ae68778b94c708d4efe9c78004"></a>

### [`0057fde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md) → [`00580108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580108.md) FUN_00580108

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005552e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552e0.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00555600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/00555600.md) · 呼出先 3件 [`0057fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580144",
      "incomplete_value": true,
      "site": "00580144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fe24",
      "incomplete_value": true,
      "site": "0057fe24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8da:8"
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
      "00580128",
      "READ",
      [
        "storage",
        "002ac8da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580128",
      "READ",
      [
        "storage",
        "002ac9a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md#insn-0057fe00) · [`0057fe30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md#insn-0057fe30) · [`0057fe40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md#insn-0057fe40)
- 新版 [`00580120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580108.md#insn-00580120) · [`00580150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580108.md#insn-00580150) · [`00580160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580108.md#insn-00580160)

~~~diff
- 0057fe00 ["COPY", "tmp:0:8", ["const:8da:8"]]
- 0057fe00 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0057fe00 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0057fe00 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00580120 ["COPY", "tmp:0:8", ["const:9a7:8"]]
+ 00580120 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00580120 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00580120 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0057fe00 bytes 6b692391
+ 00580120 bytes 6b9d2691
- 0057fe30 ["INT_ADD", "register:40f0:8", ["const:57fe30:8", "const:4:8"]]
- 0057fe30 ["CALL", null, ["callee:0057fe6c:8"]]
+ 00580150 ["INT_ADD", "register:40f0:8", ["const:580150:8", "const:4:8"]]
+ 00580150 ["CALL", null, ["callee:0057fe6c:8"]]
- 0057fe30 bytes 47ffff97
+ 00580150 bytes 47ffff97
- 0057fe40 ["INT_ADD", "register:40f0:8", ["const:57fe40:8", "const:4:8"]]
- 0057fe40 ["CALL", null, ["callee:00c58f50:8"]]
+ 00580160 ["INT_ADD", "register:40f0:8", ["const:580160:8", "const:4:8"]]
+ 00580160 ["CALL", null, ["callee:00c58f50:8"]]
- 0057fe40 bytes 50601b94
+ 00580160 bytes 7c631b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f68d2ed662cef45b27037109f0a89443"></a>

### [`0057fe94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md) → [`005801b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005801b4.md) FUN_005801b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005552e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552e4.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00555604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/00555604.md) · 呼出先 3件 [`0057fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005801e8",
      "incomplete_value": true,
      "site": "005801e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fec8",
      "incomplete_value": true,
      "site": "0057fec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3fc:8"
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
      "definition_site": "005801ec",
      "incomplete_value": true,
      "site": "005801ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057fecc",
      "incomplete_value": true,
      "site": "0057fecc",
      "value": [
        "LOAD",
        "8",
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
      "005801d4",
      "READ",
      [
        "storage",
        "002ba3fc",
        null,
        "string"
      ]
    ],
    [
      "005801e0",
      "READ",
      [
        "storage",
        "002ba402",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005801d4",
      "READ",
      [
        "storage",
        "002ba4da",
        null,
        "string"
      ]
    ],
    [
      "005801e0",
      "READ",
      [
        "storage",
        "002ba4e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057feac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md#insn-0057feac) · [`0057fed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md#insn-0057fed8) · [`0057fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md#insn-0057fee8)
- 新版 [`005801cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005801b4.md#insn-005801cc) · [`005801f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005801b4.md#insn-005801f8) · [`00580208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005801b4.md#insn-00580208)

~~~diff
- 0057feac ["COPY", "tmp:0:8", ["const:3fc:8"]]
- 0057feac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057feac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057feac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005801cc ["COPY", "tmp:0:8", ["const:4da:8"]]
+ 005801cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005801cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005801cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057feac bytes 4af10f91
+ 005801cc bytes 4a691391
- 0057fed8 ["INT_ADD", "register:40f0:8", ["const:57fed8:8", "const:4:8"]]
- 0057fed8 ["CALL", null, ["callee:0057fe6c:8"]]
+ 005801f8 ["INT_ADD", "register:40f0:8", ["const:5801f8:8", "const:4:8"]]
+ 005801f8 ["CALL", null, ["callee:0057fe6c:8"]]
- 0057fed8 bytes 1dffff97
+ 005801f8 bytes 1dffff97
- 0057fee8 ["INT_ADD", "register:40f0:8", ["const:57fee8:8", "const:4:8"]]
- 0057fee8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00580208 ["INT_ADD", "register:40f0:8", ["const:580208:8", "const:4:8"]]
+ 00580208 ["CALL", null, ["callee:00c58f50:8"]]
- 0057fee8 bytes 26601b94
+ 00580208 bytes 52631b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9d6f75cc2f08bb464df45708a0e3fb"></a>

### [`0057ffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ffe0.md) → [`00580300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580300.md) FUN_00580300

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005552ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552ec.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0055560c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/0055560c.md) · 呼出先 3件 [`0057fe6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057f/0057fe6c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580334",
      "incomplete_value": true,
      "site": "00580334",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580014",
      "incomplete_value": true,
      "site": "00580014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac5:8"
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
      "definition_site": "00580338",
      "incomplete_value": true,
      "site": "00580338",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00580018",
      "incomplete_value": true,
      "site": "00580018",
      "value": [
        "LOAD",
        "8",
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
      "00580320",
      "READ",
      [
        "storage",
        "002afac5",
        null,
        "string"
      ]
    ],
    [
      "0058032c",
      "READ",
      [
        "storage",
        "002afaca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580320",
      "READ",
      [
        "storage",
        "002afb9c",
        null,
        "string"
      ]
    ],
    [
      "0058032c",
      "READ",
      [
        "storage",
        "002afba1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ffe0.md#insn-0057fff8) · [`00580024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ffe0.md#insn-00580024) · [`00580034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ffe0.md#insn-00580034)
- 新版 [`00580318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580300.md#insn-00580318) · [`00580344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580300.md#insn-00580344) · [`00580354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580300.md#insn-00580354)

~~~diff
- 0057fff8 ["COPY", "tmp:0:8", ["const:ac5:8"]]
- 0057fff8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057fff8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057fff8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00580318 ["COPY", "tmp:0:8", ["const:b9c:8"]]
+ 00580318 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00580318 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00580318 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057fff8 bytes 4a152b91
+ 00580318 bytes 4a712e91
- 00580024 ["INT_ADD", "register:40f0:8", ["const:580024:8", "const:4:8"]]
- 00580024 ["CALL", null, ["callee:0057fe6c:8"]]
+ 00580344 ["INT_ADD", "register:40f0:8", ["const:580344:8", "const:4:8"]]
+ 00580344 ["CALL", null, ["callee:0057fe6c:8"]]
- 00580024 bytes cafeff97
+ 00580344 bytes cafeff97
- 00580034 ["INT_ADD", "register:40f0:8", ["const:580034:8", "const:4:8"]]
- 00580034 ["CALL", null, ["callee:00c58f50:8"]]
+ 00580354 ["INT_ADD", "register:40f0:8", ["const:580354:8", "const:4:8"]]
+ 00580354 ["CALL", null, ["callee:00c58f50:8"]]
- 00580034 bytes d35f1b94
+ 00580354 bytes ff621b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9126ce3885c3c7a123a606b46e77517"></a>

### [`00580088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580088.md) → [`005803a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803a8.md) FUN_005803a8

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
      "definition_site": "005803ac",
      "incomplete_value": false,
      "site": "005803b0",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058008c",
      "incomplete_value": false,
      "site": "00580090",
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
            "const:590:8"
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
      "005803b0",
      "DATA",
      [
        "storage",
        "00c6c590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005803b0",
      "DATA",
      [
        "storage",
        "00c6d560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580088.md#insn-00580088) · [`0058008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580088.md#insn-0058008c)
- 新版 [`005803a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803a8.md#insn-005803a8) · [`005803ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803a8.md#insn-005803ac)

~~~diff
- 00580088 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005803a8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00580088 bytes 68370090
+ 005803a8 bytes 683700b0
- 0058008c ["COPY", "tmp:0:8", ["const:590:8"]]
- 0058008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005803ac ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005803ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005803ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005803ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058008c bytes 08411691
+ 005803ac bytes 08811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35526f625dfcd1b728697b745526811e"></a>

### [`00580098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580098.md) → [`005803b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803b8.md) FUN_005803b8

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
      "definition_site": "005803c8",
      "incomplete_value": false,
      "site": "005803d0",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800a8",
      "incomplete_value": false,
      "site": "005800b0",
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
            "const:590:8"
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
      "005803d0",
      "DATA",
      [
        "storage",
        "00c6c590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005803d0",
      "DATA",
      [
        "storage",
        "00c6d560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005800a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580098.md#insn-005800a4) · [`005800a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580098.md#insn-005800a8) · [`005800b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580098.md#insn-005800b4)
- 新版 [`005803c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803b8.md#insn-005803c4) · [`005803c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803b8.md#insn-005803c8) · [`005803d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803b8.md#insn-005803d4)

~~~diff
- 005800a4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005803c4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005800a4 bytes 68370090
+ 005803c4 bytes 683700b0
- 005800a8 ["COPY", "tmp:0:8", ["const:590:8"]]
- 005800a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005800a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005800a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005803c8 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 005803c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005803c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005803c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005800a8 bytes 08411691
+ 005803c8 bytes 08811591
- 005800b4 ["INT_ADD", "register:40f0:8", ["const:5800b4:8", "const:4:8"]]
- 005800b4 ["CALL", null, ["callee:00c58f40:8"]]
+ 005803d4 ["INT_ADD", "register:40f0:8", ["const:5803d4:8", "const:4:8"]]
+ 005803d4 ["CALL", null, ["callee:00c58f40:8"]]
- 005800b4 bytes af5f1b94
+ 005803d4 bytes db621b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf925b01ccb3cafbc6ac622509ef7597"></a>

### [`005800d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md) → [`005803f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803f8.md) FUN_005803f8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c710.md) · 呼出先 17件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`0055c714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c714.md) [`0055c71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c71c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)
- 新版 呼出元 1件 [`0055ca30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055c/0055ca30.md) · 呼出先 17件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`0055ca34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055c/0055ca34.md) [`0055ca3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055c/0055ca3c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.69% / 新版 93.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580460",
      "incomplete_value": true,
      "site": "00580460",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580140",
      "incomplete_value": true,
      "site": "00580140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d1d:8"
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
      "definition_site": "0058047c",
      "incomplete_value": true,
      "site": "00580484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0058015c",
      "incomplete_value": true,
      "site": "00580164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580478",
      "incomplete_value": true,
      "site": "00580488",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:941:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580158",
      "incomplete_value": true,
      "site": "00580168",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:874:8"
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
      "0058044c",
      "READ",
      [
        "storage",
        "002b2d1d",
        null,
        "string"
      ]
    ],
    [
      "00580478",
      "READ",
      [
        "storage",
        "002ad874",
        null,
        "string"
      ]
    ],
    [
      "00580478",
      "READ",
      [
        "storage",
        "002ad884",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058044c",
      "READ",
      [
        "storage",
        "002b2d67",
        null,
        "string"
      ]
    ],
    [
      "00580478",
      "READ",
      [
        "storage",
        "002ad941",
        null,
        "string"
      ]
    ],
    [
      "00580478",
      "READ",
      [
        "storage",
        "002ad951",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md#insn-00580418) · [`0058010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md#insn-0058010c) · [`00580114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md#insn-00580114)
- 新版 [`00580738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803f8.md#insn-00580738) · [`0058042c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803f8.md#insn-0058042c) · [`00580434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/005803f8.md#insn-00580434)

~~~diff
- 00580418 ["INT_ADD", "register:40f0:8", ["const:580418:8", "const:4:8"]]
- 00580418 ["CALL", null, ["ram:589f48:8"]]
+ 00580738 ["INT_ADD", "register:40f0:8", ["const:580738:8", "const:4:8"]]
+ 00580738 ["CALL", null, ["ram:58a268:8"]]
- 00580418 bytes cc260094
+ 00580738 bytes cc260094
- 0058010c ["INT_ADD", "register:40f0:8", ["const:58010c:8", "const:4:8"]]
- 0058010c ["CALL", null, ["callee:005891cc:8"]]
+ 0058042c ["INT_ADD", "register:40f0:8", ["const:58042c:8", "const:4:8"]]
+ 0058042c ["CALL", null, ["callee:005891cc:8"]]
- 0058010c bytes 68230094
+ 0058042c bytes 68230094
- 00580114 ["INT_ADD", "register:40f0:8", ["const:580114:8", "const:4:8"]]
- 00580114 ["CALL", null, ["callee:005894bc:8"]]
+ 00580434 ["INT_ADD", "register:40f0:8", ["const:580434:8", "const:4:8"]]
+ 00580434 ["CALL", null, ["callee:005894bc:8"]]
- 00580114 bytes 22240094
+ 00580434 bytes 22240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-325dbe3d28a4e578915fe60d3795206d"></a>

### [`005804e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md) → [`00580804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580804.md) FUN_00580804

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c860.md) · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0055c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md) [`0057de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de28.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`0055cb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055c/0055cb80.md) · 呼出先 20件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0055cb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055c/0055cb24.md) [`0057e148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057e/0057e148.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580858",
      "incomplete_value": true,
      "site": "00580858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580538",
      "incomplete_value": true,
      "site": "00580538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a82:8"
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
      "definition_site": "00580878",
      "incomplete_value": true,
      "site": "00580880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:230:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580558",
      "incomplete_value": true,
      "site": "00580560",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e0:8"
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
      "definition_site": "00580874",
      "incomplete_value": true,
      "site": "00580884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580554",
      "incomplete_value": true,
      "site": "00580564",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:926:8"
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
      "00580848",
      "READ",
      [
        "storage",
        "002bda82",
        null,
        "string"
      ]
    ],
    [
      "00580874",
      "READ",
      [
        "storage",
        "002a7926",
        null,
        "string"
      ]
    ],
    [
      "00580874",
      "READ",
      [
        "storage",
        "002a7936",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580848",
      "READ",
      [
        "storage",
        "002bdb60",
        null,
        "string"
      ]
    ],
    [
      "00580874",
      "READ",
      [
        "storage",
        "002a7a7e",
        null,
        "string"
      ]
    ],
    [
      "00580874",
      "READ",
      [
        "storage",
        "002a7a8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005805dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md#insn-005805dc) · [`0058073c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md#insn-0058073c) · [`00580510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md#insn-00580510)
- 新版 [`005808fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580804.md#insn-005808fc) · [`00580a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580804.md#insn-00580a5c) · [`00580830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580804.md#insn-00580830)

~~~diff
- 005805dc ["INT_ADD", "register:40f0:8", ["const:5805dc:8", "const:4:8"]]
- 005805dc ["CALL", null, ["callee:00c596b0:8"]]
+ 005808fc ["INT_ADD", "register:40f0:8", ["const:5808fc:8", "const:4:8"]]
+ 005808fc ["CALL", null, ["callee:00c596b0:8"]]
- 005805dc bytes 41601b94
+ 005808fc bytes 6d631b94
- 0058073c ["INT_ADD", "register:40f0:8", ["const:58073c:8", "const:4:8"]]
- 0058073c ["CALL", null, ["ram:589f48:8"]]
+ 00580a5c ["INT_ADD", "register:40f0:8", ["const:580a5c:8", "const:4:8"]]
+ 00580a5c ["CALL", null, ["ram:58a268:8"]]
- 0058073c bytes 03260094
+ 00580a5c bytes 03260094
- 00580510 ["INT_ADD", "register:40f0:8", ["const:580510:8", "const:4:8"]]
- 00580510 ["CALL", null, ["callee:005891cc:8"]]
+ 00580830 ["INT_ADD", "register:40f0:8", ["const:580830:8", "const:4:8"]]
+ 00580830 ["CALL", null, ["callee:005891cc:8"]]
- 00580510 bytes 67220094
+ 00580830 bytes 67220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b60af9abe0956dbb6e601d25e006d6"></a>

### [`005808c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md) → [`00580be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580be8.md) FUN_00580be8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00560494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560494.md) · 呼出先 10件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`005607b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/005607b4.md) · 呼出先 10件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580c5c",
      "incomplete_value": true,
      "site": "00580c6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:209:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058093c",
      "incomplete_value": true,
      "site": "0058094c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1c9:8"
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
      "definition_site": "00580c60",
      "incomplete_value": true,
      "site": "00580c70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00580940",
      "incomplete_value": true,
      "site": "00580950",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00580c64",
      "incomplete_value": true,
      "site": "00580c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00580944",
      "incomplete_value": true,
      "site": "00580954",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00580c30",
      "READ",
      [
        "storage",
        "002c130c",
        null,
        "string"
      ]
    ],
    [
      "00580c5c",
      "READ",
      [
        "storage",
        "002a01c9",
        null,
        "string"
      ]
    ],
    [
      "00580c60",
      "READ",
      [
        "storage",
        "002a01d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580c30",
      "READ",
      [
        "storage",
        "002c1356",
        null,
        "string"
      ]
    ],
    [
      "00580c5c",
      "READ",
      [
        "storage",
        "002a0209",
        null,
        "string"
      ]
    ],
    [
      "00580c60",
      "READ",
      [
        "storage",
        "002a0219",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005808f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md#insn-005808f4) · [`005808fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md#insn-005808fc) · [`00580908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md#insn-00580908)
- 新版 [`00580c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580be8.md#insn-00580c14) · [`00580c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580be8.md#insn-00580c1c) · [`00580c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580be8.md#insn-00580c28)

~~~diff
- 005808f4 ["INT_ADD", "register:40f0:8", ["const:5808f4:8", "const:4:8"]]
- 005808f4 ["CALL", null, ["callee:005891cc:8"]]
+ 00580c14 ["INT_ADD", "register:40f0:8", ["const:580c14:8", "const:4:8"]]
+ 00580c14 ["CALL", null, ["callee:005891cc:8"]]
- 005808f4 bytes 6e210094
+ 00580c14 bytes 6e210094
- 005808fc ["INT_ADD", "register:40f0:8", ["const:5808fc:8", "const:4:8"]]
- 005808fc ["CALL", null, ["callee:005894bc:8"]]
+ 00580c1c ["INT_ADD", "register:40f0:8", ["const:580c1c:8", "const:4:8"]]
+ 00580c1c ["CALL", null, ["callee:005894bc:8"]]
- 005808fc bytes 28220094
+ 00580c1c bytes 28220094
- 00580908 ["COPY", "tmp:0:8", ["const:30c:8"]]
- 00580908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00580908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00580908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00580c28 ["COPY", "tmp:0:8", ["const:356:8"]]
+ 00580c28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00580c28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00580c28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00580908 bytes 29310c91
+ 00580c28 bytes 29590d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f453ce3f1578aae925a6c3e30bc9df"></a>

### [`00580b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md) → [`00580e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580e90.md) FUN_00580e90

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056049c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/0056049c.md) · 呼出先 8件 [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`005607bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/005607bc.md) · 呼出先 8件 [`0058af84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058af84.md) [`0059796c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059796c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580ef4",
      "incomplete_value": false,
      "site": "00580f00",
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
      "definition_site": "00580bd4",
      "incomplete_value": false,
      "site": "00580be0",
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
      "00580f00",
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
      "00580f00",
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

- 旧版 [`00580bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md#insn-00580bc0) · [`00580bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md#insn-00580bc8) · [`00580bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md#insn-00580bd0)
- 新版 [`00580ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580e90.md#insn-00580ee0) · [`00580ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580e90.md#insn-00580ee8) · [`00580ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00580/00580e90.md#insn-00580ef0)

~~~diff
- 00580bc0 ["INT_ADD", "register:40f0:8", ["const:580bc0:8", "const:4:8"]]
- 00580bc0 ["CALL", null, ["callee:00c5a200:8"]]
+ 00580ee0 ["INT_ADD", "register:40f0:8", ["const:580ee0:8", "const:4:8"]]
+ 00580ee0 ["CALL", null, ["callee:00c5a200:8"]]
- 00580bc0 bytes 9c611b94
+ 00580ee0 bytes c8641b94
- 00580bc8 ["INT_ADD", "register:40f0:8", ["const:580bc8:8", "const:4:8"]]
- 00580bc8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00580ee8 ["INT_ADD", "register:40f0:8", ["const:580ee8:8", "const:4:8"]]
+ 00580ee8 ["CALL", null, ["callee:00c58f30:8"]]
- 00580bc8 bytes e65c1b94
+ 00580ee8 bytes 12601b94
- 00580bd0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00580ef0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00580bd0 bytes 68370090
+ 00580ef0 bytes 683700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f82358a8c1fdcd788dba8a17808a3b"></a>

### [`00580ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ce0.md) → [`00581000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581000.md) FUN_00581000

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ecc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc0.md) · 呼出先 9件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`0055efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055efe0.md) · 呼出先 9件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005810c0",
      "incomplete_value": true,
      "site": "005810c0",
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
      "definition_site": "00580da0",
      "incomplete_value": true,
      "site": "00580da0",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581114",
      "incomplete_value": false,
      "site": "0058111c",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580df4",
      "incomplete_value": false,
      "site": "00580dfc",
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
            "const:630:8"
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
      "definition_site": "0058112c",
      "incomplete_value": false,
      "site": "0058112c",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580e0c",
      "incomplete_value": false,
      "site": "00580e0c",
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
            "const:680:8"
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
      "005810a8",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "005810c0",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0058111c",
      "DATA",
      [
        "storage",
        "00c6c630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005810a8",
      "READ",
      [
        "storage",
        "00c9be80",
        null,
        "pointer"
      ]
    ],
    [
      "005810c0",
      "DATA",
      [
        "storage",
        "00c68428",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0058111c",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ce0.md#insn-00580d60) · [`00580d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ce0.md#insn-00580d78) · [`00580d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ce0.md#insn-00580d7c)
- 新版 [`00581080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581000.md#insn-00581080) · [`00581098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581000.md#insn-00581098) · [`0058109c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581000.md#insn-0058109c)

~~~diff
- 00580d60 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580d60 ["INT_ADD", "register:40f0:8", ["const:580d60:8", "const:4:8"]]
- 00580d60 ["CALLIND", null, ["register:0:8"]]
+ 00581080 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00581080 ["INT_ADD", "register:40f0:8", ["const:581080:8", "const:4:8"]]
+ 00581080 ["CALLIND", null, ["register:0:8"]]
- 00580d60 bytes 20013fd6
+ 00581080 bytes 20013fd6
- 00580d78 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580d78 ["INT_ADD", "register:40f0:8", ["const:580d78:8", "const:4:8"]]
- 00580d78 ["CALLIND", null, ["register:0:8"]]
+ 00581098 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00581098 ["INT_ADD", "register:40f0:8", ["const:581098:8", "const:4:8"]]
+ 00581098 ["CALLIND", null, ["register:0:8"]]
- 00580d78 bytes 20013fd6
+ 00581098 bytes 20013fd6
- 00580d7c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0058109c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00580d7c bytes c83800d0
+ 0058109c bytes c83800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be34df58d4aaddabf5fe4ccb67c28cf9"></a>

### [`00581088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581088.md) → [`005813a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005813a8.md) FUN_005813a8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ecc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc4.md) · 呼出先 12件 [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0055efe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055efe4.md) · 呼出先 12件 [`0059796c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059796c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581448",
      "incomplete_value": true,
      "site": "00581448",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b04:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581128",
      "incomplete_value": true,
      "site": "00581128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a37:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005813e4",
      "incomplete_value": false,
      "site": "005813f4",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005810c4",
      "incomplete_value": false,
      "site": "005810d4",
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
            "const:698:8"
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
      "definition_site": "005813ec",
      "incomplete_value": false,
      "site": "005813f4",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005810cc",
      "incomplete_value": false,
      "site": "005810d4",
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
            "const:738:8"
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
      "005813e4",
      "PARAM",
      [
        "storage",
        "00c6c698",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005813ec",
      "PARAM",
      [
        "storage",
        "00c6c738",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581428",
      "READ",
      [
        "storage",
        "002aea37",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005813e4",
      "PARAM",
      [
        "storage",
        "00c6d668",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005813ec",
      "PARAM",
      [
        "storage",
        "00c6d708",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581428",
      "READ",
      [
        "storage",
        "002aeb04",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005810d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581088.md#insn-005810d4) · [`005810c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581088.md#insn-005810c0) · [`005810c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581088.md#insn-005810c4)
- 新版 [`005813f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005813a8.md#insn-005813f4) · [`005813e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005813a8.md#insn-005813e0) · [`005813e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005813a8.md#insn-005813e4)

~~~diff
- 005810d4 ["INT_ADD", "register:40f0:8", ["const:5810d4:8", "const:4:8"]]
- 005810d4 ["CALL", null, ["callee:00c596b0:8"]]
+ 005813f4 ["INT_ADD", "register:40f0:8", ["const:5813f4:8", "const:4:8"]]
+ 005813f4 ["CALL", null, ["callee:00c596b0:8"]]
- 005810d4 bytes 835d1b94
+ 005813f4 bytes af601b94
- 005810c0 ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 005813e0 ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 005810c0 bytes 413700f0
+ 005813e0 bytes 61370090
- 005810c4 ["COPY", "tmp:0:8", ["const:698:8"]]
- 005810c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005810c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005810c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005813e4 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 005813e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005813e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005813e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005810c4 bytes 21601a91
+ 005813e4 bytes 21a01991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4643ff157538a9458ce544d310887df7"></a>

### [`005812bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005812bc.md) → [`005815dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005815dc.md) FUN_005815dc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ecc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc8.md) · 呼出先 10件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0055efe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055efe8.md) · 呼出先 10件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.99% / 新版 90.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581668",
      "incomplete_value": true,
      "site": "00581678",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:baa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581348",
      "incomplete_value": true,
      "site": "00581358",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ad3:8"
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
      "definition_site": "0058166c",
      "incomplete_value": true,
      "site": "0058167c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058134c",
      "incomplete_value": true,
      "site": "0058135c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581670",
      "incomplete_value": true,
      "site": "00581680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00581350",
      "incomplete_value": true,
      "site": "00581360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00581618",
      "PARAM",
      [
        "storage",
        "00c6c698",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581620",
      "PARAM",
      [
        "storage",
        "00c6c6a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581668",
      "READ",
      [
        "storage",
        "002afad3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581618",
      "PARAM",
      [
        "storage",
        "00c6d668",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581620",
      "PARAM",
      [
        "storage",
        "00c6d678",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581668",
      "READ",
      [
        "storage",
        "002afbaa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058130c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005812bc.md#insn-0058130c) · [`005812f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005812bc.md#insn-005812f4) · [`005812f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005812bc.md#insn-005812f8)
- 新版 [`0058162c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005815dc.md#insn-0058162c) · [`00581614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005815dc.md#insn-00581614) · [`00581618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005815dc.md#insn-00581618)

~~~diff
- 0058130c ["INT_ADD", "register:40f0:8", ["const:58130c:8", "const:4:8"]]
- 0058130c ["CALL", null, ["callee:00c596b0:8"]]
+ 0058162c ["INT_ADD", "register:40f0:8", ["const:58162c:8", "const:4:8"]]
+ 0058162c ["CALL", null, ["callee:00c596b0:8"]]
- 0058130c bytes f55c1b94
+ 0058162c bytes 21601b94
- 005812f4 ["COPY", "register:4008:8", ["const:c6c000:8"]]
+ 00581614 ["COPY", "register:4008:8", ["const:c6d000:8"]]
- 005812f4 bytes 413700f0
+ 00581614 bytes 61370090
- 005812f8 ["COPY", "tmp:0:8", ["const:698:8"]]
- 005812f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005812f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005812f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00581618 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00581618 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00581618 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00581618 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005812f8 bytes 21601a91
+ 00581618 bytes 21a01991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772aee4eff5afe9bd564e472c2102849"></a>

### [`005814d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md) → [`005817f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005817f4.md) FUN_005817f4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ed48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ed48.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`0055f068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f068.md) · 呼出先 13件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0058231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.97% / 新版 90.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581878",
      "incomplete_value": true,
      "site": "0058188c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00581558",
      "incomplete_value": true,
      "site": "0058156c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581878",
      "incomplete_value": true,
      "site": "0058188c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00581558",
      "incomplete_value": true,
      "site": "0058156c",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581884",
      "incomplete_value": true,
      "site": "00581890",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00581564",
      "incomplete_value": true,
      "site": "00581570",
      "value": [
        "LOAD",
        "16",
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
      "0058186c",
      "READ",
      [
        "storage",
        "002c2f10",
        null,
        null
      ]
    ],
    [
      "00581878",
      "READ",
      [
        "storage",
        "002b74d6",
        null,
        "string"
      ]
    ],
    [
      "00581878",
      "READ",
      [
        "storage",
        "002b74e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058186c",
      "READ",
      [
        "storage",
        "002c2f60",
        null,
        null
      ]
    ],
    [
      "00581878",
      "READ",
      [
        "storage",
        "002b75a5",
        null,
        "string"
      ]
    ],
    [
      "00581878",
      "READ",
      [
        "storage",
        "002b75b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md#insn-00581678) · [`005816e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md#insn-005816e0) · [`00581508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md#insn-00581508)
- 新版 [`00581998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005817f4.md#insn-00581998) · [`00581a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005817f4.md#insn-00581a00) · [`00581828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005817f4.md#insn-00581828)

~~~diff
- 00581678 ["INT_ADD", "register:40f0:8", ["const:581678:8", "const:4:8"]]
- 00581678 ["CALL", null, ["ram:589f48:8"]]
+ 00581998 ["INT_ADD", "register:40f0:8", ["const:581998:8", "const:4:8"]]
+ 00581998 ["CALL", null, ["ram:58a268:8"]]
- 00581678 bytes 34220094
+ 00581998 bytes 34220094
- 005816e0 ["INT_ADD", "register:40f0:8", ["const:5816e0:8", "const:4:8"]]
- 005816e0 ["CALL", null, ["ram:589f48:8"]]
+ 00581a00 ["INT_ADD", "register:40f0:8", ["const:581a00:8", "const:4:8"]]
+ 00581a00 ["CALL", null, ["ram:58a268:8"]]
- 005816e0 bytes 1a220094
+ 00581a00 bytes 1a220094
- 00581508 ["INT_ADD", "register:40f0:8", ["const:581508:8", "const:4:8"]]
- 00581508 ["CALL", null, ["callee:005891cc:8"]]
+ 00581828 ["INT_ADD", "register:40f0:8", ["const:581828:8", "const:4:8"]]
+ 00581828 ["CALL", null, ["callee:005891cc:8"]]
- 00581508 bytes 691e0094
+ 00581828 bytes 691e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf67ed2367bc189fe2b0f72a2bf9e66"></a>

### [`005817a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md) → [`00581ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581ac4.md) FUN_00581ac4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0055f0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d4.md) [`0055f0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 2件 [`0055f3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f3f4.md) [`0055f3f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f3f8.md) · 呼出先 13件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0058231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581b3c",
      "incomplete_value": true,
      "site": "00581b50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058181c",
      "incomplete_value": true,
      "site": "00581830",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f10:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581c80",
      "incomplete_value": false,
      "site": "00581c8c",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581960",
      "incomplete_value": false,
      "site": "0058196c",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00581c68",
      "value": [
        "leaf",
        "ram:58a268:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00581948",
      "value": [
        "leaf",
        "ram:589f48:8"
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
      "00581b3c",
      "READ",
      [
        "storage",
        "002c2f10",
        null,
        null
      ]
    ],
    [
      "00581b48",
      "READ",
      [
        "storage",
        "002b74d6",
        null,
        "string"
      ]
    ],
    [
      "00581b48",
      "READ",
      [
        "storage",
        "002b74e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581b3c",
      "READ",
      [
        "storage",
        "002c2f60",
        null,
        null
      ]
    ],
    [
      "00581b48",
      "READ",
      [
        "storage",
        "002b75a5",
        null,
        "string"
      ]
    ],
    [
      "00581b48",
      "READ",
      [
        "storage",
        "002b75b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md#insn-00581948) · [`005819b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md#insn-005819b0) · [`005817d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md#insn-005817d8)
- 新版 [`00581c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581ac4.md#insn-00581c68) · [`00581cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581ac4.md#insn-00581cd0) · [`00581af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581ac4.md#insn-00581af8)

~~~diff
- 00581948 ["INT_ADD", "register:40f0:8", ["const:581948:8", "const:4:8"]]
- 00581948 ["CALL", null, ["ram:589f48:8"]]
+ 00581c68 ["INT_ADD", "register:40f0:8", ["const:581c68:8", "const:4:8"]]
+ 00581c68 ["CALL", null, ["ram:58a268:8"]]
- 00581948 bytes 80210094
+ 00581c68 bytes 80210094
- 005819b0 ["INT_ADD", "register:40f0:8", ["const:5819b0:8", "const:4:8"]]
- 005819b0 ["CALL", null, ["ram:589f48:8"]]
+ 00581cd0 ["INT_ADD", "register:40f0:8", ["const:581cd0:8", "const:4:8"]]
+ 00581cd0 ["CALL", null, ["ram:58a268:8"]]
- 005819b0 bytes 66210094
+ 00581cd0 bytes 66210094
- 005817d8 ["INT_ADD", "register:40f0:8", ["const:5817d8:8", "const:4:8"]]
- 005817d8 ["CALL", null, ["callee:005891cc:8"]]
+ 00581af8 ["INT_ADD", "register:40f0:8", ["const:581af8:8", "const:4:8"]]
+ 00581af8 ["CALL", null, ["callee:005891cc:8"]]
- 005817d8 bytes b51d0094
+ 00581af8 bytes b51d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0845496b393d5439453c9c00a5556faa"></a>

### [`00581a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md) → [`00581d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581d94.md) FUN_00581d94

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0055e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md) [`0055e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b0.md) [`0055e8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md) · 呼出先 2件 [`005827f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`0055eab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055eab0.md) [`0055ebd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055ebd0.md) [`0055ebd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055ebd4.md) · 呼出先 2件 [`00582b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582b18.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00581dbc",
      "incomplete_value": false,
      "site": "00581dc8",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581a9c",
      "incomplete_value": false,
      "site": "00581aa8",
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
            "const:818:8"
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
      "00581dc8",
      "DATA",
      [
        "storage",
        "00c6c818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581dc8",
      "DATA",
      [
        "storage",
        "00c6d7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md#insn-00581a90) · [`00581a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md#insn-00581a98) · [`00581a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md#insn-00581a9c)
- 新版 [`00581db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581d94.md#insn-00581db0) · [`00581db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581d94.md#insn-00581db8) · [`00581dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581d94.md#insn-00581dbc)

~~~diff
- 00581a90 ["INT_ADD", "register:40f0:8", ["const:581a90:8", "const:4:8"]]
- 00581a90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00581db0 ["INT_ADD", "register:40f0:8", ["const:581db0:8", "const:4:8"]]
+ 00581db0 ["CALL", null, ["callee:00c58f30:8"]]
- 00581a90 bytes 34591b94
+ 00581db0 bytes 605c1b94
- 00581a98 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00581db8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581a98 bytes 483700f0
+ 00581db8 bytes 68370090
- 00581a9c ["COPY", "tmp:0:8", ["const:818:8"]]
- 00581a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581dbc ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00581dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581a9c bytes 08612091
+ 00581dbc bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d5dcd03d0f32b81f350b7e99f1cc34f"></a>

### [`00581ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md) → [`00581e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581e08.md) FUN_00581e08

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0055ea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md) [`0055eb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md) · 呼出先 2件 [`00582d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`0055ed28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055ed28.md) [`0055ee7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055e/0055ee7c.md) · 呼出先 2件 [`00583040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583040.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00581e38",
      "incomplete_value": false,
      "site": "00581e44",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581b18",
      "incomplete_value": false,
      "site": "00581b24",
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
            "const:8c0:8"
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
      "00581e44",
      "DATA",
      [
        "storage",
        "00c6c8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581e44",
      "DATA",
      [
        "storage",
        "00c6d890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md#insn-00581b0c) · [`00581b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md#insn-00581b14) · [`00581b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md#insn-00581b18)
- 新版 [`00581e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581e08.md#insn-00581e2c) · [`00581e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581e08.md#insn-00581e34) · [`00581e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581e08.md#insn-00581e38)

~~~diff
- 00581b0c ["INT_ADD", "register:40f0:8", ["const:581b0c:8", "const:4:8"]]
- 00581b0c ["CALL", null, ["callee:00c58f30:8"]]
+ 00581e2c ["INT_ADD", "register:40f0:8", ["const:581e2c:8", "const:4:8"]]
+ 00581e2c ["CALL", null, ["callee:00c58f30:8"]]
- 00581b0c bytes 15591b94
+ 00581e2c bytes 415c1b94
- 00581b14 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00581e34 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581b14 bytes 483700f0
+ 00581e34 bytes 68370090
- 00581b18 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00581b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581e38 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00581e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581b18 bytes 08012391
+ 00581e38 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64158d8289300fe07edfdf2a161b8fe6"></a>

### [`00581e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e10.md) → [`00582130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582130.md) FUN_00582130

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
      "definition_site": "00582134",
      "incomplete_value": false,
      "site": "00582138",
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
      "definition_site": "00581e14",
      "incomplete_value": false,
      "site": "00581e18",
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
      "00582138",
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
      "00582138",
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

- 旧版 [`00581e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e10.md#insn-00581e10) · [`00581e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e10.md#insn-00581e14)
- 新版 [`00582130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582130.md#insn-00582130) · [`00582134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582130.md#insn-00582134)

~~~diff
- 00581e10 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00582130 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581e10 bytes 483700f0
+ 00582130 bytes 483700f0
- 00581e14 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00581e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582134 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00582134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e14 bytes 08811791
+ 00582134 bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1da7d74150c2789fdfc0d7a4112aedf"></a>

### [`00581e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e60.md) → [`00582180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582180.md) FUN_00582180

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
      "definition_site": "00582184",
      "incomplete_value": false,
      "site": "00582188",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581e64",
      "incomplete_value": false,
      "site": "00581e68",
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
            "const:630:8"
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
      "00582188",
      "DATA",
      [
        "storage",
        "00c6c630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582188",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e60.md#insn-00581e60) · [`00581e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e60.md#insn-00581e64)
- 新版 [`00582180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582180.md#insn-00582180) · [`00582184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582180.md#insn-00582184)

~~~diff
- 00581e60 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00582180 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581e60 bytes 483700f0
+ 00582180 bytes 483700f0
- 00581e64 ["COPY", "tmp:0:8", ["const:630:8"]]
- 00581e64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582184 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00582184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e64 bytes 08c11891
+ 00582184 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa1fae87b68311b5e9521e81c42054a"></a>

### [`00581e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e70.md) → [`00582190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582190.md) FUN_00582190

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
      "definition_site": "005821a0",
      "incomplete_value": false,
      "site": "005821a8",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581e80",
      "incomplete_value": false,
      "site": "00581e88",
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
            "const:630:8"
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
      "005821a8",
      "DATA",
      [
        "storage",
        "00c6c630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005821a8",
      "DATA",
      [
        "storage",
        "00c6d600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e70.md#insn-00581e7c) · [`00581e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e70.md#insn-00581e80) · [`00581e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e70.md#insn-00581e8c)
- 新版 [`0058219c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582190.md#insn-0058219c) · [`005821a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582190.md#insn-005821a0) · [`005821ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582190.md#insn-005821ac)

~~~diff
- 00581e7c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058219c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581e7c bytes 483700f0
+ 0058219c bytes 483700f0
- 00581e80 ["COPY", "tmp:0:8", ["const:630:8"]]
- 00581e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005821a0 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 005821a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005821a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005821a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e80 bytes 08c11891
+ 005821a0 bytes 08011891
- 00581e8c ["INT_ADD", "register:40f0:8", ["const:581e8c:8", "const:4:8"]]
- 00581e8c ["CALL", null, ["callee:00c58f40:8"]]
+ 005821ac ["INT_ADD", "register:40f0:8", ["const:5821ac:8", "const:4:8"]]
+ 005821ac ["CALL", null, ["callee:00c58f40:8"]]
- 00581e8c bytes 39581b94
+ 005821ac bytes 655b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d5b24023b0815c00aed9cea31aaa8c"></a>

### [`00581f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f00.md) → [`00582220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582220.md) FUN_00582220

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
      "definition_site": "00582224",
      "incomplete_value": false,
      "site": "00582228",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581f04",
      "incomplete_value": false,
      "site": "00581f08",
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
            "const:6d0:8"
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
      "00582228",
      "DATA",
      [
        "storage",
        "00c6c6d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582228",
      "DATA",
      [
        "storage",
        "00c6d6a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f00.md#insn-00581f00) · [`00581f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f00.md#insn-00581f04)
- 新版 [`00582220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582220.md#insn-00582220) · [`00582224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582220.md#insn-00582224)

~~~diff
- 00581f00 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00582220 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581f00 bytes 483700f0
+ 00582220 bytes 483700f0
- 00581f04 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00581f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582224 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00582224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581f04 bytes 08411b91
+ 00582224 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b43dc5acd0945e10bbfeb6479fc3d363"></a>

### [`00581f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f10.md) → [`00582230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582230.md) FUN_00582230

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
      "definition_site": "00582240",
      "incomplete_value": false,
      "site": "00582248",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581f20",
      "incomplete_value": false,
      "site": "00581f28",
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
            "const:6d0:8"
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
      "00582248",
      "DATA",
      [
        "storage",
        "00c6c6d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582248",
      "DATA",
      [
        "storage",
        "00c6d6a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f10.md#insn-00581f1c) · [`00581f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f10.md#insn-00581f20) · [`00581f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f10.md#insn-00581f2c)
- 新版 [`0058223c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582230.md#insn-0058223c) · [`00582240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582230.md#insn-00582240) · [`0058224c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582230.md#insn-0058224c)

~~~diff
- 00581f1c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058223c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581f1c bytes 483700f0
+ 0058223c bytes 483700f0
- 00581f20 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 00581f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582240 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00582240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581f20 bytes 08411b91
+ 00582240 bytes 08811a91
- 00581f2c ["INT_ADD", "register:40f0:8", ["const:581f2c:8", "const:4:8"]]
- 00581f2c ["CALL", null, ["callee:00c58f40:8"]]
+ 0058224c ["INT_ADD", "register:40f0:8", ["const:58224c:8", "const:4:8"]]
+ 0058224c ["CALL", null, ["callee:00c58f40:8"]]
- 00581f2c bytes 11581b94
+ 0058224c bytes 3d5b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80adb5d7afd781129bb3be0cf16482fb"></a>

### [`00581fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fac.md) → [`005822cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822cc.md) FUN_005822cc

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
      "definition_site": "005822d0",
      "incomplete_value": false,
      "site": "005822d4",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581fb0",
      "incomplete_value": false,
      "site": "00581fb4",
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
            "const:760:8"
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
      "005822d4",
      "DATA",
      [
        "storage",
        "00c6c760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005822d4",
      "DATA",
      [
        "storage",
        "00c6d730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fac.md#insn-00581fac) · [`00581fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fac.md#insn-00581fb0)
- 新版 [`005822cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822cc.md#insn-005822cc) · [`005822d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822cc.md#insn-005822d0)

~~~diff
- 00581fac ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005822cc ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581fac bytes 483700f0
+ 005822cc bytes 483700f0
- 00581fb0 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00581fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005822d0 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 005822d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005822d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005822d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581fb0 bytes 08811d91
+ 005822d0 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57bb4c87faef67c2fc00789438c03c50"></a>

### [`00581fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fbc.md) → [`005822dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822dc.md) FUN_005822dc

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
      "definition_site": "005822ec",
      "incomplete_value": false,
      "site": "005822f4",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581fcc",
      "incomplete_value": false,
      "site": "00581fd4",
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
            "const:760:8"
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
      "005822f4",
      "DATA",
      [
        "storage",
        "00c6c760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005822f4",
      "DATA",
      [
        "storage",
        "00c6d730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fbc.md#insn-00581fc8) · [`00581fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fbc.md#insn-00581fcc) · [`00581fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fbc.md#insn-00581fd8)
- 新版 [`005822e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822dc.md#insn-005822e8) · [`005822ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822dc.md#insn-005822ec) · [`005822f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005822dc.md#insn-005822f8)

~~~diff
- 00581fc8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005822e8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00581fc8 bytes 483700f0
+ 005822e8 bytes 483700f0
- 00581fcc ["COPY", "tmp:0:8", ["const:760:8"]]
- 00581fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005822ec ["COPY", "tmp:0:8", ["const:730:8"]]
+ 005822ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005822ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005822ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581fcc bytes 08811d91
+ 005822ec bytes 08c11c91
- 00581fd8 ["INT_ADD", "register:40f0:8", ["const:581fd8:8", "const:4:8"]]
- 00581fd8 ["CALL", null, ["callee:00c58f40:8"]]
+ 005822f8 ["INT_ADD", "register:40f0:8", ["const:5822f8:8", "const:4:8"]]
+ 005822f8 ["CALL", null, ["callee:00c58f40:8"]]
- 00581fd8 bytes e6571b94
+ 005822f8 bytes 125b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b165fe92ab498d5e9be5cd45a862ff"></a>

### [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) → [`0058231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md) FUN_0058231c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005814d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md) [`005817a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md) · 呼出先 5件 [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`005897d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`005817f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/005817f4.md) [`00581ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581ac4.md) · 呼出先 5件 [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589af0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.63% / 新版 81.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582358",
      "incomplete_value": false,
      "site": "00582358",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582038",
      "incomplete_value": false,
      "site": "00582038",
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
            "const:7b0:8"
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
      "definition_site": "0058239c",
      "incomplete_value": true,
      "site": "005823a4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:2c3000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058207c",
      "incomplete_value": true,
      "site": "00582084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb0:8"
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
      "definition_site": "00582398",
      "incomplete_value": true,
      "site": "005823a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:43:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582078",
      "incomplete_value": true,
      "site": "00582088",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00582358",
      "DATA",
      [
        "storage",
        "00c6c7b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00582398",
      "READ",
      [
        "storage",
        "002b4f65",
        null,
        "string"
      ]
    ],
    [
      "00582398",
      "READ",
      [
        "storage",
        "002b4f75",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00582358",
      "DATA",
      [
        "storage",
        "00c6d780",
        null,
        "undefined *"
      ]
    ],
    [
      "00582398",
      "READ",
      [
        "storage",
        "002b5043",
        null,
        "string"
      ]
    ],
    [
      "00582398",
      "READ",
      [
        "storage",
        "002b5053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md#insn-00582014) · [`00582018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md#insn-00582018) · [`00582040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md#insn-00582040)
- 新版 [`00582334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md#insn-00582334) · [`00582338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md#insn-00582338) · [`00582360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/0058231c.md#insn-00582360)

~~~diff
- 00582014 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00582334 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00582014 bytes 493700d0
+ 00582334 bytes 493700f0
- 00582018 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00582018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582338 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 00582338 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582338 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582338 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582018 bytes 29c11e91
+ 00582338 bytes 29011e91
- 00582040 ["INT_ADD", "register:40f0:8", ["const:582040:8", "const:4:8"]]
- 00582040 ["CALL", null, ["callee:00589af0:8"]]
+ 00582360 ["INT_ADD", "register:40f0:8", ["const:582360:8", "const:4:8"]]
+ 00582360 ["CALL", null, ["callee:00589af0:8"]]
- 00582040 bytes e41d0094
+ 00582360 bytes e41d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937dc8291bc86799156569f5f564500e"></a>

### [`005821d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821d8.md) → [`005824f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005824f8.md) FUN_005824f8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md)

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
      "definition_site": "00582500",
      "incomplete_value": false,
      "site": "00582500",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005821e0",
      "incomplete_value": false,
      "site": "005821e0",
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
            "const:7b0:8"
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
      "00582500",
      "DATA",
      [
        "storage",
        "00c6c7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582500",
      "DATA",
      [
        "storage",
        "00c6d780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005821d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821d8.md#insn-005821d8) · [`005821dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821d8.md#insn-005821dc)
- 新版 [`005824f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005824f8.md#insn-005824f8) · [`005824fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005824f8.md#insn-005824fc)

~~~diff
- 005821d8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005824f8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005821d8 bytes 483700d0
+ 005824f8 bytes 483700f0
- 005821dc ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 005821dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005821dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005821dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005824fc ["COPY", "tmp:0:8", ["const:780:8"]]
+ 005824fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005824fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005824fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005821dc bytes 08c11e91
+ 005824fc bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d23ab8b33e476c139b46d03e4c685966"></a>

### [`005821e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821e8.md) → [`00582508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582508.md) FUN_00582508

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00582520",
      "incomplete_value": false,
      "site": "00582520",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582200",
      "incomplete_value": false,
      "site": "00582200",
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
            "const:7b0:8"
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
      "00582520",
      "DATA",
      [
        "storage",
        "00c6c7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582520",
      "DATA",
      [
        "storage",
        "00c6d780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005821f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821e8.md#insn-005821f4) · [`005821f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821e8.md#insn-005821f8) · [`00582204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821e8.md#insn-00582204)
- 新版 [`00582514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582508.md#insn-00582514) · [`00582518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582508.md#insn-00582518) · [`00582524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582508.md#insn-00582524)

~~~diff
- 005821f4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00582514 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005821f4 bytes 483700d0
+ 00582514 bytes 483700f0
- 005821f8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 005821f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005821f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005821f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582518 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 00582518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005821f8 bytes 08c11e91
+ 00582518 bytes 08011e91
- 00582204 ["INT_ADD", "register:40f0:8", ["const:582204:8", "const:4:8"]]
- 00582204 ["CALL", null, ["callee:0058ac1c:8"]]
+ 00582524 ["INT_ADD", "register:40f0:8", ["const:582524:8", "const:4:8"]]
+ 00582524 ["CALL", null, ["callee:0058ac1c:8"]]
- 00582204 bytes be210094
+ 00582524 bytes be210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b9bd6bf2bd8c4e3ea2bcd34c2ab3572"></a>

### [`00582218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md) → [`00582538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582538.md) FUN_00582538

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00589d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`00589bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb8.md) [`00589f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md) [`0058a028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a028.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582614",
      "incomplete_value": false,
      "site": "00582620",
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
      "definition_site": "005822f4",
      "incomplete_value": false,
      "site": "00582300",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00582650",
      "value": [
        "leaf",
        "ram:58a268:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00582330",
      "value": [
        "leaf",
        "ram:589f48:8"
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
      "00582620",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00582650",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ],
  "added": [
    [
      "00582620",
      "DATA",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer"
      ]
    ],
    [
      "00582650",
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

- 旧版 [`00582330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md#insn-00582330) · [`00582248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md#insn-00582248) · [`00582260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md#insn-00582260)
- 新版 [`00582650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582538.md#insn-00582650) · [`00582568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582538.md#insn-00582568) · [`00582580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582538.md#insn-00582580)

~~~diff
- 00582330 ["INT_ADD", "register:40f0:8", ["const:582330:8", "const:4:8"]]
- 00582330 ["CALL", null, ["ram:589f48:8"]]
+ 00582650 ["INT_ADD", "register:40f0:8", ["const:582650:8", "const:4:8"]]
+ 00582650 ["CALL", null, ["ram:58a268:8"]]
- 00582330 bytes 061f0094
+ 00582650 bytes 061f0094
- 00582248 ["INT_ADD", "register:40f0:8", ["const:582248:8", "const:4:8"]]
- 00582248 ["CALL", null, ["callee:005891cc:8"]]
+ 00582568 ["INT_ADD", "register:40f0:8", ["const:582568:8", "const:4:8"]]
+ 00582568 ["CALL", null, ["callee:005891cc:8"]]
- 00582248 bytes 191b0094
+ 00582568 bytes 191b0094
- 00582260 ["INT_ADD", "register:40f0:8", ["const:582260:8", "const:4:8"]]
- 00582260 ["CALL", null, ["callee:0058a028:8"]]
+ 00582580 ["INT_ADD", "register:40f0:8", ["const:582580:8", "const:4:8"]]
+ 00582580 ["CALL", null, ["callee:0058a028:8"]]
- 00582260 bytes aa1e0094
+ 00582580 bytes aa1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0187e4953c3a59c6d7120f7475c638d1"></a>

### [`005823a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md) → [`005826c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005826c0.md) FUN_005826c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00589db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589db0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`00589bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb8.md) [`00589f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md) [`0058a0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a0d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005827a4",
      "incomplete_value": false,
      "site": "005827b0",
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
      "definition_site": "00582484",
      "incomplete_value": false,
      "site": "00582490",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005827e0",
      "value": [
        "leaf",
        "ram:58a268:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005824c0",
      "value": [
        "leaf",
        "ram:589f48:8"
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
      "005827b0",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005827e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ],
  "added": [
    [
      "005827b0",
      "DATA",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005827e0",
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

- 旧版 [`005824c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md#insn-005824c0) · [`005823d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md#insn-005823d4) · [`005823ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md#insn-005823ec)
- 新版 [`005827e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005826c0.md#insn-005827e0) · [`005826f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005826c0.md#insn-005826f4) · [`0058270c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005826c0.md#insn-0058270c)

~~~diff
- 005824c0 ["INT_ADD", "register:40f0:8", ["const:5824c0:8", "const:4:8"]]
- 005824c0 ["CALL", null, ["ram:589f48:8"]]
+ 005827e0 ["INT_ADD", "register:40f0:8", ["const:5827e0:8", "const:4:8"]]
+ 005827e0 ["CALL", null, ["ram:58a268:8"]]
- 005824c0 bytes a21e0094
+ 005827e0 bytes a21e0094
- 005823d4 ["INT_ADD", "register:40f0:8", ["const:5823d4:8", "const:4:8"]]
- 005823d4 ["CALL", null, ["callee:005891cc:8"]]
+ 005826f4 ["INT_ADD", "register:40f0:8", ["const:5826f4:8", "const:4:8"]]
+ 005826f4 ["CALL", null, ["callee:005891cc:8"]]
- 005823d4 bytes b61a0094
+ 005826f4 bytes b61a0094
- 005823ec ["INT_ADD", "register:40f0:8", ["const:5823ec:8", "const:4:8"]]
- 005823ec ["CALL", null, ["callee:0058a0d0:8"]]
+ 0058270c ["INT_ADD", "register:40f0:8", ["const:58270c:8", "const:4:8"]]
+ 0058270c ["CALL", null, ["callee:0058a0d0:8"]]
- 005823ec bytes 711e0094
+ 0058270c bytes 711e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a66fb381b011b340da6b4a8db307a79d"></a>

### [`00582534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md) → [`00582854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582854.md) FUN_00582854

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00589db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589db0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`00589bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb8.md) [`00589f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md) [`0058a0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a0d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582924",
      "incomplete_value": false,
      "site": "00582930",
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
      "definition_site": "00582604",
      "incomplete_value": false,
      "site": "00582610",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00582960",
      "value": [
        "leaf",
        "ram:58a268:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00582640",
      "value": [
        "leaf",
        "ram:589f48:8"
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
      "00582930",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00582960",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ],
  "added": [
    [
      "00582930",
      "DATA",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer"
      ]
    ],
    [
      "00582960",
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

- 旧版 [`00582640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md#insn-00582640) · [`00582568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md#insn-00582568) · [`00582580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md#insn-00582580)
- 新版 [`00582960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582854.md#insn-00582960) · [`00582888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582854.md#insn-00582888) · [`005828a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582854.md#insn-005828a0)

~~~diff
- 00582640 ["INT_ADD", "register:40f0:8", ["const:582640:8", "const:4:8"]]
- 00582640 ["CALL", null, ["ram:589f48:8"]]
+ 00582960 ["INT_ADD", "register:40f0:8", ["const:582960:8", "const:4:8"]]
+ 00582960 ["CALL", null, ["ram:58a268:8"]]
- 00582640 bytes 421e0094
+ 00582960 bytes 421e0094
- 00582568 ["INT_ADD", "register:40f0:8", ["const:582568:8", "const:4:8"]]
- 00582568 ["CALL", null, ["callee:005891cc:8"]]
+ 00582888 ["INT_ADD", "register:40f0:8", ["const:582888:8", "const:4:8"]]
+ 00582888 ["CALL", null, ["callee:005891cc:8"]]
- 00582568 bytes 511a0094
+ 00582888 bytes 511a0094
- 00582580 ["INT_ADD", "register:40f0:8", ["const:582580:8", "const:4:8"]]
- 00582580 ["CALL", null, ["callee:0058a0d0:8"]]
+ 005828a0 ["INT_ADD", "register:40f0:8", ["const:5828a0:8", "const:4:8"]]
+ 005828a0 ["CALL", null, ["callee:0058a0d0:8"]]
- 00582580 bytes 0c1e0094
+ 005828a0 bytes 0c1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eac8f26ec95d6fe9b7436d9cdc3599e"></a>

### [`005826b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md) → [`005829d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005829d0.md) FUN_005829d0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`00589bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb8.md) [`00589f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589f48.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582a60",
      "incomplete_value": false,
      "site": "00582a6c",
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
      "definition_site": "00582740",
      "incomplete_value": false,
      "site": "0058274c",
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
      "00582a6c",
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
      "00582a6c",
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

- 旧版 [`005826cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md#insn-005826cc) · [`005826d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md#insn-005826d8) · [`005826ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md#insn-005826ec)
- 新版 [`005829ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005829d0.md#insn-005829ec) · [`005829f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005829d0.md#insn-005829f8) · [`00582a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/005829d0.md#insn-00582a0c)

~~~diff
- 005826cc ["INT_ADD", "register:40f0:8", ["const:5826cc:8", "const:4:8"]]
- 005826cc ["CALL", null, ["callee:005891cc:8"]]
+ 005829ec ["INT_ADD", "register:40f0:8", ["const:5829ec:8", "const:4:8"]]
+ 005829ec ["CALL", null, ["callee:005891cc:8"]]
- 005826cc bytes f8190094
+ 005829ec bytes f8190094
- 005826d8 ["INT_ADD", "register:40f0:8", ["const:5826d8:8", "const:4:8"]]
- 005826d8 ["CALL", null, ["callee:00589bb8:8"]]
+ 005829f8 ["INT_ADD", "register:40f0:8", ["const:5829f8:8", "const:4:8"]]
+ 005829f8 ["CALL", null, ["callee:00589bb8:8"]]
- 005826d8 bytes 701c0094
+ 005829f8 bytes 701c0094
- 005826ec ["INT_ADD", "register:40f0:8", ["const:5826ec:8", "const:4:8"]]
- 005826ec ["CALL", null, ["callee:00497b94:8"]]
+ 00582a0c ["INT_ADD", "register:40f0:8", ["const:582a0c:8", "const:4:8"]]
+ 00582a0c ["CALL", null, ["callee:00497b94:8"]]
- 005826ec bytes 6254fc97
+ 00582a0c bytes 6254fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f20dafd13a84acfecf460aa0125a042a"></a>

### [`005827b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827b8.md) → [`00582ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ad8.md) FUN_00582ad8

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
      "definition_site": "00582ae8",
      "incomplete_value": false,
      "site": "00582af0",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005827c8",
      "incomplete_value": false,
      "site": "005827d0",
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
      "00582af0",
      "DATA",
      [
        "storage",
        "00c6c818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582af0",
      "DATA",
      [
        "storage",
        "00c6d7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005827c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827b8.md#insn-005827c4) · [`005827c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827b8.md#insn-005827c8) · [`005827d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827b8.md#insn-005827d4)
- 新版 [`00582ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ad8.md#insn-00582ae4) · [`00582ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ad8.md#insn-00582ae8) · [`00582af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ad8.md#insn-00582af4)

~~~diff
- 005827c4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00582ae4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 005827c4 bytes 483700d0
+ 00582ae4 bytes 483700f0
- 005827c8 ["COPY", "tmp:0:8", ["const:818:8"]]
- 005827c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005827c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005827c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582ae8 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00582ae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582ae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582ae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005827c8 bytes 08612091
+ 00582ae8 bytes 08a11f91
- 005827d4 ["INT_ADD", "register:40f0:8", ["const:5827d4:8", "const:4:8"]]
- 005827d4 ["CALL", null, ["callee:00c58f40:8"]]
+ 00582af4 ["INT_ADD", "register:40f0:8", ["const:582af4:8", "const:4:8"]]
+ 00582af4 ["CALL", null, ["callee:00c58f40:8"]]
- 005827d4 bytes e7551b94
+ 00582af4 bytes 13591b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cad1f021b6e6960f7c1c875bb25f412"></a>

### [`005827f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md) → [`00582b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582b18.md) FUN_00582b18

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00581a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)
- 新版 呼出元 1件 [`00581d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581d94.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582b48",
      "incomplete_value": false,
      "site": "00582b48",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582828",
      "incomplete_value": false,
      "site": "00582828",
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
            "const:868:8"
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
      "00582b48",
      "DATA",
      [
        "storage",
        "00c6c868",
        null,
        "undefined *"
      ]
    ],
    [
      "00582b70",
      "DATA",
      [
        "storage",
        "0035444d",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "00582b48",
      "DATA",
      [
        "storage",
        "00c6d838",
        null,
        "undefined *"
      ]
    ],
    [
      "00582b70",
      "DATA",
      [
        "storage",
        "0035444d",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md#insn-00582814) · [`00582818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md#insn-00582818) · [`00582860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md#insn-00582860)
- 新版 [`00582b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582b18.md#insn-00582b34) · [`00582b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582b18.md#insn-00582b38) · [`00582b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582b18.md#insn-00582b80)

~~~diff
- 00582814 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00582b34 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00582814 bytes 493700d0
+ 00582b34 bytes 493700f0
- 00582818 ["COPY", "tmp:0:8", ["const:868:8"]]
- 00582818 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582818 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582818 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582b38 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00582b38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582b38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582b38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582818 bytes 29a12191
+ 00582b38 bytes 29e12091
- 00582860 ["INT_ADD", "register:40f0:8", ["const:582860:8", "const:4:8"]]
- 00582860 ["CALL", null, ["callee:00c59e90:8"]]
+ 00582b80 ["INT_ADD", "register:40f0:8", ["const:582b80:8", "const:4:8"]]
+ 00582b80 ["CALL", null, ["callee:00c59e90:8"]]
- 00582860 bytes 98591b94
+ 00582b80 bytes c45c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d2c82c9e96f0bdae8bcac82ce0693d"></a>

### [`005829b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829b0.md) → [`00582cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cd0.md) FUN_00582cd0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00582ce0",
      "incomplete_value": false,
      "site": "00582ce0",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005829c0",
      "incomplete_value": false,
      "site": "005829c0",
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
            "const:868:8"
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
      "00582ce0",
      "DATA",
      [
        "storage",
        "00c6c868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582ce0",
      "DATA",
      [
        "storage",
        "00c6d838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005829b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829b0.md#insn-005829b8) · [`005829bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829b0.md#insn-005829bc)
- 新版 [`00582cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cd0.md#insn-00582cd8) · [`00582cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cd0.md#insn-00582cdc)

~~~diff
- 005829b8 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00582cd8 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 005829b8 bytes 493700d0
+ 00582cd8 bytes 493700f0
- 005829bc ["COPY", "tmp:0:8", ["const:868:8"]]
- 005829bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005829bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005829bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582cdc ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00582cdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582cdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582cdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005829bc bytes 29a12191
+ 00582cdc bytes 29e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d133e2c4bf20fc7976e3725361b0a140"></a>

### [`005829d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829d8.md) → [`00582cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cf8.md) FUN_00582cf8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00582d04",
      "incomplete_value": false,
      "site": "00582d04",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005829e4",
      "incomplete_value": false,
      "site": "005829e4",
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
            "const:868:8"
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
      "00582d04",
      "DATA",
      [
        "storage",
        "00c6c868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582d04",
      "DATA",
      [
        "storage",
        "00c6d838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005829dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829d8.md#insn-005829dc) · [`005829e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829d8.md#insn-005829e0) · [`00582a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829d8.md#insn-00582a08)
- 新版 [`00582cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cf8.md#insn-00582cfc) · [`00582d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cf8.md#insn-00582d00) · [`00582d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582cf8.md#insn-00582d28)

~~~diff
- 005829dc ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00582cfc ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 005829dc bytes 493700d0
+ 00582cfc bytes 493700f0
- 005829e0 ["COPY", "tmp:0:8", ["const:868:8"]]
- 005829e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005829e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005829e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582d00 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00582d00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005829e0 bytes 29a12191
+ 00582d00 bytes 29e12091
- 00582a08 ["COPY", "register:0:8", ["register:4048:8"]]
- 00582a08 ["INT_ADD", "register:40f0:8", ["const:582a08:8", "const:4:8"]]
- 00582a08 ["CALLIND", null, ["register:0:8"]]
+ 00582d28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582d28 ["INT_ADD", "register:40f0:8", ["const:582d28:8", "const:4:8"]]
+ 00582d28 ["CALLIND", null, ["register:0:8"]]
- 00582a08 bytes 20013fd6
+ 00582d28 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660cbc23d4f92df3bb10cfa1bdeecd2f"></a>

### [`00582cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582cd0.md) → [`00582ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ff0.md) FUN_00582ff0

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
      "definition_site": "00582ff4",
      "incomplete_value": false,
      "site": "00582ff8",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582cd4",
      "incomplete_value": false,
      "site": "00582cd8",
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
            "const:8c0:8"
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
      "00582ff8",
      "DATA",
      [
        "storage",
        "00c6c8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582ff8",
      "DATA",
      [
        "storage",
        "00c6d890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582cd0.md#insn-00582cd0) · [`00582cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582cd0.md#insn-00582cd4)
- 新版 [`00582ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ff0.md#insn-00582ff0) · [`00582ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00582/00582ff0.md#insn-00582ff4)

~~~diff
- 00582cd0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 00582ff0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00582cd0 bytes 483700d0
+ 00582ff0 bytes 483700f0
- 00582cd4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00582cd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582cd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582cd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582ff4 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00582ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582cd4 bytes 08012391
+ 00582ff4 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4d68b9c5b3df7f64d0d48ad57f29ab8"></a>

### [`00582ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582ce0.md) → [`00583000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583000.md) FUN_00583000

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
      "definition_site": "00583010",
      "incomplete_value": false,
      "site": "00583018",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582cf0",
      "incomplete_value": false,
      "site": "00582cf8",
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
            "const:8c0:8"
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
      "00583018",
      "DATA",
      [
        "storage",
        "00c6c8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583018",
      "DATA",
      [
        "storage",
        "00c6d890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582ce0.md#insn-00582cec) · [`00582cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582ce0.md#insn-00582cf0) · [`00582cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582ce0.md#insn-00582cfc)
- 新版 [`0058300c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583000.md#insn-0058300c) · [`00583010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583000.md#insn-00583010) · [`0058301c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583000.md#insn-0058301c)

~~~diff
- 00582cec ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058300c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00582cec bytes 483700d0
+ 0058300c bytes 483700d0
- 00582cf0 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00582cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583010 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00583010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582cf0 bytes 08012391
+ 00583010 bytes 08412291
- 00582cfc ["INT_ADD", "register:40f0:8", ["const:582cfc:8", "const:4:8"]]
- 00582cfc ["CALL", null, ["callee:00c58f40:8"]]
+ 0058301c ["INT_ADD", "register:40f0:8", ["const:58301c:8", "const:4:8"]]
+ 0058301c ["CALL", null, ["callee:00c58f40:8"]]
- 00582cfc bytes 9d541b94
+ 0058301c bytes c9571b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c641af0e12f59118be855450358072ae"></a>

### [`00582d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md) → [`00583040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583040.md) FUN_00583040

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00581ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md) · 呼出先 4件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f60.md)
- 新版 呼出元 1件 [`00581e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00581/00581e08.md) · 呼出先 4件 [`004bcd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00583078",
      "incomplete_value": false,
      "site": "00583078",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582d58",
      "incomplete_value": false,
      "site": "00582d58",
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
            "const:910:8"
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
      "definition_site": "005830a8",
      "incomplete_value": true,
      "site": "005830a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582d88",
      "incomplete_value": true,
      "site": "00582d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:957:8"
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
      "definition_site": "00583164",
      "incomplete_value": true,
      "site": "00583164",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582e44",
      "incomplete_value": true,
      "site": "00582e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec:8"
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
      "00583078",
      "DATA",
      [
        "storage",
        "00c6c910",
        null,
        "undefined *"
      ]
    ],
    [
      "00583098",
      "READ",
      [
        "storage",
        "002a7957",
        null,
        "string"
      ]
    ],
    [
      "00583150",
      "READ",
      [
        "storage",
        "002a20ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00583078",
      "DATA",
      [
        "storage",
        "00c6d8e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00583098",
      "READ",
      [
        "storage",
        "002a7aaf",
        null,
        "string"
      ]
    ],
    [
      "00583150",
      "READ",
      [
        "storage",
        "002a21b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md#insn-00582d48) · [`00582d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md#insn-00582d4c) · [`00582d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md#insn-00582d70)
- 新版 [`00583068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583040.md#insn-00583068) · [`0058306c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583040.md#insn-0058306c) · [`00583090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583040.md#insn-00583090)

~~~diff
- 00582d48 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00583068 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00582d48 bytes 493700d0
+ 00583068 bytes 493700d0
- 00582d4c ["COPY", "tmp:0:8", ["const:910:8"]]
- 00582d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058306c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0058306c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058306c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058306c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582d4c bytes 29412491
+ 0058306c bytes 29812391
- 00582d70 ["COPY", "tmp:0:8", ["const:957:8"]]
- 00582d70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582d70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582d70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00583090 ["COPY", "tmp:0:8", ["const:aaf:8"]]
+ 00583090 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00583090 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00583090 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582d70 bytes 295d2591
+ 00583090 bytes 29bd2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9dd98069abd232129a94c0a99d83f19"></a>

### [`0058303c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058303c.md) → [`0058335c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/0058335c.md) FUN_0058335c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0058336c",
      "incomplete_value": false,
      "site": "0058336c",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058304c",
      "incomplete_value": false,
      "site": "0058304c",
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
            "const:910:8"
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
      "0058336c",
      "DATA",
      [
        "storage",
        "00c6c910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058336c",
      "DATA",
      [
        "storage",
        "00c6d8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058303c.md#insn-00583044) · [`00583048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058303c.md#insn-00583048)
- 新版 [`00583364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/0058335c.md#insn-00583364) · [`00583368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/0058335c.md#insn-00583368)

~~~diff
- 00583044 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00583364 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00583044 bytes 493700b0
+ 00583364 bytes 493700d0
- 00583048 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00583048 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00583048 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00583048 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00583368 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00583368 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00583368 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00583368 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00583048 bytes 29412491
+ 00583368 bytes 29812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b9016f158ea2504ac327d21278c572"></a>

### [`00583064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583064.md) → [`00583384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583384.md) FUN_00583384

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00583390",
      "incomplete_value": false,
      "site": "00583390",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583070",
      "incomplete_value": false,
      "site": "00583070",
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
            "const:910:8"
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
      "00583390",
      "DATA",
      [
        "storage",
        "00c6c910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583390",
      "DATA",
      [
        "storage",
        "00c6d8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583064.md#insn-00583068) · [`0058306c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583064.md#insn-0058306c) · [`00583094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583064.md#insn-00583094)
- 新版 [`00583388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583384.md#insn-00583388) · [`0058338c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583384.md#insn-0058338c) · [`005833b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583384.md#insn-005833b4)

~~~diff
- 00583068 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 00583388 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00583068 bytes 493700b0
+ 00583388 bytes 493700d0
- 0058306c ["COPY", "tmp:0:8", ["const:910:8"]]
- 0058306c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058306c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058306c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058338c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0058338c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058338c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058338c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058306c bytes 29412491
+ 0058338c bytes 29812391
- 00583094 ["COPY", "register:0:8", ["register:4048:8"]]
- 00583094 ["INT_ADD", "register:40f0:8", ["const:583094:8", "const:4:8"]]
- 00583094 ["CALLIND", null, ["register:0:8"]]
+ 005833b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005833b4 ["INT_ADD", "register:40f0:8", ["const:5833b4:8", "const:4:8"]]
+ 005833b4 ["CALLIND", null, ["register:0:8"]]
- 00583094 bytes 20013fd6
+ 005833b4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71243034b6db545ba1f0d41ecbc301c8"></a>

### [`005834f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md) → [`00583818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583818.md) FUN_00583818

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00583660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00583980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583980.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

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
      "definition_site": "00583838",
      "incomplete_value": false,
      "site": "00583838",
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
      "definition_site": "00583518",
      "incomplete_value": false,
      "site": "00583518",
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
      "00583838",
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
      "00583838",
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

- 旧版 [`0058350c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md#insn-0058350c) · [`00583510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md#insn-00583510) · [`00583554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md#insn-00583554)
- 新版 [`0058382c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583818.md#insn-0058382c) · [`00583830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583818.md#insn-00583830) · [`00583874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583818.md#insn-00583874)

~~~diff
- 0058350c ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058382c ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058350c bytes 483700b0
+ 0058382c bytes 483700d0
- 00583510 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00583510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00583510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00583510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583830 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00583830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00583510 bytes 08612691
+ 00583830 bytes 08a12591
- 00583554 ["INT_ADD", "register:40f0:8", ["const:583554:8", "const:4:8"]]
- 00583554 ["CALL", null, ["callee:0043be80:8"]]
+ 00583874 ["INT_ADD", "register:40f0:8", ["const:583874:8", "const:4:8"]]
+ 00583874 ["CALL", null, ["callee:0043be80:8"]]
- 00583554 bytes 83e1fa97
+ 00583874 bytes 83e1fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c04934a0ee415a855a1e99317b272de"></a>

### [`00583660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md) → [`00583980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583980.md) FUN_00583980

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00561d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d70.md) · 呼出先 2件 [`005834f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00562090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562090.md) · 呼出先 2件 [`00583818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583818.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005839bc",
      "incomplete_value": false,
      "site": "005839c8",
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
      "definition_site": "0058369c",
      "incomplete_value": false,
      "site": "005836a8",
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
      "005839c8",
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
      "005839c8",
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

- 旧版 [`00583690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md#insn-00583690) · [`00583698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md#insn-00583698) · [`0058369c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md#insn-0058369c)
- 新版 [`005839b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583980.md#insn-005839b0) · [`005839b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583980.md#insn-005839b8) · [`005839bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00583/00583980.md#insn-005839bc)

~~~diff
- 00583690 ["INT_ADD", "register:40f0:8", ["const:583690:8", "const:4:8"]]
- 00583690 ["CALL", null, ["callee:00c58f30:8"]]
+ 005839b0 ["INT_ADD", "register:40f0:8", ["const:5839b0:8", "const:4:8"]]
+ 005839b0 ["CALL", null, ["callee:00c58f30:8"]]
- 00583690 bytes 34521b94
+ 005839b0 bytes 60551b94
- 00583698 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 005839b8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 00583698 bytes 483700b0
+ 005839b8 bytes 483700d0
- 0058369c ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0058369c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058369c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058369c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005839bc ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 005839bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005839bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005839bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058369c bytes 08612b91
+ 005839bc bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

