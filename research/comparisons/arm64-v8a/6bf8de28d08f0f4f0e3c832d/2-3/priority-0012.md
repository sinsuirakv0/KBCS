# v16.0.2 → v16.0.3 · 最優先の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-34abcad6bb07fa7a747a127a32b88a88"></a>

### [`00516f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md) → [`00517268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517268.md) _ZNK5Botan10Extensions10extensionsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ed0.md) · 呼出先 3件 [`0054c12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054c12c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c5aea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aea0.md) · 呼出先 3件 [`0054c44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054c/0054c44c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517384",
      "incomplete_value": false,
      "site": "005173a4",
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
            "const:da3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517064",
      "incomplete_value": false,
      "site": "00517084",
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
            "const:cd6:8"
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
      "definition_site": "0051738c",
      "incomplete_value": false,
      "site": "005173a4",
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
      "definition_site": "0051706c",
      "incomplete_value": false,
      "site": "00517084",
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517394",
      "incomplete_value": false,
      "site": "005173a4",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517074",
      "incomplete_value": false,
      "site": "00517084",
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
            "const:2f7:8"
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
      "00517384",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "0051738c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00517394",
      "PARAM",
      [
        "storage",
        "002c12f7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517384",
      "PARAM",
      [
        "storage",
        "002a9da3",
        null,
        "string"
      ]
    ],
    [
      "0051738c",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00517394",
      "PARAM",
      [
        "storage",
        "002c1341",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md#insn-00517084) · [`00516fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md#insn-00516fc4) · [`00516ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md#insn-00516ffc)
- 新版 [`005173a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517268.md#insn-005173a4) · [`005172e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517268.md#insn-005172e4) · [`0051731c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517268.md#insn-0051731c)

~~~diff
- 00517084 ["INT_ADD", "register:40f0:8", ["const:517084:8", "const:4:8"]]
- 00517084 ["CALL", null, ["callee:00c596f0:8"]]
+ 005173a4 ["INT_ADD", "register:40f0:8", ["const:5173a4:8", "const:4:8"]]
+ 005173a4 ["CALL", null, ["callee:00c596f0:8"]]
- 00517084 bytes a7051d94
+ 005173a4 bytes d3081d94
- 00516fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516fc4 ["INT_ADD", "register:40f0:8", ["const:516fc4:8", "const:4:8"]]
- 00516fc4 ["CALLIND", null, ["register:0:8"]]
+ 005172e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005172e4 ["INT_ADD", "register:40f0:8", ["const:5172e4:8", "const:4:8"]]
+ 005172e4 ["CALLIND", null, ["register:0:8"]]
- 00516fc4 bytes 00013fd6
+ 005172e4 bytes 00013fd6
- 00516ffc ["INT_ADD", "register:40f0:8", ["const:516ffc:8", "const:4:8"]]
- 00516ffc ["CALL", null, ["callee:0054c44c:8"]]
+ 0051731c ["INT_ADD", "register:40f0:8", ["const:51731c:8", "const:4:8"]]
+ 0051731c ["CALL", null, ["callee:0054c44c:8"]]
- 00516ffc bytes 4cd40094
+ 0051731c bytes 4cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c7d5f2b5abb373d94ac15ddcc4ed68a"></a>

### [`005172d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md) → [`005175f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005175f0.md) _ZNK5Botan10Extensions11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0051211c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md) · 呼出先 9件 [`005174c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0051243c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051243c.md) · 呼出先 9件 [`005177e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005177e8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517790",
      "incomplete_value": false,
      "site": "005177b0",
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
            "const:da3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517470",
      "incomplete_value": false,
      "site": "00517490",
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
            "const:cd6:8"
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
      "definition_site": "00517798",
      "incomplete_value": false,
      "site": "005177b0",
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
      "definition_site": "00517478",
      "incomplete_value": false,
      "site": "00517490",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005177a0",
      "incomplete_value": false,
      "site": "005177b0",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517480",
      "incomplete_value": false,
      "site": "00517490",
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
            "const:2f7:8"
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
      "00517790",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "00517798",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "005177a0",
      "PARAM",
      [
        "storage",
        "002c12f7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517790",
      "PARAM",
      [
        "storage",
        "002a9da3",
        null,
        "string"
      ]
    ],
    [
      "00517798",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "005177a0",
      "PARAM",
      [
        "storage",
        "002c1341",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md#insn-00517490) · [`00517320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md#insn-00517320) · [`00517334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md#insn-00517334)
- 新版 [`005177b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005175f0.md#insn-005177b0) · [`00517640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005175f0.md#insn-00517640) · [`00517654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005175f0.md#insn-00517654)

~~~diff
- 00517490 ["INT_ADD", "register:40f0:8", ["const:517490:8", "const:4:8"]]
- 00517490 ["CALL", null, ["callee:00c596f0:8"]]
+ 005177b0 ["INT_ADD", "register:40f0:8", ["const:5177b0:8", "const:4:8"]]
+ 005177b0 ["CALL", null, ["callee:00c596f0:8"]]
- 00517490 bytes a4041d94
+ 005177b0 bytes d0071d94
- 00517320 ["INT_ADD", "register:40f0:8", ["const:517320:8", "const:4:8"]]
- 00517320 ["CALL", null, ["callee:005177e8:8"]]
+ 00517640 ["INT_ADD", "register:40f0:8", ["const:517640:8", "const:4:8"]]
+ 00517640 ["CALL", null, ["callee:005177e8:8"]]
- 00517320 bytes 6a000094
+ 00517640 bytes 6a000094
- 00517334 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517334 ["INT_ADD", "register:40f0:8", ["const:517334:8", "const:4:8"]]
- 00517334 ["CALLIND", null, ["register:0:8"]]
+ 00517654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517654 ["INT_ADD", "register:40f0:8", ["const:517654:8", "const:4:8"]]
+ 00517654 ["CALLIND", null, ["register:0:8"]]
- 00517334 bytes 00013fd6
+ 00517654 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-701154305cefcb53a38dbd6d066cceea"></a>

### [`005174c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md) → [`005177e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005177e8.md) FUN_005177e8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005172d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md) [`0053c44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c44c.md) [`0054a304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a304.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 3件 [`005175f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005175f0.md) [`0053c76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053c76c.md) [`0054a624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a624.md) · 呼出先 5件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00517824",
      "incomplete_value": true,
      "site": "00517828",
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
      "definition_site": "00517504",
      "incomplete_value": true,
      "site": "00517508",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00517814",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00517828",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00517814",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00517828",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005174e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md#insn-005174e8) · [`005174f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md#insn-005174f4) · [`0051751c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md#insn-0051751c)
- 新版 [`00517808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005177e8.md#insn-00517808) · [`00517814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005177e8.md#insn-00517814) · [`0051783c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005177e8.md#insn-0051783c)

~~~diff
- 005174e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00517808 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005174e8 bytes 083c00f0
+ 00517808 bytes 283c0090
- 005174f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 005174f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00517814 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 00517814 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005174f4 bytes 080947f9
+ 00517814 bytes 08f146f9
- 0051751c ["INT_ADD", "register:40f0:8", ["const:51751c:8", "const:4:8"]]
- 0051751c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051783c ["INT_ADD", "register:40f0:8", ["const:51783c:8", "const:4:8"]]
+ 0051783c ["CALL", null, ["callee:00c58f30:8"]]
- 0051751c bytes 91021d94
+ 0051783c bytes bd051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ea9906dbf0233a00adc4a3e8cb21689"></a>

### [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) → [`005179b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005179b0.md) _ZN5Botan10Extensions11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005037ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md) [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) · 呼出先 21件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00517c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md)
- 新版 呼出元 2件 [`00503acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503acc.md) [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) · 呼出先 21件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00517f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517f94.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`0053b784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b784.md) [`0054bca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bca4.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00517b20",
      "incomplete_value": true,
      "site": "00517b20",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00517800",
      "incomplete_value": true,
      "site": "00517800",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00517cbc",
      "incomplete_value": true,
      "site": "00517cbc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051799c",
      "incomplete_value": true,
      "site": "0051799c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00517a38",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00517b10",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00517b68",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00517a38",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00517b10",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00517b68",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md#insn-00517800) · [`0051799c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md#insn-0051799c) · [`005176ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md#insn-005176ec)
- 新版 [`00517b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005179b0.md#insn-00517b20) · [`00517cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005179b0.md#insn-00517cbc) · [`00517a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005179b0.md#insn-00517a0c)

~~~diff
- 00517800 ["COPY", "register:0:8", ["register:4048:8"]]
- 00517800 ["INT_ADD", "register:40f0:8", ["const:517800:8", "const:4:8"]]
- 00517800 ["CALLIND", null, ["register:0:8"]]
+ 00517b20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00517b20 ["INT_ADD", "register:40f0:8", ["const:517b20:8", "const:4:8"]]
+ 00517b20 ["CALLIND", null, ["register:0:8"]]
- 00517800 bytes 20013fd6
+ 00517b20 bytes 20013fd6
- 0051799c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051799c ["INT_ADD", "register:40f0:8", ["const:51799c:8", "const:4:8"]]
- 0051799c ["CALLIND", null, ["register:0:8"]]
+ 00517cbc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00517cbc ["INT_ADD", "register:40f0:8", ["const:517cbc:8", "const:4:8"]]
+ 00517cbc ["CALLIND", null, ["register:0:8"]]
- 0051799c bytes 20013fd6
+ 00517cbc bytes 20013fd6
- 005176ec ["INT_ADD", "register:40f0:8", ["const:5176ec:8", "const:4:8"]]
- 005176ec ["CALL", null, ["callee:0053b784:8"]]
+ 00517a0c ["INT_ADD", "register:40f0:8", ["const:517a0c:8", "const:4:8"]]
+ 00517a0c ["CALL", null, ["callee:0053b784:8"]]
- 005176ec bytes 5e8f0094
+ 00517a0c bytes 5e8f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a4aeb64e5c76e021465e6491c39164"></a>

### [`00517c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md) → [`00517f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517f94.md) FUN_00517f94

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`005179b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005179b0.md) · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

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
      "definition_site": "00517fe4",
      "incomplete_value": true,
      "site": "00517fe4",
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
      "definition_site": "00517cc4",
      "incomplete_value": true,
      "site": "00517cc4",
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
      "00517fd0",
      "READ",
      [
        "storage",
        "00c9b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00517fe4",
      "DATA",
      [
        "storage",
        "00c6a508",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00517fd0",
      "READ",
      [
        "storage",
        "00c9c1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00517fe4",
      "DATA",
      [
        "storage",
        "00c6b4d8",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md#insn-00517ca0) · [`00517ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md#insn-00517ca8) · [`00517cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md#insn-00517cb0)
- 新版 [`00517fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517f94.md#insn-00517fc0) · [`00517fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517f94.md#insn-00517fc8) · [`00517fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/00517f94.md#insn-00517fd0)

~~~diff
- 00517ca0 ["INT_ADD", "register:40f0:8", ["const:517ca0:8", "const:4:8"]]
- 00517ca0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00517fc0 ["INT_ADD", "register:40f0:8", ["const:517fc0:8", "const:4:8"]]
+ 00517fc0 ["CALL", null, ["callee:00c58f30:8"]]
- 00517ca0 bytes b0001d94
+ 00517fc0 bytes dc031d94
- 00517ca8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00517fc8 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00517ca8 bytes 283c0090
+ 00517fc8 bytes 283c00b0
- 00517cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 00517cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00517fd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00517fd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00517cb0 bytes 08f940f9
+ 00517fd0 bytes 08e140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8219234482bb9d21bee607eb44eb0076"></a>

### [`00517d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md) → [`00518088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518088.md) _ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ef0.md) · 呼出先 6件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c5aec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aec0.md) · 呼出先 6件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518208",
      "incomplete_value": false,
      "site": "00518228",
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
            "const:da3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517ee8",
      "incomplete_value": false,
      "site": "00517f08",
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
            "const:cd6:8"
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
      "definition_site": "00518210",
      "incomplete_value": false,
      "site": "00518228",
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
      "definition_site": "00517ef0",
      "incomplete_value": false,
      "site": "00517f08",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518218",
      "incomplete_value": false,
      "site": "00518228",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517ef8",
      "incomplete_value": false,
      "site": "00517f08",
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
            "const:2f7:8"
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
      "00518114",
      "PARAM",
      [
        "storage",
        "002b61be",
        null,
        "string"
      ]
    ],
    [
      "00518208",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "00518210",
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
      "00518114",
      "PARAM",
      [
        "storage",
        "002b628d",
        null,
        "string"
      ]
    ],
    [
      "00518208",
      "PARAM",
      [
        "storage",
        "002a9da3",
        null,
        "string"
      ]
    ],
    [
      "00518210",
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

- 旧版 [`00517f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md#insn-00517f08) · [`00517da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md#insn-00517da8) · [`00517dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md#insn-00517dd4)
- 新版 [`00518228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518088.md#insn-00518228) · [`005180c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518088.md#insn-005180c8) · [`005180f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518088.md#insn-005180f4)

~~~diff
- 00517f08 ["INT_ADD", "register:40f0:8", ["const:517f08:8", "const:4:8"]]
- 00517f08 ["CALL", null, ["callee:00c596f0:8"]]
+ 00518228 ["INT_ADD", "register:40f0:8", ["const:518228:8", "const:4:8"]]
+ 00518228 ["CALL", null, ["callee:00c596f0:8"]]
- 00517f08 bytes 06021d94
+ 00518228 bytes 32051d94
- 00517da8 ["COPY", "tmp:0:8", ["const:1be:8"]]
- 00517da8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00517da8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00517da8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 005180c8 ["COPY", "tmp:0:8", ["const:28d:8"]]
+ 005180c8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 005180c8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 005180c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00517da8 bytes b5fa0691
+ 005180c8 bytes b5360a91
- 00517dd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517dd4 ["INT_ADD", "register:40f0:8", ["const:517dd4:8", "const:4:8"]]
- 00517dd4 ["CALLIND", null, ["register:0:8"]]
+ 005180f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005180f4 ["INT_ADD", "register:40f0:8", ["const:5180f4:8", "const:4:8"]]
+ 005180f4 ["CALLIND", null, ["register:0:8"]]
- 00517dd4 bytes 00013fd6
+ 005180f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1355b50db21f05fbd0b8af9f1e7c2df7"></a>

### [`005181e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md) → [`00518500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518500.md) _ZN5Botan14Cert_Extension17Basic_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c587e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md) [`00c58950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58950.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 8件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c597a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597a0.md) [`00c597b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597b0.md) [`00c59920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59920.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518560",
      "incomplete_value": false,
      "site": "00518570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ce000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518240",
      "incomplete_value": false,
      "site": "00518250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ce000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 5
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005185b4",
      "incomplete_value": true,
      "site": "005185b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518294",
      "incomplete_value": true,
      "site": "00518294",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "005185f8",
      "incomplete_value": true,
      "site": "005185f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "005182d8",
      "incomplete_value": true,
      "site": "005182d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00518560",
      "PARAM",
      [
        "storage",
        "002ce500",
        null,
        null
      ]
    ],
    [
      "005185a4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005185e8",
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
      "00518560",
      "PARAM",
      [
        "storage",
        "002ce550",
        null,
        null
      ]
    ],
    [
      "005185a4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005185e8",
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

- 旧版 [`00518250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md#insn-00518250) · [`00518294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md#insn-00518294) · [`005182d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md#insn-005182d8)
- 新版 [`00518570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518500.md#insn-00518570) · [`005185b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518500.md#insn-005185b4) · [`005185f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518500.md#insn-005185f8)

~~~diff
- 00518250 ["INT_ADD", "register:40f0:8", ["const:518250:8", "const:4:8"]]
- 00518250 ["CALL", null, ["callee:00c5a500:8"]]
+ 00518570 ["INT_ADD", "register:40f0:8", ["const:518570:8", "const:4:8"]]
+ 00518570 ["CALL", null, ["callee:00c5a500:8"]]
- 00518250 bytes b8041d94
+ 00518570 bytes e4071d94
- 00518294 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518294 ["INT_ADD", "register:40f0:8", ["const:518294:8", "const:4:8"]]
- 00518294 ["CALLIND", null, ["register:0:8"]]
+ 005185b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005185b4 ["INT_ADD", "register:40f0:8", ["const:5185b4:8", "const:4:8"]]
+ 005185b4 ["CALLIND", null, ["register:0:8"]]
- 00518294 bytes 20013fd6
+ 005185b4 bytes 20013fd6
- 005182d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005182d8 ["INT_ADD", "register:40f0:8", ["const:5182d8:8", "const:4:8"]]
- 005182d8 ["CALLIND", null, ["register:0:8"]]
+ 005185f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005185f8 ["INT_ADD", "register:40f0:8", ["const:5185f8:8", "const:4:8"]]
+ 005185f8 ["CALLIND", null, ["register:0:8"]]
- 005182d8 bytes 20013fd6
+ 005185f8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df21b919536f8af0e6ee5102ead2d9a9"></a>

### [`00518354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md) → [`00518674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518674.md) _ZNK5Botan14Cert_Extension17Basic_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59830.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005186b0",
      "incomplete_value": true,
      "site": "005186c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518390",
      "incomplete_value": true,
      "site": "005183a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:416:8"
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
      "definition_site": "005186b4",
      "incomplete_value": true,
      "site": "005186c8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00518394",
      "incomplete_value": true,
      "site": "005183a8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005186b8",
      "incomplete_value": true,
      "site": "005186cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00518398",
      "incomplete_value": true,
      "site": "005183ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005186b0",
      "READ",
      [
        "storage",
        "002bb416",
        null,
        "string"
      ]
    ],
    [
      "005186b4",
      "READ",
      [
        "storage",
        "002bb423",
        null,
        "string"
      ]
    ],
    [
      "005186b8",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005186b0",
      "READ",
      [
        "storage",
        "002bb4f4",
        null,
        "string"
      ]
    ],
    [
      "005186b4",
      "READ",
      [
        "storage",
        "002bb501",
        null,
        "string"
      ]
    ],
    [
      "005186b8",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md#insn-00518380) · [`00518388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md#insn-00518388) · [`0051838c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md#insn-0051838c)
- 新版 [`005186a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518674.md#insn-005186a0) · [`005186a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518674.md#insn-005186a8)

~~~diff
- 00518380 ["INT_ADD", "register:40f0:8", ["const:518380:8", "const:4:8"]]
- 00518380 ["CALL", null, ["callee:00c58f30:8"]]
+ 005186a0 ["INT_ADD", "register:40f0:8", ["const:5186a0:8", "const:4:8"]]
+ 005186a0 ["CALL", null, ["callee:00c58f30:8"]]
- 00518380 bytes f8fe1c94
+ 005186a0 bytes 24021d94
- 00518388 ["COPY", "tmp:0:8", ["const:416:8"]]
- 00518388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00518388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00518388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005186a8 ["COPY", "tmp:0:8", ["const:4f4:8"]]
+ 005186a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005186a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005186a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00518388 bytes 08591091
+ 005186a8 bytes 08d11391
- 0051838c ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0051838c bytes 49edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4681c2e3c4781da433ff08c968ca4ac5"></a>

### [`005184d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md) → [`005187f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/005187f8.md) _ZNK5Botan14Cert_Extension9Key_Usage12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

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
      "definition_site": "00518ac0",
      "incomplete_value": false,
      "site": "00518ac8",
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
            "const:d45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005187a0",
      "incomplete_value": false,
      "site": "005187a8",
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
            "const:c6e:8"
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
      "definition_site": "00518af8",
      "incomplete_value": true,
      "site": "00518b04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005187d8",
      "incomplete_value": true,
      "site": "005187e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518af4",
      "incomplete_value": false,
      "site": "00518b04",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "005187d4",
      "incomplete_value": false,
      "site": "005187e4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00518ac0",
      "PARAM",
      [
        "storage",
        "002b0c6e",
        null,
        "string"
      ]
    ],
    [
      "00518af4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00518af8",
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
      "00518ac0",
      "PARAM",
      [
        "storage",
        "002b0d45",
        null,
        "string"
      ]
    ],
    [
      "00518af4",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00518af8",
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

- 旧版 [`005187a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md#insn-005187a8) · [`005187e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md#insn-005187e4) · [`0051853c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md#insn-0051853c)
- 新版 [`00518ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/005187f8.md#insn-00518ac8) · [`00518b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/005187f8.md#insn-00518b04) · [`0051885c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/005187f8.md#insn-0051885c)

~~~diff
- 005187a8 ["INT_ADD", "register:40f0:8", ["const:5187a8:8", "const:4:8"]]
- 005187a8 ["CALL", null, ["callee:0043e138:8"]]
+ 00518ac8 ["INT_ADD", "register:40f0:8", ["const:518ac8:8", "const:4:8"]]
+ 00518ac8 ["CALL", null, ["callee:0043e138:8"]]
- 005187a8 bytes 9c95fc97
+ 00518ac8 bytes 9c95fc97
- 005187e4 ["INT_ADD", "register:40f0:8", ["const:5187e4:8", "const:4:8"]]
- 005187e4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00518b04 ["INT_ADD", "register:40f0:8", ["const:518b04:8", "const:4:8"]]
+ 00518b04 ["CALL", null, ["callee:00c58fb0:8"]]
- 005187e4 bytes fffd1c94
+ 00518b04 bytes 2b011d94
- 0051853c ["INT_ADD", "register:40f0:8", ["const:51853c:8", "const:4:8"]]
- 0051853c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051885c ["INT_ADD", "register:40f0:8", ["const:51885c:8", "const:4:8"]]
+ 0051885c ["CALL", null, ["callee:00c58f30:8"]]
- 0051853c bytes 89fe1c94
+ 0051885c bytes b5011d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-311f94f1f93eb9754bed5559733b2d55"></a>

### [`005188ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md) → [`00518bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518bcc.md) _ZN5Botan14Cert_Extension9Key_Usage12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 11件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.14% / 新版 91.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518e84",
      "incomplete_value": true,
      "site": "00518e84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518b64",
      "incomplete_value": true,
      "site": "00518b64",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518ec8",
      "incomplete_value": true,
      "site": "00518ec8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518ba8",
      "incomplete_value": true,
      "site": "00518ba8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00518f08",
      "incomplete_value": false,
      "site": "00518f10",
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
            "const:9c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518be8",
      "incomplete_value": false,
      "site": "00518bf0",
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
            "const:8fa:8"
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
      "00518cb8",
      "READ",
      [
        "storage",
        "002c22f0",
        null,
        null
      ]
    ],
    [
      "00518cc0",
      "READ",
      [
        "storage",
        "002c24a0",
        null,
        null
      ]
    ],
    [
      "00518cc8",
      "READ",
      [
        "storage",
        "002c2880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00518cb8",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "00518cc0",
      "READ",
      [
        "storage",
        "002c24f0",
        null,
        null
      ]
    ],
    [
      "00518cc8",
      "READ",
      [
        "storage",
        "002c28d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md#insn-00518b64) · [`00518ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md#insn-00518ba8) · [`00518bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md#insn-00518bf0)
- 新版 [`00518e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518bcc.md#insn-00518e84) · [`00518ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518bcc.md#insn-00518ec8) · [`00518f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00518/00518bcc.md#insn-00518f10)

~~~diff
- 00518b64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518b64 ["INT_ADD", "register:40f0:8", ["const:518b64:8", "const:4:8"]]
- 00518b64 ["CALLIND", null, ["register:0:8"]]
+ 00518e84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518e84 ["INT_ADD", "register:40f0:8", ["const:518e84:8", "const:4:8"]]
+ 00518e84 ["CALLIND", null, ["register:0:8"]]
- 00518b64 bytes 20013fd6
+ 00518e84 bytes 20013fd6
- 00518ba8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518ba8 ["INT_ADD", "register:40f0:8", ["const:518ba8:8", "const:4:8"]]
- 00518ba8 ["CALLIND", null, ["register:0:8"]]
+ 00518ec8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518ec8 ["INT_ADD", "register:40f0:8", ["const:518ec8:8", "const:4:8"]]
+ 00518ec8 ["CALLIND", null, ["register:0:8"]]
- 00518ba8 bytes 20013fd6
+ 00518ec8 bytes 20013fd6
- 00518bf0 ["INT_ADD", "register:40f0:8", ["const:518bf0:8", "const:4:8"]]
- 00518bf0 ["CALL", null, ["callee:0043e138:8"]]
+ 00518f10 ["INT_ADD", "register:40f0:8", ["const:518f10:8", "const:4:8"]]
+ 00518f10 ["CALL", null, ["callee:0043e138:8"]]
- 00518bf0 bytes 8a94fc97
+ 00518f10 bytes 8a94fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c92fc19680f66058cdba41f776c0e34"></a>

### [`00518d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md) → [`00519080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519080.md) _ZNK5Botan14Cert_Extension9Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59830.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005190b8",
      "incomplete_value": true,
      "site": "005190b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518d98",
      "incomplete_value": true,
      "site": "00518d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b89:8"
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
      "definition_site": "005190b0",
      "incomplete_value": true,
      "site": "005190bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00518d90",
      "incomplete_value": true,
      "site": "00518d9c",
      "value": [
        "LOAD",
        "8",
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
      "005190a0",
      "READ",
      [
        "storage",
        "002a9b89",
        null,
        "string"
      ]
    ],
    [
      "005190b0",
      "READ",
      [
        "storage",
        "002a9b90",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005190a0",
      "READ",
      [
        "storage",
        "002a9c56",
        null,
        "string"
      ]
    ],
    [
      "005190b0",
      "READ",
      [
        "storage",
        "002a9c5d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md#insn-00518d78) · [`00518dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md#insn-00518dac) · [`00518dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md#insn-00518dbc)
- 新版 [`00519098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519080.md#insn-00519098) · [`005190cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519080.md#insn-005190cc) · [`005190dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519080.md#insn-005190dc)

~~~diff
- 00518d78 ["COPY", "tmp:0:8", ["const:b89:8"]]
- 00518d78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00518d78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00518d78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00519098 ["COPY", "tmp:0:8", ["const:c56:8"]]
+ 00519098 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00519098 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00519098 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00518d78 bytes 29252e91
+ 00519098 bytes 29593191
- 00518dac ["INT_ADD", "register:40f0:8", ["const:518dac:8", "const:4:8"]]
- 00518dac ["CALL", null, ["callee:00c59830:8"]]
+ 005190cc ["INT_ADD", "register:40f0:8", ["const:5190cc:8", "const:4:8"]]
+ 005190cc ["CALL", null, ["callee:00c59830:8"]]
- 00518dac bytes adfe1c94
+ 005190cc bytes d9011d94
- 00518dbc ["INT_ADD", "register:40f0:8", ["const:518dbc:8", "const:4:8"]]
- 00518dbc ["CALL", null, ["callee:004ff500:8"]]
+ 005190dc ["INT_ADD", "register:40f0:8", ["const:5190dc:8", "const:4:8"]]
+ 005190dc ["CALL", null, ["callee:004ff500:8"]]
- 00518dbc bytes 0999ff97
+ 005190dc bytes 0999ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f310bfe855a150e3f559059d4ca122"></a>

### [`00519030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md) → [`00519350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519350.md) _ZNK5Botan14Cert_Extension14Subject_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5ab90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051938c",
      "incomplete_value": true,
      "site": "0051939c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051906c",
      "incomplete_value": true,
      "site": "0051907c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a66:8"
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
      "definition_site": "00519390",
      "incomplete_value": true,
      "site": "005193a0",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00519070",
      "incomplete_value": true,
      "site": "00519080",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
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
      "definition_site": "00519394",
      "incomplete_value": true,
      "site": "005193a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00519074",
      "incomplete_value": true,
      "site": "00519084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c0:8"
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
      "0051938c",
      "READ",
      [
        "storage",
        "002b2a66",
        null,
        "string"
      ]
    ],
    [
      "00519390",
      "READ",
      [
        "storage",
        "002b2a71",
        null,
        "string"
      ]
    ],
    [
      "00519394",
      "READ",
      [
        "storage",
        "002c26c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051938c",
      "READ",
      [
        "storage",
        "002b2ab0",
        null,
        "string"
      ]
    ],
    [
      "00519390",
      "READ",
      [
        "storage",
        "002b2abb",
        null,
        "string"
      ]
    ],
    [
      "00519394",
      "READ",
      [
        "storage",
        "002c2710",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051905c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md#insn-0051905c) · [`00519064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md#insn-00519064) · [`00519068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md#insn-00519068)
- 新版 [`0051937c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519350.md#insn-0051937c) · [`00519384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519350.md#insn-00519384)

~~~diff
- 0051905c ["INT_ADD", "register:40f0:8", ["const:51905c:8", "const:4:8"]]
- 0051905c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051937c ["INT_ADD", "register:40f0:8", ["const:51937c:8", "const:4:8"]]
+ 0051937c ["CALL", null, ["callee:00c58f30:8"]]
- 0051905c bytes c1fb1c94
+ 0051937c bytes edfe1c94
- 00519064 ["COPY", "tmp:0:8", ["const:a66:8"]]
- 00519064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00519064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00519064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00519384 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00519384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00519384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00519384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00519064 bytes 08992991
+ 00519384 bytes 08c12a91
- 00519068 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00519068 bytes 49edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0023a871cf1373edfc1f9cbe028efc63"></a>

### [`00519100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md) → [`00519420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519420.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e10.md) · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5ade0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ade0.md) · 呼出先 7件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00519460",
      "incomplete_value": true,
      "site": "00519468",
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
      "definition_site": "00519140",
      "incomplete_value": true,
      "site": "00519148",
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
      "0051945c",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00519468",
      "DATA",
      [
        "storage",
        "00c67af8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0051945c",
      "READ",
      [
        "storage",
        "00c9c250",
        null,
        "pointer"
      ]
    ],
    [
      "00519468",
      "DATA",
      [
        "storage",
        "00c68ac8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00519124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md#insn-00519124) · [`0051913c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md#insn-0051913c) · [`00519164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md#insn-00519164)
- 新版 [`00519444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519420.md#insn-00519444) · [`0051945c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519420.md#insn-0051945c) · [`00519484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519420.md#insn-00519484)

~~~diff
- 00519124 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00519444 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00519124 bytes 093c00d0
+ 00519444 bytes 093c00f0
- 0051913c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:280:8"]]
- 0051913c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051945c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:250:8"]]
+ 0051945c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0051913c bytes 294141f9
+ 0051945c bytes 292941f9
- 00519164 ["INT_ADD", "register:40f0:8", ["const:519164:8", "const:4:8"]]
- 00519164 ["CALL", null, ["callee:00c59f10:8"]]
+ 00519484 ["INT_ADD", "register:40f0:8", ["const:519484:8", "const:4:8"]]
+ 00519484 ["CALL", null, ["callee:00c59f10:8"]]
- 00519164 bytes 77ff1c94
+ 00519484 bytes a3021d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e5e02c5593056e4d396a9f25a9ea4d4"></a>

### [`00519460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md) → [`00519780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519780.md) _ZN5Botan14Cert_Extension16Authority_Key_ID12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0050acf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050acf8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c58950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58950.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0050b018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b018.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c597a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597a0.md) [`00c59920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59920.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00519814",
      "incomplete_value": true,
      "site": "00519814",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005194f4",
      "incomplete_value": true,
      "site": "005194f4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00519858",
      "incomplete_value": true,
      "site": "00519858",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00519538",
      "incomplete_value": true,
      "site": "00519538",
      "value": [
        "LOAD",
        "8",
        [
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
      "00519804",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00519848",
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
      "00519804",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00519848",
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

- 旧版 [`005194f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md#insn-005194f4) · [`00519538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md#insn-00519538) · [`00519488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md#insn-00519488)
- 新版 [`00519814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519780.md#insn-00519814) · [`00519858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519780.md#insn-00519858) · [`005197a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/00519780.md#insn-005197a8)

~~~diff
- 005194f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005194f4 ["INT_ADD", "register:40f0:8", ["const:5194f4:8", "const:4:8"]]
- 005194f4 ["CALLIND", null, ["register:0:8"]]
+ 00519814 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00519814 ["INT_ADD", "register:40f0:8", ["const:519814:8", "const:4:8"]]
+ 00519814 ["CALLIND", null, ["register:0:8"]]
- 005194f4 bytes 20013fd6
+ 00519814 bytes 20013fd6
- 00519538 ["COPY", "register:0:8", ["register:4048:8"]]
- 00519538 ["INT_ADD", "register:40f0:8", ["const:519538:8", "const:4:8"]]
- 00519538 ["CALLIND", null, ["register:0:8"]]
+ 00519858 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00519858 ["INT_ADD", "register:40f0:8", ["const:519858:8", "const:4:8"]]
+ 00519858 ["CALLIND", null, ["register:0:8"]]
- 00519538 bytes 20013fd6
+ 00519858 bytes 20013fd6
- 00519488 ["INT_ADD", "register:40f0:8", ["const:519488:8", "const:4:8"]]
- 00519488 ["CALL", null, ["callee:00c59920:8"]]
+ 005197a8 ["INT_ADD", "register:40f0:8", ["const:5197a8:8", "const:4:8"]]
+ 005197a8 ["CALL", null, ["callee:00c59920:8"]]
- 00519488 bytes 32fd1c94
+ 005197a8 bytes 5e001d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ac0b8d60665496eaa07ad64b10c925"></a>

### [`005195a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md) → [`005198c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/005198c8.md) _ZNK5Botan14Cert_Extension16Authority_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5ab90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00519910",
      "incomplete_value": true,
      "site": "00519920",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:571:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005195f0",
      "incomplete_value": true,
      "site": "00519600",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:493:8"
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
      "definition_site": "00519914",
      "incomplete_value": true,
      "site": "00519924",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005195f4",
      "incomplete_value": true,
      "site": "00519604",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00519918",
      "incomplete_value": true,
      "site": "00519928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005195f8",
      "incomplete_value": true,
      "site": "00519608",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00519910",
      "READ",
      [
        "storage",
        "002bc493",
        null,
        "string"
      ]
    ],
    [
      "00519914",
      "READ",
      [
        "storage",
        "002bc4a0",
        null,
        "string"
      ]
    ],
    [
      "00519918",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00519910",
      "READ",
      [
        "storage",
        "002bc571",
        null,
        "string"
      ]
    ],
    [
      "00519914",
      "READ",
      [
        "storage",
        "002bc57e",
        null,
        "string"
      ]
    ],
    [
      "00519918",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005195e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md#insn-005195e0) · [`005195e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md#insn-005195e8) · [`005195ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md#insn-005195ec)
- 新版 [`00519900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/005198c8.md#insn-00519900) · [`00519908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00519/005198c8.md#insn-00519908)

~~~diff
- 005195e0 ["INT_ADD", "register:40f0:8", ["const:5195e0:8", "const:4:8"]]
- 005195e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00519900 ["INT_ADD", "register:40f0:8", ["const:519900:8", "const:4:8"]]
+ 00519900 ["CALL", null, ["callee:00c58f30:8"]]
- 005195e0 bytes 60fa1c94
+ 00519900 bytes 8cfd1c94
- 005195e8 ["COPY", "tmp:0:8", ["const:493:8"]]
- 005195e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005195e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005195e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00519908 ["COPY", "tmp:0:8", ["const:571:8"]]
+ 00519908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00519908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00519908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005195e8 bytes 084d1291
+ 00519908 bytes 08c51591
- 005195ec ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 005195ec bytes 49edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a38b4a4e3d223c534addb03e8db3f00"></a>

### [`0051a088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md) → [`0051a3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a3a8.md) _ZNK5Botan14Cert_Extension18Extended_Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c598a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a3ec",
      "incomplete_value": true,
      "site": "0051a404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:283:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a0cc",
      "incomplete_value": true,
      "site": "0051a0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a5:8"
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
      "definition_site": "0051a3e8",
      "incomplete_value": true,
      "site": "0051a404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051a0c8",
      "incomplete_value": true,
      "site": "0051a0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0051a3e8",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "0051a3ec",
      "READ",
      [
        "storage",
        "002ba1a5",
        null,
        "string"
      ]
    ],
    [
      "0051a3f0",
      "READ",
      [
        "storage",
        "002ba1b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051a3e8",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ],
    [
      "0051a3ec",
      "READ",
      [
        "storage",
        "002ba283",
        null,
        "string"
      ]
    ],
    [
      "0051a3f0",
      "READ",
      [
        "storage",
        "002ba292",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md#insn-0051a0c4) · [`0051a0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md#insn-0051a0c8) · [`0051a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md#insn-0051a108)
- 新版 [`0051a3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a3a8.md#insn-0051a3e4) · [`0051a3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a3a8.md#insn-0051a3e8) · [`0051a428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a3a8.md#insn-0051a428)

~~~diff
- 0051a0c4 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 0051a0c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051a0c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051a0c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051a3e4 ["COPY", "tmp:0:8", ["const:283:8"]]
+ 0051a3e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051a3e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051a3e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051a0c4 bytes 29950691
+ 0051a3e4 bytes 290d0a91
- 0051a0c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:490:8"]]
- 0051a0c8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051a0c8 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051a0c8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051a3e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
+ 0051a3e8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051a3e8 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051a3e8 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051a0c8 bytes 0125c13d
+ 0051a3e8 bytes 0139c13d
- 0051a108 ["INT_ADD", "register:40f0:8", ["const:51a108:8", "const:4:8"]]
- 0051a108 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051a428 ["INT_ADD", "register:40f0:8", ["const:51a428:8", "const:4:8"]]
+ 0051a428 ["CALL", null, ["callee:00c58f30:8"]]
- 0051a108 bytes 96f71c94
+ 0051a428 bytes c2fa1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbddafde437e9c775f550263d1368ed6"></a>

### [`0051a1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md) → [`0051a4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a4f8.md) _ZNK5Botan14Cert_Extension16Name_Constraints12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a538",
      "incomplete_value": true,
      "site": "0051a54c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a218",
      "incomplete_value": true,
      "site": "0051a22c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:600:8"
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
      "definition_site": "0051a53c",
      "incomplete_value": true,
      "site": "0051a550",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a21c",
      "incomplete_value": true,
      "site": "0051a230",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
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
      "definition_site": "0051a540",
      "incomplete_value": true,
      "site": "0051a554",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:820:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a220",
      "incomplete_value": true,
      "site": "0051a234",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7d0:8"
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
      "0051a538",
      "READ",
      [
        "storage",
        "002a5600",
        null,
        "string"
      ]
    ],
    [
      "0051a53c",
      "READ",
      [
        "storage",
        "002a5609",
        null,
        "string"
      ]
    ],
    [
      "0051a540",
      "READ",
      [
        "storage",
        "002c27d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051a538",
      "READ",
      [
        "storage",
        "002a5758",
        null,
        "string"
      ]
    ],
    [
      "0051a53c",
      "READ",
      [
        "storage",
        "002a5761",
        null,
        "string"
      ]
    ],
    [
      "0051a540",
      "READ",
      [
        "storage",
        "002c2820",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md#insn-0051a270) · [`0051a1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md#insn-0051a1fc) · [`0051a208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md#insn-0051a208)
- 新版 [`0051a590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a4f8.md#insn-0051a590) · [`0051a51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a4f8.md#insn-0051a51c) · [`0051a528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a4f8.md#insn-0051a528)

~~~diff
- 0051a270 ["INT_ADD", "register:40f0:8", ["const:51a270:8", "const:4:8"]]
- 0051a270 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051a590 ["INT_ADD", "register:40f0:8", ["const:51a590:8", "const:4:8"]]
+ 0051a590 ["CALL", null, ["callee:00c58fb0:8"]]
- 0051a270 bytes 5cf71c94
+ 0051a590 bytes 88fa1c94
- 0051a1fc ["INT_ADD", "register:40f0:8", ["const:51a1fc:8", "const:4:8"]]
- 0051a1fc ["CALL", null, ["callee:00c58f90:8"]]
+ 0051a51c ["INT_ADD", "register:40f0:8", ["const:51a51c:8", "const:4:8"]]
+ 0051a51c ["CALL", null, ["callee:00c58f90:8"]]
- 0051a1fc bytes 71f71c94
+ 0051a51c bytes 9dfa1c94
- 0051a208 ["INT_ADD", "register:40f0:8", ["const:51a208:8", "const:4:8"]]
- 0051a208 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051a528 ["INT_ADD", "register:40f0:8", ["const:51a528:8", "const:4:8"]]
+ 0051a528 ["CALL", null, ["callee:00c58f30:8"]]
- 0051a208 bytes 56f71c94
+ 0051a528 bytes 82fa1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72eeaa7101c182ba239b1b4e0331a752"></a>

### [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) → [`0051a5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md) _ZN5Botan14Cert_Extension16Name_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 18件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) [`0051abdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md) [`0051ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 18件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0051ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md) [`0051aefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051aefc.md) [`0051b024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b024.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a738",
      "incomplete_value": true,
      "site": "0051a738",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051a418",
      "incomplete_value": true,
      "site": "0051a418",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a764",
      "incomplete_value": true,
      "site": "0051a764",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051a444",
      "incomplete_value": true,
      "site": "0051a444",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a7a8",
      "incomplete_value": true,
      "site": "0051a7a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051a488",
      "incomplete_value": true,
      "site": "0051a488",
      "value": [
        "LOAD",
        "8",
        [
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
      "0051a728",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051a754",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051a798",
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
      "0051a728",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051a754",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051a798",
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

- 旧版 [`0051a418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md#insn-0051a418) · [`0051a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md#insn-0051a444) · [`0051a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md#insn-0051a488)
- 新版 [`0051a738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md#insn-0051a738) · [`0051a764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md#insn-0051a764) · [`0051a7a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051a5e0.md#insn-0051a7a8)

~~~diff
- 0051a418 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a418 ["INT_ADD", "register:40f0:8", ["const:51a418:8", "const:4:8"]]
- 0051a418 ["CALLIND", null, ["register:0:8"]]
+ 0051a738 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a738 ["INT_ADD", "register:40f0:8", ["const:51a738:8", "const:4:8"]]
+ 0051a738 ["CALLIND", null, ["register:0:8"]]
- 0051a418 bytes 20013fd6
+ 0051a738 bytes 20013fd6
- 0051a444 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a444 ["INT_ADD", "register:40f0:8", ["const:51a444:8", "const:4:8"]]
- 0051a444 ["CALLIND", null, ["register:0:8"]]
+ 0051a764 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a764 ["INT_ADD", "register:40f0:8", ["const:51a764:8", "const:4:8"]]
+ 0051a764 ["CALLIND", null, ["register:0:8"]]
- 0051a444 bytes 20013fd6
+ 0051a764 bytes 20013fd6
- 0051a488 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a488 ["INT_ADD", "register:40f0:8", ["const:51a488:8", "const:4:8"]]
- 0051a488 ["CALLIND", null, ["register:0:8"]]
+ 0051a7a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a7a8 ["INT_ADD", "register:40f0:8", ["const:51a7a8:8", "const:4:8"]]
+ 0051a7a8 ["CALLIND", null, ["register:0:8"]]
- 0051a488 bytes 20013fd6
+ 0051a7a8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f064b797344dabc5ab69bf6296c1d900"></a>

### [`0051ae6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md) → [`0051b18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b18c.md) _ZNK5Botan14Cert_Extension16Name_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00509438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md) [`00548298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548298.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00509758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509758.md) [`005485b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005485b8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.50% / 新版 91.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b1e0",
      "incomplete_value": true,
      "site": "0051b1e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051aec0",
      "incomplete_value": true,
      "site": "0051aec4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
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
      "definition_site": "0051b2ac",
      "incomplete_value": true,
      "site": "0051b2b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051af8c",
      "incomplete_value": true,
      "site": "0051af90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a40:8"
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
      "definition_site": "0051b370",
      "incomplete_value": true,
      "site": "0051b378",
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
      "definition_site": "0051b050",
      "incomplete_value": true,
      "site": "0051b058",
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
      "0051b1e0",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ],
    [
      "0051b21c",
      "READ",
      [
        "storage",
        "002a8c72",
        null,
        "string"
      ]
    ],
    [
      "0051b21c",
      "READ",
      [
        "storage",
        "002a8c82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051b1e0",
      "READ",
      [
        "storage",
        "002c2810",
        null,
        null
      ]
    ],
    [
      "0051b21c",
      "READ",
      [
        "storage",
        "002a8dca",
        null,
        "string"
      ]
    ],
    [
      "0051b21c",
      "READ",
      [
        "storage",
        "002a8dda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051aea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md#insn-0051aea4) · [`0051aebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md#insn-0051aebc) · [`0051aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md#insn-0051aec0)
- 新版 [`0051b1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b18c.md#insn-0051b1c4) · [`0051b1dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b18c.md#insn-0051b1dc) · [`0051b1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b18c.md#insn-0051b1e0)

~~~diff
- 0051aea4 ["INT_ADD", "register:40f0:8", ["const:51aea4:8", "const:4:8"]]
- 0051aea4 ["CALL", null, ["callee:00451c10:8"]]
+ 0051b1c4 ["INT_ADD", "register:40f0:8", ["const:51b1c4:8", "const:4:8"]]
+ 0051b1c4 ["CALL", null, ["callee:00451c10:8"]]
- 0051aea4 bytes 93dafc97
+ 0051b1c4 bytes 93dafc97
- 0051aebc ["COPY", "tmp:0:8", ["const:c72:8"]]
- 0051aebc ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 0051aebc ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 0051aebc ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 0051b1dc ["COPY", "tmp:0:8", ["const:dca:8"]]
+ 0051b1dc ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 0051b1dc ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 0051b1dc ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 0051aebc bytes 39cb3191
+ 0051b1dc bytes 392b3791
- 0051aec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c0:8"]]
- 0051aec0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0051aec0 ["COPY", "register:5010:8", ["const:0:8"]]
- 0051aec0 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0051b1e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:810:8"]]
+ 0051b1e0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051b1e0 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0051b1e0 ["COPY", "register:5018:8", ["const:0:8"]]
- 0051aec0 bytes 00f1c13d
+ 0051b1e0 bytes 0005c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43e7cf90360482cf4fe445e7ab9f03bf"></a>

### [`0051b15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md) → [`0051b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b47c.md) _ZN5Botan14Cert_Extension16Name_Constraints8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocatorIS8_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) [`0054cbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054cbdc.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00540c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md) [`0054cefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054c/0054cefc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b664",
      "incomplete_value": true,
      "site": "0051b664",
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
      "definition_site": "0051b344",
      "incomplete_value": true,
      "site": "0051b344",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b664",
      "incomplete_value": true,
      "site": "0051b664",
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
      "definition_site": "0051b344",
      "incomplete_value": true,
      "site": "0051b344",
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
      "definition_site": "0051b6ec",
      "incomplete_value": true,
      "site": "0051b6ec",
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
      "definition_site": "0051b3cc",
      "incomplete_value": true,
      "site": "0051b3cc",
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
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051b4f4",
      "READ",
      [
        "storage",
        "002a5433",
        null,
        "string"
      ]
    ],
    [
      "0051b4f8",
      "READ",
      [
        "storage",
        "002a5441",
        null,
        "string"
      ]
    ],
    [
      "0051b5f0",
      "READ",
      [
        "storage",
        "002a5433",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051b4f4",
      "READ",
      [
        "storage",
        "002a558b",
        null,
        "string"
      ]
    ],
    [
      "0051b4f8",
      "READ",
      [
        "storage",
        "002a5599",
        null,
        "string"
      ]
    ],
    [
      "0051b5f0",
      "READ",
      [
        "storage",
        "002a558b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051b1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md#insn-0051b1c0) · [`0051b1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md#insn-0051b1cc) · [`0051b1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md#insn-0051b1f8)
- 新版 [`0051b4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b47c.md#insn-0051b4e0) · [`0051b4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b47c.md#insn-0051b4ec) · [`0051b518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b47c.md#insn-0051b518)

~~~diff
- 0051b1c0 ["INT_ADD", "register:40f0:8", ["const:51b1c0:8", "const:4:8"]]
- 0051b1c0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 0051b4e0 ["INT_ADD", "register:40f0:8", ["const:51b4e0:8", "const:4:8"]]
+ 0051b4e0 ["CALL", null, ["callee:00c5aa90:8"]]
- 0051b1c0 bytes 40fa1c94
+ 0051b4e0 bytes 6cfd1c94
- 0051b1cc ["COPY", "tmp:0:8", ["const:433:8"]]
- 0051b1cc ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0051b1cc ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0051b1cc ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0051b4ec ["COPY", "tmp:0:8", ["const:58b:8"]]
+ 0051b4ec ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051b4ec ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051b4ec ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0051b1cc bytes 94ce1091
+ 0051b4ec bytes 942e1691
- 0051b1f8 ["INT_ADD", "register:40f0:8", ["const:51b1f8:8", "const:4:8"]]
- 0051b1f8 ["CALL", null, ["callee:00c5aef0:8"]]
+ 0051b518 ["INT_ADD", "register:40f0:8", ["const:51b518:8", "const:4:8"]]
+ 0051b518 ["CALL", null, ["callee:00c5aef0:8"]]
- 0051b1f8 bytes 4afb1c94
+ 0051b518 bytes 76fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f4bedd051eee262f5870a07c6a5e182"></a>

### [`0051bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md) → [`0051be48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051be48.md) _ZNK5Botan14Cert_Extension20Certificate_Policies12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0054cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054cc60.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`0054cf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054c/0054cf80.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051beb4",
      "incomplete_value": true,
      "site": "0051bebc",
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
      "definition_site": "0051bb94",
      "incomplete_value": true,
      "site": "0051bb9c",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051bed8",
      "incomplete_value": true,
      "site": "0051bed8",
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
      "definition_site": "0051bbb8",
      "incomplete_value": true,
      "site": "0051bbb8",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0051c00c",
      "incomplete_value": true,
      "site": "0051c00c",
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
      "definition_site": "0051bcec",
      "incomplete_value": true,
      "site": "0051bcec",
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
      "0051be98",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0051bebc",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051bec8",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051be98",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "0051bebc",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051bec8",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051bba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md#insn-0051bba4) · [`0051bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md#insn-0051bec4) · [`0051bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md#insn-0051bb70)
- 新版 [`0051bec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051be48.md#insn-0051bec4) · [`0051c1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051be48.md#insn-0051c1e4) · [`0051be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051be48.md#insn-0051be90)

~~~diff
- 0051bba4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0051bec4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0051bba4 bytes e83b00f0
+ 0051bec4 bytes 083c0090
- 0051bec4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051bec4 ["INT_ADD", "register:40f0:8", ["const:51bec4:8", "const:4:8"]]
- 0051bec4 ["CALLIND", null, ["register:0:8"]]
+ 0051c1e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051c1e4 ["INT_ADD", "register:40f0:8", ["const:51c1e4:8", "const:4:8"]]
+ 0051c1e4 ["CALLIND", null, ["register:0:8"]]
- 0051bec4 bytes 20013fd6
+ 0051c1e4 bytes 20013fd6
- 0051bb70 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0051be90 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0051bb70 bytes e93b00f0
+ 0051be90 bytes 093c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f1e4b22142dd4a230b816694df092e"></a>

### [`0051c0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md) → [`0051c3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051c3c8.md) _ZN5Botan14Cert_Extension20Certificate_Policies12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053da4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053da4c.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`0053dd6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053dd6c.md) [`0054bca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bca4.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051c450",
      "incomplete_value": true,
      "site": "0051c450",
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
      "definition_site": "0051c130",
      "incomplete_value": true,
      "site": "0051c130",
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051c6e4",
      "incomplete_value": true,
      "site": "0051c6e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "0051c3c4",
      "incomplete_value": true,
      "site": "0051c3c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051c728",
      "incomplete_value": true,
      "site": "0051c728",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "definition_site": "0051c408",
      "incomplete_value": true,
      "site": "0051c408",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
      "0051c430",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0051c450",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051c47c",
      "DATA",
      [
        "storage",
        "00c6a558",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051c430",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "0051c450",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051c47c",
      "DATA",
      [
        "storage",
        "00c6b528",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051c0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md#insn-0051c0e8) · [`0051c3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md#insn-0051c3c4) · [`0051c408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md#insn-0051c408)
- 新版 [`0051c408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051c3c8.md#insn-0051c408) · [`0051c6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051c3c8.md#insn-0051c6e4) · [`0051c728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051c3c8.md#insn-0051c728)

~~~diff
- 0051c0e8 ["INT_ADD", "register:40f0:8", ["const:51c0e8:8", "const:4:8"]]
- 0051c0e8 ["CALL", null, ["callee:00c59920:8"]]
+ 0051c408 ["INT_ADD", "register:40f0:8", ["const:51c408:8", "const:4:8"]]
+ 0051c408 ["CALL", null, ["callee:00c59920:8"]]
- 0051c0e8 bytes 1af21c94
+ 0051c408 bytes 46f51c94
- 0051c3c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051c3c4 ["INT_ADD", "register:40f0:8", ["const:51c3c4:8", "const:4:8"]]
- 0051c3c4 ["CALLIND", null, ["register:0:8"]]
+ 0051c6e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051c6e4 ["INT_ADD", "register:40f0:8", ["const:51c6e4:8", "const:4:8"]]
+ 0051c6e4 ["CALLIND", null, ["register:0:8"]]
- 0051c3c4 bytes 20013fd6
+ 0051c6e4 bytes 20013fd6
- 0051c408 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051c408 ["INT_ADD", "register:40f0:8", ["const:51c408:8", "const:4:8"]]
- 0051c408 ["CALLIND", null, ["register:0:8"]]
+ 0051c728 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051c728 ["INT_ADD", "register:40f0:8", ["const:51c728:8", "const:4:8"]]
+ 0051c728 ["CALLIND", null, ["register:0:8"]]
- 0051c408 bytes 20013fd6
+ 0051c728 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73eb1398af237b7597dcdfd41a9668e5"></a>

### [`0051c6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md) → [`0051ca1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ca1c.md) _ZNK5Botan14Cert_Extension20Certificate_Policies11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c598a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c598a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.04% / 新版 91.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ca5c",
      "incomplete_value": true,
      "site": "0051ca70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c73c",
      "incomplete_value": true,
      "site": "0051c750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:78b:8"
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
      "definition_site": "0051ca58",
      "incomplete_value": true,
      "site": "0051ca70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c738",
      "incomplete_value": true,
      "site": "0051c750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ad0:8"
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
      "definition_site": "0051ca74",
      "incomplete_value": true,
      "site": "0051ca78",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c754",
      "incomplete_value": true,
      "site": "0051c758",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
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
      "0051ca58",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ],
    [
      "0051ca5c",
      "READ",
      [
        "storage",
        "002ae78b",
        null,
        "string"
      ]
    ],
    [
      "0051ca74",
      "READ",
      [
        "storage",
        "002ae795",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051ca58",
      "READ",
      [
        "storage",
        "002c2b20",
        null,
        null
      ]
    ],
    [
      "0051ca5c",
      "READ",
      [
        "storage",
        "002ae858",
        null,
        "string"
      ]
    ],
    [
      "0051ca74",
      "READ",
      [
        "storage",
        "002ae862",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md#insn-0051c734) · [`0051c738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md#insn-0051c738) · [`0051c77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md#insn-0051c77c)
- 新版 [`0051ca54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ca1c.md#insn-0051ca54) · [`0051ca58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ca1c.md#insn-0051ca58) · [`0051ca9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ca1c.md#insn-0051ca9c)

~~~diff
- 0051c734 ["COPY", "tmp:0:8", ["const:78b:8"]]
- 0051c734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051c734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051c734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051ca54 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0051ca54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051ca54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051ca54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051c734 bytes 292d1e91
+ 0051ca54 bytes 29612191
- 0051c738 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad0:8"]]
- 0051c738 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051c738 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051c738 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051ca58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b20:8"]]
+ 0051ca58 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051ca58 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051ca58 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051c738 bytes 01b5c23d
+ 0051ca58 bytes 01c9c23d
- 0051c77c ["INT_ADD", "register:40f0:8", ["const:51c77c:8", "const:4:8"]]
- 0051c77c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051ca9c ["INT_ADD", "register:40f0:8", ["const:51ca9c:8", "const:4:8"]]
+ 0051ca9c ["CALL", null, ["callee:00c58f30:8"]]
- 0051c77c bytes f9ed1c94
+ 0051ca9c bytes 25f11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38653228d51361155ef8798b13171c1f"></a>

### [`0051caf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md) → [`0051ce10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ce10.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ce90",
      "incomplete_value": true,
      "site": "0051ce90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cb70",
      "incomplete_value": true,
      "site": "0051cb70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f9c:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051cf84",
      "incomplete_value": true,
      "site": "0051cf84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051cc64",
      "incomplete_value": true,
      "site": "0051cc64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0051ce80",
      "READ",
      [
        "storage",
        "002b5f9c",
        null,
        "string"
      ]
    ],
    [
      "0051cf74",
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
      "0051ce80",
      "READ",
      [
        "storage",
        "002b606b",
        null,
        "string"
      ]
    ],
    [
      "0051cf74",
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

- 旧版 [`0051cc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md#insn-0051cc64) · [`0051cb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md#insn-0051cb24) · [`0051cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md#insn-0051cb40)
- 新版 [`0051cf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ce10.md#insn-0051cf84) · [`0051ce44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ce10.md#insn-0051ce44) · [`0051ce60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051ce10.md#insn-0051ce60)

~~~diff
- 0051cc64 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cc64 ["INT_ADD", "register:40f0:8", ["const:51cc64:8", "const:4:8"]]
- 0051cc64 ["CALLIND", null, ["register:0:8"]]
+ 0051cf84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051cf84 ["INT_ADD", "register:40f0:8", ["const:51cf84:8", "const:4:8"]]
+ 0051cf84 ["CALLIND", null, ["register:0:8"]]
- 0051cc64 bytes 20013fd6
+ 0051cf84 bytes 20013fd6
- 0051cb24 ["INT_ADD", "register:40f0:8", ["const:51cb24:8", "const:4:8"]]
- 0051cb24 ["CALL", null, ["callee:00c5aa00:8"]]
+ 0051ce44 ["INT_ADD", "register:40f0:8", ["const:51ce44:8", "const:4:8"]]
+ 0051ce44 ["CALL", null, ["callee:00c5aa00:8"]]
- 0051cb24 bytes c3f31c94
+ 0051ce44 bytes eff61c94
- 0051cb40 ["INT_ADD", "register:40f0:8", ["const:51cb40:8", "const:4:8"]]
- 0051cb40 ["CALL", null, ["callee:00c59750:8"]]
+ 0051ce60 ["INT_ADD", "register:40f0:8", ["const:51ce60:8", "const:4:8"]]
+ 0051ce60 ["CALL", null, ["callee:00c59750:8"]]
- 0051cb40 bytes 10ef1c94
+ 0051ce60 bytes 3cf21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7edc8ba635a48e80aba90709cdc16d47"></a>

### [`0051cd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md) → [`0051d03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d03c.md) _ZN5Botan14Cert_Extension28Authority_Information_Access12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051d0ec",
      "incomplete_value": true,
      "site": "0051d108",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cdcc",
      "incomplete_value": true,
      "site": "0051cde8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051d0c8",
      "incomplete_value": true,
      "site": "0051d0c8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051cda8",
      "incomplete_value": true,
      "site": "0051cda8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d368",
      "incomplete_value": true,
      "site": "0051d368",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051d048",
      "incomplete_value": true,
      "site": "0051d048",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051d0b8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051d0ec",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ],
    [
      "0051d178",
      "READ",
      [
        "storage",
        "002b5f9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051d0b8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051d0ec",
      "READ",
      [
        "storage",
        "002c2810",
        null,
        null
      ]
    ],
    [
      "0051d178",
      "READ",
      [
        "storage",
        "002b606b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051cda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md#insn-0051cda8) · [`0051d048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md#insn-0051d048) · [`0051d30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md#insn-0051d30c)
- 新版 [`0051d0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d03c.md#insn-0051d0c8) · [`0051d368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d03c.md#insn-0051d368) · [`0051d62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d03c.md#insn-0051d62c)

~~~diff
- 0051cda8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cda8 ["INT_ADD", "register:40f0:8", ["const:51cda8:8", "const:4:8"]]
- 0051cda8 ["CALLIND", null, ["register:0:8"]]
+ 0051d0c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d0c8 ["INT_ADD", "register:40f0:8", ["const:51d0c8:8", "const:4:8"]]
+ 0051d0c8 ["CALLIND", null, ["register:0:8"]]
- 0051cda8 bytes 20013fd6
+ 0051d0c8 bytes 20013fd6
- 0051d048 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d048 ["INT_ADD", "register:40f0:8", ["const:51d048:8", "const:4:8"]]
- 0051d048 ["CALLIND", null, ["register:0:8"]]
+ 0051d368 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d368 ["INT_ADD", "register:40f0:8", ["const:51d368:8", "const:4:8"]]
+ 0051d368 ["CALLIND", null, ["register:0:8"]]
- 0051d048 bytes 20013fd6
+ 0051d368 bytes 20013fd6
- 0051d30c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d30c ["INT_ADD", "register:40f0:8", ["const:51d30c:8", "const:4:8"]]
- 0051d30c ["CALLIND", null, ["register:0:8"]]
+ 0051d62c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d62c ["INT_ADD", "register:40f0:8", ["const:51d62c:8", "const:4:8"]]
+ 0051d62c ["CALLIND", null, ["register:0:8"]]
- 0051d30c bytes 20013fd6
+ 0051d62c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd5f51d977d7bf1b867287a0d2dc4232"></a>

### [`0051d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md) → [`0051d868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d868.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.14% / 新版 85.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051d8c8",
      "incomplete_value": true,
      "site": "0051d8c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:22a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d5a8",
      "incomplete_value": true,
      "site": "0051d5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
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
      "definition_site": "0051d8cc",
      "incomplete_value": true,
      "site": "0051d8cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051d5ac",
      "incomplete_value": true,
      "site": "0051d5ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051d904",
      "incomplete_value": true,
      "site": "0051d90c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b57:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d5e4",
      "incomplete_value": true,
      "site": "0051d5ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b0d:8"
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
      "0051d8b8",
      "READ",
      [
        "storage",
        "002c11e0",
        null,
        "string"
      ]
    ],
    [
      "0051d8bc",
      "READ",
      [
        "storage",
        "002c11e6",
        null,
        "string"
      ]
    ],
    [
      "0051d904",
      "READ",
      [
        "storage",
        "002b1b0d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051d8b8",
      "READ",
      [
        "storage",
        "002c122a",
        null,
        "string"
      ]
    ],
    [
      "0051d8bc",
      "READ",
      [
        "storage",
        "002c1230",
        null,
        "string"
      ]
    ],
    [
      "0051d904",
      "READ",
      [
        "storage",
        "002b1b57",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md#insn-0051d590) · [`0051d5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md#insn-0051d5b8) · [`0051d5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md#insn-0051d5c8)
- 新版 [`0051d8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d868.md#insn-0051d8b0) · [`0051d8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d868.md#insn-0051d8d8) · [`0051d8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d868.md#insn-0051d8e8)

~~~diff
- 0051d590 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 0051d590 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051d590 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051d590 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051d8b0 ["COPY", "tmp:0:8", ["const:22a:8"]]
+ 0051d8b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051d8b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051d8b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051d590 bytes 29810791
+ 0051d8b0 bytes 29a90891
- 0051d5b8 ["INT_ADD", "register:40f0:8", ["const:51d5b8:8", "const:4:8"]]
- 0051d5b8 ["CALL", null, ["callee:004ff500:8"]]
+ 0051d8d8 ["INT_ADD", "register:40f0:8", ["const:51d8d8:8", "const:4:8"]]
+ 0051d8d8 ["CALL", null, ["callee:004ff500:8"]]
- 0051d5b8 bytes 0a87ff97
+ 0051d8d8 bytes 0a87ff97
- 0051d5c8 ["INT_ADD", "register:40f0:8", ["const:51d5c8:8", "const:4:8"]]
- 0051d5c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 0051d8e8 ["INT_ADD", "register:40f0:8", ["const:51d8e8:8", "const:4:8"]]
+ 0051d8e8 ["CALL", null, ["callee:00c58f50:8"]]
- 0051d5c8 bytes 6eea1c94
+ 0051d8e8 bytes 9aed1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30397fe092761926bf5e81d7a528dd0c"></a>

### [`0051d6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md) → [`0051d9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d9c0.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e80.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5ae50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae50.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "definition_site": "0051da24",
      "incomplete_value": false,
      "site": "0051da2c",
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
            "const:b07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d704",
      "incomplete_value": false,
      "site": "0051d70c",
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
            "const:a30:8"
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
      "definition_site": "0051da60",
      "incomplete_value": true,
      "site": "0051da6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051d740",
      "incomplete_value": true,
      "site": "0051d74c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051da5c",
      "incomplete_value": false,
      "site": "0051da6c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0051d73c",
      "incomplete_value": false,
      "site": "0051d74c",
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
      "0051da24",
      "PARAM",
      [
        "storage",
        "002afa30",
        null,
        "string"
      ]
    ],
    [
      "0051da5c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0051da60",
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
      "0051da24",
      "PARAM",
      [
        "storage",
        "002afb07",
        null,
        "string"
      ]
    ],
    [
      "0051da5c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0051da60",
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

- 旧版 [`0051d70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md#insn-0051d70c) · [`0051d74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md#insn-0051d74c) · [`0051d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md#insn-0051d6f8)
- 新版 [`0051da2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d9c0.md#insn-0051da2c) · [`0051da6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d9c0.md#insn-0051da6c) · [`0051da18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051d9c0.md#insn-0051da18)

~~~diff
- 0051d70c ["INT_ADD", "register:40f0:8", ["const:51d70c:8", "const:4:8"]]
- 0051d70c ["CALL", null, ["callee:0043e138:8"]]
+ 0051da2c ["INT_ADD", "register:40f0:8", ["const:51da2c:8", "const:4:8"]]
+ 0051da2c ["CALL", null, ["callee:0043e138:8"]]
- 0051d70c bytes c381fc97
+ 0051da2c bytes c381fc97
- 0051d74c ["INT_ADD", "register:40f0:8", ["const:51d74c:8", "const:4:8"]]
- 0051d74c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051da6c ["INT_ADD", "register:40f0:8", ["const:51da6c:8", "const:4:8"]]
+ 0051da6c ["CALL", null, ["callee:00c58fb0:8"]]
- 0051d74c bytes 25ea1c94
+ 0051da6c bytes 51ed1c94
- 0051d6f8 ["INT_ADD", "register:40f0:8", ["const:51d6f8:8", "const:4:8"]]
- 0051d6f8 ["CALL", null, ["callee:00c58f90:8"]]
+ 0051da18 ["INT_ADD", "register:40f0:8", ["const:51da18:8", "const:4:8"]]
+ 0051da18 ["CALL", null, ["callee:00c58f90:8"]]
- 0051d6f8 bytes 32ea1c94
+ 0051da18 bytes 5eed1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8522c36a91ed34b5fb82ad30d4a7e82"></a>

### [`0051d7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md) → [`0051dac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dac0.md) _ZNK5Botan14Cert_Extension10CRL_Number4copyEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "definition_site": "0051db08",
      "incomplete_value": true,
      "site": "0051db10",
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
      "definition_site": "0051d7e8",
      "incomplete_value": true,
      "site": "0051d7f0",
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
      "definition_site": "0051db4c",
      "incomplete_value": false,
      "site": "0051db54",
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
            "const:35c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d82c",
      "incomplete_value": false,
      "site": "0051d834",
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
            "const:28d:8"
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
      "definition_site": "0051db88",
      "incomplete_value": true,
      "site": "0051db94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051d868",
      "incomplete_value": true,
      "site": "0051d874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051dafc",
      "READ",
      [
        "storage",
        "00c9b270",
        null,
        "pointer"
      ]
    ],
    [
      "0051db10",
      "DATA",
      [
        "storage",
        "00c68d90",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "0051db4c",
      "PARAM",
      [
        "storage",
        "002b828d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051dafc",
      "READ",
      [
        "storage",
        "00c9c240",
        null,
        "pointer"
      ]
    ],
    [
      "0051db10",
      "DATA",
      [
        "storage",
        "00c69d60",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "0051db4c",
      "PARAM",
      [
        "storage",
        "002b835c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md#insn-0051d834) · [`0051d874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md#insn-0051d874) · [`0051d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md#insn-0051d7d0)
- 新版 [`0051db54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dac0.md#insn-0051db54) · [`0051db94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dac0.md#insn-0051db94) · [`0051daf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dac0.md#insn-0051daf0)

~~~diff
- 0051d834 ["INT_ADD", "register:40f0:8", ["const:51d834:8", "const:4:8"]]
- 0051d834 ["CALL", null, ["callee:0043e138:8"]]
+ 0051db54 ["INT_ADD", "register:40f0:8", ["const:51db54:8", "const:4:8"]]
+ 0051db54 ["CALL", null, ["callee:0043e138:8"]]
- 0051d834 bytes 7981fc97
+ 0051db54 bytes 7981fc97
- 0051d874 ["INT_ADD", "register:40f0:8", ["const:51d874:8", "const:4:8"]]
- 0051d874 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051db94 ["INT_ADD", "register:40f0:8", ["const:51db94:8", "const:4:8"]]
+ 0051db94 ["CALL", null, ["callee:00c58fb0:8"]]
- 0051d874 bytes dbe91c94
+ 0051db94 bytes 07ed1c94
- 0051d7d0 ["INT_ADD", "register:40f0:8", ["const:51d7d0:8", "const:4:8"]]
- 0051d7d0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051daf0 ["INT_ADD", "register:40f0:8", ["const:51daf0:8", "const:4:8"]]
+ 0051daf0 ["CALL", null, ["callee:00c58f30:8"]]
- 0051d7d0 bytes e4e91c94
+ 0051daf0 bytes 10ed1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf896ba970261c2cce74205abedd65d2"></a>

### [`0051d8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md) → [`0051dbe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dbe8.md) _ZNK5Botan14Cert_Extension10CRL_Number12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies

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
      "definition_site": "0051dc60",
      "incomplete_value": true,
      "site": "0051dc60",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051d940",
      "incomplete_value": true,
      "site": "0051d940",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051dcd8",
      "incomplete_value": true,
      "site": "0051dcd8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051d9b8",
      "incomplete_value": true,
      "site": "0051d9b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "0051dc50",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051dcc8",
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
      "0051dc50",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051dcc8",
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

- 旧版 [`0051d940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md#insn-0051d940) · [`0051d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md#insn-0051d9b8) · [`0051d904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md#insn-0051d904)
- 新版 [`0051dc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dbe8.md#insn-0051dc60) · [`0051dcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dbe8.md#insn-0051dcd8) · [`0051dc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051dbe8.md#insn-0051dc24)

~~~diff
- 0051d940 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d940 ["INT_ADD", "register:40f0:8", ["const:51d940:8", "const:4:8"]]
- 0051d940 ["CALLIND", null, ["register:0:8"]]
+ 0051dc60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dc60 ["INT_ADD", "register:40f0:8", ["const:51dc60:8", "const:4:8"]]
+ 0051dc60 ["CALLIND", null, ["register:0:8"]]
- 0051d940 bytes 20013fd6
+ 0051dc60 bytes 20013fd6
- 0051d9b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d9b8 ["INT_ADD", "register:40f0:8", ["const:51d9b8:8", "const:4:8"]]
- 0051d9b8 ["CALLIND", null, ["register:0:8"]]
+ 0051dcd8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dcd8 ["INT_ADD", "register:40f0:8", ["const:51dcd8:8", "const:4:8"]]
+ 0051dcd8 ["CALLIND", null, ["register:0:8"]]
- 0051d9b8 bytes 20013fd6
+ 0051dcd8 bytes 20013fd6
- 0051d904 ["INT_ADD", "register:40f0:8", ["const:51d904:8", "const:4:8"]]
- 0051d904 ["CALL", null, ["callee:00c599c0:8"]]
+ 0051dc24 ["INT_ADD", "register:40f0:8", ["const:51dc24:8", "const:4:8"]]
+ 0051dc24 ["CALL", null, ["callee:00c599c0:8"]]
- 0051d904 bytes 3bec1c94
+ 0051dc24 bytes 67ef1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a1d592d4a2e915023e9b77f10b2535f"></a>

### [`0051db0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md) → [`0051de2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051de2c.md) _ZNK5Botan14Cert_Extension10CRL_Number11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59830.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051de4c",
      "incomplete_value": true,
      "site": "0051de68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051db2c",
      "incomplete_value": true,
      "site": "0051db48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
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
      "0051de4c",
      "READ",
      [
        "storage",
        "002ab3a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051de4c",
      "READ",
      [
        "storage",
        "002ab46d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051db24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md#insn-0051db24) · [`0051db50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md#insn-0051db50) · [`0051db60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md#insn-0051db60)
- 新版 [`0051de44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051de2c.md#insn-0051de44) · [`0051de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051de2c.md#insn-0051de70) · [`0051de80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051de2c.md#insn-0051de80)

~~~diff
- 0051db24 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 0051db24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051db24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051db24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051de44 ["COPY", "tmp:0:8", ["const:46d:8"]]
+ 0051de44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051de44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051de44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051db24 bytes 29810e91
+ 0051de44 bytes 29b51191
- 0051db50 ["INT_ADD", "register:40f0:8", ["const:51db50:8", "const:4:8"]]
- 0051db50 ["CALL", null, ["callee:00c59830:8"]]
+ 0051de70 ["INT_ADD", "register:40f0:8", ["const:51de70:8", "const:4:8"]]
+ 0051de70 ["CALL", null, ["callee:00c59830:8"]]
- 0051db50 bytes 44eb1c94
+ 0051de70 bytes 70ee1c94
- 0051db60 ["INT_ADD", "register:40f0:8", ["const:51db60:8", "const:4:8"]]
- 0051db60 ["CALL", null, ["callee:004ff500:8"]]
+ 0051de80 ["INT_ADD", "register:40f0:8", ["const:51de80:8", "const:4:8"]]
+ 0051de80 ["CALL", null, ["callee:004ff500:8"]]
- 0051db60 bytes a085ff97
+ 0051de80 bytes a085ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988d351ce8f7fdf221c6dbfa0ca974cd"></a>

### [`0051dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md) → [`0051df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051df04.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies

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
      "definition_site": "0051df7c",
      "incomplete_value": true,
      "site": "0051df7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051dc5c",
      "incomplete_value": true,
      "site": "0051dc5c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051dff4",
      "incomplete_value": true,
      "site": "0051dff4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051dcd4",
      "incomplete_value": true,
      "site": "0051dcd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "0051df6c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051dfe4",
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
      "0051df6c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051dfe4",
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

- 旧版 [`0051dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md#insn-0051dc5c) · [`0051dcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md#insn-0051dcd4) · [`0051dc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md#insn-0051dc20)
- 新版 [`0051df7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051df04.md#insn-0051df7c) · [`0051dff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051df04.md#insn-0051dff4) · [`0051df40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051d/0051df04.md#insn-0051df40)

~~~diff
- 0051dc5c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dc5c ["INT_ADD", "register:40f0:8", ["const:51dc5c:8", "const:4:8"]]
- 0051dc5c ["CALLIND", null, ["register:0:8"]]
+ 0051df7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051df7c ["INT_ADD", "register:40f0:8", ["const:51df7c:8", "const:4:8"]]
+ 0051df7c ["CALLIND", null, ["register:0:8"]]
- 0051dc5c bytes 20013fd6
+ 0051df7c bytes 20013fd6
- 0051dcd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dcd4 ["INT_ADD", "register:40f0:8", ["const:51dcd4:8", "const:4:8"]]
- 0051dcd4 ["CALLIND", null, ["register:0:8"]]
+ 0051dff4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dff4 ["INT_ADD", "register:40f0:8", ["const:51dff4:8", "const:4:8"]]
+ 0051dff4 ["CALLIND", null, ["register:0:8"]]
- 0051dcd4 bytes 20013fd6
+ 0051dff4 bytes 20013fd6
- 0051dc20 ["INT_ADD", "register:40f0:8", ["const:51dc20:8", "const:4:8"]]
- 0051dc20 ["CALL", null, ["callee:00c599c0:8"]]
+ 0051df40 ["INT_ADD", "register:40f0:8", ["const:51df40:8", "const:4:8"]]
+ 0051df40 ["CALL", null, ["callee:00c599c0:8"]]
- 0051dc20 bytes 74eb1c94
+ 0051df40 bytes a0ee1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cabb3704b00d659b9355a36fb238bfa9"></a>

### [`0051de2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md) → [`0051e14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e14c.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59830.md)

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
      "definition_site": "0051e16c",
      "incomplete_value": true,
      "site": "0051e194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:376:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051de4c",
      "incomplete_value": true,
      "site": "0051de74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a7:8"
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
      "0051e16c",
      "READ",
      [
        "storage",
        "002b82a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051e16c",
      "READ",
      [
        "storage",
        "002b8376",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051de44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md#insn-0051de44) · [`0051de7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md#insn-0051de7c) · [`0051de8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md#insn-0051de8c)
- 新版 [`0051e164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e14c.md#insn-0051e164) · [`0051e19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e14c.md#insn-0051e19c) · [`0051e1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e14c.md#insn-0051e1ac)

~~~diff
- 0051de44 ["COPY", "tmp:0:8", ["const:2a7:8"]]
- 0051de44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0051de44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0051de44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0051e164 ["COPY", "tmp:0:8", ["const:376:8"]]
+ 0051e164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0051e164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0051e164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0051de44 bytes 4a9d0a91
+ 0051e164 bytes 4ad90d91
- 0051de7c ["INT_ADD", "register:40f0:8", ["const:51de7c:8", "const:4:8"]]
- 0051de7c ["CALL", null, ["callee:00c59830:8"]]
+ 0051e19c ["INT_ADD", "register:40f0:8", ["const:51e19c:8", "const:4:8"]]
+ 0051e19c ["CALL", null, ["callee:00c59830:8"]]
- 0051de7c bytes 79ea1c94
+ 0051e19c bytes a5ed1c94
- 0051de8c ["INT_ADD", "register:40f0:8", ["const:51de8c:8", "const:4:8"]]
- 0051de8c ["CALL", null, ["callee:004ff500:8"]]
+ 0051e1ac ["INT_ADD", "register:40f0:8", ["const:51e1ac:8", "const:4:8"]]
+ 0051e1ac ["CALL", null, ["callee:004ff500:8"]]
- 0051de8c bytes d584ff97
+ 0051e1ac bytes d584ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eeb77c1fc612c58338201eeb2360afc"></a>

### [`0051df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md) → [`0051e230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e230.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points12encode_innerEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e274",
      "incomplete_value": true,
      "site": "0051e280",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051df54",
      "incomplete_value": true,
      "site": "0051df60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
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
      "definition_site": "0051e270",
      "incomplete_value": true,
      "site": "0051e284",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051df50",
      "incomplete_value": true,
      "site": "0051df64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
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
      "definition_site": "0051e270",
      "incomplete_value": true,
      "site": "0051e284",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051df50",
      "incomplete_value": true,
      "site": "0051df64",
      "value": [
        "LOAD",
        "16",
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
      "0051e270",
      "READ",
      [
        "storage",
        "002ab4ef",
        null,
        "string"
      ]
    ],
    [
      "0051e270",
      "READ",
      [
        "storage",
        "002ab4ff",
        null,
        "string"
      ]
    ],
    [
      "0051e274",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051e270",
      "READ",
      [
        "storage",
        "002ab5bc",
        null,
        "string"
      ]
    ],
    [
      "0051e270",
      "READ",
      [
        "storage",
        "002ab5cc",
        null,
        "string"
      ]
    ],
    [
      "0051e274",
      "READ",
      [
        "storage",
        "002c2810",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md#insn-0051dfa0) · [`0051df34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md#insn-0051df34) · [`0051df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md#insn-0051df40)
- 新版 [`0051e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e230.md#insn-0051e2c0) · [`0051e254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e230.md#insn-0051e254) · [`0051e260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e230.md#insn-0051e260)

~~~diff
- 0051dfa0 ["INT_ADD", "register:40f0:8", ["const:51dfa0:8", "const:4:8"]]
- 0051dfa0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051e2c0 ["INT_ADD", "register:40f0:8", ["const:51e2c0:8", "const:4:8"]]
+ 0051e2c0 ["CALL", null, ["callee:00c58fb0:8"]]
- 0051dfa0 bytes 10e81c94
+ 0051e2c0 bytes 3ceb1c94
- 0051df34 ["INT_ADD", "register:40f0:8", ["const:51df34:8", "const:4:8"]]
- 0051df34 ["CALL", null, ["callee:00c58f90:8"]]
+ 0051e254 ["INT_ADD", "register:40f0:8", ["const:51e254:8", "const:4:8"]]
+ 0051e254 ["CALL", null, ["callee:00c58f90:8"]]
- 0051df34 bytes 23e81c94
+ 0051e254 bytes 4feb1c94
- 0051df40 ["INT_ADD", "register:40f0:8", ["const:51df40:8", "const:4:8"]]
- 0051df40 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051e260 ["INT_ADD", "register:40f0:8", ["const:51e260:8", "const:4:8"]]
+ 0051e260 ["CALL", null, ["callee:00c58f30:8"]]
- 0051df40 bytes 08e81c94
+ 0051e260 bytes 34eb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8afbdcb8890cd9a573aa5561d4114774"></a>

### [`0051dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md) → [`0051e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e310.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e5dc",
      "incomplete_value": true,
      "site": "0051e5e4",
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
      "definition_site": "0051e2bc",
      "incomplete_value": true,
      "site": "0051e2c4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0051e5ec",
      "incomplete_value": true,
      "site": "0051e5ec",
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
      "definition_site": "0051e2cc",
      "incomplete_value": true,
      "site": "0051e2cc",
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
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e5ec",
      "incomplete_value": true,
      "site": "0051e5ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051e2cc",
      "incomplete_value": true,
      "site": "0051e2cc",
      "value": [
        "LOAD",
        "8",
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
      "0051e38c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051e450",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ],
    [
      "0051e47c",
      "PARAM",
      [
        "storage",
        "002a0f7a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051e38c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e450",
      "PARAM",
      [
        "storage",
        "002bd7f8",
        null,
        null
      ]
    ],
    [
      "0051e47c",
      "PARAM",
      [
        "storage",
        "002a0fba",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md#insn-0051e07c) · [`0051e024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md#insn-0051e024) · [`0051e038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md#insn-0051e038)
- 新版 [`0051e39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e310.md#insn-0051e39c) · [`0051e344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e310.md#insn-0051e344) · [`0051e358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e310.md#insn-0051e358)

~~~diff
- 0051e07c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e07c ["INT_ADD", "register:40f0:8", ["const:51e07c:8", "const:4:8"]]
- 0051e07c ["CALLIND", null, ["register:0:8"]]
+ 0051e39c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e39c ["INT_ADD", "register:40f0:8", ["const:51e39c:8", "const:4:8"]]
+ 0051e39c ["CALLIND", null, ["register:0:8"]]
- 0051e07c bytes 20013fd6
+ 0051e39c bytes 20013fd6
- 0051e024 ["INT_ADD", "register:40f0:8", ["const:51e024:8", "const:4:8"]]
- 0051e024 ["CALL", null, ["callee:00c59920:8"]]
+ 0051e344 ["INT_ADD", "register:40f0:8", ["const:51e344:8", "const:4:8"]]
+ 0051e344 ["CALL", null, ["callee:00c59920:8"]]
- 0051e024 bytes 4bea1c94
+ 0051e344 bytes 77ed1c94
- 0051e038 ["INT_ADD", "register:40f0:8", ["const:51e038:8", "const:4:8"]]
- 0051e038 ["CALL", null, ["callee:00c5af00:8"]]
+ 0051e358 ["INT_ADD", "register:40f0:8", ["const:51e358:8", "const:4:8"]]
+ 0051e358 ["CALL", null, ["callee:00c5af00:8"]]
- 0051e038 bytes beef1c94
+ 0051e358 bytes eaf21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea10a6cb83dcbde944f63131ff733c6"></a>

### [`0051e3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md) → [`0051e6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e6f8.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f30.md) · 呼出先 11件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aae4.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`0053cac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cac8.md) [`0053d5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d5ac.md)
- 新版 呼出元 1件 [`00c5af00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af00.md) · 呼出先 11件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053ae04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ae04.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`0053cde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cde8.md) [`0053d8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d8cc.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e75c",
      "incomplete_value": true,
      "site": "0051e764",
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
      "definition_site": "0051e43c",
      "incomplete_value": true,
      "site": "0051e444",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051e914",
      "incomplete_value": true,
      "site": "0051e914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0051e5f4",
      "incomplete_value": true,
      "site": "0051e5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0051e74c",
      "READ",
      [
        "storage",
        "00c9b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e750",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "0051e764",
      "DATA",
      [
        "storage",
        "00c68ef8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0051e74c",
      "READ",
      [
        "storage",
        "00c9c288",
        null,
        "pointer"
      ]
    ],
    [
      "0051e750",
      "READ",
      [
        "storage",
        "00c9c168",
        null,
        "pointer"
      ]
    ],
    [
      "0051e764",
      "DATA",
      [
        "storage",
        "00c69ec8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md#insn-0051e5f4) · [`0051e41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md#insn-0051e41c) · [`0051e420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md#insn-0051e420)
- 新版 [`0051e914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e6f8.md#insn-0051e914) · [`0051e73c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e6f8.md#insn-0051e73c) · [`0051e740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e6f8.md#insn-0051e740)

~~~diff
- 0051e5f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e5f4 ["INT_ADD", "register:40f0:8", ["const:51e5f4:8", "const:4:8"]]
- 0051e5f4 ["CALLIND", null, ["register:0:8"]]
+ 0051e914 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e914 ["INT_ADD", "register:40f0:8", ["const:51e914:8", "const:4:8"]]
+ 0051e914 ["CALLIND", null, ["register:0:8"]]
- 0051e5f4 bytes 20013fd6
+ 0051e914 bytes 20013fd6
- 0051e41c ["INT_ADD", "register:40f0:8", ["const:51e41c:8", "const:4:8"]]
- 0051e41c ["CALL", null, ["callee:00c597a0:8"]]
+ 0051e73c ["INT_ADD", "register:40f0:8", ["const:51e73c:8", "const:4:8"]]
+ 0051e73c ["CALL", null, ["callee:00c597a0:8"]]
- 0051e41c bytes ede81c94
+ 0051e73c bytes 19ec1c94
- 0051e420 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0051e740 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0051e420 bytes e83b00b0
+ 0051e740 bytes e83b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1e269eac47f6fd212c685054db85266"></a>

### [`0051e6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md) → [`0051e9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e9d4.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ea14",
      "incomplete_value": true,
      "site": "0051ea28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:47c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e6f4",
      "incomplete_value": true,
      "site": "0051e708",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:39e:8"
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
      "0051ea14",
      "READ",
      [
        "storage",
        "002ba39e",
        null,
        "string"
      ]
    ],
    [
      "0051ea18",
      "READ",
      [
        "storage",
        "002ba3ab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051ea14",
      "READ",
      [
        "storage",
        "002ba47c",
        null,
        "string"
      ]
    ],
    [
      "0051ea18",
      "READ",
      [
        "storage",
        "002ba489",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md#insn-0051e6ec) · [`0051e73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md#insn-0051e73c) · [`0051e74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md#insn-0051e74c)
- 新版 [`0051ea0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e9d4.md#insn-0051ea0c) · [`0051ea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e9d4.md#insn-0051ea5c) · [`0051ea6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051e9d4.md#insn-0051ea6c)

~~~diff
- 0051e6ec ["COPY", "tmp:0:8", ["const:39e:8"]]
- 0051e6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0051e6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0051e6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0051ea0c ["COPY", "tmp:0:8", ["const:47c:8"]]
+ 0051ea0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0051ea0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0051ea0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0051e6ec bytes 08790e91
+ 0051ea0c bytes 08f11191
- 0051e73c ["INT_ADD", "register:40f0:8", ["const:51e73c:8", "const:4:8"]]
- 0051e73c ["CALL", null, ["callee:004ff500:8"]]
+ 0051ea5c ["INT_ADD", "register:40f0:8", ["const:51ea5c:8", "const:4:8"]]
+ 0051ea5c ["CALL", null, ["callee:004ff500:8"]]
- 0051e73c bytes a982ff97
+ 0051ea5c bytes a982ff97
- 0051e74c ["INT_ADD", "register:40f0:8", ["const:51e74c:8", "const:4:8"]]
- 0051e74c ["CALL", null, ["callee:00c58f50:8"]]
+ 0051ea6c ["INT_ADD", "register:40f0:8", ["const:51ea6c:8", "const:4:8"]]
+ 0051ea6c ["CALL", null, ["callee:00c58f50:8"]]
- 0051e74c bytes 0de61c94
+ 0051ea6c bytes 39e91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c53c3612694d479ec7e1b913947a74b"></a>

### [`0051e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md) → [`0051ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ead0.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051eb14",
      "incomplete_value": true,
      "site": "0051eb20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e7f4",
      "incomplete_value": true,
      "site": "0051e800",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
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
      "definition_site": "0051eb10",
      "incomplete_value": true,
      "site": "0051eb24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e7f0",
      "incomplete_value": true,
      "site": "0051e804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
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
      "definition_site": "0051eb10",
      "incomplete_value": true,
      "site": "0051eb24",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051e7f0",
      "incomplete_value": true,
      "site": "0051e804",
      "value": [
        "LOAD",
        "16",
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
      "0051eb10",
      "READ",
      [
        "storage",
        "002ab4ef",
        null,
        "string"
      ]
    ],
    [
      "0051eb10",
      "READ",
      [
        "storage",
        "002ab4ff",
        null,
        "string"
      ]
    ],
    [
      "0051eb14",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051eb10",
      "READ",
      [
        "storage",
        "002ab5bc",
        null,
        "string"
      ]
    ],
    [
      "0051eb10",
      "READ",
      [
        "storage",
        "002ab5cc",
        null,
        "string"
      ]
    ],
    [
      "0051eb14",
      "READ",
      [
        "storage",
        "002c2810",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md#insn-0051e840) · [`0051e7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md#insn-0051e7d4) · [`0051e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md#insn-0051e7e0)
- 新版 [`0051eb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ead0.md#insn-0051eb60) · [`0051eaf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ead0.md#insn-0051eaf4) · [`0051eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ead0.md#insn-0051eb00)

~~~diff
- 0051e840 ["INT_ADD", "register:40f0:8", ["const:51e840:8", "const:4:8"]]
- 0051e840 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051eb60 ["INT_ADD", "register:40f0:8", ["const:51eb60:8", "const:4:8"]]
+ 0051eb60 ["CALL", null, ["callee:00c58fb0:8"]]
- 0051e840 bytes e8e51c94
+ 0051eb60 bytes 14e91c94
- 0051e7d4 ["INT_ADD", "register:40f0:8", ["const:51e7d4:8", "const:4:8"]]
- 0051e7d4 ["CALL", null, ["callee:00c58f90:8"]]
+ 0051eaf4 ["INT_ADD", "register:40f0:8", ["const:51eaf4:8", "const:4:8"]]
+ 0051eaf4 ["CALL", null, ["callee:00c58f90:8"]]
- 0051e7d4 bytes fbe51c94
+ 0051eaf4 bytes 27e91c94
- 0051e7e0 ["INT_ADD", "register:40f0:8", ["const:51e7e0:8", "const:4:8"]]
- 0051e7e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0051eb00 ["INT_ADD", "register:40f0:8", ["const:51eb00:8", "const:4:8"]]
+ 0051eb00 ["CALL", null, ["callee:00c58f30:8"]]
- 0051e7e0 bytes e0e51c94
+ 0051eb00 bytes 0ce91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53240f756c0d28bd80903d61eef711a3"></a>

### [`0051e890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md) → [`0051ebb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ebb0.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies

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
      "definition_site": "0051eccc",
      "incomplete_value": true,
      "site": "0051eccc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051e9ac",
      "incomplete_value": true,
      "site": "0051e9ac",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051ed10",
      "incomplete_value": true,
      "site": "0051ed10",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0051e9f0",
      "incomplete_value": true,
      "site": "0051e9f0",
      "value": [
        "LOAD",
        "8",
        [
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
      "0051ecbc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051ed00",
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
      "0051ecbc",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051ed00",
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

- 旧版 [`0051e9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md#insn-0051e9ac) · [`0051e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md#insn-0051e9f0) · [`0051e8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md#insn-0051e8c4)
- 新版 [`0051eccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ebb0.md#insn-0051eccc) · [`0051ed10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ebb0.md#insn-0051ed10) · [`0051ebe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ebb0.md#insn-0051ebe4)

~~~diff
- 0051e9ac ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e9ac ["INT_ADD", "register:40f0:8", ["const:51e9ac:8", "const:4:8"]]
- 0051e9ac ["CALLIND", null, ["register:0:8"]]
+ 0051eccc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051eccc ["INT_ADD", "register:40f0:8", ["const:51eccc:8", "const:4:8"]]
+ 0051eccc ["CALLIND", null, ["register:0:8"]]
- 0051e9ac bytes 20013fd6
+ 0051eccc bytes 20013fd6
- 0051e9f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e9f0 ["INT_ADD", "register:40f0:8", ["const:51e9f0:8", "const:4:8"]]
- 0051e9f0 ["CALLIND", null, ["register:0:8"]]
+ 0051ed10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051ed10 ["INT_ADD", "register:40f0:8", ["const:51ed10:8", "const:4:8"]]
+ 0051ed10 ["CALLIND", null, ["register:0:8"]]
- 0051e9f0 bytes 20013fd6
+ 0051ed10 bytes 20013fd6
- 0051e8c4 ["INT_ADD", "register:40f0:8", ["const:51e8c4:8", "const:4:8"]]
- 0051e8c4 ["CALL", null, ["callee:00c597a0:8"]]
+ 0051ebe4 ["INT_ADD", "register:40f0:8", ["const:51ebe4:8", "const:4:8"]]
+ 0051ebe4 ["CALL", null, ["callee:00c597a0:8"]]
- 0051e8c4 bytes c3e71c94
+ 0051ebe4 bytes efea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e8d12db275fa6c123f022864b6b3f0"></a>

### [`0051ec4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md) → [`0051ef6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ef6c.md) FUN_0051ef6c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051efb0",
      "incomplete_value": true,
      "site": "0051efc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051ec90",
      "incomplete_value": true,
      "site": "0051eca0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051efac",
      "incomplete_value": true,
      "site": "0051efc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ec8c",
      "incomplete_value": true,
      "site": "0051eca4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c3d:8"
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
      "definition_site": "0051efac",
      "incomplete_value": true,
      "site": "0051efc4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051ec8c",
      "incomplete_value": true,
      "site": "0051eca4",
      "value": [
        "LOAD",
        "16",
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
      "0051efac",
      "READ",
      [
        "storage",
        "002b2c3d",
        null,
        "string"
      ]
    ],
    [
      "0051efac",
      "READ",
      [
        "storage",
        "002b2c4d",
        null,
        "string"
      ]
    ],
    [
      "0051efb0",
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
      "0051efac",
      "READ",
      [
        "storage",
        "002b2c87",
        null,
        "string"
      ]
    ],
    [
      "0051efac",
      "READ",
      [
        "storage",
        "002b2c97",
        null,
        "string"
      ]
    ],
    [
      "0051efb0",
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

- 旧版 [`0051ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md#insn-0051ece4) · [`0051ec70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md#insn-0051ec70) · [`0051ec7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md#insn-0051ec7c)
- 新版 [`0051f004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ef6c.md#insn-0051f004) · [`0051ef90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ef6c.md#insn-0051ef90) · [`0051ef9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051e/0051ef6c.md#insn-0051ef9c)

~~~diff
- 0051ece4 ["INT_ADD", "register:40f0:8", ["const:51ece4:8", "const:4:8"]]
- 0051ece4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051f004 ["INT_ADD", "register:40f0:8", ["const:51f004:8", "const:4:8"]]
+ 0051f004 ["CALL", null, ["callee:00c58fb0:8"]]
- 0051ece4 bytes bfe41c94
+ 0051f004 bytes ebe71c94
- 0051ec70 ["INT_ADD", "register:40f0:8", ["const:51ec70:8", "const:4:8"]]
- 0051ec70 ["CALL", null, ["callee:00c58f90:8"]]
+ 0051ef90 ["INT_ADD", "register:40f0:8", ["const:51ef90:8", "const:4:8"]]
+ 0051ef90 ["CALL", null, ["callee:00c58f90:8"]]
- 0051ec70 bytes d4e41c94
+ 0051ef90 bytes 00e81c94
- 0051ec7c ["INT_ADD", "register:40f0:8", ["const:51ec7c:8", "const:4:8"]]
- 0051ec7c ["CALL", null, ["callee:00c58f30:8"]]
+ 0051ef9c ["INT_ADD", "register:40f0:8", ["const:51ef9c:8", "const:4:8"]]
+ 0051ef9c ["CALL", null, ["callee:00c58f30:8"]]
- 0051ec7c bytes b9e41c94
+ 0051ef9c bytes e5e71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41eb638d02b8f7dd9fab7b07a13b9139"></a>

### [`0051ee0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md) → [`0051f12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f12c.md) FUN_0051f12c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`004ff500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff500.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051f248",
      "incomplete_value": true,
      "site": "0051f25c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051ef28",
      "incomplete_value": true,
      "site": "0051ef3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051f244",
      "incomplete_value": true,
      "site": "0051f260",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d32:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ef24",
      "incomplete_value": true,
      "site": "0051ef40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c54:8"
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
      "definition_site": "0051f244",
      "incomplete_value": true,
      "site": "0051f260",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051ef24",
      "incomplete_value": true,
      "site": "0051ef40",
      "value": [
        "LOAD",
        "16",
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
      "0051f1c8",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ],
    [
      "0051f1f4",
      "PARAM",
      [
        "storage",
        "002a0f7a",
        null,
        null
      ]
    ],
    [
      "0051f244",
      "READ",
      [
        "storage",
        "002bec54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051f1c8",
      "PARAM",
      [
        "storage",
        "002bd7f8",
        null,
        null
      ]
    ],
    [
      "0051f1f4",
      "PARAM",
      [
        "storage",
        "002a0fba",
        null,
        null
      ]
    ],
    [
      "0051f244",
      "READ",
      [
        "storage",
        "002bed32",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051ee44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md#insn-0051ee44) · [`0051ee4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md#insn-0051ee4c) · [`0051ee64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md#insn-0051ee64)
- 新版 [`0051f164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f12c.md#insn-0051f164) · [`0051f16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f12c.md#insn-0051f16c) · [`0051f184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f12c.md#insn-0051f184)

~~~diff
- 0051ee44 ["INT_ADD", "register:40f0:8", ["const:51ee44:8", "const:4:8"]]
- 0051ee44 ["CALL", null, ["callee:00c5aa10:8"]]
+ 0051f164 ["INT_ADD", "register:40f0:8", ["const:51f164:8", "const:4:8"]]
+ 0051f164 ["CALL", null, ["callee:00c5aa10:8"]]
- 0051ee44 bytes ffea1c94
+ 0051f164 bytes 2bee1c94
- 0051ee4c ["INT_ADD", "register:40f0:8", ["const:51ee4c:8", "const:4:8"]]
- 0051ee4c ["CALL", null, ["callee:00451c10:8"]]
+ 0051f16c ["INT_ADD", "register:40f0:8", ["const:51f16c:8", "const:4:8"]]
+ 0051f16c ["CALL", null, ["callee:00451c10:8"]]
- 0051ee4c bytes a9cafc97
+ 0051f16c bytes a9cafc97
- 0051ee64 ["COPY", "tmp:0:8", ["const:71a:8"]]
- 0051ee64 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0051ee64 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0051ee64 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0051f184 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 0051f184 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051f184 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051f184 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0051ee64 bytes 946a1c91
+ 0051f184 bytes 94e21f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4faaef5d1bf36dc18e1e3d1b7cba4e"></a>

### [`0051f234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md) → [`0051f554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f554.md) _ZN5Botan11X509_Object11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c587e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004a5ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c597a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597a0.md) [`00c597b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597b0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051f624",
      "incomplete_value": true,
      "site": "0051f624",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051f304",
      "incomplete_value": true,
      "site": "0051f304",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051f668",
      "incomplete_value": true,
      "site": "0051f668",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "0051f348",
      "incomplete_value": true,
      "site": "0051f348",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "0051f614",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051f658",
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
      "0051f614",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0051f658",
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

- 旧版 [`0051f304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md#insn-0051f304) · [`0051f348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md#insn-0051f348) · [`0051f268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md#insn-0051f268)
- 新版 [`0051f624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f554.md#insn-0051f624) · [`0051f668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f554.md#insn-0051f668) · [`0051f588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f554.md#insn-0051f588)

~~~diff
- 0051f304 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f304 ["INT_ADD", "register:40f0:8", ["const:51f304:8", "const:4:8"]]
- 0051f304 ["CALLIND", null, ["register:0:8"]]
+ 0051f624 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f624 ["INT_ADD", "register:40f0:8", ["const:51f624:8", "const:4:8"]]
+ 0051f624 ["CALLIND", null, ["register:0:8"]]
- 0051f304 bytes 20013fd6
+ 0051f624 bytes 20013fd6
- 0051f348 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f348 ["INT_ADD", "register:40f0:8", ["const:51f348:8", "const:4:8"]]
- 0051f348 ["CALLIND", null, ["register:0:8"]]
+ 0051f668 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f668 ["INT_ADD", "register:40f0:8", ["const:51f668:8", "const:4:8"]]
+ 0051f668 ["CALLIND", null, ["register:0:8"]]
- 0051f348 bytes 20013fd6
+ 0051f668 bytes 20013fd6
- 0051f268 ["INT_ADD", "register:40f0:8", ["const:51f268:8", "const:4:8"]]
- 0051f268 ["CALL", null, ["callee:00c597a0:8"]]
+ 0051f588 ["INT_ADD", "register:40f0:8", ["const:51f588:8", "const:4:8"]]
+ 0051f588 ["CALL", null, ["callee:00c597a0:8"]]
- 0051f268 bytes 5ae51c94
+ 0051f588 bytes 86e81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8dad279201b7a8495b5f9b530797d09"></a>

### [`0051f5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md) → [`0051f8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f8e4.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f60.md) · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0051fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md)
- 新版 呼出元 1件 [`00c5af30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af30.md) · 呼出先 16件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0051fd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051fd70.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00547ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ecc.md) [`00547ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0051f920",
      "incomplete_value": false,
      "site": "0051f928",
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
      "definition_site": "0051f600",
      "incomplete_value": false,
      "site": "0051f608",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051fb84",
      "incomplete_value": false,
      "site": "0051fb90",
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
            "const:caf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f864",
      "incomplete_value": false,
      "site": "0051f870",
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
            "const:c65:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051fbd8",
      "incomplete_value": true,
      "site": "0051fbe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f8b8",
      "incomplete_value": true,
      "site": "0051f8c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
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
      "0051f928",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "0051f96c",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "0051f96c",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0051f928",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ],
    [
      "0051f96c",
      "READ",
      [
        "storage",
        "00c6b770",
        null,
        "pointer"
      ]
    ],
    [
      "0051f96c",
      "READ",
      [
        "storage",
        "00c6b778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051f870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md#insn-0051f870) · [`0051f8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md#insn-0051f8c4) · [`0051f8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md#insn-0051f8ec)
- 新版 [`0051fb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f8e4.md#insn-0051fb90) · [`0051fbe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f8e4.md#insn-0051fbe4) · [`0051fc0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f8e4.md#insn-0051fc0c)

~~~diff
- 0051f870 ["INT_ADD", "register:40f0:8", ["const:51f870:8", "const:4:8"]]
- 0051f870 ["CALL", null, ["callee:00c59000:8"]]
+ 0051fb90 ["INT_ADD", "register:40f0:8", ["const:51fb90:8", "const:4:8"]]
+ 0051fb90 ["CALL", null, ["callee:00c59000:8"]]
- 0051f870 bytes f0e11c94
+ 0051fb90 bytes 1ce51c94
- 0051f8c4 ["INT_ADD", "register:40f0:8", ["const:51f8c4:8", "const:4:8"]]
- 0051f8c4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0051fbe4 ["INT_ADD", "register:40f0:8", ["const:51fbe4:8", "const:4:8"]]
+ 0051fbe4 ["CALL", null, ["callee:00c58fb0:8"]]
- 0051f8c4 bytes c7e11c94
+ 0051fbe4 bytes f3e41c94
- 0051f8ec ["INT_ADD", "register:40f0:8", ["const:51f8ec:8", "const:4:8"]]
- 0051f8ec ["CALL", null, ["callee:00c59150:8"]]
+ 0051fc0c ["INT_ADD", "register:40f0:8", ["const:51fc0c:8", "const:4:8"]]
+ 0051fc0c ["CALL", null, ["callee:00c59150:8"]]
- 0051f8ec bytes 25e21c94
+ 0051fc0c bytes 51e51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6f78106fcf75198ebdff15d9d963fbd"></a>

### [`0051fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md) → [`0051fd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051fd70.md) FUN_0051fd70

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0051f5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md) [`00520090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md) · 呼出先 15件 [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`0051f8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051f8e4.md) [`005203b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/005203b0.md) · 呼出先 15件 [`004a5adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5adc.md) [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.01% / 新版 96.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051fdb0",
      "incomplete_value": true,
      "site": "0051fdb0",
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
      "definition_site": "0051fa90",
      "incomplete_value": true,
      "site": "0051fa90",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00520058",
      "incomplete_value": true,
      "site": "00520058",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051fd38",
      "incomplete_value": true,
      "site": "0051fd38",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005200dc",
      "incomplete_value": true,
      "site": "005200dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051fdbc",
      "incomplete_value": true,
      "site": "0051fdbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051fd98",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0051fdb0",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051fddc",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0051fd98",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0051fdb0",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051fddc",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051fa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md#insn-0051fa9c) · [`0051fae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md#insn-0051fae0) · [`0051fd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md#insn-0051fd38)
- 新版 [`0051fdbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051fd70.md#insn-0051fdbc) · [`0051fe00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051fd70.md#insn-0051fe00) · [`00520058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051fd70.md#insn-00520058)

~~~diff
- 0051fa9c ["INT_ADD", "register:40f0:8", ["const:51fa9c:8", "const:4:8"]]
- 0051fa9c ["CALL", null, ["callee:00c59730:8"]]
+ 0051fdbc ["INT_ADD", "register:40f0:8", ["const:51fdbc:8", "const:4:8"]]
+ 0051fdbc ["CALL", null, ["callee:00c59730:8"]]
- 0051fa9c bytes 31e31c94
+ 0051fdbc bytes 5de61c94
- 0051fae0 ["INT_ADD", "register:40f0:8", ["const:51fae0:8", "const:4:8"]]
- 0051fae0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0051fe00 ["INT_ADD", "register:40f0:8", ["const:51fe00:8", "const:4:8"]]
+ 0051fe00 ["CALL", null, ["callee:00c58f50:8"]]
- 0051fae0 bytes 28e11c94
+ 0051fe00 bytes 54e41c94
- 0051fd38 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051fd38 ["INT_ADD", "register:40f0:8", ["const:51fd38:8", "const:4:8"]]
- 0051fd38 ["CALLIND", null, ["register:0:8"]]
+ 00520058 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00520058 ["INT_ADD", "register:40f0:8", ["const:520058:8", "const:4:8"]]
+ 00520058 ["CALLIND", null, ["register:0:8"]]
- 0051fd38 bytes 20013fd6
+ 00520058 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93420f74fefc838d8e922c8e8cf762f2"></a>

### [`00520090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md) → [`005203b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/005203b0.md) _ZNK5Botan11X509_Object16verify_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d80.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`004acc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md) [`0051fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md) [`00547b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b54.md)
- 新版 呼出元 1件 [`00c5ad50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad50.md) · 呼出先 19件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004a6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6f7c.md) [`004acf84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ac/004acf84.md) [`0051fd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051f/0051fd70.md) [`00547e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547e74.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005203f8",
      "incomplete_value": false,
      "site": "005203f8",
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
      "definition_site": "005200d8",
      "incomplete_value": false,
      "site": "005200d8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052078c",
      "incomplete_value": false,
      "site": "00520794",
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
            "const:c9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052046c",
      "incomplete_value": false,
      "site": "00520474",
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
            "const:b43:8"
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
      "definition_site": "005207a0",
      "incomplete_value": false,
      "site": "005207a8",
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
            "const:373:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520480",
      "incomplete_value": false,
      "site": "00520488",
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
            "const:295:8"
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
      "005203f8",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "0052043c",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "0052043c",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005203f8",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ],
    [
      "0052043c",
      "READ",
      [
        "storage",
        "00c6b770",
        null,
        "pointer"
      ]
    ],
    [
      "0052043c",
      "READ",
      [
        "storage",
        "00c6b778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md#insn-00520154) · [`00520474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md#insn-00520474) · [`00520488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md#insn-00520488)
- 新版 [`00520474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/005203b0.md#insn-00520474) · [`00520794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/005203b0.md#insn-00520794) · [`005207a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/005203b0.md#insn-005207a8)

~~~diff
- 00520154 ["COPY", "register:0:8", ["register:4048:8"]]
- 00520154 ["INT_ADD", "register:40f0:8", ["const:520154:8", "const:4:8"]]
- 00520154 ["CALLIND", null, ["register:0:8"]]
+ 00520474 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00520474 ["INT_ADD", "register:40f0:8", ["const:520474:8", "const:4:8"]]
+ 00520474 ["CALLIND", null, ["register:0:8"]]
- 00520154 bytes 20013fd6
+ 00520474 bytes 20013fd6
- 00520474 ["INT_ADD", "register:40f0:8", ["const:520474:8", "const:4:8"]]
- 00520474 ["CALL", null, ["callee:004acf84:8"]]
+ 00520794 ["INT_ADD", "register:40f0:8", ["const:520794:8", "const:4:8"]]
+ 00520794 ["CALL", null, ["callee:004acf84:8"]]
- 00520474 bytes fc31fe97
+ 00520794 bytes fc31fe97
- 00520488 ["INT_ADD", "register:40f0:8", ["const:520488:8", "const:4:8"]]
- 00520488 ["CALL", null, ["callee:004acf84:8"]]
+ 005207a8 ["INT_ADD", "register:40f0:8", ["const:5207a8:8", "const:4:8"]]
+ 005207a8 ["CALL", null, ["callee:004acf84:8"]]
- 00520488 bytes f731fe97
+ 005207a8 bytes f731fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daba5c5bd932f7caa81ce65b1f31da69"></a>

### [`00520a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a24.md) → [`00520d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520d44.md) _ZNK5Botan16X509_Certificate9PEM_labelEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520d68",
      "incomplete_value": true,
      "site": "00520d68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:492:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520a48",
      "incomplete_value": true,
      "site": "00520a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b4:8"
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
      "00520d58",
      "READ",
      [
        "storage",
        "002ba3b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00520d58",
      "READ",
      [
        "storage",
        "002ba492",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a24.md#insn-00520a2c)
- 新版 [`00520d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520d44.md#insn-00520d4c)

~~~diff
- 00520a2c ["COPY", "tmp:0:8", ["const:3b4:8"]]
- 00520a2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00520a2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00520a2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00520d4c ["COPY", "tmp:0:8", ["const:492:8"]]
+ 00520d4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00520d4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00520d4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00520a2c bytes 4ad10e91
+ 00520d4c bytes 4a491291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21568011486d592568615f1e74bea7a3"></a>

### [`00520a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md) → [`00520d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520d70.md) _ZNK5Botan16X509_Certificate20alternate_PEM_labelsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520d94",
      "incomplete_value": true,
      "site": "00520da4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520a74",
      "incomplete_value": true,
      "site": "00520a84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d98:8"
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
      "00520d94",
      "READ",
      [
        "storage",
        "002b1d98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00520d94",
      "READ",
      [
        "storage",
        "002b1de2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md#insn-00520a68) · [`00520a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md#insn-00520a94) · [`00520aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md#insn-00520aa4)
- 新版 [`00520d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520d70.md#insn-00520d88) · [`00520db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520d70.md#insn-00520db4) · [`00520dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520d70.md#insn-00520dc4)

~~~diff
- 00520a68 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00520a68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00520a68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00520a68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00520d88 ["COPY", "tmp:0:8", ["const:de2:8"]]
+ 00520d88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00520d88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00520d88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00520a68 bytes 29613691
+ 00520d88 bytes 29893791
- 00520a94 ["INT_ADD", "register:40f0:8", ["const:520a94:8", "const:4:8"]]
- 00520a94 ["CALL", null, ["callee:004738a0:8"]]
+ 00520db4 ["INT_ADD", "register:40f0:8", ["const:520db4:8", "const:4:8"]]
+ 00520db4 ["CALL", null, ["callee:004738a0:8"]]
- 00520a94 bytes bb4afd97
+ 00520db4 bytes bb4afd97
- 00520aa4 ["INT_ADD", "register:40f0:8", ["const:520aa4:8", "const:4:8"]]
- 00520aa4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00520dc4 ["INT_ADD", "register:40f0:8", ["const:520dc4:8", "const:4:8"]]
+ 00520dc4 ["CALL", null, ["callee:00c58f50:8"]]
- 00520aa4 bytes 37dd1c94
+ 00520dc4 bytes 63e01c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dae1cfd362ab83667cc3c489f3906c8"></a>

### [`00520af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md) → [`00520e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520e18.md) _ZN5Botan16X509_CertificateC1ERNS_10DataSourceE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5ad20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520e58",
      "incomplete_value": true,
      "site": "00520e58",
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
      "definition_site": "00520b38",
      "incomplete_value": true,
      "site": "00520b38",
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
      "definition_site": "00520e58",
      "incomplete_value": true,
      "site": "00520e58",
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
      "definition_site": "00520b38",
      "incomplete_value": true,
      "site": "00520b38",
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
      "definition_site": "00520e98",
      "incomplete_value": true,
      "site": "00520ea0",
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
      "definition_site": "00520b78",
      "incomplete_value": true,
      "site": "00520b80",
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
      "00520e38",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00520e40",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00520e58",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00520e38",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00520e40",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00520e58",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md#insn-00520b10) · [`00520b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md#insn-00520b14) · [`00520b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md#insn-00520b18)
- 新版 [`00520e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520e18.md#insn-00520e30) · [`00520e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520e18.md#insn-00520e34) · [`00520e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520e18.md#insn-00520e38)

~~~diff
- 00520b10 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00520e30 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00520b10 bytes c83b00f0
+ 00520e30 bytes e83b0090
- 00520b14 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00520e34 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00520b14 bytes ca3b00d0
+ 00520e34 bytes ca3b00f0
- 00520b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 00520b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520e38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 00520e38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520b18 bytes 081541f9
+ 00520e38 bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c28027068a6e74fbda718738e08076"></a>

### [`00520c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md) → [`00520f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f6c.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c90.md) · 呼出先 7件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00c5ac60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac60.md) · 呼出先 7件 [`00540728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520fac",
      "incomplete_value": true,
      "site": "00520fac",
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
      "definition_site": "00520c8c",
      "incomplete_value": true,
      "site": "00520c8c",
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
      "definition_site": "00520fac",
      "incomplete_value": true,
      "site": "00520fac",
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
      "definition_site": "00520c8c",
      "incomplete_value": true,
      "site": "00520c8c",
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
      "definition_site": "00520ff4",
      "incomplete_value": true,
      "site": "00521000",
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
      "definition_site": "00520cd4",
      "incomplete_value": true,
      "site": "00520ce0",
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
      "00520f8c",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00520f94",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00520fac",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00520f8c",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00520f94",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00520fac",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md#insn-00520d38) · [`00520c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md#insn-00520c64) · [`00520c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md#insn-00520c68)
- 新版 [`00521058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f6c.md#insn-00521058) · [`00520f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f6c.md#insn-00520f84) · [`00520f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00520/00520f6c.md#insn-00520f88)

~~~diff
- 00520d38 ["COPY", "register:0:8", ["register:4048:8"]]
- 00520d38 ["INT_ADD", "register:40f0:8", ["const:520d38:8", "const:4:8"]]
- 00520d38 ["CALLIND", null, ["register:0:8"]]
+ 00521058 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00521058 ["INT_ADD", "register:40f0:8", ["const:521058:8", "const:4:8"]]
+ 00521058 ["CALLIND", null, ["register:0:8"]]
- 00520d38 bytes 20013fd6
+ 00521058 bytes 20013fd6
- 00520c64 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00520f84 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00520c64 bytes c83b00f0
+ 00520f84 bytes e83b0090
- 00520c68 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00520f88 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00520c68 bytes ca3b00d0
+ 00520f88 bytes ca3b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04e9578a21199f963740ff0f35db0dad"></a>

### [`00520dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md) → [`005210e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/005210e4.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b30.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)
- 新版 呼出元 1件 [`00c5ab00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab00.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5a700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a700.md) [`00c5a710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a710.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00521124",
      "incomplete_value": true,
      "site": "00521124",
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
      "definition_site": "00520e04",
      "incomplete_value": true,
      "site": "00520e04",
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
      "definition_site": "00521124",
      "incomplete_value": true,
      "site": "00521124",
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
      "definition_site": "00520e04",
      "incomplete_value": true,
      "site": "00520e04",
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
      "definition_site": "00521164",
      "incomplete_value": true,
      "site": "0052116c",
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
      "definition_site": "00520e44",
      "incomplete_value": true,
      "site": "00520e4c",
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
      "00521104",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0052110c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00521124",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00521104",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "0052110c",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00521124",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md#insn-00520ddc) · [`00520de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md#insn-00520de0) · [`00520de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md#insn-00520de4)
- 新版 [`005210fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/005210e4.md#insn-005210fc) · [`00521100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/005210e4.md#insn-00521100) · [`00521104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/005210e4.md#insn-00521104)

~~~diff
- 00520ddc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005210fc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00520ddc bytes c83b00f0
+ 005210fc bytes c83b00f0
- 00520de0 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00521100 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00520de0 bytes ca3b00d0
+ 00521100 bytes ca3b00d0
- 00520de4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 00520de4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00521104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 00521104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520de4 bytes 081541f9
+ 00521104 bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a31eb42ef0f497f5407b4578931c9e4f"></a>

### [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) → [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) _ZN5Botan16X509_Certificate12force_decodeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 68件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md)
- 新版 呼出元 0件  · 呼出先 68件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`004a5adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5adc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `call_target` 8件, `store_value` 14件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005214b4",
      "incomplete_value": true,
      "site": "005214b8",
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
      "definition_site": "00521194",
      "incomplete_value": true,
      "site": "00521198",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00521580",
      "incomplete_value": false,
      "site": "00521580",
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
      "definition_site": "00521260",
      "incomplete_value": false,
      "site": "00521260",
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
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005219c8",
      "incomplete_value": true,
      "site": "005219c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005216a8",
      "incomplete_value": true,
      "site": "005216a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:781:8"
              ]
            ]
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
      "00521388",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005214ac",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "005214b8",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00521388",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005214ac",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "005214b8",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md#insn-00521078) · [`0052123c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md#insn-0052123c) · [`005213a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md#insn-005213a4)
- 新版 [`00521398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md#insn-00521398) · [`0052155c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md#insn-0052155c) · [`005216c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md#insn-005216c4)

~~~diff
- 00521078 ["COPY", "register:0:8", ["register:4048:8"]]
- 00521078 ["INT_ADD", "register:40f0:8", ["const:521078:8", "const:4:8"]]
- 00521078 ["CALLIND", null, ["register:0:8"]]
+ 00521398 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00521398 ["INT_ADD", "register:40f0:8", ["const:521398:8", "const:4:8"]]
+ 00521398 ["CALLIND", null, ["register:0:8"]]
- 00521078 bytes 20013fd6
+ 00521398 bytes 20013fd6
- 0052123c ["COPY", "register:0:8", ["register:4048:8"]]
- 0052123c ["INT_ADD", "register:40f0:8", ["const:52123c:8", "const:4:8"]]
- 0052123c ["CALLIND", null, ["register:0:8"]]
+ 0052155c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052155c ["INT_ADD", "register:40f0:8", ["const:52155c:8", "const:4:8"]]
+ 0052155c ["CALLIND", null, ["register:0:8"]]
- 0052123c bytes 20013fd6
+ 0052155c bytes 20013fd6
- 005213a4 ["INT_ADD", "register:40f0:8", ["const:5213a4:8", "const:4:8"]]
- 005213a4 ["CALL", null, ["callee:0043e138:8"]]
+ 005216c4 ["INT_ADD", "register:40f0:8", ["const:5216c4:8", "const:4:8"]]
+ 005216c4 ["CALL", null, ["callee:0043e138:8"]]
- 005213a4 bytes 9d72fc97
+ 005216c4 bytes 9d72fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba06b798f4f4d1de3604caa3d07c8dc"></a>

### [`005228a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md) → [`00522bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522bc4.md) _ZNK5Botan16X509_Certificate4dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "00522c24",
      "incomplete_value": false,
      "site": "00522c2c",
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
            "const:d6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522904",
      "incomplete_value": false,
      "site": "0052290c",
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
            "const:c93:8"
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
      "definition_site": "00522c60",
      "incomplete_value": true,
      "site": "00522c6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00522940",
      "incomplete_value": true,
      "site": "0052294c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00522c5c",
      "incomplete_value": false,
      "site": "00522c6c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0052293c",
      "incomplete_value": false,
      "site": "0052294c",
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
      "00522c24",
      "PARAM",
      [
        "storage",
        "002b0c93",
        null,
        "string"
      ]
    ],
    [
      "00522c5c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00522c60",
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
      "00522c24",
      "PARAM",
      [
        "storage",
        "002b0d6a",
        null,
        "string"
      ]
    ],
    [
      "00522c5c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00522c60",
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

- 旧版 [`0052290c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md#insn-0052290c) · [`0052294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md#insn-0052294c) · [`005228f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md#insn-005228f8)
- 新版 [`00522c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522bc4.md#insn-00522c2c) · [`00522c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522bc4.md#insn-00522c6c) · [`00522c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522bc4.md#insn-00522c18)

~~~diff
- 0052290c ["INT_ADD", "register:40f0:8", ["const:52290c:8", "const:4:8"]]
- 0052290c ["CALL", null, ["callee:0043e138:8"]]
+ 00522c2c ["INT_ADD", "register:40f0:8", ["const:522c2c:8", "const:4:8"]]
+ 00522c2c ["CALL", null, ["callee:0043e138:8"]]
- 0052290c bytes 436dfc97
+ 00522c2c bytes 436dfc97
- 0052294c ["INT_ADD", "register:40f0:8", ["const:52294c:8", "const:4:8"]]
- 0052294c ["CALL", null, ["callee:00c58fb0:8"]]
+ 00522c6c ["INT_ADD", "register:40f0:8", ["const:522c6c:8", "const:4:8"]]
+ 00522c6c ["CALL", null, ["callee:00c58fb0:8"]]
- 0052294c bytes a5d51c94
+ 00522c6c bytes d1d81c94
- 005228f8 ["INT_ADD", "register:40f0:8", ["const:5228f8:8", "const:4:8"]]
- 005228f8 ["CALL", null, ["callee:00c58f90:8"]]
+ 00522c18 ["INT_ADD", "register:40f0:8", ["const:522c18:8", "const:4:8"]]
+ 00522c18 ["CALL", null, ["callee:00c58f90:8"]]
- 005228f8 bytes b2d51c94
+ 00522c18 bytes ded81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c45540fe24468b331b7259478d505385"></a>

### [`00522ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md) → [`00522ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522ec0.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_10Usage_TypeE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f70.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md) [`00c59d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d10.md)
- 新版 呼出元 1件 [`00c5af40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af40.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md) [`00c5ace0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ace0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.30% / 新版 90.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00522f4c",
      "incomplete_value": true,
      "site": "00522f58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522c2c",
      "incomplete_value": true,
      "site": "00522c38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ceb:8"
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
      "definition_site": "00522ff4",
      "incomplete_value": true,
      "site": "00522ff4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ccf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522cd4",
      "incomplete_value": true,
      "site": "00522cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf1:8"
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
      "definition_site": "00522fe8",
      "incomplete_value": true,
      "site": "00522ff8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00522cc8",
      "incomplete_value": true,
      "site": "00522cd8",
      "value": [
        "LOAD",
        "8",
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
      "00522f4c",
      "READ",
      [
        "storage",
        "002b4ceb",
        null,
        "string"
      ]
    ],
    [
      "00522fe4",
      "READ",
      [
        "storage",
        "002bebf1",
        null,
        "string"
      ]
    ],
    [
      "00522fe8",
      "READ",
      [
        "storage",
        "002bebf8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00522f4c",
      "READ",
      [
        "storage",
        "002b4dc9",
        null,
        "string"
      ]
    ],
    [
      "00522fe4",
      "READ",
      [
        "storage",
        "002beccf",
        null,
        "string"
      ]
    ],
    [
      "00522fe8",
      "READ",
      [
        "storage",
        "002becd6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md#insn-00522be4) · [`00522bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md#insn-00522bf4) · [`00522c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md#insn-00522c04)
- 新版 [`00522f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522ec0.md#insn-00522f04) · [`00522f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522ec0.md#insn-00522f14) · [`00522f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00522/00522ec0.md#insn-00522f24)

~~~diff
- 00522be4 ["INT_ADD", "register:40f0:8", ["const:522be4:8", "const:4:8"]]
- 00522be4 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522f04 ["INT_ADD", "register:40f0:8", ["const:522f04:8", "const:4:8"]]
+ 00522f04 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522be4 bytes b7db1c94
+ 00522f04 bytes e3de1c94
- 00522bf4 ["INT_ADD", "register:40f0:8", ["const:522bf4:8", "const:4:8"]]
- 00522bf4 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522f14 ["INT_ADD", "register:40f0:8", ["const:522f14:8", "const:4:8"]]
+ 00522f14 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522bf4 bytes b3db1c94
+ 00522f14 bytes dfde1c94
- 00522c04 ["INT_ADD", "register:40f0:8", ["const:522c04:8", "const:4:8"]]
- 00522c04 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00522f24 ["INT_ADD", "register:40f0:8", ["const:522f24:8", "const:4:8"]]
+ 00522f24 ["CALL", null, ["callee:00c5aa90:8"]]
- 00522c04 bytes afdb1c94
+ 00522f24 bytes dbde1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d31690250c4aab3287a379a3c97974"></a>

### [`0052310c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md) → [`0052342c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052342c.md) _ZNK5Botan16X509_Certificate12subject_infoERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f80.md) · 呼出先 16件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5af50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af50.md) · 呼出先 16件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`004421f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/004421f4.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`005483f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005483f8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00523760",
      "incomplete_value": false,
      "site": "00523768",
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
            "const:5dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00523440",
      "incomplete_value": false,
      "site": "00523448",
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
            "const:510:8"
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
      "definition_site": "0052379c",
      "incomplete_value": false,
      "site": "005237a4",
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
            "const:fb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052347c",
      "incomplete_value": false,
      "site": "00523484",
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
            "const:ed6:8"
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
      "definition_site": "005237d8",
      "incomplete_value": false,
      "site": "005237e0",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005234b8",
      "incomplete_value": false,
      "site": "005234c0",
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
            "const:1bc:8"
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
      "00523760",
      "PARAM",
      [
        "storage",
        "002ab510",
        null,
        "string"
      ]
    ],
    [
      "0052379c",
      "PARAM",
      [
        "storage",
        "002b4ed6",
        null,
        "string"
      ]
    ],
    [
      "005237d8",
      "PARAM",
      [
        "storage",
        "002a11bc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00523760",
      "PARAM",
      [
        "storage",
        "002ab5dd",
        null,
        "string"
      ]
    ],
    [
      "0052379c",
      "PARAM",
      [
        "storage",
        "002b4fb4",
        null,
        "string"
      ]
    ],
    [
      "005237d8",
      "PARAM",
      [
        "storage",
        "002a11fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005231a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md#insn-005231a0) · [`00523448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md#insn-00523448) · [`00523484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md#insn-00523484)
- 新版 [`005234c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052342c.md#insn-005234c0) · [`00523768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052342c.md#insn-00523768) · [`005237a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00523/0052342c.md#insn-005237a4)

~~~diff
- 005231a0 ["INT_ADD", "register:40f0:8", ["const:5231a0:8", "const:4:8"]]
- 005231a0 ["CALL", null, ["callee:005483f8:8"]]
+ 005234c0 ["INT_ADD", "register:40f0:8", ["const:5234c0:8", "const:4:8"]]
+ 005234c0 ["CALL", null, ["callee:005483f8:8"]]
- 005231a0 bytes ce930094
+ 005234c0 bytes ce930094
- 00523448 ["INT_ADD", "register:40f0:8", ["const:523448:8", "const:4:8"]]
- 00523448 ["CALL", null, ["callee:004421f4:8"]]
+ 00523768 ["INT_ADD", "register:40f0:8", ["const:523768:8", "const:4:8"]]
+ 00523768 ["CALL", null, ["callee:004421f4:8"]]
- 00523448 bytes a37afc97
+ 00523768 bytes a37afc97
- 00523484 ["INT_ADD", "register:40f0:8", ["const:523484:8", "const:4:8"]]
- 00523484 ["CALL", null, ["callee:004421f4:8"]]
+ 005237a4 ["INT_ADD", "register:40f0:8", ["const:5237a4:8", "const:4:8"]]
+ 005237a4 ["CALL", null, ["callee:004421f4:8"]]
- 00523484 bytes 947afc97
+ 005237a4 bytes 947afc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96a5fda5fcfc431b8dc7f93e01f54dd5"></a>

### [`00524a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md) → [`00524d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524d40.md) _ZNK5Botan16X509_Certificate9to_stringEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`0053f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.84% / 新版 92.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 47件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00524d84",
      "incomplete_value": true,
      "site": "00524d98",
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
      "definition_site": "00524a64",
      "incomplete_value": true,
      "site": "00524a78",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00524d90",
      "incomplete_value": true,
      "site": "00524d9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00524a70",
      "incomplete_value": true,
      "site": "00524a7c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00524da4",
      "incomplete_value": true,
      "site": "00524da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
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
      "definition_site": "00524a84",
      "incomplete_value": true,
      "site": "00524a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
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
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00524d6c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00524d7c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00524d90",
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
      "00524d6c",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00524d7c",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00524d90",
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

- 旧版 [`00524af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md#insn-00524af4) · [`00524b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md#insn-00524b00) · [`00524b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md#insn-00524b1c)
- 新版 [`00524e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524d40.md#insn-00524e14) · [`00524e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524d40.md#insn-00524e20) · [`00524e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524d40.md#insn-00524e3c)

~~~diff
- 00524af4 ["INT_ADD", "register:40f0:8", ["const:524af4:8", "const:4:8"]]
- 00524af4 ["CALL", null, ["callee:00459830:8"]]
+ 00524e14 ["INT_ADD", "register:40f0:8", ["const:524e14:8", "const:4:8"]]
+ 00524e14 ["CALL", null, ["callee:00459830:8"]]
- 00524af4 bytes 87d2fc97
+ 00524e14 bytes 87d2fc97
- 00524b00 ["INT_ADD", "register:40f0:8", ["const:524b00:8", "const:4:8"]]
- 00524b00 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00524e20 ["INT_ADD", "register:40f0:8", ["const:524e20:8", "const:4:8"]]
+ 00524e20 ["CALL", null, ["callee:00c5aa90:8"]]
- 00524b00 bytes f0d31c94
+ 00524e20 bytes 1cd71c94
- 00524b1c ["INT_ADD", "register:40f0:8", ["const:524b1c:8", "const:4:8"]]
- 00524b1c ["CALL", null, ["callee:00459830:8"]]
+ 00524e3c ["INT_ADD", "register:40f0:8", ["const:524e3c:8", "const:4:8"]]
+ 00524e3c ["CALL", null, ["callee:00459830:8"]]
- 00524b1c bytes 7dd2fc97
+ 00524e3c bytes 7dd2fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4f076074fa22b2e0bc7e0a2dcfe297"></a>

### [`00526320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md) → [`00526640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526640.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`0054bca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bca4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526680",
      "incomplete_value": true,
      "site": "00526684",
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
      "definition_site": "00526360",
      "incomplete_value": true,
      "site": "00526364",
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
      "00526674",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00526684",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526674",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00526684",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md#insn-0052634c) · [`00526354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md#insn-00526354) · [`00526378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md#insn-00526378)
- 新版 [`0052666c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526640.md#insn-0052666c) · [`00526674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526640.md#insn-00526674) · [`00526698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526640.md#insn-00526698)

~~~diff
- 0052634c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052666c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052634c bytes a83b0090
+ 0052666c bytes a83b00b0
- 00526354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00526354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00526674 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 00526674 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00526354 bytes 080947f9
+ 00526674 bytes 08f146f9
- 00526378 ["INT_ADD", "register:40f0:8", ["const:526378:8", "const:4:8"]]
- 00526378 ["CALL", null, ["callee:00c58f30:8"]]
+ 00526698 ["INT_ADD", "register:40f0:8", ["const:526698:8", "const:4:8"]]
+ 00526698 ["CALL", null, ["callee:00c58f30:8"]]
- 00526378 bytes fac61c94
+ 00526698 bytes 26ca1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa7da630af03382137fc6bf9e8743596"></a>

### [`005263f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md) → [`00526710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526710.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0054d884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d884.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054dba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054dba4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md)

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
      "definition_site": "00526760",
      "incomplete_value": true,
      "site": "00526768",
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
      "definition_site": "00526440",
      "incomplete_value": true,
      "site": "00526448",
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
      "00526758",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00526768",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526758",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00526768",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00526418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md#insn-00526418) · [`0052642c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md#insn-0052642c) · [`00526438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md#insn-00526438)
- 新版 [`00526738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526710.md#insn-00526738) · [`0052674c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526710.md#insn-0052674c) · [`00526758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526710.md#insn-00526758)

~~~diff
- 00526418 ["INT_ADD", "register:40f0:8", ["const:526418:8", "const:4:8"]]
- 00526418 ["CALL", null, ["callee:00c59720:8"]]
+ 00526738 ["INT_ADD", "register:40f0:8", ["const:526738:8", "const:4:8"]]
+ 00526738 ["CALL", null, ["callee:00c59720:8"]]
- 00526418 bytes cec81c94
+ 00526738 bytes facb1c94
- 0052642c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0052674c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0052642c bytes a93b0090
+ 0052674c bytes a93b00b0
- 00526438 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
- 00526438 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00526758 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 00526758 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00526438 bytes 290947f9
+ 00526758 bytes 29f146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82db02905d394b866f761c759aa80106"></a>

### [`005264ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md) → [`0052680c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/0052680c.md) _ZN5Botan17X509_Cert_OptionsC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00547ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ecc.md) [`00547ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526888",
      "incomplete_value": true,
      "site": "00526888",
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
      "definition_site": "00526568",
      "incomplete_value": true,
      "site": "00526568",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526890",
      "incomplete_value": true,
      "site": "00526890",
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
      "definition_site": "00526570",
      "incomplete_value": true,
      "site": "00526570",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005268b8",
      "incomplete_value": true,
      "site": "005268b8",
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
      "definition_site": "00526598",
      "incomplete_value": true,
      "site": "00526598",
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
      "00526874",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00526888",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00526890",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526874",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ],
    [
      "00526888",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00526890",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005265bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md#insn-005265bc) · [`005267c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md#insn-005267c8) · [`00526804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md#insn-00526804)
- 新版 [`005268dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/0052680c.md#insn-005268dc) · [`00526ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/0052680c.md#insn-00526ae8) · [`00526b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/0052680c.md#insn-00526b24)

~~~diff
- 005265bc ["INT_ADD", "register:40f0:8", ["const:5265bc:8", "const:4:8"]]
- 005265bc ["CALL", null, ["callee:00c59230:8"]]
+ 005268dc ["INT_ADD", "register:40f0:8", ["const:5268dc:8", "const:4:8"]]
+ 005268dc ["CALL", null, ["callee:00c59230:8"]]
- 005265bc bytes 29c71c94
+ 005268dc bytes 55ca1c94
- 005267c8 ["INT_ADD", "register:40f0:8", ["const:5267c8:8", "const:4:8"]]
- 005267c8 ["CALL", null, ["callee:00c59150:8"]]
+ 00526ae8 ["INT_ADD", "register:40f0:8", ["const:526ae8:8", "const:4:8"]]
+ 00526ae8 ["CALL", null, ["callee:00c59150:8"]]
- 005267c8 bytes 6ec61c94
+ 00526ae8 bytes 9ac91c94
- 00526804 ["INT_ADD", "register:40f0:8", ["const:526804:8", "const:4:8"]]
- 00526804 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00526b24 ["INT_ADD", "register:40f0:8", ["const:526b24:8", "const:4:8"]]
+ 00526b24 ["CALL", null, ["callee:00c58fb0:8"]]
- 00526804 bytes f7c51c94
+ 00526b24 bytes 23c91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1163e85c12a1329ff733165a0af2a175"></a>

### [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) → [`00526d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fb0.md) · 呼出先 29件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)
- 新版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af80.md) · 呼出先 29件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00511584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md) [`0052811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/0052811c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005272c8",
      "incomplete_value": true,
      "site": "005272cc",
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
                "register:4050:8"
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
      "definition_site": "00526fa8",
      "incomplete_value": true,
      "site": "00526fac",
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
                "register:4050:8"
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
    "ordinal": 58,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00527f5c",
      "incomplete_value": false,
      "site": "00527f64",
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
            "const:8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527c3c",
      "incomplete_value": false,
      "site": "00527c44",
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
            "const:fbb:8"
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00527f98",
      "incomplete_value": true,
      "site": "00527fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00527c78",
      "incomplete_value": true,
      "site": "00527c84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 88,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00527224",
      "READ",
      [
        "storage",
        "00ca54a8",
        null,
        "undefined8"
      ]
    ],
    [
      "005273cc",
      "READ",
      [
        "storage",
        "00ca54a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00527f5c",
      "PARAM",
      [
        "storage",
        "002b8fbb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00527224",
      "READ",
      [
        "storage",
        "00ca6468",
        null,
        "undefined8"
      ]
    ],
    [
      "005273cc",
      "READ",
      [
        "storage",
        "00ca6468",
        null,
        "undefined8"
      ]
    ],
    [
      "00527f5c",
      "PARAM",
      [
        "storage",
        "002b908a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00527c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md#insn-00527c44) · [`00527c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md#insn-00527c84) · [`00526a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md#insn-00526a6c)
- 新版 [`00527f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md#insn-00527f64) · [`00527fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md#insn-00527fa4) · [`00526d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md#insn-00526d8c)

~~~diff
- 00527c44 ["INT_ADD", "register:40f0:8", ["const:527c44:8", "const:4:8"]]
- 00527c44 ["CALL", null, ["callee:0043e138:8"]]
+ 00527f64 ["INT_ADD", "register:40f0:8", ["const:527f64:8", "const:4:8"]]
+ 00527f64 ["CALL", null, ["callee:0043e138:8"]]
- 00527c44 bytes 7558fc97
+ 00527f64 bytes 7558fc97
- 00527c84 ["INT_ADD", "register:40f0:8", ["const:527c84:8", "const:4:8"]]
- 00527c84 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00527fa4 ["INT_ADD", "register:40f0:8", ["const:527fa4:8", "const:4:8"]]
+ 00527fa4 ["CALL", null, ["callee:00c58fb0:8"]]
- 00527c84 bytes d7c01c94
+ 00527fa4 bytes 03c41c94
- 00526a6c ["INT_ADD", "register:40f0:8", ["const:526a6c:8", "const:4:8"]]
- 00526a6c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00526d8c ["INT_ADD", "register:40f0:8", ["const:526d8c:8", "const:4:8"]]
+ 00526d8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00526a6c bytes 35cc1c94
+ 00526d8c bytes 61cf1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9990fad4cd7670ad2fe0bea80878cb1"></a>

### [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) → [`00528188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md) _ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8Respons

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fc0.md) · 呼出先 21件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00501630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501630.md) [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)
- 新版 呼出元 1件 [`00c5af90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5af90.md) · 呼出先 21件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00501950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501950.md) [`0052811c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/0052811c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.36% / 新版 99.36%

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
      "definition_site": "005285f4",
      "incomplete_value": false,
      "site": "005285fc",
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
            "const:9ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005282d4",
      "incomplete_value": false,
      "site": "005282dc",
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
            "const:921:8"
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
      "definition_site": "00528630",
      "incomplete_value": true,
      "site": "0052863c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00528310",
      "incomplete_value": true,
      "site": "0052831c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052862c",
      "incomplete_value": false,
      "site": "0052863c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0052830c",
      "incomplete_value": false,
      "site": "0052831c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 22,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005285f4",
      "PARAM",
      [
        "storage",
        "002ae921",
        null,
        "string"
      ]
    ],
    [
      "0052862c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00528630",
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
      "005285f4",
      "PARAM",
      [
        "storage",
        "002ae9ee",
        null,
        "string"
      ]
    ],
    [
      "0052862c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00528630",
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

- 旧版 [`00527fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md#insn-00527fbc) · [`005282dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md#insn-005282dc) · [`0052831c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md#insn-0052831c)
- 新版 [`005282dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md#insn-005282dc) · [`005285fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md#insn-005285fc) · [`0052863c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md#insn-0052863c)

~~~diff
- 00527fbc ["INT_ADD", "register:40f0:8", ["const:527fbc:8", "const:4:8"]]
- 00527fbc ["CALL", null, ["callee:00c54d60:8"]]
+ 005282dc ["INT_ADD", "register:40f0:8", ["const:5282dc:8", "const:4:8"]]
+ 005282dc ["CALL", null, ["callee:00c54d60:8"]]
- 00527fbc bytes 6daf1c94
+ 005282dc bytes a1b21c94
- 005282dc ["INT_ADD", "register:40f0:8", ["const:5282dc:8", "const:4:8"]]
- 005282dc ["CALL", null, ["callee:0043e138:8"]]
+ 005285fc ["INT_ADD", "register:40f0:8", ["const:5285fc:8", "const:4:8"]]
+ 005285fc ["CALL", null, ["callee:0043e138:8"]]
- 005282dc bytes cf56fc97
+ 005285fc bytes cf56fc97
- 0052831c ["INT_ADD", "register:40f0:8", ["const:52831c:8", "const:4:8"]]
- 0052831c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0052863c ["INT_ADD", "register:40f0:8", ["const:52863c:8", "const:4:8"]]
+ 0052863c ["CALL", null, ["callee:00c58fb0:8"]]
- 0052831c bytes 31bf1c94
+ 0052863c bytes 5dc21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2e3c022a25090f7b16f0778d3d6b353"></a>

### [`005283e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md) → [`00528704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528704.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fd0.md) · 呼出先 29件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0053f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f850.md)
- 新版 呼出元 1件 [`00c5afa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afa0.md) · 呼出先 29件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0053fb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fb70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

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
      "definition_site": "0052915c",
      "incomplete_value": false,
      "site": "00529164",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528e3c",
      "incomplete_value": false,
      "site": "00528e44",
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
            "const:22a:8"
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
      "definition_site": "00529198",
      "incomplete_value": true,
      "site": "005291a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00528e78",
      "incomplete_value": true,
      "site": "00528e84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00529194",
      "incomplete_value": false,
      "site": "005291a4",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00528e74",
      "incomplete_value": false,
      "site": "00528e84",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 58,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052915c",
      "PARAM",
      [
        "storage",
        "002a422a",
        null,
        "string"
      ]
    ],
    [
      "00529194",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00529198",
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
      "0052915c",
      "PARAM",
      [
        "storage",
        "002a42f5",
        null,
        "string"
      ]
    ],
    [
      "00529194",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00529198",
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

- 旧版 [`00528e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md#insn-00528e44) · [`00528e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md#insn-00528e84) · [`00528468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md#insn-00528468)
- 新版 [`00529164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528704.md#insn-00529164) · [`005291a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528704.md#insn-005291a4) · [`00528788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528704.md#insn-00528788)

~~~diff
- 00528e44 ["INT_ADD", "register:40f0:8", ["const:528e44:8", "const:4:8"]]
- 00528e44 ["CALL", null, ["callee:0043e138:8"]]
+ 00529164 ["INT_ADD", "register:40f0:8", ["const:529164:8", "const:4:8"]]
+ 00529164 ["CALL", null, ["callee:0043e138:8"]]
- 00528e44 bytes f553fc97
+ 00529164 bytes f553fc97
- 00528e84 ["INT_ADD", "register:40f0:8", ["const:528e84:8", "const:4:8"]]
- 00528e84 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005291a4 ["INT_ADD", "register:40f0:8", ["const:5291a4:8", "const:4:8"]]
+ 005291a4 ["CALL", null, ["callee:00c58fb0:8"]]
- 00528e84 bytes 57bc1c94
+ 005291a4 bytes 83bf1c94
- 00528468 ["INT_ADD", "register:40f0:8", ["const:528468:8", "const:4:8"]]
- 00528468 ["CALL", null, ["callee:00c58f30:8"]]
+ 00528788 ["INT_ADD", "register:40f0:8", ["const:528788:8", "const:4:8"]]
+ 00528788 ["CALL", null, ["callee:00c58f30:8"]]
- 00528468 bytes bebe1c94
+ 00528788 bytes eac11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90d54c1157fd29de561d38ca07fdb78"></a>

### [`00528fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md) → [`005292e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/005292e0.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fe0.md) · 呼出先 16件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00548d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548d5c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`00c5afb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afb0.md) · 呼出先 16件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0054907c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/0054907c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00529528",
      "incomplete_value": false,
      "site": "00529548",
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
            "const:864:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529208",
      "incomplete_value": false,
      "site": "00529228",
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
            "const:70c:8"
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
      "definition_site": "00529530",
      "incomplete_value": false,
      "site": "00529548",
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
      "definition_site": "00529210",
      "incomplete_value": false,
      "site": "00529228",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00529538",
      "incomplete_value": false,
      "site": "00529548",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529218",
      "incomplete_value": false,
      "site": "00529228",
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
            "const:1cb:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00529528",
      "PARAM",
      [
        "storage",
        "002a670c",
        null,
        "string"
      ]
    ],
    [
      "00529530",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00529538",
      "PARAM",
      [
        "storage",
        "002b61cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00529528",
      "PARAM",
      [
        "storage",
        "002a6864",
        null,
        "string"
      ]
    ],
    [
      "00529530",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00529538",
      "PARAM",
      [
        "storage",
        "002b629a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md#insn-00529228) · [`00529244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md#insn-00529244) · [`00529280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md#insn-00529280)
- 新版 [`00529548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/005292e0.md#insn-00529548) · [`00529564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/005292e0.md#insn-00529564) · [`005295a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/005292e0.md#insn-005295a0)

~~~diff
- 00529228 ["INT_ADD", "register:40f0:8", ["const:529228:8", "const:4:8"]]
- 00529228 ["CALL", null, ["callee:00c596f0:8"]]
+ 00529548 ["INT_ADD", "register:40f0:8", ["const:529548:8", "const:4:8"]]
+ 00529548 ["CALL", null, ["callee:00c596f0:8"]]
- 00529228 bytes 3ebd1c94
+ 00529548 bytes 6ac01c94
- 00529244 ["INT_ADD", "register:40f0:8", ["const:529244:8", "const:4:8"]]
- 00529244 ["CALL", null, ["callee:0043e138:8"]]
+ 00529564 ["INT_ADD", "register:40f0:8", ["const:529564:8", "const:4:8"]]
+ 00529564 ["CALL", null, ["callee:0043e138:8"]]
- 00529244 bytes f552fc97
+ 00529564 bytes f552fc97
- 00529280 ["INT_ADD", "register:40f0:8", ["const:529280:8", "const:4:8"]]
- 00529280 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005295a0 ["INT_ADD", "register:40f0:8", ["const:5295a0:8", "const:4:8"]]
+ 005295a0 ["CALL", null, ["callee:00c58fb0:8"]]
- 00529280 bytes 58bb1c94
+ 005295a0 bytes 84be1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf6938746855becdb197ea9fd4c121a1"></a>

### [`00529374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md) → [`00529694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/00529694.md) _ZN5Botan4PKIX22build_certificate_pathERNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certi

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00540910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540910.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00502b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b58.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00540c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.43% / 新版 99.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005298fc",
      "incomplete_value": true,
      "site": "005298fc",
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
      "definition_site": "005295dc",
      "incomplete_value": true,
      "site": "005295dc",
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
      "005298f0",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "005298fc",
      "DATA",
      [
        "storage",
        "00c67868",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "005298f0",
      "READ",
      [
        "storage",
        "00c9c198",
        null,
        "pointer"
      ]
    ],
    [
      "005298fc",
      "DATA",
      [
        "storage",
        "00c68838",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005293b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md#insn-005293b8) · [`00529404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md#insn-00529404) · [`00529418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md#insn-00529418)
- 新版 [`005296d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/00529694.md#insn-005296d8) · [`00529724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/00529694.md#insn-00529724) · [`00529738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/00529694.md#insn-00529738)

~~~diff
- 005293b8 ["INT_ADD", "register:40f0:8", ["const:5293b8:8", "const:4:8"]]
- 005293b8 ["CALL", null, ["callee:00c5aa90:8"]]
+ 005296d8 ["INT_ADD", "register:40f0:8", ["const:5296d8:8", "const:4:8"]]
+ 005296d8 ["CALL", null, ["callee:00c5aa90:8"]]
- 005293b8 bytes c2c11c94
+ 005296d8 bytes eec41c94
- 00529404 ["INT_ADD", "register:40f0:8", ["const:529404:8", "const:4:8"]]
- 00529404 ["CALL", null, ["callee:00c54d60:8"]]
+ 00529724 ["INT_ADD", "register:40f0:8", ["const:529724:8", "const:4:8"]]
+ 00529724 ["CALL", null, ["callee:00c54d60:8"]]
- 00529404 bytes 5baa1c94
+ 00529724 bytes 8fad1c94
- 00529418 ["INT_ADD", "register:40f0:8", ["const:529418:8", "const:4:8"]]
- 00529418 ["CALL", null, ["callee:005488f8:8"]]
+ 00529738 ["INT_ADD", "register:40f0:8", ["const:529738:8", "const:4:8"]]
+ 00529738 ["CALL", null, ["callee:005488f8:8"]]
- 00529418 bytes 707c0094
+ 00529738 bytes 707c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2cf0203b82594c3cf4cb29d359da952"></a>

### [`0052b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md) → [`0052b488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b488.md) _ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ff0.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5afc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afc0.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

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
      "definition_site": "0052b898",
      "incomplete_value": false,
      "site": "0052b8a0",
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
            "const:315:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b578",
      "incomplete_value": false,
      "site": "0052b580",
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
            "const:24a:8"
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
      "definition_site": "0052b8d4",
      "incomplete_value": true,
      "site": "0052b8e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052b5b4",
      "incomplete_value": true,
      "site": "0052b5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052b8d0",
      "incomplete_value": false,
      "site": "0052b8e0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0052b5b0",
      "incomplete_value": false,
      "site": "0052b5c0",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0052b898",
      "PARAM",
      [
        "storage",
        "002a424a",
        null,
        "string"
      ]
    ],
    [
      "0052b8d0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0052b8d4",
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
      "0052b898",
      "PARAM",
      [
        "storage",
        "002a4315",
        null,
        "string"
      ]
    ],
    [
      "0052b8d0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0052b8d4",
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

- 旧版 [`0052b580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md#insn-0052b580) · [`0052b5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md#insn-0052b5c0) · [`0052b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md#insn-0052b210)
- 新版 [`0052b8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b488.md#insn-0052b8a0) · [`0052b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b488.md#insn-0052b8e0) · [`0052b530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b488.md#insn-0052b530)

~~~diff
- 0052b580 ["INT_ADD", "register:40f0:8", ["const:52b580:8", "const:4:8"]]
- 0052b580 ["CALL", null, ["callee:0043e138:8"]]
+ 0052b8a0 ["INT_ADD", "register:40f0:8", ["const:52b8a0:8", "const:4:8"]]
+ 0052b8a0 ["CALL", null, ["callee:0043e138:8"]]
- 0052b580 bytes 264afc97
+ 0052b8a0 bytes 264afc97
- 0052b5c0 ["INT_ADD", "register:40f0:8", ["const:52b5c0:8", "const:4:8"]]
- 0052b5c0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0052b8e0 ["INT_ADD", "register:40f0:8", ["const:52b8e0:8", "const:4:8"]]
+ 0052b8e0 ["CALL", null, ["callee:00c58fb0:8"]]
- 0052b5c0 bytes 88b21c94
+ 0052b8e0 bytes b4b51c94
- 0052b210 ["INT_ADD", "register:40f0:8", ["const:52b210:8", "const:4:8"]]
- 0052b210 ["CALL", null, ["callee:0043bf04:8"]]
+ 0052b530 ["INT_ADD", "register:40f0:8", ["const:52b530:8", "const:4:8"]]
+ 0052b530 ["CALL", null, ["callee:0043bf04:8"]]
- 0052b210 bytes 7542fc97
+ 0052b530 bytes 7542fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76a3a2bf569b2efcf1d785b0ce3df9a5"></a>

### [`0052b614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md) → [`0052b934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b934.md) _ZN5Botan4PKIX14overall_statusERKNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a000.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5afd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afd0.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "definition_site": "0052b9fc",
      "incomplete_value": false,
      "site": "0052ba04",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b6dc",
      "incomplete_value": false,
      "site": "0052b6e4",
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
            "const:cbe:8"
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
      "definition_site": "0052ba38",
      "incomplete_value": true,
      "site": "0052ba44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052b718",
      "incomplete_value": true,
      "site": "0052b724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052ba34",
      "incomplete_value": false,
      "site": "0052ba44",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0052b714",
      "incomplete_value": false,
      "site": "0052b724",
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
      "0052b9fc",
      "PARAM",
      [
        "storage",
        "002b2cbe",
        null,
        "string"
      ]
    ],
    [
      "0052ba34",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0052ba38",
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
      "0052b9fc",
      "PARAM",
      [
        "storage",
        "002b2d08",
        null,
        "string"
      ]
    ],
    [
      "0052ba34",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0052ba38",
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

- 旧版 [`0052b6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md#insn-0052b6e4) · [`0052b724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md#insn-0052b724) · [`0052b6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md#insn-0052b6d0)
- 新版 [`0052ba04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b934.md#insn-0052ba04) · [`0052ba44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b934.md#insn-0052ba44) · [`0052b9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052b934.md#insn-0052b9f0)

~~~diff
- 0052b6e4 ["INT_ADD", "register:40f0:8", ["const:52b6e4:8", "const:4:8"]]
- 0052b6e4 ["CALL", null, ["callee:0043e138:8"]]
+ 0052ba04 ["INT_ADD", "register:40f0:8", ["const:52ba04:8", "const:4:8"]]
+ 0052ba04 ["CALL", null, ["callee:0043e138:8"]]
- 0052b6e4 bytes cd49fc97
+ 0052ba04 bytes cd49fc97
- 0052b724 ["INT_ADD", "register:40f0:8", ["const:52b724:8", "const:4:8"]]
- 0052b724 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0052ba44 ["INT_ADD", "register:40f0:8", ["const:52ba44:8", "const:4:8"]]
+ 0052ba44 ["CALL", null, ["callee:00c58fb0:8"]]
- 0052b724 bytes 2fb21c94
+ 0052ba44 bytes 5bb51c94
- 0052b6d0 ["INT_ADD", "register:40f0:8", ["const:52b6d0:8", "const:4:8"]]
- 0052b6d0 ["CALL", null, ["callee:00c58f90:8"]]
+ 0052b9f0 ["INT_ADD", "register:40f0:8", ["const:52b9f0:8", "const:4:8"]]
+ 0052b9f0 ["CALL", null, ["callee:00c58f90:8"]]
- 0052b6d0 bytes 3cb21c94
+ 0052b9f0 bytes 68b51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c11555ebd7667505c8e16d0c6e5cc3a"></a>

### [`0052b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md) → [`0052ba98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052ba98.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md) · 呼出先 28件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00529df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529df8.md) [`0052c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md) [`0052c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md)
- 新版 呼出元 1件 [`00c5afe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5afe0.md) · 呼出先 28件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0052a118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052a/0052a118.md) [`0052c5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c5a4.md) [`0052c6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052c/0052c6b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.03% / 新版 99.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052bb10",
      "incomplete_value": true,
      "site": "0052bb14",
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
      "definition_site": "0052b7f0",
      "incomplete_value": true,
      "site": "0052b7f4",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052bb34",
      "incomplete_value": true,
      "site": "0052bb38",
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
      "definition_site": "0052b814",
      "incomplete_value": true,
      "site": "0052b818",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052bc80",
      "value": [
        "leaf",
        "ram:52a118:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b960",
      "value": [
        "leaf",
        "ram:529df8:8"
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
      "0052bb08",
      "READ",
      [
        "storage",
        "00c9b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0052bb14",
      "DATA",
      [
        "storage",
        "00c6a810",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0052bb30",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052bb08",
      "READ",
      [
        "storage",
        "00c9c178",
        null,
        "pointer"
      ]
    ],
    [
      "0052bb14",
      "DATA",
      [
        "storage",
        "00c6b7e0",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0052bb30",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md#insn-0052b960) · [`0052be04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md#insn-0052be04) · [`0052c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md#insn-0052c0e4)
- 新版 [`0052bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052ba98.md#insn-0052bc80) · [`0052c124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052ba98.md#insn-0052c124) · [`0052c404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052b/0052ba98.md#insn-0052c404)

~~~diff
- 0052b960 ["INT_ADD", "register:40f0:8", ["const:52b960:8", "const:4:8"]]
- 0052b960 ["CALL", null, ["ram:529df8:8"]]
+ 0052bc80 ["INT_ADD", "register:40f0:8", ["const:52bc80:8", "const:4:8"]]
+ 0052bc80 ["CALL", null, ["ram:52a118:8"]]
- 0052b960 bytes 26f9ff97
+ 0052bc80 bytes 26f9ff97
- 0052be04 ["INT_ADD", "register:40f0:8", ["const:52be04:8", "const:4:8"]]
- 0052be04 ["CALL", null, ["callee:0053fb70:8"]]
+ 0052c124 ["INT_ADD", "register:40f0:8", ["const:52c124:8", "const:4:8"]]
+ 0052c124 ["CALL", null, ["callee:0053fb70:8"]]
- 0052be04 bytes 934e0094
+ 0052c124 bytes 934e0094
- 0052c0e4 ["INT_ADD", "register:40f0:8", ["const:52c0e4:8", "const:4:8"]]
- 0052c0e4 ["CALL", null, ["callee:0043e138:8"]]
+ 0052c404 ["INT_ADD", "register:40f0:8", ["const:52c404:8", "const:4:8"]]
+ 0052c404 ["CALL", null, ["callee:0043e138:8"]]
- 0052c0e4 bytes 4d47fc97
+ 0052c404 bytes 4d47fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9504794f8c6ef09f2ee29ecfa3032a2"></a>

### [`0052d154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md) → [`0052d474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d474.md) _ZNK5Botan22Path_Validation_Result10trust_rootEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "definition_site": "0052d4e4",
      "incomplete_value": false,
      "site": "0052d4ec",
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
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052d1c4",
      "incomplete_value": false,
      "site": "0052d1cc",
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
            "const:de2:8"
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
      "definition_site": "0052d520",
      "incomplete_value": true,
      "site": "0052d52c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052d200",
      "incomplete_value": true,
      "site": "0052d20c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052d51c",
      "incomplete_value": false,
      "site": "0052d52c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0052d1fc",
      "incomplete_value": false,
      "site": "0052d20c",
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
      "0052d4e4",
      "PARAM",
      [
        "storage",
        "002bede2",
        null,
        "string"
      ]
    ],
    [
      "0052d51c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0052d520",
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
      "0052d4e4",
      "PARAM",
      [
        "storage",
        "002beec0",
        null,
        "string"
      ]
    ],
    [
      "0052d51c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0052d520",
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

- 旧版 [`0052d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md#insn-0052d1cc) · [`0052d20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md#insn-0052d20c) · [`0052d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md#insn-0052d230)
- 新版 [`0052d4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d474.md#insn-0052d4ec) · [`0052d52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d474.md#insn-0052d52c) · [`0052d550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d474.md#insn-0052d550)

~~~diff
- 0052d1cc ["INT_ADD", "register:40f0:8", ["const:52d1cc:8", "const:4:8"]]
- 0052d1cc ["CALL", null, ["callee:0043e138:8"]]
+ 0052d4ec ["INT_ADD", "register:40f0:8", ["const:52d4ec:8", "const:4:8"]]
+ 0052d4ec ["CALL", null, ["callee:0043e138:8"]]
- 0052d1cc bytes 1343fc97
+ 0052d4ec bytes 1343fc97
- 0052d20c ["INT_ADD", "register:40f0:8", ["const:52d20c:8", "const:4:8"]]
- 0052d20c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0052d52c ["INT_ADD", "register:40f0:8", ["const:52d52c:8", "const:4:8"]]
+ 0052d52c ["CALL", null, ["callee:00c58fb0:8"]]
- 0052d20c bytes 75ab1c94
+ 0052d52c bytes a1ae1c94
- 0052d230 ["INT_ADD", "register:40f0:8", ["const:52d230:8", "const:4:8"]]
- 0052d230 ["CALL", null, ["callee:0043e138:8"]]
+ 0052d550 ["INT_ADD", "register:40f0:8", ["const:52d550:8", "const:4:8"]]
+ 0052d550 ["CALL", null, ["callee:0043e138:8"]]
- 0052d230 bytes fa42fc97
+ 0052d550 bytes fa42fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a0059b3d54fbe78b70a335a441e45c1"></a>

### [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) → [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) _ZN5Botan4X50923create_self_signed_certERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9al

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 27件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004c0ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md) [`00500f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f4c.md) [`00505314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`004c0dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0dd8.md) [`0050126c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/0050126c.md) [`00505634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505634.md) [`005103c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.23% / 新版 95.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052d8c4",
      "incomplete_value": true,
      "site": "0052d8c4",
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
      "definition_site": "0052d5a4",
      "incomplete_value": true,
      "site": "0052d5a4",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0052d910",
      "incomplete_value": true,
      "site": "0052d910",
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
      "definition_site": "0052d5f0",
      "incomplete_value": true,
      "site": "0052d5f0",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0052da78",
      "incomplete_value": true,
      "site": "0052da80",
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
      "definition_site": "0052d758",
      "incomplete_value": true,
      "site": "0052d760",
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
      "0052d8ac",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0052d8c4",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052d8fc",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052d8ac",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0052d8c4",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052d8fc",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052d654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md#insn-0052d654) · [`0052d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md#insn-0052d578) · [`0052d58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md#insn-0052d58c)
- 新版 [`0052d974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md#insn-0052d974) · [`0052d898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md#insn-0052d898) · [`0052d8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md#insn-0052d8ac)

~~~diff
- 0052d654 ["INT_ADD", "register:40f0:8", ["const:52d654:8", "const:4:8"]]
- 0052d654 ["CALL", null, ["callee:0052df6c:8"]]
+ 0052d974 ["INT_ADD", "register:40f0:8", ["const:52d974:8", "const:4:8"]]
+ 0052d974 ["CALL", null, ["callee:0052df6c:8"]]
- 0052d654 bytes 7e010094
+ 0052d974 bytes 7e010094
- 0052d578 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0052d898 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0052d578 bytes 693b00b0
+ 0052d898 bytes 693b00d0
- 0052d58c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e08:8"]]
- 0052d58c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052d8ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
+ 0052d8ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052d58c bytes 290547f9
+ 0052d8ac bytes 29ed46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce3deb148f71c526fec6abd3abe07776"></a>

### [`0052de5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md) → [`0052e17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e17c.md) FUN_0052e17c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 10件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 10件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`004ff6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff6dc.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.54% / 新版 87.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e1c4",
      "incomplete_value": true,
      "site": "0052e1c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:67a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052dea4",
      "incomplete_value": true,
      "site": "0052dea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:522:8"
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
      "definition_site": "0052e1bc",
      "incomplete_value": true,
      "site": "0052e1c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0052de9c",
      "incomplete_value": true,
      "site": "0052dea8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e22c",
      "incomplete_value": true,
      "site": "0052e22c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052df0c",
      "incomplete_value": true,
      "site": "0052df0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d6:8"
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
      "0052e1a4",
      "READ",
      [
        "storage",
        "002a6522",
        null,
        "string"
      ]
    ],
    [
      "0052e1bc",
      "READ",
      [
        "storage",
        "002a6529",
        null,
        "string"
      ]
    ],
    [
      "0052e218",
      "READ",
      [
        "storage",
        "002bb2d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0052e1a4",
      "READ",
      [
        "storage",
        "002a667a",
        null,
        "string"
      ]
    ],
    [
      "0052e1bc",
      "READ",
      [
        "storage",
        "002a6681",
        null,
        "string"
      ]
    ],
    [
      "0052e218",
      "READ",
      [
        "storage",
        "002bb3b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052dee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md#insn-0052dee8) · [`0052de7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md#insn-0052de7c) · [`0052deb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md#insn-0052deb8)
- 新版 [`0052e208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e17c.md#insn-0052e208) · [`0052e19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e17c.md#insn-0052e19c) · [`0052e1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e17c.md#insn-0052e1d8)

~~~diff
- 0052dee8 ["INT_ADD", "register:40f0:8", ["const:52dee8:8", "const:4:8"]]
- 0052dee8 ["CALL", null, ["callee:00c58f50:8"]]
+ 0052e208 ["INT_ADD", "register:40f0:8", ["const:52e208:8", "const:4:8"]]
+ 0052e208 ["CALL", null, ["callee:00c58f50:8"]]
- 0052dee8 bytes 26a81c94
+ 0052e208 bytes 52ab1c94
- 0052de7c ["COPY", "tmp:0:8", ["const:522:8"]]
- 0052de7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0052de7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0052de7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0052e19c ["COPY", "tmp:0:8", ["const:67a:8"]]
+ 0052e19c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0052e19c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0052e19c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0052de7c bytes 29891491
+ 0052e19c bytes 29e91991
- 0052deb8 ["INT_ADD", "register:40f0:8", ["const:52deb8:8", "const:4:8"]]
- 0052deb8 ["CALL", null, ["callee:00c59720:8"]]
+ 0052e1d8 ["INT_ADD", "register:40f0:8", ["const:52e1d8:8", "const:4:8"]]
+ 0052e1d8 ["CALL", null, ["callee:00c59720:8"]]
- 0052deb8 bytes 26aa1c94
+ 0052e1d8 bytes 52ad1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59feb04dea703a8a5064e34406737976"></a>

### [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) → [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) _ZN5Botan4X50915create_cert_reqERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorI

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`004c0ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md) [`00500f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f4c.md) [`00505314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`004c0dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c0/004c0dd8.md) [`0050126c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/0050126c.md) [`00505634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505634.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.73% / 新版 93.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 5件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e6e8",
      "incomplete_value": true,
      "site": "0052e6e8",
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
      "definition_site": "0052e3c8",
      "incomplete_value": true,
      "site": "0052e3c8",
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
      "definition_site": "0052e734",
      "incomplete_value": true,
      "site": "0052e734",
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
      "definition_site": "0052e414",
      "incomplete_value": true,
      "site": "0052e414",
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
      "definition_site": "0052e898",
      "incomplete_value": true,
      "site": "0052e8a0",
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
      "definition_site": "0052e578",
      "incomplete_value": true,
      "site": "0052e580",
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
      "0052e6d0",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0052e6e8",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052e720",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052e6d0",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0052e6e8",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052e720",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md#insn-0052e478) · [`0052e598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md#insn-0052e598) · [`0052e5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md#insn-0052e5a0)
- 新版 [`0052e798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md#insn-0052e798) · [`0052e8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md#insn-0052e8b8) · [`0052e8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md#insn-0052e8c0)

~~~diff
- 0052e478 ["INT_ADD", "register:40f0:8", ["const:52e478:8", "const:4:8"]]
- 0052e478 ["CALL", null, ["callee:0052df6c:8"]]
+ 0052e798 ["INT_ADD", "register:40f0:8", ["const:52e798:8", "const:4:8"]]
+ 0052e798 ["CALL", null, ["callee:0052df6c:8"]]
- 0052e478 bytes f5fdff97
+ 0052e798 bytes f5fdff97
- 0052e598 ["INT_ADD", "register:40f0:8", ["const:52e598:8", "const:4:8"]]
- 0052e598 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052e8b8 ["INT_ADD", "register:40f0:8", ["const:52e8b8:8", "const:4:8"]]
+ 0052e8b8 ["CALL", null, ["callee:00c58f30:8"]]
- 0052e598 bytes 72a61c94
+ 0052e8b8 bytes 9ea91c94
- 0052e5a0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0052e8c0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0052e5a0 bytes 683b00b0
+ 0052e8c0 bytes 683b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1fc2963a5fea8d9977487f8bff56e6a"></a>

### [`0052f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md) → [`0052f320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f320.md) FUN_0052f320

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f0f4.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f414.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f358",
      "incomplete_value": true,
      "site": "0052f358",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f038",
      "incomplete_value": true,
      "site": "0052f038",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f384",
      "incomplete_value": true,
      "site": "0052f384",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f064",
      "incomplete_value": true,
      "site": "0052f064",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f3b0",
      "incomplete_value": true,
      "site": "0052f3b0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f090",
      "incomplete_value": true,
      "site": "0052f090",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052f348",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f374",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f3a0",
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
      "0052f348",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f374",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f3a0",
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

- 旧版 [`0052f038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md#insn-0052f038) · [`0052f064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md#insn-0052f064) · [`0052f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md#insn-0052f090)
- 新版 [`0052f358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f320.md#insn-0052f358) · [`0052f384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f320.md#insn-0052f384) · [`0052f3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f320.md#insn-0052f3b0)

~~~diff
- 0052f038 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f038 ["INT_ADD", "register:40f0:8", ["const:52f038:8", "const:4:8"]]
- 0052f038 ["CALLIND", null, ["register:0:8"]]
+ 0052f358 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f358 ["INT_ADD", "register:40f0:8", ["const:52f358:8", "const:4:8"]]
+ 0052f358 ["CALLIND", null, ["register:0:8"]]
- 0052f038 bytes 20013fd6
+ 0052f358 bytes 20013fd6
- 0052f064 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f064 ["INT_ADD", "register:40f0:8", ["const:52f064:8", "const:4:8"]]
- 0052f064 ["CALLIND", null, ["register:0:8"]]
+ 0052f384 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f384 ["INT_ADD", "register:40f0:8", ["const:52f384:8", "const:4:8"]]
+ 0052f384 ["CALLIND", null, ["register:0:8"]]
- 0052f064 bytes 20013fd6
+ 0052f384 bytes 20013fd6
- 0052f090 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f090 ["INT_ADD", "register:40f0:8", ["const:52f090:8", "const:4:8"]]
- 0052f090 ["CALLIND", null, ["register:0:8"]]
+ 0052f3b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f3b0 ["INT_ADD", "register:40f0:8", ["const:52f3b0:8", "const:4:8"]]
+ 0052f3b0 ["CALLIND", null, ["register:0:8"]]
- 0052f090 bytes 20013fd6
+ 0052f3b0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83621c19e068218c461958ad9584c657"></a>

### [`0052f2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md) → [`0052f5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f5c8.md) FUN_0052f5c8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0052f5e4",
      "incomplete_value": true,
      "site": "0052f5e8",
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
      "definition_site": "0052f2c4",
      "incomplete_value": true,
      "site": "0052f2c8",
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
      "0052f5e0",
      "READ",
      [
        "storage",
        "00c9aee0",
        null,
        "pointer"
      ]
    ],
    [
      "0052f5e8",
      "DATA",
      [
        "storage",
        "00c67ba0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f5e0",
      "READ",
      [
        "storage",
        "00c9beb0",
        null,
        "pointer"
      ]
    ],
    [
      "0052f5e8",
      "DATA",
      [
        "storage",
        "00c68b70",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md#insn-0052f2b4) · [`0052f2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md#insn-0052f2b8) · [`0052f2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md#insn-0052f2c0)
- 新版 [`0052f5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f5c8.md#insn-0052f5d4) · [`0052f5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f5c8.md#insn-0052f5d8) · [`0052f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f5c8.md#insn-0052f5e0)

~~~diff
- 0052f2b4 ["INT_ADD", "register:40f0:8", ["const:52f2b4:8", "const:4:8"]]
- 0052f2b4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052f5d4 ["INT_ADD", "register:40f0:8", ["const:52f5d4:8", "const:4:8"]]
+ 0052f5d4 ["CALL", null, ["callee:00c58f30:8"]]
- 0052f2b4 bytes 2ba31c94
+ 0052f5d4 bytes 57a61c94
- 0052f2b8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052f5d8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052f2b8 bytes 483b00f0
+ 0052f5d8 bytes 683b0090
- 0052f2c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 0052f2c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f5e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
+ 0052f5e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f2c0 bytes 087147f9
+ 0052f5e0 bytes 085947f9
~~~


<a id="compare-5927b2f36e60e6e20c6fd6b0b6cd2d5e"></a>

### [`0052f2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md) → [`0052f60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f60c.md) FUN_0052f60c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f3e0.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f700.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f644",
      "incomplete_value": true,
      "site": "0052f644",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f324",
      "incomplete_value": true,
      "site": "0052f324",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f670",
      "incomplete_value": true,
      "site": "0052f670",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f350",
      "incomplete_value": true,
      "site": "0052f350",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f69c",
      "incomplete_value": true,
      "site": "0052f69c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f37c",
      "incomplete_value": true,
      "site": "0052f37c",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052f634",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f660",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f68c",
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
      "0052f634",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f660",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f68c",
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

- 旧版 [`0052f324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md#insn-0052f324) · [`0052f350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md#insn-0052f350) · [`0052f37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md#insn-0052f37c)
- 新版 [`0052f644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f60c.md#insn-0052f644) · [`0052f670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f60c.md#insn-0052f670) · [`0052f69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f60c.md#insn-0052f69c)

~~~diff
- 0052f324 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f324 ["INT_ADD", "register:40f0:8", ["const:52f324:8", "const:4:8"]]
- 0052f324 ["CALLIND", null, ["register:0:8"]]
+ 0052f644 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f644 ["INT_ADD", "register:40f0:8", ["const:52f644:8", "const:4:8"]]
+ 0052f644 ["CALLIND", null, ["register:0:8"]]
- 0052f324 bytes 20013fd6
+ 0052f644 bytes 20013fd6
- 0052f350 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f350 ["INT_ADD", "register:40f0:8", ["const:52f350:8", "const:4:8"]]
- 0052f350 ["CALLIND", null, ["register:0:8"]]
+ 0052f670 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f670 ["INT_ADD", "register:40f0:8", ["const:52f670:8", "const:4:8"]]
+ 0052f670 ["CALLIND", null, ["register:0:8"]]
- 0052f350 bytes 20013fd6
+ 0052f670 bytes 20013fd6
- 0052f37c ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f37c ["INT_ADD", "register:40f0:8", ["const:52f37c:8", "const:4:8"]]
- 0052f37c ["CALLIND", null, ["register:0:8"]]
+ 0052f69c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f69c ["INT_ADD", "register:40f0:8", ["const:52f69c:8", "const:4:8"]]
+ 0052f69c ["CALLIND", null, ["register:0:8"]]
- 0052f37c bytes 20013fd6
+ 0052f69c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9b64dde925146e9413570affbb8a34"></a>

### [`0052f594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md) → [`0052f8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8b4.md) FUN_0052f8b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0052f8d0",
      "incomplete_value": true,
      "site": "0052f8d4",
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
      "definition_site": "0052f5b0",
      "incomplete_value": true,
      "site": "0052f5b4",
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
      "0052f8cc",
      "READ",
      [
        "storage",
        "00c9aee8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f8d4",
      "DATA",
      [
        "storage",
        "00c67c78",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f8cc",
      "READ",
      [
        "storage",
        "00c9beb8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f8d4",
      "DATA",
      [
        "storage",
        "00c68c48",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md#insn-0052f5a0) · [`0052f5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md#insn-0052f5a4) · [`0052f5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md#insn-0052f5ac)
- 新版 [`0052f8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8b4.md#insn-0052f8c0) · [`0052f8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8b4.md#insn-0052f8c4) · [`0052f8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8b4.md#insn-0052f8cc)

~~~diff
- 0052f5a0 ["INT_ADD", "register:40f0:8", ["const:52f5a0:8", "const:4:8"]]
- 0052f5a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0052f8c0 ["INT_ADD", "register:40f0:8", ["const:52f8c0:8", "const:4:8"]]
+ 0052f8c0 ["CALL", null, ["callee:00c58f30:8"]]
- 0052f5a0 bytes 70a21c94
+ 0052f8c0 bytes 9ca51c94
- 0052f5a4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052f8c4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052f5a4 bytes 483b00f0
+ 0052f8c4 bytes 683b0090
- 0052f5ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
- 0052f5ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f8cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb8:8"]]
+ 0052f8cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f5ac bytes 087547f9
+ 0052f8cc bytes 085d47f9
~~~


<a id="compare-c0930fbb57f61076d120f07789314c4e"></a>

### [`0052f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md) → [`0052f8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8f8.md) FUN_0052f8f8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f6cc.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f9ec.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f930",
      "incomplete_value": true,
      "site": "0052f930",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f610",
      "incomplete_value": true,
      "site": "0052f610",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f95c",
      "incomplete_value": true,
      "site": "0052f95c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f63c",
      "incomplete_value": true,
      "site": "0052f63c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f988",
      "incomplete_value": true,
      "site": "0052f988",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052f668",
      "incomplete_value": true,
      "site": "0052f668",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052f920",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f94c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f978",
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
      "0052f920",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f94c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f978",
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

- 旧版 [`0052f610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md#insn-0052f610) · [`0052f63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md#insn-0052f63c) · [`0052f668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md#insn-0052f668)
- 新版 [`0052f930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8f8.md#insn-0052f930) · [`0052f95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8f8.md#insn-0052f95c) · [`0052f988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052f8f8.md#insn-0052f988)

~~~diff
- 0052f610 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f610 ["INT_ADD", "register:40f0:8", ["const:52f610:8", "const:4:8"]]
- 0052f610 ["CALLIND", null, ["register:0:8"]]
+ 0052f930 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f930 ["INT_ADD", "register:40f0:8", ["const:52f930:8", "const:4:8"]]
+ 0052f930 ["CALLIND", null, ["register:0:8"]]
- 0052f610 bytes 20013fd6
+ 0052f930 bytes 20013fd6
- 0052f63c ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f63c ["INT_ADD", "register:40f0:8", ["const:52f63c:8", "const:4:8"]]
- 0052f63c ["CALLIND", null, ["register:0:8"]]
+ 0052f95c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f95c ["INT_ADD", "register:40f0:8", ["const:52f95c:8", "const:4:8"]]
+ 0052f95c ["CALLIND", null, ["register:0:8"]]
- 0052f63c bytes 20013fd6
+ 0052f95c bytes 20013fd6
- 0052f668 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f668 ["INT_ADD", "register:40f0:8", ["const:52f668:8", "const:4:8"]]
- 0052f668 ["CALLIND", null, ["register:0:8"]]
+ 0052f988 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f988 ["INT_ADD", "register:40f0:8", ["const:52f988:8", "const:4:8"]]
+ 0052f988 ["CALLIND", null, ["register:0:8"]]
- 0052f668 bytes 20013fd6
+ 0052f988 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f270dabde947fccb9c14ea20f87935"></a>

### [`0052f880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md) → [`0052fba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fba0.md) FUN_0052fba0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0052fbbc",
      "incomplete_value": true,
      "site": "0052fbc0",
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
      "definition_site": "0052f89c",
      "incomplete_value": true,
      "site": "0052f8a0",
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
      "0052fbb8",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0052fbc0",
      "DATA",
      [
        "storage",
        "00c67d28",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052fbb8",
      "READ",
      [
        "storage",
        "00c9bec0",
        null,
        "pointer"
      ]
    ],
    [
      "0052fbc0",
      "DATA",
      [
        "storage",
        "00c68cf8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md#insn-0052f88c) · [`0052f890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md#insn-0052f890) · [`0052f898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md#insn-0052f898)
- 新版 [`0052fbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fba0.md#insn-0052fbac) · [`0052fbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fba0.md#insn-0052fbb0) · [`0052fbb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fba0.md#insn-0052fbb8)

~~~diff
- 0052f88c ["INT_ADD", "register:40f0:8", ["const:52f88c:8", "const:4:8"]]
- 0052f88c ["CALL", null, ["callee:00c58f30:8"]]
+ 0052fbac ["INT_ADD", "register:40f0:8", ["const:52fbac:8", "const:4:8"]]
+ 0052fbac ["CALL", null, ["callee:00c58f30:8"]]
- 0052f88c bytes b5a11c94
+ 0052fbac bytes e1a41c94
- 0052f890 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052fbb0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052f890 bytes 483b00f0
+ 0052fbb0 bytes 683b0090
- 0052f898 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 0052f898 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
+ 0052fbb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f898 bytes 087947f9
+ 0052fbb8 bytes 086147f9
~~~


<a id="compare-cf168fe362276fec21c3d5d72ff3f91a"></a>

### [`0052f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md) → [`0052fbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fbfc.md) FUN_0052fbfc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fc30",
      "incomplete_value": true,
      "site": "0052fc30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052f910",
      "incomplete_value": true,
      "site": "0052f910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052fc20",
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
      "0052fc20",
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

- 旧版 [`0052f910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md#insn-0052f910) · [`0052f8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md#insn-0052f8f8) · [`0052f900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md#insn-0052f900)
- 新版 [`0052fc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fbfc.md#insn-0052fc30) · [`0052fc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fbfc.md#insn-0052fc18) · [`0052fc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fbfc.md#insn-0052fc20)

~~~diff
- 0052f910 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f910 ["INT_ADD", "register:40f0:8", ["const:52f910:8", "const:4:8"]]
- 0052f910 ["CALLIND", null, ["register:0:8"]]
+ 0052fc30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fc30 ["INT_ADD", "register:40f0:8", ["const:52fc30:8", "const:4:8"]]
+ 0052fc30 ["CALLIND", null, ["register:0:8"]]
- 0052f910 bytes 20013fd6
+ 0052fc30 bytes 20013fd6
- 0052f8f8 ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 0052fc18 ["COPY", "register:4048:8", ["const:c68000:8"]]
- 0052f8f8 bytes c9390090
+ 0052fc18 bytes c93900b0
- 0052f900 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
- 0052f900 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fc20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d8:8"]]
+ 0052fc20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f900 bytes 290544f9
+ 0052fc20 bytes 29ed43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1582ef97499d610c37e515b6ce6de5bd"></a>

### [`0052f960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md) → [`0052fc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fc80.md) FUN_0052fc80

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fc9c",
      "incomplete_value": true,
      "site": "0052fca0",
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
      "definition_site": "0052f97c",
      "incomplete_value": true,
      "site": "0052f980",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fcc4",
      "incomplete_value": true,
      "site": "0052fcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052f9a4",
      "incomplete_value": true,
      "site": "0052f9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052fc94",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "0052fca0",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fcb4",
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
      "0052fc94",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "0052fca0",
      "DATA",
      [
        "storage",
        "00c674c0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fcb4",
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

- 旧版 [`0052f9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md#insn-0052f9a4) · [`0052f96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md#insn-0052f96c) · [`0052f974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md#insn-0052f974)
- 新版 [`0052fcc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fc80.md#insn-0052fcc4) · [`0052fc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fc80.md#insn-0052fc8c) · [`0052fc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fc80.md#insn-0052fc94)

~~~diff
- 0052f9a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f9a4 ["INT_ADD", "register:40f0:8", ["const:52f9a4:8", "const:4:8"]]
- 0052f9a4 ["CALLIND", null, ["register:0:8"]]
+ 0052fcc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fcc4 ["INT_ADD", "register:40f0:8", ["const:52fcc4:8", "const:4:8"]]
+ 0052fcc4 ["CALLIND", null, ["register:0:8"]]
- 0052f9a4 bytes 20013fd6
+ 0052fcc4 bytes 20013fd6
- 0052f96c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052fc8c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052f96c bytes 483b00f0
+ 0052fc8c bytes 683b0090
- 0052f974 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 0052f974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fc94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 0052fc94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f974 bytes 088147f9
+ 0052fc94 bytes 086947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30376c53e64fea511992e05062229f6b"></a>

### [`0052f9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md) → [`0052fd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fd14.md) FUN_0052fd14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fd30",
      "incomplete_value": true,
      "site": "0052fd34",
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
      "definition_site": "0052fa10",
      "incomplete_value": true,
      "site": "0052fa14",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fd58",
      "incomplete_value": true,
      "site": "0052fd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052fa38",
      "incomplete_value": true,
      "site": "0052fa38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052fd28",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "0052fd34",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fd48",
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
      "0052fd28",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "0052fd34",
      "DATA",
      [
        "storage",
        "00c674c0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fd48",
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

- 旧版 [`0052fa38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md#insn-0052fa38) · [`0052fa00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md#insn-0052fa00) · [`0052fa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md#insn-0052fa08)
- 新版 [`0052fd58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fd14.md#insn-0052fd58) · [`0052fd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fd14.md#insn-0052fd20) · [`0052fd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fd14.md#insn-0052fd28)

~~~diff
- 0052fa38 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fa38 ["INT_ADD", "register:40f0:8", ["const:52fa38:8", "const:4:8"]]
- 0052fa38 ["CALLIND", null, ["register:0:8"]]
+ 0052fd58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fd58 ["INT_ADD", "register:40f0:8", ["const:52fd58:8", "const:4:8"]]
+ 0052fd58 ["CALLIND", null, ["register:0:8"]]
- 0052fa38 bytes 20013fd6
+ 0052fd58 bytes 20013fd6
- 0052fa00 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052fd20 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052fa00 bytes 483b00f0
+ 0052fd20 bytes 683b0090
- 0052fa08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 0052fa08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fd28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 0052fd28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fa08 bytes 088147f9
+ 0052fd28 bytes 086947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53df68ba3decab7399c4e4dc6de90453"></a>

### [`0052fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md) → [`0052fdac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fdac.md) FUN_0052fdac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fdc8",
      "incomplete_value": true,
      "site": "0052fdcc",
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
      "definition_site": "0052faa8",
      "incomplete_value": true,
      "site": "0052faac",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fdf0",
      "incomplete_value": true,
      "site": "0052fdf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0052fad0",
      "incomplete_value": true,
      "site": "0052fad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0052fdc0",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "0052fdcc",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fde0",
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
      "0052fdc0",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "0052fdcc",
      "DATA",
      [
        "storage",
        "00c674c0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fde0",
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

- 旧版 [`0052fad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md#insn-0052fad0) · [`0052fa98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md#insn-0052fa98) · [`0052faa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md#insn-0052faa0)
- 新版 [`0052fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fdac.md#insn-0052fdf0) · [`0052fdb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fdac.md#insn-0052fdb8) · [`0052fdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fdac.md#insn-0052fdc0)

~~~diff
- 0052fad0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fad0 ["INT_ADD", "register:40f0:8", ["const:52fad0:8", "const:4:8"]]
- 0052fad0 ["CALLIND", null, ["register:0:8"]]
+ 0052fdf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fdf0 ["INT_ADD", "register:40f0:8", ["const:52fdf0:8", "const:4:8"]]
+ 0052fdf0 ["CALLIND", null, ["register:0:8"]]
- 0052fad0 bytes 20013fd6
+ 0052fdf0 bytes 20013fd6
- 0052fa98 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0052fdb8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052fa98 bytes 483b00f0
+ 0052fdb8 bytes 683b0090
- 0052faa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 0052faa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fdc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 0052fdc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052faa0 bytes 088147f9
+ 0052fdc0 bytes 086947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9584f74de1945f674cde7f968dfb3597"></a>

### [`0052fb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md) → [`0052fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fe40.md) FUN_0052fe40

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fe64",
      "incomplete_value": true,
      "site": "0052fe68",
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
      "definition_site": "0052fb44",
      "incomplete_value": true,
      "site": "0052fb48",
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
      "definition_site": "0052fea0",
      "incomplete_value": true,
      "site": "0052fea4",
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
      "definition_site": "0052fb80",
      "incomplete_value": true,
      "site": "0052fb84",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0052fe88",
      "incomplete_value": true,
      "site": "0052fe88",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052fb68",
      "incomplete_value": true,
      "site": "0052fb68",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052fe5c",
      "READ",
      [
        "storage",
        "00c9b068",
        null,
        "pointer"
      ]
    ],
    [
      "0052fe68",
      "DATA",
      [
        "storage",
        "00c67ff0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fe78",
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
      "0052fe5c",
      "READ",
      [
        "storage",
        "00c9c038",
        null,
        "pointer"
      ]
    ],
    [
      "0052fe68",
      "DATA",
      [
        "storage",
        "00c68fc0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fe78",
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

- 旧版 [`0052fb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md#insn-0052fb68) · [`0052fba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md#insn-0052fba4) · [`0052fb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md#insn-0052fb30)
- 新版 [`0052fe88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fe40.md#insn-0052fe88) · [`0052fec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fe40.md#insn-0052fec4) · [`0052fe50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052fe40.md#insn-0052fe50)

~~~diff
- 0052fb68 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fb68 ["INT_ADD", "register:40f0:8", ["const:52fb68:8", "const:4:8"]]
- 0052fb68 ["CALLIND", null, ["register:0:8"]]
+ 0052fe88 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fe88 ["INT_ADD", "register:40f0:8", ["const:52fe88:8", "const:4:8"]]
+ 0052fe88 ["CALLIND", null, ["register:0:8"]]
- 0052fb68 bytes 20013fd6
+ 0052fe88 bytes 20013fd6
- 0052fba4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fba4 ["INT_ADD", "register:40f0:8", ["const:52fba4:8", "const:4:8"]]
- 0052fba4 ["CALLIND", null, ["register:0:8"]]
+ 0052fec4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fec4 ["INT_ADD", "register:40f0:8", ["const:52fec4:8", "const:4:8"]]
+ 0052fec4 ["CALLIND", null, ["register:0:8"]]
- 0052fba4 bytes 20013fd6
+ 0052fec4 bytes 20013fd6
- 0052fb30 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0052fe50 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0052fb30 bytes 683b0090
+ 0052fe50 bytes 683b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fa455075ace77184bdaf65ed271444"></a>

### [`0052fbfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md) → [`0052ff1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052ff1c.md) FUN_0052ff1c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052ff40",
      "incomplete_value": true,
      "site": "0052ff44",
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
      "definition_site": "0052fc20",
      "incomplete_value": true,
      "site": "0052fc24",
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
      "definition_site": "0052ff7c",
      "incomplete_value": true,
      "site": "0052ff80",
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
      "definition_site": "0052fc5c",
      "incomplete_value": true,
      "site": "0052fc60",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0052ff64",
      "incomplete_value": true,
      "site": "0052ff64",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052fc44",
      "incomplete_value": true,
      "site": "0052fc44",
      "value": [
        "LOAD",
        "8",
        [
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
      "0052ff38",
      "READ",
      [
        "storage",
        "00c9b068",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff44",
      "DATA",
      [
        "storage",
        "00c67ff0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052ff54",
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
      "0052ff38",
      "READ",
      [
        "storage",
        "00c9c038",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff44",
      "DATA",
      [
        "storage",
        "00c68fc0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052ff54",
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

- 旧版 [`0052fc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md#insn-0052fc44) · [`0052fc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md#insn-0052fc80) · [`0052fc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md#insn-0052fc0c)
- 新版 [`0052ff64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052ff1c.md#insn-0052ff64) · [`0052ffa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052ff1c.md#insn-0052ffa0) · [`0052ff2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052f/0052ff1c.md#insn-0052ff2c)

~~~diff
- 0052fc44 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fc44 ["INT_ADD", "register:40f0:8", ["const:52fc44:8", "const:4:8"]]
- 0052fc44 ["CALLIND", null, ["register:0:8"]]
+ 0052ff64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052ff64 ["INT_ADD", "register:40f0:8", ["const:52ff64:8", "const:4:8"]]
+ 0052ff64 ["CALLIND", null, ["register:0:8"]]
- 0052fc44 bytes 20013fd6
+ 0052ff64 bytes 20013fd6
- 0052fc80 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fc80 ["INT_ADD", "register:40f0:8", ["const:52fc80:8", "const:4:8"]]
- 0052fc80 ["CALLIND", null, ["register:0:8"]]
+ 0052ffa0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052ffa0 ["INT_ADD", "register:40f0:8", ["const:52ffa0:8", "const:4:8"]]
+ 0052ffa0 ["CALLIND", null, ["register:0:8"]]
- 0052fc80 bytes 20013fd6
+ 0052ffa0 bytes 20013fd6
- 0052fc0c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0052ff2c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0052fc0c bytes 683b0090
+ 0052ff2c bytes 683b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c9a7736a3922e049566ebb6481e6d0b"></a>

### [`0052fce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md) → [`00530000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530000.md) FUN_00530000

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530024",
      "incomplete_value": true,
      "site": "00530028",
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
      "definition_site": "0052fd04",
      "incomplete_value": true,
      "site": "0052fd08",
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
      "definition_site": "00530060",
      "incomplete_value": true,
      "site": "00530064",
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
      "definition_site": "0052fd40",
      "incomplete_value": true,
      "site": "0052fd44",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530048",
      "incomplete_value": true,
      "site": "00530048",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0052fd28",
      "incomplete_value": true,
      "site": "0052fd28",
      "value": [
        "LOAD",
        "8",
        [
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
      "0053001c",
      "READ",
      [
        "storage",
        "00c9b068",
        null,
        "pointer"
      ]
    ],
    [
      "00530028",
      "DATA",
      [
        "storage",
        "00c67ff0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "00530038",
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
      "0053001c",
      "READ",
      [
        "storage",
        "00c9c038",
        null,
        "pointer"
      ]
    ],
    [
      "00530028",
      "DATA",
      [
        "storage",
        "00c68fc0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "00530038",
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

- 旧版 [`0052fd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md#insn-0052fd28) · [`0052fd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md#insn-0052fd64) · [`0052fcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md#insn-0052fcf0)
- 新版 [`00530048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530000.md#insn-00530048) · [`00530084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530000.md#insn-00530084) · [`00530010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530000.md#insn-00530010)

~~~diff
- 0052fd28 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fd28 ["INT_ADD", "register:40f0:8", ["const:52fd28:8", "const:4:8"]]
- 0052fd28 ["CALLIND", null, ["register:0:8"]]
+ 00530048 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530048 ["INT_ADD", "register:40f0:8", ["const:530048:8", "const:4:8"]]
+ 00530048 ["CALLIND", null, ["register:0:8"]]
- 0052fd28 bytes 20013fd6
+ 00530048 bytes 20013fd6
- 0052fd64 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fd64 ["INT_ADD", "register:40f0:8", ["const:52fd64:8", "const:4:8"]]
- 0052fd64 ["CALLIND", null, ["register:0:8"]]
+ 00530084 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530084 ["INT_ADD", "register:40f0:8", ["const:530084:8", "const:4:8"]]
+ 00530084 ["CALLIND", null, ["register:0:8"]]
- 0052fd64 bytes 20013fd6
+ 00530084 bytes 20013fd6
- 0052fcf0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00530010 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0052fcf0 bytes 683b0090
+ 00530010 bytes 683b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9bf3a72ebc93d885d79c0ffe434376d"></a>

### [`0052feb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md) → [`005301d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005301d4.md) FUN_005301d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005301f4",
      "incomplete_value": true,
      "site": "005301f8",
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
      "definition_site": "0052fed4",
      "incomplete_value": true,
      "site": "0052fed8",
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
      "005301e8",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "005301f8",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "005301e8",
      "READ",
      [
        "storage",
        "00c9bee8",
        null,
        "pointer"
      ]
    ],
    [
      "005301f8",
      "DATA",
      [
        "storage",
        "00c67578",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md#insn-0052fec0) · [`0052fec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md#insn-0052fec8) · [`0052fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md#insn-0052fee8)
- 新版 [`005301e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005301d4.md#insn-005301e0) · [`005301e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005301d4.md#insn-005301e8) · [`00530208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005301d4.md#insn-00530208)

~~~diff
- 0052fec0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005301e0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052fec0 bytes 483b00f0
+ 005301e0 bytes 483b00f0
- 0052fec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 0052fec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005301e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
+ 005301e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fec8 bytes 088d47f9
+ 005301e8 bytes 087547f9
- 0052fee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fee8 ["INT_ADD", "register:40f0:8", ["const:52fee8:8", "const:4:8"]]
- 0052fee8 ["CALLIND", null, ["register:0:8"]]
+ 00530208 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00530208 ["INT_ADD", "register:40f0:8", ["const:530208:8", "const:4:8"]]
+ 00530208 ["CALLIND", null, ["register:0:8"]]
- 0052fee8 bytes 00013fd6
+ 00530208 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cfe9478f33d4496d912f178c28c97f9"></a>

### [`0052ff14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md) → [`00530234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530234.md) FUN_00530234

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530254",
      "incomplete_value": true,
      "site": "00530258",
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
      "definition_site": "0052ff34",
      "incomplete_value": true,
      "site": "0052ff38",
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
      "00530248",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "00530258",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "00530248",
      "READ",
      [
        "storage",
        "00c9bee8",
        null,
        "pointer"
      ]
    ],
    [
      "00530258",
      "DATA",
      [
        "storage",
        "00c67578",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ff20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md#insn-0052ff20) · [`0052ff28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md#insn-0052ff28) · [`0052ff48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md#insn-0052ff48)
- 新版 [`00530240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530234.md#insn-00530240) · [`00530248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530234.md#insn-00530248) · [`00530268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530234.md#insn-00530268)

~~~diff
- 0052ff20 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00530240 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052ff20 bytes 483b00f0
+ 00530240 bytes 483b00f0
- 0052ff28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 0052ff28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530248 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
+ 00530248 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052ff28 bytes 088d47f9
+ 00530248 bytes 087547f9
- 0052ff48 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ff48 ["INT_ADD", "register:40f0:8", ["const:52ff48:8", "const:4:8"]]
- 0052ff48 ["CALLIND", null, ["register:0:8"]]
+ 00530268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00530268 ["INT_ADD", "register:40f0:8", ["const:530268:8", "const:4:8"]]
+ 00530268 ["CALLIND", null, ["register:0:8"]]
- 0052ff48 bytes 00013fd6
+ 00530268 bytes 00013fd6
~~~


<a id="compare-b1b624f9ec2c938c6475a4fecb5d0bf1"></a>

### [`0052ff78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md) → [`00530298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530298.md) FUN_00530298

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005302b8",
      "incomplete_value": true,
      "site": "005302bc",
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
      "definition_site": "0052ff98",
      "incomplete_value": true,
      "site": "0052ff9c",
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
      "005302ac",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "005302bc",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "005302ac",
      "READ",
      [
        "storage",
        "00c9bee8",
        null,
        "pointer"
      ]
    ],
    [
      "005302bc",
      "DATA",
      [
        "storage",
        "00c67578",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ff84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md#insn-0052ff84) · [`0052ff8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md#insn-0052ff8c) · [`0052ffac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md#insn-0052ffac)
- 新版 [`005302a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530298.md#insn-005302a4) · [`005302ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530298.md#insn-005302ac) · [`005302cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530298.md#insn-005302cc)

~~~diff
- 0052ff84 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005302a4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0052ff84 bytes 483b00f0
+ 005302a4 bytes 483b00f0
- 0052ff8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 0052ff8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005302ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
+ 005302ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052ff8c bytes 088d47f9
+ 005302ac bytes 087547f9
- 0052ffac ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ffac ["INT_ADD", "register:40f0:8", ["const:52ffac:8", "const:4:8"]]
- 0052ffac ["CALLIND", null, ["register:0:8"]]
+ 005302cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005302cc ["INT_ADD", "register:40f0:8", ["const:5302cc:8", "const:4:8"]]
+ 005302cc ["CALLIND", null, ["register:0:8"]]
- 0052ffac bytes 00013fd6
+ 005302cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f76b622e6fdd47b0d3181ed5bb30847"></a>

### [`00530328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md) → [`00530648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530648.md) FUN_00530648

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005303fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005303fc.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0053071c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/0053071c.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005306c4",
      "incomplete_value": true,
      "site": "005306c8",
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
      "definition_site": "005303a4",
      "incomplete_value": true,
      "site": "005303a8",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530680",
      "incomplete_value": true,
      "site": "00530680",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530360",
      "incomplete_value": true,
      "site": "00530360",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005306ac",
      "incomplete_value": true,
      "site": "005306ac",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053038c",
      "incomplete_value": true,
      "site": "0053038c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530670",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0053069c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005306bc",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00530670",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0053069c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005306bc",
      "READ",
      [
        "storage",
        "00c9bfd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md#insn-00530360) · [`0053038c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md#insn-0053038c) · [`005303c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md#insn-005303c8)
- 新版 [`00530680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530648.md#insn-00530680) · [`005306ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530648.md#insn-005306ac) · [`005306e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530648.md#insn-005306e8)

~~~diff
- 00530360 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530360 ["INT_ADD", "register:40f0:8", ["const:530360:8", "const:4:8"]]
- 00530360 ["CALLIND", null, ["register:0:8"]]
+ 00530680 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530680 ["INT_ADD", "register:40f0:8", ["const:530680:8", "const:4:8"]]
+ 00530680 ["CALLIND", null, ["register:0:8"]]
- 00530360 bytes 20013fd6
+ 00530680 bytes 20013fd6
- 0053038c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053038c ["INT_ADD", "register:40f0:8", ["const:53038c:8", "const:4:8"]]
- 0053038c ["CALLIND", null, ["register:0:8"]]
+ 005306ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 005306ac ["INT_ADD", "register:40f0:8", ["const:5306ac:8", "const:4:8"]]
+ 005306ac ["CALLIND", null, ["register:0:8"]]
- 0053038c bytes 20013fd6
+ 005306ac bytes 20013fd6
- 005303c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005303c8 ["INT_ADD", "register:40f0:8", ["const:5303c8:8", "const:4:8"]]
- 005303c8 ["CALLIND", null, ["register:0:8"]]
+ 005306e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005306e8 ["INT_ADD", "register:40f0:8", ["const:5306e8:8", "const:4:8"]]
+ 005306e8 ["CALLIND", null, ["register:0:8"]]
- 005303c8 bytes 20013fd6
+ 005306e8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9949cf70021253d189e699241ba1de"></a>

### [`005304b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md) → [`005307d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005307d8.md) FUN_005307d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053081c",
      "incomplete_value": true,
      "site": "0053081c",
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
      "definition_site": "005304fc",
      "incomplete_value": true,
      "site": "005304fc",
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
      "00530814",
      "READ",
      [
        "storage",
        "00c9b098",
        null,
        "pointer"
      ]
    ],
    [
      "0053081c",
      "DATA",
      [
        "storage",
        "00c68600",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00530814",
      "READ",
      [
        "storage",
        "00c9c068",
        null,
        "pointer"
      ]
    ],
    [
      "0053081c",
      "DATA",
      [
        "storage",
        "00c695d0",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005304cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md#insn-005304cc) · [`005304e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md#insn-005304e4) · [`005304e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md#insn-005304e8)
- 新版 [`005307ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005307d8.md#insn-005307ec) · [`00530804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005307d8.md#insn-00530804) · [`00530808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005307d8.md#insn-00530808)

~~~diff
- 005304cc ["INT_ADD", "register:40f0:8", ["const:5304cc:8", "const:4:8"]]
- 005304cc ["CALL", null, ["callee:00c58f30:8"]]
+ 005307ec ["INT_ADD", "register:40f0:8", ["const:5307ec:8", "const:4:8"]]
+ 005307ec ["CALL", null, ["callee:00c58f30:8"]]
- 005304cc bytes a59e1c94
+ 005307ec bytes d1a11c94
- 005304e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005304e4 ["INT_ADD", "register:40f0:8", ["const:5304e4:8", "const:4:8"]]
- 005304e4 ["CALLIND", null, ["register:0:8"]]
+ 00530804 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530804 ["INT_ADD", "register:40f0:8", ["const:530804:8", "const:4:8"]]
+ 00530804 ["CALLIND", null, ["register:0:8"]]
- 005304e4 bytes 20013fd6
+ 00530804 bytes 20013fd6
- 005304e8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00530808 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 005304e8 bytes 493b00f0
+ 00530808 bytes 693b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071cd8456572727594e546d1f83a717a"></a>

### [`00530520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md) → [`00530840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530840.md) FUN_00530840

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

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
      "definition_site": "00530878",
      "incomplete_value": false,
      "site": "00530884",
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
            "const:d76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530558",
      "incomplete_value": false,
      "site": "00530564",
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
            "const:c1e:8"
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
      "definition_site": "005308a4",
      "incomplete_value": false,
      "site": "005308ac",
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
      "definition_site": "00530584",
      "incomplete_value": false,
      "site": "0053058c",
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
      "00530878",
      "PARAM",
      [
        "storage",
        "002a8c1e",
        null,
        "string"
      ]
    ],
    [
      "005308a4",
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
      "00530878",
      "PARAM",
      [
        "storage",
        "002a8d76",
        null,
        "string"
      ]
    ],
    [
      "005308a4",
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

- 旧版 [`00530564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md#insn-00530564) · [`0053058c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md#insn-0053058c) · [`00530550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md#insn-00530550)
- 新版 [`00530884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530840.md#insn-00530884) · [`005308ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530840.md#insn-005308ac) · [`00530870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530840.md#insn-00530870)

~~~diff
- 00530564 ["INT_ADD", "register:40f0:8", ["const:530564:8", "const:4:8"]]
- 00530564 ["CALL", null, ["callee:00c59000:8"]]
+ 00530884 ["INT_ADD", "register:40f0:8", ["const:530884:8", "const:4:8"]]
+ 00530884 ["CALL", null, ["callee:00c59000:8"]]
- 00530564 bytes b39e1c94
+ 00530884 bytes dfa11c94
- 0053058c ["INT_ADD", "register:40f0:8", ["const:53058c:8", "const:4:8"]]
- 0053058c ["CALL", null, ["callee:00c59010:8"]]
+ 005308ac ["INT_ADD", "register:40f0:8", ["const:5308ac:8", "const:4:8"]]
+ 005308ac ["CALL", null, ["callee:00c59010:8"]]
- 0053058c bytes ad9e1c94
+ 005308ac bytes d9a11c94
- 00530550 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530550 ["INT_ADD", "register:40f0:8", ["const:530550:8", "const:4:8"]]
- 00530550 ["CALLIND", null, ["register:0:8"]]
+ 00530870 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530870 ["INT_ADD", "register:40f0:8", ["const:530870:8", "const:4:8"]]
+ 00530870 ["CALLIND", null, ["register:0:8"]]
- 00530550 bytes 20013fd6
+ 00530870 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8bda3e6da5cb861cbc607775cd70f7b"></a>

### [`005306a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md) → [`005309c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005309c4.md) FUN_005309c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005309e8",
      "incomplete_value": true,
      "site": "005309ec",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005306c8",
      "incomplete_value": true,
      "site": "005306cc",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530a0c",
      "incomplete_value": true,
      "site": "00530a0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005306ec",
      "incomplete_value": true,
      "site": "005306ec",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530a38",
      "incomplete_value": true,
      "site": "00530a38",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530718",
      "incomplete_value": true,
      "site": "00530718",
      "value": [
        "LOAD",
        "8",
        [
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
      "005309e0",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "005309ec",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005309fc",
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
      "005309e0",
      "READ",
      [
        "storage",
        "00c9c078",
        null,
        "pointer"
      ]
    ],
    [
      "005309ec",
      "DATA",
      [
        "storage",
        "00c68148",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005309fc",
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

- 旧版 [`005306ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md#insn-005306ec) · [`00530718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md#insn-00530718) · [`005306b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md#insn-005306b4)
- 新版 [`00530a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005309c4.md#insn-00530a0c) · [`00530a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005309c4.md#insn-00530a38) · [`005309d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/005309c4.md#insn-005309d4)

~~~diff
- 005306ec ["COPY", "register:0:8", ["register:4048:8"]]
- 005306ec ["INT_ADD", "register:40f0:8", ["const:5306ec:8", "const:4:8"]]
- 005306ec ["CALLIND", null, ["register:0:8"]]
+ 00530a0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530a0c ["INT_ADD", "register:40f0:8", ["const:530a0c:8", "const:4:8"]]
+ 00530a0c ["CALLIND", null, ["register:0:8"]]
- 005306ec bytes 20013fd6
+ 00530a0c bytes 20013fd6
- 00530718 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530718 ["INT_ADD", "register:40f0:8", ["const:530718:8", "const:4:8"]]
- 00530718 ["CALLIND", null, ["register:0:8"]]
+ 00530a38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530a38 ["INT_ADD", "register:40f0:8", ["const:530a38:8", "const:4:8"]]
+ 00530a38 ["CALLIND", null, ["register:0:8"]]
- 00530718 bytes 20013fd6
+ 00530a38 bytes 20013fd6
- 005306b4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005309d4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005306b4 bytes 483b00f0
+ 005309d4 bytes 683b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-053a1fb589f7f61fb3d3d2c373c2153c"></a>

### [`00530748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md) → [`00530a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530a68.md) FUN_00530a68

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530a8c",
      "incomplete_value": true,
      "site": "00530a90",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053076c",
      "incomplete_value": true,
      "site": "00530770",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530ab0",
      "incomplete_value": true,
      "site": "00530ab0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530790",
      "incomplete_value": true,
      "site": "00530790",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530adc",
      "incomplete_value": true,
      "site": "00530adc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005307bc",
      "incomplete_value": true,
      "site": "005307bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530a84",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "00530a90",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530aa0",
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
      "00530a84",
      "READ",
      [
        "storage",
        "00c9c078",
        null,
        "pointer"
      ]
    ],
    [
      "00530a90",
      "DATA",
      [
        "storage",
        "00c68148",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530aa0",
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

- 旧版 [`00530790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md#insn-00530790) · [`005307bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md#insn-005307bc) · [`00530758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md#insn-00530758)
- 新版 [`00530ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530a68.md#insn-00530ab0) · [`00530adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530a68.md#insn-00530adc) · [`00530a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530a68.md#insn-00530a78)

~~~diff
- 00530790 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530790 ["INT_ADD", "register:40f0:8", ["const:530790:8", "const:4:8"]]
- 00530790 ["CALLIND", null, ["register:0:8"]]
+ 00530ab0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530ab0 ["INT_ADD", "register:40f0:8", ["const:530ab0:8", "const:4:8"]]
+ 00530ab0 ["CALLIND", null, ["register:0:8"]]
- 00530790 bytes 20013fd6
+ 00530ab0 bytes 20013fd6
- 005307bc ["COPY", "register:0:8", ["register:4048:8"]]
- 005307bc ["INT_ADD", "register:40f0:8", ["const:5307bc:8", "const:4:8"]]
- 005307bc ["CALLIND", null, ["register:0:8"]]
+ 00530adc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530adc ["INT_ADD", "register:40f0:8", ["const:530adc:8", "const:4:8"]]
+ 00530adc ["CALLIND", null, ["register:0:8"]]
- 005307bc bytes 20013fd6
+ 00530adc bytes 20013fd6
- 00530758 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00530a78 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00530758 bytes 483b00f0
+ 00530a78 bytes 683b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb784c0c734b44f898015b07808013ff"></a>

### [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) → [`00530b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md) FUN_00530b2c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004c7c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7c64.md) [`004c7ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md) [`005308f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005308f8.md) [`00530984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530984.md) [`0053098c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053098c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 6件 [`004c7f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7f84.md) [`004c7fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c7/004c7fc0.md) [`00530c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530c18.md) [`00530ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530ca4.md) [`00530cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cac.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530b64",
      "incomplete_value": true,
      "site": "00530b68",
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
      "definition_site": "00530844",
      "incomplete_value": true,
      "site": "00530848",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530b98",
      "incomplete_value": true,
      "site": "00530b98",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "00530878",
      "incomplete_value": true,
      "site": "00530878",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530bec",
      "incomplete_value": true,
      "site": "00530bec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "definition_site": "005308cc",
      "incomplete_value": true,
      "site": "005308cc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
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
      "00530b58",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00530b68",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00530b88",
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
      "00530b58",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "00530b68",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00530b88",
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

- 旧版 [`00530878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md#insn-00530878) · [`005308cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md#insn-005308cc) · [`00530828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md#insn-00530828)
- 新版 [`00530b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md#insn-00530b98) · [`00530bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md#insn-00530bec) · [`00530b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530b2c.md#insn-00530b48)

~~~diff
- 00530878 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530878 ["INT_ADD", "register:40f0:8", ["const:530878:8", "const:4:8"]]
- 00530878 ["CALLIND", null, ["register:0:8"]]
+ 00530b98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b98 ["INT_ADD", "register:40f0:8", ["const:530b98:8", "const:4:8"]]
+ 00530b98 ["CALLIND", null, ["register:0:8"]]
- 00530878 bytes 20013fd6
+ 00530b98 bytes 20013fd6
- 005308cc ["COPY", "register:0:8", ["register:4048:8"]]
- 005308cc ["INT_ADD", "register:40f0:8", ["const:5308cc:8", "const:4:8"]]
- 005308cc ["CALLIND", null, ["register:0:8"]]
+ 00530bec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530bec ["INT_ADD", "register:40f0:8", ["const:530bec:8", "const:4:8"]]
+ 00530bec ["CALLIND", null, ["register:0:8"]]
- 005308cc bytes 20013fd6
+ 00530bec bytes 20013fd6
- 00530828 ["COPY", "register:40b0:8", ["const:c67000:8"]]
+ 00530b48 ["COPY", "register:40b0:8", ["const:c68000:8"]]
- 00530828 bytes b63900f0
+ 00530b48 bytes d6390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-696ee6baec8be4adee3ebee937416ad5"></a>

### [`005309b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md) → [`00530cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cd4.md) FUN_00530cd4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00530a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530a88.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00530da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530da8.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530d50",
      "incomplete_value": true,
      "site": "00530d54",
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
      "definition_site": "00530a30",
      "incomplete_value": true,
      "site": "00530a34",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530d0c",
      "incomplete_value": true,
      "site": "00530d0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005309ec",
      "incomplete_value": true,
      "site": "005309ec",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530d38",
      "incomplete_value": true,
      "site": "00530d38",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530a18",
      "incomplete_value": true,
      "site": "00530a18",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530cfc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530d28",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530d48",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00530cfc",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00530d28",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00530d48",
      "READ",
      [
        "storage",
        "00c9bfd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005309ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md#insn-005309ec) · [`00530a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md#insn-00530a18) · [`00530a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md#insn-00530a54)
- 新版 [`00530d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cd4.md#insn-00530d0c) · [`00530d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cd4.md#insn-00530d38) · [`00530d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530cd4.md#insn-00530d74)

~~~diff
- 005309ec ["COPY", "register:0:8", ["register:4048:8"]]
- 005309ec ["INT_ADD", "register:40f0:8", ["const:5309ec:8", "const:4:8"]]
- 005309ec ["CALLIND", null, ["register:0:8"]]
+ 00530d0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d0c ["INT_ADD", "register:40f0:8", ["const:530d0c:8", "const:4:8"]]
+ 00530d0c ["CALLIND", null, ["register:0:8"]]
- 005309ec bytes 20013fd6
+ 00530d0c bytes 20013fd6
- 00530a18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530a18 ["INT_ADD", "register:40f0:8", ["const:530a18:8", "const:4:8"]]
- 00530a18 ["CALLIND", null, ["register:0:8"]]
+ 00530d38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d38 ["INT_ADD", "register:40f0:8", ["const:530d38:8", "const:4:8"]]
+ 00530d38 ["CALLIND", null, ["register:0:8"]]
- 00530a18 bytes 20013fd6
+ 00530d38 bytes 20013fd6
- 00530a54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530a54 ["INT_ADD", "register:40f0:8", ["const:530a54:8", "const:4:8"]]
- 00530a54 ["CALLIND", null, ["register:0:8"]]
+ 00530d74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d74 ["INT_ADD", "register:40f0:8", ["const:530d74:8", "const:4:8"]]
+ 00530d74 ["CALLIND", null, ["register:0:8"]]
- 00530a54 bytes 20013fd6
+ 00530d74 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6dc02bcb96a09412086719736a8ef7"></a>

### [`00530b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md) → [`00530e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530e34.md) FUN_00530e34

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530e84",
      "incomplete_value": true,
      "site": "00530e88",
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
      "definition_site": "00530b64",
      "incomplete_value": true,
      "site": "00530b68",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530e6c",
      "incomplete_value": true,
      "site": "00530e6c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530b4c",
      "incomplete_value": true,
      "site": "00530b4c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530ea8",
      "incomplete_value": true,
      "site": "00530ea8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530b88",
      "incomplete_value": true,
      "site": "00530b88",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530e5c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530e7c",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00530e88",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530e5c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00530e7c",
      "READ",
      [
        "storage",
        "00c9bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "00530e88",
      "DATA",
      [
        "storage",
        "00c67d78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md#insn-00530b4c) · [`00530b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md#insn-00530b88) · [`00530b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md#insn-00530b2c)
- 新版 [`00530e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530e34.md#insn-00530e6c) · [`00530ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530e34.md#insn-00530ea8) · [`00530e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530e34.md#insn-00530e4c)

~~~diff
- 00530b4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00530b4c ["INT_ADD", "register:40f0:8", ["const:530b4c:8", "const:4:8"]]
- 00530b4c ["CALLIND", null, ["register:0:8"]]
+ 00530e6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530e6c ["INT_ADD", "register:40f0:8", ["const:530e6c:8", "const:4:8"]]
+ 00530e6c ["CALLIND", null, ["register:0:8"]]
- 00530b4c bytes 20013fd6
+ 00530e6c bytes 20013fd6
- 00530b88 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530b88 ["INT_ADD", "register:40f0:8", ["const:530b88:8", "const:4:8"]]
- 00530b88 ["CALLIND", null, ["register:0:8"]]
+ 00530ea8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530ea8 ["INT_ADD", "register:40f0:8", ["const:530ea8:8", "const:4:8"]]
+ 00530ea8 ["CALLIND", null, ["register:0:8"]]
- 00530b88 bytes 20013fd6
+ 00530ea8 bytes 20013fd6
- 00530b2c ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00530e4c ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00530b2c bytes b53900f0
+ 00530e4c bytes d5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fe6bbc042ce44dde54287d48d471d34"></a>

### [`00530bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md) → [`00530ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530ed8.md) FUN_00530ed8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530f28",
      "incomplete_value": true,
      "site": "00530f2c",
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
      "definition_site": "00530c08",
      "incomplete_value": true,
      "site": "00530c0c",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00530f10",
      "incomplete_value": true,
      "site": "00530f10",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530bf0",
      "incomplete_value": true,
      "site": "00530bf0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530f4c",
      "incomplete_value": true,
      "site": "00530f4c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530c2c",
      "incomplete_value": true,
      "site": "00530c2c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00530f00",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530f20",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00530f2c",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530f00",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00530f20",
      "READ",
      [
        "storage",
        "00c9bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "00530f2c",
      "DATA",
      [
        "storage",
        "00c67d78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md#insn-00530bf0) · [`00530c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md#insn-00530c2c) · [`00530bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md#insn-00530bd0)
- 新版 [`00530f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530ed8.md#insn-00530f10) · [`00530f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530ed8.md#insn-00530f4c) · [`00530ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530ed8.md#insn-00530ef0)

~~~diff
- 00530bf0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530bf0 ["INT_ADD", "register:40f0:8", ["const:530bf0:8", "const:4:8"]]
- 00530bf0 ["CALLIND", null, ["register:0:8"]]
+ 00530f10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530f10 ["INT_ADD", "register:40f0:8", ["const:530f10:8", "const:4:8"]]
+ 00530f10 ["CALLIND", null, ["register:0:8"]]
- 00530bf0 bytes 20013fd6
+ 00530f10 bytes 20013fd6
- 00530c2c ["COPY", "register:0:8", ["register:4048:8"]]
- 00530c2c ["INT_ADD", "register:40f0:8", ["const:530c2c:8", "const:4:8"]]
- 00530c2c ["CALLIND", null, ["register:0:8"]]
+ 00530f4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530f4c ["INT_ADD", "register:40f0:8", ["const:530f4c:8", "const:4:8"]]
+ 00530f4c ["CALLIND", null, ["register:0:8"]]
- 00530c2c bytes 20013fd6
+ 00530f4c bytes 20013fd6
- 00530bd0 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00530ef0 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00530bd0 bytes b53900f0
+ 00530ef0 bytes d5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd2304ad3192b7cd26a13c65c6896e4"></a>

### [`00530cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md) → [`00530fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530fdc.md) FUN_00530fdc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053102c",
      "incomplete_value": true,
      "site": "00531030",
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
      "definition_site": "00530d0c",
      "incomplete_value": true,
      "site": "00530d10",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00531014",
      "incomplete_value": true,
      "site": "00531014",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530cf4",
      "incomplete_value": true,
      "site": "00530cf4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00531050",
      "incomplete_value": true,
      "site": "00531050",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530d30",
      "incomplete_value": true,
      "site": "00530d30",
      "value": [
        "LOAD",
        "8",
        [
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
      "00531004",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00531024",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00531030",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00531004",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00531024",
      "READ",
      [
        "storage",
        "00c9bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "00531030",
      "DATA",
      [
        "storage",
        "00c67d78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md#insn-00530cf4) · [`00530d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md#insn-00530d30) · [`00530cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md#insn-00530cd4)
- 新版 [`00531014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530fdc.md#insn-00531014) · [`00531050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530fdc.md#insn-00531050) · [`00530ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00530/00530fdc.md#insn-00530ff4)

~~~diff
- 00530cf4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530cf4 ["INT_ADD", "register:40f0:8", ["const:530cf4:8", "const:4:8"]]
- 00530cf4 ["CALLIND", null, ["register:0:8"]]
+ 00531014 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00531014 ["INT_ADD", "register:40f0:8", ["const:531014:8", "const:4:8"]]
+ 00531014 ["CALLIND", null, ["register:0:8"]]
- 00530cf4 bytes 20013fd6
+ 00531014 bytes 20013fd6
- 00530d30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530d30 ["INT_ADD", "register:40f0:8", ["const:530d30:8", "const:4:8"]]
- 00530d30 ["CALLIND", null, ["register:0:8"]]
+ 00531050 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00531050 ["INT_ADD", "register:40f0:8", ["const:531050:8", "const:4:8"]]
+ 00531050 ["CALLIND", null, ["register:0:8"]]
- 00530d30 bytes 20013fd6
+ 00531050 bytes 20013fd6
- 00530cd4 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00530ff4 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00530cd4 bytes b53900f0
+ 00530ff4 bytes d5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ffeab1884e72b8d936cd2add9215a0f"></a>

### [`00530d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md) → [`00531080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531080.md) FUN_00531080

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005310d0",
      "incomplete_value": true,
      "site": "005310d4",
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
      "definition_site": "00530db0",
      "incomplete_value": true,
      "site": "00530db4",
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
    "kind": "call_target",
    "new": {
      "definition_site": "005310b8",
      "incomplete_value": true,
      "site": "005310b8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530d98",
      "incomplete_value": true,
      "site": "00530d98",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005310f4",
      "incomplete_value": true,
      "site": "005310f4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00530dd4",
      "incomplete_value": true,
      "site": "00530dd4",
      "value": [
        "LOAD",
        "8",
        [
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
      "005310a8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005310c8",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "005310d4",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "005310a8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005310c8",
      "READ",
      [
        "storage",
        "00c9bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "005310d4",
      "DATA",
      [
        "storage",
        "00c67d78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md#insn-00530d98) · [`00530dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md#insn-00530dd4) · [`00530d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530d60.md#insn-00530d78)
- 新版 [`005310b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531080.md#insn-005310b8) · [`005310f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531080.md#insn-005310f4) · [`00531098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531080.md#insn-00531098)

~~~diff
- 00530d98 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530d98 ["INT_ADD", "register:40f0:8", ["const:530d98:8", "const:4:8"]]
- 00530d98 ["CALLIND", null, ["register:0:8"]]
+ 005310b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005310b8 ["INT_ADD", "register:40f0:8", ["const:5310b8:8", "const:4:8"]]
+ 005310b8 ["CALLIND", null, ["register:0:8"]]
- 00530d98 bytes 20013fd6
+ 005310b8 bytes 20013fd6
- 00530dd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530dd4 ["INT_ADD", "register:40f0:8", ["const:530dd4:8", "const:4:8"]]
- 00530dd4 ["CALLIND", null, ["register:0:8"]]
+ 005310f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005310f4 ["INT_ADD", "register:40f0:8", ["const:5310f4:8", "const:4:8"]]
+ 005310f4 ["CALLIND", null, ["register:0:8"]]
- 00530dd4 bytes 20013fd6
+ 005310f4 bytes 20013fd6
- 00530d78 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00531098 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00530d78 bytes b53900f0
+ 00531098 bytes b53900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912ac7825f5f7422e933396c5bcf97de"></a>

### [`00530eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md) → [`0053120c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053120c.md) FUN_0053120c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531244",
      "incomplete_value": true,
      "site": "00531244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530f24",
      "incomplete_value": true,
      "site": "00530f24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f7:8"
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
      "00531234",
      "READ",
      [
        "storage",
        "002b72f7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531234",
      "READ",
      [
        "storage",
        "002b73c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md#insn-00530f08) · [`00530f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md#insn-00530f30) · [`00530f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530eec.md#insn-00530f40)
- 新版 [`00531228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053120c.md#insn-00531228) · [`00531250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053120c.md#insn-00531250) · [`00531260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053120c.md#insn-00531260)

~~~diff
- 00530f08 ["COPY", "tmp:0:8", ["const:2f7:8"]]
- 00530f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00530f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00530f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531228 ["COPY", "tmp:0:8", ["const:3c6:8"]]
+ 00531228 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531228 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531228 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00530f08 bytes 29dd0b91
+ 00531228 bytes 29190f91
- 00530f30 ["INT_ADD", "register:40f0:8", ["const:530f30:8", "const:4:8"]]
- 00530f30 ["CALL", null, ["callee:00c59730:8"]]
+ 00531250 ["INT_ADD", "register:40f0:8", ["const:531250:8", "const:4:8"]]
+ 00531250 ["CALL", null, ["callee:00c59730:8"]]
- 00530f30 bytes 0c9e1c94
+ 00531250 bytes 38a11c94
- 00530f40 ["INT_ADD", "register:40f0:8", ["const:530f40:8", "const:4:8"]]
- 00530f40 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531260 ["INT_ADD", "register:40f0:8", ["const:531260:8", "const:4:8"]]
+ 00531260 ["CALL", null, ["callee:00c58f50:8"]]
- 00530f40 bytes 109c1c94
+ 00531260 bytes 3c9f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d76d81c8d0bf2f3d793e58785c74fd40"></a>

### [`0053102c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md) → [`0053134c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053134c.md) FUN_0053134c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531384",
      "incomplete_value": true,
      "site": "00531384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531064",
      "incomplete_value": true,
      "site": "00531064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:781:8"
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
      "00531374",
      "READ",
      [
        "storage",
        "002ae781",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531374",
      "READ",
      [
        "storage",
        "002ae84e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md#insn-00531048) · [`00531070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md#insn-00531070) · [`00531080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053102c.md#insn-00531080)
- 新版 [`00531368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053134c.md#insn-00531368) · [`00531390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053134c.md#insn-00531390) · [`005313a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053134c.md#insn-005313a0)

~~~diff
- 00531048 ["COPY", "tmp:0:8", ["const:781:8"]]
- 00531048 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531048 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531048 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531368 ["COPY", "tmp:0:8", ["const:84e:8"]]
+ 00531368 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531368 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531368 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531048 bytes 29051e91
+ 00531368 bytes 29392191
- 00531070 ["INT_ADD", "register:40f0:8", ["const:531070:8", "const:4:8"]]
- 00531070 ["CALL", null, ["callee:00c59730:8"]]
+ 00531390 ["INT_ADD", "register:40f0:8", ["const:531390:8", "const:4:8"]]
+ 00531390 ["CALL", null, ["callee:00c59730:8"]]
- 00531070 bytes bc9d1c94
+ 00531390 bytes e8a01c94
- 00531080 ["INT_ADD", "register:40f0:8", ["const:531080:8", "const:4:8"]]
- 00531080 ["CALL", null, ["callee:00c58f50:8"]]
+ 005313a0 ["INT_ADD", "register:40f0:8", ["const:5313a0:8", "const:4:8"]]
+ 005313a0 ["CALL", null, ["callee:00c58f50:8"]]
- 00531080 bytes c09b1c94
+ 005313a0 bytes ec9e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52aecb3085086fdbf56e4ca93fe6b48d"></a>

### [`005310d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005310d4.md) → [`005313f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005313f4.md) FUN_005313f4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00531410",
      "incomplete_value": true,
      "site": "00531410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005310f0",
      "incomplete_value": true,
      "site": "005310f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b89:8"
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
      "definition_site": "00531408",
      "incomplete_value": true,
      "site": "00531414",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005310e8",
      "incomplete_value": true,
      "site": "005310f4",
      "value": [
        "LOAD",
        "8",
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
      "00531400",
      "READ",
      [
        "storage",
        "002a9b89",
        null,
        "string"
      ]
    ],
    [
      "00531408",
      "READ",
      [
        "storage",
        "002a9b90",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531400",
      "READ",
      [
        "storage",
        "002a9c56",
        null,
        "string"
      ]
    ],
    [
      "00531408",
      "READ",
      [
        "storage",
        "002a9c5d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005310dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/005310d4.md#insn-005310dc)
- 新版 [`005313fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005313f4.md#insn-005313fc)

~~~diff
- 005310dc ["COPY", "tmp:0:8", ["const:b89:8"]]
- 005310dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005310dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005310dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005313fc ["COPY", "tmp:0:8", ["const:c56:8"]]
+ 005313fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005313fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005313fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005310dc bytes 4a252e91
+ 005313fc bytes 4a593191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5a7caa108096e563c77e6bc35a7d5e9"></a>

### [`0053114c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md) → [`0053146c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053146c.md) FUN_0053146c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005314a4",
      "incomplete_value": true,
      "site": "005314a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531184",
      "incomplete_value": true,
      "site": "00531184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3c:8"
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
      "00531494",
      "READ",
      [
        "storage",
        "002b4d3c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531494",
      "READ",
      [
        "storage",
        "002b4e1a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md#insn-00531168) · [`00531190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md#insn-00531190) · [`005311a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053114c.md#insn-005311a0)
- 新版 [`00531488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053146c.md#insn-00531488) · [`005314b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053146c.md#insn-005314b0) · [`005314c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053146c.md#insn-005314c0)

~~~diff
- 00531168 ["COPY", "tmp:0:8", ["const:d3c:8"]]
- 00531168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531488 ["COPY", "tmp:0:8", ["const:e1a:8"]]
+ 00531488 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531488 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531488 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531168 bytes 29f13491
+ 00531488 bytes 29693891
- 00531190 ["INT_ADD", "register:40f0:8", ["const:531190:8", "const:4:8"]]
- 00531190 ["CALL", null, ["callee:00c59730:8"]]
+ 005314b0 ["INT_ADD", "register:40f0:8", ["const:5314b0:8", "const:4:8"]]
+ 005314b0 ["CALL", null, ["callee:00c59730:8"]]
- 00531190 bytes 749d1c94
+ 005314b0 bytes a0a01c94
- 005311a0 ["INT_ADD", "register:40f0:8", ["const:5311a0:8", "const:4:8"]]
- 005311a0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005314c0 ["INT_ADD", "register:40f0:8", ["const:5314c0:8", "const:4:8"]]
+ 005314c0 ["CALL", null, ["callee:00c58f50:8"]]
- 005311a0 bytes 789b1c94
+ 005314c0 bytes a49e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

