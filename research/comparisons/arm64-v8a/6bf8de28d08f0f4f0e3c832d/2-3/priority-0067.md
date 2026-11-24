# v16.0.2 → v16.0.3 · 最優先の変更候補 (67)

[一覧の目次](README.md)

<a id="compare-30048a4e641627a4cb11e47e45db14ed"></a>

### [`00ac77e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac7/00ac77e4.md) → [`00ac87d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac8/00ac87d8.md) _INIT_245

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac8814",
      "incomplete_value": true,
      "site": "00ac8830",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ac7820",
      "incomplete_value": true,
      "site": "00ac783c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ac8838",
      "incomplete_value": true,
      "site": "00ac8854",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ac7844",
      "incomplete_value": true,
      "site": "00ac7860",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ac8858",
      "incomplete_value": true,
      "site": "00ac8874",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00ac7864",
      "incomplete_value": true,
      "site": "00ac7880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00ac8814",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00ac8838",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00ac8858",
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
      "00ac8814",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00ac8838",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00ac8858",
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

- 旧版 [`00ac7944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac7/00ac77e4.md#insn-00ac7944) · [`00ac7a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac7/00ac77e4.md#insn-00ac7a18) · [`00ac780c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac7/00ac77e4.md#insn-00ac780c)
- 新版 [`00ac8938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac8/00ac87d8.md#insn-00ac8938) · [`00ac8a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac8/00ac87d8.md#insn-00ac8a0c) · [`00ac8800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac8/00ac87d8.md#insn-00ac8800)

~~~diff
- 00ac7944 ["INT_ADD", "register:40f0:8", ["const:ac7944:8", "const:4:8"]]
- 00ac7944 ["CALL", null, ["callee:0043bb58:8"]]
+ 00ac8938 ["INT_ADD", "register:40f0:8", ["const:ac8938:8", "const:4:8"]]
+ 00ac8938 ["CALL", null, ["callee:0043bb58:8"]]
- 00ac7944 bytes bdcfe597
+ 00ac8938 bytes 88cce597
- 00ac7a18 ["INT_ADD", "register:40f0:8", ["const:ac7a18:8", "const:4:8"]]
- 00ac7a18 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00ac8a0c ["INT_ADD", "register:40f0:8", ["const:ac8a0c:8", "const:4:8"]]
+ 00ac8a0c ["CALL", null, ["callee:00c58ed0:8"]]
- 00ac7a18 bytes 3a410694
+ 00ac8a0c bytes 31410694
- 00ac780c ["COPY", "register:4098:8", ["const:1124000:8"]]
+ 00ac8800 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ac780c bytes f33200b0
+ 00ac8800 bytes f33200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a953b05c3626e4f0198f335dd49665d6"></a>

### [`00ac8050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8050.md) → [`00ac9044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9044.md) FUN_00ac9044

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac7bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac7/00ac7bf8.md) · 呼出先 14件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md) [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 1件 [`00ac8bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac8/00ac8bec.md) · 呼出先 14件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0046dcd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dcd4.md) [`0046dda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dda8.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.65% / 新版 99.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac9348",
      "incomplete_value": true,
      "site": "00ac934c",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_MULT",
            "8",
            [
              "INT2FLOAT",
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac8354",
      "incomplete_value": true,
      "site": "00ac8358",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_MULT",
            "8",
            [
              "INT2FLOAT",
              "LOAD"
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
      "site": "00ac9100",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac810c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00ac9100",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00ac933c",
      "READ",
      [
        "storage",
        "002c4198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ac9100",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00ac933c",
      "READ",
      [
        "storage",
        "002c41e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac810c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8050.md#insn-00ac810c) · [`00ac8088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8050.md#insn-00ac8088) · [`00ac809c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8050.md#insn-00ac809c)
- 新版 [`00ac9100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9044.md#insn-00ac9100) · [`00ac907c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9044.md#insn-00ac907c) · [`00ac9090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9044.md#insn-00ac9090)

~~~diff
- 00ac810c ["INT_ADD", "register:40f0:8", ["const:ac810c:8", "const:4:8"]]
- 00ac810c ["CALL", null, ["ram:47ad34:8"]]
+ 00ac9100 ["INT_ADD", "register:40f0:8", ["const:ac9100:8", "const:4:8"]]
+ 00ac9100 ["CALL", null, ["ram:47b054:8"]]
- 00ac810c bytes 0acbe697
+ 00ac9100 bytes d5c7e697
- 00ac8088 ["INT_ADD", "register:40f0:8", ["const:ac8088:8", "const:4:8"]]
- 00ac8088 ["CALL", null, ["callee:008524fc:8"]]
+ 00ac907c ["INT_ADD", "register:40f0:8", ["const:ac907c:8", "const:4:8"]]
+ 00ac907c ["CALL", null, ["callee:008524fc:8"]]
- 00ac8088 bytes 3225f697
+ 00ac907c bytes 2025f697
- 00ac809c ["INT_ADD", "register:40f0:8", ["const:ac809c:8", "const:4:8"]]
- 00ac809c ["CALL", null, ["callee:008524fc:8"]]
+ 00ac9090 ["INT_ADD", "register:40f0:8", ["const:ac9090:8", "const:4:8"]]
+ 00ac9090 ["CALL", null, ["callee:008524fc:8"]]
- 00ac809c bytes 2d25f697
+ 00ac9090 bytes 1b25f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70a68d6a3449da4131bcfa937e8f1494"></a>

### [`00ac88cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac88cc.md) → [`00ac98c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac98c0.md) FUN_00ac98c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0082c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) [`008c38b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c3/008c38b4.md) · 呼出先 6件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0065351c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/0065351c.md) [`00653520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653520.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00ac8a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8a18.md)
- 新版 呼出元 3件 [`0082d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082d868.md) [`0082dd1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082dd1c.md) [`008c4860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c4/008c4860.md) · 呼出先 6件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`006538cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006538cc.md) [`006538d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006538d0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00ac9a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9a0c.md)

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
      "definition_site": "00ac9938",
      "incomplete_value": false,
      "site": "00ac993c",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac8944",
      "incomplete_value": false,
      "site": "00ac8948",
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
            "const:908:8"
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
      "00ac993c",
      "DATA",
      [
        "storage",
        "00c73908",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac998c",
      "READ",
      [
        "storage",
        "00c73928",
        null,
        "pointer"
      ]
    ],
    [
      "00ac998c",
      "READ",
      [
        "storage",
        "00c73930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac993c",
      "DATA",
      [
        "storage",
        "00c748d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac998c",
      "READ",
      [
        "storage",
        "00c748f8",
        null,
        "pointer"
      ]
    ],
    [
      "00ac998c",
      "READ",
      [
        "storage",
        "00c74900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac88cc.md#insn-00ac8920) · [`00ac8924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac88cc.md#insn-00ac8924) · [`00ac8940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac88cc.md#insn-00ac8940)
- 新版 [`00ac9914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac98c0.md#insn-00ac9914) · [`00ac9918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac98c0.md#insn-00ac9918) · [`00ac9934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac98c0.md#insn-00ac9934)

~~~diff
- 00ac8920 ["INT_ADD", "register:40f0:8", ["const:ac8920:8", "const:4:8"]]
- 00ac8920 ["CALL", null, ["callee:008524fc:8"]]
+ 00ac9914 ["INT_ADD", "register:40f0:8", ["const:ac9914:8", "const:4:8"]]
+ 00ac9914 ["CALL", null, ["callee:008524fc:8"]]
- 00ac8920 bytes 0c23f697
+ 00ac9914 bytes fa22f697
- 00ac8924 ["INT_ADD", "register:40f0:8", ["const:ac8924:8", "const:4:8"]]
- 00ac8924 ["CALL", null, ["callee:0046cd24:8"]]
+ 00ac9918 ["INT_ADD", "register:40f0:8", ["const:ac9918:8", "const:4:8"]]
+ 00ac9918 ["CALL", null, ["callee:0046cd24:8"]]
- 00ac8924 bytes 3890e697
+ 00ac9918 bytes 038de697
- 00ac8940 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00ac9934 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00ac8940 bytes 480d00f0
+ 00ac9934 bytes 480d00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8f477118a6e5ecc49f7c9c7b91878ce"></a>

### [`00ac8a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8a18.md) → [`00ac9a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9a0c.md) FUN_00ac9a0c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`00643130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00643/00643130.md) [`0067e838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e838.md) [`006e4dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4dc4.md) [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`008dc988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dc/008dc988.md) · 呼出先 5件 [`00acb0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb0d8.md) [`00acb278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb278.md) [`00acb27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb27c.md) [`00acb2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb2b0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 12件 [`006434e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00643/006434e0.md) [`0067ebe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067ebe8.md) [`006e5174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e5174.md) [`0073cd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073c/0073cd40.md) [`008dd934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008dd/008dd934.md) · 呼出先 5件 [`00acc0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc0cc.md) [`00acc26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc26c.md) [`00acc270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc270.md) [`00acc2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc2a4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac9ad8",
      "incomplete_value": false,
      "site": "00ac9aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac8ae4",
      "incomplete_value": false,
      "site": "00ac8af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "definition_site": "00ac9ad8",
      "incomplete_value": false,
      "site": "00ac9af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac8ae4",
      "incomplete_value": false,
      "site": "00ac8b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "00ac9aec",
      "DATA",
      [
        "storage",
        "00c8d810",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac9af8",
      "DATA",
      [
        "storage",
        "00c8d810",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac9b24",
      "READ",
      [
        "storage",
        "00c8d830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac9aec",
      "DATA",
      [
        "storage",
        "00c8e7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac9af8",
      "DATA",
      [
        "storage",
        "00c8e7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac9b24",
      "READ",
      [
        "storage",
        "00c8e800",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8a18.md#insn-00ac8a74) · [`00ac8aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8a18.md#insn-00ac8aa0) · [`00ac8ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8a18.md#insn-00ac8ab0)
- 新版 [`00ac9a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9a0c.md#insn-00ac9a68) · [`00ac9a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9a0c.md#insn-00ac9a94) · [`00ac9aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9a0c.md#insn-00ac9aa4)

~~~diff
- 00ac8a74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ac8a74 ["INT_ADD", "register:40f0:8", ["const:ac8a74:8", "const:4:8"]]
- 00ac8a74 ["CALLIND", null, ["register:0:8"]]
+ 00ac9a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac9a68 ["INT_ADD", "register:40f0:8", ["const:ac9a68:8", "const:4:8"]]
+ 00ac9a68 ["CALLIND", null, ["register:0:8"]]
- 00ac8a74 bytes 00013fd6
+ 00ac9a68 bytes 00013fd6
- 00ac8aa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ac8aa0 ["INT_ADD", "register:40f0:8", ["const:ac8aa0:8", "const:4:8"]]
- 00ac8aa0 ["CALLIND", null, ["register:0:8"]]
+ 00ac9a94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac9a94 ["INT_ADD", "register:40f0:8", ["const:ac9a94:8", "const:4:8"]]
+ 00ac9a94 ["CALLIND", null, ["register:0:8"]]
- 00ac8aa0 bytes 00013fd6
+ 00ac9a94 bytes 00013fd6
- 00ac8ab0 ["INT_ADD", "register:40f0:8", ["const:ac8ab0:8", "const:4:8"]]
- 00ac8ab0 ["CALL", null, ["callee:00acc0cc:8"]]
+ 00ac9aa4 ["INT_ADD", "register:40f0:8", ["const:ac9aa4:8", "const:4:8"]]
+ 00ac9aa4 ["CALL", null, ["callee:00acc0cc:8"]]
- 00ac8ab0 bytes 8a090094
+ 00ac9aa4 bytes 8a090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4fc9ce647c1fbc23ed5f821a912d179"></a>

### [`00ac8e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e1c.md) → [`00ac9e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9e10.md) FUN_00ac9e10

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`00789ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789ca8.md) [`0082acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082a/0082acc0.md) [`0082cd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd70.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 0件 
- 新版 呼出元 6件 [`0078a084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078a/0078a084.md) [`0082bc6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082b/0082bc6c.md) [`0082dd1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082d/0082dd1c.md) [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`00a76e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a76/00a76e10.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac8e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e1c.md#insn-00ac8e20) · [`00ac8e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e1c.md#insn-00ac8e28)
- 新版 [`00ac9e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9e10.md#insn-00ac9e14) · [`00ac9e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9e10.md#insn-00ac9e1c)

~~~diff
- 00ac8e20 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00ac8e20 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00ac9e14 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00ac9e14 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ac8e20 bytes 28010034
+ 00ac9e14 bytes 28010034
- 00ac8e28 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00ac8e28 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00ac9e1c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00ac9e1c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ac8e28 bytes e8000034
+ 00ac9e1c bytes e8000034
~~~


<a id="compare-ed6afae7413f5c50b4838845d2dbeeeb"></a>

### [`00ac8ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8ecc.md) → [`00ac9ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9ec0.md) FUN_00ac9ec0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00657fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md) [`0068aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aae0.md) [`006d3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d3/006d3e94.md) [`007001b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007001b0.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 6件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md) [`0085b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b2fc.md) [`0085b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b304.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md)
- 新版 呼出元 8件 [`0065837c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/0065837c.md) [`0068ae90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068ae90.md) [`006d4244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d4/006d4244.md) [`00700560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700560.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 6件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085ab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab50.md) [`0085c2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2a8.md) [`0085c2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2b0.md) [`0085c2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2e4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.60% / 新版 72.60%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8ed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8ed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8ed8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac8ed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac8ed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac8edc",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ac9ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ac9ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00ac9ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8ecc.md#insn-00ac8ed4) · [`00ac8ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8ecc.md#insn-00ac8ed8) · [`00ac8edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8ecc.md#insn-00ac8edc)

~~~diff
- 00ac8ed4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ac8ed4 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00ac8ed4 bytes e80f1dfc
- 00ac8ed8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac8ed8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac8ed8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 00ac8ed8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac8ed8 bytes fdfb00a9
- 00ac8edc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00ac8edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00ac8edc bytes f50f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414c561d708e3ec869874011a30673cc"></a>

### [`00ac9134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9134.md) → [`00aca128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca128.md) FUN_00aca128

採用 · 移動量 `+0xff4` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 8件 [`00657fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md) [`0068aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068aae0.md) [`006d3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d3/006d3e94.md) [`007001b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/007001b0.md) [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 0件 
- 新版 呼出元 8件 [`0065837c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/0065837c.md) [`0068ae90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068a/0068ae90.md) [`006d4244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d4/006d4244.md) [`00700560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700560.md) [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-54d49ee7aaf78600854fed9b0109b30b"></a>

### [`00ac9150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9150.md) → [`00aca144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca144.md) FUN_00aca144

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`0065cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md) [`0065d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md) [`0068be68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068b/0068be68.md) [`006d4dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4dec.md) [`0070059c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070059c.md) · 呼出先 4件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`00ac8ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8ff0.md)
- 新版 呼出元 9件 [`0065d0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065d/0065d0bc.md) [`0065da20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065d/0065da20.md) [`0068c218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0068c/0068c218.md) [`006d519c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d519c.md) [`0070094c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/0070094c.md) · 呼出先 4件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`00ac9fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac9/00ac9fe4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.62% / 新版 73.62%

CFGの説明率　旧版 5.41% / 新版 5.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9164"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac9160",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9164",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9168",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aca154",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aca158",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aca15c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9150.md#insn-00ac9160) · [`00ac9164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9150.md#insn-00ac9164) · [`00ac9168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9150.md#insn-00ac9168)

~~~diff
- 00ac9160 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ac9160 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ac9160 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ac9160 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9160 bytes f85f04a9
- 00ac9164 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ac9164 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ac9164 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ac9164 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9164 bytes f65705a9
- 00ac9168 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ac9168 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ac9168 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ac9168 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9168 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1db7f17304aa13617a18c7be7c427750"></a>

### [`00ac93dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac93dc.md) → [`00aca3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca3d0.md) FUN_00aca3d0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0098546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/0098546c.md) · 呼出先 2件 [`00acb2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb2b0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00986418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00986/00986418.md) · 呼出先 2件 [`00acc2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc2a4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 82.35% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ac9400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac93dc.md#insn-00ac9400) · [`00ac9408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac93dc.md#insn-00ac9408) · [`00ac9418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac93dc.md#insn-00ac9418)
- 新版 [`00aca3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca3d0.md#insn-00aca3f4) · [`00aca3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca3d0.md#insn-00aca3fc) · [`00aca40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca3d0.md#insn-00aca40c)

~~~diff
- 00ac9400 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ac9400 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00aca3f4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aca3f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ac9400 bytes 280100b4
+ 00aca3f4 bytes 280100b4
- 00ac9408 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00aca3fc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00ac9408 bytes 20010054
+ 00aca3fc bytes 20010054
- 00ac9418 ["COPY", "register:0:8", ["register:4048:8"]]
- 00ac9418 ["INT_ADD", "register:40f0:8", ["const:ac9418:8", "const:4:8"]]
- 00ac9418 ["CALLIND", null, ["register:0:8"]]
+ 00aca40c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00aca40c ["INT_ADD", "register:40f0:8", ["const:aca40c:8", "const:4:8"]]
+ 00aca40c ["CALLIND", null, ["register:0:8"]]
- 00ac9418 bytes 20013fd6
+ 00aca40c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9c6c78c63a68cf5b3f914d0751a8ef"></a>

### [`00ac9604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9604.md) → [`00aca5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca5f8.md) FUN_00aca5f8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`0078df90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078df90.md) [`0078e2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e2d8.md) [`0082f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082f180.md) [`008c2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md) [`008fd554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd554.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 12件 [`0078e36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e36c.md) [`0078e6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e6b4.md) [`0083012c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00830/0083012c.md) [`008c38c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c38c0.md) [`008fe500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fe/008fe500.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 53.85% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac963c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ac96d4",
      "incomplete_value": true,
      "site": "00ac96d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:2f38:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ac96cc",
      "incomplete_value": true,
      "site": "00ac96d8",
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
      "unmatched:00ac963c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ],
  "added": [
    [
      "00aca630",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac963c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9604.md#insn-00ac963c) · [`00ac96d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9604.md#insn-00ac96d8)
- 新版 [`00aca6cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca5f8.md#insn-00aca6cc) · [`00aca630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca5f8.md#insn-00aca630)

~~~diff
- 00ac963c ["INT_ADD", "register:40f0:8", ["const:ac963c:8", "const:4:8"]]
- 00ac963c ["CALL", null, ["callee:008b89cc:8"]]
- 00ac963c bytes f9b8f797
- 00ac96d8 ["INT_ADD", "register:40f0:8", ["const:ac96d8:8", "const:4:8"]]
- 00ac96d8 ["CALL", null, ["callee:008b89cc:8"]]
+ 00aca6cc ["INT_ADD", "register:40f0:8", ["const:aca6cc:8", "const:4:8"]]
+ 00aca6cc ["CALL", null, ["callee:008b89cc:8"]]
- 00ac96d8 bytes d2b8f797
+ 00aca6cc bytes c0b8f797
+ 00aca630 ["INT_ADD", "register:40f0:8", ["const:aca630:8", "const:4:8"]]
+ 00aca630 ["CALL", null, ["callee:008b89cc:8"]]
+ 00aca630 bytes e7b8f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad2ae2acf2a4dc4d930fe247674a66b4"></a>

### [`00ac96f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac96f8.md) → [`00aca6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca6ec.md) FUN_00aca6ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00838acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838acc.md) [`008bf8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf8ac.md) [`008d2af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2af8.md) [`008d8760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8760.md) [`008d9c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c58.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 9件 [`00839a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00839/00839a78.md) [`008c0858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c0/008c0858.md) [`008d3aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d3/008d3aa4.md) [`008d970c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d970c.md) [`008dac04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008dac04.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.25% / 新版 85.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac96f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac96f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac96fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac96f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac96fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9730",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ],
  "added": [
    [
      "00aca6ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aca6f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aca724",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac96f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac96f8.md#insn-00ac96f8) · [`00ac96fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac96f8.md#insn-00ac96fc) · [`00ac9730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac96f8.md#insn-00ac9730)

~~~diff
- 00ac96f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac96f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac96f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ac96f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ac96f8 bytes fd7bbea9
- 00ac96fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ac96fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ac96fc bytes f30b00f9
- 00ac9730 ["INT_ADD", "register:40f0:8", ["const:ac9730:8", "const:4:8"]]
- 00ac9730 ["CALL", null, ["callee:008b89cc:8"]]
- 00ac9730 bytes bcb8f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98e682053e16e78d03c55ed5cc4df189"></a>

### [`00ac97ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac97ec.md) → [`00aca7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca7e0.md) FUN_00aca7e0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`006460c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006460c0.md) [`00680e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00680/00680e48.md) [`006e79e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md) [`0073ee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073e/0073ee8c.md) [`008dda58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008dda58.md) · 呼出先 6件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md)
- 新版 呼出元 10件 [`00646470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/00646470.md) [`006811f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00681/006811f8.md) [`006e7d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md) [`0073f23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073f/0073f23c.md) [`008dea04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008dea04.md) · 呼出先 6件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`004699bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004699bc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 15.09% / 新版 13.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aca814"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9af0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac9820",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aca830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ac9ae4"
      ]
    ],
    [
      "00aca8b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ac9ae4"
      ]
    ]
  ],
  "added": [
    [
      "00aca814",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aca830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00acaad8"
      ]
    ],
    [
      "00aca8b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00acaad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac97ec.md#insn-00ac9820) · [`00ac989c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac97ec.md#insn-00ac989c) · [`00ac9964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac97ec.md#insn-00ac9964)
- 新版 [`00aca890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca7e0.md#insn-00aca890) · [`00aca958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca7e0.md#insn-00aca958)

~~~diff
- 00ac9820 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00ac9820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac9820 bytes e80f00f9
- 00ac989c ["INT_ADD", "register:40f0:8", ["const:ac989c:8", "const:4:8"]]
- 00ac989c ["CALL", null, ["callee:004692e8:8"]]
+ 00aca890 ["INT_ADD", "register:40f0:8", ["const:aca890:8", "const:4:8"]]
+ 00aca890 ["CALL", null, ["callee:004692e8:8"]]
- 00ac989c bytes cb7de697
+ 00aca890 bytes 967ae697
- 00ac9964 ["INT_ADD", "register:40f0:8", ["const:ac9964:8", "const:4:8"]]
- 00ac9964 ["CALL", null, ["callee:00467ec0:8"]]
+ 00aca958 ["INT_ADD", "register:40f0:8", ["const:aca958:8", "const:4:8"]]
+ 00aca958 ["CALL", null, ["callee:00467ec0:8"]]
- 00ac9964 bytes 8f78e697
+ 00aca958 bytes 5a75e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6da977060a1fac33f73058fe656bdde5"></a>

### [`00ac9b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b2c.md) → [`00acab20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acab20.md) FUN_00acab20

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 5件 [`00788d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788d04.md) [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) [`008fea38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fea38.md) [`00a3deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3deac.md) [`00ac04c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac0/00ac04c4.md) · 呼出先 0件 
- 新版 呼出元 5件 [`007890e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00789/007890e0.md) [`0082fe24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fe24.md) [`008ff9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ff/008ff9e4.md) [`00a3eea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3e/00a3eea0.md) [`00ac14b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ac1/00ac14b8.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-db6f17e35a7621870bc2909a064c0f19"></a>

### [`00ac9b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b44.md) → [`00acab38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acab38.md) FUN_00acab38

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`008cac14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008cac14.md) [`00a735a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a73/00a735a0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`008cbbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cb/008cbbc0.md) [`00a74594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a74/00a74594.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-c47f1e7b9683f0126c1562bbee20b2e3"></a>

### [`00ac9b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b5c.md) → [`00acab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acab50.md) FUN_00acab50

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00788d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788d04.md) [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) [`008cac14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008cac14.md) [`008d1c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1c94.md) [`008fea38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fea38.md) · 呼出先 17件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b6f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f88.md)
- 新版 呼出元 7件 [`007890e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00789/007890e0.md) [`0082fe24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fe24.md) [`008cbbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cb/008cbbc0.md) [`008d2c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d2/008d2c40.md) [`008ff9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ff/008ff9e4.md) · 呼出先 17件 [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b7f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f34.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 75.00% / 新版 87.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9b64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac9b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9b64",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9b68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00acab54",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00acab58",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00acab5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b5c.md#insn-00ac9b60) · [`00ac9b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b5c.md#insn-00ac9b64) · [`00ac9b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b5c.md#insn-00ac9b68)

~~~diff
- 00ac9b60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac9b60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac9b60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00ac9b60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9b60 bytes fd7b08a9
- 00ac9b64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00ac9b64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00ac9b64 bytes f94b00f9
- 00ac9b68 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ac9b68 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ac9b68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00ac9b68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9b68 bytes f85f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-179134abf8b4245bde1709ccba9618ed"></a>

### [`00ac9fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9fd0.md) → [`00acafc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acafc4.md) FUN_00acafc4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00788d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788d04.md) [`0082ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) [`008cac14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008cac14.md) [`008fea38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fea38.md) [`00a3deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3deac.md) · 呼出先 15件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md)
- 新版 呼出元 6件 [`007890e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00789/007890e0.md) [`0082fe24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082f/0082fe24.md) [`008cbbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cb/008cbbc0.md) [`008ff9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ff/008ff9e4.md) [`00a3eea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3e/00a3eea0.md) · 呼出先 15件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00acb134",
      "incomplete_value": false,
      "site": "00acb148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aca140",
      "incomplete_value": false,
      "site": "00aca154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:910:8"
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
      "00acb09c",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00acb0b0",
      "DATA",
      [
        "storage",
        "00c8b828",
        null,
        "undefined *"
      ]
    ],
    [
      "00acb0c8",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00acb09c",
      "READ",
      [
        "storage",
        "00c9c408",
        null,
        "pointer"
      ]
    ],
    [
      "00acb0b0",
      "DATA",
      [
        "storage",
        "00c8c7f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00acb0c8",
      "READ",
      [
        "storage",
        "00c9c410",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9fd0.md#insn-00aca008) · [`00aca00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9fd0.md#insn-00aca00c) · [`00aca01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9fd0.md#insn-00aca01c)
- 新版 [`00acaffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acafc4.md#insn-00acaffc) · [`00acb000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acafc4.md#insn-00acb000) · [`00acb010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00acafc4.md#insn-00acb010)

~~~diff
- 00aca008 ["INT_ADD", "register:40f0:8", ["const:aca008:8", "const:4:8"]]
- 00aca008 ["CALL", null, ["callee:008524fc:8"]]
+ 00acaffc ["INT_ADD", "register:40f0:8", ["const:acaffc:8", "const:4:8"]]
+ 00acaffc ["CALL", null, ["callee:008524fc:8"]]
- 00aca008 bytes 521df697
+ 00acaffc bytes 401df697
- 00aca00c ["INT_ADD", "register:40f0:8", ["const:aca00c:8", "const:4:8"]]
- 00aca00c ["CALL", null, ["callee:0046cd24:8"]]
+ 00acb000 ["INT_ADD", "register:40f0:8", ["const:acb000:8", "const:4:8"]]
+ 00acb000 ["CALL", null, ["callee:0046cd24:8"]]
- 00aca00c bytes 7e8ae697
+ 00acb000 bytes 4987e697
- 00aca01c ["INT_ADD", "register:40f0:8", ["const:aca01c:8", "const:4:8"]]
- 00aca01c ["CALL", null, ["callee:0048a2ac:8"]]
+ 00acb010 ["INT_ADD", "register:40f0:8", ["const:acb010:8", "const:4:8"]]
+ 00acb010 ["CALL", null, ["callee:0048a2ac:8"]]
- 00aca01c bytes dcffe697
+ 00acb010 bytes a7fce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4af1b3e4fae39485596320ab67be7fce"></a>

### [`00acb244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb244.md) → [`00acc238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc238.md) FUN_00acc238

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acc24c",
      "incomplete_value": false,
      "site": "00acc250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb258",
      "incomplete_value": false,
      "site": "00acb25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "00acc250",
      "DATA",
      [
        "storage",
        "00c8d810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acc250",
      "DATA",
      [
        "storage",
        "00c8e7e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb244.md#insn-00acb250) · [`00acb254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb244.md#insn-00acb254) · [`00acb258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb244.md#insn-00acb258)
- 新版 [`00acc244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc238.md#insn-00acc244) · [`00acc248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc238.md#insn-00acc248) · [`00acc24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc238.md#insn-00acc24c)

~~~diff
- 00acb250 ["INT_ADD", "register:40f0:8", ["const:acb250:8", "const:4:8"]]
- 00acb250 ["CALL", null, ["callee:00c58f30:8"]]
+ 00acc244 ["INT_ADD", "register:40f0:8", ["const:acc244:8", "const:4:8"]]
+ 00acc244 ["CALL", null, ["callee:00c58f30:8"]]
- 00acb250 bytes 44330694
+ 00acc244 bytes 3b330694
- 00acb254 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00acc248 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acb254 bytes 080e00d0
+ 00acc248 bytes 080e00d0
- 00acb258 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00acb258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acc24c ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00acc24c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc24c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc24c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb258 bytes 08412091
+ 00acc24c bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9392d75272a8851056c77f466feffc1"></a>

### [`00acb268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb268.md) → [`00acc25c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc25c.md) FUN_00acc25c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acc260",
      "incomplete_value": false,
      "site": "00acc264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb26c",
      "incomplete_value": false,
      "site": "00acb270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "00acc264",
      "DATA",
      [
        "storage",
        "00c8d810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acc264",
      "DATA",
      [
        "storage",
        "00c8e7e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb268.md#insn-00acb268) · [`00acb26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb268.md#insn-00acb26c)
- 新版 [`00acc25c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc25c.md#insn-00acc25c) · [`00acc260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc25c.md#insn-00acc260)

~~~diff
- 00acb268 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00acc25c ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acb268 bytes 080e00d0
+ 00acc25c bytes 080e00d0
- 00acb26c ["COPY", "tmp:0:8", ["const:810:8"]]
- 00acb26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acc260 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00acc260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb26c bytes 08412091
+ 00acc260 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08506e16bc2d68730f31e51ea3ce4239"></a>

### [`00acb41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb41c.md) → [`00acc410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc410.md) FUN_00acc410

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acc424",
      "incomplete_value": false,
      "site": "00acc428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb430",
      "incomplete_value": false,
      "site": "00acb434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "00acc428",
      "DATA",
      [
        "storage",
        "00c8d890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acc428",
      "DATA",
      [
        "storage",
        "00c8e860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb41c.md#insn-00acb428) · [`00acb42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb41c.md#insn-00acb42c) · [`00acb430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb41c.md#insn-00acb430)
- 新版 [`00acc41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc410.md#insn-00acc41c) · [`00acc420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc410.md#insn-00acc420) · [`00acc424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc410.md#insn-00acc424)

~~~diff
- 00acb428 ["INT_ADD", "register:40f0:8", ["const:acb428:8", "const:4:8"]]
- 00acb428 ["CALL", null, ["callee:00c58f30:8"]]
+ 00acc41c ["INT_ADD", "register:40f0:8", ["const:acc41c:8", "const:4:8"]]
+ 00acc41c ["CALL", null, ["callee:00c58f30:8"]]
- 00acb428 bytes ce320694
+ 00acc41c bytes c5320694
- 00acb42c ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00acc420 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acb42c bytes 080e00d0
+ 00acc420 bytes 080e00d0
- 00acb430 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00acb430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acc424 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00acc424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb430 bytes 08412291
+ 00acc424 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a63fdb9bb788bda81df7674bf8281b2"></a>

### [`00acb440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb440.md) → [`00acc434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc434.md) FUN_00acc434

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acc438",
      "incomplete_value": false,
      "site": "00acc43c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb444",
      "incomplete_value": false,
      "site": "00acb448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "00acc43c",
      "DATA",
      [
        "storage",
        "00c8d890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acc43c",
      "DATA",
      [
        "storage",
        "00c8e860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb440.md#insn-00acb440) · [`00acb444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb440.md#insn-00acb444)
- 新版 [`00acc434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc434.md#insn-00acc434) · [`00acc438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc434.md#insn-00acc438)

~~~diff
- 00acb440 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00acc434 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acb440 bytes 080e00d0
+ 00acc434 bytes 080e00d0
- 00acb444 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00acb444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acc438 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00acc438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb444 bytes 08412291
+ 00acc438 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d00174c78092627862d87d6a0fdd15"></a>

### [`00acb458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb458.md) → [`00acc44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc44c.md) FUN_00acc44c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

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
      "site": "00acc4ec",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb4f8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acc4f8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb504",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00acc4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00acc4f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00acc4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00acc4f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb458.md#insn-00acb4f8) · [`00acb504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb458.md#insn-00acb504) · [`00acb470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb458.md#insn-00acb470)
- 新版 [`00acc4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc44c.md#insn-00acc4ec) · [`00acc4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc44c.md#insn-00acc4f8) · [`00acc464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc44c.md#insn-00acc464)

~~~diff
- 00acb4f8 ["INT_ADD", "register:40f0:8", ["const:acb4f8:8", "const:4:8"]]
- 00acb4f8 ["CALL", null, ["ram:47ad34:8"]]
+ 00acc4ec ["INT_ADD", "register:40f0:8", ["const:acc4ec:8", "const:4:8"]]
+ 00acc4ec ["CALL", null, ["ram:47b054:8"]]
- 00acb4f8 bytes 0fbee697
+ 00acc4ec bytes dabae697
- 00acb504 ["INT_ADD", "register:40f0:8", ["const:acb504:8", "const:4:8"]]
- 00acb504 ["CALL", null, ["ram:47ad34:8"]]
+ 00acc4f8 ["INT_ADD", "register:40f0:8", ["const:acc4f8:8", "const:4:8"]]
+ 00acc4f8 ["CALL", null, ["ram:47b054:8"]]
- 00acb504 bytes 0cbee697
+ 00acc4f8 bytes d7bae697
- 00acb470 ["INT_ADD", "register:40f0:8", ["const:acb470:8", "const:4:8"]]
- 00acb470 ["CALL", null, ["callee:008b7ea8:8"]]
+ 00acc464 ["INT_ADD", "register:40f0:8", ["const:acc464:8", "const:4:8"]]
+ 00acc464 ["CALL", null, ["callee:008b7ea8:8"]]
- 00acb470 bytes a3aef797
+ 00acc464 bytes 91aef797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb2f22932569fef31736b7db839ef2a"></a>

### [`00acb580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb580.md) → [`00acc574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc574.md) FUN_00acc574

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acc588",
      "incomplete_value": false,
      "site": "00acc58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb594",
      "incomplete_value": false,
      "site": "00acb598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:910:8"
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
      "00acc58c",
      "DATA",
      [
        "storage",
        "00c8d910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acc58c",
      "DATA",
      [
        "storage",
        "00c8e8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb580.md#insn-00acb58c) · [`00acb590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb580.md#insn-00acb590) · [`00acb594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb580.md#insn-00acb594)
- 新版 [`00acc580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc574.md#insn-00acc580) · [`00acc584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc574.md#insn-00acc584) · [`00acc588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc574.md#insn-00acc588)

~~~diff
- 00acb58c ["INT_ADD", "register:40f0:8", ["const:acb58c:8", "const:4:8"]]
- 00acb58c ["CALL", null, ["callee:00c58f30:8"]]
+ 00acc580 ["INT_ADD", "register:40f0:8", ["const:acc580:8", "const:4:8"]]
+ 00acc580 ["CALL", null, ["callee:00c58f30:8"]]
- 00acb58c bytes 75320694
+ 00acc580 bytes 6c320694
- 00acb590 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00acc584 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acb590 bytes 080e00d0
+ 00acc584 bytes 080e00d0
- 00acb594 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00acb594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acc588 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00acc588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb594 bytes 08412491
+ 00acc588 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35aa12d8f70d66ae955293cb1484e8a5"></a>

### [`00acb5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5a4.md) → [`00acc598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc598.md) FUN_00acc598

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acc59c",
      "incomplete_value": false,
      "site": "00acc5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb5a8",
      "incomplete_value": false,
      "site": "00acb5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
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
      "00acc5a0",
      "DATA",
      [
        "storage",
        "00c8d910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acc5a0",
      "DATA",
      [
        "storage",
        "00c8e8e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5a4.md#insn-00acb5a4) · [`00acb5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5a4.md#insn-00acb5a8)
- 新版 [`00acc598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc598.md#insn-00acc598) · [`00acc59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc598.md#insn-00acc59c)

~~~diff
- 00acb5a4 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00acc598 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acb5a4 bytes 080e00d0
+ 00acc598 bytes 080e00d0
- 00acb5a8 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00acb5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acc59c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00acc59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acc59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb5a8 bytes 08412491
+ 00acc59c bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b20d18dbf84886bea94d7ef8c72043e0"></a>

### [`00acb5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5bc.md) → [`00acc5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc5b0.md) FUN_00acc5b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047d1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d1fc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0047d51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d51c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acc5d4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb5e0",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00acc5e0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb5ec",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00acc6d0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb6dc",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00acc5d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00acc5e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00acc6d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00acc5d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00acc5e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00acc6d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5bc.md#insn-00acb5e0) · [`00acb5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5bc.md#insn-00acb5ec) · [`00acb6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb5bc.md#insn-00acb6dc)
- 新版 [`00acc5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc5b0.md#insn-00acc5d4) · [`00acc5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc5b0.md#insn-00acc5e0) · [`00acc6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc5b0.md#insn-00acc6d0)

~~~diff
- 00acb5e0 ["INT_ADD", "register:40f0:8", ["const:acb5e0:8", "const:4:8"]]
- 00acb5e0 ["CALL", null, ["ram:47ad34:8"]]
+ 00acc5d4 ["INT_ADD", "register:40f0:8", ["const:acc5d4:8", "const:4:8"]]
+ 00acc5d4 ["CALL", null, ["ram:47b054:8"]]
- 00acb5e0 bytes d5bde697
+ 00acc5d4 bytes a0bae697
- 00acb5ec ["INT_ADD", "register:40f0:8", ["const:acb5ec:8", "const:4:8"]]
- 00acb5ec ["CALL", null, ["ram:47ad34:8"]]
+ 00acc5e0 ["INT_ADD", "register:40f0:8", ["const:acc5e0:8", "const:4:8"]]
+ 00acc5e0 ["CALL", null, ["ram:47b054:8"]]
- 00acb5ec bytes d2bde697
+ 00acc5e0 bytes 9dbae697
- 00acb6dc ["INT_ADD", "register:40f0:8", ["const:acb6dc:8", "const:4:8"]]
- 00acb6dc ["CALL", null, ["ram:47ad34:8"]]
+ 00acc6d0 ["INT_ADD", "register:40f0:8", ["const:acc6d0:8", "const:4:8"]]
+ 00acc6d0 ["CALL", null, ["ram:47b054:8"]]
- 00acb6dc bytes 96bde697
+ 00acc6d0 bytes 61bae697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12e86e2d6685df5b472befd0cf970add"></a>

### [`00acb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb738.md) → [`00acc72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc72c.md) _INIT_246

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acc768",
      "incomplete_value": true,
      "site": "00acc784",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb774",
      "incomplete_value": true,
      "site": "00acb790",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acc78c",
      "incomplete_value": true,
      "site": "00acc7a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb798",
      "incomplete_value": true,
      "site": "00acb7b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acc7ac",
      "incomplete_value": true,
      "site": "00acc7c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00acb7b8",
      "incomplete_value": true,
      "site": "00acb7d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00acc768",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00acc78c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00acc7ac",
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
      "00acc768",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00acc78c",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00acc7ac",
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

- 旧版 [`00acb898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb738.md#insn-00acb898) · [`00acb96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb738.md#insn-00acb96c) · [`00acb760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb738.md#insn-00acb760)
- 新版 [`00acc88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc72c.md#insn-00acc88c) · [`00acc960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc72c.md#insn-00acc960) · [`00acc754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00acc72c.md#insn-00acc754)

~~~diff
- 00acb898 ["INT_ADD", "register:40f0:8", ["const:acb898:8", "const:4:8"]]
- 00acb898 ["CALL", null, ["callee:0043bb58:8"]]
+ 00acc88c ["INT_ADD", "register:40f0:8", ["const:acc88c:8", "const:4:8"]]
+ 00acc88c ["CALL", null, ["callee:0043bb58:8"]]
- 00acb898 bytes e8bfe597
+ 00acc88c bytes b3bce597
- 00acb96c ["INT_ADD", "register:40f0:8", ["const:acb96c:8", "const:4:8"]]
- 00acb96c ["CALL", null, ["callee:00c58ed0:8"]]
+ 00acc960 ["INT_ADD", "register:40f0:8", ["const:acc960:8", "const:4:8"]]
+ 00acc960 ["CALL", null, ["callee:00c58ed0:8"]]
- 00acb96c bytes 65310694
+ 00acc960 bytes 5c310694
- 00acb760 ["COPY", "register:4098:8", ["const:1124000:8"]]
+ 00acc754 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00acb760 bytes d33200b0
+ 00acc754 bytes d33200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b90ad4d51af0ebcc9bcd9c9acdf6d490"></a>

### [`00acbac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbac8.md) → [`00accabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accabc.md) FUN_00accabc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00731f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731f1c.md) [`009355f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/009355f0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`007322cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00732/007322cc.md) [`0093659c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00936/0093659c.md) · 呼出先 0件 

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
      "definition_site": "00accac4",
      "incomplete_value": false,
      "site": "00accac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbad0",
      "incomplete_value": false,
      "site": "00acbad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "00accac8",
      "DATA",
      [
        "storage",
        "00c8d990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00accac8",
      "DATA",
      [
        "storage",
        "00c8e960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acbacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbac8.md#insn-00acbacc) · [`00acbad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbac8.md#insn-00acbad0)
- 新版 [`00accac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accabc.md#insn-00accac0) · [`00accac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accabc.md#insn-00accac4)

~~~diff
- 00acbacc ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00accac0 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acbacc bytes 080e00d0
+ 00accac0 bytes 080e00d0
- 00acbad0 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00acbad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acbad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acbad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00accac4 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00accac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00accac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00accac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acbad0 bytes 08412691
+ 00accac4 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fe077051b4208b35b07a2a3bcb74a1d"></a>

### [`00acbaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbaf8.md) → [`00accaec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accaec.md) FUN_00accaec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00731fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/00731fc4.md) [`00732020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732020.md) [`009359a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/009359a4.md) [`00935a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935a30.md) [`00acc088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc088.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 6件 [`00732374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00732/00732374.md) [`007323d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00732/007323d0.md) [`00936950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00936/00936950.md) [`009369dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00936/009369dc.md) [`00acd07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd07c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00accb08",
      "incomplete_value": false,
      "site": "00accb0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbb14",
      "incomplete_value": false,
      "site": "00acbb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "00accb0c",
      "DATA",
      [
        "storage",
        "00c8d990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00accb0c",
      "DATA",
      [
        "storage",
        "00c8e960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acbb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbaf8.md#insn-00acbb10) · [`00acbb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbaf8.md#insn-00acbb14) · [`00acbb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbaf8.md#insn-00acbb50)
- 新版 [`00accb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accaec.md#insn-00accb04) · [`00accb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accaec.md#insn-00accb08) · [`00accb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accaec.md#insn-00accb44)

~~~diff
- 00acbb10 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00accb04 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acbb10 bytes 080e00d0
+ 00accb04 bytes 080e00d0
- 00acbb14 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00acbb14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acbb14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acbb14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00accb08 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00accb08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00accb08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00accb08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acbb14 bytes 08412691
+ 00accb08 bytes 08812591
- 00acbb50 ["INT_ADD", "register:40f0:8", ["const:acbb50:8", "const:4:8"]]
- 00acbb50 ["CALL", null, ["callee:00c54d90:8"]]
+ 00accb44 ["INT_ADD", "register:40f0:8", ["const:accb44:8", "const:4:8"]]
+ 00accb44 ["CALL", null, ["callee:00c54d90:8"]]
- 00acbb50 bytes 94200694
+ 00accb44 bytes 93200694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548099bb1380129798ae0dd8e9896dc3"></a>

### [`00acbdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md) → [`00accdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accdb0.md) FUN_00accdb0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00935704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00935/00935704.md) · 呼出先 7件 [`00acc0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc0e8.md) [`00acc140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc140.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`009366b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00936/009366b0.md) · 呼出先 7件 [`00acd0dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd0dc.md) [`00acd134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd134.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00accdf8",
      "incomplete_value": false,
      "site": "00acce00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbe04",
      "incomplete_value": false,
      "site": "00acbe0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00acce00",
      "DATA",
      [
        "storage",
        "00c8d9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00acce64",
      "READ",
      [
        "storage",
        "00c8d9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acce00",
      "DATA",
      [
        "storage",
        "00c8e990",
        null,
        "pointer"
      ]
    ],
    [
      "00acce64",
      "READ",
      [
        "storage",
        "00c8e9a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acbdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md#insn-00acbdf8) · [`00acbe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md#insn-00acbe00) · [`00acbe04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md#insn-00acbe04)
- 新版 [`00accdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accdb0.md#insn-00accdec) · [`00accdf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accdb0.md#insn-00accdf4) · [`00accdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accdb0.md#insn-00accdf8)

~~~diff
- 00acbdf8 ["INT_ADD", "register:40f0:8", ["const:acbdf8:8", "const:4:8"]]
- 00acbdf8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00accdec ["INT_ADD", "register:40f0:8", ["const:accdec:8", "const:4:8"]]
+ 00accdec ["CALL", null, ["callee:00c58f30:8"]]
- 00acbdf8 bytes 5a300694
+ 00accdec bytes 51300694
- 00acbe00 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00accdf4 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00acbe00 bytes 080e00d0
+ 00accdf4 bytes 080e00d0
- 00acbe04 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00acbe04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acbe04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acbe04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00accdf8 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00accdf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00accdf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00accdf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acbe04 bytes 08012791
+ 00accdf8 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7457b559a9d121ed5fbc86da88954595"></a>

### [`00acc140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc140.md) → [`00acd134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd134.md) FUN_00acd134

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00acbdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00acc29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc29c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00accdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accdb0.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00acd290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd290.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 93.10% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00acc274",
      "incomplete_value": true,
      "site": "00acc28c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00acc170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc140.md#insn-00acc170) · [`00acc1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc140.md#insn-00acc1a4) · [`00acc1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc140.md#insn-00acc1ac)
- 新版 [`00acd164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd134.md#insn-00acd164) · [`00acd198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd134.md#insn-00acd198) · [`00acd1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd134.md#insn-00acd1a0)

~~~diff
- 00acc170 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00acc170 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00acd164 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00acd164 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00acc170 bytes 090900b5
+ 00acd164 bytes 090900b5
- 00acc1a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00acc1a4 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
+ 00acd198 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00acd198 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00acc1a4 bytes a80700b5
+ 00acd198 bytes a80700b5
- 00acc1ac ["INT_ADD", "register:40f0:8", ["const:acc1ac:8", "const:4:8"]]
- 00acc1ac ["CALL", null, ["callee:00c58f30:8"]]
+ 00acd1a0 ["INT_ADD", "register:40f0:8", ["const:acd1a0:8", "const:4:8"]]
+ 00acd1a0 ["CALL", null, ["callee:00c58f30:8"]]
- 00acc1ac bytes 6d2f0694
+ 00acd1a0 bytes 642f0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1898695e26d0c248603f796ad547960"></a>

### [`00acc29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc29c.md) → [`00acd290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd290.md) FUN_00acd290

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00acc140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc140.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00acd134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd134.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00acd29c",
      "incomplete_value": false,
      "site": "00acd2a0",
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
      "definition_site": "00acc2a8",
      "incomplete_value": false,
      "site": "00acc2ac",
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
      "00acd29c",
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
      "00acd29c",
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

- 旧版 [`00acc2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc29c.md#insn-00acc2ac) · [`00acc2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc29c.md#insn-00acc2a4) · [`00acc2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc29c.md#insn-00acc2a8)
- 新版 [`00acd2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd290.md#insn-00acd2a0) · [`00acd298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd290.md#insn-00acd298) · [`00acd29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd290.md#insn-00acd29c)

~~~diff
- 00acc2ac ["INT_ADD", "register:40f0:8", ["const:acc2ac:8", "const:4:8"]]
- 00acc2ac ["CALL", null, ["callee:0043bad8:8"]]
+ 00acd2a0 ["INT_ADD", "register:40f0:8", ["const:acd2a0:8", "const:4:8"]]
+ 00acd2a0 ["CALL", null, ["callee:0043bad8:8"]]
- 00acc2ac bytes 43bde597
+ 00acd2a0 bytes 0ebae597
- 00acc2a4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00acd298 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00acc2a4 bytes 40bffff0
+ 00acd298 bytes 40bffff0
- 00acc2a8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00acc2a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00acc2a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00acc2a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00acd29c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00acd29c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00acd29c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00acd29c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00acc2a8 bytes 00303e91
+ 00acd29c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-824ccd932b8aa18e4fe128a802107f09"></a>

### [`00acc2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc2b0.md) → [`00acd2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd2a4.md) _INIT_247

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 55.93% / 新版 55.93%

CFGの説明率　旧版 75.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_store_alignment` 34件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc2e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc2f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc2f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00acc2e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acc2ec",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00acc2f4",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00acd2d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00acd2e0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00acd2e8",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acc2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc2b0.md#insn-00acc2e0) · [`00acc2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc2b0.md#insn-00acc2f4) · [`00acc2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc2b0.md#insn-00acc2f8)

~~~diff
- 00acc2e0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00acc2e0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00acc2e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00acc2e0 bytes a9831ff8
- 00acc2f4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00acc2f4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00acc2f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00acc2f4 bytes ea130278
- 00acc2f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00acc2f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00acc2f8 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70082e895d5d4cb49eadb5f0bc0f5956"></a>

### [`00acebcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acebcc.md) → [`00acfbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfbc0.md) FUN_00acfbc0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`005e12e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e12e4.md) [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`005e1790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1790.md) [`0066242c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/0066242c.md) [`006624d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/006624d0.md) · 呼出先 11件 [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md)
- 新版 呼出元 16件 [`005e1694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1694.md) [`005e1a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1a10.md) [`005e1b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1b40.md) [`006627dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/006627dc.md) [`00662880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/00662880.md) · 呼出先 11件 [`00676b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676b3c.md) [`007bcd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007bc/007bcd04.md) [`008011a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/008011a8.md) [`00803674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803674.md) [`00803b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b14.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 36.84% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00acec10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00acfc04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00acfc48",
      "incomplete_value": false,
      "site": "00acfc4c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00acec10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acebcc.md#insn-00acec10) · [`00acec58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acebcc.md#insn-00acec58) · [`00acec7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acebcc.md#insn-00acec7c)
- 新版 [`00acfc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfbc0.md#insn-00acfc4c) · [`00acfc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfbc0.md#insn-00acfc70)

~~~diff
- 00acec10 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00acec10 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00acec10 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00acec10 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00acec10 bytes 16019f1a
- 00acec58 ["INT_ADD", "register:40f0:8", ["const:acec58:8", "const:4:8"]]
- 00acec58 ["CALL", null, ["callee:00803674:8"]]
+ 00acfc4c ["INT_ADD", "register:40f0:8", ["const:acfc4c:8", "const:4:8"]]
+ 00acfc4c ["CALL", null, ["callee:00803674:8"]]
- 00acec58 bytes aecef497
+ 00acfc4c bytes 8acef497
- 00acec7c ["INT_ADD", "register:40f0:8", ["const:acec7c:8", "const:4:8"]]
- 00acec7c ["CALL", null, ["callee:00676b3c:8"]]
+ 00acfc70 ["INT_ADD", "register:40f0:8", ["const:acfc70:8", "const:4:8"]]
+ 00acfc70 ["CALL", null, ["callee:00676b3c:8"]]
- 00acec7c bytes c49eee97
+ 00acfc70 bytes b39bee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe3644143bbfac69816126fe30a300cb"></a>

### [`00acee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acee90.md) → [`00acfe84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfe84.md) FUN_00acfe84

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`005e12e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e12e4.md) [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`005e1790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1790.md) [`007de918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007de/007de918.md) [`007fe158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fe158.md) · 呼出先 8件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00acecc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acecc4.md) [`00aeae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 11件 [`005e1694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1694.md) [`005e1a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1a10.md) [`005e1b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1b40.md) [`007df87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007df/007df87c.md) [`007ff0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ff/007ff0bc.md) · 呼出先 8件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00acfcb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfcb8.md) [`00aebe80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aebe80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acfeec",
      "incomplete_value": true,
      "site": "00acfef4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aceef8",
      "incomplete_value": true,
      "site": "00acef00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad00f8",
      "incomplete_value": false,
      "site": "00ad00fc",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acf104",
      "incomplete_value": false,
      "site": "00acf108",
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
      "00acfeec",
      "READ",
      [
        "storage",
        "002c29a0",
        null,
        null
      ]
    ],
    [
      "00ad00f8",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acfeec",
      "READ",
      [
        "storage",
        "002c29f0",
        null,
        null
      ]
    ],
    [
      "00ad00f8",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acee90.md#insn-00acf108) · [`00aceec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acee90.md#insn-00aceec8) · [`00aceef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acee90.md#insn-00aceef8)
- 新版 [`00ad00fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfe84.md#insn-00ad00fc) · [`00acfebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfe84.md#insn-00acfebc) · [`00acfeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfe84.md#insn-00acfeec)

~~~diff
- 00acf108 ["INT_ADD", "register:40f0:8", ["const:acf108:8", "const:4:8"]]
- 00acf108 ["CALL", null, ["callee:00442c90:8"]]
+ 00ad00fc ["INT_ADD", "register:40f0:8", ["const:ad00fc:8", "const:4:8"]]
+ 00ad00fc ["CALL", null, ["callee:00442c90:8"]]
- 00acf108 bytes 1acee597
+ 00ad00fc bytes e5cae597
- 00aceec8 ["INT_ADD", "register:40f0:8", ["const:aceec8:8", "const:4:8"]]
- 00aceec8 ["CALL", null, ["callee:00acfcb8:8"]]
+ 00acfebc ["INT_ADD", "register:40f0:8", ["const:acfebc:8", "const:4:8"]]
+ 00acfebc ["CALL", null, ["callee:00acfcb8:8"]]
- 00aceec8 bytes 7fffff97
+ 00acfebc bytes 7fffff97
- 00aceef8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
- 00aceef8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00aceef8 ["COPY", "register:5030:8", ["const:0:8"]]
- 00aceef8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00acfeec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f0:8"]]
+ 00acfeec ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00acfeec ["COPY", "register:5030:8", ["const:0:8"]]
+ 00acfeec ["COPY", "register:5038:8", ["const:0:8"]]
- 00aceef8 bytes 0169c23d
+ 00acfeec bytes 017dc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1cd43fadeb6cffff1716dcd1bef60f7"></a>

### [`00acf228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf228.md) → [`00ad021c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad021c.md) FUN_00ad021c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 6件 [`0066242c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/0066242c.md) [`006624d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/006624d0.md) [`00662574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/00662574.md) [`007de918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007de/007de918.md) [`00acc640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc640.md) · 呼出先 8件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00acecc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acecc4.md) [`00aeae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 6件 [`006627dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/006627dc.md) [`00662880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/00662880.md) [`00662924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/00662924.md) [`007df87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007df/007df87c.md) [`00acd634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acd/00acd634.md) · 呼出先 8件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00acfcb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfcb8.md) [`00aebe80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aebe80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 90.91% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad027c",
      "incomplete_value": true,
      "site": "00ad0284",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acf288",
      "incomplete_value": true,
      "site": "00acf290",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad0438",
      "incomplete_value": false,
      "site": "00ad043c",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acf444",
      "incomplete_value": false,
      "site": "00acf448",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad04a8",
      "incomplete_value": true,
      "site": "00ad04ac",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "00ad027c",
      "READ",
      [
        "storage",
        "002c29a0",
        null,
        null
      ]
    ],
    [
      "00ad0438",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ad027c",
      "READ",
      [
        "storage",
        "002c29f0",
        null,
        null
      ]
    ],
    [
      "00ad0438",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf228.md#insn-00acf448) · [`00acf4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf228.md#insn-00acf4b8) · [`00acf25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf228.md#insn-00acf25c)
- 新版 [`00ad043c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad021c.md#insn-00ad043c) · [`00ad04ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad021c.md#insn-00ad04ac) · [`00ad0250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad021c.md#insn-00ad0250)

~~~diff
- 00acf448 ["INT_ADD", "register:40f0:8", ["const:acf448:8", "const:4:8"]]
- 00acf448 ["CALL", null, ["callee:00442c90:8"]]
+ 00ad043c ["INT_ADD", "register:40f0:8", ["const:ad043c:8", "const:4:8"]]
+ 00ad043c ["CALL", null, ["callee:00442c90:8"]]
- 00acf448 bytes 4acde597
+ 00ad043c bytes 15cae597
- 00acf4b8 ["INT_ADD", "register:40f0:8", ["const:acf4b8:8", "const:4:8"]]
- 00acf4b8 ["CALL", null, ["callee:00470ba0:8"]]
+ 00ad04ac ["INT_ADD", "register:40f0:8", ["const:ad04ac:8", "const:4:8"]]
+ 00ad04ac ["CALL", null, ["callee:00470ba0:8"]]
- 00acf4b8 bytes f284e697
+ 00ad04ac bytes bd81e697
- 00acf25c ["INT_ADD", "register:40f0:8", ["const:acf25c:8", "const:4:8"]]
- 00acf25c ["CALL", null, ["callee:00acfcb8:8"]]
+ 00ad0250 ["INT_ADD", "register:40f0:8", ["const:ad0250:8", "const:4:8"]]
+ 00ad0250 ["CALL", null, ["callee:00acfcb8:8"]]
- 00acf25c bytes 9afeff97
+ 00ad0250 bytes 9afeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29ca3cbd4377bf23dfab0b7a51d86fba"></a>

### [`00acf4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf4f4.md) → [`00ad04e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad04e8.md) FUN_00ad04e8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 3件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acf4f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acf4f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acf4f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00acf4f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acf4f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acf4fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad04e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ad04ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ad04f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf4f4.md#insn-00acf4f4) · [`00acf4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf4f4.md#insn-00acf4f8) · [`00acf4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf4f4.md#insn-00acf4fc)

~~~diff
- 00acf4f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00acf4f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00acf4f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00acf4f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00acf4f4 bytes fd7bbda9
- 00acf4f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00acf4f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00acf4f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00acf4f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00acf4f8 bytes f65701a9
- 00acf4fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00acf4fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00acf4fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00acf4fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00acf4fc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8db7c5b0907770004a4d07f76765d9"></a>

### [`00acfa94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfa94.md) → [`00ad0a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0a88.md) FUN_00ad0a88

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 6件 [`00695c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md) [`009a2b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a2/009a2b88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 6件 [`00695fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695fb4.md) [`009a3b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a3/009a3b34.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad0ac4",
      "incomplete_value": false,
      "site": "00ad0adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acfad0",
      "incomplete_value": false,
      "site": "00acfae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
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
      "00ad0ac4",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad0ac4",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfa94.md#insn-00acfae8) · [`00acfad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfa94.md#insn-00acfad0) · [`00acfb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfa94.md#insn-00acfb00)
- 新版 [`00ad0adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0a88.md#insn-00ad0adc) · [`00ad0ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0a88.md#insn-00ad0ac4) · [`00ad0af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0a88.md#insn-00ad0af4)

~~~diff
- 00acfae8 ["INT_ADD", "register:40f0:8", ["const:acfae8:8", "const:4:8"]]
- 00acfae8 ["CALL", null, ["callee:00695fb4:8"]]
+ 00ad0adc ["INT_ADD", "register:40f0:8", ["const:ad0adc:8", "const:4:8"]]
+ 00ad0adc ["CALL", null, ["callee:00695fb4:8"]]
- 00acfae8 bytes 4718ef97
+ 00ad0adc bytes 3615ef97
- 00acfad0 ["COPY", "tmp:0:8", ["const:735:8"]]
- 00acfad0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00acfad0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00acfad0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00ad0ac4 ["COPY", "tmp:0:8", ["const:785:8"]]
+ 00ad0ac4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad0ac4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad0ac4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00acfad0 bytes 42d41c91
+ 00ad0ac4 bytes 42141e91
- 00acfb00 ["INT_ADD", "register:40f0:8", ["const:acfb00:8", "const:4:8"]]
- 00acfb00 ["CALL", null, ["callee:00c54d60:8"]]
+ 00ad0af4 ["INT_ADD", "register:40f0:8", ["const:ad0af4:8", "const:4:8"]]
+ 00ad0af4 ["CALL", null, ["callee:00c54d60:8"]]
- 00acfb00 bytes 9c100694
+ 00ad0af4 bytes 9b100694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c05b6ccc459b7ed06eb10158a315708d"></a>

### [`00acfc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfc50.md) → [`00ad0c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0c44.md) FUN_00ad0c44

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 6件 [`00695c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md) [`009a2b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a2/009a2b88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 6件 [`00695fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695fb4.md) [`009a3b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a3/009a3b34.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ad0c80",
      "incomplete_value": false,
      "site": "00ad0c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acfc8c",
      "incomplete_value": false,
      "site": "00acfca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
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
      "00ad0c80",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad0c80",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfc50.md#insn-00acfca4) · [`00acfc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfc50.md#insn-00acfc8c) · [`00acfcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfc50.md#insn-00acfcbc)
- 新版 [`00ad0c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0c44.md#insn-00ad0c98) · [`00ad0c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0c44.md#insn-00ad0c80) · [`00ad0cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0c44.md#insn-00ad0cb0)

~~~diff
- 00acfca4 ["INT_ADD", "register:40f0:8", ["const:acfca4:8", "const:4:8"]]
- 00acfca4 ["CALL", null, ["callee:00695fb4:8"]]
+ 00ad0c98 ["INT_ADD", "register:40f0:8", ["const:ad0c98:8", "const:4:8"]]
+ 00ad0c98 ["CALL", null, ["callee:00695fb4:8"]]
- 00acfca4 bytes d817ef97
+ 00ad0c98 bytes c714ef97
- 00acfc8c ["COPY", "tmp:0:8", ["const:735:8"]]
- 00acfc8c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00acfc8c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00acfc8c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00ad0c80 ["COPY", "tmp:0:8", ["const:785:8"]]
+ 00ad0c80 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad0c80 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00ad0c80 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00acfc8c bytes 42d41c91
+ 00ad0c80 bytes 42141e91
- 00acfcbc ["INT_ADD", "register:40f0:8", ["const:acfcbc:8", "const:4:8"]]
- 00acfcbc ["CALL", null, ["callee:00c54d60:8"]]
+ 00ad0cb0 ["INT_ADD", "register:40f0:8", ["const:ad0cb0:8", "const:4:8"]]
+ 00ad0cb0 ["CALL", null, ["callee:00c54d60:8"]]
- 00acfcbc bytes 2d100694
+ 00ad0cb0 bytes 2c100694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d4a90136f32e1c3d6e46e8bce95057a"></a>

### [`00acfd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfd30.md) → [`00ad0d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad0d24.md) FUN_00ad0d24

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) [`00aec9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md) · 呼出先 17件 [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00498210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498210.md) [`00633824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/00633824.md) [`00666c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00666/00666c68.md) [`00695c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00695/00695c04.md)
- 新版 呼出元 3件 [`00ad19bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad19bc.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) [`00aed9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9f0.md) · 呼出先 17件 [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00498530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498530.md) [`00633bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00633/00633bd4.md) [`00667018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00667/00667018.md) [`00695fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00695/00695fb4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.99% / 新版 77.99%

CFGの説明率　旧版 45.45% / 新版 45.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfd88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad0058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad005c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ad0d68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00acfd84"
      ]
    ],
    [
      "unmatched:00acfd78",
      "READ",
      [
        "storage",
        "00ca46f0",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00acfd80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad1320"
      ]
    ]
  ],
  "added": [
    [
      "00ad0d68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad0d78"
      ]
    ],
    [
      "00ad0d6c",
      "READ",
      [
        "storage",
        "00ca56c0",
        null,
        "undefined4"
      ]
    ],
    [
      "00ad0d74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ad1320"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfd30.md#insn-00acfd80) · [`00acfd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfd30.md#insn-00acfd88) · [`00acfd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acfd30.md#insn-00acfd90)

~~~diff
- 00acfd80 ["CBRANCH", null, ["local:b85:8", "register:101:1"]]
- 00acfd80 bytes 602d0054
- 00acfd88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6f0:8"]]
- 00acfd88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00acfd88 bytes 14f106b9
- 00acfd90 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00acfd90 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00acfd90 bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bd007ec536c31d19eea1d1876c17f6"></a>

### [`00ad0410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0410.md) → [`00ad1404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1404.md) FUN_00ad1404

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 8件 [`008bc920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc920.md) [`008c2538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2538.md) [`008c42e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c4/008c42e4.md) [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) [`008c8e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8e60.md) · 呼出先 3件 [`009df688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df688.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)
- 新版 呼出元 8件 [`008bd8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd8cc.md) [`008c34e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c34e4.md) [`008c5290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c5/008c5290.md) [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) [`008c9e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c9/008c9e0c.md) · 呼出先 3件 [`009e0634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0634.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e3f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e3/009e3f94.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00ad046c",
      "incomplete_value": true,
      "site": "00ad0478",
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
              [
                "live",
                "register:4040:8"
              ]
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


#### 変更候補の命令位置

- 旧版 [`00ad0430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0410.md#insn-00ad0430) · [`00ad0444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0410.md#insn-00ad0444) · [`00ad0450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0410.md#insn-00ad0450)
- 新版 [`00ad1424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1404.md#insn-00ad1424) · [`00ad1438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1404.md#insn-00ad1438) · [`00ad1444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1404.md#insn-00ad1444)

~~~diff
- 00ad0430 ["INT_ADD", "register:40f0:8", ["const:ad0430:8", "const:4:8"]]
- 00ad0430 ["CALL", null, ["callee:009e1fc0:8"]]
+ 00ad1424 ["INT_ADD", "register:40f0:8", ["const:ad1424:8", "const:4:8"]]
+ 00ad1424 ["CALL", null, ["callee:009e1fc0:8"]]
- 00ad0430 bytes f942fc97
+ 00ad1424 bytes e742fc97
- 00ad0444 ["INT_ADD", "register:40f0:8", ["const:ad0444:8", "const:4:8"]]
- 00ad0444 ["CALL", null, ["callee:009e3f94:8"]]
+ 00ad1438 ["INT_ADD", "register:40f0:8", ["const:ad1438:8", "const:4:8"]]
+ 00ad1438 ["CALL", null, ["callee:009e3f94:8"]]
- 00ad0444 bytes e94afc97
+ 00ad1438 bytes d74afc97
- 00ad0450 ["INT_ADD", "register:40f0:8", ["const:ad0450:8", "const:4:8"]]
- 00ad0450 ["CALL", null, ["callee:009e0634:8"]]
+ 00ad1444 ["INT_ADD", "register:40f0:8", ["const:ad1444:8", "const:4:8"]]
+ 00ad1444 ["CALL", null, ["callee:009e0634:8"]]
- 00ad0450 bytes 8e3cfc97
+ 00ad1444 bytes 7c3cfc97
~~~


<a id="compare-346a4bd6e7a1fe33b46fd7cc13bfe202"></a>

### [`00ad047c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad047c.md) → [`00ad1470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1470.md) FUN_00ad1470

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00aede7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aede7c.md) [`00af1748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af1/00af1748.md) · 呼出先 9件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md)
- 新版 呼出元 2件 [`00aeee70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aeee70.md) [`00af273c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af2/00af273c.md) · 呼出先 9件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md) [`008bbccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbccc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.43% / 新版 93.43%

CFGの説明率　旧版 86.67% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad1524",
      "incomplete_value": true,
      "site": "00ad1524",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad0530",
      "incomplete_value": true,
      "site": "00ad0530",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:870:8"
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
      "definition_site": "00ad1594",
      "incomplete_value": true,
      "site": "00ad15a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad05a0",
      "incomplete_value": true,
      "site": "00ad05b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:804:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad15fc",
      "incomplete_value": false,
      "site": "00ad15fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad0608",
      "incomplete_value": false,
      "site": "00ad0608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00ad14ac",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ],
    [
      "00ad1514",
      "READ",
      [
        "storage",
        "002a1870",
        null,
        "string"
      ]
    ],
    [
      "00ad1540",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "00ad14ac",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ],
    [
      "00ad1514",
      "READ",
      [
        "storage",
        "002a18b0",
        null,
        "string"
      ]
    ],
    [
      "00ad1540",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad04a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad047c.md#insn-00ad04a0) · [`00ad04a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad047c.md#insn-00ad04a8) · [`00ad0510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad047c.md#insn-00ad0510)
- 新版 [`00ad1494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1470.md#insn-00ad1494) · [`00ad149c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1470.md#insn-00ad149c) · [`00ad1504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad1470.md#insn-00ad1504)

~~~diff
- 00ad04a0 ["INT_ADD", "register:40f0:8", ["const:ad04a0:8", "const:4:8"]]
- 00ad04a0 ["CALL", null, ["callee:008524fc:8"]]
+ 00ad1494 ["INT_ADD", "register:40f0:8", ["const:ad1494:8", "const:4:8"]]
+ 00ad1494 ["CALL", null, ["callee:008524fc:8"]]
- 00ad04a0 bytes 2c04f697
+ 00ad1494 bytes 1a04f697
- 00ad04a8 ["INT_ADD", "register:40f0:8", ["const:ad04a8:8", "const:4:8"]]
- 00ad04a8 ["CALL", null, ["callee:008524fc:8"]]
+ 00ad149c ["INT_ADD", "register:40f0:8", ["const:ad149c:8", "const:4:8"]]
+ 00ad149c ["CALL", null, ["callee:008524fc:8"]]
- 00ad04a8 bytes 2a04f697
+ 00ad149c bytes 1804f697
- 00ad0510 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ad0510 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00ad1504 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00ad1504 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00ad0510 bytes 4b0b0054
+ 00ad1504 bytes 4b0b0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa009c78a7c973b3c0bc3c5f99b92939"></a>

### [`00ad0748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0748.md) → [`00ad173c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad173c.md) FUN_00ad173c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00aede7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aede7c.md) · 呼出先 9件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bb144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bb144.md)
- 新版 呼出元 1件 [`00aeee70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aeee70.md) · 呼出先 9件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md) [`008bc0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc0f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad17a0",
      "incomplete_value": true,
      "site": "00ad17a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad07ac",
      "incomplete_value": true,
      "site": "00ad07ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb2:8"
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
      "definition_site": "00ad1814",
      "incomplete_value": true,
      "site": "00ad1828",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8ba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad0820",
      "incomplete_value": true,
      "site": "00ad0834",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:87a:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad187c",
      "incomplete_value": false,
      "site": "00ad187c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad0888",
      "incomplete_value": false,
      "site": "00ad0888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00ad1790",
      "READ",
      [
        "storage",
        "002adfb2",
        null,
        "string"
      ]
    ],
    [
      "00ad1814",
      "READ",
      [
        "storage",
        "002a187a",
        null,
        "string"
      ]
    ],
    [
      "00ad187c",
      "DATA",
      [
        "storage",
        "00c8dac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ad1790",
      "READ",
      [
        "storage",
        "002ae07f",
        null,
        "string"
      ]
    ],
    [
      "00ad1814",
      "READ",
      [
        "storage",
        "002a18ba",
        null,
        "string"
      ]
    ],
    [
      "00ad187c",
      "DATA",
      [
        "storage",
        "00c8ea98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad0780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0748.md#insn-00ad0780) · [`00ad0790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0748.md#insn-00ad0790) · [`00ad0794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad0748.md#insn-00ad0794)
- 新版 [`00ad1774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad173c.md#insn-00ad1774) · [`00ad1784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad173c.md#insn-00ad1784) · [`00ad1788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad173c.md#insn-00ad1788)

~~~diff
- 00ad0780 ["INT_ADD", "register:40f0:8", ["const:ad0780:8", "const:4:8"]]
- 00ad0780 ["CALL", null, ["callee:008524fc:8"]]
+ 00ad1774 ["INT_ADD", "register:40f0:8", ["const:ad1774:8", "const:4:8"]]
+ 00ad1774 ["CALL", null, ["callee:008524fc:8"]]
- 00ad0780 bytes 7403f697
+ 00ad1774 bytes 6203f697
- 00ad0790 ["COPY", "register:4048:8", ["const:2ad000:8"]]
+ 00ad1784 ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 00ad0790 bytes e9beffb0
+ 00ad1784 bytes e9beffb0
- 00ad0794 ["COPY", "tmp:0:8", ["const:fb2:8"]]
- 00ad0794 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad0794 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad0794 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad1788 ["COPY", "tmp:0:8", ["const:7f:8"]]
+ 00ad1788 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad1788 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad1788 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad0794 bytes 29c93e91
+ 00ad1788 bytes 29fd0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743f18f8819c2d4f7c8749594ab90474"></a>

### [`00ad6a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6a90.md) → [`00ad7a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7a84.md) FUN_00ad7a84

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 4件 [`00664e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e80.md) [`009df688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df688.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)
- 新版 呼出元 1件 [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 4件 [`00665230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665230.md) [`009e0634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0634.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e3f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e3/009e3f94.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 22.22% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6a90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6a90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6a94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad6a90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad6a94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad7a84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ad7a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6a90.md#insn-00ad6a90) · [`00ad6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6a90.md#insn-00ad6a94) · [`00ad6ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6a90.md#insn-00ad6ac4)
- 新版 [`00ad7ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7a84.md#insn-00ad7ab8)

~~~diff
- 00ad6a90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ad6a90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ad6a90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ad6a90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ad6a90 bytes fd7bbea9
- 00ad6a94 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ad6a94 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ad6a94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ad6a94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad6a94 bytes f44f01a9
- 00ad6ac4 ["INT_ADD", "register:40f0:8", ["const:ad6ac4:8", "const:4:8"]]
- 00ad6ac4 ["CALL", null, ["callee:009e3f94:8"]]
+ 00ad7ab8 ["INT_ADD", "register:40f0:8", ["const:ad7ab8:8", "const:4:8"]]
+ 00ad7ab8 ["CALL", null, ["callee:009e3f94:8"]]
- 00ad6ac4 bytes 4931fc97
+ 00ad7ab8 bytes 3731fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2af87c11f349f040e76625f5833727f"></a>

### [`00ad6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md) → [`00ad7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7aec.md) FUN_00ad7aec

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00ad09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad0/00ad09c8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) [`00ae0cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0cd8.md) [`00aec9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md) [`00af01a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md) · 呼出先 23件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md) [`00615950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615950.md) [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`00743de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743de8.md)
- 新版 呼出元 6件 [`00ad19bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad1/00ad19bc.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) [`00ae1ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae1ccc.md) [`00aed9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9f0.md) [`00af1198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1198.md) · 呼出先 23件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005c08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c08e0.md) [`00615d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00615/00615d00.md) [`00676b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676b3c.md) [`00744198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744198.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.16% / 新版 90.16%

CFGの説明率　旧版 12.50% / 新版 12.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_condition` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6afc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad6af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad6afc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad6b00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad7aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ad7af0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ad7af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md#insn-00ad6af8) · [`00ad6afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md#insn-00ad6afc) · [`00ad6b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md#insn-00ad6b00)

~~~diff
- 00ad6af8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ad6af8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ad6af8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00ad6af8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ad6af8 bytes fd7bbba9
- 00ad6afc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ad6afc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ad6afc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ad6afc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad6afc bytes fa6701a9
- 00ad6b00 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ad6b00 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ad6b00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ad6b00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad6b00 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a33e241647e270f1c07a08381d7d2314"></a>

### [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) → [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) FUN_00ad7fb0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 150件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 150件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.74% / 新版 76.74%

CFGの説明率　旧版 36.71% / 新版 36.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 210件, `call_target` 13件, `store_condition` 18件, `store_value` 5件, `unresolved_branch_alignment` 199件, `unresolved_call_alignment` 170件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 182件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad7000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad7358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad7768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad7000",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad7004",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ],
    [
      "00ad80a8",
      "DATA",
      [
        "storage",
        "00477de0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad7ff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00ad7ff8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ],
    [
      "00ad80fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad7000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md#insn-00ad7000) · [`00ad711c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md#insn-00ad711c) · [`00ad7358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md#insn-00ad7358)
- 新版 [`00ad8110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md#insn-00ad8110)

~~~diff
- 00ad7000 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ad7000 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe0:8"]]
- 00ad7000 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ad7000 bytes a8031ef8
- 00ad711c ["INT_ADD", "register:40f0:8", ["const:ad711c:8", "const:4:8"]]
- 00ad711c ["CALL", null, ["callee:00658870:8"]]
+ 00ad8110 ["INT_ADD", "register:40f0:8", ["const:ad8110:8", "const:4:8"]]
+ 00ad8110 ["CALL", null, ["callee:00658870:8"]]
- 00ad711c bytes e904ee97
+ 00ad8110 bytes d801ee97
- 00ad7358 ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:38:8"]]
- 00ad7358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:4"]]
- 00ad7358 bytes cc3900b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d809ec28a52a99980a15eab7db5d5cf3"></a>

### [`00adf288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md) → [`00ae027c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae0/00ae027c.md) FUN_00ae027c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`007fa9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fa/007fa9e8.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) [`009fd2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd2e4.md) [`00a003b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a003b0.md) [`00a045fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a045fc.md) · 呼出先 43件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md)
- 新版 呼出元 6件 [`007fb94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fb/007fb94c.md) [`0098ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098e/0098ec08.md) [`009fe290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fe/009fe290.md) [`00a0135c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a0135c.md) [`00a055a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a055a8.md) · 呼出先 43件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004421f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/004421f4.md) [`0045001c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/0045001c.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.82% / 新版 79.82%

CFGの説明率　旧版 39.35% / 新版 39.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 38件, `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 27件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf6c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf87c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfa80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae02c8",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ],
    [
      "00ae02d0",
      "DATA",
      [
        "storage",
        "00436bc8",
        null,
        "byte[47]"
      ]
    ],
    [
      "00ae02d0",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "00ae02c8",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "uleb128"
      ]
    ],
    [
      "00ae02d0",
      "DATA",
      [
        "storage",
        "00436bc8",
        null,
        "dword"
      ]
    ],
    [
      "00ae02d0",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adf6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md#insn-00adf6c8) · [`00adf87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md#insn-00adf87c) · [`00adfa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md#insn-00adfa80)

~~~diff
- 00adf6c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adf6c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 00adf6c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adf6c8 bytes a8031bf8
- 00adf87c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:4:8"]]
- 00adf87c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00adf87c bytes 680700b9
- 00adfa80 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adfa80 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00adfa80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adfa80 bytes a8031af8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b9bff072fbb0d0be5052e0bf1de88e5"></a>

### [`00ae0c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0c04.md) → [`00ae1bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae1bf8.md) FUN_00ae1bf8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`008c8e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8e60.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 4件 [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e3140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3140.md) [`00b096f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b096f8.md) [`00b0a890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0a890.md)
- 新版 呼出元 2件 [`008c9e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c9/008c9e0c.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 4件 [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e40ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e4/009e40ec.md) [`00b0a6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0a/00b0a6ec.md) [`00b0b884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0b/00b0b884.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0c04.md#insn-00ae0c18) · [`00ae0c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0c04.md#insn-00ae0c48) · [`00ae0c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0c04.md#insn-00ae0c4c)
- 新版 [`00ae1c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae1bf8.md#insn-00ae1c0c) · [`00ae1c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae1bf8.md#insn-00ae1c3c) · [`00ae1c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae1bf8.md#insn-00ae1c40)

~~~diff
- 00ae0c18 ["INT_ADD", "register:40f0:8", ["const:ae0c18:8", "const:4:8"]]
- 00ae0c18 ["CALL", null, ["callee:00b0a6ec:8"]]
+ 00ae1c0c ["INT_ADD", "register:40f0:8", ["const:ae1c0c:8", "const:4:8"]]
+ 00ae1c0c ["CALL", null, ["callee:00b0a6ec:8"]]
- 00ae0c18 bytes b8a20094
+ 00ae1c0c bytes b8a20094
- 00ae0c48 ["INT_ADD", "register:40f0:8", ["const:ae0c48:8", "const:4:8"]]
- 00ae0c48 ["CALL", null, ["callee:009e1fc0:8"]]
+ 00ae1c3c ["INT_ADD", "register:40f0:8", ["const:ae1c3c:8", "const:4:8"]]
+ 00ae1c3c ["CALL", null, ["callee:009e1fc0:8"]]
- 00ae0c48 bytes f300fc97
+ 00ae1c3c bytes e100fc97
- 00ae0c4c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00ae0c4c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ae0c4c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ae0c4c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00ae1c40 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00ae1c40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ae1c40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ae1c40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ae0c4c bytes e0000036
+ 00ae1c40 bytes e0000036
~~~


<a id="compare-b8dba517990b331f3ec1b15e5e310a9d"></a>

### [`00ae0cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0cd8.md) → [`00ae1ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae1ccc.md) FUN_00ae1ccc

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 20件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00665da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665da4.md) [`008b6f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f98.md)
- 新版 呼出元 2件 [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 20件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00666154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00666/00666154.md) [`008b7f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f44.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.55% / 新版 83.55%

CFGの説明率　旧版 67.78% / 新版 73.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0ce0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae0cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0ce0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae1cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00ae1cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ae1cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0cd8.md#insn-00ae0cdc) · [`00ae0ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0cd8.md#insn-00ae0ce0) · [`00ae0ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae0cd8.md#insn-00ae0ce4)

~~~diff
- 00ae0cdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae0cdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae0cdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00ae0cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0cdc bytes fd7b0aa9
- 00ae0ce0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ae0ce0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00ae0ce0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00ae0ce0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0ce0 bytes fc6f0ba9
- 00ae0ce4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ae0ce4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ae0ce4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00ae0ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0ce4 bytes fa670ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6688ffc4a0bdb67ae871338cac31fa26"></a>

### [`00ae124c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae124c.md) → [`00ae2240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae2240.md) FUN_00ae2240

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 1件 [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md)
- 新版 呼出元 1件 [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 1件 [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae1294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae124c.md#insn-00ae1294)
- 新版 [`00ae2288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae2240.md#insn-00ae2288)

~~~diff
- 00ae1294 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae1294 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00ae1294 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
+ 00ae2288 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00ae2288 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00ae2288 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00ae1294 bytes 6d000054
+ 00ae2288 bytes 6d000054
~~~


<a id="compare-ecbb794a9195c969b8731420b95ae02e"></a>

### [`00ae12b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae12b0.md) → [`00ae22a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae22a4.md) FUN_00ae22a4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 3件 [`009df688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df688.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)
- 新版 呼出元 1件 [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 3件 [`009e0634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0634.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e3f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e3/009e3f94.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae12d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae12b0.md#insn-00ae12d8) · [`00ae12dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae12b0.md#insn-00ae12dc) · [`00ae12ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae12b0.md#insn-00ae12ec)
- 新版 [`00ae22cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae22a4.md#insn-00ae22cc) · [`00ae22d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae22a4.md#insn-00ae22d0) · [`00ae22e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae22a4.md#insn-00ae22e0)

~~~diff
- 00ae12d8 ["INT_ADD", "register:40f0:8", ["const:ae12d8:8", "const:4:8"]]
- 00ae12d8 ["CALL", null, ["callee:009e1fc0:8"]]
+ 00ae22cc ["INT_ADD", "register:40f0:8", ["const:ae22cc:8", "const:4:8"]]
+ 00ae22cc ["CALL", null, ["callee:009e1fc0:8"]]
- 00ae12d8 bytes 4ffffb97
+ 00ae22cc bytes 3dfffb97
- 00ae12dc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00ae12dc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ae12dc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ae12dc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00ae22d0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00ae22d0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ae22d0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ae22d0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ae12dc bytes 60010036
+ 00ae22d0 bytes 60010036
- 00ae12ec ["INT_ADD", "register:40f0:8", ["const:ae12ec:8", "const:4:8"]]
- 00ae12ec ["CALL", null, ["callee:009e3f94:8"]]
+ 00ae22e0 ["INT_ADD", "register:40f0:8", ["const:ae22e0:8", "const:4:8"]]
+ 00ae22e0 ["CALL", null, ["callee:009e3f94:8"]]
- 00ae12ec bytes 3f07fc97
+ 00ae22e0 bytes 2d07fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c20cc0d1b9eb83a10091bb1503f8dae"></a>

### [`00aea3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea3f0.md) → [`00aeb3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb3e4.md) FUN_00aeb3e4

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) [`00aef1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef1e8.md) [`00aeff08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md) · 呼出先 10件 [`005c0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md) [`00743f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743f84.md) [`00744048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744048.md) [`007441f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/007441f0.md) [`00744260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md)
- 新版 呼出元 3件 [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) [`00af01dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af01dc.md) [`00af0efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0efc.md) · 呼出先 10件 [`005c08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c08e0.md) [`00744334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744334.md) [`007443f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007443f8.md) [`007445a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007445a0.md) [`00744610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.72% / 新版 92.72%

CFGの説明率　旧版 9.52% / 新版 9.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea4a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aeb498"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aeb448",
      "incomplete_value": true,
      "site": "00aeb44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "INT_OR"
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00aea4a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb618"
      ]
    ],
    [
      "00aeb4b0",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ],
    [
      "00aeb56c",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "00aeb498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb618"
      ]
    ],
    [
      "00aeb4b0",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ],
    [
      "00aeb56c",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea3f0.md#insn-00aea458) · [`00aea4a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea3f0.md#insn-00aea4a4) · [`00aea510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea3f0.md#insn-00aea510)
- 新版 [`00aeb44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb3e4.md#insn-00aeb44c) · [`00aeb504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb3e4.md#insn-00aeb504)

~~~diff
- 00aea458 ["INT_ADD", "register:40f0:8", ["const:aea458:8", "const:4:8"]]
- 00aea458 ["CALL", null, ["callee:00a43078:8"]]
+ 00aeb44c ["INT_ADD", "register:40f0:8", ["const:aeb44c:8", "const:4:8"]]
+ 00aeb44c ["CALL", null, ["callee:00a43078:8"]]
- 00aea458 bytes 0b5ffd97
+ 00aeb44c bytes 0b5ffd97
- 00aea4a4 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 00aea4a4 bytes 000c0054
- 00aea510 ["INT_ADD", "register:40f0:8", ["const:aea510:8", "const:4:8"]]
- 00aea510 ["CALL", null, ["callee:007445a0:8"]]
+ 00aeb504 ["INT_ADD", "register:40f0:8", ["const:aeb504:8", "const:4:8"]]
+ 00aeb504 ["CALL", null, ["callee:007445a0:8"]]
- 00aea510 bytes 3867f197
+ 00aeb504 bytes 2764f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ae2f54133d3a8f35d22c493e1be1fd7"></a>

### [`00aea64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea64c.md) → [`00aeb640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb640.md) FUN_00aeb640

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) [`00aef1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef1e8.md) [`00aeff08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md) · 呼出先 4件 [`005c0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md) [`00743f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00743/00743f84.md) [`007441f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/007441f0.md) [`00744260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md)
- 新版 呼出元 3件 [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) [`00af01dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af01dc.md) [`00af0efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0efc.md) · 呼出先 4件 [`005c08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c08e0.md) [`00744334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744334.md) [`007445a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/007445a0.md) [`00744610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 72.04% / 新版 72.04%

CFGの説明率　旧版 35.29% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea6f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aeb6e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aea740",
      "incomplete_value": true,
      "site": "00aea790",
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
            "const:4a0:8"
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
      "00aeb690",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ],
    [
      "unmatched:00aea6f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb794"
      ]
    ],
    [
      "00aeb730",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "00aeb690",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ],
    [
      "00aeb6e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb794"
      ]
    ],
    [
      "00aeb730",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea64c.md#insn-00aea6f0) · [`00aea790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea64c.md#insn-00aea790)
- 新版 [`00aeb784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb640.md#insn-00aeb784) · [`00aeb6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb640.md#insn-00aeb6e4)

~~~diff
- 00aea6f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aea6f0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00aea6f0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00aea6f0 ["CBRANCH", null, ["local:b11:8", "tmp:2:1"]]
- 00aea6f0 bytes 8c050054
- 00aea790 ["INT_ADD", "register:40f0:8", ["const:aea790:8", "const:4:8"]]
- 00aea790 ["CALL", null, ["callee:005c08e0:8"]]
+ 00aeb784 ["INT_ADD", "register:40f0:8", ["const:aeb784:8", "const:4:8"]]
+ 00aeb784 ["CALL", null, ["callee:005c08e0:8"]]
- 00aea790 bytes 6857eb97
+ 00aeb784 bytes 5754eb97
+ 00aeb6e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00aeb6e4 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00aeb6e4 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00aeb6e4 ["CBRANCH", null, ["local:b11:8", "tmp:2:1"]]
+ 00aeb6e4 bytes 8c050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81043dcfff5984a7067d4c0e94d2933d"></a>

### [`00aea7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea7c0.md) → [`00aeb7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb7b4.md) FUN_00aeb7b4

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) [`00af0dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0dec.md) · 呼出先 21件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b30.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md)
- 新版 呼出元 2件 [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) [`00af1de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1de0.md) · 呼出先 21件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e50.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 70.57% / 新版 70.57%

CFGの説明率　旧版 19.48% / 新版 19.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 11件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aeb7e8",
      "incomplete_value": true,
      "site": "00aeb7e8",
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
      "definition_site": "00aea7f4",
      "incomplete_value": true,
      "site": "00aea7f4",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea8e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea970"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeb7dc",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb7f0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00aeb7f8",
      "PARAM",
      [
        "storage",
        "00c8da20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00aeb7dc",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb7f0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00aeb7f8",
      "PARAM",
      [
        "storage",
        "00c8e9f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea7c0.md#insn-00aea80c) · [`00aea8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea7c0.md#insn-00aea8b0) · [`00aea8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aea7c0.md#insn-00aea8d4)
- 新版 [`00aeb800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb7b4.md#insn-00aeb800) · [`00aeb8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb7b4.md#insn-00aeb8a4) · [`00aeb8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aeb7b4.md#insn-00aeb8c8)

~~~diff
- 00aea80c ["INT_ADD", "register:40f0:8", ["const:aea80c:8", "const:4:8"]]
- 00aea80c ["CALL", null, ["callee:00c596b0:8"]]
+ 00aeb800 ["INT_ADD", "register:40f0:8", ["const:aeb800:8", "const:4:8"]]
+ 00aeb800 ["CALL", null, ["callee:00c596b0:8"]]
- 00aea80c bytes b5b70594
+ 00aeb800 bytes acb70594
- 00aea8b0 ["INT_ADD", "register:40f0:8", ["const:aea8b0:8", "const:4:8"]]
- 00aea8b0 ["CALL", null, ["callee:00ae00f4:8"]]
+ 00aeb8a4 ["INT_ADD", "register:40f0:8", ["const:aeb8a4:8", "const:4:8"]]
+ 00aeb8a4 ["CALL", null, ["callee:00ae00f4:8"]]
- 00aea8b0 bytes 14d2ff97
+ 00aeb8a4 bytes 14d2ff97
- 00aea8d4 ["INT_ADD", "register:40f0:8", ["const:aea8d4:8", "const:4:8"]]
- 00aea8d4 ["CALL", null, ["callee:0046de1c:8"]]
+ 00aeb8c8 ["INT_ADD", "register:40f0:8", ["const:aeb8c8:8", "const:4:8"]]
+ 00aeb8c8 ["CALL", null, ["callee:0046de1c:8"]]
- 00aea8d4 bytes 8a0ce697
+ 00aeb8c8 bytes 5509e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1690b671a0dbf10bcc52adef77114dc"></a>

### [`00aeae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md) → [`00aebe80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aeb/00aebe80.md) FUN_00aebe80

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00acecc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acecc4.md) [`00acee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acee90.md) [`00acf228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acf/00acf228.md) · 呼出先 6件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 3件 [`00acfcb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfcb8.md) [`00acfe84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfe84.md) [`00ad021c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad0/00ad021c.md) · 呼出先 6件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.87% / 新版 85.87%

CFGの説明率　旧版 21.74% / 新版 20.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaeb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeaea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeaeb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeaeec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebf94"
      ]
    ]
  ],
  "added": [
    [
      "00aebe98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aebea8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aebee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aebf94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md#insn-00aeaea4) · [`00aeaeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md#insn-00aeaeb4) · [`00aeaeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md#insn-00aeaeec)

~~~diff
- 00aeaea4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeaea4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeaea4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00aeaea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeaea4 bytes f44f08a9
- 00aeaeb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aeaeb4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aeaeb4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aeaeb4 bytes a8831ff8
- 00aeaeec ["CBRANCH", null, ["local:b30:8", "register:101:1"]]
- 00aeaeec bytes a0050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072ae62edb3122f4b5faf9a49252b69f"></a>

### [`00aeb030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb030.md) → [`00aec024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aec/00aec024.md) FUN_00aec024

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0066242c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/0066242c.md) [`006624d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00662/006624d0.md)
- 新版 呼出元 2件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 18件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`006627dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/006627dc.md) [`00662880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00662/00662880.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.42% / 新版 90.42%

CFGの説明率　旧版 31.58% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 22件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb464"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aec344",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeb380"
      ]
    ],
    [
      "00aec350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeb380"
      ]
    ],
    [
      "unmatched:00aeb378",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec354"
      ]
    ]
  ],
  "added": [
    [
      "00aec344",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec374"
      ]
    ],
    [
      "00aec350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec374"
      ]
    ],
    [
      "00aec36c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec354"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb030.md#insn-00aeb378) · [`00aeb38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb030.md#insn-00aeb38c) · [`00aeb3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb030.md#insn-00aeb3e0)

~~~diff
- 00aeb378 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeb378 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00aeb378 bytes 48ffffb5
- 00aeb38c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00aeb38c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeb38c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00aeb38c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00aeb38c bytes 1f7c03a9
- 00aeb3e0 ["CBRANCH", null, ["local:b74:8", "register:101:1"]]
- 00aeb3e0 bytes 80110054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aadba89e7d4b06d6784e8b4cdd6f074"></a>

### [`00aeb97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb97c.md) → [`00aec970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aec/00aec970.md) FUN_00aec970

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aeb030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb030.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00aec024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aec/00aec024.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.39% / 新版 80.39%

CFGの説明率　旧版 5.00% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb97c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb97c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb980"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb97c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb980",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb984",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec970",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aec974",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aec978",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb97c.md#insn-00aeb97c) · [`00aeb980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb97c.md#insn-00aeb980) · [`00aeb984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aeb97c.md#insn-00aeb984)

~~~diff
- 00aeb97c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb97c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb97c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aeb97c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb97c bytes fd7bbca9
- 00aeb980 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aeb980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00aeb980 bytes f70b00f9
- 00aeb984 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aeb984 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aeb984 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aeb984 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb984 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f13fb0cd4e9439094d9936da33ba89b0"></a>

### [`00aebc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aebc30.md) → [`00aecc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aec/00aecc24.md) FUN_00aecc24

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af01a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md) [`00af075c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af075c.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00665da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665da4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 2件 [`00af1198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1198.md) [`00af1750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1750.md) · 呼出先 12件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00666154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00666/00666154.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.31% / 新版 74.31%

CFGの説明率　旧版 20.24% / 新版 19.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebc58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebc60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebc58",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebc60",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aecc5c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aecc4c",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "00aecc54",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aecc5c",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aebc30.md#insn-00aebc58) · [`00aebc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aebc30.md#insn-00aebc60) · [`00aebc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aebc30.md#insn-00aebc6c)
- 新版 [`00aecc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aec/00aecc24.md#insn-00aecc60)

~~~diff
- 00aebc58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00aebc58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aebc58 bytes e80700f9
- 00aebc60 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aebc60 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aebc60 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aebc60 bytes a8831ff8
- 00aebc6c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aebc6c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00aecc60 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aecc60 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aebc6c bytes 280100b4
+ 00aecc60 bytes 280100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbeec276d52634f07884d9ccba92f1d8"></a>

### [`00aec00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec00c.md) → [`00aed000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed000.md) FUN_00aed000

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`007075c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/007075c0.md) [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) · 呼出先 10件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00664e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e50.md) [`00b03c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03c30.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 3件 [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`00707970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00707/00707970.md) [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) · 呼出先 10件 [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00665200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665200.md) [`00b04c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b04/00b04c24.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 64.81% / 新版 72.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec020"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec01c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec020",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec024",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed010",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aed014",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aed018",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec00c.md#insn-00aec01c) · [`00aec020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec00c.md#insn-00aec020) · [`00aec024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec00c.md#insn-00aec024)

~~~diff
- 00aec01c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00aec01c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00aec01c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00aec01c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec01c bytes f85f06a9
- 00aec020 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aec020 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aec020 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00aec020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec020 bytes f65707a9
- 00aec024 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aec024 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aec024 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00aec024 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec024 bytes f44f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efcde20d7cdb837f160034d42ef75285"></a>

### [`00aec27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec27c.md) → [`00aed270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed270.md) FUN_00aed270

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00adf288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00ae027c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae0/00ae027c.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 44.44% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec32c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aed320"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec310"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec310",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aed310"
      ]
    ]
  ],
  "added": [
    [
      "00aed304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aed310"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec27c.md#insn-00aec310) · [`00aec320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec27c.md#insn-00aec320) · [`00aec32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec27c.md#insn-00aec32c)
- 新版 [`00aed314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed270.md#insn-00aed314)

~~~diff
- 00aec310 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aec310 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00aec310 bytes 680000b4
- 00aec320 ["INT_ADD", "register:40f0:8", ["const:aec320:8", "const:4:8"]]
- 00aec320 ["CALL", null, ["callee:0043bf04:8"]]
+ 00aed314 ["INT_ADD", "register:40f0:8", ["const:aed314:8", "const:4:8"]]
+ 00aed314 ["CALL", null, ["callee:0043bf04:8"]]
- 00aec320 bytes 313ee597
+ 00aed314 bytes fc3ae597
- 00aec32c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00aec32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aec32c bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ba6f6e9090b58df89e580d6cccc5714"></a>

### [`00aec348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec348.md) → [`00aed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed33c.md) FUN_00aed33c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aec5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec5c8.md) · 呼出先 7件 [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md) [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`006b223c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b223c.md) [`006b76ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b76ec.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00aed5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed5bc.md) · 呼出先 7件 [`0067e9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0067e/0067e9d8.md) [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`006b25ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b25ec.md) [`006b7a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b7/006b7a9c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.00% / 新版 55.00%

CFGの説明率　旧版 14.49% / 新版 14.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec34c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec348",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec34c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec350",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed33c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aed340",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aed344",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec348.md#insn-00aec348) · [`00aec34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec348.md#insn-00aec34c) · [`00aec350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec348.md#insn-00aec350)

~~~diff
- 00aec348 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aec348 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aec348 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aec348 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aec348 bytes fd7bbda9
- 00aec34c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aec34c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aec34c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aec34c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec34c bytes f65701a9
- 00aec350 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aec350 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aec350 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aec350 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec350 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6ecf6f4f0769635cbd9cf6f30034a6d"></a>

### [`00aec5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec5c8.md) → [`00aed5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed5bc.md) FUN_00aed5bc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00aec348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec348.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00aed33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed33c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aec5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec5c8.md#insn-00aec5d8)
- 新版 [`00aed5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed5bc.md#insn-00aed5cc)

~~~diff
- 00aec5d8 ["INT_ADD", "register:40f0:8", ["const:aec5d8:8", "const:4:8"]]
- 00aec5d8 ["CALL", null, ["callee:00aed33c:8"]]
+ 00aed5cc ["INT_ADD", "register:40f0:8", ["const:aed5cc:8", "const:4:8"]]
+ 00aed5cc ["CALL", null, ["callee:00aed33c:8"]]
- 00aec5d8 bytes 5cffff97
+ 00aed5cc bytes 5cffff97
~~~


<a id="compare-a3fd4975dcc36cb8e359c2374537732c"></a>

### [`00aec640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec640.md) → [`00aed634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed634.md) FUN_00aed634

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`005c0530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c0/005c0530.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`005c08e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c0/005c08e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 23.08% / 新版 22.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec6d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec7c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec808"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00aed6a8",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ],
    [
      "unmatched:00aec6d8",
      "DATA",
      [
        "storage",
        "00333be0",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00aed674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00aed6a8",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "qword"
      ]
    ],
    [
      "00aed6cc",
      "DATA",
      [
        "storage",
        "00333be0",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec640.md#insn-00aec680) · [`00aec68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec640.md#insn-00aec68c) · [`00aec6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec640.md#insn-00aec6d8)
- 新版 [`00aed680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed634.md#insn-00aed680)

~~~diff
- 00aec680 ["INT_ADD", "register:40f0:8", ["const:aec680:8", "const:4:8"]]
- 00aec680 ["CALL", null, ["ram:47ad34:8"]]
- 00aec680 bytes ad39e697
- 00aec68c ["INT_ADD", "register:40f0:8", ["const:aec68c:8", "const:4:8"]]
- 00aec68c ["CALL", null, ["callee:0047d134:8"]]
+ 00aed680 ["INT_ADD", "register:40f0:8", ["const:aed680:8", "const:4:8"]]
+ 00aed680 ["CALL", null, ["callee:0047d134:8"]]
- 00aec68c bytes e241e697
+ 00aed680 bytes ad3ee697
- 00aec6d8 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00aec6d8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aec6d8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00aec6d8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00aec6d8 bytes 146828b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6cef5cdd62c4076648a123a84581f3"></a>

### [`00aec9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9ac.md) → [`00aed9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9a0.md) FUN_00aed9a0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aed9c4",
      "incomplete_value": false,
      "site": "00aed9c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec9d0",
      "incomplete_value": false,
      "site": "00aec9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00aed9c4",
      "DATA",
      [
        "storage",
        "00c8dac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aed9c4",
      "DATA",
      [
        "storage",
        "00c8ea98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9ac.md#insn-00aec9c0) · [`00aec9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9ac.md#insn-00aec9c8) · [`00aec9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9ac.md#insn-00aec9cc)
- 新版 [`00aed9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9a0.md#insn-00aed9b4) · [`00aed9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9a0.md#insn-00aed9bc) · [`00aed9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9a0.md#insn-00aed9c0)

~~~diff
- 00aec9c0 ["INT_ADD", "register:40f0:8", ["const:aec9c0:8", "const:4:8"]]
- 00aec9c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00aed9b4 ["INT_ADD", "register:40f0:8", ["const:aed9b4:8", "const:4:8"]]
+ 00aed9b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00aec9c0 bytes 68ad0594
+ 00aed9b4 bytes 5fad0594
- 00aec9c8 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00aed9bc ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00aec9c8 bytes 080d00b0
+ 00aed9bc bytes 080d00b0
- 00aec9cc ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00aec9cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec9cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec9cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed9c0 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00aed9c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed9c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed9c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec9cc bytes 08212b91
+ 00aed9c0 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-372955afb88e43feae3068d9206197da"></a>

### [`00aec9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md) → [`00aed9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aed/00aed9f0.md) FUN_00aed9f0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 29件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 0件  · 呼出先 29件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.29% / 新版 82.29%

CFGの説明率　旧版 38.02% / 新版 36.80%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 2件, `store_condition` 3件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeca10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeca10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeca14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeca10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeca14",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeca24",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeda04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeda08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aeda18",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeca10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md#insn-00aeca10) · [`00aeca14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md#insn-00aeca14) · [`00aeca24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec9fc.md#insn-00aeca24)

~~~diff
- 00aeca10 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aeca10 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aeca10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00aeca10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeca10 bytes f65712a9
- 00aeca14 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeca14 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeca14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00aeca14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeca14 bytes f44f13a9
- 00aeca24 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aeca24 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00aeca24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aeca24 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8d560c00fe486e107e67c282d8f464d"></a>

### [`00aed408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed408.md) → [`00aee3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee3fc.md) FUN_00aee3fc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aee420",
      "incomplete_value": false,
      "site": "00aee420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed42c",
      "incomplete_value": false,
      "site": "00aed42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00aee420",
      "DATA",
      [
        "storage",
        "00c8db48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aee420",
      "DATA",
      [
        "storage",
        "00c8eb18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed408.md#insn-00aed41c) · [`00aed424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed408.md#insn-00aed424) · [`00aed428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed408.md#insn-00aed428)
- 新版 [`00aee410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee3fc.md#insn-00aee410) · [`00aee418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee3fc.md#insn-00aee418) · [`00aee41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee3fc.md#insn-00aee41c)

~~~diff
- 00aed41c ["INT_ADD", "register:40f0:8", ["const:aed41c:8", "const:4:8"]]
- 00aed41c ["CALL", null, ["callee:00c58f30:8"]]
+ 00aee410 ["INT_ADD", "register:40f0:8", ["const:aee410:8", "const:4:8"]]
+ 00aee410 ["CALL", null, ["callee:00c58f30:8"]]
- 00aed41c bytes d1aa0594
+ 00aee410 bytes c8aa0594
- 00aed424 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00aee418 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00aed424 bytes 080d0090
+ 00aee418 bytes 080d0090
- 00aed428 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00aed428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee41c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00aee41c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee41c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee41c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed428 bytes 08212d91
+ 00aee41c bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb2ca4c3a0befcbf128326100674e02a"></a>

### [`00aed6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed6ec.md) → [`00aee6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee6e0.md) FUN_00aee6e0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a46944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46944.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`00a47938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47938.md) [`00a47c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 45.45% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aee758"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed710"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aed710",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00aed718",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aee718"
      ]
    ],
    [
      "00aee710",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00aee704",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00aee70c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aee718"
      ]
    ],
    [
      "00aee710",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed6ec.md#insn-00aed710) · [`00aed71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed6ec.md#insn-00aed71c) · [`00aed764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed6ec.md#insn-00aed764)
- 新版 [`00aee710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee6e0.md#insn-00aee710)

~~~diff
- 00aed710 ["INT_ADD", "register:40f0:8", ["const:aed710:8", "const:4:8"]]
- 00aed710 ["CALL", null, ["ram:47ad34:8"]]
- 00aed710 bytes 8935e697
- 00aed71c ["INT_ADD", "register:40f0:8", ["const:aed71c:8", "const:4:8"]]
- 00aed71c ["CALL", null, ["ram:47ad34:8"]]
+ 00aee710 ["INT_ADD", "register:40f0:8", ["const:aee710:8", "const:4:8"]]
+ 00aee710 ["CALL", null, ["ram:47b054:8"]]
- 00aed71c bytes 8635e697
+ 00aee710 bytes 5132e697
- 00aed764 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00aed764 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00aed764 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00aed764 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00aed764 bytes 14692a38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da3df6bc8f19c00a4cc1bb750c916543"></a>

### [`00aed814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed814.md) → [`00aee808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee808.md) FUN_00aee808

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e3140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3140.md) [`00ae08cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae0/00ae08cc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e40ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e4/009e40ec.md) [`00ae18c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae1/00ae18c0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 52.17% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed838"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aee838",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aed844",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00aee860",
      "value": [
        "leaf",
        "ram:ae18c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aed86c",
      "value": [
        "leaf",
        "ram:ae08cc:8"
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
      "unmatched:00aed838",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00aed840",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aee840"
      ]
    ],
    [
      "00aee838",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00aee82c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00aee834",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aee840"
      ]
    ],
    [
      "00aee838",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed814.md#insn-00aed838) · [`00aed844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed814.md#insn-00aed844) · [`00aed86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed814.md#insn-00aed86c)
- 新版 [`00aee838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee808.md#insn-00aee838) · [`00aee860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee808.md#insn-00aee860)

~~~diff
- 00aed838 ["INT_ADD", "register:40f0:8", ["const:aed838:8", "const:4:8"]]
- 00aed838 ["CALL", null, ["ram:47ad34:8"]]
- 00aed838 bytes 3f35e697
- 00aed844 ["INT_ADD", "register:40f0:8", ["const:aed844:8", "const:4:8"]]
- 00aed844 ["CALL", null, ["ram:47ad34:8"]]
+ 00aee838 ["INT_ADD", "register:40f0:8", ["const:aee838:8", "const:4:8"]]
+ 00aee838 ["CALL", null, ["ram:47b054:8"]]
- 00aed844 bytes 3c35e697
+ 00aee838 bytes 0732e697
- 00aed86c ["INT_ADD", "register:40f0:8", ["const:aed86c:8", "const:4:8"]]
- 00aed86c ["CALL", null, ["ram:ae08cc:8"]]
+ 00aee860 ["INT_ADD", "register:40f0:8", ["const:aee860:8", "const:4:8"]]
+ 00aee860 ["CALL", null, ["ram:ae18c0:8"]]
- 00aed86c bytes 18ccff97
+ 00aee860 bytes 18ccff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79ec7f07cfee8706452f3199a61fad4"></a>

### [`00aed99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed99c.md) → [`00aee990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee990.md) FUN_00aee990

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aee9b4",
      "incomplete_value": false,
      "site": "00aee9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed9c0",
      "incomplete_value": false,
      "site": "00aed9c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00aee9b4",
      "DATA",
      [
        "storage",
        "00c8dcc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aee9b4",
      "DATA",
      [
        "storage",
        "00c8ec98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed99c.md#insn-00aed9b0) · [`00aed9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed99c.md#insn-00aed9b8) · [`00aed9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed99c.md#insn-00aed9bc)
- 新版 [`00aee9a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee990.md#insn-00aee9a4) · [`00aee9ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee990.md#insn-00aee9ac) · [`00aee9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee990.md#insn-00aee9b0)

~~~diff
- 00aed9b0 ["INT_ADD", "register:40f0:8", ["const:aed9b0:8", "const:4:8"]]
- 00aed9b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00aee9a4 ["INT_ADD", "register:40f0:8", ["const:aee9a4:8", "const:4:8"]]
+ 00aee9a4 ["CALL", null, ["callee:00c58f30:8"]]
- 00aed9b0 bytes 6ca90594
+ 00aee9a4 bytes 63a90594
- 00aed9b8 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00aee9ac ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00aed9b8 bytes 080d0090
+ 00aee9ac bytes 080d0090
- 00aed9bc ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00aed9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee9b0 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00aee9b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee9b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee9b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed9bc bytes 08213391
+ 00aee9b0 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3db88a67dd5e4d5bdf149cfacc8434"></a>

### [`00aed9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed9ec.md) → [`00aee9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee9e0.md) FUN_00aee9e0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.56% / 新版 88.56%

CFGの説明率　旧版 22.22% / 新版 21.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeda84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeda88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeda8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeea08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeda70"
      ]
    ],
    [
      "00aeea10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeda40"
      ]
    ],
    [
      "00aeea18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00aeea08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeea64"
      ]
    ],
    [
      "00aeea10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeea34"
      ]
    ],
    [
      "00aeea18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeda24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed9ec.md#insn-00aeda24) · [`00aeda40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed9ec.md#insn-00aeda40) · [`00aeda50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aed9ec.md#insn-00aeda50)
- 新版 [`00aeea18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aee9e0.md#insn-00aeea18)

~~~diff
- 00aeda24 ["INT_ADD", "register:40f0:8", ["const:aeda24:8", "const:4:8"]]
- 00aeda24 ["CALL", null, ["ram:47ad34:8"]]
+ 00aeea18 ["INT_ADD", "register:40f0:8", ["const:aeea18:8", "const:4:8"]]
+ 00aeea18 ["CALL", null, ["ram:47b054:8"]]
- 00aeda24 bytes c434e697
+ 00aeea18 bytes 8f31e697
- 00aeda40 ["INT_ADD", "register:40f0:8", ["const:aeda40:8", "const:4:8"]]
- 00aeda40 ["CALL", null, ["ram:47ad34:8"]]
- 00aeda40 bytes bd34e697
- 00aeda50 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aeda50 ["CBRANCH", null, ["local:b55:8", "tmp:0:1"]]
- 00aeda50 bytes e11a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc00d4b487654b5368bb538cae7c2939"></a>

### [`00aede60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aede60.md) → [`00aeee54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aeee54.md) FUN_00aeee54

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aeee60",
      "incomplete_value": false,
      "site": "00aeee60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aede6c",
      "incomplete_value": false,
      "site": "00aede6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00aeee60",
      "DATA",
      [
        "storage",
        "00c8dd38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeee60",
      "DATA",
      [
        "storage",
        "00c8ed08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aede64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aede60.md#insn-00aede64) · [`00aede68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aed/00aede60.md#insn-00aede68)
- 新版 [`00aeee58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aeee54.md#insn-00aeee58) · [`00aeee5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aee/00aeee54.md#insn-00aeee5c)

~~~diff
- 00aede64 ["COPY", "register:4048:8", ["const:c8d000:8"]]
+ 00aeee58 ["COPY", "register:4048:8", ["const:c8e000:8"]]
- 00aede64 bytes 090d0090
+ 00aeee58 bytes 090d0090
- 00aede68 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00aede68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aede68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aede68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aeee5c ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00aeee5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aeee5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aeee5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aede68 bytes 29e13491
+ 00aeee5c bytes 29213491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05a36ed130f13781541023bc1e2b61d1"></a>

### [`00aee904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aee904.md) → [`00aef8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aef8f8.md) FUN_00aef8f8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`00492480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.74% / 新版 69.74%

CFGの説明率　旧版 25.00% / 新版 27.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee9a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee908",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aef974"
      ]
    ],
    [
      "unmatched:00aee930",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aee954"
      ]
    ]
  ],
  "added": [
    [
      "00aef8fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aef91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aef974"
      ]
    ],
    [
      "00aef924",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aef948"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aee904.md#insn-00aee908) · [`00aee928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aee904.md#insn-00aee928) · [`00aee930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aee904.md#insn-00aee930)

~~~diff
- 00aee908 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aee908 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aee908 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00aee908 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee908 bytes fd7b04a9
- 00aee928 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00aee928 bytes c0020054
- 00aee930 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00aee930 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9e13891e7d39bfb5ef3de0faf37234"></a>

### [`00aeeaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeaec.md) → [`00aefae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefae0.md) FUN_00aefae0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b98a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98a8.md) [`008bb568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bb568.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008ba854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba854.md) [`008bc514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bc514.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeeb08"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aefb18",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aeeb24",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00aefafc"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeeb08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00aefb18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00aefafc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00aefb18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeeb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeaec.md#insn-00aeeb08) · [`00aeeb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeaec.md#insn-00aeeb24)
- 新版 [`00aefb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefae0.md#insn-00aefb18) · [`00aefafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefae0.md#insn-00aefafc)

~~~diff
- 00aeeb08 ["INT_ADD", "register:40f0:8", ["const:aeeb08:8", "const:4:8"]]
- 00aeeb08 ["CALL", null, ["ram:47ad34:8"]]
- 00aeeb08 bytes 8b30e697
- 00aeeb24 ["INT_ADD", "register:40f0:8", ["const:aeeb24:8", "const:4:8"]]
- 00aeeb24 ["CALL", null, ["ram:47ad34:8"]]
+ 00aefb18 ["INT_ADD", "register:40f0:8", ["const:aefb18:8", "const:4:8"]]
+ 00aefb18 ["CALL", null, ["ram:47b054:8"]]
- 00aeeb24 bytes 8430e697
+ 00aefb18 bytes 4f2de697
+ 00aefafc ["INT_ADD", "register:40f0:8", ["const:aefafc:8", "const:4:8"]]
+ 00aefafc ["CALL", null, ["ram:47b054:8"]]
+ 00aefafc bytes 562de697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e14027bb398c8434ee35fc55ffd297e"></a>

### [`00aeeb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeb94.md) → [`00aefb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefb88.md) FUN_00aefb88

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aefb9c",
      "incomplete_value": false,
      "site": "00aefba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeeba8",
      "incomplete_value": false,
      "site": "00aeebac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "00aefba0",
      "DATA",
      [
        "storage",
        "00c8dea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aefba0",
      "DATA",
      [
        "storage",
        "00c8ee78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeeba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeb94.md#insn-00aeeba0) · [`00aeeba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeb94.md#insn-00aeeba4) · [`00aeeba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeb94.md#insn-00aeeba8)
- 新版 [`00aefb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefb88.md#insn-00aefb94) · [`00aefb98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefb88.md#insn-00aefb98) · [`00aefb9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefb88.md#insn-00aefb9c)

~~~diff
- 00aeeba0 ["INT_ADD", "register:40f0:8", ["const:aeeba0:8", "const:4:8"]]
- 00aeeba0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00aefb94 ["INT_ADD", "register:40f0:8", ["const:aefb94:8", "const:4:8"]]
+ 00aefb94 ["CALL", null, ["callee:00c58f30:8"]]
- 00aeeba0 bytes f0a40594
+ 00aefb94 bytes e7a40594
- 00aeeba4 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00aefb98 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00aeeba4 bytes e80c00f0
+ 00aefb98 bytes e80c00f0
- 00aeeba8 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 00aeeba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeeba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeeba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aefb9c ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 00aefb9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aefb9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aefb9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeeba8 bytes 08a13a91
+ 00aefb9c bytes 08e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd9276f0a604d1538f621c33361e8c6"></a>

### [`00aeebd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeebd0.md) → [`00aefbc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefbc4.md) FUN_00aefbc4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00aefbe0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aeebec",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00aefbe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00aefbe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeebec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeebd0.md#insn-00aeebec) · [`00aeebf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeebd0.md#insn-00aeebf8)
- 新版 [`00aefbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefbc4.md#insn-00aefbe0) · [`00aefbec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefbc4.md#insn-00aefbec)

~~~diff
- 00aeebec ["INT_ADD", "register:40f0:8", ["const:aeebec:8", "const:4:8"]]
- 00aeebec ["CALL", null, ["ram:47ad34:8"]]
+ 00aefbe0 ["INT_ADD", "register:40f0:8", ["const:aefbe0:8", "const:4:8"]]
+ 00aefbe0 ["CALL", null, ["ram:47b054:8"]]
- 00aeebec bytes 5230e697
+ 00aefbe0 bytes 1d2de697
- 00aeebf8 ["INT_ADD", "register:40f0:8", ["const:aeebf8:8", "const:4:8"]]
- 00aeebf8 ["CALL", null, ["callee:0047d134:8"]]
+ 00aefbec ["INT_ADD", "register:40f0:8", ["const:aefbec:8", "const:4:8"]]
+ 00aefbec ["CALL", null, ["callee:0047d134:8"]]
- 00aeebf8 bytes 8738e697
+ 00aefbec bytes 5235e697
~~~


<a id="compare-81f4c1a124b1a3d51e0b5e63a2c2406e"></a>

### [`00aeec8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeec8c.md) → [`00aefc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefc80.md) FUN_00aefc80

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046db2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db2c.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046de4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de4c.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 64.29% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeecb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aefca8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aefcd8",
      "incomplete_value": true,
      "site": "00aefcd8",
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
      "definition_site": "00aeece4",
      "incomplete_value": true,
      "site": "00aeece4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeecb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aefcd4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00aefce0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00aefca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00aefcd4",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00aefce0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeecb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeec8c.md#insn-00aeecb4) · [`00aeecc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeec8c.md#insn-00aeecc8) · [`00aeece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeec8c.md#insn-00aeece4)
- 新版 [`00aefcbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefc80.md#insn-00aefcbc) · [`00aefcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefc80.md#insn-00aefcd8)

~~~diff
- 00aeecb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aeecb4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aeecb4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aeecb4 bytes a8831ff8
- 00aeecc8 ["INT_ADD", "register:40f0:8", ["const:aeecc8:8", "const:4:8"]]
- 00aeecc8 ["CALL", null, ["callee:008ba294:8"]]
+ 00aefcbc ["INT_ADD", "register:40f0:8", ["const:aefcbc:8", "const:4:8"]]
+ 00aefcbc ["CALL", null, ["callee:008ba294:8"]]
- 00aeecc8 bytes 8829f797
+ 00aefcbc bytes 7629f797
- 00aeece4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00aeece4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00aefcd8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00aefcd8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aeece4 bytes 200100b4
+ 00aefcd8 bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcfd0d8a05c13b760e1c996355e1ad5a"></a>

### [`00aeef94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeef94.md) → [`00aeff88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aeff88.md) FUN_00aeff88

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) [`00aef154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef154.md) [`00aef158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef158.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0065919c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00659/0065919c.md) [`00af0148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0148.md) [`00af014c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af014c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.48% / 新版 85.48%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef024"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeffbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00aeffd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00aef020",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeffbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00aeffd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00af0014",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeefc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeef94.md#insn-00aeefc8) · [`00aeefe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeef94.md#insn-00aeefe4) · [`00aef020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeef94.md#insn-00aef020)
- 新版 [`00aeffbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aeff88.md#insn-00aeffbc) · [`00aeffd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aeff88.md#insn-00aeffd8)

~~~diff
- 00aeefc8 ["INT_ADD", "register:40f0:8", ["const:aeefc8:8", "const:4:8"]]
- 00aeefc8 ["CALL", null, ["ram:47ad34:8"]]
+ 00aeffbc ["INT_ADD", "register:40f0:8", ["const:aeffbc:8", "const:4:8"]]
+ 00aeffbc ["CALL", null, ["ram:47b054:8"]]
- 00aeefc8 bytes 5b2fe697
+ 00aeffbc bytes 262ce697
- 00aeefe4 ["INT_ADD", "register:40f0:8", ["const:aeefe4:8", "const:4:8"]]
- 00aeefe4 ["CALL", null, ["ram:47ad34:8"]]
+ 00aeffd8 ["INT_ADD", "register:40f0:8", ["const:aeffd8:8", "const:4:8"]]
+ 00aeffd8 ["CALL", null, ["ram:47b054:8"]]
- 00aeefe4 bytes 542fe697
+ 00aeffd8 bytes 1f2ce697
- 00aef020 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00aef020 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aef020 bytes f31300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79ca25657268b3468f6b31f05e198af9"></a>

### [`00aef1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef1e8.md) → [`00af01dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af01dc.md) FUN_00af01dc

採用 · 移動量 `+0xff4` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 33件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md)
- 新版 呼出元 0件  · 呼出先 33件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.11% / 新版 87.11%

CFGの説明率　旧版 32.63% / 新版 31.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef2d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef2f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef2f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af021c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aef24c"
      ]
    ],
    [
      "00af0224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00aef24c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00af021c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af0240"
      ]
    ],
    [
      "00af0224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00af0240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef1e8.md#insn-00aef2d8) · [`00aef2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef1e8.md#insn-00aef2f8) · [`00aef330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef1e8.md#insn-00aef330)

~~~diff
- 00aef2d8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aef2d8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:9:8"]]
- 00aef2d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aef2d8 bytes e99300f8
- 00aef2f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aef2f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aef2f8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00aef2f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef2f8 bytes a84f3ca9
- 00aef330 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aef330 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aef330 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff90:8"]]
- 00aef330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef330 bytes a84f39a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a1eee73503d1fb3eb0c70d67a1a187"></a>

### [`00aef94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef94c.md) → [`00af0940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0940.md) FUN_00af0940

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af094c",
      "incomplete_value": false,
      "site": "00af094c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aef958",
      "incomplete_value": false,
      "site": "00aef958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "00af094c",
      "DATA",
      [
        "storage",
        "00c8e138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af094c",
      "DATA",
      [
        "storage",
        "00c8f108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef94c.md#insn-00aef950) · [`00aef954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef94c.md#insn-00aef954)
- 新版 [`00af0944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0940.md#insn-00af0944) · [`00af0948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0940.md#insn-00af0948)

~~~diff
- 00aef950 ["COPY", "register:4048:8", ["const:c8e000:8"]]
+ 00af0944 ["COPY", "register:4048:8", ["const:c8f000:8"]]
- 00aef950 bytes e90c00f0
+ 00af0944 bytes e90c00f0
- 00aef954 ["COPY", "tmp:0:8", ["const:138:8"]]
- 00aef954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aef954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aef954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af0948 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00af0948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aef954 bytes 29e10491
+ 00af0948 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b090db83d5e7cc5d881eb7e5e49ff398"></a>

### [`00aef968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef968.md) → [`00af095c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af095c.md) FUN_00af095c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.72% / 新版 87.72%

CFGの説明率　旧版 29.17% / 新版 29.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef96c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aef968",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aef96c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aef9b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00af095c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af0960",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af09a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef968.md#insn-00aef968) · [`00aef96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef968.md#insn-00aef96c) · [`00aef9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aef968.md#insn-00aef9b0)

~~~diff
- 00aef968 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aef968 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aef968 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aef968 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aef968 bytes fd7bbea9
- 00aef96c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aef96c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aef96c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aef96c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef96c bytes f44f01a9
- 00aef9b0 ["INT_ADD", "register:40f0:8", ["const:aef9b0:8", "const:4:8"]]
- 00aef9b0 ["CALL", null, ["ram:47ad34:8"]]
- 00aef9b0 bytes e12ce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8fd5b3122b814ecf2bed6cb1b8cb75f"></a>

### [`00aefaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefaac.md) → [`00af0aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0aa0.md) FUN_00af0aa0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0aac",
      "incomplete_value": false,
      "site": "00af0aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aefab8",
      "incomplete_value": false,
      "site": "00aefab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "00af0aac",
      "DATA",
      [
        "storage",
        "00c8e1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0aac",
      "DATA",
      [
        "storage",
        "00c8f188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefaac.md#insn-00aefab0) · [`00aefab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefaac.md#insn-00aefab4)
- 新版 [`00af0aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0aa0.md#insn-00af0aa4) · [`00af0aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0aa0.md#insn-00af0aa8)

~~~diff
- 00aefab0 ["COPY", "register:4048:8", ["const:c8e000:8"]]
+ 00af0aa4 ["COPY", "register:4048:8", ["const:c8f000:8"]]
- 00aefab0 bytes e90c00f0
+ 00af0aa4 bytes e90c00f0
- 00aefab4 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00aefab4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aefab4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aefab4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af0aa8 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00af0aa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0aa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0aa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aefab4 bytes 29e10691
+ 00af0aa8 bytes 29210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-902659b7eb045df32f3541c9cde79c60"></a>

### [`00aefac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefac8.md) → [`00af0abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0abc.md) FUN_00af0abc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b7a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7a60.md) [`008b7f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f14.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af0ad0",
      "incomplete_value": true,
      "site": "00af0ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aefadc",
      "incomplete_value": true,
      "site": "00aefae0",
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
            "const:2f38:8"
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
    "new": null,
    "old": {
      "definition_site": "00aefad8",
      "incomplete_value": false,
      "site": "00aefae0",
      "value": [
        "leaf",
        "const:326:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aefae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefac8.md#insn-00aefae0) · [`00aefadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefac8.md#insn-00aefadc) · [`00aefae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefac8.md#insn-00aefae8)
- 新版 [`00af0ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0abc.md#insn-00af0ad4) · [`00af0adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0abc.md#insn-00af0adc)

~~~diff
- 00aefae0 ["INT_ADD", "register:40f0:8", ["const:aefae0:8", "const:4:8"]]
- 00aefae0 ["CALL", null, ["callee:008b89cc:8"]]
+ 00af0ad4 ["INT_ADD", "register:40f0:8", ["const:af0ad4:8", "const:4:8"]]
+ 00af0ad4 ["CALL", null, ["callee:008b89cc:8"]]
- 00aefae0 bytes d01ff797
+ 00af0ad4 bytes be1ff797
- 00aefadc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aefadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aefadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aefadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aefadc bytes 0001098b
- 00aefae8 ["INT_ADD", "register:40f0:8", ["const:aefae8:8", "const:4:8"]]
- 00aefae8 ["CALL", null, ["callee:008b7f14:8"]]
+ 00af0adc ["INT_ADD", "register:40f0:8", ["const:af0adc:8", "const:4:8"]]
+ 00af0adc ["CALL", null, ["callee:008b7f14:8"]]
- 00aefae8 bytes 201df797
+ 00af0adc bytes 0e1df797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23ae323836b1d9ee3fbaa7d508e3ffda"></a>

### [`00aefb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefb74.md) → [`00af0b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0b68.md) FUN_00af0b68

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`008b6df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6df4.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`008b7da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7da0.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 10.53% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af0bb8",
      "incomplete_value": true,
      "site": "00af0bb8",
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
      "definition_site": "00aefbc4",
      "incomplete_value": true,
      "site": "00aefbc4",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefd88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefd90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af0bb4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aefbcc",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00aefbd4",
      "PARAM",
      [
        "storage",
        "00c8da20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00af0bb4",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "00af0bc0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00af0bc8",
      "PARAM",
      [
        "storage",
        "00c8e9f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefb74.md#insn-00aefba0) · [`00aefbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefb74.md#insn-00aefbdc) · [`00aefc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefb74.md#insn-00aefc1c)
- 新版 [`00af0b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0b68.md#insn-00af0b94) · [`00af0bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0b68.md#insn-00af0bd0) · [`00af0c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0b68.md#insn-00af0c10)

~~~diff
- 00aefba0 ["INT_ADD", "register:40f0:8", ["const:aefba0:8", "const:4:8"]]
- 00aefba0 ["CALL", null, ["callee:008ba294:8"]]
+ 00af0b94 ["INT_ADD", "register:40f0:8", ["const:af0b94:8", "const:4:8"]]
+ 00af0b94 ["CALL", null, ["callee:008ba294:8"]]
- 00aefba0 bytes d225f797
+ 00af0b94 bytes c025f797
- 00aefbdc ["INT_ADD", "register:40f0:8", ["const:aefbdc:8", "const:4:8"]]
- 00aefbdc ["CALL", null, ["callee:00c596b0:8"]]
+ 00af0bd0 ["INT_ADD", "register:40f0:8", ["const:af0bd0:8", "const:4:8"]]
+ 00af0bd0 ["CALL", null, ["callee:00c596b0:8"]]
- 00aefbdc bytes c1a20594
+ 00af0bd0 bytes b8a20594
- 00aefc1c ["INT_ADD", "register:40f0:8", ["const:aefc1c:8", "const:4:8"]]
- 00aefc1c ["CALL", null, ["callee:008ba810:8"]]
+ 00af0c10 ["INT_ADD", "register:40f0:8", ["const:af0c10:8", "const:4:8"]]
+ 00af0c10 ["CALL", null, ["callee:008ba810:8"]]
- 00aefc1c bytes 1227f797
+ 00af0c10 bytes 0027f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034c50d3b0b5e694d955317069c63de3"></a>

### [`00aefeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefeb0.md) → [`00af0ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0ea4.md) FUN_00af0ea4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0ec4",
      "incomplete_value": false,
      "site": "00af0ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aefed0",
      "incomplete_value": false,
      "site": "00aefed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
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
      "00af0ec8",
      "DATA",
      [
        "storage",
        "00c8e2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0ec8",
      "DATA",
      [
        "storage",
        "00c8f288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefeb0.md#insn-00aefec4) · [`00aefecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefeb0.md#insn-00aefecc) · [`00aefed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefeb0.md#insn-00aefed0)
- 新版 [`00af0eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0ea4.md#insn-00af0eb8) · [`00af0ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0ea4.md#insn-00af0ec0) · [`00af0ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0ea4.md#insn-00af0ec4)

~~~diff
- 00aefec4 ["INT_ADD", "register:40f0:8", ["const:aefec4:8", "const:4:8"]]
- 00aefec4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00af0eb8 ["INT_ADD", "register:40f0:8", ["const:af0eb8:8", "const:4:8"]]
+ 00af0eb8 ["CALL", null, ["callee:00c58f30:8"]]
- 00aefec4 bytes 27a00594
+ 00af0eb8 bytes 1ea00594
- 00aefecc ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00af0ec0 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00aefecc bytes e80c00f0
+ 00af0ec0 bytes e80c00f0
- 00aefed0 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00aefed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aefed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aefed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af0ec4 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 00af0ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aefed0 bytes 08e10a91
+ 00af0ec4 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca845f003fffd097ba09929567fffada"></a>

### [`00aefee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefee8.md) → [`00af0edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0edc.md) FUN_00af0edc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0ee0",
      "incomplete_value": false,
      "site": "00af0ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aefeec",
      "incomplete_value": false,
      "site": "00aefef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
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
      "00af0ee4",
      "DATA",
      [
        "storage",
        "00c8e2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0ee4",
      "DATA",
      [
        "storage",
        "00c8f288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefee8.md#insn-00aefee8) · [`00aefeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefee8.md#insn-00aefeec)
- 新版 [`00af0edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0edc.md#insn-00af0edc) · [`00af0ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0edc.md#insn-00af0ee0)

~~~diff
- 00aefee8 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00af0edc ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00aefee8 bytes e80c00f0
+ 00af0edc bytes e80c00f0
- 00aefeec ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00aefeec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aefeec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aefeec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af0ee0 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 00af0ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aefeec bytes 08e10a91
+ 00af0ee0 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed18d3ba671b44e153fb0cf9b4aa59f"></a>

### [`00aeff08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md) → [`00af0efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0efc.md) FUN_00af0efc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`008b97f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b97f8.md) [`00a46944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46944.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`008ba7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba7a4.md) [`00a47938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47938.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 20.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeff28"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeff50"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aeffa4",
      "incomplete_value": true,
      "site": "00aeffac",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00aeff28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00aeff50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00af0f1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00af0f44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeff28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md#insn-00aeff28) · [`00aeff50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md#insn-00aeff50) · [`00aeffac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md#insn-00aeffac)
- 新版 [`00af0fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0efc.md#insn-00af0fa0)

~~~diff
- 00aeff28 ["INT_ADD", "register:40f0:8", ["const:aeff28:8", "const:4:8"]]
- 00aeff28 ["CALL", null, ["ram:47ad34:8"]]
- 00aeff28 bytes 832be697
- 00aeff50 ["INT_ADD", "register:40f0:8", ["const:aeff50:8", "const:4:8"]]
- 00aeff50 ["CALL", null, ["ram:47ad34:8"]]
- 00aeff50 bytes 792be697
- 00aeffac ["INT_ADD", "register:40f0:8", ["const:aeffac:8", "const:4:8"]]
- 00aeffac ["CALL", null, ["callee:008ba7a4:8"]]
+ 00af0fa0 ["INT_ADD", "register:40f0:8", ["const:af0fa0:8", "const:4:8"]]
+ 00af0fa0 ["CALL", null, ["callee:008ba7a4:8"]]
- 00aeffac bytes 1326f797
+ 00af0fa0 bytes 0126f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d87c004e551aba7a1627b426bd9d0bb2"></a>

### [`00af001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af001c.md) → [`00af1010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1010.md) FUN_00af1010

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1030",
      "incomplete_value": false,
      "site": "00af1034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af003c",
      "incomplete_value": false,
      "site": "00af0040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "00af1034",
      "DATA",
      [
        "storage",
        "00c8e348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1034",
      "DATA",
      [
        "storage",
        "00c8f318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af001c.md#insn-00af0030) · [`00af0038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af001c.md#insn-00af0038) · [`00af003c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af001c.md#insn-00af003c)
- 新版 [`00af1024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1010.md#insn-00af1024) · [`00af102c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1010.md#insn-00af102c) · [`00af1030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1010.md#insn-00af1030)

~~~diff
- 00af0030 ["INT_ADD", "register:40f0:8", ["const:af0030:8", "const:4:8"]]
- 00af0030 ["CALL", null, ["callee:00c58f30:8"]]
+ 00af1024 ["INT_ADD", "register:40f0:8", ["const:af1024:8", "const:4:8"]]
+ 00af1024 ["CALL", null, ["callee:00c58f30:8"]]
- 00af0030 bytes cc9f0594
+ 00af1024 bytes c39f0594
- 00af0038 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00af102c ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00af0038 bytes e80c00d0
+ 00af102c bytes e80c00d0
- 00af003c ["COPY", "tmp:0:8", ["const:348:8"]]
- 00af003c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af003c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af003c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1030 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 00af1030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af003c bytes 08210d91
+ 00af1030 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bee5613b5444b3b7249b19d7994af8f"></a>

### [`00af0074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0074.md) → [`00af1068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1068.md) FUN_00af1068

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa8.md) [`00b0b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f54.md) [`00b0c6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0c/00b0c6d0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 41.67% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af00a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af10a0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af00ac",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00af1094"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af1090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af10c8"
      ]
    ],
    [
      "unmatched:00af00a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00af00a8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00af10c4"
      ]
    ]
  ],
  "added": [
    [
      "00af1090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af110c"
      ]
    ],
    [
      "00af1094",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00af109c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00af10c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af00a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0074.md#insn-00af00a0) · [`00af00ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0074.md#insn-00af00ac)
- 新版 [`00af10a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1068.md#insn-00af10a0) · [`00af1094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1068.md#insn-00af1094)

~~~diff
- 00af00a0 ["INT_ADD", "register:40f0:8", ["const:af00a0:8", "const:4:8"]]
- 00af00a0 ["CALL", null, ["ram:47ad34:8"]]
- 00af00a0 bytes 252be697
- 00af00ac ["INT_ADD", "register:40f0:8", ["const:af00ac:8", "const:4:8"]]
- 00af00ac ["CALL", null, ["ram:47ad34:8"]]
+ 00af10a0 ["INT_ADD", "register:40f0:8", ["const:af10a0:8", "const:4:8"]]
+ 00af10a0 ["CALL", null, ["ram:47b054:8"]]
- 00af00ac bytes 222be697
+ 00af10a0 bytes ed27e697
+ 00af1094 ["INT_ADD", "register:40f0:8", ["const:af1094:8", "const:4:8"]]
+ 00af1094 ["CALL", null, ["ram:47b054:8"]]
+ 00af1094 bytes f027e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f68c7ebddb9c517f5a7ee085c55ae7bf"></a>

### [`00af01a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md) → [`00af1198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1198.md) FUN_00af1198

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`00744260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`00744610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00744/00744610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.46% / 新版 79.46%

CFGの説明率　旧版 22.22% / 新版 20.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af01b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af01b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af01bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af01b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af01bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af01cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af11ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af11b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af11c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af01b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md#insn-00af01b8) · [`00af01bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md#insn-00af01bc) · [`00af01cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af01a4.md#insn-00af01cc)

~~~diff
- 00af01b8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af01b8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af01b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00af01b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af01b8 bytes f6570ba9
- 00af01bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af01bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af01bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00af01bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af01bc bytes f44f0ca9
- 00af01cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af01cc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00af01cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af01cc bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-712ae134f24c9f066ad510237cfbcc78"></a>

### [`00af0680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0680.md) → [`00af1674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1674.md) FUN_00af1674

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1678",
      "incomplete_value": false,
      "site": "00af167c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0684",
      "incomplete_value": false,
      "site": "00af0688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00af167c",
      "DATA",
      [
        "storage",
        "00c8e438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af167c",
      "DATA",
      [
        "storage",
        "00c8f408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0680.md#insn-00af0680) · [`00af0684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0680.md#insn-00af0684)
- 新版 [`00af1674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1674.md#insn-00af1674) · [`00af1678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1674.md#insn-00af1678)

~~~diff
- 00af0680 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00af1674 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00af0680 bytes e80c00d0
+ 00af1674 bytes e80c00d0
- 00af0684 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00af0684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af0684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af0684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1678 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00af1678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af0684 bytes 08e11091
+ 00af1678 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de186e72d673de0af2db4b27857dbf38"></a>

### [`00af0698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0698.md) → [`00af168c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af168c.md) FUN_00af168c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00af16b0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af06bc",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00af16b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00af16b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af06bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0698.md#insn-00af06bc) · [`00af06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0698.md#insn-00af06c8)
- 新版 [`00af16b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af168c.md#insn-00af16b0) · [`00af16bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af168c.md#insn-00af16bc)

~~~diff
- 00af06bc ["INT_ADD", "register:40f0:8", ["const:af06bc:8", "const:4:8"]]
- 00af06bc ["CALL", null, ["ram:47ad34:8"]]
+ 00af16b0 ["INT_ADD", "register:40f0:8", ["const:af16b0:8", "const:4:8"]]
+ 00af16b0 ["CALL", null, ["ram:47b054:8"]]
- 00af06bc bytes 9e29e697
+ 00af16b0 bytes 6926e697
- 00af06c8 ["INT_ADD", "register:40f0:8", ["const:af06c8:8", "const:4:8"]]
- 00af06c8 ["CALL", null, ["callee:0047d134:8"]]
+ 00af16bc ["INT_ADD", "register:40f0:8", ["const:af16bc:8", "const:4:8"]]
+ 00af16bc ["CALL", null, ["callee:0047d134:8"]]
- 00af06c8 bytes d331e697
+ 00af16bc bytes 9e2ee697
~~~


<a id="compare-5eb0edeafd18aa8814f1b98567692e8b"></a>

### [`00af075c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af075c.md) → [`00af1750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1750.md) FUN_00af1750

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00aebc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aeb/00aebc30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00aecc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aec/00aecc24.md)

変更の種類 branch_condition_or_target, call, call_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af075c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af075c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0760"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af075c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af0760",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af177c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00af1750",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af1754",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af177c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af075c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af075c.md#insn-00af075c) · [`00af0760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af075c.md#insn-00af0760) · [`00af0788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af075c.md#insn-00af0788)
- 新版 [`00af177c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1750.md#insn-00af177c)

~~~diff
- 00af075c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af075c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af075c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af075c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af075c bytes fd7bbea9
- 00af0760 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af0760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00af0760 bytes f30b00f9
- 00af0788 ["INT_ADD", "register:40f0:8", ["const:af0788:8", "const:4:8"]]
- 00af0788 ["CALL", null, ["ram:47ad34:8"]]
+ 00af177c ["INT_ADD", "register:40f0:8", ["const:af177c:8", "const:4:8"]]
+ 00af177c ["CALL", null, ["ram:47b054:8"]]
- 00af0788 bytes 6b29e697
+ 00af177c bytes 3626e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a08b8c3ddab191ef5240227d7da107b"></a>

### [`00af0810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0810.md) → [`00af1804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1804.md) FUN_00af1804

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af181c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af180c",
      "incomplete_value": false,
      "site": "00af1810",
      "value": [
        "leaf",
        "const:10:8"
      ]
    },
    "old": null,
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
      "unmatched:00af0828",
      "DATA",
      [
        "storage",
        "00c8e548",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00af082c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af181c",
      "DATA",
      [
        "storage",
        "00c8f518",
        null,
        "undefined *"
      ]
    ],
    [
      "00af1820",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af081c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0810.md#insn-00af081c) · [`00af0828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0810.md#insn-00af0828) · [`00af0830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0810.md#insn-00af0830)
- 新版 [`00af1810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1804.md#insn-00af1810)

~~~diff
- 00af081c ["INT_ADD", "register:40f0:8", ["const:af081c:8", "const:4:8"]]
- 00af081c ["CALL", null, ["callee:00c58f30:8"]]
+ 00af1810 ["INT_ADD", "register:40f0:8", ["const:af1810:8", "const:4:8"]]
+ 00af1810 ["CALL", null, ["callee:00c58f30:8"]]
- 00af081c bytes d19d0594
+ 00af1810 bytes c89d0594
- 00af0828 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00af0828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af0828 bytes 080000f9
- 00af0830 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af0830 ["RETURN", null, ["register:0:8"]]
- 00af0830 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f36781ace5b862ee8eba81ffaaecb54"></a>

### [`00af0834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0834.md) → [`00af1828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1828.md) FUN_00af1828

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af182c",
      "incomplete_value": false,
      "site": "00af1830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0838",
      "incomplete_value": false,
      "site": "00af083c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00af1830",
      "DATA",
      [
        "storage",
        "00c8e548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1830",
      "DATA",
      [
        "storage",
        "00c8f518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0834.md#insn-00af0834) · [`00af0838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0834.md#insn-00af0838)
- 新版 [`00af1828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1828.md#insn-00af1828) · [`00af182c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1828.md#insn-00af182c)

~~~diff
- 00af0834 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00af1828 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00af0834 bytes e80c00d0
+ 00af1828 bytes e80c00d0
- 00af0838 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00af0838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af0838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af0838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af182c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00af182c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af182c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af182c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af0838 bytes 08211591
+ 00af182c bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de555dfae19e3f53827616a95fd37ed"></a>

### [`00af084c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af084c.md) → [`00af1840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1840.md) FUN_00af1840

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0854"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af1848"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af1868",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af0874",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "unmatched:00af0854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1888"
      ]
    ],
    [
      "00af1868",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00af1848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1888"
      ]
    ],
    [
      "00af1868",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af084c.md#insn-00af0854) · [`00af0874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af084c.md#insn-00af0874)
- 新版 [`00af1868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1840.md#insn-00af1868) · [`00af1848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1840.md#insn-00af1848)

~~~diff
- 00af0854 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af0854 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00af0854 bytes 01020054
- 00af0874 ["INT_ADD", "register:40f0:8", ["const:af0874:8", "const:4:8"]]
- 00af0874 ["CALL", null, ["ram:47ad34:8"]]
+ 00af1868 ["INT_ADD", "register:40f0:8", ["const:af1868:8", "const:4:8"]]
+ 00af1868 ["CALL", null, ["ram:47b054:8"]]
- 00af0874 bytes 3029e697
+ 00af1868 bytes fb25e697
+ 00af1848 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00af1848 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00af1848 bytes 01020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ec34250c9034064a66ddcea453293ff"></a>

### [`00af08f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af08f8.md) → [`00af18ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af18ec.md) FUN_00af18ec

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af18f8",
      "incomplete_value": false,
      "site": "00af18f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0904",
      "incomplete_value": false,
      "site": "00af0904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00af18f8",
      "DATA",
      [
        "storage",
        "00c8e5c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af18f8",
      "DATA",
      [
        "storage",
        "00c8f598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af08fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af08f8.md#insn-00af08fc) · [`00af0900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af08f8.md#insn-00af0900)
- 新版 [`00af18f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af18ec.md#insn-00af18f0) · [`00af18f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af18ec.md#insn-00af18f4)

~~~diff
- 00af08fc ["COPY", "register:4048:8", ["const:c8e000:8"]]
+ 00af18f0 ["COPY", "register:4048:8", ["const:c8f000:8"]]
- 00af08fc bytes e90c00d0
+ 00af18f0 bytes e90c00d0
- 00af0900 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00af0900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af0900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af0900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af18f4 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00af18f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af18f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af18f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af0900 bytes 29211791
+ 00af18f4 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b72a54b5147ca2a3852882483a7880"></a>

### [`00af0914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0914.md) → [`00af1908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1908.md) FUN_00af1908

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b9624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9624.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008ba5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba5d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.83% / 新版 85.83%

CFGの説明率　旧版 79.49% / 新版 79.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af099c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af09a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af09a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af1940",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00af0994",
      "READ",
      [
        "storage",
        "002adfd3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af099c",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af1940",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00af1988",
      "READ",
      [
        "storage",
        "002ae0a0",
        null,
        "string"
      ]
    ],
    [
      "00af1990",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af094c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0914.md#insn-00af094c) · [`00af099c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0914.md#insn-00af099c) · [`00af09a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0914.md#insn-00af09a0)
- 新版 [`00af1940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1908.md#insn-00af1940)

~~~diff
- 00af094c ["INT_ADD", "register:40f0:8", ["const:af094c:8", "const:4:8"]]
- 00af094c ["CALL", null, ["ram:47ad34:8"]]
+ 00af1940 ["INT_ADD", "register:40f0:8", ["const:af1940:8", "const:4:8"]]
+ 00af1940 ["CALL", null, ["ram:47b054:8"]]
- 00af094c bytes fa28e697
+ 00af1940 bytes c525e697
- 00af099c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00af099c ["COPY", "tmp:1:8", ["register:8:8"]]
- 00af099c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00af099c bytes e8030039
- 00af09a0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00af09a0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:11:8"]]
- 00af09a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00af09a0 bytes ea130178
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cef7a1cf9ea3f4d534e4f79a33d8b13b"></a>

### [`00af0c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c20.md) → [`00af1c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c14.md) FUN_00af1c14

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af1c38"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0c44",
      "DATA",
      [
        "storage",
        "00c8e638",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00af0c48",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af0c4c",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af1c38",
      "DATA",
      [
        "storage",
        "00c8f608",
        null,
        "undefined *"
      ]
    ],
    [
      "00af1c3c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af1c40",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c20.md#insn-00af0c34) · [`00af0c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c20.md#insn-00af0c44) · [`00af0c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c20.md#insn-00af0c50)
- 新版 [`00af1c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c14.md#insn-00af1c28)

~~~diff
- 00af0c34 ["INT_ADD", "register:40f0:8", ["const:af0c34:8", "const:4:8"]]
- 00af0c34 ["CALL", null, ["callee:00c58f30:8"]]
+ 00af1c28 ["INT_ADD", "register:40f0:8", ["const:af1c28:8", "const:4:8"]]
+ 00af1c28 ["CALL", null, ["callee:00c58f30:8"]]
- 00af0c34 bytes cb9c0594
+ 00af1c28 bytes c29c0594
- 00af0c44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af0c44 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af0c44 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00af0c44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af0c44 bytes 082400a9
- 00af0c50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af0c50 ["RETURN", null, ["register:0:8"]]
- 00af0c50 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06158878fae6863868b7f0b65035551d"></a>

### [`00af0c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c54.md) → [`00af1c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c48.md) FUN_00af1c48

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1c54",
      "incomplete_value": false,
      "site": "00af1c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0c60",
      "incomplete_value": false,
      "site": "00af0c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
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
      "00af1c54",
      "DATA",
      [
        "storage",
        "00c8e638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1c54",
      "DATA",
      [
        "storage",
        "00c8f608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c54.md#insn-00af0c58) · [`00af0c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c54.md#insn-00af0c5c)
- 新版 [`00af1c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c48.md#insn-00af1c4c) · [`00af1c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c48.md#insn-00af1c50)

~~~diff
- 00af0c58 ["COPY", "register:4048:8", ["const:c8e000:8"]]
+ 00af1c4c ["COPY", "register:4048:8", ["const:c8f000:8"]]
- 00af0c58 bytes e90c00d0
+ 00af1c4c bytes e90c00d0
- 00af0c5c ["COPY", "tmp:0:8", ["const:638:8"]]
- 00af0c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af0c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af0c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af1c50 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00af1c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af1c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af1c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af0c5c bytes 29e11891
+ 00af1c50 bytes 29211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33065a275342eb27538b8ada51492bd2"></a>

### [`00af0c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c70.md) → [`00af1c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c64.md) FUN_00af1c64

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0cbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af1c70"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0c98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af1cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1cac"
      ]
    ],
    [
      "unmatched:00af0c98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00af0cbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1cc8"
      ]
    ]
  ],
  "added": [
    [
      "00af1c70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1cac"
      ]
    ],
    [
      "00af1c8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00af1cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1cc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c70.md#insn-00af0c98) · [`00af0cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0c70.md#insn-00af0cbc)
- 新版 [`00af1c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1c64.md#insn-00af1c70)

~~~diff
- 00af0c98 ["INT_ADD", "register:40f0:8", ["const:af0c98:8", "const:4:8"]]
- 00af0c98 ["CALL", null, ["ram:47ad34:8"]]
- 00af0c98 bytes 2728e697
- 00af0cbc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af0cbc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00af0cbc bytes c1000054
+ 00af1c70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00af1c70 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00af1c70 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0d5e3070128f51aeae54d62f7d0bdd"></a>

### [`00af0d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d04.md) → [`00af1cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1cf8.md) FUN_00af1cf8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0d04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0d04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0d08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0d04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af0d08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af0d28",
      "DATA",
      [
        "storage",
        "00c8e6b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af1cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af1d1c",
      "DATA",
      [
        "storage",
        "00c8f688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d04.md#insn-00af0d04) · [`00af0d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d04.md#insn-00af0d08) · [`00af0d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d04.md#insn-00af0d18)
- 新版 [`00af1d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1cf8.md#insn-00af1d0c)

~~~diff
- 00af0d04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af0d04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af0d04 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af0d04 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af0d04 bytes fd7bbea9
- 00af0d08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af0d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00af0d08 bytes f30b00f9
- 00af0d18 ["INT_ADD", "register:40f0:8", ["const:af0d18:8", "const:4:8"]]
- 00af0d18 ["CALL", null, ["callee:00c58f30:8"]]
+ 00af1d0c ["INT_ADD", "register:40f0:8", ["const:af1d0c:8", "const:4:8"]]
+ 00af1d0c ["CALL", null, ["callee:00c58f30:8"]]
- 00af0d18 bytes 929c0594
+ 00af1d0c bytes 899c0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f0bc5b7a5460c38684f6a472cad9c6"></a>

### [`00af0d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d9c.md) → [`00af1d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1d90.md) FUN_00af1d90

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1db4",
      "incomplete_value": false,
      "site": "00af1db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0dc0",
      "incomplete_value": false,
      "site": "00af0dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
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
      "00af1db4",
      "DATA",
      [
        "storage",
        "00c8e738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1db4",
      "DATA",
      [
        "storage",
        "00c8f708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d9c.md#insn-00af0db0) · [`00af0db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d9c.md#insn-00af0db8) · [`00af0dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0d9c.md#insn-00af0dbc)
- 新版 [`00af1da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1d90.md#insn-00af1da4) · [`00af1dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1d90.md#insn-00af1dac) · [`00af1db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1d90.md#insn-00af1db0)

~~~diff
- 00af0db0 ["INT_ADD", "register:40f0:8", ["const:af0db0:8", "const:4:8"]]
- 00af0db0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00af1da4 ["INT_ADD", "register:40f0:8", ["const:af1da4:8", "const:4:8"]]
+ 00af1da4 ["CALL", null, ["callee:00c58f30:8"]]
- 00af0db0 bytes 6c9c0594
+ 00af1da4 bytes 639c0594
- 00af0db8 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00af1dac ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00af0db8 bytes e80c00d0
+ 00af1dac bytes e80c00d0
- 00af0dbc ["COPY", "tmp:0:8", ["const:738:8"]]
- 00af0dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af0dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af0dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1db0 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00af1db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af0dbc bytes 08e11c91
+ 00af1db0 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

