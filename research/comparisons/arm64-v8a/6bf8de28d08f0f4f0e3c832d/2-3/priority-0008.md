# v16.0.2 → v16.0.3 · 最優先の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-d6fa676e6f9b1f7baf7cd48cf972c60b"></a>

### [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) → [`004b8ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8ecc.md) FUN_004b8ecc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) [`004b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md) [`004d73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md) [`004d7948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md) · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 4件 [`004b8328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8328.md) [`004b9074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9074.md) [`004d76f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d7/004d76f0.md) [`004d7c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d7/004d7c68.md) · 呼出先 1件 [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b9050",
      "incomplete_value": false,
      "site": "004b9070",
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
            "const:6dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8d30",
      "incomplete_value": false,
      "site": "004b8d50",
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
            "const:584:8"
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
      "definition_site": "004b9058",
      "incomplete_value": false,
      "site": "004b9070",
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
    "old": {
      "definition_site": "004b8d38",
      "incomplete_value": false,
      "site": "004b8d50",
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
            "const:ed:8"
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
      "definition_site": "004b9060",
      "incomplete_value": false,
      "site": "004b9070",
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
            "const:a0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8d40",
      "incomplete_value": false,
      "site": "004b8d50",
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
            "const:935:8"
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
      "004b9050",
      "PARAM",
      [
        "storage",
        "002a6584",
        null,
        "string"
      ]
    ],
    [
      "004b9058",
      "PARAM",
      [
        "storage",
        "002b60ed",
        null,
        "string"
      ]
    ],
    [
      "004b9060",
      "PARAM",
      [
        "storage",
        "002af935",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b9050",
      "PARAM",
      [
        "storage",
        "002a66dc",
        null,
        "string"
      ]
    ],
    [
      "004b9058",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        "string"
      ]
    ],
    [
      "004b9060",
      "PARAM",
      [
        "storage",
        "002afa0c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md#insn-004b8d50) · [`004b8d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md#insn-004b8d30) · [`004b8d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md#insn-004b8d38)
- 新版 [`004b9070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8ecc.md#insn-004b9070) · [`004b9050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8ecc.md#insn-004b9050) · [`004b9058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8ecc.md#insn-004b9058)

~~~diff
- 004b8d50 ["INT_ADD", "register:40f0:8", ["const:4b8d50:8", "const:4:8"]]
- 004b8d50 ["CALL", null, ["callee:00c596f0:8"]]
+ 004b9070 ["INT_ADD", "register:40f0:8", ["const:4b9070:8", "const:4:8"]]
+ 004b9070 ["CALL", null, ["callee:00c596f0:8"]]
- 004b8d50 bytes 747e1e94
+ 004b9070 bytes a0811e94
- 004b8d30 ["COPY", "tmp:0:8", ["const:584:8"]]
- 004b8d30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b8d30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b8d30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b9050 ["COPY", "tmp:0:8", ["const:6dc:8"]]
+ 004b9050 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b9050 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b9050 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b8d30 bytes 00101691
+ 004b9050 bytes 00701b91
- 004b8d38 ["COPY", "tmp:0:8", ["const:ed:8"]]
- 004b8d38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b8d38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b8d38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b9058 ["COPY", "tmp:0:8", ["const:1bc:8"]]
+ 004b9058 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b9058 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b9058 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b8d38 bytes 21b40391
+ 004b9058 bytes 21f00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21fdaaac508c9b40c6b9f9d32121d39d"></a>

### [`004b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md) → [`004b9074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9074.md) _ZN5Botan6BigIntmIERKS0_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d10.md) · 呼出先 6件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) [`004b8f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8f94.md) [`004d6c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6c04.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)
- 新版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ce0.md) · 呼出先 6件 [`004b8b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8b14.md) [`004b8ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8ecc.md) [`004b92b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b92b4.md) [`004d6f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d6/004d6f24.md) [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.31% / 新版 99.31%

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
      "site": "004b91a4",
      "value": [
        "leaf",
        "ram:4b92b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8e84",
      "value": [
        "leaf",
        "ram:4b8f94:8"
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
      "004b91a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b8f94"
      ]
    ]
  ],
  "added": [
    [
      "004b91a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b92b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md#insn-004b8e84) · [`004b8dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md#insn-004b8dd4) · [`004b8e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md#insn-004b8e14)
- 新版 [`004b91a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9074.md#insn-004b91a4) · [`004b90f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9074.md#insn-004b90f4) · [`004b9134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9074.md#insn-004b9134)

~~~diff
- 004b8e84 ["INT_ADD", "register:40f0:8", ["const:4b8e84:8", "const:4:8"]]
- 004b8e84 ["CALL", null, ["ram:4b8f94:8"]]
+ 004b91a4 ["INT_ADD", "register:40f0:8", ["const:4b91a4:8", "const:4:8"]]
+ 004b91a4 ["CALL", null, ["ram:4b92b4:8"]]
- 004b8e84 bytes 44000094
+ 004b91a4 bytes 44000094
- 004b8dd4 ["INT_ADD", "register:40f0:8", ["const:4b8dd4:8", "const:4:8"]]
- 004b8dd4 ["CALL", null, ["callee:004b8b14:8"]]
+ 004b90f4 ["INT_ADD", "register:40f0:8", ["const:4b90f4:8", "const:4:8"]]
+ 004b90f4 ["CALL", null, ["callee:004b8b14:8"]]
- 004b8dd4 bytes 88feff97
+ 004b90f4 bytes 88feff97
- 004b8e14 ["INT_ADD", "register:40f0:8", ["const:4b8e14:8", "const:4:8"]]
- 004b8e14 ["CALL", null, ["callee:00540c80:8"]]
+ 004b9134 ["INT_ADD", "register:40f0:8", ["const:4b9134:8", "const:4:8"]]
+ 004b9134 ["CALL", null, ["callee:00540c80:8"]]
- 004b8e14 bytes d31e0294
+ 004b9134 bytes d31e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b5d042708fe52911da265ea8761f35"></a>

### [`004b96bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md) → [`004b99dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b99dc.md) _ZN5BotanrmERKNS_6BigIntES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d70.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d40.md) · 呼出先 11件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b9a90",
      "incomplete_value": true,
      "site": "004b9a94",
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
      "definition_site": "004b9770",
      "incomplete_value": true,
      "site": "004b9774",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b9ab4",
      "incomplete_value": true,
      "site": "004b9ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b9794",
      "incomplete_value": true,
      "site": "004b9798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
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
      "definition_site": "004b9ab0",
      "incomplete_value": false,
      "site": "004b9ab8",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004b9790",
      "incomplete_value": false,
      "site": "004b9798",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004b9a7c",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004b9a94",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9ab0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b9a7c",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "004b9a94",
      "DATA",
      [
        "storage",
        "00c6ad00",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9ab0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b9798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md#insn-004b9798) · [`004b9820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md#insn-004b9820) · [`004b9894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md#insn-004b9894)
- 新版 [`004b9ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b99dc.md#insn-004b9ab8) · [`004b9b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b99dc.md#insn-004b9b40) · [`004b9bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b99dc.md#insn-004b9bb4)

~~~diff
- 004b9798 ["INT_ADD", "register:40f0:8", ["const:4b9798:8", "const:4:8"]]
- 004b9798 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004b9ab8 ["INT_ADD", "register:40f0:8", ["const:4b9ab8:8", "const:4:8"]]
+ 004b9ab8 ["CALL", null, ["callee:00c58fb0:8"]]
- 004b9798 bytes 127a1e94
+ 004b9ab8 bytes 3e7d1e94
- 004b9820 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b9820 ["INT_ADD", "register:40f0:8", ["const:4b9820:8", "const:4:8"]]
- 004b9820 ["CALLIND", null, ["register:0:8"]]
+ 004b9b40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b9b40 ["INT_ADD", "register:40f0:8", ["const:4b9b40:8", "const:4:8"]]
+ 004b9b40 ["CALLIND", null, ["register:0:8"]]
- 004b9820 bytes 20013fd6
+ 004b9b40 bytes 20013fd6
- 004b9894 ["INT_ADD", "register:40f0:8", ["const:4b9894:8", "const:4:8"]]
- 004b9894 ["CALL", null, ["callee:0043e138:8"]]
+ 004b9bb4 ["INT_ADD", "register:40f0:8", ["const:4b9bb4:8", "const:4:8"]]
+ 004b9bb4 ["CALL", null, ["callee:0043e138:8"]]
- 004b9894 bytes 6111fe97
+ 004b9bb4 bytes 6111fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15d35ea531bcdf16f9cc3237e62d4073"></a>

### [`004b993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md) → [`004b9c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9c5c.md) _ZN5Botan6BigIntrMEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004bbecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

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
      "definition_site": "004b9e58",
      "incomplete_value": true,
      "site": "004b9e5c",
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
      "definition_site": "004b9b38",
      "incomplete_value": true,
      "site": "004b9b3c",
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
      "definition_site": "004b9e60",
      "incomplete_value": true,
      "site": "004b9e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b9b40",
      "incomplete_value": true,
      "site": "004b9b44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
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
      "definition_site": "004b9e4c",
      "incomplete_value": false,
      "site": "004b9e64",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004b9b2c",
      "incomplete_value": false,
      "site": "004b9b44",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004b9e38",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004b9e4c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b9e5c",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004b9e38",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "004b9e4c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004b9e5c",
      "DATA",
      [
        "storage",
        "00c6ad00",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b9b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md#insn-004b9b44) · [`004b9990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md#insn-004b9990) · [`004b99e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md#insn-004b99e4)
- 新版 [`004b9e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9c5c.md#insn-004b9e64) · [`004b9cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9c5c.md#insn-004b9cb0) · [`004b9d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9c5c.md#insn-004b9d04)

~~~diff
- 004b9b44 ["INT_ADD", "register:40f0:8", ["const:4b9b44:8", "const:4:8"]]
- 004b9b44 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004b9e64 ["INT_ADD", "register:40f0:8", ["const:4b9e64:8", "const:4:8"]]
+ 004b9e64 ["CALL", null, ["callee:00c58fb0:8"]]
- 004b9b44 bytes 27791e94
+ 004b9e64 bytes 537c1e94
- 004b9990 ["INT_ADD", "register:40f0:8", ["const:4b9990:8", "const:4:8"]]
- 004b9990 ["CALL", null, ["callee:00c59130:8"]]
+ 004b9cb0 ["INT_ADD", "register:40f0:8", ["const:4b9cb0:8", "const:4:8"]]
+ 004b9cb0 ["CALL", null, ["callee:00c59130:8"]]
- 004b9990 bytes f4791e94
+ 004b9cb0 bytes 207d1e94
- 004b99e4 ["INT_ADD", "register:40f0:8", ["const:4b99e4:8", "const:4:8"]]
- 004b99e4 ["CALL", null, ["callee:004bbecc:8"]]
+ 004b9d04 ["INT_ADD", "register:40f0:8", ["const:4b9d04:8", "const:4:8"]]
+ 004b9d04 ["CALL", null, ["callee:004bbecc:8"]]
- 004b99e4 bytes 72080094
+ 004b9d04 bytes 72080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94bf419f6ab4a7dfdb8a9037b8d59d5f"></a>

### [`004ba4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md) → [`004ba7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba7f8.md) _ZN5BotanrmERKNS_6BigIntEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58da0.md) · 呼出先 4件 [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d70.md) · 呼出先 4件 [`004bbecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

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
      "definition_site": "004ba94c",
      "incomplete_value": true,
      "site": "004ba950",
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
      "definition_site": "004ba62c",
      "incomplete_value": true,
      "site": "004ba630",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ba954",
      "incomplete_value": true,
      "site": "004ba958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ba634",
      "incomplete_value": true,
      "site": "004ba638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
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
      "definition_site": "004ba940",
      "incomplete_value": false,
      "site": "004ba958",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004ba620",
      "incomplete_value": false,
      "site": "004ba638",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004ba92c",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004ba940",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004ba950",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ba92c",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "004ba940",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004ba950",
      "DATA",
      [
        "storage",
        "00c6ad00",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ba638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md#insn-004ba638) · [`004ba574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md#insn-004ba574) · [`004ba5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md#insn-004ba5d4)
- 新版 [`004ba958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba7f8.md#insn-004ba958) · [`004ba894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba7f8.md#insn-004ba894) · [`004ba8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba7f8.md#insn-004ba8f4)

~~~diff
- 004ba638 ["INT_ADD", "register:40f0:8", ["const:4ba638:8", "const:4:8"]]
- 004ba638 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004ba958 ["INT_ADD", "register:40f0:8", ["const:4ba958:8", "const:4:8"]]
+ 004ba958 ["CALL", null, ["callee:00c58fb0:8"]]
- 004ba638 bytes 6a761e94
+ 004ba958 bytes 96791e94
- 004ba574 ["INT_ADD", "register:40f0:8", ["const:4ba574:8", "const:4:8"]]
- 004ba574 ["CALL", null, ["callee:004bbecc:8"]]
+ 004ba894 ["INT_ADD", "register:40f0:8", ["const:4ba894:8", "const:4:8"]]
+ 004ba894 ["CALL", null, ["callee:004bbecc:8"]]
- 004ba574 bytes 8e050094
+ 004ba894 bytes 8e050094
- 004ba5d4 ["INT_ADD", "register:40f0:8", ["const:4ba5d4:8", "const:4:8"]]
- 004ba5d4 ["CALL", null, ["callee:00c58f90:8"]]
+ 004ba8f4 ["INT_ADD", "register:40f0:8", ["const:4ba8f4:8", "const:4:8"]]
+ 004ba8f4 ["CALL", null, ["callee:00c58f90:8"]]
- 004ba5d4 bytes 7b761e94
+ 004ba8f4 bytes a7791e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b679bfec55a2c4b39dcc9b8f51b3ce65"></a>

### [`004bb16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md) → [`004bb48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb48c.md) _ZNK5Botan6BigInt13get_substringEmm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58de0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59db0.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb658",
      "incomplete_value": false,
      "site": "004bb660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:f84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb338",
      "incomplete_value": false,
      "site": "004bb340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:f44:8"
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
      "definition_site": "004bb694",
      "incomplete_value": true,
      "site": "004bb6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb374",
      "incomplete_value": true,
      "site": "004bb380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
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
      "definition_site": "004bb690",
      "incomplete_value": false,
      "site": "004bb6a0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bb370",
      "incomplete_value": false,
      "site": "004bb380",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bb658",
      "PARAM",
      [
        "storage",
        "0029ef44",
        null,
        "string"
      ]
    ],
    [
      "004bb690",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bb694",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bb658",
      "PARAM",
      [
        "storage",
        "0029ef84",
        null,
        "string"
      ]
    ],
    [
      "004bb690",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bb694",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md#insn-004bb340) · [`004bb380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md#insn-004bb380) · [`004bb32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md#insn-004bb32c)
- 新版 [`004bb660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb48c.md#insn-004bb660) · [`004bb6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb48c.md#insn-004bb6a0) · [`004bb64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb48c.md#insn-004bb64c)

~~~diff
- 004bb340 ["INT_ADD", "register:40f0:8", ["const:4bb340:8", "const:4:8"]]
- 004bb340 ["CALL", null, ["callee:0043e138:8"]]
+ 004bb660 ["INT_ADD", "register:40f0:8", ["const:4bb660:8", "const:4:8"]]
+ 004bb660 ["CALL", null, ["callee:0043e138:8"]]
- 004bb340 bytes b60afe97
+ 004bb660 bytes b60afe97
- 004bb380 ["INT_ADD", "register:40f0:8", ["const:4bb380:8", "const:4:8"]]
- 004bb380 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bb6a0 ["INT_ADD", "register:40f0:8", ["const:4bb6a0:8", "const:4:8"]]
+ 004bb6a0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bb380 bytes 18731e94
+ 004bb6a0 bytes 44761e94
- 004bb32c ["INT_ADD", "register:40f0:8", ["const:4bb32c:8", "const:4:8"]]
- 004bb32c ["CALL", null, ["callee:00c58f90:8"]]
+ 004bb64c ["INT_ADD", "register:40f0:8", ["const:4bb64c:8", "const:4:8"]]
+ 004bb64c ["CALL", null, ["callee:00c58f90:8"]]
- 004bb32c bytes 25731e94
+ 004bb64c bytes 51761e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aab5a40033d219bd81aaf6aa77e87444"></a>

### [`004bb3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md) → [`004bb6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb6f4.md) _ZNK5Botan6BigInt9to_u32bitEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb7dc",
      "incomplete_value": false,
      "site": "004bb7e4",
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
            "const:927:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb4bc",
      "incomplete_value": false,
      "site": "004bb4c4",
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
            "const:849:8"
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
      "definition_site": "004bb818",
      "incomplete_value": true,
      "site": "004bb824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb4f8",
      "incomplete_value": true,
      "site": "004bb504",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
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
      "definition_site": "004bb814",
      "incomplete_value": false,
      "site": "004bb824",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bb4f4",
      "incomplete_value": false,
      "site": "004bb504",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bb7dc",
      "PARAM",
      [
        "storage",
        "002bd849",
        null,
        "string"
      ]
    ],
    [
      "004bb814",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bb818",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bb7dc",
      "PARAM",
      [
        "storage",
        "002bd927",
        null,
        "string"
      ]
    ],
    [
      "004bb814",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bb818",
      "READ",
      [
        "storage",
        "00c9be38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md#insn-004bb4c4) · [`004bb504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md#insn-004bb504) · [`004bb528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md#insn-004bb528)
- 新版 [`004bb7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb6f4.md#insn-004bb7e4) · [`004bb824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb6f4.md#insn-004bb824) · [`004bb848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb6f4.md#insn-004bb848)

~~~diff
- 004bb4c4 ["INT_ADD", "register:40f0:8", ["const:4bb4c4:8", "const:4:8"]]
- 004bb4c4 ["CALL", null, ["callee:0043e138:8"]]
+ 004bb7e4 ["INT_ADD", "register:40f0:8", ["const:4bb7e4:8", "const:4:8"]]
+ 004bb7e4 ["CALL", null, ["callee:0043e138:8"]]
- 004bb4c4 bytes 550afe97
+ 004bb7e4 bytes 550afe97
- 004bb504 ["INT_ADD", "register:40f0:8", ["const:4bb504:8", "const:4:8"]]
- 004bb504 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bb824 ["INT_ADD", "register:40f0:8", ["const:4bb824:8", "const:4:8"]]
+ 004bb824 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bb504 bytes b7721e94
+ 004bb824 bytes e3751e94
- 004bb528 ["INT_ADD", "register:40f0:8", ["const:4bb528:8", "const:4:8"]]
- 004bb528 ["CALL", null, ["callee:0043e138:8"]]
+ 004bb848 ["INT_ADD", "register:40f0:8", ["const:4bb848:8", "const:4:8"]]
+ 004bb848 ["CALL", null, ["callee:0043e138:8"]]
- 004bb528 bytes 3c0afe97
+ 004bb848 bytes 3c0afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6184be17853dbfb6e43928cf7f9671"></a>

### [`004bb770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md) → [`004bba90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bba90.md) _ZN5Botan6BigInt17const_time_lookupERNSt6__ndk16vectorIjNS_16secure_allocatorIjEEEERKNS2_IS0_NS1_9allocatorIS0_EEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58df0.md) · 呼出先 2件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c59dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59dc0.md) · 呼出先 2件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bbc00",
      "incomplete_value": false,
      "site": "004bbc20",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8e0",
      "incomplete_value": false,
      "site": "004bb900",
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
            "const:1cb:8"
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
      "definition_site": "004bbc08",
      "incomplete_value": false,
      "site": "004bbc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:fb2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8e8",
      "incomplete_value": false,
      "site": "004bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:f72:8"
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
      "definition_site": "004bbc10",
      "incomplete_value": false,
      "site": "004bbc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:5c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8f0",
      "incomplete_value": false,
      "site": "004bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:4e3:8"
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
      "004bbc00",
      "PARAM",
      [
        "storage",
        "002b81cb",
        null,
        "string"
      ]
    ],
    [
      "004bbc08",
      "PARAM",
      [
        "storage",
        "0029ef72",
        null,
        "string"
      ]
    ],
    [
      "004bbc10",
      "PARAM",
      [
        "storage",
        "002bc4e3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bbc00",
      "PARAM",
      [
        "storage",
        "002b829a",
        null,
        "string"
      ]
    ],
    [
      "004bbc08",
      "PARAM",
      [
        "storage",
        "0029efb2",
        null,
        "string"
      ]
    ],
    [
      "004bbc10",
      "PARAM",
      [
        "storage",
        "002bc5c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md#insn-004bb900) · [`004bb7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md#insn-004bb7a8) · [`004bb8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md#insn-004bb8e0)
- 新版 [`004bbc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bba90.md#insn-004bbc20) · [`004bbac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bba90.md#insn-004bbac8) · [`004bbc00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bba90.md#insn-004bbc00)

~~~diff
- 004bb900 ["INT_ADD", "register:40f0:8", ["const:4bb900:8", "const:4:8"]]
- 004bb900 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bbc20 ["INT_ADD", "register:40f0:8", ["const:4bbc20:8", "const:4:8"]]
+ 004bbc20 ["CALL", null, ["callee:00c596f0:8"]]
- 004bb900 bytes 88731e94
+ 004bbc20 bytes b4761e94
- 004bb7a8 ["INT_ADD", "register:40f0:8", ["const:4bb7a8:8", "const:4:8"]]
- 004bb7a8 ["CALL", null, ["callee:00c59130:8"]]
+ 004bbac8 ["INT_ADD", "register:40f0:8", ["const:4bbac8:8", "const:4:8"]]
+ 004bbac8 ["CALL", null, ["callee:00c59130:8"]]
- 004bb7a8 bytes 6e721e94
+ 004bbac8 bytes 9a751e94
- 004bb8e0 ["COPY", "tmp:0:8", ["const:1cb:8"]]
- 004bb8e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bb8e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bb8e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bbc00 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 004bbc00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bbc00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bbc00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bb8e0 bytes 002c0791
+ 004bbc00 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1a34f39dab7f9d50b28d1c553cf9bc7"></a>

### [`004bb904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md) → [`004bbc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbc24.md) FUN_004bbc24

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`00c58d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d10.md)
- 新版 呼出元 1件 [`004b6a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b6a88.md) · 呼出先 7件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c599c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599c0.md) [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md) [`00c59ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ce0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.13% / 新版 96.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bbdb4",
      "incomplete_value": true,
      "site": "004bbdb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bba94",
      "incomplete_value": true,
      "site": "004bba94",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bbe44",
      "incomplete_value": true,
      "site": "004bbe44",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbb24",
      "incomplete_value": true,
      "site": "004bbb24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bbe74",
      "incomplete_value": true,
      "site": "004bbe74",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbb54",
      "incomplete_value": true,
      "site": "004bbb54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "004bbda4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004bbe34",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004bbe64",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bbda4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004bbe34",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004bbe64",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md#insn-004bba94) · [`004bbb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md#insn-004bbb24) · [`004bbb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md#insn-004bbb54)
- 新版 [`004bbdb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbc24.md#insn-004bbdb4) · [`004bbe44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbc24.md#insn-004bbe44) · [`004bbe74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbc24.md#insn-004bbe74)

~~~diff
- 004bba94 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bba94 ["INT_ADD", "register:40f0:8", ["const:4bba94:8", "const:4:8"]]
- 004bba94 ["CALLIND", null, ["register:0:8"]]
+ 004bbdb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bbdb4 ["INT_ADD", "register:40f0:8", ["const:4bbdb4:8", "const:4:8"]]
+ 004bbdb4 ["CALLIND", null, ["register:0:8"]]
- 004bba94 bytes 20013fd6
+ 004bbdb4 bytes 20013fd6
- 004bbb24 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bbb24 ["INT_ADD", "register:40f0:8", ["const:4bbb24:8", "const:4:8"]]
- 004bbb24 ["CALLIND", null, ["register:0:8"]]
+ 004bbe44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bbe44 ["INT_ADD", "register:40f0:8", ["const:4bbe44:8", "const:4:8"]]
+ 004bbe44 ["CALLIND", null, ["register:0:8"]]
- 004bbb24 bytes 20013fd6
+ 004bbe44 bytes 20013fd6
- 004bbb54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bbb54 ["INT_ADD", "register:40f0:8", ["const:4bbb54:8", "const:4:8"]]
- 004bbb54 ["CALLIND", null, ["register:0:8"]]
+ 004bbe74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bbe74 ["INT_ADD", "register:40f0:8", ["const:4bbe74:8", "const:4:8"]]
+ 004bbe74 ["CALLIND", null, ["register:0:8"]]
- 004bbb54 bytes 20013fd6
+ 004bbe74 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd5b2c1c3a60ab7d0bf09dc3b169ced8"></a>

### [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) → [`004bbecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md) FUN_004bbecc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) [`004b993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md) [`004ba4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md) [`004ddf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dd/004ddf48.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 4件 [`004b6a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b6a88.md) [`004b9c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b9/004b9c5c.md) [`004ba7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ba/004ba7f8.md) [`004de268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004de268.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bbf38",
      "incomplete_value": false,
      "site": "004bbf40",
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
            "const:eb3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbc18",
      "incomplete_value": false,
      "site": "004bbc20",
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
            "const:dd5:8"
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
      "definition_site": "004bbf74",
      "incomplete_value": true,
      "site": "004bbf80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbc54",
      "incomplete_value": true,
      "site": "004bbc60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
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
      "definition_site": "004bbf70",
      "incomplete_value": false,
      "site": "004bbf80",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bbc50",
      "incomplete_value": false,
      "site": "004bbc60",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bbf38",
      "PARAM",
      [
        "storage",
        "002b4dd5",
        null,
        "string"
      ]
    ],
    [
      "004bbf70",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bbf74",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bbf38",
      "PARAM",
      [
        "storage",
        "002b4eb3",
        null,
        "string"
      ]
    ],
    [
      "004bbf70",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bbf74",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bbc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md#insn-004bbc20) · [`004bbc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md#insn-004bbc60) · [`004bbc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md#insn-004bbc0c)
- 新版 [`004bbf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md#insn-004bbf40) · [`004bbf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md#insn-004bbf80) · [`004bbf2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md#insn-004bbf2c)

~~~diff
- 004bbc20 ["INT_ADD", "register:40f0:8", ["const:4bbc20:8", "const:4:8"]]
- 004bbc20 ["CALL", null, ["callee:0043e138:8"]]
+ 004bbf40 ["INT_ADD", "register:40f0:8", ["const:4bbf40:8", "const:4:8"]]
+ 004bbf40 ["CALL", null, ["callee:0043e138:8"]]
- 004bbc20 bytes 7e08fe97
+ 004bbf40 bytes 7e08fe97
- 004bbc60 ["INT_ADD", "register:40f0:8", ["const:4bbc60:8", "const:4:8"]]
- 004bbc60 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bbf80 ["INT_ADD", "register:40f0:8", ["const:4bbf80:8", "const:4:8"]]
+ 004bbf80 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bbc60 bytes e0701e94
+ 004bbf80 bytes 0c741e94
- 004bbc0c ["INT_ADD", "register:40f0:8", ["const:4bbc0c:8", "const:4:8"]]
- 004bbc0c ["CALL", null, ["callee:00c58f90:8"]]
+ 004bbf2c ["INT_ADD", "register:40f0:8", ["const:4bbf2c:8", "const:4:8"]]
+ 004bbf2c ["CALL", null, ["callee:00c58f90:8"]]
- 004bbc0c bytes ed701e94
+ 004bbf2c bytes 19741e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ef60608b4342380b8d592d2326b8dd"></a>

### [`004bc040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md) → [`004bc360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc360.md) _ZN5Botan11BlockCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bc3d8",
      "incomplete_value": false,
      "site": "004bc3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:18b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc0b8",
      "incomplete_value": false,
      "site": "004bc0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "definition_site": "004bc418",
      "incomplete_value": true,
      "site": "004bc424",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc0f8",
      "incomplete_value": true,
      "site": "004bc104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
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
      "definition_site": "004bc414",
      "incomplete_value": false,
      "site": "004bc424",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bc0f4",
      "incomplete_value": false,
      "site": "004bc104",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bc3d8",
      "PARAM",
      [
        "storage",
        "002a40c0",
        null,
        "string"
      ]
    ],
    [
      "004bc414",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bc418",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bc3d8",
      "PARAM",
      [
        "storage",
        "002a418b",
        null,
        "string"
      ]
    ],
    [
      "004bc414",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bc418",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md#insn-004bc0c0) · [`004bc104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md#insn-004bc104) · [`004bc074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md#insn-004bc074)
- 新版 [`004bc3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc360.md#insn-004bc3e0) · [`004bc424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc360.md#insn-004bc424) · [`004bc394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc360.md#insn-004bc394)

~~~diff
- 004bc0c0 ["INT_ADD", "register:40f0:8", ["const:4bc0c0:8", "const:4:8"]]
- 004bc0c0 ["CALL", null, ["callee:0043e138:8"]]
+ 004bc3e0 ["INT_ADD", "register:40f0:8", ["const:4bc3e0:8", "const:4:8"]]
+ 004bc3e0 ["CALL", null, ["callee:0043e138:8"]]
- 004bc0c0 bytes 5607fe97
+ 004bc3e0 bytes 5607fe97
- 004bc104 ["INT_ADD", "register:40f0:8", ["const:4bc104:8", "const:4:8"]]
- 004bc104 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bc424 ["INT_ADD", "register:40f0:8", ["const:4bc424:8", "const:4:8"]]
+ 004bc424 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bc104 bytes b76f1e94
+ 004bc424 bytes e3721e94
- 004bc074 ["INT_ADD", "register:40f0:8", ["const:4bc074:8", "const:4:8"]]
- 004bc074 ["CALL", null, ["callee:00c59dd0:8"]]
+ 004bc394 ["INT_ADD", "register:40f0:8", ["const:4bc394:8", "const:4:8"]]
+ 004bc394 ["CALL", null, ["callee:00c59dd0:8"]]
- 004bc074 bytes 63731e94
+ 004bc394 bytes 8f761e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97d3792b3e4e757791ccc2029ce25f72"></a>

### [`004bc3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md) → [`004bc718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc718.md) _ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e30.md) · 呼出先 9件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c59e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e00.md) · 呼出先 9件 [`004a6bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6bac.md) [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.64% / 新版 93.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bc750",
      "incomplete_value": true,
      "site": "004bc750",
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
      "definition_site": "004bc430",
      "incomplete_value": true,
      "site": "004bc430",
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
      "definition_site": "004bc7f4",
      "incomplete_value": false,
      "site": "004bc800",
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
            "const:411:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc4d4",
      "incomplete_value": false,
      "site": "004bc4e0",
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
            "const:333:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bc820",
      "incomplete_value": false,
      "site": "004bc828",
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
            "const:c87:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc500",
      "incomplete_value": false,
      "site": "004bc508",
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
            "const:bba:8"
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
      "004bc740",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "004bc750",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc7f4",
      "PARAM",
      [
        "storage",
        "002bb333",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc740",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "004bc750",
      "DATA",
      [
        "storage",
        "00c674c0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc7f4",
      "PARAM",
      [
        "storage",
        "002bb411",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md#insn-004bc4e0) · [`004bc508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md#insn-004bc508) · [`004bc554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md#insn-004bc554)
- 新版 [`004bc800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc718.md#insn-004bc800) · [`004bc828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc718.md#insn-004bc828) · [`004bc874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bc718.md#insn-004bc874)

~~~diff
- 004bc4e0 ["INT_ADD", "register:40f0:8", ["const:4bc4e0:8", "const:4:8"]]
- 004bc4e0 ["CALL", null, ["callee:00c59000:8"]]
+ 004bc800 ["INT_ADD", "register:40f0:8", ["const:4bc800:8", "const:4:8"]]
+ 004bc800 ["CALL", null, ["callee:00c59000:8"]]
- 004bc4e0 bytes d46e1e94
+ 004bc800 bytes 00721e94
- 004bc508 ["INT_ADD", "register:40f0:8", ["const:4bc508:8", "const:4:8"]]
- 004bc508 ["CALL", null, ["callee:00c59010:8"]]
+ 004bc828 ["INT_ADD", "register:40f0:8", ["const:4bc828:8", "const:4:8"]]
+ 004bc828 ["CALL", null, ["callee:00c59010:8"]]
- 004bc508 bytes ce6e1e94
+ 004bc828 bytes fa711e94
- 004bc554 ["INT_ADD", "register:40f0:8", ["const:4bc554:8", "const:4:8"]]
- 004bc554 ["CALL", null, ["callee:00c59010:8"]]
+ 004bc874 ["INT_ADD", "register:40f0:8", ["const:4bc874:8", "const:4:8"]]
+ 004bc874 ["CALL", null, ["callee:00c59010:8"]]
- 004bc554 bytes bb6e1e94
+ 004bc874 bytes e7711e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3f73bbc16aaad5cc67d7cddd441755c"></a>

### [`004bc778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md) → [`004bca98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bca98.md) _ZNK5Botan8CBC_Mode4nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e40.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c59e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e10.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bcae0",
      "incomplete_value": false,
      "site": "004bcae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc7c0",
      "incomplete_value": false,
      "site": "004bc7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:cd:8"
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
      "definition_site": "004bcb8c",
      "incomplete_value": false,
      "site": "004bcb94",
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
            "const:1d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc86c",
      "incomplete_value": false,
      "site": "004bc874",
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
            "const:fdd:8"
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
      "definition_site": "004bcc20",
      "incomplete_value": false,
      "site": "004bcc40",
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
            "const:913:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc900",
      "incomplete_value": false,
      "site": "004bc920",
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
            "const:846:8"
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
      "004bcae0",
      "PARAM",
      [
        "storage",
        "002a40cd",
        null,
        "string"
      ]
    ],
    [
      "004bcb8c",
      "PARAM",
      [
        "storage",
        "0029ffdd",
        null,
        "string"
      ]
    ],
    [
      "004bcc20",
      "PARAM",
      [
        "storage",
        "002ac846",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcae0",
      "PARAM",
      [
        "storage",
        "002a4198",
        null,
        "string"
      ]
    ],
    [
      "004bcb8c",
      "PARAM",
      [
        "storage",
        "002a001d",
        null,
        "string"
      ]
    ],
    [
      "004bcc20",
      "PARAM",
      [
        "storage",
        "002ac913",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md#insn-004bc7c8) · [`004bc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md#insn-004bc874) · [`004bc920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md#insn-004bc920)
- 新版 [`004bcae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bca98.md#insn-004bcae8) · [`004bcb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bca98.md#insn-004bcb94) · [`004bcc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bca98.md#insn-004bcc40)

~~~diff
- 004bc7c8 ["INT_ADD", "register:40f0:8", ["const:4bc7c8:8", "const:4:8"]]
- 004bc7c8 ["CALL", null, ["callee:00c59010:8"]]
+ 004bcae8 ["INT_ADD", "register:40f0:8", ["const:4bcae8:8", "const:4:8"]]
+ 004bcae8 ["CALL", null, ["callee:00c59010:8"]]
- 004bc7c8 bytes 1e6e1e94
+ 004bcae8 bytes 4a711e94
- 004bc874 ["INT_ADD", "register:40f0:8", ["const:4bc874:8", "const:4:8"]]
- 004bc874 ["CALL", null, ["callee:00c59010:8"]]
+ 004bcb94 ["INT_ADD", "register:40f0:8", ["const:4bcb94:8", "const:4:8"]]
+ 004bcb94 ["CALL", null, ["callee:00c59010:8"]]
- 004bc874 bytes f36d1e94
+ 004bcb94 bytes 1f711e94
- 004bc920 ["INT_ADD", "register:40f0:8", ["const:4bc920:8", "const:4:8"]]
- 004bc920 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bcc40 ["INT_ADD", "register:40f0:8", ["const:4bcc40:8", "const:4:8"]]
+ 004bcc40 ["CALL", null, ["callee:00c596f0:8"]]
- 004bc920 bytes 806f1e94
+ 004bcc40 bytes ac721e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2766cb9103d51acb04256f9781873d00"></a>

### [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) → [`004bcd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md) FUN_004bcd60

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`004bca38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca38.md) [`004bf484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf484.md) [`004c40a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md) [`004c44e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md) [`004c4d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md) · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e50.md)
- 新版 呼出元 10件 [`004bcd58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd58.md) [`004bf7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf7a4.md) [`004c43c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c43c8.md) [`004c4808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4808.md) [`004c506c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c506c.md) · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "004bce58",
      "incomplete_value": true,
      "site": "004bce64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcb38",
      "incomplete_value": true,
      "site": "004bcb44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "definition_site": "004bce54",
      "incomplete_value": false,
      "site": "004bce64",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bcb34",
      "incomplete_value": false,
      "site": "004bcb44",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bce54",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bce58",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "004bce58",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bce54",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bce58",
      "READ",
      [
        "storage",
        "00c9bed8",
        null,
        "pointer"
      ]
    ],
    [
      "004bce58",
      "PARAM",
      [
        "storage",
        "00c67ec8",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md#insn-004bcb44) · [`004bca78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md#insn-004bca78) · [`004bcab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md#insn-004bcab8)
- 新版 [`004bce64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md#insn-004bce64) · [`004bcd98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md#insn-004bcd98) · [`004bcdd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md#insn-004bcdd8)

~~~diff
- 004bcb44 ["INT_ADD", "register:40f0:8", ["const:4bcb44:8", "const:4:8"]]
- 004bcb44 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bce64 ["INT_ADD", "register:40f0:8", ["const:4bce64:8", "const:4:8"]]
+ 004bce64 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bcb44 bytes 276d1e94
+ 004bce64 bytes 53701e94
- 004bca78 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bca78 ["INT_ADD", "register:40f0:8", ["const:4bca78:8", "const:4:8"]]
- 004bca78 ["CALLIND", null, ["register:0:8"]]
+ 004bcd98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bcd98 ["INT_ADD", "register:40f0:8", ["const:4bcd98:8", "const:4:8"]]
+ 004bcd98 ["CALLIND", null, ["register:0:8"]]
- 004bca78 bytes 20013fd6
+ 004bcd98 bytes 20013fd6
- 004bcab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bcab8 ["INT_ADD", "register:40f0:8", ["const:4bcab8:8", "const:4:8"]]
- 004bcab8 ["CALLIND", null, ["register:0:8"]]
+ 004bcdd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcdd8 ["INT_ADD", "register:40f0:8", ["const:4bcdd8:8", "const:4:8"]]
+ 004bcdd8 ["CALLIND", null, ["register:0:8"]]
- 004bcab8 bytes 00013fd6
+ 004bcdd8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17bbdc06301a614e3a924ef0e987001"></a>

### [`004bcb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md) → [`004bceb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bceb4.md) _ZN5Botan8CBC_Mode9start_msgEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00543720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

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
      "definition_site": "004bcfa4",
      "incomplete_value": true,
      "site": "004bcfb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcc84",
      "incomplete_value": true,
      "site": "004bcc90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "definition_site": "004bcfa0",
      "incomplete_value": false,
      "site": "004bcfb0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bcc80",
      "incomplete_value": false,
      "site": "004bcc90",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bcfa0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bcfa4",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004bcfa4",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcfa0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bcfa4",
      "READ",
      [
        "storage",
        "00c9bee0",
        null,
        "pointer"
      ]
    ],
    [
      "004bcfa4",
      "PARAM",
      [
        "storage",
        "00c67550",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md#insn-004bcc90) · [`004bcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md#insn-004bcbcc) · [`004bcc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md#insn-004bcc34)
- 新版 [`004bcfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bceb4.md#insn-004bcfb0) · [`004bceec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bceb4.md#insn-004bceec) · [`004bcf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bceb4.md#insn-004bcf54)

~~~diff
- 004bcc90 ["INT_ADD", "register:40f0:8", ["const:4bcc90:8", "const:4:8"]]
- 004bcc90 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bcfb0 ["INT_ADD", "register:40f0:8", ["const:4bcfb0:8", "const:4:8"]]
+ 004bcfb0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bcc90 bytes d46c1e94
+ 004bcfb0 bytes 00701e94
- 004bcbcc ["COPY", "register:0:8", ["register:4040:8"]]
- 004bcbcc ["INT_ADD", "register:40f0:8", ["const:4bcbcc:8", "const:4:8"]]
- 004bcbcc ["CALLIND", null, ["register:0:8"]]
+ 004bceec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bceec ["INT_ADD", "register:40f0:8", ["const:4bceec:8", "const:4:8"]]
+ 004bceec ["CALLIND", null, ["register:0:8"]]
- 004bcbcc bytes 00013fd6
+ 004bceec bytes 00013fd6
- 004bcc34 ["INT_ADD", "register:40f0:8", ["const:4bcc34:8", "const:4:8"]]
- 004bcc34 ["CALL", null, ["callee:00c58f90:8"]]
+ 004bcf54 ["INT_ADD", "register:40f0:8", ["const:4bcf54:8", "const:4:8"]]
+ 004bcf54 ["CALL", null, ["callee:00c58f90:8"]]
- 004bcc34 bytes e36c1e94
+ 004bcf54 bytes 0f701e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d74b9ca74fc5f935ad5c50f007ff327f"></a>

### [`004bcce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md) → [`004bd008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd008.md) _ZNK5Botan14CBC_Encryption13output_lengthEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd048",
      "incomplete_value": false,
      "site": "004bd068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcd28",
      "incomplete_value": false,
      "site": "004bcd48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:72:8"
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
      "definition_site": "004bd050",
      "incomplete_value": false,
      "site": "004bd068",
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
            "const:62e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcd30",
      "incomplete_value": false,
      "site": "004bcd48",
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
            "const:561:8"
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
      "definition_site": "004bd058",
      "incomplete_value": false,
      "site": "004bd068",
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
            "const:3b4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcd38",
      "incomplete_value": false,
      "site": "004bcd48",
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
            "const:2e5:8"
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
      "004bd048",
      "PARAM",
      [
        "storage",
        "002a2072",
        null,
        "string"
      ]
    ],
    [
      "004bd050",
      "PARAM",
      [
        "storage",
        "002ab561",
        null,
        "string"
      ]
    ],
    [
      "004bd058",
      "PARAM",
      [
        "storage",
        "002b82e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd048",
      "PARAM",
      [
        "storage",
        "002a20b2",
        null,
        "string"
      ]
    ],
    [
      "004bd050",
      "PARAM",
      [
        "storage",
        "002ab62e",
        null,
        "string"
      ]
    ],
    [
      "004bd058",
      "PARAM",
      [
        "storage",
        "002b83b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md#insn-004bcd48) · [`004bcd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md#insn-004bcd28) · [`004bcd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md#insn-004bcd30)
- 新版 [`004bd068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd008.md#insn-004bd068) · [`004bd048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd008.md#insn-004bd048) · [`004bd050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd008.md#insn-004bd050)

~~~diff
- 004bcd48 ["INT_ADD", "register:40f0:8", ["const:4bcd48:8", "const:4:8"]]
- 004bcd48 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bd068 ["INT_ADD", "register:40f0:8", ["const:4bd068:8", "const:4:8"]]
+ 004bd068 ["CALL", null, ["callee:00c596f0:8"]]
- 004bcd48 bytes 766e1e94
+ 004bd068 bytes a2711e94
- 004bcd28 ["COPY", "tmp:0:8", ["const:72:8"]]
- 004bcd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bcd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bcd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bd048 ["COPY", "tmp:0:8", ["const:b2:8"]]
+ 004bd048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bd048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bd048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bcd28 bytes 00c80191
+ 004bd048 bytes 00c80291
- 004bcd30 ["COPY", "tmp:0:8", ["const:561:8"]]
- 004bcd30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bcd30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bcd30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bd050 ["COPY", "tmp:0:8", ["const:62e:8"]]
+ 004bd050 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bd050 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bd050 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bcd30 bytes 21841591
+ 004bd050 bytes 21b81891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcdb257f7840a3d04a82e6a64d676828"></a>

### [`004bcd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md) → [`004bd06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd06c.md) _ZN5Botan14CBC_Encryption7processEPhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00543898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543bb8.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.42% / 新版 97.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd2b4",
      "incomplete_value": false,
      "site": "004bd2d4",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcf94",
      "incomplete_value": false,
      "site": "004bcfb4",
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
            "const:bc4:8"
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
      "definition_site": "004bd2bc",
      "incomplete_value": false,
      "site": "004bd2d4",
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
            "const:26:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcf9c",
      "incomplete_value": false,
      "site": "004bcfb4",
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
            "const:fe6:8"
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
      "definition_site": "004bd2c4",
      "incomplete_value": false,
      "site": "004bd2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcfa4",
      "incomplete_value": false,
      "site": "004bcfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:d3:8"
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
      "004bd2b4",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bd2bc",
      "PARAM",
      [
        "storage",
        "0029ffe6",
        null,
        "string"
      ]
    ],
    [
      "004bd2c4",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd2b4",
      "PARAM",
      [
        "storage",
        "002a8d1c",
        null,
        "string"
      ]
    ],
    [
      "004bd2bc",
      "PARAM",
      [
        "storage",
        "002a0026",
        null,
        "string"
      ]
    ],
    [
      "004bd2c4",
      "PARAM",
      [
        "storage",
        "002a419e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md#insn-004bcfb4) · [`004bce2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md#insn-004bce2c) · [`004bce48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md#insn-004bce48)
- 新版 [`004bd2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd06c.md#insn-004bd2d4) · [`004bd14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd06c.md#insn-004bd14c) · [`004bd168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd06c.md#insn-004bd168)

~~~diff
- 004bcfb4 ["INT_ADD", "register:40f0:8", ["const:4bcfb4:8", "const:4:8"]]
- 004bcfb4 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bd2d4 ["INT_ADD", "register:40f0:8", ["const:4bd2d4:8", "const:4:8"]]
+ 004bd2d4 ["CALL", null, ["callee:00c596f0:8"]]
- 004bcfb4 bytes db6d1e94
+ 004bd2d4 bytes 07711e94
- 004bce2c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bce2c ["INT_ADD", "register:40f0:8", ["const:4bce2c:8", "const:4:8"]]
- 004bce2c ["CALLIND", null, ["register:0:8"]]
+ 004bd14c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bd14c ["INT_ADD", "register:40f0:8", ["const:4bd14c:8", "const:4:8"]]
+ 004bd14c ["CALLIND", null, ["register:0:8"]]
- 004bce2c bytes 00013fd6
+ 004bd14c bytes 00013fd6
- 004bce48 ["INT_ADD", "register:40f0:8", ["const:4bce48:8", "const:4:8"]]
- 004bce48 ["CALL", null, ["callee:00543bb8:8"]]
+ 004bd168 ["INT_ADD", "register:40f0:8", ["const:4bd168:8", "const:4:8"]]
+ 004bd168 ["CALL", null, ["callee:00543bb8:8"]]
- 004bce48 bytes 941a0294
+ 004bd168 bytes 941a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2320e8f4ac5f3fcc89f359bea714a8a9"></a>

### [`004bcfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md) → [`004bd2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd2d8.md) _ZN5Botan14CBC_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.34% / 新版 90.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd3fc",
      "incomplete_value": false,
      "site": "004bd41c",
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
            "const:7d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd0dc",
      "incomplete_value": false,
      "site": "004bd0fc",
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
            "const:709:8"
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
      "definition_site": "004bd404",
      "incomplete_value": false,
      "site": "004bd41c",
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
            "const:e2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd0e4",
      "incomplete_value": false,
      "site": "004bd0fc",
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
            "const:d4e:8"
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
      "definition_site": "004bd40c",
      "incomplete_value": false,
      "site": "004bd41c",
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
            "const:2d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd0ec",
      "incomplete_value": false,
      "site": "004bd0fc",
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
            "const:1f9:8"
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
      "004bd3fc",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004bd404",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ],
    [
      "004bd40c",
      "PARAM",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd3fc",
      "PARAM",
      [
        "storage",
        "002ad7d6",
        null,
        "string"
      ]
    ],
    [
      "004bd404",
      "PARAM",
      [
        "storage",
        "002b4e2c",
        null,
        "string"
      ]
    ],
    [
      "004bd40c",
      "PARAM",
      [
        "storage",
        "002ba2d7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md#insn-004bd0fc) · [`004bd134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md#insn-004bd134) · [`004bd168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md#insn-004bd168)
- 新版 [`004bd41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd2d8.md#insn-004bd41c) · [`004bd454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd2d8.md#insn-004bd454) · [`004bd488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd2d8.md#insn-004bd488)

~~~diff
- 004bd0fc ["INT_ADD", "register:40f0:8", ["const:4bd0fc:8", "const:4:8"]]
- 004bd0fc ["CALL", null, ["callee:00c596f0:8"]]
+ 004bd41c ["INT_ADD", "register:40f0:8", ["const:4bd41c:8", "const:4:8"]]
+ 004bd41c ["CALL", null, ["callee:00c596f0:8"]]
- 004bd0fc bytes 896d1e94
+ 004bd41c bytes b5701e94
- 004bd134 ["INT_ADD", "register:40f0:8", ["const:4bd134:8", "const:4:8"]]
- 004bd134 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bd454 ["INT_ADD", "register:40f0:8", ["const:4bd454:8", "const:4:8"]]
+ 004bd454 ["CALL", null, ["callee:00c596f0:8"]]
- 004bd134 bytes 7b6d1e94
+ 004bd454 bytes a7701e94
- 004bd168 ["INT_ADD", "register:40f0:8", ["const:4bd168:8", "const:4:8"]]
- 004bd168 ["CALL", null, ["callee:00c59000:8"]]
+ 004bd488 ["INT_ADD", "register:40f0:8", ["const:4bd488:8", "const:4:8"]]
+ 004bd488 ["CALL", null, ["callee:00c59000:8"]]
- 004bd168 bytes b26b1e94
+ 004bd488 bytes de6e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40166e7ed193976efb0bffeb47e6bf40"></a>

### [`004bd298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md) → [`004bd5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd5b8.md) _ZN5Botan14CTS_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00540604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd870",
      "incomplete_value": true,
      "site": "004bd870",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd550",
      "incomplete_value": true,
      "site": "004bd550",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd930",
      "incomplete_value": false,
      "site": "004bd950",
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
            "const:7d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd610",
      "incomplete_value": false,
      "site": "004bd630",
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
            "const:709:8"
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
      "definition_site": "004bd938",
      "incomplete_value": false,
      "site": "004bd950",
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
            "const:e2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd618",
      "incomplete_value": false,
      "site": "004bd630",
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
            "const:d4e:8"
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
      "004bd860",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004bd930",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004bd938",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd860",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004bd930",
      "PARAM",
      [
        "storage",
        "002ad7d6",
        null,
        "string"
      ]
    ],
    [
      "004bd938",
      "PARAM",
      [
        "storage",
        "002b4e2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md#insn-004bd550) · [`004bd630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md#insn-004bd630) · [`004bd658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md#insn-004bd658)
- 新版 [`004bd870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd5b8.md#insn-004bd870) · [`004bd950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd5b8.md#insn-004bd950) · [`004bd978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd5b8.md#insn-004bd978)

~~~diff
- 004bd550 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bd550 ["INT_ADD", "register:40f0:8", ["const:4bd550:8", "const:4:8"]]
- 004bd550 ["CALLIND", null, ["register:0:8"]]
+ 004bd870 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bd870 ["INT_ADD", "register:40f0:8", ["const:4bd870:8", "const:4:8"]]
+ 004bd870 ["CALLIND", null, ["register:0:8"]]
- 004bd550 bytes 20013fd6
+ 004bd870 bytes 20013fd6
- 004bd630 ["INT_ADD", "register:40f0:8", ["const:4bd630:8", "const:4:8"]]
- 004bd630 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bd950 ["INT_ADD", "register:40f0:8", ["const:4bd950:8", "const:4:8"]]
+ 004bd950 ["CALL", null, ["callee:00c596f0:8"]]
- 004bd630 bytes 3c6c1e94
+ 004bd950 bytes 686f1e94
- 004bd658 ["INT_ADD", "register:40f0:8", ["const:4bd658:8", "const:4:8"]]
- 004bd658 ["CALL", null, ["callee:00c59010:8"]]
+ 004bd978 ["INT_ADD", "register:40f0:8", ["const:4bd978:8", "const:4:8"]]
+ 004bd978 ["CALL", null, ["callee:00c59010:8"]]
- 004bd658 bytes 7a6a1e94
+ 004bd978 bytes a66d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4848475102424115203c06f077fd3d15"></a>

### [`004bd7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md) → [`004bdadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdadc.md) _ZN5Botan14CBC_Decryption7processEPhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdd0c",
      "incomplete_value": false,
      "site": "004bdd2c",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd9ec",
      "incomplete_value": false,
      "site": "004bda0c",
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
            "const:bc4:8"
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
      "definition_site": "004bdd14",
      "incomplete_value": false,
      "site": "004bdd2c",
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
            "const:ba2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd9f4",
      "incomplete_value": false,
      "site": "004bda0c",
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
            "const:acb:8"
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
      "definition_site": "004bdd1c",
      "incomplete_value": false,
      "site": "004bdd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd9fc",
      "incomplete_value": false,
      "site": "004bda0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:d3:8"
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
      "004bdd0c",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bdd14",
      "PARAM",
      [
        "storage",
        "002b0acb",
        null,
        "string"
      ]
    ],
    [
      "004bdd1c",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bdd0c",
      "PARAM",
      [
        "storage",
        "002a8d1c",
        null,
        "string"
      ]
    ],
    [
      "004bdd14",
      "PARAM",
      [
        "storage",
        "002b0ba2",
        null,
        "string"
      ]
    ],
    [
      "004bdd1c",
      "PARAM",
      [
        "storage",
        "002a419e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bda0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md#insn-004bda0c) · [`004bd854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md#insn-004bd854) · [`004bd95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md#insn-004bd95c)
- 新版 [`004bdd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdadc.md#insn-004bdd2c) · [`004bdb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdadc.md#insn-004bdb74) · [`004bdc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdadc.md#insn-004bdc7c)

~~~diff
- 004bda0c ["INT_ADD", "register:40f0:8", ["const:4bda0c:8", "const:4:8"]]
- 004bda0c ["CALL", null, ["callee:00c596f0:8"]]
+ 004bdd2c ["INT_ADD", "register:40f0:8", ["const:4bdd2c:8", "const:4:8"]]
+ 004bdd2c ["CALL", null, ["callee:00c596f0:8"]]
- 004bda0c bytes 456b1e94
+ 004bdd2c bytes 716e1e94
- 004bd854 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bd854 ["INT_ADD", "register:40f0:8", ["const:4bd854:8", "const:4:8"]]
- 004bd854 ["CALLIND", null, ["register:0:8"]]
+ 004bdb74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bdb74 ["INT_ADD", "register:40f0:8", ["const:4bdb74:8", "const:4:8"]]
+ 004bdb74 ["CALLIND", null, ["register:0:8"]]
- 004bd854 bytes 00013fd6
+ 004bdb74 bytes 00013fd6
- 004bd95c ["INT_ADD", "register:40f0:8", ["const:4bd95c:8", "const:4:8"]]
- 004bd95c ["CALL", null, ["callee:00c58fe0:8"]]
+ 004bdc7c ["INT_ADD", "register:40f0:8", ["const:4bdc7c:8", "const:4:8"]]
+ 004bdc7c ["CALL", null, ["callee:00c58fe0:8"]]
- 004bd95c bytes ad691e94
+ 004bdc7c bytes d96c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b9e3acdf1da4c71739920f56e95e2d1"></a>

### [`004bda10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md) → [`004bdd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdd30.md) _ZN5Botan14CBC_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.30% / 新版 94.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdf00",
      "incomplete_value": false,
      "site": "004bdf08",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bdbe0",
      "incomplete_value": false,
      "site": "004bdbe8",
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
            "const:93:8"
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
      "definition_site": "004bdf50",
      "incomplete_value": true,
      "site": "004bdf5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004bdc30",
      "incomplete_value": true,
      "site": "004bdc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdf4c",
      "incomplete_value": false,
      "site": "004bdf5c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bdc2c",
      "incomplete_value": false,
      "site": "004bdc3c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bdf00",
      "PARAM",
      [
        "storage",
        "002c1093",
        null,
        "string"
      ]
    ],
    [
      "004bdf4c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bdf50",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bdf00",
      "PARAM",
      [
        "storage",
        "002c10dd",
        null,
        "string"
      ]
    ],
    [
      "004bdf4c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bdf50",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bdbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md#insn-004bdbe8) · [`004bdc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md#insn-004bdc3c) · [`004bdc78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md#insn-004bdc78)
- 新版 [`004bdf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdd30.md#insn-004bdf08) · [`004bdf5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdd30.md#insn-004bdf5c) · [`004bdf98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bdd30.md#insn-004bdf98)

~~~diff
- 004bdbe8 ["INT_ADD", "register:40f0:8", ["const:4bdbe8:8", "const:4:8"]]
- 004bdbe8 ["CALL", null, ["callee:00c59010:8"]]
+ 004bdf08 ["INT_ADD", "register:40f0:8", ["const:4bdf08:8", "const:4:8"]]
+ 004bdf08 ["CALL", null, ["callee:00c59010:8"]]
- 004bdbe8 bytes 16691e94
+ 004bdf08 bytes 426c1e94
- 004bdc3c ["INT_ADD", "register:40f0:8", ["const:4bdc3c:8", "const:4:8"]]
- 004bdc3c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bdf5c ["INT_ADD", "register:40f0:8", ["const:4bdf5c:8", "const:4:8"]]
+ 004bdf5c ["CALL", null, ["callee:00c58fb0:8"]]
- 004bdc3c bytes e9681e94
+ 004bdf5c bytes 156c1e94
- 004bdc78 ["INT_ADD", "register:40f0:8", ["const:4bdc78:8", "const:4:8"]]
- 004bdc78 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bdf98 ["INT_ADD", "register:40f0:8", ["const:4bdf98:8", "const:4:8"]]
+ 004bdf98 ["CALL", null, ["callee:00c596f0:8"]]
- 004bdc78 bytes aa6a1e94
+ 004bdf98 bytes d66d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d3b4d9d6404c92dfc0c0fbfa3295e78"></a>

### [`004bde1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md) → [`004be13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be13c.md) _ZN5Botan14CTS_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00540604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.99% / 新版 94.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004be4c0",
      "incomplete_value": true,
      "site": "004be4c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be1a0",
      "incomplete_value": true,
      "site": "004be1a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004be58c",
      "incomplete_value": false,
      "site": "004be5ac",
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
            "const:7d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be26c",
      "incomplete_value": false,
      "site": "004be28c",
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
            "const:709:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004be594",
      "incomplete_value": false,
      "site": "004be5ac",
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
            "const:e2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be274",
      "incomplete_value": false,
      "site": "004be28c",
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
            "const:d4e:8"
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
      "004be4b0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004be58c",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004be594",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004be4b0",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004be58c",
      "PARAM",
      [
        "storage",
        "002ad7d6",
        null,
        "string"
      ]
    ],
    [
      "004be594",
      "PARAM",
      [
        "storage",
        "002b4e2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md#insn-004be1a0) · [`004be28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md#insn-004be28c) · [`004be2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md#insn-004be2b4)
- 新版 [`004be4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be13c.md#insn-004be4c0) · [`004be5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be13c.md#insn-004be5ac) · [`004be5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be13c.md#insn-004be5d4)

~~~diff
- 004be1a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004be1a0 ["INT_ADD", "register:40f0:8", ["const:4be1a0:8", "const:4:8"]]
- 004be1a0 ["CALLIND", null, ["register:0:8"]]
+ 004be4c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004be4c0 ["INT_ADD", "register:40f0:8", ["const:4be4c0:8", "const:4:8"]]
+ 004be4c0 ["CALLIND", null, ["register:0:8"]]
- 004be1a0 bytes 20013fd6
+ 004be4c0 bytes 20013fd6
- 004be28c ["INT_ADD", "register:40f0:8", ["const:4be28c:8", "const:4:8"]]
- 004be28c ["CALL", null, ["callee:00c596f0:8"]]
+ 004be5ac ["INT_ADD", "register:40f0:8", ["const:4be5ac:8", "const:4:8"]]
+ 004be5ac ["CALL", null, ["callee:00c596f0:8"]]
- 004be28c bytes 25691e94
+ 004be5ac bytes 516c1e94
- 004be2b4 ["INT_ADD", "register:40f0:8", ["const:4be2b4:8", "const:4:8"]]
- 004be2b4 ["CALL", null, ["callee:00c59010:8"]]
+ 004be5d4 ["INT_ADD", "register:40f0:8", ["const:4be5d4:8", "const:4:8"]]
+ 004be5d4 ["CALL", null, ["callee:00c59010:8"]]
- 004be2b4 bytes 63671e94
+ 004be5d4 bytes 8f6a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b93878bff778eb62e49774b96b58c289"></a>

### [`004be464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md) → [`004be784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be784.md) _ZN5Botan5CPUID9to_stringEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e70.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c59e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e40.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004beb34",
      "incomplete_value": true,
      "site": "004beb34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be814",
      "incomplete_value": true,
      "site": "004be814",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bebf4",
      "incomplete_value": true,
      "site": "004bebf4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be8d4",
      "incomplete_value": true,
      "site": "004be8d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004be7c8",
      "incomplete_value": true,
      "site": "004be7c8",
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
      "definition_site": "004be4a8",
      "incomplete_value": true,
      "site": "004be4a8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004be7b4",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004be7bc",
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be8d4",
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004be7b4",
      "READ",
      [
        "storage",
        "00c9bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "004be7bc",
      "READ",
      [
        "storage",
        "00ca62f8",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be8d4",
      "READ",
      [
        "storage",
        "00ca62f8",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md#insn-004be48c) · [`004be494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md#insn-004be494) · [`004be4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md#insn-004be4c8)
- 新版 [`004be7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be784.md#insn-004be7ac) · [`004be7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be784.md#insn-004be7b4) · [`004be7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004be784.md#insn-004be7e8)

~~~diff
- 004be48c ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 004be7ac ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 004be48c bytes f83e0090
+ 004be7ac bytes f83e00b0
- 004be494 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:de8:8"]]
- 004be494 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004be7b4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:db8:8"]]
+ 004be7b4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004be494 bytes 18f746f9
+ 004be7b4 bytes 18df46f9
- 004be4c8 ["INT_ADD", "register:40f0:8", ["const:4be4c8:8", "const:4:8"]]
- 004be4c8 ["CALL", null, ["callee:00c58f30:8"]]
+ 004be7e8 ["INT_ADD", "register:40f0:8", ["const:4be7e8:8", "const:4:8"]]
+ 004be7e8 ["CALL", null, ["callee:00c58f30:8"]]
- 004be4c8 bytes a6661e94
+ 004be7e8 bytes d2691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d10cd7ea5fc7abd7e69e94166e3246d4"></a>

### [`004bebdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md) → [`004beefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beefc.md) _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bef18",
      "incomplete_value": false,
      "site": "004bef28",
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
            "const:6c4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bebf8",
      "incomplete_value": false,
      "site": "004bec08",
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
            "const:56c:8"
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
      "definition_site": "004bef60",
      "incomplete_value": false,
      "site": "004bef68",
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
            "const:cef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bec40",
      "incomplete_value": false,
      "site": "004bec48",
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
            "const:c11:8"
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
      "004bef18",
      "PARAM",
      [
        "storage",
        "002a656c",
        null,
        "string"
      ]
    ],
    [
      "004bef60",
      "PARAM",
      [
        "storage",
        "002b4c11",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004bef18",
      "PARAM",
      [
        "storage",
        "002a66c4",
        null,
        "string"
      ]
    ],
    [
      "004bef60",
      "PARAM",
      [
        "storage",
        "002b4cef",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bec08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md#insn-004bec08) · [`004bec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md#insn-004bec48) · [`004bebf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md#insn-004bebf8)
- 新版 [`004bef28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beefc.md#insn-004bef28) · [`004bef68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beefc.md#insn-004bef68) · [`004bef18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beefc.md#insn-004bef18)

~~~diff
- 004bec08 ["INT_ADD", "register:40f0:8", ["const:4bec08:8", "const:4:8"]]
- 004bec08 ["CALL", null, ["callee:00459830:8"]]
+ 004bef28 ["INT_ADD", "register:40f0:8", ["const:4bef28:8", "const:4:8"]]
+ 004bef28 ["CALL", null, ["callee:00459830:8"]]
- 004bec08 bytes 426afe97
+ 004bef28 bytes 426afe97
- 004bec48 ["INT_ADD", "register:40f0:8", ["const:4bec48:8", "const:4:8"]]
- 004bec48 ["CALL", null, ["callee:00459830:8"]]
+ 004bef68 ["INT_ADD", "register:40f0:8", ["const:4bef68:8", "const:4:8"]]
+ 004bef68 ["CALL", null, ["callee:00459830:8"]]
- 004bec48 bytes 326afe97
+ 004bef68 bytes 326afe97
- 004bebf8 ["COPY", "tmp:0:8", ["const:56c:8"]]
- 004bebf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bebf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bebf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bef18 ["COPY", "tmp:0:8", ["const:6c4:8"]]
+ 004bef18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bef18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bef18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bebf8 bytes 21b01591
+ 004bef18 bytes 21101b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c00901682eeabd9a47d453f605e3b27e"></a>

### [`004becb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becb0.md) → [`004befd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004befd0.md) _ZN5Botan5CPUID10initializeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "004befdc",
      "incomplete_value": true,
      "site": "004befdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004becbc",
      "incomplete_value": true,
      "site": "004becbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
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
      "004befd8",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004befdc",
      "WRITE",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004befd8",
      "READ",
      [
        "storage",
        "00c9bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "004befdc",
      "WRITE",
      [
        "storage",
        "00ca62f8",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004becb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becb0.md#insn-004becb0) · [`004becb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becb0.md#insn-004becb8)
- 新版 [`004befd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004befd0.md#insn-004befd0) · [`004befd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004befd0.md#insn-004befd8)

~~~diff
- 004becb0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004befd0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004becb0 bytes e83e0090
+ 004befd0 bytes e83e00b0
- 004becb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de8:8"]]
- 004becb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004befd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 004befd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004becb8 bytes 08f546f9
+ 004befd8 bytes 08dd46f9
~~~


<a id="compare-5a4aca9fc5653a28112eedd1ff627097"></a>

### [`004bef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md) → [`004bf28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf28c.md) _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e80.md) · 呼出先 8件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e50.md) · 呼出先 8件 [`004a6bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6bac.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bf2c8",
      "incomplete_value": true,
      "site": "004bf2c8",
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
      "definition_site": "004befa8",
      "incomplete_value": true,
      "site": "004befa8",
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
      "definition_site": "004bf348",
      "incomplete_value": false,
      "site": "004bf354",
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
            "const:411:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf028",
      "incomplete_value": false,
      "site": "004bf034",
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
            "const:333:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf374",
      "incomplete_value": false,
      "site": "004bf37c",
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
            "const:c87:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf054",
      "incomplete_value": false,
      "site": "004bf05c",
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
            "const:bba:8"
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
      "004bf2b4",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "004bf2c8",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bf348",
      "PARAM",
      [
        "storage",
        "002bb333",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf2b4",
      "READ",
      [
        "storage",
        "00c9bee8",
        null,
        "pointer"
      ]
    ],
    [
      "004bf2c8",
      "DATA",
      [
        "storage",
        "00c67578",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bf348",
      "PARAM",
      [
        "storage",
        "002bb411",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md#insn-004bf034) · [`004bf05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md#insn-004bf05c) · [`004bf0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md#insn-004bf0a8)
- 新版 [`004bf354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf28c.md#insn-004bf354) · [`004bf37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf28c.md#insn-004bf37c) · [`004bf3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf28c.md#insn-004bf3c8)

~~~diff
- 004bf034 ["INT_ADD", "register:40f0:8", ["const:4bf034:8", "const:4:8"]]
- 004bf034 ["CALL", null, ["callee:00c59000:8"]]
+ 004bf354 ["INT_ADD", "register:40f0:8", ["const:4bf354:8", "const:4:8"]]
+ 004bf354 ["CALL", null, ["callee:00c59000:8"]]
- 004bf034 bytes ff631e94
+ 004bf354 bytes 2b671e94
- 004bf05c ["INT_ADD", "register:40f0:8", ["const:4bf05c:8", "const:4:8"]]
- 004bf05c ["CALL", null, ["callee:00c59010:8"]]
+ 004bf37c ["INT_ADD", "register:40f0:8", ["const:4bf37c:8", "const:4:8"]]
+ 004bf37c ["CALL", null, ["callee:00c59010:8"]]
- 004bf05c bytes f9631e94
+ 004bf37c bytes 25671e94
- 004bf0a8 ["INT_ADD", "register:40f0:8", ["const:4bf0a8:8", "const:4:8"]]
- 004bf0a8 ["CALL", null, ["callee:00c59010:8"]]
+ 004bf3c8 ["INT_ADD", "register:40f0:8", ["const:4bf3c8:8", "const:4:8"]]
+ 004bf3c8 ["CALL", null, ["callee:00c59010:8"]]
- 004bf0a8 bytes e6631e94
+ 004bf3c8 bytes 12671e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cafc97697480c62567fb3c0e3bf904c"></a>

### [`004bf278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md) → [`004bf598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf598.md) _ZNK5Botan8ECB_Mode4nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e90.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c59e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e60.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf5d8",
      "incomplete_value": false,
      "site": "004bf5e0",
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
            "const:6d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf2b8",
      "incomplete_value": false,
      "site": "004bf2c0",
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
            "const:57a:8"
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
      "004bf5d8",
      "PARAM",
      [
        "storage",
        "002a657a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf5d8",
      "PARAM",
      [
        "storage",
        "002a66d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md#insn-004bf2c0) · [`004bf2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md#insn-004bf2b0) · [`004bf2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md#insn-004bf2b8)
- 新版 [`004bf5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf598.md#insn-004bf5e0) · [`004bf5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf598.md#insn-004bf5d0) · [`004bf5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf598.md#insn-004bf5d8)

~~~diff
- 004bf2c0 ["INT_ADD", "register:40f0:8", ["const:4bf2c0:8", "const:4:8"]]
- 004bf2c0 ["CALL", null, ["callee:00c59010:8"]]
+ 004bf5e0 ["INT_ADD", "register:40f0:8", ["const:4bf5e0:8", "const:4:8"]]
+ 004bf5e0 ["CALL", null, ["callee:00c59010:8"]]
- 004bf2c0 bytes 60631e94
+ 004bf5e0 bytes 8c661e94
- 004bf2b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bf2b0 ["INT_ADD", "register:40f0:8", ["const:4bf2b0:8", "const:4:8"]]
- 004bf2b0 ["CALLIND", null, ["register:0:8"]]
+ 004bf5d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf5d0 ["INT_ADD", "register:40f0:8", ["const:4bf5d0:8", "const:4:8"]]
+ 004bf5d0 ["CALLIND", null, ["register:0:8"]]
- 004bf2b0 bytes 20013fd6
+ 004bf5d0 bytes 20013fd6
- 004bf2b8 ["COPY", "tmp:0:8", ["const:57a:8"]]
- 004bf2b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bf2b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bf2b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bf5d8 ["COPY", "tmp:0:8", ["const:6d2:8"]]
+ 004bf5d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf5d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf5d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bf2b8 bytes 21e81591
+ 004bf5d8 bytes 21481b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3825241556430b293763a10dd1645331"></a>

### [`004bf48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md) → [`004bf7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf7ac.md) _ZN5Botan8ECB_Mode9start_msgEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "definition_site": "004bf854",
      "incomplete_value": true,
      "site": "004bf860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf534",
      "incomplete_value": true,
      "site": "004bf540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
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
      "definition_site": "004bf850",
      "incomplete_value": false,
      "site": "004bf860",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bf530",
      "incomplete_value": false,
      "site": "004bf540",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004bf850",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bf854",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004bf854",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bf850",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bf854",
      "READ",
      [
        "storage",
        "00c9bee0",
        null,
        "pointer"
      ]
    ],
    [
      "004bf854",
      "PARAM",
      [
        "storage",
        "00c67550",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md#insn-004bf540) · [`004bf4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md#insn-004bf4e4) · [`004bf4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md#insn-004bf4fc)
- 新版 [`004bf860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf7ac.md#insn-004bf860) · [`004bf804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf7ac.md#insn-004bf804) · [`004bf81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf7ac.md#insn-004bf81c)

~~~diff
- 004bf540 ["INT_ADD", "register:40f0:8", ["const:4bf540:8", "const:4:8"]]
- 004bf540 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bf860 ["INT_ADD", "register:40f0:8", ["const:4bf860:8", "const:4:8"]]
+ 004bf860 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bf540 bytes a8621e94
+ 004bf860 bytes d4651e94
- 004bf4e4 ["INT_ADD", "register:40f0:8", ["const:4bf4e4:8", "const:4:8"]]
- 004bf4e4 ["CALL", null, ["callee:00c58f90:8"]]
+ 004bf804 ["INT_ADD", "register:40f0:8", ["const:4bf804:8", "const:4:8"]]
+ 004bf804 ["CALL", null, ["callee:00c58f90:8"]]
- 004bf4e4 bytes b7621e94
+ 004bf804 bytes e3651e94
- 004bf4fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004bf4fc ["INT_ADD", "register:40f0:8", ["const:4bf4fc:8", "const:4:8"]]
- 004bf4fc ["CALLIND", null, ["register:0:8"]]
+ 004bf81c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf81c ["INT_ADD", "register:40f0:8", ["const:4bf81c:8", "const:4:8"]]
+ 004bf81c ["CALLIND", null, ["register:0:8"]]
- 004bf4fc bytes 20013fd6
+ 004bf81c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743c2d649fa76fbc55347796161e432d"></a>

### [`004bf59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md) → [`004bf8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf8bc.md) _ZNK5Botan14ECB_Encryption13output_lengthEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf90c",
      "incomplete_value": false,
      "site": "004bf92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf5ec",
      "incomplete_value": false,
      "site": "004bf60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:72:8"
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
      "definition_site": "004bf914",
      "incomplete_value": false,
      "site": "004bf92c",
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
            "const:62e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf5f4",
      "incomplete_value": false,
      "site": "004bf60c",
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
            "const:561:8"
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
      "definition_site": "004bf91c",
      "incomplete_value": false,
      "site": "004bf92c",
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
            "const:3b4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf5fc",
      "incomplete_value": false,
      "site": "004bf60c",
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
            "const:2e5:8"
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
      "004bf90c",
      "PARAM",
      [
        "storage",
        "002a2072",
        null,
        "string"
      ]
    ],
    [
      "004bf914",
      "PARAM",
      [
        "storage",
        "002ab561",
        null,
        "string"
      ]
    ],
    [
      "004bf91c",
      "PARAM",
      [
        "storage",
        "002b82e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf90c",
      "PARAM",
      [
        "storage",
        "002a20b2",
        null,
        "string"
      ]
    ],
    [
      "004bf914",
      "PARAM",
      [
        "storage",
        "002ab62e",
        null,
        "string"
      ]
    ],
    [
      "004bf91c",
      "PARAM",
      [
        "storage",
        "002b83b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md#insn-004bf60c) · [`004bf5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md#insn-004bf5b8) · [`004bf5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md#insn-004bf5ec)
- 新版 [`004bf92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf8bc.md#insn-004bf92c) · [`004bf8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf8bc.md#insn-004bf8d8) · [`004bf90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf8bc.md#insn-004bf90c)

~~~diff
- 004bf60c ["INT_ADD", "register:40f0:8", ["const:4bf60c:8", "const:4:8"]]
- 004bf60c ["CALL", null, ["callee:00c596f0:8"]]
+ 004bf92c ["INT_ADD", "register:40f0:8", ["const:4bf92c:8", "const:4:8"]]
+ 004bf92c ["CALL", null, ["callee:00c596f0:8"]]
- 004bf60c bytes 45641e94
+ 004bf92c bytes 71671e94
- 004bf5b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf5b8 ["INT_ADD", "register:40f0:8", ["const:4bf5b8:8", "const:4:8"]]
- 004bf5b8 ["CALLIND", null, ["register:0:8"]]
+ 004bf8d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf8d8 ["INT_ADD", "register:40f0:8", ["const:4bf8d8:8", "const:4:8"]]
+ 004bf8d8 ["CALLIND", null, ["register:0:8"]]
- 004bf5b8 bytes 00013fd6
+ 004bf8d8 bytes 00013fd6
- 004bf5ec ["COPY", "tmp:0:8", ["const:72:8"]]
- 004bf5ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bf5ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bf5ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bf90c ["COPY", "tmp:0:8", ["const:b2:8"]]
+ 004bf90c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bf90c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bf90c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bf5ec bytes 00c80191
+ 004bf90c bytes 00c80291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8588cbdd34b424b91a03add6f7d8a8f0"></a>

### [`004bf610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md) → [`004bf930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf930.md) _ZN5Botan14ECB_Encryption7processEPhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf998",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf678",
      "incomplete_value": false,
      "site": "004bf698",
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
            "const:bc4:8"
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
      "definition_site": "004bf9a0",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:173:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf680",
      "incomplete_value": false,
      "site": "004bf698",
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
            "const:a8:8"
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
      "definition_site": "004bf9a8",
      "incomplete_value": false,
      "site": "004bf9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf688",
      "incomplete_value": false,
      "site": "004bf698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:d3:8"
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
      "004bf998",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bf9a0",
      "PARAM",
      [
        "storage",
        "002a30a8",
        null,
        "string"
      ]
    ],
    [
      "004bf9a8",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf998",
      "PARAM",
      [
        "storage",
        "002a8d1c",
        null,
        "string"
      ]
    ],
    [
      "004bf9a0",
      "PARAM",
      [
        "storage",
        "002a3173",
        null,
        "string"
      ]
    ],
    [
      "004bf9a8",
      "PARAM",
      [
        "storage",
        "002a419e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md#insn-004bf698) · [`004bf638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md#insn-004bf638) · [`004bf65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md#insn-004bf65c)
- 新版 [`004bf9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf930.md#insn-004bf9b8) · [`004bf958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf930.md#insn-004bf958) · [`004bf97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf930.md#insn-004bf97c)

~~~diff
- 004bf698 ["INT_ADD", "register:40f0:8", ["const:4bf698:8", "const:4:8"]]
- 004bf698 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bf9b8 ["INT_ADD", "register:40f0:8", ["const:4bf9b8:8", "const:4:8"]]
+ 004bf9b8 ["CALL", null, ["callee:00c596f0:8"]]
- 004bf698 bytes 22641e94
+ 004bf9b8 bytes 4e671e94
- 004bf638 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf638 ["INT_ADD", "register:40f0:8", ["const:4bf638:8", "const:4:8"]]
- 004bf638 ["CALLIND", null, ["register:0:8"]]
+ 004bf958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf958 ["INT_ADD", "register:40f0:8", ["const:4bf958:8", "const:4:8"]]
+ 004bf958 ["CALLIND", null, ["register:0:8"]]
- 004bf638 bytes 00013fd6
+ 004bf958 bytes 00013fd6
- 004bf65c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf65c ["INT_ADD", "register:40f0:8", ["const:4bf65c:8", "const:4:8"]]
- 004bf65c ["CALLIND", null, ["register:0:8"]]
+ 004bf97c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf97c ["INT_ADD", "register:40f0:8", ["const:4bf97c:8", "const:4:8"]]
+ 004bf97c ["CALLIND", null, ["register:0:8"]]
- 004bf65c bytes 00013fd6
+ 004bf97c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f15beaaeb15bf74ad08830fe391219"></a>

### [`004bf69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md) → [`004bf9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf9bc.md) _ZN5Botan14ECB_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfae8",
      "incomplete_value": false,
      "site": "004bfb08",
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
            "const:7d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf7c8",
      "incomplete_value": false,
      "site": "004bf7e8",
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
            "const:709:8"
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
      "definition_site": "004bfaf0",
      "incomplete_value": false,
      "site": "004bfb08",
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
            "const:e2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf7d0",
      "incomplete_value": false,
      "site": "004bf7e8",
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
            "const:d4e:8"
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
      "definition_site": "004bfaf8",
      "incomplete_value": false,
      "site": "004bfb08",
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
            "const:2d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf7d8",
      "incomplete_value": false,
      "site": "004bf7e8",
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
            "const:1f9:8"
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
      "004bfae8",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004bfaf0",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ],
    [
      "004bfaf8",
      "PARAM",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bfae8",
      "PARAM",
      [
        "storage",
        "002ad7d6",
        null,
        "string"
      ]
    ],
    [
      "004bfaf0",
      "PARAM",
      [
        "storage",
        "002b4e2c",
        null,
        "string"
      ]
    ],
    [
      "004bfaf8",
      "PARAM",
      [
        "storage",
        "002ba2d7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md#insn-004bf7e8) · [`004bf814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md#insn-004bf814) · [`004bf868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md#insn-004bf868)
- 新版 [`004bfb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf9bc.md#insn-004bfb08) · [`004bfb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf9bc.md#insn-004bfb34) · [`004bfb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf9bc.md#insn-004bfb88)

~~~diff
- 004bf7e8 ["INT_ADD", "register:40f0:8", ["const:4bf7e8:8", "const:4:8"]]
- 004bf7e8 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bfb08 ["INT_ADD", "register:40f0:8", ["const:4bfb08:8", "const:4:8"]]
+ 004bfb08 ["CALL", null, ["callee:00c596f0:8"]]
- 004bf7e8 bytes ce631e94
+ 004bfb08 bytes fa661e94
- 004bf814 ["INT_ADD", "register:40f0:8", ["const:4bf814:8", "const:4:8"]]
- 004bf814 ["CALL", null, ["callee:00c59000:8"]]
+ 004bfb34 ["INT_ADD", "register:40f0:8", ["const:4bfb34:8", "const:4:8"]]
+ 004bfb34 ["CALL", null, ["callee:00c59000:8"]]
- 004bf814 bytes 07621e94
+ 004bfb34 bytes 33651e94
- 004bf868 ["INT_ADD", "register:40f0:8", ["const:4bf868:8", "const:4:8"]]
- 004bf868 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bfb88 ["INT_ADD", "register:40f0:8", ["const:4bfb88:8", "const:4:8"]]
+ 004bfb88 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bf868 bytes de611e94
+ 004bfb88 bytes 0a651e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0bc44c186b58120c201cde021b5602a"></a>

### [`004bf930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md) → [`004bfc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfc50.md) _ZN5Botan14ECB_Decryption7processEPhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfcb8",
      "incomplete_value": false,
      "site": "004bfcd8",
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
            "const:d1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf998",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:bc4:8"
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
      "definition_site": "004bfcc0",
      "incomplete_value": false,
      "site": "004bfcd8",
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
            "const:ba2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf9a0",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:acb:8"
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
      "definition_site": "004bfcc8",
      "incomplete_value": false,
      "site": "004bfcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf9a8",
      "incomplete_value": false,
      "site": "004bf9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:d3:8"
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
      "004bfcb8",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bfcc0",
      "PARAM",
      [
        "storage",
        "002b0acb",
        null,
        "string"
      ]
    ],
    [
      "004bfcc8",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bfcb8",
      "PARAM",
      [
        "storage",
        "002a8d1c",
        null,
        "string"
      ]
    ],
    [
      "004bfcc0",
      "PARAM",
      [
        "storage",
        "002b0ba2",
        null,
        "string"
      ]
    ],
    [
      "004bfcc8",
      "PARAM",
      [
        "storage",
        "002a419e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md#insn-004bf9b8) · [`004bf958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md#insn-004bf958) · [`004bf97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md#insn-004bf97c)
- 新版 [`004bfcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfc50.md#insn-004bfcd8) · [`004bfc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfc50.md#insn-004bfc78) · [`004bfc9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfc50.md#insn-004bfc9c)

~~~diff
- 004bf9b8 ["INT_ADD", "register:40f0:8", ["const:4bf9b8:8", "const:4:8"]]
- 004bf9b8 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bfcd8 ["INT_ADD", "register:40f0:8", ["const:4bfcd8:8", "const:4:8"]]
+ 004bfcd8 ["CALL", null, ["callee:00c596f0:8"]]
- 004bf9b8 bytes 5a631e94
+ 004bfcd8 bytes 86661e94
- 004bf958 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf958 ["INT_ADD", "register:40f0:8", ["const:4bf958:8", "const:4:8"]]
- 004bf958 ["CALLIND", null, ["register:0:8"]]
+ 004bfc78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfc78 ["INT_ADD", "register:40f0:8", ["const:4bfc78:8", "const:4:8"]]
+ 004bfc78 ["CALLIND", null, ["register:0:8"]]
- 004bf958 bytes 00013fd6
+ 004bfc78 bytes 00013fd6
- 004bf97c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf97c ["INT_ADD", "register:40f0:8", ["const:4bf97c:8", "const:4:8"]]
- 004bf97c ["CALLIND", null, ["register:0:8"]]
+ 004bfc9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfc9c ["INT_ADD", "register:40f0:8", ["const:4bfc9c:8", "const:4:8"]]
+ 004bfc9c ["CALLIND", null, ["register:0:8"]]
- 004bf97c bytes 00013fd6
+ 004bfc9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268425f10e2eba5e239675e6502f344b"></a>

### [`004bf9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md) → [`004bfcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfcdc.md) _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfe4c",
      "incomplete_value": false,
      "site": "004bfe54",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfb2c",
      "incomplete_value": false,
      "site": "004bfb34",
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
            "const:93:8"
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
      "definition_site": "004bfe9c",
      "incomplete_value": true,
      "site": "004bfea8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004bfb7c",
      "incomplete_value": true,
      "site": "004bfb88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
      "definition_site": "004bfe98",
      "incomplete_value": false,
      "site": "004bfea8",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bfb78",
      "incomplete_value": false,
      "site": "004bfb88",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bfe4c",
      "PARAM",
      [
        "storage",
        "002c1093",
        null,
        "string"
      ]
    ],
    [
      "004bfe98",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bfe9c",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bfe4c",
      "PARAM",
      [
        "storage",
        "002c10dd",
        null,
        "string"
      ]
    ],
    [
      "004bfe98",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004bfe9c",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bfb34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md#insn-004bfb34) · [`004bfb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md#insn-004bfb88) · [`004bfbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md#insn-004bfbc0)
- 新版 [`004bfe54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfcdc.md#insn-004bfe54) · [`004bfea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfcdc.md#insn-004bfea8) · [`004bfee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bfcdc.md#insn-004bfee0)

~~~diff
- 004bfb34 ["INT_ADD", "register:40f0:8", ["const:4bfb34:8", "const:4:8"]]
- 004bfb34 ["CALL", null, ["callee:00c59010:8"]]
+ 004bfe54 ["INT_ADD", "register:40f0:8", ["const:4bfe54:8", "const:4:8"]]
+ 004bfe54 ["CALL", null, ["callee:00c59010:8"]]
- 004bfb34 bytes 43611e94
+ 004bfe54 bytes 6f641e94
- 004bfb88 ["INT_ADD", "register:40f0:8", ["const:4bfb88:8", "const:4:8"]]
- 004bfb88 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004bfea8 ["INT_ADD", "register:40f0:8", ["const:4bfea8:8", "const:4:8"]]
+ 004bfea8 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bfb88 bytes 16611e94
+ 004bfea8 bytes 42641e94
- 004bfbc0 ["INT_ADD", "register:40f0:8", ["const:4bfbc0:8", "const:4:8"]]
- 004bfbc0 ["CALL", null, ["callee:00c596f0:8"]]
+ 004bfee0 ["INT_ADD", "register:40f0:8", ["const:4bfee0:8", "const:4:8"]]
+ 004bfee0 ["CALL", null, ["callee:00c596f0:8"]]
- 004bfbc0 bytes d8621e94
+ 004bfee0 bytes 04661e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d47145b2c780e235ec3e0f145afcda34"></a>

### [`004bfd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md) → [`004c0064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0064.md) _ZN5Botan13EMSA_PKCS1v1511encoding_ofERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmRNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004bfe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004c0198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0198.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c0104",
      "incomplete_value": false,
      "site": "004c010c",
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
            "const:e3b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfde4",
      "incomplete_value": false,
      "site": "004bfdec",
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
            "const:d5d:8"
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
      "definition_site": "004c013c",
      "incomplete_value": true,
      "site": "004c0148",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfe1c",
      "incomplete_value": true,
      "site": "004bfe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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
      "definition_site": "004c0138",
      "incomplete_value": false,
      "site": "004c0148",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004bfe18",
      "incomplete_value": false,
      "site": "004bfe28",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c0104",
      "PARAM",
      [
        "storage",
        "002b4d5d",
        null,
        "string"
      ]
    ],
    [
      "004c0138",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c013c",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c0104",
      "PARAM",
      [
        "storage",
        "002b4e3b",
        null,
        "string"
      ]
    ],
    [
      "004c0138",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c013c",
      "READ",
      [
        "storage",
        "00c9be38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bfdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md#insn-004bfdec) · [`004bfe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md#insn-004bfe28) · [`004bfd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md#insn-004bfd8c)
- 新版 [`004c010c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0064.md#insn-004c010c) · [`004c0148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0064.md#insn-004c0148) · [`004c00ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0064.md#insn-004c00ac)

~~~diff
- 004bfdec ["INT_ADD", "register:40f0:8", ["const:4bfdec:8", "const:4:8"]]
- 004bfdec ["CALL", null, ["callee:0043e138:8"]]
+ 004c010c ["INT_ADD", "register:40f0:8", ["const:4c010c:8", "const:4:8"]]
+ 004c010c ["CALL", null, ["callee:0043e138:8"]]
- 004bfdec bytes 0bf8fd97
+ 004c010c bytes 0bf8fd97
- 004bfe28 ["INT_ADD", "register:40f0:8", ["const:4bfe28:8", "const:4:8"]]
- 004bfe28 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c0148 ["INT_ADD", "register:40f0:8", ["const:4c0148:8", "const:4:8"]]
+ 004c0148 ["CALL", null, ["callee:00c58fb0:8"]]
- 004bfe28 bytes 6e601e94
+ 004c0148 bytes 9a631e94
- 004bfd8c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfd8c ["INT_ADD", "register:40f0:8", ["const:4bfd8c:8", "const:4:8"]]
- 004bfd8c ["CALLIND", null, ["register:0:8"]]
+ 004c00ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c00ac ["INT_ADD", "register:40f0:8", ["const:4c00ac:8", "const:4:8"]]
+ 004c00ac ["CALLIND", null, ["register:0:8"]]
- 004bfd8c bytes 00013fd6
+ 004c00ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8afe4f72ba00d0de886879acfd41eda"></a>

### [`004bfe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md) → [`004c0198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0198.md) FUN_004c0198

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004bfd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md) [`004c00b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md) [`004c174c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c174c.md) [`004c1764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1764.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 4件 [`004c0064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0064.md) [`004c03d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c03d4.md) [`004c1a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1a6c.md) [`004c1a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1a84.md) · 呼出先 10件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c02f8",
      "incomplete_value": false,
      "site": "004c0300",
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
            "const:e1a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bffd8",
      "incomplete_value": false,
      "site": "004bffe0",
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
            "const:d4d:8"
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
      "definition_site": "004c0330",
      "incomplete_value": true,
      "site": "004c033c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0010",
      "incomplete_value": true,
      "site": "004c001c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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
      "definition_site": "004c032c",
      "incomplete_value": false,
      "site": "004c033c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c000c",
      "incomplete_value": false,
      "site": "004c001c",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c02f8",
      "PARAM",
      [
        "storage",
        "002a8d4d",
        null,
        "string"
      ]
    ],
    [
      "004c032c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c0330",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c02f8",
      "PARAM",
      [
        "storage",
        "002a8e1a",
        null,
        "string"
      ]
    ],
    [
      "004c032c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c0330",
      "READ",
      [
        "storage",
        "00c9be38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md#insn-004bffe0) · [`004c001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md#insn-004c001c) · [`004c0054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md#insn-004c0054)
- 新版 [`004c0300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0198.md#insn-004c0300) · [`004c033c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0198.md#insn-004c033c) · [`004c0374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0198.md#insn-004c0374)

~~~diff
- 004bffe0 ["INT_ADD", "register:40f0:8", ["const:4bffe0:8", "const:4:8"]]
- 004bffe0 ["CALL", null, ["callee:0043e138:8"]]
+ 004c0300 ["INT_ADD", "register:40f0:8", ["const:4c0300:8", "const:4:8"]]
+ 004c0300 ["CALL", null, ["callee:0043e138:8"]]
- 004bffe0 bytes 8ef7fd97
+ 004c0300 bytes 8ef7fd97
- 004c001c ["INT_ADD", "register:40f0:8", ["const:4c001c:8", "const:4:8"]]
- 004c001c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c033c ["INT_ADD", "register:40f0:8", ["const:4c033c:8", "const:4:8"]]
+ 004c033c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c001c bytes f15f1e94
+ 004c033c bytes 1d631e94
- 004c0054 ["INT_ADD", "register:40f0:8", ["const:4c0054:8", "const:4:8"]]
- 004c0054 ["CALL", null, ["callee:00c596f0:8"]]
+ 004c0374 ["INT_ADD", "register:40f0:8", ["const:4c0374:8", "const:4:8"]]
+ 004c0374 ["CALL", null, ["callee:00c596f0:8"]]
- 004c0054 bytes b3611e94
+ 004c0374 bytes df641e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff00366d8411f009eacff43ce49a8750"></a>

### [`004c00b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md) → [`004c03d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c03d4.md) _ZN5Botan13EMSA_PKCS1v156verifyERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEES7_m

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004bfe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004c0198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0198.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c0498",
      "incomplete_value": true,
      "site": "004c0498",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0178",
      "incomplete_value": true,
      "site": "004c0178",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "004c0488",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c0488",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md#insn-004c0178) · [`004c00fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md#insn-004c00fc) · [`004c011c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md#insn-004c011c)
- 新版 [`004c0498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c03d4.md#insn-004c0498) · [`004c041c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c03d4.md#insn-004c041c) · [`004c043c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c03d4.md#insn-004c043c)

~~~diff
- 004c0178 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0178 ["INT_ADD", "register:40f0:8", ["const:4c0178:8", "const:4:8"]]
- 004c0178 ["CALLIND", null, ["register:0:8"]]
+ 004c0498 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0498 ["INT_ADD", "register:40f0:8", ["const:4c0498:8", "const:4:8"]]
+ 004c0498 ["CALLIND", null, ["register:0:8"]]
- 004c0178 bytes 20013fd6
+ 004c0498 bytes 20013fd6
- 004c00fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004c00fc ["INT_ADD", "register:40f0:8", ["const:4c00fc:8", "const:4:8"]]
- 004c00fc ["CALLIND", null, ["register:0:8"]]
+ 004c041c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c041c ["INT_ADD", "register:40f0:8", ["const:4c041c:8", "const:4:8"]]
+ 004c041c ["CALLIND", null, ["register:0:8"]]
- 004c00fc bytes 00013fd6
+ 004c041c bytes 00013fd6
- 004c011c ["INT_ADD", "register:40f0:8", ["const:4c011c:8", "const:4:8"]]
- 004c011c ["CALL", null, ["callee:004c0198:8"]]
+ 004c043c ["INT_ADD", "register:40f0:8", ["const:4c043c:8", "const:4:8"]]
+ 004c043c ["CALL", null, ["callee:004c0198:8"]]
- 004c011c bytes 57ffff97
+ 004c043c bytes 57ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a868a1e6404855bab449bc26ddcfd96d"></a>

### [`004c01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md) → [`004c04e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c04e8.md) _ZNK5Botan13EMSA_PKCS1v1515config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004c07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md) [`004c09a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004c0b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0b14.md) [`004c0cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0cc8.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c0624",
      "incomplete_value": true,
      "site": "004c0624",
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
      "definition_site": "004c0304",
      "incomplete_value": true,
      "site": "004c0304",
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c066c",
      "incomplete_value": false,
      "site": "004c0674",
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
      "definition_site": "004c034c",
      "incomplete_value": false,
      "site": "004c0354",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c0828",
      "incomplete_value": false,
      "site": "004c0830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:1a6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0508",
      "incomplete_value": false,
      "site": "004c0510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:db:8"
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
      "004c0618",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004c0624",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c066c",
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
      "004c0618",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "004c0624",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c066c",
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

- 旧版 [`004c0354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md#insn-004c0354) · [`004c0510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md#insn-004c0510) · [`004c054c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md#insn-004c054c)
- 新版 [`004c0674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c04e8.md#insn-004c0674) · [`004c0830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c04e8.md#insn-004c0830) · [`004c086c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c04e8.md#insn-004c086c)

~~~diff
- 004c0354 ["INT_ADD", "register:40f0:8", ["const:4c0354:8", "const:4:8"]]
- 004c0354 ["CALL", null, ["callee:00c59010:8"]]
+ 004c0674 ["INT_ADD", "register:40f0:8", ["const:4c0674:8", "const:4:8"]]
+ 004c0674 ["CALL", null, ["callee:00c59010:8"]]
- 004c0354 bytes 3b5f1e94
+ 004c0674 bytes 67621e94
- 004c0510 ["INT_ADD", "register:40f0:8", ["const:4c0510:8", "const:4:8"]]
- 004c0510 ["CALL", null, ["callee:0043e138:8"]]
+ 004c0830 ["INT_ADD", "register:40f0:8", ["const:4c0830:8", "const:4:8"]]
+ 004c0830 ["CALL", null, ["callee:0043e138:8"]]
- 004c0510 bytes 42f6fd97
+ 004c0830 bytes 42f6fd97
- 004c054c ["INT_ADD", "register:40f0:8", ["const:4c054c:8", "const:4:8"]]
- 004c054c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c086c ["INT_ADD", "register:40f0:8", ["const:4c086c:8", "const:4:8"]]
+ 004c086c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c054c bytes a55e1e94
+ 004c086c bytes d1611e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac6f037495406a1d835e067032ecfe1c"></a>

### [`004c09a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md) → [`004c0cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0cc8.md) FUN_004c0cc8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 1件 [`004c04e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c04e8.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c0d00",
      "incomplete_value": false,
      "site": "004c0d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:e96:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c09e0",
      "incomplete_value": false,
      "site": "004c09ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c0d2c",
      "incomplete_value": false,
      "site": "004c0d34",
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
            "const:3a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0a0c",
      "incomplete_value": false,
      "site": "004c0a14",
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
            "const:2d6:8"
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
      "004c0d00",
      "PARAM",
      [
        "storage",
        "002bedb8",
        null,
        "string"
      ]
    ],
    [
      "004c0d2c",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c0d00",
      "PARAM",
      [
        "storage",
        "002bee96",
        null,
        "string"
      ]
    ],
    [
      "004c0d2c",
      "PARAM",
      [
        "storage",
        "002ab3a3",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c09ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md#insn-004c09ec) · [`004c0a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md#insn-004c0a14) · [`004c09d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md#insn-004c09d8)
- 新版 [`004c0d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0cc8.md#insn-004c0d0c) · [`004c0d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0cc8.md#insn-004c0d34) · [`004c0cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0cc8.md#insn-004c0cf8)

~~~diff
- 004c09ec ["INT_ADD", "register:40f0:8", ["const:4c09ec:8", "const:4:8"]]
- 004c09ec ["CALL", null, ["callee:00c59000:8"]]
+ 004c0d0c ["INT_ADD", "register:40f0:8", ["const:4c0d0c:8", "const:4:8"]]
+ 004c0d0c ["CALL", null, ["callee:00c59000:8"]]
- 004c09ec bytes 915d1e94
+ 004c0d0c bytes bd601e94
- 004c0a14 ["INT_ADD", "register:40f0:8", ["const:4c0a14:8", "const:4:8"]]
- 004c0a14 ["CALL", null, ["callee:00c59010:8"]]
+ 004c0d34 ["INT_ADD", "register:40f0:8", ["const:4c0d34:8", "const:4:8"]]
+ 004c0d34 ["CALL", null, ["callee:00c59010:8"]]
- 004c0a14 bytes 8b5d1e94
+ 004c0d34 bytes b7601e94
- 004c09d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c09d8 ["INT_ADD", "register:40f0:8", ["const:4c09d8:8", "const:4:8"]]
- 004c09d8 ["CALLIND", null, ["register:0:8"]]
+ 004c0cf8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0cf8 ["INT_ADD", "register:40f0:8", ["const:4c0cf8:8", "const:4:8"]]
+ 004c0cf8 ["CALLIND", null, ["register:0:8"]]
- 004c09d8 bytes 20013fd6
+ 004c0cf8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ef248728200fe4c925ac42104f4dac"></a>

### [`004c0afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md) → [`004c0e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0e1c.md) _ZN5Botan13EMSA_PKCS1v15C2EPNS_12HashFunctionE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c595e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c595e0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58eb0.md)
- 新版 呼出元 1件 [`00c5a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a5b0.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c0e4c",
      "incomplete_value": true,
      "site": "004c0e58",
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
      "definition_site": "004c0b2c",
      "incomplete_value": true,
      "site": "004c0b38",
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
      "004c0e40",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "004c0e58",
      "DATA",
      [
        "storage",
        "00c66648",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c0e40",
      "READ",
      [
        "storage",
        "00c9bef0",
        null,
        "pointer"
      ]
    ],
    [
      "004c0e58",
      "DATA",
      [
        "storage",
        "00c67618",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md#insn-004c0b14) · [`004c0b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md#insn-004c0b20) · [`004c0b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md#insn-004c0b24)
- 新版 [`004c0e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0e1c.md#insn-004c0e34) · [`004c0e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0e1c.md#insn-004c0e40)

~~~diff
- 004c0b14 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c0e34 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c0b14 bytes c93e00d0
+ 004c0e34 bytes c93e00f0
- 004c0b20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f20:8"]]
- 004c0b20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c0e40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ef0:8"]]
+ 004c0e40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c0b20 bytes 299147f9
+ 004c0e40 bytes 297947f9
- 004c0b24 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004c0b24 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d572debe0decaddff9bb9373b6f56d66"></a>

### [`004c0c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md) → [`004c0f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0f44.md) _ZN5Botan12pkcs_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58eb0.md) · 呼出先 9件 [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`004cc1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc1cc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c59e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e80.md) · 呼出先 9件 [`004421f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/004421f4.md) [`004cc4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cc/004cc4ec.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c109c",
      "incomplete_value": true,
      "site": "004c10ac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:f56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0d7c",
      "incomplete_value": true,
      "site": "004c0d8c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:f06:8"
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
      "definition_site": "004c115c",
      "incomplete_value": false,
      "site": "004c1164",
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
            "const:82f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0e3c",
      "incomplete_value": false,
      "site": "004c0e44",
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
            "const:762:8"
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
      "definition_site": "004c118c",
      "incomplete_value": false,
      "site": "004c1194",
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
            "const:c1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0e6c",
      "incomplete_value": false,
      "site": "004c0e74",
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
            "const:b52:8"
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
      "004c109c",
      "READ",
      [
        "storage",
        "002caf06",
        null,
        null
      ]
    ],
    [
      "004c115c",
      "PARAM",
      [
        "storage",
        "002ae762",
        null,
        "string"
      ]
    ],
    [
      "004c1180",
      "PARAM",
      [
        "storage",
        "002caf36",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c109c",
      "READ",
      [
        "storage",
        "002caf56",
        null,
        null
      ]
    ],
    [
      "004c115c",
      "PARAM",
      [
        "storage",
        "002ae82f",
        null,
        "string"
      ]
    ],
    [
      "004c1180",
      "PARAM",
      [
        "storage",
        "002caf86",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md#insn-004c0df4) · [`004c0e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md#insn-004c0e44) · [`004c0e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md#insn-004c0e74)
- 新版 [`004c1114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0f44.md#insn-004c1114) · [`004c1164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0f44.md#insn-004c1164) · [`004c1194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0f44.md#insn-004c1194)

~~~diff
- 004c0df4 ["INT_ADD", "register:40f0:8", ["const:4c0df4:8", "const:4:8"]]
- 004c0df4 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c1114 ["INT_ADD", "register:40f0:8", ["const:4c1114:8", "const:4:8"]]
+ 004c1114 ["CALL", null, ["callee:00c58f30:8"]]
- 004c0df4 bytes 5b5c1e94
+ 004c1114 bytes 875f1e94
- 004c0e44 ["INT_ADD", "register:40f0:8", ["const:4c0e44:8", "const:4:8"]]
- 004c0e44 ["CALL", null, ["callee:004421f4:8"]]
+ 004c1164 ["INT_ADD", "register:40f0:8", ["const:4c1164:8", "const:4:8"]]
+ 004c1164 ["CALL", null, ["callee:004421f4:8"]]
- 004c0e44 bytes 2404fe97
+ 004c1164 bytes 2404fe97
- 004c0e74 ["INT_ADD", "register:40f0:8", ["const:4c0e74:8", "const:4:8"]]
- 004c0e74 ["CALL", null, ["callee:004421f4:8"]]
+ 004c1194 ["INT_ADD", "register:40f0:8", ["const:4c1194:8", "const:4:8"]]
+ 004c1194 ["CALL", null, ["callee:004421f4:8"]]
- 004c0e74 bytes 1804fe97
+ 004c1194 bytes 1804fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a00a6993ef52275824fbda9c21998b7b"></a>

### [`004c1164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md) → [`004c1484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1484.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c595d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c595d0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58eb0.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)
- 新版 呼出元 1件 [`00c5a5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a5a0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e80.md) [`00c59e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c14b8",
      "incomplete_value": true,
      "site": "004c14c0",
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
      "definition_site": "004c1198",
      "incomplete_value": true,
      "site": "004c11a0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c14a8",
      "READ",
      [
        "storage",
        "00c9af28",
        null,
        "pointer"
      ]
    ],
    [
      "004c14c0",
      "DATA",
      [
        "storage",
        "00c666a0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c14a8",
      "READ",
      [
        "storage",
        "00c9bef8",
        null,
        "pointer"
      ]
    ],
    [
      "004c14c0",
      "DATA",
      [
        "storage",
        "00c67670",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c117c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md#insn-004c117c) · [`004c1188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md#insn-004c1188) · [`004c11e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md#insn-004c11e0)
- 新版 [`004c149c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1484.md#insn-004c149c) · [`004c14a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1484.md#insn-004c14a8) · [`004c1500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1484.md#insn-004c1500)

~~~diff
- 004c117c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c149c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c117c bytes c83e00b0
+ 004c149c bytes c83e00d0
- 004c1188 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 004c1188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c14a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
+ 004c14a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1188 bytes 089547f9
+ 004c14a8 bytes 087d47f9
- 004c11e0 ["INT_ADD", "register:40f0:8", ["const:4c11e0:8", "const:4:8"]]
- 004c11e0 ["CALL", null, ["callee:00c59e80:8"]]
+ 004c1500 ["INT_ADD", "register:40f0:8", ["const:4c1500:8", "const:4:8"]]
+ 004c1500 ["CALL", null, ["callee:00c59e80:8"]]
- 004c11e0 bytes 345f1e94
+ 004c1500 bytes 60621e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e86d3f0a2dc7fcc121244c4dc67962"></a>

### [`004c1620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md) → [`004c1940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1940.md) _ZN5Botan17EMSA_PKCS1v15_Raw8raw_dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c19c8",
      "incomplete_value": false,
      "site": "004c19d0",
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
            "const:d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c16a8",
      "incomplete_value": false,
      "site": "004c16b0",
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
            "const:4:8"
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
      "definition_site": "004c1a04",
      "incomplete_value": true,
      "site": "004c1a10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c16e4",
      "incomplete_value": true,
      "site": "004c16f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
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
      "definition_site": "004c1a00",
      "incomplete_value": false,
      "site": "004c1a10",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c16e0",
      "incomplete_value": false,
      "site": "004c16f0",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c19c8",
      "PARAM",
      [
        "storage",
        "002b6004",
        null,
        "string"
      ]
    ],
    [
      "004c1a00",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c1a04",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c19c8",
      "PARAM",
      [
        "storage",
        "002b60d3",
        null,
        "string"
      ]
    ],
    [
      "004c1a00",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c1a04",
      "READ",
      [
        "storage",
        "00c9be38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c16b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md#insn-004c16b0) · [`004c16f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md#insn-004c16f0) · [`004c169c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md#insn-004c169c)
- 新版 [`004c19d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1940.md#insn-004c19d0) · [`004c1a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1940.md#insn-004c1a10) · [`004c19bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1940.md#insn-004c19bc)

~~~diff
- 004c16b0 ["INT_ADD", "register:40f0:8", ["const:4c16b0:8", "const:4:8"]]
- 004c16b0 ["CALL", null, ["callee:0043e138:8"]]
+ 004c19d0 ["INT_ADD", "register:40f0:8", ["const:4c19d0:8", "const:4:8"]]
+ 004c19d0 ["CALL", null, ["callee:0043e138:8"]]
- 004c16b0 bytes daf1fd97
+ 004c19d0 bytes daf1fd97
- 004c16f0 ["INT_ADD", "register:40f0:8", ["const:4c16f0:8", "const:4:8"]]
- 004c16f0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c1a10 ["INT_ADD", "register:40f0:8", ["const:4c1a10:8", "const:4:8"]]
+ 004c1a10 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c16f0 bytes 3c5a1e94
+ 004c1a10 bytes 685d1e94
- 004c169c ["INT_ADD", "register:40f0:8", ["const:4c169c:8", "const:4:8"]]
- 004c169c ["CALL", null, ["callee:00c58f90:8"]]
+ 004c19bc ["INT_ADD", "register:40f0:8", ["const:4c19bc:8", "const:4:8"]]
+ 004c19bc ["CALL", null, ["callee:00c58f90:8"]]
- 004c169c bytes 495a1e94
+ 004c19bc bytes 755d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1aaedaf3781db59826e70af87d08a3b"></a>

### [`004c1860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md) → [`004c1b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1b80.md) _ZN5Botan4PSSRC2EPNS_12HashFunctionE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c1ba0",
      "incomplete_value": true,
      "site": "004c1ba4",
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
      "definition_site": "004c1880",
      "incomplete_value": true,
      "site": "004c1884",
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
      "004c1b98",
      "READ",
      [
        "storage",
        "00c9af30",
        null,
        "pointer"
      ]
    ],
    [
      "004c1ba4",
      "DATA",
      [
        "storage",
        "00c666f8",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c1b98",
      "READ",
      [
        "storage",
        "00c9bf00",
        null,
        "pointer"
      ]
    ],
    [
      "004c1ba4",
      "DATA",
      [
        "storage",
        "00c676c8",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c186c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md#insn-004c186c) · [`004c1878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md#insn-004c1878) · [`004c1890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md#insn-004c1890)
- 新版 [`004c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1b80.md#insn-004c1b8c) · [`004c1b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1b80.md#insn-004c1b98) · [`004c1bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1b80.md#insn-004c1bb0)

~~~diff
- 004c186c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c1b8c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c186c bytes c83e00b0
+ 004c1b8c bytes c83e00d0
- 004c1878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
- 004c1878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004c1b98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1878 bytes 089947f9
+ 004c1b98 bytes 088147f9
- 004c1890 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1890 ["INT_ADD", "register:40f0:8", ["const:4c1890:8", "const:4:8"]]
- 004c1890 ["CALLIND", null, ["register:0:8"]]
+ 004c1bb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1bb0 ["INT_ADD", "register:40f0:8", ["const:4c1bb0:8", "const:4:8"]]
+ 004c1bb0 ["CALLIND", null, ["register:0:8"]]
- 004c1890 bytes 00013fd6
+ 004c1bb0 bytes 00013fd6
~~~


<a id="compare-f0eb7b1dd2ae7f16d7b5814cc8003d60"></a>

### [`004c1a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md) → [`004c1d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1d70.md) FUN_004c1d70

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004c1954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1954.md) [`004c2edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2edc.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 2件 [`004c1c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1c74.md) [`004c31fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c31fc.md) · 呼出先 11件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.30% / 新版 98.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c2020",
      "incomplete_value": true,
      "site": "004c2020",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1d00",
      "incomplete_value": true,
      "site": "004c1d00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2070",
      "incomplete_value": false,
      "site": "004c2078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:72c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1d50",
      "incomplete_value": false,
      "site": "004c1d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:64e:8"
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
      "definition_site": "004c20ac",
      "incomplete_value": true,
      "site": "004c20b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1d8c",
      "incomplete_value": true,
      "site": "004c1d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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
      "004c2010",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c2070",
      "PARAM",
      [
        "storage",
        "002bc64e",
        null,
        "string"
      ]
    ],
    [
      "004c20a8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c2010",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004c2070",
      "PARAM",
      [
        "storage",
        "002bc72c",
        null,
        "string"
      ]
    ],
    [
      "004c20a8",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c1d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md#insn-004c1d00) · [`004c1d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md#insn-004c1d58) · [`004c1d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md#insn-004c1d98)
- 新版 [`004c2020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1d70.md#insn-004c2020) · [`004c2078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1d70.md#insn-004c2078) · [`004c20b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c1/004c1d70.md#insn-004c20b8)

~~~diff
- 004c1d00 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1d00 ["INT_ADD", "register:40f0:8", ["const:4c1d00:8", "const:4:8"]]
- 004c1d00 ["CALLIND", null, ["register:0:8"]]
+ 004c2020 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2020 ["INT_ADD", "register:40f0:8", ["const:4c2020:8", "const:4:8"]]
+ 004c2020 ["CALLIND", null, ["register:0:8"]]
- 004c1d00 bytes 20013fd6
+ 004c2020 bytes 20013fd6
- 004c1d58 ["INT_ADD", "register:40f0:8", ["const:4c1d58:8", "const:4:8"]]
- 004c1d58 ["CALL", null, ["callee:0043e138:8"]]
+ 004c2078 ["INT_ADD", "register:40f0:8", ["const:4c2078:8", "const:4:8"]]
+ 004c2078 ["CALL", null, ["callee:0043e138:8"]]
- 004c1d58 bytes 30f0fd97
+ 004c2078 bytes 30f0fd97
- 004c1d98 ["INT_ADD", "register:40f0:8", ["const:4c1d98:8", "const:4:8"]]
- 004c1d98 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c20b8 ["INT_ADD", "register:40f0:8", ["const:4c20b8:8", "const:4:8"]]
+ 004c20b8 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c1d98 bytes 92581e94
+ 004c20b8 bytes be5b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da2011dbc08a90ad2ba4df7ae4969a8a"></a>

### [`004c1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md) → [`004c21a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c21a4.md) FUN_004c21a4

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004c1e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e7c.md) [`004c2fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fd8.md) · 呼出先 10件 [`004b1434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1434.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`004bfce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00543898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md)
- 新版 呼出元 2件 [`004c219c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c219c.md) [`004c32f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c32f8.md) · 呼出先 10件 [`004b1754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b1/004b1754.md) [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`004c0004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0004.md) [`00540604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md) [`00543bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543bb8.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c2590",
      "incomplete_value": true,
      "site": "004c2590",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2270",
      "incomplete_value": true,
      "site": "004c2270",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c2580",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c2580",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md#insn-004c2270) · [`004c1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md#insn-004c1ec4) · [`004c1f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md#insn-004c1f2c)
- 新版 [`004c2590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c21a4.md#insn-004c2590) · [`004c21e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c21a4.md#insn-004c21e4) · [`004c224c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c21a4.md#insn-004c224c)

~~~diff
- 004c2270 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2270 ["INT_ADD", "register:40f0:8", ["const:4c2270:8", "const:4:8"]]
- 004c2270 ["CALLIND", null, ["register:0:8"]]
+ 004c2590 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2590 ["INT_ADD", "register:40f0:8", ["const:4c2590:8", "const:4:8"]]
+ 004c2590 ["CALLIND", null, ["register:0:8"]]
- 004c2270 bytes 20013fd6
+ 004c2590 bytes 20013fd6
- 004c1ec4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1ec4 ["INT_ADD", "register:40f0:8", ["const:4c1ec4:8", "const:4:8"]]
- 004c1ec4 ["CALLIND", null, ["register:0:8"]]
+ 004c21e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c21e4 ["INT_ADD", "register:40f0:8", ["const:4c21e4:8", "const:4:8"]]
+ 004c21e4 ["CALLIND", null, ["register:0:8"]]
- 004c1ec4 bytes 00013fd6
+ 004c21e4 bytes 00013fd6
- 004c1f2c ["INT_ADD", "register:40f0:8", ["const:4c1f2c:8", "const:4:8"]]
- 004c1f2c ["CALL", null, ["callee:00540604:8"]]
+ 004c224c ["INT_ADD", "register:40f0:8", ["const:4c224c:8", "const:4:8"]]
+ 004c224c ["CALL", null, ["callee:00540604:8"]]
- 004c1f2c bytes eef80194
+ 004c224c bytes eef80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d0f8ff33d830a8d607c88b76fe8a888"></a>

### [`004c22d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md) → [`004c25f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c25f0.md) _ZNK5Botan4PSSR4nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2630",
      "incomplete_value": false,
      "site": "004c263c",
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
            "const:fdc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2310",
      "incomplete_value": false,
      "site": "004c231c",
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
            "const:f0d:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c265c",
      "incomplete_value": false,
      "site": "004c2664",
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
            "const:80f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c233c",
      "incomplete_value": false,
      "site": "004c2344",
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
            "const:742:8"
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
      "definition_site": "004c26cc",
      "incomplete_value": false,
      "site": "004c26d4",
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
            "const:3a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c23ac",
      "incomplete_value": false,
      "site": "004c23b4",
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
            "const:2d6:8"
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
      "004c2630",
      "PARAM",
      [
        "storage",
        "002b8f0d",
        null,
        "string"
      ]
    ],
    [
      "004c265c",
      "PARAM",
      [
        "storage",
        "002ad742",
        null,
        "string"
      ]
    ],
    [
      "004c26cc",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c2630",
      "PARAM",
      [
        "storage",
        "002b8fdc",
        null,
        "string"
      ]
    ],
    [
      "004c265c",
      "PARAM",
      [
        "storage",
        "002ad80f",
        null,
        "string"
      ]
    ],
    [
      "004c26cc",
      "PARAM",
      [
        "storage",
        "002ab3a3",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c231c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md#insn-004c231c) · [`004c2344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md#insn-004c2344) · [`004c23b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md#insn-004c23b4)
- 新版 [`004c263c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c25f0.md#insn-004c263c) · [`004c2664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c25f0.md#insn-004c2664) · [`004c26d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c25f0.md#insn-004c26d4)

~~~diff
- 004c231c ["INT_ADD", "register:40f0:8", ["const:4c231c:8", "const:4:8"]]
- 004c231c ["CALL", null, ["callee:00c59000:8"]]
+ 004c263c ["INT_ADD", "register:40f0:8", ["const:4c263c:8", "const:4:8"]]
+ 004c263c ["CALL", null, ["callee:00c59000:8"]]
- 004c231c bytes 45571e94
+ 004c263c bytes 715a1e94
- 004c2344 ["INT_ADD", "register:40f0:8", ["const:4c2344:8", "const:4:8"]]
- 004c2344 ["CALL", null, ["callee:00c59010:8"]]
+ 004c2664 ["INT_ADD", "register:40f0:8", ["const:4c2664:8", "const:4:8"]]
+ 004c2664 ["CALL", null, ["callee:00c59010:8"]]
- 004c2344 bytes 3f571e94
+ 004c2664 bytes 6b5a1e94
- 004c23b4 ["INT_ADD", "register:40f0:8", ["const:4c23b4:8", "const:4:8"]]
- 004c23b4 ["CALL", null, ["callee:00c59010:8"]]
+ 004c26d4 ["INT_ADD", "register:40f0:8", ["const:4c26d4:8", "const:4:8"]]
+ 004c26d4 ["CALL", null, ["callee:00c59010:8"]]
- 004c23b4 bytes 23571e94
+ 004c26d4 bytes 4f5a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11e7e37144c04edd7a4f042b0973635f"></a>

### [`004c253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md) → [`004c285c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c285c.md) _ZNK5Botan4PSSR15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`004c07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`004c0b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0b14.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.99% / 新版 94.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 4件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c2998",
      "incomplete_value": true,
      "site": "004c2998",
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
      "definition_site": "004c2678",
      "incomplete_value": true,
      "site": "004c2678",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c29d8",
      "incomplete_value": true,
      "site": "004c29d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c26b8",
      "incomplete_value": true,
      "site": "004c26b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a6f:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004c2b54",
      "incomplete_value": true,
      "site": "004c2b54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2834",
      "incomplete_value": true,
      "site": "004c2834",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c298c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004c2998",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c29c0",
      "READ",
      [
        "storage",
        "002b1a6f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c298c",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "004c2998",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c29c0",
      "READ",
      [
        "storage",
        "002b1ab9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c266c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md#insn-004c266c) · [`004c2834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md#insn-004c2834) · [`004c2894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md#insn-004c2894)
- 新版 [`004c298c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c285c.md#insn-004c298c) · [`004c2b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c285c.md#insn-004c2b54) · [`004c2bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c285c.md#insn-004c2bb4)

~~~diff
- 004c266c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
- 004c266c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c298c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 004c298c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c266c bytes 080547f9
+ 004c298c bytes 08ed46f9
- 004c2834 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2834 ["INT_ADD", "register:40f0:8", ["const:4c2834:8", "const:4:8"]]
- 004c2834 ["CALLIND", null, ["register:0:8"]]
+ 004c2b54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2b54 ["INT_ADD", "register:40f0:8", ["const:4c2b54:8", "const:4:8"]]
+ 004c2b54 ["CALLIND", null, ["register:0:8"]]
- 004c2834 bytes 20013fd6
+ 004c2b54 bytes 20013fd6
- 004c2894 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2894 ["INT_ADD", "register:40f0:8", ["const:4c2894:8", "const:4:8"]]
- 004c2894 ["CALLIND", null, ["register:0:8"]]
+ 004c2bb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2bb4 ["INT_ADD", "register:40f0:8", ["const:4c2bb4:8", "const:4:8"]]
+ 004c2bb4 ["CALLIND", null, ["register:0:8"]]
- 004c2894 bytes 20013fd6
+ 004c2bb4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31d5b9979c77a6cd762c83eabea61a76"></a>

### [`004c2cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md) → [`004c3014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3014.md) _ZN5Botan8PSSR_RawC1EPNS_12HashFunctionE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "004c3034",
      "incomplete_value": true,
      "site": "004c3038",
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
      "definition_site": "004c2d14",
      "incomplete_value": true,
      "site": "004c2d18",
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
      "004c302c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004c3038",
      "DATA",
      [
        "storage",
        "00c66750",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c302c",
      "READ",
      [
        "storage",
        "00c9bf08",
        null,
        "pointer"
      ]
    ],
    [
      "004c3038",
      "DATA",
      [
        "storage",
        "00c67720",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md#insn-004c2d00) · [`004c2d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md#insn-004c2d0c) · [`004c2d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md#insn-004c2d24)
- 新版 [`004c3020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3014.md#insn-004c3020) · [`004c302c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3014.md#insn-004c302c) · [`004c3044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3014.md#insn-004c3044)

~~~diff
- 004c2d00 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c3020 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c2d00 bytes c83e0090
+ 004c3020 bytes c83e0090
- 004c2d0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
- 004c2d0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c302c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f08:8"]]
+ 004c302c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c2d0c bytes 089d47f9
+ 004c302c bytes 088547f9
- 004c2d24 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c2d24 ["INT_ADD", "register:40f0:8", ["const:4c2d24:8", "const:4:8"]]
- 004c2d24 ["CALLIND", null, ["register:0:8"]]
+ 004c3044 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3044 ["INT_ADD", "register:40f0:8", ["const:4c3044:8", "const:4:8"]]
+ 004c3044 ["CALLIND", null, ["register:0:8"]]
- 004c2d24 bytes 00013fd6
+ 004c3044 bytes 00013fd6
~~~


<a id="compare-4537cf45da52f3343817034b7f25789c"></a>

### [`004c2d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md) → [`004c30b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c30b4.md) _ZN5Botan8PSSR_Raw8raw_dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3158",
      "incomplete_value": false,
      "site": "004c3160",
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
            "const:18c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2e38",
      "incomplete_value": false,
      "site": "004c2e40",
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
            "const:c1:8"
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
      "definition_site": "004c3190",
      "incomplete_value": true,
      "site": "004c319c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2e70",
      "incomplete_value": true,
      "site": "004c2e7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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
      "definition_site": "004c318c",
      "incomplete_value": false,
      "site": "004c319c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c2e6c",
      "incomplete_value": false,
      "site": "004c2e7c",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c3158",
      "PARAM",
      [
        "storage",
        "002a30c1",
        null,
        "string"
      ]
    ],
    [
      "004c318c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c3190",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c3158",
      "PARAM",
      [
        "storage",
        "002a318c",
        null,
        "string"
      ]
    ],
    [
      "004c318c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c3190",
      "READ",
      [
        "storage",
        "00c9be38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md#insn-004c2e40) · [`004c2e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md#insn-004c2e7c) · [`004c2de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md#insn-004c2de8)
- 新版 [`004c3160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c30b4.md#insn-004c3160) · [`004c319c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c30b4.md#insn-004c319c) · [`004c3108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c30b4.md#insn-004c3108)

~~~diff
- 004c2e40 ["INT_ADD", "register:40f0:8", ["const:4c2e40:8", "const:4:8"]]
- 004c2e40 ["CALL", null, ["callee:0043e138:8"]]
+ 004c3160 ["INT_ADD", "register:40f0:8", ["const:4c3160:8", "const:4:8"]]
+ 004c3160 ["CALL", null, ["callee:0043e138:8"]]
- 004c2e40 bytes f6ebfd97
+ 004c3160 bytes f6ebfd97
- 004c2e7c ["INT_ADD", "register:40f0:8", ["const:4c2e7c:8", "const:4:8"]]
- 004c2e7c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c319c ["INT_ADD", "register:40f0:8", ["const:4c319c:8", "const:4:8"]]
+ 004c319c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c2e7c bytes 59541e94
+ 004c319c bytes 85571e94
- 004c2de8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2de8 ["INT_ADD", "register:40f0:8", ["const:4c2de8:8", "const:4:8"]]
- 004c2de8 ["CALLIND", null, ["register:0:8"]]
+ 004c3108 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c3108 ["INT_ADD", "register:40f0:8", ["const:4c3108:8", "const:4:8"]]
+ 004c3108 ["CALLIND", null, ["register:0:8"]]
- 004c2de8 bytes 20013fd6
+ 004c3108 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-359c154bd46615eeaffcc1f584a92e78"></a>

### [`004c2fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md) → [`004c3300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3300.md) _ZNK5Botan8PSSR_Raw4nameEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3340",
      "incomplete_value": false,
      "site": "004c334c",
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
            "const:61:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3020",
      "incomplete_value": false,
      "site": "004c302c",
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
            "const:21:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c336c",
      "incomplete_value": false,
      "site": "004c3374",
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
            "const:80f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c304c",
      "incomplete_value": false,
      "site": "004c3054",
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
            "const:742:8"
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
      "definition_site": "004c33dc",
      "incomplete_value": false,
      "site": "004c33e4",
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
            "const:3a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c30bc",
      "incomplete_value": false,
      "site": "004c30c4",
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
            "const:2d6:8"
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
      "004c3340",
      "PARAM",
      [
        "storage",
        "002a1021",
        null,
        "string"
      ]
    ],
    [
      "004c336c",
      "PARAM",
      [
        "storage",
        "002ad742",
        null,
        "string"
      ]
    ],
    [
      "004c33dc",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c3340",
      "PARAM",
      [
        "storage",
        "002a1061",
        null,
        "string"
      ]
    ],
    [
      "004c336c",
      "PARAM",
      [
        "storage",
        "002ad80f",
        null,
        "string"
      ]
    ],
    [
      "004c33dc",
      "PARAM",
      [
        "storage",
        "002ab3a3",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c302c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md#insn-004c302c) · [`004c3054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md#insn-004c3054) · [`004c30c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md#insn-004c30c4)
- 新版 [`004c334c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3300.md#insn-004c334c) · [`004c3374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3300.md#insn-004c3374) · [`004c33e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3300.md#insn-004c33e4)

~~~diff
- 004c302c ["INT_ADD", "register:40f0:8", ["const:4c302c:8", "const:4:8"]]
- 004c302c ["CALL", null, ["callee:00c59000:8"]]
+ 004c334c ["INT_ADD", "register:40f0:8", ["const:4c334c:8", "const:4:8"]]
+ 004c334c ["CALL", null, ["callee:00c59000:8"]]
- 004c302c bytes 01541e94
+ 004c334c bytes 2d571e94
- 004c3054 ["INT_ADD", "register:40f0:8", ["const:4c3054:8", "const:4:8"]]
- 004c3054 ["CALL", null, ["callee:00c59010:8"]]
+ 004c3374 ["INT_ADD", "register:40f0:8", ["const:4c3374:8", "const:4:8"]]
+ 004c3374 ["CALL", null, ["callee:00c59010:8"]]
- 004c3054 bytes fb531e94
+ 004c3374 bytes 27571e94
- 004c30c4 ["INT_ADD", "register:40f0:8", ["const:4c30c4:8", "const:4:8"]]
- 004c30c4 ["CALL", null, ["callee:00c59010:8"]]
+ 004c33e4 ["INT_ADD", "register:40f0:8", ["const:4c33e4:8", "const:4:8"]]
+ 004c33e4 ["CALL", null, ["callee:00c59010:8"]]
- 004c30c4 bytes df531e94
+ 004c33e4 bytes 0b571e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2dc28f0ef2731f93f37f01de85b54c7"></a>

### [`004c324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md) → [`004c356c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c356c.md) _ZN5Botan14Entropy_Source6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "004c3630",
      "incomplete_value": false,
      "site": "004c3638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3310",
      "incomplete_value": false,
      "site": "004c3318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "004c3638",
      "DATA",
      [
        "storage",
        "00c69d58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c3638",
      "DATA",
      [
        "storage",
        "00c6ad28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md#insn-004c3308) · [`004c330c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md#insn-004c330c) · [`004c3310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md#insn-004c3310)
- 新版 [`004c3628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c356c.md#insn-004c3628) · [`004c362c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c356c.md#insn-004c362c) · [`004c3630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c356c.md#insn-004c3630)

~~~diff
- 004c3308 ["INT_ADD", "register:40f0:8", ["const:4c3308:8", "const:4:8"]]
- 004c3308 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c3628 ["INT_ADD", "register:40f0:8", ["const:4c3628:8", "const:4:8"]]
+ 004c3628 ["CALL", null, ["callee:00c58f30:8"]]
- 004c3308 bytes 16531e94
+ 004c3628 bytes 42561e94
- 004c330c ["COPY", "register:4048:8", ["const:c69000:8"]]
+ 004c362c ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 004c330c bytes 293d00d0
+ 004c362c bytes 293d00f0
- 004c3310 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 004c3310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c3310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c3310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c3630 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 004c3630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c3630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c3630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c3310 bytes 29613591
+ 004c3630 bytes 29a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd17d797debf44c3881fdd09d4908e5b"></a>

### [`004c3b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md) → [`004c3e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e9c.md) _ZN5Botan15Entropy_Sources14global_sourcesEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004c3edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3edc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440e60.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`004c41fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c41fc.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 87.94% / 新版 87.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3f04",
      "incomplete_value": false,
      "site": "004c3f08",
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
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3be4",
      "incomplete_value": false,
      "site": "004c3be8",
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
            "const:360:8"
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
      "definition_site": "004c3f14",
      "incomplete_value": false,
      "site": "004c3f20",
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
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3bf4",
      "incomplete_value": false,
      "site": "004c3c00",
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
            "const:d8a:8"
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
      "definition_site": "004c3f2c",
      "incomplete_value": false,
      "site": "004c3f34",
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
            "const:c9d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3c0c",
      "incomplete_value": false,
      "site": "004c3c14",
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
            "const:bd0:8"
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
      "004c3ec8",
      "READ",
      [
        "storage",
        "00ca5360",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3ee4",
      "DATA",
      [
        "storage",
        "00ca5348",
        null,
        null
      ]
    ],
    [
      "004c3f04",
      "PARAM",
      [
        "storage",
        "00ca5360",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004c3ec8",
      "READ",
      [
        "storage",
        "00ca6320",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3ee4",
      "DATA",
      [
        "storage",
        "00ca6308",
        null,
        null
      ]
    ],
    [
      "004c3f04",
      "PARAM",
      [
        "storage",
        "00ca6320",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md#insn-004c3be8) · [`004c3c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md#insn-004c3c00) · [`004c3c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md#insn-004c3c14)
- 新版 [`004c3f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e9c.md#insn-004c3f08) · [`004c3f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e9c.md#insn-004c3f20) · [`004c3f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c3e9c.md#insn-004c3f34)

~~~diff
- 004c3be8 ["INT_ADD", "register:40f0:8", ["const:4c3be8:8", "const:4:8"]]
- 004c3be8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 004c3f08 ["INT_ADD", "register:40f0:8", ["const:4c3f08:8", "const:4:8"]]
+ 004c3f08 ["CALL", null, ["callee:00c58ef0:8"]]
- 004c3be8 bytes ce501e94
+ 004c3f08 bytes fa531e94
- 004c3c00 ["INT_ADD", "register:40f0:8", ["const:4c3c00:8", "const:4:8"]]
- 004c3c00 ["CALL", null, ["callee:0043e138:8"]]
+ 004c3f20 ["INT_ADD", "register:40f0:8", ["const:4c3f20:8", "const:4:8"]]
+ 004c3f20 ["CALL", null, ["callee:0043e138:8"]]
- 004c3c00 bytes 86e8fd97
+ 004c3f20 bytes 86e8fd97
- 004c3c14 ["INT_ADD", "register:40f0:8", ["const:4c3c14:8", "const:4:8"]]
- 004c3c14 ["CALL", null, ["callee:0043e138:8"]]
+ 004c3f34 ["INT_ADD", "register:40f0:8", ["const:4c3f34:8", "const:4:8"]]
+ 004c3f34 ["CALL", null, ["callee:0043e138:8"]]
- 004c3c14 bytes 81e8fd97
+ 004c3f34 bytes 81e8fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d36f29d99e4d8fea3397290da38e55b2"></a>

### [`004c3f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md) → [`004c4278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4278.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c42ac",
      "incomplete_value": true,
      "site": "004c42b4",
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
      "definition_site": "004c3f8c",
      "incomplete_value": true,
      "site": "004c3f94",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c42e8",
      "incomplete_value": true,
      "site": "004c42f0",
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
      "definition_site": "004c3fc8",
      "incomplete_value": true,
      "site": "004c3fd0",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4368",
      "incomplete_value": true,
      "site": "004c4370",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c4048",
      "incomplete_value": true,
      "site": "004c4050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c4298",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c42b4",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c42dc",
      "READ",
      [
        "storage",
        "00c9af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4298",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c42b4",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c42dc",
      "READ",
      [
        "storage",
        "00c9bf18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md#insn-004c4050) · [`004c3f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md#insn-004c3f6c) · [`004c3f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md#insn-004c3f78)
- 新版 [`004c4370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4278.md#insn-004c4370) · [`004c428c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4278.md#insn-004c428c) · [`004c4298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4278.md#insn-004c4298)

~~~diff
- 004c4050 ["INT_ADD", "register:40f0:8", ["const:4c4050:8", "const:4:8"]]
- 004c4050 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c4370 ["INT_ADD", "register:40f0:8", ["const:4c4370:8", "const:4:8"]]
+ 004c4370 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c4050 bytes e44f1e94
+ 004c4370 bytes 10531e94
- 004c3f6c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c428c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c3f6c bytes a83e00f0
+ 004c428c bytes a83e00f0
- 004c3f78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c3f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c4298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c3f78 bytes 08a147f9
+ 004c4298 bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed2fd2f5deb17793d363858f659eb3d7"></a>

### [`004c40a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md) → [`004c43c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c43c8.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherERKNS_11OctetStringE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004bcd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4404",
      "incomplete_value": true,
      "site": "004c440c",
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
      "definition_site": "004c40e4",
      "incomplete_value": true,
      "site": "004c40ec",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c4444",
      "incomplete_value": true,
      "site": "004c444c",
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
      "definition_site": "004c4124",
      "incomplete_value": true,
      "site": "004c412c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c44d8",
      "incomplete_value": true,
      "site": "004c44e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c41b8",
      "incomplete_value": true,
      "site": "004c41c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c43f0",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c440c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4434",
      "READ",
      [
        "storage",
        "00c9af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c43f0",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c440c",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4434",
      "READ",
      [
        "storage",
        "00c9bf18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c41c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md#insn-004c41c0) · [`004c40c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md#insn-004c40c4) · [`004c40d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md#insn-004c40d0)
- 新版 [`004c44e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c43c8.md#insn-004c44e0) · [`004c43e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c43c8.md#insn-004c43e4) · [`004c43f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c43c8.md#insn-004c43f0)

~~~diff
- 004c41c0 ["INT_ADD", "register:40f0:8", ["const:4c41c0:8", "const:4:8"]]
- 004c41c0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c44e0 ["INT_ADD", "register:40f0:8", ["const:4c44e0:8", "const:4:8"]]
+ 004c44e0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c41c0 bytes 884f1e94
+ 004c44e0 bytes b4521e94
- 004c40c4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c43e4 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c40c4 bytes a93e00d0
+ 004c43e4 bytes a93e00f0
- 004c40d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 004c40d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c43f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f10:8"]]
+ 004c43f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c40d0 bytes 29a147f9
+ 004c43f0 bytes 298947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3e7b56e18718271139a541ebc2bb80"></a>

### [`004c4240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md) → [`004c4560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4560.md) _ZN5Botan19StreamCipher_FilterC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4594",
      "incomplete_value": true,
      "site": "004c459c",
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
      "definition_site": "004c4274",
      "incomplete_value": true,
      "site": "004c427c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c45d4",
      "incomplete_value": true,
      "site": "004c45dc",
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
      "definition_site": "004c42b4",
      "incomplete_value": true,
      "site": "004c42bc",
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4674",
      "incomplete_value": true,
      "site": "004c467c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c4354",
      "incomplete_value": true,
      "site": "004c435c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c4580",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c459c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c45c4",
      "READ",
      [
        "storage",
        "00c9af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4580",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c459c",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c45c4",
      "READ",
      [
        "storage",
        "00c9bf18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c435c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md#insn-004c435c) · [`004c4254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md#insn-004c4254) · [`004c4260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md#insn-004c4260)
- 新版 [`004c467c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4560.md#insn-004c467c) · [`004c4574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4560.md#insn-004c4574) · [`004c4580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4560.md#insn-004c4580)

~~~diff
- 004c435c ["INT_ADD", "register:40f0:8", ["const:4c435c:8", "const:4:8"]]
- 004c435c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c467c ["INT_ADD", "register:40f0:8", ["const:4c467c:8", "const:4:8"]]
+ 004c467c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c435c bytes 214f1e94
+ 004c467c bytes 4d521e94
- 004c4254 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c4574 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c4254 bytes a83e00d0
+ 004c4574 bytes a83e00f0
- 004c4260 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c4260 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4580 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c4580 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4260 bytes 08a147f9
+ 004c4580 bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b87c954d41c680f7284feb5cc594cc6"></a>

### [`004c43d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md) → [`004c46f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c46f4.md) _ZN5Botan12StreamCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f20.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ef0.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c476c",
      "incomplete_value": false,
      "site": "004c4774",
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
            "const:33e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c444c",
      "incomplete_value": false,
      "site": "004c4454",
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
            "const:260:8"
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
      "definition_site": "004c47ac",
      "incomplete_value": true,
      "site": "004c47b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c448c",
      "incomplete_value": true,
      "site": "004c4498",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
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
      "definition_site": "004c47a8",
      "incomplete_value": false,
      "site": "004c47b8",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c4488",
      "incomplete_value": false,
      "site": "004c4498",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c476c",
      "PARAM",
      [
        "storage",
        "002ba260",
        null,
        "string"
      ]
    ],
    [
      "004c47a8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c47ac",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c476c",
      "PARAM",
      [
        "storage",
        "002ba33e",
        null,
        "string"
      ]
    ],
    [
      "004c47a8",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c47ac",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md#insn-004c4454) · [`004c4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md#insn-004c4498) · [`004c4408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md#insn-004c4408)
- 新版 [`004c4774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c46f4.md#insn-004c4774) · [`004c47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c46f4.md#insn-004c47b8) · [`004c4728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c46f4.md#insn-004c4728)

~~~diff
- 004c4454 ["INT_ADD", "register:40f0:8", ["const:4c4454:8", "const:4:8"]]
- 004c4454 ["CALL", null, ["callee:0043e138:8"]]
+ 004c4774 ["INT_ADD", "register:40f0:8", ["const:4c4774:8", "const:4:8"]]
+ 004c4774 ["CALL", null, ["callee:0043e138:8"]]
- 004c4454 bytes 71e6fd97
+ 004c4774 bytes 71e6fd97
- 004c4498 ["INT_ADD", "register:40f0:8", ["const:4c4498:8", "const:4:8"]]
- 004c4498 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c47b8 ["INT_ADD", "register:40f0:8", ["const:4c47b8:8", "const:4:8"]]
+ 004c47b8 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c4498 bytes d24e1e94
+ 004c47b8 bytes fe511e94
- 004c4408 ["INT_ADD", "register:40f0:8", ["const:4c4408:8", "const:4:8"]]
- 004c4408 ["CALL", null, ["callee:00c59f00:8"]]
+ 004c4728 ["INT_ADD", "register:40f0:8", ["const:4c4728:8", "const:4:8"]]
+ 004c4728 ["CALL", null, ["callee:00c59f00:8"]]
- 004c4408 bytes ca521e94
+ 004c4728 bytes f6551e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a01b73950098a6aba27059adc6b69ce"></a>

### [`004c44e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md) → [`004c4808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4808.md) _ZN5Botan19StreamCipher_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004bcd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4844",
      "incomplete_value": true,
      "site": "004c484c",
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
      "definition_site": "004c4524",
      "incomplete_value": true,
      "site": "004c452c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c4884",
      "incomplete_value": true,
      "site": "004c488c",
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
      "definition_site": "004c4564",
      "incomplete_value": true,
      "site": "004c456c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4938",
      "incomplete_value": true,
      "site": "004c4940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c4618",
      "incomplete_value": true,
      "site": "004c4620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c4830",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c484c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4874",
      "READ",
      [
        "storage",
        "00c9af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4830",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c484c",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4874",
      "READ",
      [
        "storage",
        "00c9bf18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md#insn-004c4620) · [`004c4504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md#insn-004c4504) · [`004c4510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md#insn-004c4510)
- 新版 [`004c4940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4808.md#insn-004c4940) · [`004c4824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4808.md#insn-004c4824) · [`004c4830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4808.md#insn-004c4830)

~~~diff
- 004c4620 ["INT_ADD", "register:40f0:8", ["const:4c4620:8", "const:4:8"]]
- 004c4620 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c4940 ["INT_ADD", "register:40f0:8", ["const:4c4940:8", "const:4:8"]]
+ 004c4940 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c4620 bytes 704e1e94
+ 004c4940 bytes 9c511e94
- 004c4504 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c4824 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c4504 bytes a93e00d0
+ 004c4824 bytes a93e00f0
- 004c4510 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 004c4510 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4830 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f10:8"]]
+ 004c4830 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4510 bytes 29a147f9
+ 004c4830 bytes 298947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f2cbcd32e5be17726afcc3a02d32aad"></a>

### [`004c4734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md) → [`004c4a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4a54.md) _ZN5Botan11Hash_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f10.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4a90",
      "incomplete_value": true,
      "site": "004c4a98",
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
      "definition_site": "004c4770",
      "incomplete_value": true,
      "site": "004c4778",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c4ac4",
      "incomplete_value": true,
      "site": "004c4acc",
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
      "definition_site": "004c47a4",
      "incomplete_value": true,
      "site": "004c47ac",
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
      "004c4a7c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4a98",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4ab8",
      "READ",
      [
        "storage",
        "00c9af50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4a7c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c4a98",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4ab8",
      "READ",
      [
        "storage",
        "00c9bf20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md#insn-004c4750) · [`004c475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md#insn-004c475c) · [`004c4790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md#insn-004c4790)
- 新版 [`004c4a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4a54.md#insn-004c4a70) · [`004c4a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4a54.md#insn-004c4a7c) · [`004c4ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4a54.md#insn-004c4ab0)

~~~diff
- 004c4750 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c4a70 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c4750 bytes a93e00d0
+ 004c4a70 bytes a93e00f0
- 004c475c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 004c475c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4a7c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f10:8"]]
+ 004c4a7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c475c bytes 29a147f9
+ 004c4a7c bytes 298947f9
- 004c4790 ["INT_ADD", "register:40f0:8", ["const:4c4790:8", "const:4:8"]]
- 004c4790 ["CALL", null, ["callee:00543fbc:8"]]
+ 004c4ab0 ["INT_ADD", "register:40f0:8", ["const:4c4ab0:8", "const:4:8"]]
+ 004c4ab0 ["CALL", null, ["callee:00543fbc:8"]]
- 004c4790 bytes 43fd0194
+ 004c4ab0 bytes 43fd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e3e46012dfa9e0432cb3cf9fd2d4ec2"></a>

### [`004c4858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md) → [`004c4b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4b78.md) _ZN5Botan6FilterC2Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4b9c",
      "incomplete_value": true,
      "site": "004c4ba0",
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
      "definition_site": "004c487c",
      "incomplete_value": true,
      "site": "004c4880",
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
      "004c4b94",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4ba0",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c4b94",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c4ba0",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md#insn-004c4868) · [`004c4874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md#insn-004c4874) · [`004c4878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md#insn-004c4878)
- 新版 [`004c4b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4b78.md#insn-004c4b88) · [`004c4b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4b78.md#insn-004c4b94)

~~~diff
- 004c4868 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c4b88 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c4868 bytes a83e00d0
+ 004c4b88 bytes a83e00f0
- 004c4874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c4874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4b94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c4b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4874 bytes 08a147f9
+ 004c4b94 bytes 088947f9
- 004c4878 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004c4878 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab78e250a432d74d82c48c577bf38d4"></a>

### [`004c48dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md) → [`004c4bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4bfc.md) _ZN5Botan12HashFunction15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f40.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f10.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4c74",
      "incomplete_value": false,
      "site": "004c4c7c",
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
            "const:f8f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4954",
      "incomplete_value": false,
      "site": "004c495c",
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
            "const:f4f:8"
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
      "definition_site": "004c4cb4",
      "incomplete_value": true,
      "site": "004c4cc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4994",
      "incomplete_value": true,
      "site": "004c49a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
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
      "definition_site": "004c4cb0",
      "incomplete_value": false,
      "site": "004c4cc0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c4990",
      "incomplete_value": false,
      "site": "004c49a0",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c4c74",
      "PARAM",
      [
        "storage",
        "002a1f4f",
        null,
        null
      ]
    ],
    [
      "004c4cb0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c4cb4",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4c74",
      "PARAM",
      [
        "storage",
        "002a1f8f",
        null,
        null
      ]
    ],
    [
      "004c4cb0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c4cb4",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c495c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md#insn-004c495c) · [`004c49a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md#insn-004c49a0) · [`004c4910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md#insn-004c4910)
- 新版 [`004c4c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4bfc.md#insn-004c4c7c) · [`004c4cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4bfc.md#insn-004c4cc0) · [`004c4c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4bfc.md#insn-004c4c30)

~~~diff
- 004c495c ["INT_ADD", "register:40f0:8", ["const:4c495c:8", "const:4:8"]]
- 004c495c ["CALL", null, ["callee:0043e138:8"]]
+ 004c4c7c ["INT_ADD", "register:40f0:8", ["const:4c4c7c:8", "const:4:8"]]
+ 004c4c7c ["CALL", null, ["callee:0043e138:8"]]
- 004c495c bytes 2fe5fd97
+ 004c4c7c bytes 2fe5fd97
- 004c49a0 ["INT_ADD", "register:40f0:8", ["const:4c49a0:8", "const:4:8"]]
- 004c49a0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c4cc0 ["INT_ADD", "register:40f0:8", ["const:4c4cc0:8", "const:4:8"]]
+ 004c4cc0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c49a0 bytes 904d1e94
+ 004c4cc0 bytes bc501e94
- 004c4910 ["INT_ADD", "register:40f0:8", ["const:4c4910:8", "const:4:8"]]
- 004c4910 ["CALL", null, ["callee:00c59e90:8"]]
+ 004c4c30 ["INT_ADD", "register:40f0:8", ["const:4c4c30:8", "const:4:8"]]
+ 004c4c30 ["CALL", null, ["callee:00c59e90:8"]]
- 004c4910 bytes 6c511e94
+ 004c4c30 bytes 98541e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1478495114d85705871784bdbf717c38"></a>

### [`004c4b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md) → [`004c4e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4e34.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4e70",
      "incomplete_value": true,
      "site": "004c4e78",
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
      "definition_site": "004c4b50",
      "incomplete_value": true,
      "site": "004c4b58",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c4ea4",
      "incomplete_value": true,
      "site": "004c4eac",
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
      "definition_site": "004c4b84",
      "incomplete_value": true,
      "site": "004c4b8c",
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
      "004c4e5c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4e78",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4e98",
      "READ",
      [
        "storage",
        "00c9af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4e5c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c4e78",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4e98",
      "READ",
      [
        "storage",
        "00c9bf28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md#insn-004c4b30) · [`004c4b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md#insn-004c4b3c) · [`004c4b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md#insn-004c4b70)
- 新版 [`004c4e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4e34.md#insn-004c4e50) · [`004c4e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4e34.md#insn-004c4e5c) · [`004c4e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4e34.md#insn-004c4e90)

~~~diff
- 004c4b30 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c4e50 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c4b30 bytes a93e00d0
+ 004c4e50 bytes a93e00f0
- 004c4b3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 004c4b3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4e5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f10:8"]]
+ 004c4e5c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4b3c bytes 29a147f9
+ 004c4e5c bytes 298947f9
- 004c4b70 ["INT_ADD", "register:40f0:8", ["const:4c4b70:8", "const:4:8"]]
- 004c4b70 ["CALL", null, ["callee:00543fbc:8"]]
+ 004c4e90 ["INT_ADD", "register:40f0:8", ["const:4c4e90:8", "const:4:8"]]
+ 004c4e90 ["CALL", null, ["callee:00543fbc:8"]]
- 004c4b70 bytes 4bfc0194
+ 004c4e90 bytes 4bfc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12a53e3a720616d46cfe860f50a7f4d5"></a>

### [`004c4c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md) → [`004c4f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4f58.md) _ZN5Botan25MessageAuthenticationCode15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f50.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f20.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4fd0",
      "incomplete_value": false,
      "site": "004c4fd8",
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
            "const:7d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4cb0",
      "incomplete_value": false,
      "site": "004c4cb8",
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
            "const:707:8"
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
      "definition_site": "004c5010",
      "incomplete_value": true,
      "site": "004c501c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4cf0",
      "incomplete_value": true,
      "site": "004c4cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
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
      "definition_site": "004c500c",
      "incomplete_value": false,
      "site": "004c501c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c4cec",
      "incomplete_value": false,
      "site": "004c4cfc",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c4fd0",
      "PARAM",
      [
        "storage",
        "002ac707",
        null,
        null
      ]
    ],
    [
      "004c500c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c5010",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4fd0",
      "PARAM",
      [
        "storage",
        "002ac7d4",
        null,
        null
      ]
    ],
    [
      "004c500c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c5010",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md#insn-004c4cb8) · [`004c4cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md#insn-004c4cfc) · [`004c4c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md#insn-004c4c6c)
- 新版 [`004c4fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4f58.md#insn-004c4fd8) · [`004c501c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4f58.md#insn-004c501c) · [`004c4f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c4/004c4f58.md#insn-004c4f8c)

~~~diff
- 004c4cb8 ["INT_ADD", "register:40f0:8", ["const:4c4cb8:8", "const:4:8"]]
- 004c4cb8 ["CALL", null, ["callee:0043e138:8"]]
+ 004c4fd8 ["INT_ADD", "register:40f0:8", ["const:4c4fd8:8", "const:4:8"]]
+ 004c4fd8 ["CALL", null, ["callee:0043e138:8"]]
- 004c4cb8 bytes 58e4fd97
+ 004c4fd8 bytes 58e4fd97
- 004c4cfc ["INT_ADD", "register:40f0:8", ["const:4c4cfc:8", "const:4:8"]]
- 004c4cfc ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c501c ["INT_ADD", "register:40f0:8", ["const:4c501c:8", "const:4:8"]]
+ 004c501c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c4cfc bytes b94c1e94
+ 004c501c bytes e54f1e94
- 004c4c6c ["INT_ADD", "register:40f0:8", ["const:4c4c6c:8", "const:4:8"]]
- 004c4c6c ["CALL", null, ["callee:00c59f30:8"]]
+ 004c4f8c ["INT_ADD", "register:40f0:8", ["const:4c4f8c:8", "const:4:8"]]
+ 004c4f8c ["CALL", null, ["callee:00c59f30:8"]]
- 004c4c6c bytes bd501e94
+ 004c4f8c bytes e9531e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08aa2341900647378d56e2ea2451146b"></a>

### [`004c4d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md) → [`004c506c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c506c.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f50.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bcd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bcd60.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c50ac",
      "incomplete_value": true,
      "site": "004c50b4",
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
      "definition_site": "004c4d8c",
      "incomplete_value": true,
      "site": "004c4d94",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c50e0",
      "incomplete_value": true,
      "site": "004c50e8",
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
      "definition_site": "004c4dc0",
      "incomplete_value": true,
      "site": "004c4dc8",
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
      "004c5094",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c50b4",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c50d4",
      "READ",
      [
        "storage",
        "00c9af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5094",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c50b4",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c50d4",
      "READ",
      [
        "storage",
        "00c9bf28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md#insn-004c4d68) · [`004c4d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md#insn-004c4d74) · [`004c4d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md#insn-004c4d90)
- 新版 [`004c5088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c506c.md#insn-004c5088) · [`004c5094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c506c.md#insn-004c5094)

~~~diff
- 004c4d68 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c5088 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c4d68 bytes a93e00d0
+ 004c5088 bytes a93e00d0
- 004c4d74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 004c4d74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5094 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f10:8"]]
+ 004c5094 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4d74 bytes 29a147f9
+ 004c5094 bytes 298947f9
- 004c4d90 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 004c4d90 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5783ddf884de782773c1fac8a47b8b1f"></a>

### [`004c4fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md) → [`004c52ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c52ec.md) _ZN5Botan12Keyed_Filter6set_ivERKNS_11OctetStringE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

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
      "definition_site": "004c53a0",
      "incomplete_value": true,
      "site": "004c53ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5080",
      "incomplete_value": true,
      "site": "004c508c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
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
      "definition_site": "004c539c",
      "incomplete_value": false,
      "site": "004c53ac",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c507c",
      "incomplete_value": false,
      "site": "004c508c",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c539c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c53a0",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004c53a0",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c539c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c53a0",
      "READ",
      [
        "storage",
        "00c9bee0",
        null,
        "pointer"
      ]
    ],
    [
      "004c53a0",
      "PARAM",
      [
        "storage",
        "00c67550",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c508c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md#insn-004c508c) · [`004c502c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md#insn-004c502c) · [`004c5044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md#insn-004c5044)
- 新版 [`004c53ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c52ec.md#insn-004c53ac) · [`004c534c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c52ec.md#insn-004c534c) · [`004c5364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c52ec.md#insn-004c5364)

~~~diff
- 004c508c ["INT_ADD", "register:40f0:8", ["const:4c508c:8", "const:4:8"]]
- 004c508c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c53ac ["INT_ADD", "register:40f0:8", ["const:4c53ac:8", "const:4:8"]]
+ 004c53ac ["CALL", null, ["callee:00c58fb0:8"]]
- 004c508c bytes d54b1e94
+ 004c53ac bytes 014f1e94
- 004c502c ["INT_ADD", "register:40f0:8", ["const:4c502c:8", "const:4:8"]]
- 004c502c ["CALL", null, ["callee:00c58f90:8"]]
+ 004c534c ["INT_ADD", "register:40f0:8", ["const:4c534c:8", "const:4:8"]]
+ 004c534c ["CALL", null, ["callee:00c58f90:8"]]
- 004c502c bytes e54b1e94
+ 004c534c bytes 114f1e94
- 004c5044 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c5044 ["INT_ADD", "register:40f0:8", ["const:4c5044:8", "const:4:8"]]
- 004c5044 ["CALLIND", null, ["register:0:8"]]
+ 004c5364 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c5364 ["INT_ADD", "register:40f0:8", ["const:4c5364:8", "const:4:8"]]
+ 004c5364 ["CALLIND", null, ["register:0:8"]]
- 004c5044 bytes 20013fd6
+ 004c5364 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e90b726b4252932fe9e6c230d22de2"></a>

### [`004c50e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md) → [`004c5400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5400.md) _ZN5Botan5ChainC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5438",
      "incomplete_value": true,
      "site": "004c543c",
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
      "definition_site": "004c5118",
      "incomplete_value": true,
      "site": "004c511c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c5468",
      "incomplete_value": true,
      "site": "004c546c",
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
      "definition_site": "004c5148",
      "incomplete_value": true,
      "site": "004c514c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5420",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c543c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c545c",
      "READ",
      [
        "storage",
        "00c9af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5420",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c543c",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c545c",
      "READ",
      [
        "storage",
        "00c9bf30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c50f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md#insn-004c50f8) · [`004c5100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md#insn-004c5100) · [`004c5134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md#insn-004c5134)
- 新版 [`004c5418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5400.md#insn-004c5418) · [`004c5420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5400.md#insn-004c5420) · [`004c5454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5400.md#insn-004c5454)

~~~diff
- 004c50f8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c5418 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c50f8 bytes a83e00b0
+ 004c5418 bytes a83e00d0
- 004c5100 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c5100 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5420 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c5420 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5100 bytes 08a147f9
+ 004c5420 bytes 088947f9
- 004c5134 ["INT_ADD", "register:40f0:8", ["const:4c5134:8", "const:4:8"]]
- 004c5134 ["CALL", null, ["callee:00543fbc:8"]]
+ 004c5454 ["INT_ADD", "register:40f0:8", ["const:4c5454:8", "const:4:8"]]
+ 004c5454 ["CALL", null, ["callee:00543fbc:8"]]
- 004c5134 bytes dafa0194
+ 004c5454 bytes dafa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f212ca4d4d6d93ab478ea93b1cb32c2"></a>

### [`004c52a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md) → [`004c55c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c55c8.md) _ZN5Botan5ChainC1EPPNS_6FilterEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c55f4",
      "incomplete_value": true,
      "site": "004c55f8",
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
      "definition_site": "004c52d4",
      "incomplete_value": true,
      "site": "004c52d8",
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
      "definition_site": "004c5624",
      "incomplete_value": true,
      "site": "004c5628",
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
      "definition_site": "004c5304",
      "incomplete_value": true,
      "site": "004c5308",
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
      "004c55e4",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c55f8",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5618",
      "READ",
      [
        "storage",
        "00c9af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c55e4",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c55f8",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5618",
      "READ",
      [
        "storage",
        "00c9bf30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c52b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md#insn-004c52b8) · [`004c52c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md#insn-004c52c4) · [`004c52f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md#insn-004c52f0)
- 新版 [`004c55d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c55c8.md#insn-004c55d8) · [`004c55e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c55c8.md#insn-004c55e4) · [`004c5610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c55c8.md#insn-004c5610)

~~~diff
- 004c52b8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c55d8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c52b8 bytes a83e00b0
+ 004c55d8 bytes a83e00d0
- 004c52c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c52c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c55e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c55e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c52c4 bytes 08a147f9
+ 004c55e4 bytes 088947f9
- 004c52f0 ["INT_ADD", "register:40f0:8", ["const:4c52f0:8", "const:4:8"]]
- 004c52f0 ["CALL", null, ["callee:00543fbc:8"]]
+ 004c5610 ["INT_ADD", "register:40f0:8", ["const:4c5610:8", "const:4:8"]]
+ 004c5610 ["CALL", null, ["callee:00543fbc:8"]]
- 004c52f0 bytes 6bfa0194
+ 004c5610 bytes 6bfa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489a42ee91aa5ccfba7578b79e363c74"></a>

### [`004c53c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md) → [`004c56e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c56e8.md) _ZN5Botan4ForkC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00543ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543ddc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`005440fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440fc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5730",
      "incomplete_value": true,
      "site": "004c5738",
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
      "definition_site": "004c5410",
      "incomplete_value": true,
      "site": "004c5418",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5768",
      "incomplete_value": true,
      "site": "004c5770",
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
      "definition_site": "004c5448",
      "incomplete_value": true,
      "site": "004c5450",
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
      "004c5714",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5738",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c575c",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5714",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c5738",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c575c",
      "READ",
      [
        "storage",
        "00c9bf38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c53e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md#insn-004c53e8) · [`004c53f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md#insn-004c53f4) · [`004c5414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md#insn-004c5414)
- 新版 [`004c5708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c56e8.md#insn-004c5708) · [`004c5714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c56e8.md#insn-004c5714)

~~~diff
- 004c53e8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c5708 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c53e8 bytes a93e00b0
+ 004c5708 bytes a93e00d0
- 004c53f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
- 004c53f4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5714 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f10:8"]]
+ 004c5714 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c53f4 bytes 29a147f9
+ 004c5714 bytes 298947f9
- 004c5414 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004c5414 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5911f12bbcccdb0865afcb404966ba45"></a>

### [`004c5520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md) → [`004c5840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5840.md) _ZN5Botan4ForkC1EPPNS_6FilterEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00543ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543ddc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`005440fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c586c",
      "incomplete_value": true,
      "site": "004c5870",
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
      "definition_site": "004c554c",
      "incomplete_value": true,
      "site": "004c5550",
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
      "definition_site": "004c58a0",
      "incomplete_value": true,
      "site": "004c58a8",
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
      "definition_site": "004c5580",
      "incomplete_value": true,
      "site": "004c5588",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c585c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5870",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5890",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c585c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c5870",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5890",
      "READ",
      [
        "storage",
        "00c9bf38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md#insn-004c5530) · [`004c553c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md#insn-004c553c) · [`004c5568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md#insn-004c5568)
- 新版 [`004c5850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5840.md#insn-004c5850) · [`004c585c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5840.md#insn-004c585c) · [`004c5888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5840.md#insn-004c5888)

~~~diff
- 004c5530 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c5850 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c5530 bytes a83e00b0
+ 004c5850 bytes a83e00d0
- 004c553c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c553c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c585c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c585c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c553c bytes 08a147f9
+ 004c585c bytes 088947f9
- 004c5568 ["INT_ADD", "register:40f0:8", ["const:4c5568:8", "const:4:8"]]
- 004c5568 ["CALL", null, ["callee:00543fbc:8"]]
+ 004c5888 ["INT_ADD", "register:40f0:8", ["const:4c5888:8", "const:4:8"]]
+ 004c5888 ["CALL", null, ["callee:00543fbc:8"]]
- 004c5568 bytes cdf90194
+ 004c5888 bytes cdf90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fae0d78d7fc4e9c885474ba74b338dd"></a>

### [`004c5628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md) → [`004c5948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5948.md) _ZN5Botan15Buffered_FilterC2Emm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f70.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c59f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f40.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.36% / 新版 91.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c597c",
      "incomplete_value": true,
      "site": "004c597c",
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
      "definition_site": "004c565c",
      "incomplete_value": true,
      "site": "004c565c",
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
      "definition_site": "004c59e8",
      "incomplete_value": false,
      "site": "004c59f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c56c8",
      "incomplete_value": false,
      "site": "004c56d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:11d:8"
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
      "definition_site": "004c5a20",
      "incomplete_value": true,
      "site": "004c5a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5700",
      "incomplete_value": true,
      "site": "004c570c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "004c5970",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ],
    [
      "004c597c",
      "DATA",
      [
        "storage",
        "00c66978",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c59e8",
      "PARAM",
      [
        "storage",
        "002a411d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c5970",
      "READ",
      [
        "storage",
        "00c9bf40",
        null,
        "pointer"
      ]
    ],
    [
      "004c597c",
      "DATA",
      [
        "storage",
        "00c67948",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c59e8",
      "PARAM",
      [
        "storage",
        "002a41e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c56d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md#insn-004c56d0) · [`004c570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md#insn-004c570c) · [`004c572c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md#insn-004c572c)
- 新版 [`004c59f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5948.md#insn-004c59f0) · [`004c5a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5948.md#insn-004c5a2c) · [`004c5a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5948.md#insn-004c5a4c)

~~~diff
- 004c56d0 ["INT_ADD", "register:40f0:8", ["const:4c56d0:8", "const:4:8"]]
- 004c56d0 ["CALL", null, ["callee:0043e138:8"]]
+ 004c59f0 ["INT_ADD", "register:40f0:8", ["const:4c59f0:8", "const:4:8"]]
+ 004c59f0 ["CALL", null, ["callee:0043e138:8"]]
- 004c56d0 bytes d2e1fd97
+ 004c59f0 bytes d2e1fd97
- 004c570c ["INT_ADD", "register:40f0:8", ["const:4c570c:8", "const:4:8"]]
- 004c570c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c5a2c ["INT_ADD", "register:40f0:8", ["const:4c5a2c:8", "const:4:8"]]
+ 004c5a2c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c570c bytes 354a1e94
+ 004c5a2c bytes 614d1e94
- 004c572c ["INT_ADD", "register:40f0:8", ["const:4c572c:8", "const:4:8"]]
- 004c572c ["CALL", null, ["callee:0043e138:8"]]
+ 004c5a4c ["INT_ADD", "register:40f0:8", ["const:4c5a4c:8", "const:4:8"]]
+ 004c5a4c ["CALL", null, ["callee:0043e138:8"]]
- 004c572c bytes bbe1fd97
+ 004c5a4c bytes bbe1fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-696f605017f58540969437f1e875fb21"></a>

### [`004c5914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md) → [`004c5c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5c34.md) _ZN5Botan15Buffered_Filter7end_msgEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f90.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c59f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59f60.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c5cfc",
      "incomplete_value": false,
      "site": "004c5d04",
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
            "const:1ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c59dc",
      "incomplete_value": false,
      "site": "004c59e4",
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
            "const:ef:8"
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
      "definition_site": "004c5d34",
      "incomplete_value": true,
      "site": "004c5d40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5a14",
      "incomplete_value": true,
      "site": "004c5a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "definition_site": "004c5d30",
      "incomplete_value": false,
      "site": "004c5d40",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c5a10",
      "incomplete_value": false,
      "site": "004c5a20",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c5cfc",
      "PARAM",
      [
        "storage",
        "002a30ef",
        null,
        "string"
      ]
    ],
    [
      "004c5d30",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c5d34",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5cfc",
      "PARAM",
      [
        "storage",
        "002a31ba",
        null,
        "string"
      ]
    ],
    [
      "004c5d30",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c5d34",
      "READ",
      [
        "storage",
        "00c9be28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c59e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md#insn-004c59e4) · [`004c5a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md#insn-004c5a20) · [`004c5980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md#insn-004c5980)
- 新版 [`004c5d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5c34.md#insn-004c5d04) · [`004c5d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5c34.md#insn-004c5d40) · [`004c5ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5c34.md#insn-004c5ca0)

~~~diff
- 004c59e4 ["INT_ADD", "register:40f0:8", ["const:4c59e4:8", "const:4:8"]]
- 004c59e4 ["CALL", null, ["callee:0043e138:8"]]
+ 004c5d04 ["INT_ADD", "register:40f0:8", ["const:4c5d04:8", "const:4:8"]]
+ 004c5d04 ["CALL", null, ["callee:0043e138:8"]]
- 004c59e4 bytes 0de1fd97
+ 004c5d04 bytes 0de1fd97
- 004c5a20 ["INT_ADD", "register:40f0:8", ["const:4c5a20:8", "const:4:8"]]
- 004c5a20 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c5d40 ["INT_ADD", "register:40f0:8", ["const:4c5d40:8", "const:4:8"]]
+ 004c5d40 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c5a20 bytes 70491e94
+ 004c5d40 bytes 9c4c1e94
- 004c5980 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c5980 ["INT_ADD", "register:40f0:8", ["const:4c5980:8", "const:4:8"]]
- 004c5980 ["CALLIND", null, ["register:0:8"]]
+ 004c5ca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5ca0 ["INT_ADD", "register:40f0:8", ["const:4c5ca0:8", "const:4:8"]]
+ 004c5ca0 ["CALLIND", null, ["register:0:8"]]
- 004c5980 bytes 00013fd6
+ 004c5ca0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad220e36dc54da1a306b50dcf7629e18"></a>

### [`004c5a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md) → [`004c5d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5d90.md) _ZN5Botan18Cipher_Mode_FilterC1EPNS_11Cipher_ModeE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59060.md) · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c5a030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a030.md) · 呼出先 7件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5db8",
      "incomplete_value": true,
      "site": "004c5dbc",
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
      "definition_site": "004c5a98",
      "incomplete_value": true,
      "site": "004c5a9c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5de8",
      "incomplete_value": true,
      "site": "004c5dec",
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
      "definition_site": "004c5ac8",
      "incomplete_value": true,
      "site": "004c5acc",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5e5c",
      "incomplete_value": true,
      "site": "004c5e64",
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
      "definition_site": "004c5b3c",
      "incomplete_value": true,
      "site": "004c5b44",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5dac",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5dbc",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5ddc",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5dac",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c5dbc",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5ddc",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md#insn-004c5bec) · [`004c5a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md#insn-004c5a84) · [`004c5a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md#insn-004c5a8c)
- 新版 [`004c5f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5d90.md#insn-004c5f0c) · [`004c5da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5d90.md#insn-004c5da4) · [`004c5dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c5/004c5d90.md#insn-004c5dac)

~~~diff
- 004c5bec ["INT_ADD", "register:40f0:8", ["const:4c5bec:8", "const:4:8"]]
- 004c5bec ["CALL", null, ["callee:00c596f0:8"]]
+ 004c5f0c ["INT_ADD", "register:40f0:8", ["const:4c5f0c:8", "const:4:8"]]
+ 004c5f0c ["CALL", null, ["callee:00c596f0:8"]]
- 004c5bec bytes cd4a1e94
+ 004c5f0c bytes f94d1e94
- 004c5a84 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c5da4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c5a84 bytes a83e00b0
+ 004c5da4 bytes a83e00d0
- 004c5a8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c5a8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5dac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c5dac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5a8c bytes 08a147f9
+ 004c5dac bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd9c0c3957a2b99fc8e9a38c01dff72"></a>

### [`004c5e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md) → [`004c6158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6158.md) _ZN5Botan18Cipher_Mode_Filter9start_msgEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.39% / 新版 96.39%

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
      "definition_site": "004c6210",
      "incomplete_value": false,
      "site": "004c621c",
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
            "const:3df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5ef0",
      "incomplete_value": false,
      "site": "004c5efc",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c623c",
      "incomplete_value": false,
      "site": "004c6244",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5f1c",
      "incomplete_value": false,
      "site": "004c5f24",
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
            "const:6d0:8"
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
      "definition_site": "004c6290",
      "incomplete_value": true,
      "site": "004c629c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5f70",
      "incomplete_value": true,
      "site": "004c5f7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "004c6210",
      "PARAM",
      [
        "storage",
        "002b7310",
        null,
        "string"
      ]
    ],
    [
      "004c623c",
      "PARAM",
      [
        "storage",
        "002ac6d0",
        null,
        "string"
      ]
    ],
    [
      "004c628c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c6210",
      "PARAM",
      [
        "storage",
        "002b73df",
        null,
        "string"
      ]
    ],
    [
      "004c623c",
      "PARAM",
      [
        "storage",
        "002ac79d",
        null,
        "string"
      ]
    ],
    [
      "004c628c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md#insn-004c5efc) · [`004c5f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md#insn-004c5f24) · [`004c5f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md#insn-004c5f7c)
- 新版 [`004c621c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6158.md#insn-004c621c) · [`004c6244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6158.md#insn-004c6244) · [`004c629c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6158.md#insn-004c629c)

~~~diff
- 004c5efc ["INT_ADD", "register:40f0:8", ["const:4c5efc:8", "const:4:8"]]
- 004c5efc ["CALL", null, ["callee:00c59000:8"]]
+ 004c621c ["INT_ADD", "register:40f0:8", ["const:4c621c:8", "const:4:8"]]
+ 004c621c ["CALL", null, ["callee:00c59000:8"]]
- 004c5efc bytes 4d481e94
+ 004c621c bytes 794b1e94
- 004c5f24 ["INT_ADD", "register:40f0:8", ["const:4c5f24:8", "const:4:8"]]
- 004c5f24 ["CALL", null, ["callee:00c59010:8"]]
+ 004c6244 ["INT_ADD", "register:40f0:8", ["const:4c6244:8", "const:4:8"]]
+ 004c6244 ["CALL", null, ["callee:00c59010:8"]]
- 004c5f24 bytes 47481e94
+ 004c6244 bytes 734b1e94
- 004c5f7c ["INT_ADD", "register:40f0:8", ["const:4c5f7c:8", "const:4:8"]]
- 004c5f7c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c629c ["INT_ADD", "register:40f0:8", ["const:4c629c:8", "const:4:8"]]
+ 004c629c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c5f7c bytes 19481e94
+ 004c629c bytes 454b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-028fad73b29ae2729bc13f1bb6323cea"></a>

### [`004c61f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md) → [`004c6514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6514.md) _ZN5Botan15DataSink_Stream5writeEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6590",
      "incomplete_value": false,
      "site": "004c659c",
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
            "const:3e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6270",
      "incomplete_value": false,
      "site": "004c627c",
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
            "const:318:8"
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
      "definition_site": "004c65d0",
      "incomplete_value": true,
      "site": "004c65dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c62b0",
      "incomplete_value": true,
      "site": "004c62bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
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
      "definition_site": "004c65cc",
      "incomplete_value": false,
      "site": "004c65dc",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c62ac",
      "incomplete_value": false,
      "site": "004c62bc",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c6590",
      "PARAM",
      [
        "storage",
        "002b7318",
        null,
        "string"
      ]
    ],
    [
      "004c65cc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c65d0",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c6590",
      "PARAM",
      [
        "storage",
        "002b73e7",
        null,
        "string"
      ]
    ],
    [
      "004c65cc",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c65d0",
      "READ",
      [
        "storage",
        "00c9be20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c627c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md#insn-004c627c) · [`004c62bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md#insn-004c62bc) · [`004c621c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md#insn-004c621c)
- 新版 [`004c659c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6514.md#insn-004c659c) · [`004c65dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6514.md#insn-004c65dc) · [`004c653c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6514.md#insn-004c653c)

~~~diff
- 004c627c ["INT_ADD", "register:40f0:8", ["const:4c627c:8", "const:4:8"]]
- 004c627c ["CALL", null, ["callee:00c59150:8"]]
+ 004c659c ["INT_ADD", "register:40f0:8", ["const:4c659c:8", "const:4:8"]]
+ 004c659c ["CALL", null, ["callee:00c59150:8"]]
- 004c627c bytes c1471e94
+ 004c659c bytes ed4a1e94
- 004c62bc ["INT_ADD", "register:40f0:8", ["const:4c62bc:8", "const:4:8"]]
- 004c62bc ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c65dc ["INT_ADD", "register:40f0:8", ["const:4c65dc:8", "const:4:8"]]
+ 004c65dc ["CALL", null, ["callee:00c58fb0:8"]]
- 004c62bc bytes 49471e94
+ 004c65dc bytes 754a1e94
- 004c621c ["INT_ADD", "register:40f0:8", ["const:4c621c:8", "const:4:8"]]
- 004c621c ["CALL", null, ["callee:00c59d10:8"]]
+ 004c653c ["INT_ADD", "register:40f0:8", ["const:4c653c:8", "const:4:8"]]
+ 004c653c ["CALL", null, ["callee:00c59d10:8"]]
- 004c621c bytes c94a1e94
+ 004c653c bytes f54d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2765c537b539cf4129775b6137e7d4b3"></a>

### [`004c6318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md) → [`004c6638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6638.md) _ZN5Botan15DataSink_StreamC2ERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6664",
      "incomplete_value": true,
      "site": "004c6668",
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
      "definition_site": "004c6344",
      "incomplete_value": true,
      "site": "004c6348",
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
      "definition_site": "004c6694",
      "incomplete_value": true,
      "site": "004c6698",
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
      "definition_site": "004c6374",
      "incomplete_value": true,
      "site": "004c6378",
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
      "004c6654",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c6668",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6688",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c6654",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c6668",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6688",
      "READ",
      [
        "storage",
        "00c9bf58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md#insn-004c6328) · [`004c6334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md#insn-004c6334) · [`004c6360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md#insn-004c6360)
- 新版 [`004c6648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6638.md#insn-004c6648) · [`004c6654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6638.md#insn-004c6654) · [`004c6680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6638.md#insn-004c6680)

~~~diff
- 004c6328 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c6648 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c6328 bytes a83e0090
+ 004c6648 bytes a83e00b0
- 004c6334 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 004c6334 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 004c6654 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c6334 bytes 08a147f9
+ 004c6654 bytes 088947f9
- 004c6360 ["INT_ADD", "register:40f0:8", ["const:4c6360:8", "const:4:8"]]
- 004c6360 ["CALL", null, ["callee:00543fbc:8"]]
+ 004c6680 ["INT_ADD", "register:40f0:8", ["const:4c6680:8", "const:4:8"]]
+ 004c6680 ["CALL", null, ["callee:00543fbc:8"]]
- 004c6360 bytes 4ff60194
+ 004c6680 bytes 4ff60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f162b3bda61764e1367e2995d58cf7d"></a>

### [`004c63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md) → [`004c6714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6714.md) _ZN5Botan15DataSink_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004c6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004c6934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6934.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6750",
      "incomplete_value": true,
      "site": "004c6758",
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
      "definition_site": "004c6430",
      "incomplete_value": true,
      "site": "004c6438",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c6784",
      "incomplete_value": true,
      "site": "004c6788",
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
      "definition_site": "004c6464",
      "incomplete_value": true,
      "site": "004c6468",
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6828",
      "incomplete_value": false,
      "site": "004c6834",
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
            "const:bb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6508",
      "incomplete_value": false,
      "site": "004c6514",
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
            "const:ae0:8"
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
      "004c673c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c6758",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6778",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c673c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c6758",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6778",
      "READ",
      [
        "storage",
        "00c9bf58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md#insn-004c6514) · [`004c6550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md#insn-004c6550) · [`004c6410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md#insn-004c6410)
- 新版 [`004c6834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6714.md#insn-004c6834) · [`004c6870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6714.md#insn-004c6870) · [`004c6730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6714.md#insn-004c6730)

~~~diff
- 004c6514 ["INT_ADD", "register:40f0:8", ["const:4c6514:8", "const:4:8"]]
- 004c6514 ["CALL", null, ["callee:00c59150:8"]]
+ 004c6834 ["INT_ADD", "register:40f0:8", ["const:4c6834:8", "const:4:8"]]
+ 004c6834 ["CALL", null, ["callee:00c59150:8"]]
- 004c6514 bytes 1b471e94
+ 004c6834 bytes 474a1e94
- 004c6550 ["INT_ADD", "register:40f0:8", ["const:4c6550:8", "const:4:8"]]
- 004c6550 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c6870 ["INT_ADD", "register:40f0:8", ["const:4c6870:8", "const:4:8"]]
+ 004c6870 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c6550 bytes a4461e94
+ 004c6870 bytes d0491e94
- 004c6410 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004c6730 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004c6410 bytes a93e0090
+ 004c6730 bytes a93e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95111a015a47a9e6acdf72aeb20407a1"></a>

### [`004c6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md) → [`004c6934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6934.md) FUN_004c6934

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md) · 呼出先 4件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fd0.md) [`00c58fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fe0.md)
- 新版 呼出元 1件 [`004c6714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6714.md) · 呼出先 4件 [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fa0.md) [`00c59fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fb0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.45% / 新版 85.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6978",
      "incomplete_value": true,
      "site": "004c6978",
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
      "definition_site": "004c6658",
      "incomplete_value": true,
      "site": "004c6658",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6970",
      "incomplete_value": true,
      "site": "004c697c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004c6650",
      "incomplete_value": true,
      "site": "004c665c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004c6984",
      "incomplete_value": true,
      "site": "004c6984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "004c6664",
      "incomplete_value": true,
      "site": "004c6664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "004c6958",
      "READ",
      [
        "storage",
        "00c9af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c695c",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "004c6970",
      "READ",
      [
        "storage",
        "00c931a0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004c6958",
      "READ",
      [
        "storage",
        "00c9bf60",
        null,
        "pointer"
      ]
    ],
    [
      "004c695c",
      "READ",
      [
        "storage",
        "00c9bf68",
        null,
        "pointer"
      ]
    ],
    [
      "004c6970",
      "READ",
      [
        "storage",
        "00c94170",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c662c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md#insn-004c662c) · [`004c6630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md#insn-004c6630) · [`004c6638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md#insn-004c6638)
- 新版 [`004c694c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6934.md#insn-004c694c) · [`004c6950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6934.md#insn-004c6950) · [`004c6958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6934.md#insn-004c6958)

~~~diff
- 004c662c ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 004c694c ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 004c662c bytes b93e0090
+ 004c694c bytes b93e00b0
- 004c6630 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 004c6950 ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 004c6630 bytes b83e0090
+ 004c6950 bytes b83e00b0
- 004c6638 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:f90:8"]]
- 004c6638 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6958 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:f60:8"]]
+ 004c6958 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004c6638 bytes 39cb47f9
+ 004c6958 bytes 39b347f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc961509b85d303b04a81632e057a309"></a>

### [`004c6a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md) → [`004c6d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6d64.md) _ZN5Botan6Filter8set_portEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6dd0",
      "incomplete_value": false,
      "site": "004c6dd8",
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
            "const:107:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6ab0",
      "incomplete_value": false,
      "site": "004c6ab8",
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
            "const:bd:8"
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
      "definition_site": "004c6e0c",
      "incomplete_value": true,
      "site": "004c6e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6aec",
      "incomplete_value": true,
      "site": "004c6af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
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
      "definition_site": "004c6e08",
      "incomplete_value": false,
      "site": "004c6e18",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c6ae8",
      "incomplete_value": false,
      "site": "004c6af8",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c6dd0",
      "PARAM",
      [
        "storage",
        "002c10bd",
        null,
        "string"
      ]
    ],
    [
      "004c6e08",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c6e0c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c6dd0",
      "PARAM",
      [
        "storage",
        "002c1107",
        null,
        "string"
      ]
    ],
    [
      "004c6e08",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c6e0c",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md#insn-004c6ab8) · [`004c6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md#insn-004c6af8) · [`004c6aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md#insn-004c6aa4)
- 新版 [`004c6dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6d64.md#insn-004c6dd8) · [`004c6e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6d64.md#insn-004c6e18) · [`004c6dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6d64.md#insn-004c6dc4)

~~~diff
- 004c6ab8 ["INT_ADD", "register:40f0:8", ["const:4c6ab8:8", "const:4:8"]]
- 004c6ab8 ["CALL", null, ["callee:0043e138:8"]]
+ 004c6dd8 ["INT_ADD", "register:40f0:8", ["const:4c6dd8:8", "const:4:8"]]
+ 004c6dd8 ["CALL", null, ["callee:0043e138:8"]]
- 004c6ab8 bytes d8dcfd97
+ 004c6dd8 bytes d8dcfd97
- 004c6af8 ["INT_ADD", "register:40f0:8", ["const:4c6af8:8", "const:4:8"]]
- 004c6af8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c6e18 ["INT_ADD", "register:40f0:8", ["const:4c6e18:8", "const:4:8"]]
+ 004c6e18 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c6af8 bytes 3a451e94
+ 004c6e18 bytes 66481e94
- 004c6aa4 ["INT_ADD", "register:40f0:8", ["const:4c6aa4:8", "const:4:8"]]
- 004c6aa4 ["CALL", null, ["callee:00c58f90:8"]]
+ 004c6dc4 ["INT_ADD", "register:40f0:8", ["const:4c6dc4:8", "const:4:8"]]
+ 004c6dc4 ["CALL", null, ["callee:00c58f90:8"]]
- 004c6aa4 bytes 47451e94
+ 004c6dc4 bytes 73481e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33b711d64aa2fde24983e8368f500d01"></a>

### [`004c6b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md) → [`004c6ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ea4.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59040.md) · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5a010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a010.md) · 呼出先 8件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

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
      "definition_site": "004c6f48",
      "incomplete_value": true,
      "site": "004c6f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6c28",
      "incomplete_value": true,
      "site": "004c6c30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
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
      "definition_site": "004c6f44",
      "incomplete_value": false,
      "site": "004c6f50",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c6c24",
      "incomplete_value": false,
      "site": "004c6c30",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c6f44",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c6f48",
      "READ",
      [
        "storage",
        "00c9afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6f48",
      "PARAM",
      [
        "storage",
        "00c66ae8",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c6f44",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c6f48",
      "READ",
      [
        "storage",
        "00c9bf70",
        null,
        "pointer"
      ]
    ],
    [
      "004c6f48",
      "PARAM",
      [
        "storage",
        "00c67ab8",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md#insn-004c6c30) · [`004c6bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md#insn-004c6bb0) · [`004c6bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md#insn-004c6bc0)
- 新版 [`004c6f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ea4.md#insn-004c6f50) · [`004c6ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ea4.md#insn-004c6ed0) · [`004c6ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6ea4.md#insn-004c6ee0)

~~~diff
- 004c6c30 ["INT_ADD", "register:40f0:8", ["const:4c6c30:8", "const:4:8"]]
- 004c6c30 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c6f50 ["INT_ADD", "register:40f0:8", ["const:4c6f50:8", "const:4:8"]]
+ 004c6f50 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c6c30 bytes ec441e94
+ 004c6f50 bytes 18481e94
- 004c6bb0 ["INT_ADD", "register:40f0:8", ["const:4c6bb0:8", "const:4:8"]]
- 004c6bb0 ["CALL", null, ["callee:00c5a020:8"]]
+ 004c6ed0 ["INT_ADD", "register:40f0:8", ["const:4c6ed0:8", "const:4:8"]]
+ 004c6ed0 ["CALL", null, ["callee:00c5a020:8"]]
- 004c6bb0 bytes 28491e94
+ 004c6ed0 bytes 544c1e94
- 004c6bc0 ["INT_ADD", "register:40f0:8", ["const:4c6bc0:8", "const:4:8"]]
- 004c6bc0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c6ee0 ["INT_ADD", "register:40f0:8", ["const:4c6ee0:8", "const:4:8"]]
+ 004c6ee0 ["CALL", null, ["callee:00c58f30:8"]]
- 004c6bc0 bytes e8441e94
+ 004c6ee0 bytes 14481e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c831973a005fe04ae03ed7e866a14b89"></a>

### [`004c6c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md) → [`004c6fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6fa8.md) _ZN5Botan15get_cipher_modeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirES8_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59050.md) · 呼出先 27件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`004d1b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1b64.md) [`004d1bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1bfc.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md)
- 新版 呼出元 1件 [`00c5a020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a020.md) · 呼出先 27件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`004d1e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d1/004d1e84.md) [`004d1f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d1/004d1f1c.md) [`00547ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ecc.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c7008",
      "incomplete_value": true,
      "site": "004c7008",
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
      "definition_site": "004c6ce8",
      "incomplete_value": true,
      "site": "004c6ce8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c7064",
      "incomplete_value": false,
      "site": "004c7070",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6d44",
      "incomplete_value": false,
      "site": "004c6d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "004c7134",
      "incomplete_value": true,
      "site": "004c7138",
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
      "definition_site": "004c6e14",
      "incomplete_value": true,
      "site": "004c6e18",
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
      "004c7000",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004c7008",
      "DATA",
      [
        "storage",
        "00c69e30",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c7070",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c7000",
      "READ",
      [
        "storage",
        "00c9bf78",
        null,
        "pointer"
      ]
    ],
    [
      "004c7008",
      "DATA",
      [
        "storage",
        "00c6ae00",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c7070",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md#insn-004c6cc4) · [`004c6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md#insn-004c6cd4) · [`004c6cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md#insn-004c6cd8)
- 新版 [`004c6fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6fa8.md#insn-004c6fe4) · [`004c6ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6fa8.md#insn-004c6ff4) · [`004c6ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6fa8.md#insn-004c6ff8)

~~~diff
- 004c6cc4 ["INT_ADD", "register:40f0:8", ["const:4c6cc4:8", "const:4:8"]]
- 004c6cc4 ["CALL", null, ["callee:00c59f00:8"]]
+ 004c6fe4 ["INT_ADD", "register:40f0:8", ["const:4c6fe4:8", "const:4:8"]]
+ 004c6fe4 ["CALL", null, ["callee:00c59f00:8"]]
- 004c6cc4 bytes 9b481e94
+ 004c6fe4 bytes c74b1e94
- 004c6cd4 ["INT_ADD", "register:40f0:8", ["const:4c6cd4:8", "const:4:8"]]
- 004c6cd4 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c6ff4 ["INT_ADD", "register:40f0:8", ["const:4c6ff4:8", "const:4:8"]]
+ 004c6ff4 ["CALL", null, ["callee:00c58f30:8"]]
- 004c6cd4 bytes a3441e94
+ 004c6ff4 bytes cf471e94
- 004c6cd8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c6ff8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c6cd8 bytes a83e0090
+ 004c6ff8 bytes a83e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f16816c257e106eee69c03f42450f1ff"></a>

### [`004c788c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md) → [`004c7bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7bac.md) _ZN5Botan11SecureQueue4readEPhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c590c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590c0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c5a090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a090.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c7c80",
      "incomplete_value": true,
      "site": "004c7c80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7960",
      "incomplete_value": true,
      "site": "004c7960",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
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
      "004c7c70",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c7c70",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md#insn-004c7960) · [`004c78c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md#insn-004c78c0) · [`004c7910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md#insn-004c7910)
- 新版 [`004c7c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7bac.md#insn-004c7c80) · [`004c7be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7bac.md#insn-004c7be0) · [`004c7c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7bac.md#insn-004c7c30)

~~~diff
- 004c7960 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c7960 ["INT_ADD", "register:40f0:8", ["const:4c7960:8", "const:4:8"]]
- 004c7960 ["CALLIND", null, ["register:0:8"]]
+ 004c7c80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c7c80 ["INT_ADD", "register:40f0:8", ["const:4c7c80:8", "const:4:8"]]
+ 004c7c80 ["CALLIND", null, ["register:0:8"]]
- 004c7960 bytes 20013fd6
+ 004c7c80 bytes 20013fd6
- 004c78c0 ["COPY", "register:40d0:8", ["const:c67000:8"]]
+ 004c7be0 ["COPY", "register:40d0:8", ["const:c68000:8"]]
- 004c78c0 bytes 1a3d0090
+ 004c7be0 bytes 1a3d00b0
- 004c7910 ["INT_ADD", "register:40f0:8", ["const:4c7910:8", "const:4:8"]]
- 004c7910 ["CALL", null, ["callee:00c58fe0:8"]]
+ 004c7c30 ["INT_ADD", "register:40f0:8", ["const:4c7c30:8", "const:4:8"]]
+ 004c7c30 ["CALL", null, ["callee:00c58fe0:8"]]
- 004c7910 bytes c0411e94
+ 004c7c30 bytes ec441e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5ca6db42fa48ff9044d808229a1edc9"></a>

### [`004c7b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md) → [`004c7e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7e28.md) FUN_004c7e28

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c8c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8c58.md) · 呼出先 3件 [`00543f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543f0c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`004c8f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8f78.md) · 呼出先 3件 [`0054422c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/0054422c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7f00",
      "incomplete_value": false,
      "site": "004c7f20",
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
            "const:ca4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7be0",
      "incomplete_value": false,
      "site": "004c7c00",
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
            "const:bd7:8"
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
      "definition_site": "004c7f08",
      "incomplete_value": false,
      "site": "004c7f20",
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
            "const:caa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7be8",
      "incomplete_value": false,
      "site": "004c7c00",
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
            "const:bdd:8"
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
      "definition_site": "004c7f10",
      "incomplete_value": false,
      "site": "004c7f20",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7bf0",
      "incomplete_value": false,
      "site": "004c7c00",
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
            "const:580:8"
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
      "004c7f00",
      "PARAM",
      [
        "storage",
        "002a9bd7",
        null,
        "string"
      ]
    ],
    [
      "004c7f08",
      "PARAM",
      [
        "storage",
        "002a9bdd",
        null,
        "string"
      ]
    ],
    [
      "004c7f10",
      "PARAM",
      [
        "storage",
        "002a6580",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c7f00",
      "PARAM",
      [
        "storage",
        "002a9ca4",
        null,
        "string"
      ]
    ],
    [
      "004c7f08",
      "PARAM",
      [
        "storage",
        "002a9caa",
        null,
        "string"
      ]
    ],
    [
      "004c7f10",
      "PARAM",
      [
        "storage",
        "002a66d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md#insn-004c7c00) · [`004c7c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md#insn-004c7c38) · [`004c7b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md#insn-004c7b7c)
- 新版 [`004c7f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7e28.md#insn-004c7f20) · [`004c7f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7e28.md#insn-004c7f58) · [`004c7e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7e28.md#insn-004c7e9c)

~~~diff
- 004c7c00 ["INT_ADD", "register:40f0:8", ["const:4c7c00:8", "const:4:8"]]
- 004c7c00 ["CALL", null, ["callee:00c596f0:8"]]
+ 004c7f20 ["INT_ADD", "register:40f0:8", ["const:4c7f20:8", "const:4:8"]]
+ 004c7f20 ["CALL", null, ["callee:00c596f0:8"]]
- 004c7c00 bytes c8421e94
+ 004c7f20 bytes f4451e94
- 004c7c38 ["INT_ADD", "register:40f0:8", ["const:4c7c38:8", "const:4:8"]]
- 004c7c38 ["CALL", null, ["callee:00c596f0:8"]]
+ 004c7f58 ["INT_ADD", "register:40f0:8", ["const:4c7f58:8", "const:4:8"]]
+ 004c7f58 ["CALL", null, ["callee:00c596f0:8"]]
- 004c7c38 bytes ba421e94
+ 004c7f58 bytes e6451e94
- 004c7b7c ["INT_ADD", "register:40f0:8", ["const:4c7b7c:8", "const:4:8"]]
- 004c7b7c ["CALL", null, ["callee:0054422c:8"]]
+ 004c7e9c ["INT_ADD", "register:40f0:8", ["const:4c7e9c:8", "const:4:8"]]
+ 004c7e9c ["CALL", null, ["callee:0054422c:8"]]
- 004c7b7c bytes e4f00194
+ 004c7e9c bytes e4f00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580ac504f2682fb7242b6c0e975bdd91"></a>

### [`004c7db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md) → [`004c80d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c80d8.md) _ZN5Botan4PipeC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c590e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5a0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0b0.md)

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
      "definition_site": "004c810c",
      "incomplete_value": true,
      "site": "004c8114",
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
      "definition_site": "004c7dec",
      "incomplete_value": true,
      "site": "004c7df4",
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
      "004c80f8",
      "READ",
      [
        "storage",
        "00c9afd0",
        null,
        "pointer"
      ]
    ],
    [
      "004c8114",
      "DATA",
      [
        "storage",
        "00c66b10",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c80f8",
      "READ",
      [
        "storage",
        "00c9bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "004c8114",
      "DATA",
      [
        "storage",
        "00c67ae0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md#insn-004c7dcc) · [`004c7dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md#insn-004c7dd8) · [`004c7dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md#insn-004c7dfc)
- 新版 [`004c80ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c80d8.md#insn-004c80ec) · [`004c80f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c80d8.md#insn-004c80f8) · [`004c811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c80d8.md#insn-004c811c)

~~~diff
- 004c7dcc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c80ec ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c7dcc bytes 883e00f0
+ 004c80ec bytes 883e00f0
- 004c7dd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
- 004c7dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c80f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004c80f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7dd8 bytes 08e947f9
+ 004c80f8 bytes 08d147f9
- 004c7dfc ["INT_ADD", "register:40f0:8", ["const:4c7dfc:8", "const:4:8"]]
- 004c7dfc ["CALL", null, ["callee:00c58f30:8"]]
+ 004c811c ["INT_ADD", "register:40f0:8", ["const:4c811c:8", "const:4:8"]]
+ 004c811c ["CALL", null, ["callee:00c58f30:8"]]
- 004c7dfc bytes 59401e94
+ 004c811c bytes 85431e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b463e765d1d8f11bfa91f179e01ebd"></a>

### [`004c7e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md) → [`004c8198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8198.md) _ZN5Botan4PipeC2ESt16initializer_listIPNS_6FilterEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c590e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5a0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0b0.md)

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
      "definition_site": "004c81c4",
      "incomplete_value": true,
      "site": "004c81c8",
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
      "definition_site": "004c7ea4",
      "incomplete_value": true,
      "site": "004c7ea8",
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
      "004c81b4",
      "READ",
      [
        "storage",
        "00c9afd0",
        null,
        "pointer"
      ]
    ],
    [
      "004c81c8",
      "DATA",
      [
        "storage",
        "00c66b10",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c81b4",
      "READ",
      [
        "storage",
        "00c9bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "004c81c8",
      "DATA",
      [
        "storage",
        "00c67ae0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md#insn-004c7e88) · [`004c7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md#insn-004c7e94) · [`004c7eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md#insn-004c7eb0)
- 新版 [`004c81a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8198.md#insn-004c81a8) · [`004c81b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8198.md#insn-004c81b4) · [`004c81d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8198.md#insn-004c81d0)

~~~diff
- 004c7e88 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c81a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c7e88 bytes 883e00f0
+ 004c81a8 bytes 883e00f0
- 004c7e94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
- 004c7e94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c81b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 004c81b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7e94 bytes 08e947f9
+ 004c81b4 bytes 08d147f9
- 004c7eb0 ["INT_ADD", "register:40f0:8", ["const:4c7eb0:8", "const:4:8"]]
- 004c7eb0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c81d0 ["INT_ADD", "register:40f0:8", ["const:4c81d0:8", "const:4:8"]]
+ 004c81d0 ["CALL", null, ["callee:00c58f30:8"]]
- 004c7eb0 bytes 2c401e94
+ 004c81d0 bytes 58431e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-609251596275f6fc3b3227e69f7770a3"></a>

### [`004c7f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md) → [`004c8238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8238.md) _ZN5Botan4Pipe9do_appendEPNS_6FilterE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c590e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590e0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5a0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0b0.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c826c",
      "incomplete_value": true,
      "site": "004c8270",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004c7f4c",
      "incomplete_value": true,
      "site": "004c7f50",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004c8304",
      "incomplete_value": false,
      "site": "004c830c",
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
            "const:b1b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7fe4",
      "incomplete_value": false,
      "site": "004c7fec",
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
            "const:ad1:8"
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
      "definition_site": "004c8340",
      "incomplete_value": true,
      "site": "004c834c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8020",
      "incomplete_value": true,
      "site": "004c802c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "004c8260",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8304",
      "PARAM",
      [
        "storage",
        "002b2ad1",
        null,
        "string"
      ]
    ],
    [
      "004c833c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c8260",
      "READ",
      [
        "storage",
        "00c9bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8304",
      "PARAM",
      [
        "storage",
        "002b2b1b",
        null,
        "string"
      ]
    ],
    [
      "004c833c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md#insn-004c7fec) · [`004c802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md#insn-004c802c) · [`004c8050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md#insn-004c8050)
- 新版 [`004c830c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8238.md#insn-004c830c) · [`004c834c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8238.md#insn-004c834c) · [`004c8370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8238.md#insn-004c8370)

~~~diff
- 004c7fec ["INT_ADD", "register:40f0:8", ["const:4c7fec:8", "const:4:8"]]
- 004c7fec ["CALL", null, ["callee:0043e138:8"]]
+ 004c830c ["INT_ADD", "register:40f0:8", ["const:4c830c:8", "const:4:8"]]
+ 004c830c ["CALL", null, ["callee:0043e138:8"]]
- 004c7fec bytes 8bd7fd97
+ 004c830c bytes 8bd7fd97
- 004c802c ["INT_ADD", "register:40f0:8", ["const:4c802c:8", "const:4:8"]]
- 004c802c ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c834c ["INT_ADD", "register:40f0:8", ["const:4c834c:8", "const:4:8"]]
+ 004c834c ["CALL", null, ["callee:00c58fb0:8"]]
- 004c802c bytes ed3f1e94
+ 004c834c bytes 19431e94
- 004c8050 ["INT_ADD", "register:40f0:8", ["const:4c8050:8", "const:4:8"]]
- 004c8050 ["CALL", null, ["callee:0043e138:8"]]
+ 004c8370 ["INT_ADD", "register:40f0:8", ["const:4c8370:8", "const:4:8"]]
+ 004c8370 ["CALL", null, ["callee:0043e138:8"]]
- 004c8050 bytes 72d7fd97
+ 004c8370 bytes 72d7fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d03a150f66cb3f602e48e44dc53bc66a"></a>

### [`004c81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md) → [`004c84f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84f8.md) _ZN5Botan4Pipe8destructEPNS_6FilterE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md)
- 新版 呼出元 1件 [`00c5a0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0c0.md) · 呼出先 1件 [`00c5a0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0c0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c8520",
      "incomplete_value": true,
      "site": "004c8524",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004c8200",
      "incomplete_value": true,
      "site": "004c8204",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "004c8514",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8514",
      "READ",
      [
        "storage",
        "00c9bfa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c81ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md#insn-004c81ec) · [`004c81f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md#insn-004c81f4) · [`004c8224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md#insn-004c8224)
- 新版 [`004c850c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84f8.md#insn-004c850c) · [`004c8514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84f8.md#insn-004c8514) · [`004c8544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c84f8.md#insn-004c8544)

~~~diff
- 004c81ec ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004c850c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004c81ec bytes 883e00d0
+ 004c850c bytes 883e00f0
- 004c81f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
- 004c81f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 004c8514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c81f4 bytes 08ed47f9
+ 004c8514 bytes 08d547f9
- 004c8224 ["INT_ADD", "register:40f0:8", ["const:4c8224:8", "const:4:8"]]
- 004c8224 ["CALL", null, ["callee:00c5a0c0:8"]]
+ 004c8544 ["INT_ADD", "register:40f0:8", ["const:4c8544:8", "const:4:8"]]
+ 004c8544 ["CALL", null, ["callee:00c5a0c0:8"]]
- 004c8224 bytes b3431e94
+ 004c8544 bytes df461e94
~~~


<a id="compare-58f3a86bb5ba17d89256ab013e7ef229"></a>

### [`004c82d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md) → [`004c85f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85f8.md) _ZNK5Botan4Pipe9remainingEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md) · 呼出先 5件 [`004c974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5a0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0e0.md) · 呼出先 5件 [`004c9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

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
      "definition_site": "004c862c",
      "incomplete_value": true,
      "site": "004c862c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c830c",
      "incomplete_value": true,
      "site": "004c830c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d91:8"
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
      "definition_site": "004c8720",
      "incomplete_value": true,
      "site": "004c8728",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8400",
      "incomplete_value": true,
      "site": "004c8408",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
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
      "definition_site": "004c871c",
      "incomplete_value": false,
      "site": "004c8728",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c83fc",
      "incomplete_value": false,
      "site": "004c8408",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c8618",
      "READ",
      [
        "storage",
        "002b4d91",
        null,
        "string"
      ]
    ],
    [
      "004c871c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c8720",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8618",
      "READ",
      [
        "storage",
        "002b4e6f",
        null,
        "string"
      ]
    ],
    [
      "004c871c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c8720",
      "READ",
      [
        "storage",
        "00c9bfb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md#insn-004c8408) · [`004c82f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md#insn-004c82f0) · [`004c83cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md#insn-004c83cc)
- 新版 [`004c8728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85f8.md#insn-004c8728) · [`004c8610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85f8.md#insn-004c8610) · [`004c86ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85f8.md#insn-004c86ec)

~~~diff
- 004c8408 ["INT_ADD", "register:40f0:8", ["const:4c8408:8", "const:4:8"]]
- 004c8408 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c8728 ["INT_ADD", "register:40f0:8", ["const:4c8728:8", "const:4:8"]]
+ 004c8728 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8408 bytes f63e1e94
+ 004c8728 bytes 22421e94
- 004c82f0 ["COPY", "tmp:0:8", ["const:d91:8"]]
- 004c82f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004c82f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004c82f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004c8610 ["COPY", "tmp:0:8", ["const:e6f:8"]]
+ 004c8610 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004c8610 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004c8610 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004c82f0 bytes 4a453691
+ 004c8610 bytes 4abd3991
- 004c83cc ["INT_ADD", "register:40f0:8", ["const:4c83cc:8", "const:4:8"]]
- 004c83cc ["CALL", null, ["callee:00c58f90:8"]]
+ 004c86ec ["INT_ADD", "register:40f0:8", ["const:4c86ec:8", "const:4:8"]]
+ 004c86ec ["CALL", null, ["callee:00c58f90:8"]]
- 004c83cc bytes fd3e1e94
+ 004c86ec bytes 29421e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b45f131ae0f58e8092371e3ce710f8bb"></a>

### [`004c8450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md) → [`004c8770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8770.md) _ZN5Botan4Pipe15set_default_msgEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c87e0",
      "incomplete_value": false,
      "site": "004c87e8",
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
            "const:c4d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c84c0",
      "incomplete_value": false,
      "site": "004c84c8",
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
            "const:c03:8"
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
      "definition_site": "004c881c",
      "incomplete_value": true,
      "site": "004c8828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c84fc",
      "incomplete_value": true,
      "site": "004c8508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
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
      "definition_site": "004c8818",
      "incomplete_value": false,
      "site": "004c8828",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c84f8",
      "incomplete_value": false,
      "site": "004c8508",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c87e0",
      "PARAM",
      [
        "storage",
        "002b1c03",
        null,
        "string"
      ]
    ],
    [
      "004c8818",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c881c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c87e0",
      "PARAM",
      [
        "storage",
        "002b1c4d",
        null,
        "string"
      ]
    ],
    [
      "004c8818",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c881c",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c84c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md#insn-004c84c8) · [`004c8508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md#insn-004c8508) · [`004c84b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md#insn-004c84b4)
- 新版 [`004c87e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8770.md#insn-004c87e8) · [`004c8828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8770.md#insn-004c8828) · [`004c87d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8770.md#insn-004c87d4)

~~~diff
- 004c84c8 ["INT_ADD", "register:40f0:8", ["const:4c84c8:8", "const:4:8"]]
- 004c84c8 ["CALL", null, ["callee:0043e138:8"]]
+ 004c87e8 ["INT_ADD", "register:40f0:8", ["const:4c87e8:8", "const:4:8"]]
+ 004c87e8 ["CALL", null, ["callee:0043e138:8"]]
- 004c84c8 bytes 54d6fd97
+ 004c87e8 bytes 54d6fd97
- 004c8508 ["INT_ADD", "register:40f0:8", ["const:4c8508:8", "const:4:8"]]
- 004c8508 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c8828 ["INT_ADD", "register:40f0:8", ["const:4c8828:8", "const:4:8"]]
+ 004c8828 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8508 bytes b63e1e94
+ 004c8828 bytes e2411e94
- 004c84b4 ["INT_ADD", "register:40f0:8", ["const:4c84b4:8", "const:4:8"]]
- 004c84b4 ["CALL", null, ["callee:00c58f90:8"]]
+ 004c87d4 ["INT_ADD", "register:40f0:8", ["const:4c87d4:8", "const:4:8"]]
+ 004c87d4 ["CALL", null, ["callee:00c58f90:8"]]
- 004c84b4 bytes c33e1e94
+ 004c87d4 bytes ef411e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8e20c082cdc64f324796a2a2e67e53d"></a>

### [`004c85b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md) → [`004c88d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c88d0.md) _ZN5Botan4Pipe9start_msgEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a0f0.md) · 呼出先 10件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8924",
      "incomplete_value": true,
      "site": "004c8928",
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
      "definition_site": "004c8604",
      "incomplete_value": true,
      "site": "004c8608",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8948",
      "incomplete_value": false,
      "site": "004c8954",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8628",
      "incomplete_value": false,
      "site": "004c8634",
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
            "const:c28:8"
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
      "definition_site": "004c89b0",
      "incomplete_value": false,
      "site": "004c89b8",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8690",
      "incomplete_value": false,
      "site": "004c8698",
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
            "const:790:8"
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
      "004c891c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c8928",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8954",
      "DATA",
      [
        "storage",
        "00c66c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c891c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c8928",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8954",
      "DATA",
      [
        "storage",
        "00c67bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md#insn-004c8698) · [`004c86d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md#insn-004c86d4) · [`004c85ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md#insn-004c85ec)
- 新版 [`004c89b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c88d0.md#insn-004c89b8) · [`004c89f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c88d0.md#insn-004c89f4) · [`004c890c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c88d0.md#insn-004c890c)

~~~diff
- 004c8698 ["INT_ADD", "register:40f0:8", ["const:4c8698:8", "const:4:8"]]
- 004c8698 ["CALL", null, ["callee:0043e138:8"]]
+ 004c89b8 ["INT_ADD", "register:40f0:8", ["const:4c89b8:8", "const:4:8"]]
+ 004c89b8 ["CALL", null, ["callee:0043e138:8"]]
- 004c8698 bytes e0d5fd97
+ 004c89b8 bytes e0d5fd97
- 004c86d4 ["INT_ADD", "register:40f0:8", ["const:4c86d4:8", "const:4:8"]]
- 004c86d4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c89f4 ["INT_ADD", "register:40f0:8", ["const:4c89f4:8", "const:4:8"]]
+ 004c89f4 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c86d4 bytes 433e1e94
+ 004c89f4 bytes 6f411e94
- 004c85ec ["INT_ADD", "register:40f0:8", ["const:4c85ec:8", "const:4:8"]]
- 004c85ec ["CALL", null, ["callee:00c58f30:8"]]
+ 004c890c ["INT_ADD", "register:40f0:8", ["const:4c890c:8", "const:4:8"]]
+ 004c890c ["CALL", null, ["callee:00c58f30:8"]]
- 004c85ec bytes 5d3e1e94
+ 004c890c bytes 89411e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e489ddd77060d60453d51364e085ae4"></a>

### [`004c8750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md) → [`004c8a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8a70.md) _ZN5Botan4Pipe5writeEPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5a100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a100.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8adc",
      "incomplete_value": false,
      "site": "004c8ae4",
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
            "const:6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c87bc",
      "incomplete_value": false,
      "site": "004c87c4",
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
            "const:2b:8"
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
      "definition_site": "004c8b18",
      "incomplete_value": true,
      "site": "004c8b24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c87f8",
      "incomplete_value": true,
      "site": "004c8804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
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
      "definition_site": "004c8b14",
      "incomplete_value": false,
      "site": "004c8b24",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c87f4",
      "incomplete_value": false,
      "site": "004c8804",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c8adc",
      "PARAM",
      [
        "storage",
        "002a102b",
        null,
        "string"
      ]
    ],
    [
      "004c8b14",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c8b18",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8adc",
      "PARAM",
      [
        "storage",
        "002a106b",
        null,
        "string"
      ]
    ],
    [
      "004c8b14",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c8b18",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c87c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md#insn-004c87c4) · [`004c8804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md#insn-004c8804) · [`004c87b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md#insn-004c87b0)
- 新版 [`004c8ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8a70.md#insn-004c8ae4) · [`004c8b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8a70.md#insn-004c8b24) · [`004c8ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8a70.md#insn-004c8ad0)

~~~diff
- 004c87c4 ["INT_ADD", "register:40f0:8", ["const:4c87c4:8", "const:4:8"]]
- 004c87c4 ["CALL", null, ["callee:0043e138:8"]]
+ 004c8ae4 ["INT_ADD", "register:40f0:8", ["const:4c8ae4:8", "const:4:8"]]
+ 004c8ae4 ["CALL", null, ["callee:0043e138:8"]]
- 004c87c4 bytes 95d5fd97
+ 004c8ae4 bytes 95d5fd97
- 004c8804 ["INT_ADD", "register:40f0:8", ["const:4c8804:8", "const:4:8"]]
- 004c8804 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c8b24 ["INT_ADD", "register:40f0:8", ["const:4c8b24:8", "const:4:8"]]
+ 004c8b24 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8804 bytes f73d1e94
+ 004c8b24 bytes 23411e94
- 004c87b0 ["INT_ADD", "register:40f0:8", ["const:4c87b0:8", "const:4:8"]]
- 004c87b0 ["CALL", null, ["callee:00c58f90:8"]]
+ 004c8ad0 ["INT_ADD", "register:40f0:8", ["const:4c8ad0:8", "const:4:8"]]
+ 004c8ad0 ["CALL", null, ["callee:00c58f90:8"]]
- 004c87b0 bytes 043e1e94
+ 004c8ad0 bytes 30411e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e15851ebd9e34e25a2cf58bf8dbc854"></a>

### [`004c8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md) → [`004c8b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8b78.md) _ZN5Botan4Pipe7end_msgEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`004c7ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a110.md) · 呼出先 12件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`004c7fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7fc0.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8be0",
      "incomplete_value": true,
      "site": "004c8be4",
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
      "definition_site": "004c88c0",
      "incomplete_value": true,
      "site": "004c88c4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c8bd0",
      "incomplete_value": true,
      "site": "004c8bd0",
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
      "definition_site": "004c88b0",
      "incomplete_value": true,
      "site": "004c88b0",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8c18",
      "incomplete_value": true,
      "site": "004c8c18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c88f8",
      "incomplete_value": true,
      "site": "004c88f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "004c8bd8",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c8be4",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8c08",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8bd8",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "004c8be4",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8c08",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c88f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md#insn-004c88f8) · [`004c8954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md#insn-004c8954) · [`004c8990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md#insn-004c8990)
- 新版 [`004c8c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8b78.md#insn-004c8c18) · [`004c8c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8b78.md#insn-004c8c74) · [`004c8cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8b78.md#insn-004c8cb0)

~~~diff
- 004c88f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c88f8 ["INT_ADD", "register:40f0:8", ["const:4c88f8:8", "const:4:8"]]
- 004c88f8 ["CALLIND", null, ["register:0:8"]]
+ 004c8c18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c8c18 ["INT_ADD", "register:40f0:8", ["const:4c8c18:8", "const:4:8"]]
+ 004c8c18 ["CALLIND", null, ["register:0:8"]]
- 004c88f8 bytes 20013fd6
+ 004c8c18 bytes 20013fd6
- 004c8954 ["INT_ADD", "register:40f0:8", ["const:4c8954:8", "const:4:8"]]
- 004c8954 ["CALL", null, ["callee:0043e138:8"]]
+ 004c8c74 ["INT_ADD", "register:40f0:8", ["const:4c8c74:8", "const:4:8"]]
+ 004c8c74 ["CALL", null, ["callee:0043e138:8"]]
- 004c8954 bytes 31d5fd97
+ 004c8c74 bytes 31d5fd97
- 004c8990 ["INT_ADD", "register:40f0:8", ["const:4c8990:8", "const:4:8"]]
- 004c8990 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c8cb0 ["INT_ADD", "register:40f0:8", ["const:4c8cb0:8", "const:4:8"]]
+ 004c8cb0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8990 bytes 943d1e94
+ 004c8cb0 bytes c0401e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89dff8f58ce6b8d59fcd90b12688566a"></a>

### [`004c8af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md) → [`004c8e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8e14.md) _ZN5Botan4Pipe5writeERNS_10DataSourceE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59170.md) · 呼出先 9件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 1件 [`00c5a140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a140.md) · 呼出先 9件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8ed0",
      "incomplete_value": true,
      "site": "004c8ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8bb0",
      "incomplete_value": true,
      "site": "004c8bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "definition_site": "004c8f2c",
      "incomplete_value": true,
      "site": "004c8f34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8c0c",
      "incomplete_value": true,
      "site": "004c8c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8f30",
      "incomplete_value": true,
      "site": "004c8f34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8c10",
      "incomplete_value": true,
      "site": "004c8c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c8ebc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f2c",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f2c",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c8ebc",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f2c",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f2c",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md#insn-004c8bb0) · [`004c8c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md#insn-004c8c14) · [`004c8b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md#insn-004c8b34)
- 新版 [`004c8ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8e14.md#insn-004c8ed0) · [`004c8f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8e14.md#insn-004c8f34) · [`004c8e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c8e14.md#insn-004c8e54)

~~~diff
- 004c8bb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8bb0 ["INT_ADD", "register:40f0:8", ["const:4c8bb0:8", "const:4:8"]]
- 004c8bb0 ["CALLIND", null, ["register:0:8"]]
+ 004c8ed0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c8ed0 ["INT_ADD", "register:40f0:8", ["const:4c8ed0:8", "const:4:8"]]
+ 004c8ed0 ["CALLIND", null, ["register:0:8"]]
- 004c8bb0 bytes 20013fd6
+ 004c8ed0 bytes 20013fd6
- 004c8c14 ["INT_ADD", "register:40f0:8", ["const:4c8c14:8", "const:4:8"]]
- 004c8c14 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c8f34 ["INT_ADD", "register:40f0:8", ["const:4c8f34:8", "const:4:8"]]
+ 004c8f34 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8c14 bytes f33c1e94
+ 004c8f34 bytes 1f401e94
- 004c8b34 ["INT_ADD", "register:40f0:8", ["const:4c8b34:8", "const:4:8"]]
- 004c8b34 ["CALL", null, ["callee:00c59ad0:8"]]
+ 004c8e54 ["INT_ADD", "register:40f0:8", ["const:4c8e54:8", "const:4:8"]]
+ 004c8e54 ["CALL", null, ["callee:00c59ad0:8"]]
- 004c8b34 bytes f33f1e94
+ 004c8e54 bytes 1f431e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b6c3525a8c25b8ae765e1fe09812b4d"></a>

### [`004c8da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md) → [`004c90c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c90c8.md) _ZN5Botan4Pipe13append_filterEPNS_6FilterE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9130",
      "incomplete_value": false,
      "site": "004c9138",
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
            "const:5c3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8e10",
      "incomplete_value": false,
      "site": "004c8e18",
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
            "const:46b:8"
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
      "definition_site": "004c916c",
      "incomplete_value": true,
      "site": "004c9178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8e4c",
      "incomplete_value": true,
      "site": "004c8e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
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
      "definition_site": "004c9168",
      "incomplete_value": false,
      "site": "004c9178",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c8e48",
      "incomplete_value": false,
      "site": "004c8e58",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c9130",
      "PARAM",
      [
        "storage",
        "002a546b",
        null,
        "string"
      ]
    ],
    [
      "004c9168",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c916c",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c9130",
      "PARAM",
      [
        "storage",
        "002a55c3",
        null,
        "string"
      ]
    ],
    [
      "004c9168",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c916c",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md#insn-004c8e18) · [`004c8e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md#insn-004c8e58) · [`004c8e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md#insn-004c8e04)
- 新版 [`004c9138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c90c8.md#insn-004c9138) · [`004c9178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c90c8.md#insn-004c9178) · [`004c9124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c90c8.md#insn-004c9124)

~~~diff
- 004c8e18 ["INT_ADD", "register:40f0:8", ["const:4c8e18:8", "const:4:8"]]
- 004c8e18 ["CALL", null, ["callee:0043e138:8"]]
+ 004c9138 ["INT_ADD", "register:40f0:8", ["const:4c9138:8", "const:4:8"]]
+ 004c9138 ["CALL", null, ["callee:0043e138:8"]]
- 004c8e18 bytes 00d4fd97
+ 004c9138 bytes 00d4fd97
- 004c8e58 ["INT_ADD", "register:40f0:8", ["const:4c8e58:8", "const:4:8"]]
- 004c8e58 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c9178 ["INT_ADD", "register:40f0:8", ["const:4c9178:8", "const:4:8"]]
+ 004c9178 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8e58 bytes 623c1e94
+ 004c9178 bytes 8e3f1e94
- 004c8e04 ["INT_ADD", "register:40f0:8", ["const:4c8e04:8", "const:4:8"]]
- 004c8e04 ["CALL", null, ["callee:00c58f90:8"]]
+ 004c9124 ["INT_ADD", "register:40f0:8", ["const:4c9124:8", "const:4:8"]]
+ 004c9124 ["CALL", null, ["callee:00c58f90:8"]]
- 004c8e04 bytes 6f3c1e94
+ 004c9124 bytes 9b3f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-413ff51e1ad8ae64c7002908839692f4"></a>

### [`004c8eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md) → [`004c91cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c91cc.md) _ZN5Botan4Pipe7prependEPNS_6FilterE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c9208",
      "incomplete_value": true,
      "site": "004c920c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004c8ee8",
      "incomplete_value": true,
      "site": "004c8eec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9298",
      "incomplete_value": false,
      "site": "004c92a0",
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
            "const:162:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8f78",
      "incomplete_value": false,
      "site": "004c8f80",
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
            "const:93:8"
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
      "definition_site": "004c92d4",
      "incomplete_value": true,
      "site": "004c92e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8fb4",
      "incomplete_value": true,
      "site": "004c8fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "004c91fc",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9298",
      "PARAM",
      [
        "storage",
        "002b6093",
        null,
        "string"
      ]
    ],
    [
      "004c92d0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c91fc",
      "READ",
      [
        "storage",
        "00c9bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9298",
      "PARAM",
      [
        "storage",
        "002b6162",
        null,
        "string"
      ]
    ],
    [
      "004c92d0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md#insn-004c8f80) · [`004c8fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md#insn-004c8fc0) · [`004c8fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md#insn-004c8fe4)
- 新版 [`004c92a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c91cc.md#insn-004c92a0) · [`004c92e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c91cc.md#insn-004c92e0) · [`004c9304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c91cc.md#insn-004c9304)

~~~diff
- 004c8f80 ["INT_ADD", "register:40f0:8", ["const:4c8f80:8", "const:4:8"]]
- 004c8f80 ["CALL", null, ["callee:0043e138:8"]]
+ 004c92a0 ["INT_ADD", "register:40f0:8", ["const:4c92a0:8", "const:4:8"]]
+ 004c92a0 ["CALL", null, ["callee:0043e138:8"]]
- 004c8f80 bytes a6d3fd97
+ 004c92a0 bytes a6d3fd97
- 004c8fc0 ["INT_ADD", "register:40f0:8", ["const:4c8fc0:8", "const:4:8"]]
- 004c8fc0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c92e0 ["INT_ADD", "register:40f0:8", ["const:4c92e0:8", "const:4:8"]]
+ 004c92e0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c8fc0 bytes 083c1e94
+ 004c92e0 bytes 343f1e94
- 004c8fe4 ["INT_ADD", "register:40f0:8", ["const:4c8fe4:8", "const:4:8"]]
- 004c8fe4 ["CALL", null, ["callee:0043e138:8"]]
+ 004c9304 ["INT_ADD", "register:40f0:8", ["const:4c9304:8", "const:4:8"]]
+ 004c9304 ["CALL", null, ["callee:0043e138:8"]]
- 004c8fe4 bytes 8dd3fd97
+ 004c9304 bytes 8dd3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67c2c7e6671439e4f3d01f646cb00a1a"></a>

### [`004c90e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md) → [`004c9404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9404.md) _ZN5Botan4Pipe3popEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c94b0",
      "incomplete_value": false,
      "site": "004c94b8",
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
            "const:622:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9190",
      "incomplete_value": false,
      "site": "004c9198",
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
            "const:4ca:8"
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
      "definition_site": "004c94ec",
      "incomplete_value": true,
      "site": "004c94f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c91cc",
      "incomplete_value": true,
      "site": "004c91d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "004c94e8",
      "incomplete_value": false,
      "site": "004c94f8",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c91c8",
      "incomplete_value": false,
      "site": "004c91d8",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c94b0",
      "PARAM",
      [
        "storage",
        "002a54ca",
        null,
        "string"
      ]
    ],
    [
      "004c94e8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c94ec",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c94b0",
      "PARAM",
      [
        "storage",
        "002a5622",
        null,
        "string"
      ]
    ],
    [
      "004c94e8",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c94ec",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md#insn-004c9198) · [`004c91d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md#insn-004c91d8) · [`004c91fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md#insn-004c91fc)
- 新版 [`004c94b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9404.md#insn-004c94b8) · [`004c94f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9404.md#insn-004c94f8) · [`004c951c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9404.md#insn-004c951c)

~~~diff
- 004c9198 ["INT_ADD", "register:40f0:8", ["const:4c9198:8", "const:4:8"]]
- 004c9198 ["CALL", null, ["callee:0043e138:8"]]
+ 004c94b8 ["INT_ADD", "register:40f0:8", ["const:4c94b8:8", "const:4:8"]]
+ 004c94b8 ["CALL", null, ["callee:0043e138:8"]]
- 004c9198 bytes 20d3fd97
+ 004c94b8 bytes 20d3fd97
- 004c91d8 ["INT_ADD", "register:40f0:8", ["const:4c91d8:8", "const:4:8"]]
- 004c91d8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c94f8 ["INT_ADD", "register:40f0:8", ["const:4c94f8:8", "const:4:8"]]
+ 004c94f8 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c91d8 bytes 823b1e94
+ 004c94f8 bytes ae3e1e94
- 004c91fc ["INT_ADD", "register:40f0:8", ["const:4c91fc:8", "const:4:8"]]
- 004c91fc ["CALL", null, ["callee:0043e138:8"]]
+ 004c951c ["INT_ADD", "register:40f0:8", ["const:4c951c:8", "const:4:8"]]
+ 004c951c ["CALL", null, ["callee:0043e138:8"]]
- 004c91fc bytes 07d3fd97
+ 004c951c bytes 07d3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca02d401f2c2472ad373eebe59eafd0"></a>

### [`004c9290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md) → [`004c95b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c95b0.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9688",
      "incomplete_value": true,
      "site": "004c9688",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9368",
      "incomplete_value": true,
      "site": "004c9368",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "definition_site": "004c96e8",
      "incomplete_value": true,
      "site": "004c96f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c93c8",
      "incomplete_value": true,
      "site": "004c93d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c96ec",
      "incomplete_value": true,
      "site": "004c96f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c93cc",
      "incomplete_value": true,
      "site": "004c93d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c9678",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c96e8",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004c96e8",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9678",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004c96e8",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "004c96e8",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md#insn-004c9368) · [`004c93d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md#insn-004c93d0) · [`004c93ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md#insn-004c93ec)
- 新版 [`004c9688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c95b0.md#insn-004c9688) · [`004c96f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c95b0.md#insn-004c96f0) · [`004c970c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c95b0.md#insn-004c970c)

~~~diff
- 004c9368 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9368 ["INT_ADD", "register:40f0:8", ["const:4c9368:8", "const:4:8"]]
- 004c9368 ["CALLIND", null, ["register:0:8"]]
+ 004c9688 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9688 ["INT_ADD", "register:40f0:8", ["const:4c9688:8", "const:4:8"]]
+ 004c9688 ["CALLIND", null, ["register:0:8"]]
- 004c9368 bytes 20013fd6
+ 004c9688 bytes 20013fd6
- 004c93d0 ["INT_ADD", "register:40f0:8", ["const:4c93d0:8", "const:4:8"]]
- 004c93d0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c96f0 ["INT_ADD", "register:40f0:8", ["const:4c96f0:8", "const:4:8"]]
+ 004c96f0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c93d0 bytes 043b1e94
+ 004c96f0 bytes 303e1e94
- 004c93ec ["INT_ADD", "register:40f0:8", ["const:4c93ec:8", "const:4:8"]]
- 004c93ec ["CALL", null, ["callee:0043e138:8"]]
+ 004c970c ["INT_ADD", "register:40f0:8", ["const:4c970c:8", "const:4:8"]]
+ 004c970c ["CALL", null, ["callee:0043e138:8"]]
- 004c93ec bytes 8bd2fd97
+ 004c970c bytes 8bd2fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d126507ef08df5edecc41aeeea3b043"></a>

### [`004c94a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md) → [`004c97c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c97c8.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9888",
      "incomplete_value": true,
      "site": "004c9888",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9568",
      "incomplete_value": true,
      "site": "004c9568",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "definition_site": "004c98e8",
      "incomplete_value": true,
      "site": "004c98f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c95c8",
      "incomplete_value": true,
      "site": "004c95d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c98ec",
      "incomplete_value": true,
      "site": "004c98f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c95cc",
      "incomplete_value": true,
      "site": "004c95d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c9878",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c98e8",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004c98e8",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9878",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004c98e8",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "004c98e8",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md#insn-004c9568) · [`004c95d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md#insn-004c95d0) · [`004c95ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md#insn-004c95ec)
- 新版 [`004c9888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c97c8.md#insn-004c9888) · [`004c98f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c97c8.md#insn-004c98f0) · [`004c990c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c97c8.md#insn-004c990c)

~~~diff
- 004c9568 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9568 ["INT_ADD", "register:40f0:8", ["const:4c9568:8", "const:4:8"]]
- 004c9568 ["CALLIND", null, ["register:0:8"]]
+ 004c9888 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9888 ["INT_ADD", "register:40f0:8", ["const:4c9888:8", "const:4:8"]]
+ 004c9888 ["CALLIND", null, ["register:0:8"]]
- 004c9568 bytes 20013fd6
+ 004c9888 bytes 20013fd6
- 004c95d0 ["INT_ADD", "register:40f0:8", ["const:4c95d0:8", "const:4:8"]]
- 004c95d0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c98f0 ["INT_ADD", "register:40f0:8", ["const:4c98f0:8", "const:4:8"]]
+ 004c98f0 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c95d0 bytes 843a1e94
+ 004c98f0 bytes b03d1e94
- 004c95ec ["INT_ADD", "register:40f0:8", ["const:4c95ec:8", "const:4:8"]]
- 004c95ec ["CALL", null, ["callee:0043e138:8"]]
+ 004c990c ["INT_ADD", "register:40f0:8", ["const:4c990c:8", "const:4:8"]]
+ 004c990c ["CALL", null, ["callee:0043e138:8"]]
- 004c95ec bytes 0bd2fd97
+ 004c990c bytes 0bd2fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff2c1926855df4f56aa3b53f1ba369c"></a>

### [`004c96a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c96a0.md) → [`004c99c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c99c0.md) _ZNK5Botan4Pipe14get_message_noERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004c9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "definition_site": "004c9a4c",
      "incomplete_value": true,
      "site": "004c9a54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c972c",
      "incomplete_value": true,
      "site": "004c9734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
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
      "definition_site": "004c9a48",
      "incomplete_value": false,
      "site": "004c9a54",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c9728",
      "incomplete_value": false,
      "site": "004c9734",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c9a48",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c9a4c",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c9a4c",
      "PARAM",
      [
        "storage",
        "00c66c68",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9a48",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c9a4c",
      "READ",
      [
        "storage",
        "00c9bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "004c9a4c",
      "PARAM",
      [
        "storage",
        "00c67c38",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c96a0.md#insn-004c9734) · [`004c970c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c96a0.md#insn-004c970c) · [`004c971c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c96a0.md#insn-004c971c)
- 新版 [`004c9a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c99c0.md#insn-004c9a54) · [`004c9a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c99c0.md#insn-004c9a2c) · [`004c9a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c99c0.md#insn-004c9a3c)

~~~diff
- 004c9734 ["INT_ADD", "register:40f0:8", ["const:4c9734:8", "const:4:8"]]
- 004c9734 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c9a54 ["INT_ADD", "register:40f0:8", ["const:4c9a54:8", "const:4:8"]]
+ 004c9a54 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c9734 bytes 2b3a1e94
+ 004c9a54 bytes 573d1e94
- 004c970c ["INT_ADD", "register:40f0:8", ["const:4c970c:8", "const:4:8"]]
- 004c970c ["CALL", null, ["callee:00c58f90:8"]]
+ 004c9a2c ["INT_ADD", "register:40f0:8", ["const:4c9a2c:8", "const:4:8"]]
+ 004c9a2c ["CALL", null, ["callee:00c58f90:8"]]
- 004c970c bytes 2d3a1e94
+ 004c9a2c bytes 593d1e94
- 004c971c ["INT_ADD", "register:40f0:8", ["const:4c971c:8", "const:4:8"]]
- 004c971c ["CALL", null, ["callee:004c9a6c:8"]]
+ 004c9a3c ["INT_ADD", "register:40f0:8", ["const:4c9a3c:8", "const:4:8"]]
+ 004c9a3c ["CALL", null, ["callee:004c9a6c:8"]]
- 004c971c bytes 0c000094
+ 004c9a3c bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f898291d72a5c8ab68a8c92cb1bbf4"></a>

### [`004c974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md) → [`004c9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md) FUN_004c9a6c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004c82d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md) [`004c96a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c96a0.md) [`004c99c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c99c0.md) [`004c9d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9d3c.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 4件 [`004c85f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c8/004c85f8.md) [`004c99c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c99c0.md) [`004c9ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ce0.md) [`004ca05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ca/004ca05c.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9b34",
      "incomplete_value": true,
      "site": "004c9b38",
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
      "definition_site": "004c9814",
      "incomplete_value": true,
      "site": "004c9818",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9b68",
      "incomplete_value": true,
      "site": "004c9b6c",
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
      "definition_site": "004c9848",
      "incomplete_value": true,
      "site": "004c984c",
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9a8c",
      "incomplete_value": false,
      "site": "004c9aa0",
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
            "const:a8b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c976c",
      "incomplete_value": false,
      "site": "004c9780",
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
            "const:9ad:8"
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
      "004c9a8c",
      "PARAM",
      [
        "storage",
        "002bd9ad",
        null,
        "string"
      ]
    ],
    [
      "004c9aa8",
      "PARAM",
      [
        "storage",
        "002bb454",
        null,
        "string"
      ]
    ],
    [
      "004c9b18",
      "PARAM",
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
      "004c9a8c",
      "PARAM",
      [
        "storage",
        "002bda8b",
        null,
        "string"
      ]
    ],
    [
      "004c9aa8",
      "PARAM",
      [
        "storage",
        "002bb532",
        null,
        "string"
      ]
    ],
    [
      "004c9b18",
      "PARAM",
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

- 旧版 [`004c9780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md#insn-004c9780) · [`004c9790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md#insn-004c9790) · [`004c9804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md#insn-004c9804)
- 新版 [`004c9aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md#insn-004c9aa0) · [`004c9ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md#insn-004c9ab0) · [`004c9b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md#insn-004c9b24)

~~~diff
- 004c9780 ["INT_ADD", "register:40f0:8", ["const:4c9780:8", "const:4:8"]]
- 004c9780 ["CALL", null, ["callee:00c59150:8"]]
+ 004c9aa0 ["INT_ADD", "register:40f0:8", ["const:4c9aa0:8", "const:4:8"]]
+ 004c9aa0 ["CALL", null, ["callee:00c59150:8"]]
- 004c9780 bytes 803a1e94
+ 004c9aa0 bytes ac3d1e94
- 004c9790 ["INT_ADD", "register:40f0:8", ["const:4c9790:8", "const:4:8"]]
- 004c9790 ["CALL", null, ["callee:00c59010:8"]]
+ 004c9ab0 ["INT_ADD", "register:40f0:8", ["const:4c9ab0:8", "const:4:8"]]
+ 004c9ab0 ["CALL", null, ["callee:00c59010:8"]]
- 004c9790 bytes 2c3a1e94
+ 004c9ab0 bytes 583d1e94
- 004c9804 ["INT_ADD", "register:40f0:8", ["const:4c9804:8", "const:4:8"]]
- 004c9804 ["CALL", null, ["callee:00c59820:8"]]
+ 004c9b24 ["INT_ADD", "register:40f0:8", ["const:4c9b24:8", "const:4:8"]]
+ 004c9b24 ["CALL", null, ["callee:00c59820:8"]]
- 004c9804 bytes 133c1e94
+ 004c9b24 bytes 3f3f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3b7158869b0a944a4000153ab7adb72"></a>

### [`004c99c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c99c0.md) → [`004c9ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ce0.md) _ZN5Botan4Pipe4readEPhmm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59190.md) · 呼出先 6件 [`004c974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5a160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a160.md) · 呼出先 6件 [`004c9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9a6c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "definition_site": "004c9de4",
      "incomplete_value": true,
      "site": "004c9dec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9ac4",
      "incomplete_value": true,
      "site": "004c9acc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
              ]
            ]
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
      "definition_site": "004c9de0",
      "incomplete_value": false,
      "site": "004c9dec",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "004c9ac0",
      "incomplete_value": false,
      "site": "004c9acc",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "004c9de0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c9de4",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004c9de4",
      "PARAM",
      [
        "storage",
        "00c66c68",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9de0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "004c9de4",
      "READ",
      [
        "storage",
        "00c9bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "004c9de4",
      "PARAM",
      [
        "storage",
        "00c67c38",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c99c0.md#insn-004c9acc) · [`004c9a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c99c0.md#insn-004c9a64) · [`004c9a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c99c0.md#insn-004c9a94)
- 新版 [`004c9dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ce0.md#insn-004c9dec) · [`004c9d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ce0.md#insn-004c9d84) · [`004c9db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ce0.md#insn-004c9db4)

~~~diff
- 004c9acc ["INT_ADD", "register:40f0:8", ["const:4c9acc:8", "const:4:8"]]
- 004c9acc ["CALL", null, ["callee:00c58fb0:8"]]
+ 004c9dec ["INT_ADD", "register:40f0:8", ["const:4c9dec:8", "const:4:8"]]
+ 004c9dec ["CALL", null, ["callee:00c58fb0:8"]]
- 004c9acc bytes 45391e94
+ 004c9dec bytes 713c1e94
- 004c9a64 ["INT_ADD", "register:40f0:8", ["const:4c9a64:8", "const:4:8"]]
- 004c9a64 ["CALL", null, ["callee:00c5a090:8"]]
+ 004c9d84 ["INT_ADD", "register:40f0:8", ["const:4c9d84:8", "const:4:8"]]
+ 004c9d84 ["CALL", null, ["callee:00c5a090:8"]]
- 004c9a64 bytes 973d1e94
+ 004c9d84 bytes c3401e94
- 004c9a94 ["INT_ADD", "register:40f0:8", ["const:4c9a94:8", "const:4:8"]]
- 004c9a94 ["CALL", null, ["callee:00c58f90:8"]]
+ 004c9db4 ["INT_ADD", "register:40f0:8", ["const:4c9db4:8", "const:4:8"]]
+ 004c9db4 ["CALL", null, ["callee:00c58f90:8"]]
- 004c9a94 bytes 4b391e94
+ 004c9db4 bytes 773c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69a114a98fa0c208af36f6efa7ca87ce"></a>

### [`004c9bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9bb4.md) → [`004c9ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ed4.md) _ZN5Botan4Pipe18read_all_as_stringEm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9fa4",
      "incomplete_value": true,
      "site": "004c9fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9c84",
      "incomplete_value": true,
      "site": "004c9c84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca000",
      "incomplete_value": true,
      "site": "004ca008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c9ce0",
      "incomplete_value": true,
      "site": "004c9ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca004",
      "incomplete_value": true,
      "site": "004ca008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c9ce4",
      "incomplete_value": true,
      "site": "004c9ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c9f90",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004ca000",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca000",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9f90",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca000",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "004ca000",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9bb4.md#insn-004c9c84) · [`004c9ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9bb4.md#insn-004c9ce8) · [`004c9c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9bb4.md#insn-004c9c00)
- 新版 [`004c9fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ed4.md#insn-004c9fa4) · [`004ca008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ed4.md#insn-004ca008) · [`004c9f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c9/004c9ed4.md#insn-004c9f20)

~~~diff
- 004c9c84 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9c84 ["INT_ADD", "register:40f0:8", ["const:4c9c84:8", "const:4:8"]]
- 004c9c84 ["CALLIND", null, ["register:0:8"]]
+ 004c9fa4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9fa4 ["INT_ADD", "register:40f0:8", ["const:4c9fa4:8", "const:4:8"]]
+ 004c9fa4 ["CALLIND", null, ["register:0:8"]]
- 004c9c84 bytes 20013fd6
+ 004c9fa4 bytes 20013fd6
- 004c9ce8 ["INT_ADD", "register:40f0:8", ["const:4c9ce8:8", "const:4:8"]]
- 004c9ce8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004ca008 ["INT_ADD", "register:40f0:8", ["const:4ca008:8", "const:4:8"]]
+ 004ca008 ["CALL", null, ["callee:00c58fb0:8"]]
- 004c9ce8 bytes be381e94
+ 004ca008 bytes ea3b1e94
- 004c9c00 ["INT_ADD", "register:40f0:8", ["const:4c9c00:8", "const:4:8"]]
- 004c9c00 ["CALL", null, ["callee:00c59ad0:8"]]
+ 004c9f20 ["INT_ADD", "register:40f0:8", ["const:4c9f20:8", "const:4:8"]]
+ 004c9f20 ["CALL", null, ["callee:00c59ad0:8"]]
- 004c9c00 bytes c03b1e94
+ 004c9f20 bytes ec3e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

